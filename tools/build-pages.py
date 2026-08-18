#!/usr/bin/env python3
"""
Собрать две страницы из одного источника: английскую в /index.html и русскую
в /ru/index.html.

Зачем. Раньше язык переключался скриптом на одном адресе. Поиску это отдаёт
один документ: русская версия не могла ранжироваться в принципе, а title,
description и Open Graph не переводились вовсе — движок обходил только тело
страницы. Два адреса это чинят и попутно снимают вспышку чужого языка при
загрузке и двойную загрузку скриншотов.

Источник — src/page.html: обычная английская страница со словарём внутри.
Скрипт вынимает словарь, подставляет строки и пишет оба файла.

Запуск:  python3 tools/build-pages.py
После:   node tools/update-csp.js index.html && node tools/update-csp.js ru/index.html
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src", "page.html")
SITE = "https://www.morphtrack.app"

# Шапка документа переводится отдельно: в ней нет элементов с ключами.
HEAD_RU = {
    "title": "MorphTrack — личная лента фото и ИИ-разбор изменений",
    "description": (
        "Снимай фото прогресса и отмечай рутину. ИИ сравнивает снимки за период, "
        "описывает, что изменилось, и показывает, какие привычки совпали с "
        "изменениями. Фото хранятся в ЕС, без рекламы и трекинга."
    ),
    "og:title": "MorphTrack — увидь, что на самом деле изменилось",
    "og:description": (
        "Фото прогресса, отметки рутины и ИИ-разбор: что изменилось зона за зоной "
        "и какие привычки шли рядом. Фото хранятся в ЕС."
    ),
    "og:locale": "ru_RU",
}

FAQ_RU_ORDER = ["faq1", "faq2", "faq3", "faq4", "faq5"]


def read_source():
    if not os.path.exists(SRC):
        sys.exit(f"нет источника: {SRC}")
    return open(SRC, encoding="utf-8").read()


def extract_dict(html):
    m = re.search(r"var I18N = \{ ru: \{(.*?)\n  \} \};", html, re.S)
    if not m:
        sys.exit("словарь не найден")
    body = "{" + m.group(1) + "}"
    return json.loads(body)


def strip_i18n_script(html):
    """Убрать скрипт переключения целиком — на статических страницах он не нужен.

    Ищем по <script>…</script>, внутри которого объявлен словарь: полагаться на
    точную форму отступов нельзя, её меняет любая правка.
    """
    out, removed = [], 0
    for block in re.split(r"(?s)(<script\b[^>]*>.*?</script>)", html):
        if block.startswith("<script") and "var I18N" in block:
            removed += 1
            continue
        out.append(block)
    if removed != 1:
        sys.exit(f"ожидался один скрипт со словарём, найдено {removed}")
    return "".join(out).replace("\n\n\n", "\n\n")


def swap_toggle(html, lang):
    """Кнопки -> ссылки между двумя адресами."""
    en_cls = ' class="lang-btn is-on"' if lang == "en" else ' class="lang-btn"'
    ru_cls = ' class="lang-btn is-on"' if lang == "ru" else ' class="lang-btn"'
    new = (
        '<div class="lang" role="group" aria-label="Language">'
        f'<a{en_cls} href="/" hreflang="en"{" aria-current=\"page\"" if lang == "en" else ""}>EN</a>'
        f'<a{ru_cls} href="/ru/" hreflang="ru"{" aria-current=\"page\"" if lang == "ru" else ""}>RU</a>'
        "</div>"
    )
    return re.sub(r'<div class="lang".*?</div>', new, html, count=1, flags=re.S)


def apply_ru(html, ru):
    """Подставить русские строки в тело страницы."""
    missing = []

    def text(m):
        key = m.group(1)
        if key not in ru:
            missing.append(key)
            return m.group(0)
        return m.group(0)[: m.end(2) - m.start(0)] + ru[key] + m.group(4)

    # содержимое элементов с ключами
    pat = re.compile(
        r'(?s)(<(?:p|h1|h2|h3|span|small|li|cite|a|b|em)\b[^>]*\bdata-i18n="([a-z0-9_]+)"[^>]*>)(.*?)(</(?:p|h1|h2|h3|span|small|li|cite|a|b|em)>)'
    )

    def repl(m):
        open_tag, key, _old, close_tag = m.group(1), m.group(2), m.group(3), m.group(4)
        if key not in ru:
            missing.append(key)
            return m.group(0)
        return open_tag + ru[key] + close_tag

    html = pat.sub(repl, html)

    # картинки: русский вариант становится основным
    html = re.sub(
        r'src="(/img/[^"]+)" data-i18n-src="([^"]+)"',
        lambda m: f'src="{m.group(2)}"',
        html,
    )
    # ссылки на юридические страницы
    html = re.sub(
        r'href="(v2/[^"]+)" data-i18n-href="([^"]+)"',
        lambda m: f'href="/{m.group(2)}"',
        html,
    )
    return html, missing


def clean_en(html):
    """Убрать из английской версии служебные атрибуты второй версии."""
    html = re.sub(r' data-i18n-src="[^"]*"', "", html)
    html = re.sub(r' data-i18n-href="[^"]*"', "", html)
    html = re.sub(r' data-i18n="[a-z0-9_]+"', "", html)
    html = re.sub(r'href="(v2/[^"]+)"', lambda m: f'href="/{m.group(1)}"', html)
    return html


def clean_ru_attrs(html):
    html = re.sub(r' data-i18n-src="[^"]*"', "", html)
    html = re.sub(r' data-i18n-href="[^"]*"', "", html)
    html = re.sub(r' data-i18n="[a-z0-9_]+"', "", html)
    return html


def set_head(html, lang, ru):
    canon = f"{SITE}/" if lang == "en" else f"{SITE}/ru/"
    alt_en, alt_ru = f"{SITE}/", f"{SITE}/ru/"

    html = html.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{canon}">', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{canon}">', html, count=1)

    if lang == "ru":
        html = re.sub(r"<title>.*?</title>", f"<title>{HEAD_RU['title']}</title>", html, count=1, flags=re.S)
        html = re.sub(r'<meta name="description" content="[^"]*">',
                      f'<meta name="description" content="{HEAD_RU["description"]}">', html, count=1)
        html = re.sub(r'<meta property="og:title" content="[^"]*">',
                      f'<meta property="og:title" content="{HEAD_RU["og:title"]}">', html, count=1)
        html = re.sub(r'<meta property="og:description" content="[^"]*">',
                      f'<meta property="og:description" content="{HEAD_RU["og:description"]}">', html, count=1)
        html = re.sub(r'<meta property="og:locale" content="[^"]*">',
                      f'<meta property="og:locale" content="{HEAD_RU["og:locale"]}">', html, count=1)
        html = re.sub(r'<meta name="twitter:title" content="[^"]*">',
                      f'<meta name="twitter:title" content="{HEAD_RU["og:title"]}">', html, count=1)
        html = re.sub(r'<meta name="twitter:description" content="[^"]*">',
                      f'<meta name="twitter:description" content="{HEAD_RU["og:description"]}">', html, count=1)
        # структурированные данные: вопросы и ответы на языке страницы
        def faq_ru(m):
            data = json.loads(m.group(0)[len('<script type="application/ld+json">'):-len("</script>")])
            for i, k in enumerate(FAQ_RU_ORDER):
                q = re.sub(r"<[^>]+>", "", ru[k + "_q"])
                a = re.sub(r"<[^>]+>", "", ru[k + "_a"])
                data["mainEntity"][i]["name"] = q
                data["mainEntity"][i]["acceptedAnswer"]["text"] = a
            data["inLanguage"] = "ru"
            return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"
        html = re.sub(r'<script type="application/ld\+json">\{"@context"[^\n]*"FAQPage".*?</script>',
                      faq_ru, html, count=1, flags=re.S)

    # обе версии указывают друг на друга
    hreflang = (f'\n<link rel="alternate" hreflang="en" href="{alt_en}">'
                f'\n<link rel="alternate" hreflang="ru" href="{alt_ru}">'
                f'\n<link rel="alternate" hreflang="x-default" href="{alt_en}">')
    html = html.replace(f'<link rel="canonical" href="{canon}">',
                        f'<link rel="canonical" href="{canon}">{hreflang}', 1)
    return html


def main():
    src = read_source()
    ru = extract_dict(src)

    base = strip_i18n_script(src)

    en = clean_en(swap_toggle(base, "en"))
    en = set_head(en, "en", ru)

    ru_html, missing = apply_ru(base, ru)
    ru_html = clean_ru_attrs(swap_toggle(ru_html, "ru"))
    ru_html = set_head(ru_html, "ru", ru)

    if missing:
        sys.exit(f"нет перевода для ключей: {sorted(set(missing))}")

    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(en)
    os.makedirs(os.path.join(ROOT, "ru"), exist_ok=True)
    open(os.path.join(ROOT, "ru", "index.html"), "w", encoding="utf-8").write(ru_html)

    print(f"index.html     {len(en)//1024} КБ")
    print(f"ru/index.html  {len(ru_html)//1024} КБ")
    print(f"ключей в словаре: {len(ru)}")


if __name__ == "__main__":
    main()
