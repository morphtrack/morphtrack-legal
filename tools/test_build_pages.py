#!/usr/bin/env python3
"""Проверки сборщика страниц.

Ловят один конкретный класс поломки: элемент с data-i18n, внутри которого есть
вложенный тег. На таких девяти элементах старая регулярка обрывалась на `</em>`
или `</a>` и оставляла английский хвост на русской странице.

Запуск:  python3 tools/test_build_pages.py
"""
import importlib.util
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    "build_pages", os.path.join(ROOT, "tools", "build-pages.py")
)
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

failures = []


def check(name, cond, detail=""):
    if cond:
        print(f"  OK   {name}")
    else:
        print(f"  ПАДЁТ {name}  {detail}")
        failures.append(name)


print("apply_ru на вложенных тегах:")

# Ровно та форма, на которой ломался pr_h2.
src = '<h2 data-i18n="k">Photos of your face deserve <em class="ser">real</em> rules.</h2>'
got, missing = bp.apply_ru(src, {"k": 'Фотографии заслуживают <em class="ser">настоящих</em> правил.'})
check(
    "вложенный <em> не обрывает элемент",
    got == '<h2 data-i18n="k">Фотографии заслуживают <em class="ser">настоящих</em> правил.</h2>',
    f"получено: {got}",
)
check("английский хвост не остался", "rules." not in got, f"получено: {got}")

# faq_ask: внутри <a>, а не <em>.
src = '<p data-i18n="k">Write to <a href="mailto:x@y.z">x@y.z</a> — a person answers.</p>'
got, _ = bp.apply_ru(src, {"k": 'Напиши на <a href="mailto:x@y.z">x@y.z</a> — ответит человек.'})
check("вложенный <a> не обрывает элемент", "a person answers" not in got, f"получено: {got}")

# Элемент без вложенности не должен пострадать.
src = '<p data-i18n="k">Plain text.</p>'
got, _ = bp.apply_ru(src, {"k": "Простой текст."})
check("простой элемент цел", got == '<p data-i18n="k">Простой текст.</p>', f"получено: {got}")

# Отсутствующий ключ по-прежнему попадает в missing, а текст не трогается.
src = '<p data-i18n="nope">Keep me.</p>'
got, missing = bp.apply_ru(src, {})
check("пропавший ключ отмечен", missing == ["nope"] and "Keep me." in got, f"{missing} / {got}")

# Два элемента подряд — второй не должен съесть закрывающий тег первого.
src = '<p data-i18n="a">One <em>x</em>.</p><p data-i18n="b">Two.</p>'
got, _ = bp.apply_ru(src, {"a": "Раз.", "b": "Два."})
check("соседние элементы не слипаются", got == '<p data-i18n="a">Раз.</p><p data-i18n="b">Два.</p>', f"получено: {got}")

print("\nсобранная русская страница:")

ru_path = os.path.join(ROOT, "ru", "index.html")
if not os.path.exists(ru_path):
    print("  ПРОПУСК  ru/index.html ещё не собран")
else:
    page = open(ru_path, encoding="utf-8").read()
    body = re.sub(r"(?s)<(script|style)\b.*?</\1>", " ", page)
    text = re.sub(r"<[^>]+>", " ", body)

    # Хвосты, которые оставляла старая регулярка.
    for tail in ("rules.", "the answer.", "a person answers", "before you waste months",
                 "no limits", "side by side", "photo by photo", "free and unlimited",
                 "something of their own"):
        check(f"нет хвоста «{tail}»", tail not in text)

    # Двойная точка от съеденного закрывающего тега.
    check("нет двойных точек", ".." not in re.sub(r"\.\.\.", "", text))

    # Осиротевших закрывающих тегов быть не должно.
    opens = len(re.findall(r"<em\b", body))
    closes = len(re.findall(r"</em>", body))
    check("теги <em> сбалансированы", opens == closes, f"{opens} открывающих против {closes} закрывающих")

print()
if failures:
    print(f"ПРОВАЛЕНО проверок: {len(failures)} — {', '.join(failures)}")
    sys.exit(1)
print("все проверки прошли")
