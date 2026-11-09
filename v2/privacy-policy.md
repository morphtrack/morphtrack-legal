---
title: Privacy Policy
lang: en
---

# Privacy Policy

_Updated: 9 November 2026_

Mobile consent disclosure identifier: **2026-11-04**.

[Русская версия](https://www.morphtrack.app/v2/ru/privacy-policy) · [Health data policy](https://www.morphtrack.app/v2/consumer-health-data) · [Deletion](https://www.morphtrack.app/v2/delete-account)

This clarification describes the separate product-statistics choice, the transitional mode for older versions and account-wide withdrawal, alongside the existing processing, recipients and retention. Publication is not consent. [Previous revision](https://www.morphtrack.app/archive/before-2026-11-05-compatibility/privacy-policy).

This revision clarifies the move of new backup processing to DigitalOcean and the remaining historical GitHub artifacts until their original expiration. Purposes and consent choices are unchanged. [Previous revision](https://www.morphtrack.app/archive/before-2026-11-09-recovery/privacy-policy).

## 1. Who is responsible

**Raisat Ramazanova, an individual developer based in Serbia**, operates MorphTrack (also called Morph). MorphTrack is a trade name, not a separate legal entity. Contact: **[morphtrack.app@gmail.com](mailto:morphtrack.app@gmail.com)**.

This policy covers the app and website. Our separate [Consumer Health Data Privacy Policy](https://www.morphtrack.app/v2/consumer-health-data) explains health-related information.

## 2. Information we handle

- **Account and sign-in:** email, display name, password hash for email sign-in, verification status and sessions. With Apple or Google sign-in, we receive a provider identifier and the name/email it makes available, including an Apple relay address where chosen. We do not receive your Apple or Google password. Linking and token records support sign-in and disconnection.
- **Your journal:** photos and generated image sizes, avatars, photo dates and notes, trackers and goals, capture settings, routine factors and dates. These can reveal health information.
- **Optional profile:** details you provide, such as age, gender, skin type, activity, sleep and smoking habits. You can leave them blank or remove them.
- **AI records:** requested analyses, observations, retained input context and your journal-permission and AI-sharing choices. Where age confirmation is collected, we record it; this is not identity-document verification.
- **Purchases:** store, product, receipt/purchase token, transaction identifiers and entitlement. A pseudonymous account identifier links a purchase to your account. Apple or Google handles payment details; we do not receive your card number.
- **Support:** messages, contact details and information you include.
- **Technical information:** request route, status, timing, account identifiers and error/security events. IP addresses are used for network delivery and abuse prevention and are recorded in API access logs.

**Photo metadata:** uploaded images are re-encoded to remove embedded camera metadata, including GPS tags. We separately retain photo dates and image dimensions for the journal. Re-encoding does not remove information visible in a picture or text you enter.

## 3. Purposes and legal grounds

Account and journal data provide the features you request; purchase records validate subscriptions; support messages let us answer you; limited technical records support operation, security and troubleshooting.

Where GDPR or comparable rules apply, our grounds are performance of the service contract, legitimate interests in security and reliability, legal obligations, and consent for optional processing that requires it. **Health data also requires a separate permitted basis under sensitive-data rules.** Where explicit consent is required, it must cover the relevant purpose and be obtained separately. Accepting this policy or uploading a photo does not by itself establish that consent. In app versions that support the updated choices, one screen explains journal processing, optional OpenAI sharing and optional product statistics. You separately confirm that you are 18 or older and accept the Terms/acknowledge the Privacy Policy, then choose each processing permission independently. The processing choices start off; continuing records only the choices you actually make, with the disclosure version and date. AI and statistics are optional. Older app versions may not show all controls. Their transitional statistics mode is described in the product-statistics section; using an older version or accepting Terms is not treated as separate consent. Update the app or contact us to manage these choices. Once saved, account permissions apply across devices, including older versions.

You may withdraw consent without affecting processing already lawfully carried out. A feature may stop working if it needs the data covered by withdrawal. Controls and requests are described below.

### Internal product statistics

Internal dashboards use account identifiers, recent authenticated activity, and the dates, counts, types and statuses of registrations, photos, trackers, factors, routine marks, analyses and subscriptions to evaluate active/returning use, feature adoption and subscription conversion. Reports may also group tracker and factor names, including names you enter. Those names can reveal health information. Calculations may include journal records saved before you opted in. Photo contents, notes, analysis text, optional profile details, email addresses and device details are not used in these product-statistics queries. Data is processed by the infrastructure providers described below; it is not sent to OpenAI for statistics.

The source records remain account-linked even when a report displays totals. Refusing statistics does not restrict the journal, AI or purchases. After an account moves to the updated permission protocol, it is excluded from product dashboards until you give separate, explicit statistics permission. Before that transition, accounts used only in older versions retain the previous server-side statistics without a new consent prompt, unless you have already declined statistics or withdrawn journal permission. This compatibility mode does not create a consent record. Updating the app while staying signed in also ends the previous mode until you make your choice. A refusal or withdrawal applies on all devices: returning to an older version does not turn statistics back on. In versions with this control, turn off statistics in **More → About → AI and your data**, or contact us. Withdrawal excludes your account from future calculations and clears the recent-activity timestamp; it does not automatically delete the underlying journal or subscription records needed for their original purposes. Withdrawing journal permission also stops AI and statistics. Necessary sign-in, payment, error and security monitoring remains separate and does not depend on this optional choice. Website analytics is separate too.

### Mobile error diagnostics (version 2.0.9 and later)

To detect failures of sign-in, registration, purchases, email flows, photo upload and analysis, the app sends a small operational event to our API. It contains a random event identifier, a predefined failure category and reason, iOS/Android, app version/build and event time. It does not contain an account/device identifier, email, photo, journal text, receipt, token, raw error message or stack trace. These diagnostics are used to detect and troubleshoot failures, not to measure product engagement, and do not depend on optional product-statistics permission. They can be sent before sign-in.

Unhandled Dart/Flutter errors are included. Where the operating system makes them available, we also receive a coarse crash/hang category: Android 11+ reports this on a later launch; iOS MetricKit may deliver it later and its timestamp represents a reporting window. No full OS diagnostic payload or memory contents are transmitted. Collection is best-effort and does not cover every failure. Expected cancellation is not reported as a failure.

The app bounds and deduplicates its queue, retaining pending events for up to seven days and retrying when it can connect. Events pass through Cloudflare to our DigitalOcean-hosted API and central logs, configured for 30-day retention; a hash of the random event identifier is retained for up to seven days to prevent duplicate delivery. Network infrastructure still processes IP addresses for delivery/security; therefore we do not describe these events as anonymous. Expired local events are discarded when the app runs; deleting an account does not immediately erase dormant device or device-backup copies. Device backups follow your OS settings. Replay-prevention hashes may remain in restricted database backups under the periods below. Events are not sent to OpenAI and do not authorise a purchase or change your permissions. Apple/Google may separately process diagnostics under your platform settings.

## 4. Optional AI analysis

AI journal analysis starts when you request it and have enabled AI sharing. We send OpenAI selected photos and dates, tracker name/goal and capture settings, relevant routine/ongoing factors and dates, app language, and previous-analysis context where used. A photo note is included only when marked shareable with AI. Your email and optional profile fields are not included as separate AI inputs; a goal, note or picture can still reveal them.

Results and retained input context remain in your account. **Deleting a source photo or changing a note's sharing setting does not erase a saved analysis or recall a previous provider request.** Delete the analysis too, or ask us to delete associated data.

We do not use your journal to train our models. OpenAI's API does not train on customer inputs/outputs by default. Standard abuse-monitoring retention is up to 30 days, with legal and safety exceptions, including flagged image review. We do not promise zero provider retention. See [OpenAI's data controls](https://developers.openai.com/api/docs/guides/your-data).

Turn off future AI sharing in **More → About → AI and your data**, or contact us. This does not delete past results. AI can be wrong; it is not medical advice and does not make decisions about you with legal or similarly significant effects.

## 5. Photos, permissions and advertising

The camera provides preview and capture when you take a photo; library access is used for selected uploads. The optional framing guide is fixed, not face recognition. We do not create faceprints or identify people from photos. AI may describe visible features; that is different from identifying you.

Camera, library and notification permissions are controlled in device settings. The app keeps private local caches and sign-in tokens in device secure storage. Signing out clears app caches; exports and device/OS backups are separate copies under your control.

We do not sell personal or consumer health data, use journal content for advertising, or disclose it for cross-context behavioural advertising. The app has no advertising or usage-analytics SDKs. We do use the server-side product statistics described in section 3; absence of an SDK does not mean absence of analytics. Website analytics is separate.

## 6. Recipients and locations

- **DigitalOcean:** backend, account database and private photo storage in Frankfurt, Germany. From 9 November 2026, new database backups are also created, checked in an isolated restore environment, encrypted and stored here with 30-day retention. Database copies can contain notes, factors and saved AI results; original photo files are stored separately and are not included. Private encrypted hourly deletion-recovery exports are retained for 90 days and contain limited identifiers, object types and deletion/withdrawal times, not journal text or photo files. The live recovery journal currently has no automatic expiry; its purpose and retention review are described in the Privacy Policy.
- **OpenAI:** the AI inputs/outputs above; processing may occur in the US and other provider locations.
- **Resend:** verification and password-reset emails, including destination address and message content. Email data is stored in the US. These emails do not include journal photos or AI results.
- **Google/Gmail:** correspondence sent to our support mailbox. Avoid medical records or unnecessary sensitive attachments.
- **Apple and Google:** store payments and, if selected, sign-in. These functions receive transaction/sign-in information, not your photo journal.
- **GitHub Actions:** source code, CI and job orchestration with technical completion statuses. New backup and restore-check jobs run in DigitalOcean and do not send plaintext journal records or backup files to GitHub. Previously created private encrypted GitHub artifacts remain until their original expiration: database copies for up to 30 days and deletion-recovery exports for up to 90 days after creation. Access is restricted to recovery work; GitHub processing may occur outside Germany.
- **Cloudflare:** API delivery and protection. Requests and their contents, including journal data transmitted through the API, pass through Cloudflare; processing may occur outside Germany. This is separate from website analytics.
- **GitHub Pages and Cloudflare Web Analytics:** public website hosting and measurement. They can process network/browser information, visited pages and performance events. Cloudflare Web Analytics measures site traffic and performance; it is not connected to your private journal.

Providers process data for the relevant service under applicable terms and data-protection arrangements. Some also act independently for payment, account, security or legal obligations. Not every provider acts only as our processor.

Internal access is restricted to authorised support, operations, security, the product statistics described above and legal compliance. Journal content is not public to other users. Limited disclosure may be required by law or necessary to establish or defend legal claims, subject to applicable safeguards.

Processing may occur outside your country, including in Serbia through operation/support, Germany and the US. Where law requires transfer safeguards, these must cover the transfer, such as applicable standard contractual clauses. Contact us for information about safeguards relevant to your data.

## 7. Storage periods

- **Unfinished email registrations:** new registrations expire after 24 hours if the email is not confirmed. Expired registration records are removed by scheduled cleanup or when the address is registered again. Earlier unconfirmed accounts without an expiry are reviewed separately. Verification email/provider records follow the retention periods below.
- **Encrypted database backups:** configured retention is 30 days. Access is restricted to recovery work; deletion requests must be reapplied before recovered data returns to normal use. This is not the retention period of every provider or exported copy.
- **Deletion-recovery journal:** we retain object/event identifiers, object types and deletion/withdrawal times to prevent deleted data or withdrawn permissions from returning after a restore. These records do not contain photo files, journal text, email addresses or sign-in tokens, but identifiers can still be personal data. Encrypted exports have a configured 90-day retention period. The live recovery journal currently has no automatic expiry; its retention must cover the backups that could restore the affected records and is reviewed for that recovery purpose. It is not used to reconstruct your journal or for product statistics.
- **Product statistics:** the account-linked records follow the retention/deletion rules for the source account, activity, journal or subscription records. Aggregating them in a report does not create a separate anonymous-data exemption.
- **Analysis allowance records:** a minimal account-linked usage record remains when you delete a successful analysis, so deleting results does not reset the monthly limit. It contains identifiers and usage timing, not the photos or analysis text, and is removed with the account.
- **Journal and profile:** while you keep the content/account, subject to deletion. AI results may outlive individual source photos.
- **Deleted trackers and factors:** hidden immediately; scheduled cleanup becomes eligible after 30 days and runs periodically. This is not a guarantee of complete erasure by day 30. An explicit legal deletion request follows the applicable deadline.
- **Application logs:** our central log service is configured for 30 days. Provider security records and narrowly justified legal/security holds may have different periods.
- **Transactional emails:** Resend publishes default 30-day email/log retention, with separate backup/legal exceptions; see its [security information](https://resend.com/security).
- **Support and legal records:** while needed to resolve the request and for applicable legal obligations or claims. We limit retained records to that purpose, rather than keeping the whole journal.

We do not promise instant disappearance of every residual/provider copy or an unverified fixed backup lifetime. For an applicable deletion request, we identify relevant copies, instruct recipients where required, and explain lawful exceptions and deadlines. See the [deletion procedure](https://www.morphtrack.app/v2/delete-account).

## 8. Security

We use HTTPS, authenticated access, private photo storage and access restrictions. No system is completely secure. Storage is not end-to-end encrypted: the service processes content to provide requested features.

## 9. Choices and rights

You can edit profile details, delete content, disable future AI sharing, or delete your account in **More → Profile → Delete account**. For access/export, correction, withdrawal, restriction, objection, deletion or recipient information, email **morphtrack.app@gmail.com**, subject **Privacy request**. Rights depend on applicable law.

We verify identity proportionately, preferably through an authenticated account or verified control of its email. We do not require a new account, payment, your password or unnecessary health information. An authorised representative may contact us; we may verify their authority.

Under GDPR, we respond within one month, with a lawful extension explained within that month. Under applicable US consumer-health rules, the usual response period is 45 days; shorter deletion deadlines can apply. See the [health policy](https://www.morphtrack.app/v2/consumer-health-data). We explain refusals and review appeals sent with subject **Privacy appeal**, within 45 days or an earlier applicable deadline.

You may complain to the authority competent under the law that applies to your case: for example, Serbia's Commissioner under Serbian data-protection law, the competent supervisory authority under EEA/UK law, or a state's Attorney General where that US state's law applies. US complaint channels are not intended as universal destinations for all users. Complaining is optional, and our internal appeal does not limit statutory complaint rights. The [Health Data Policy](https://www.morphtrack.app/v2/consumer-health-data) provides further details. We do not discriminate for exercising privacy rights.

## 10. Age and changes

MorphTrack is intended for adults **18 and over**. Contact us if you believe we hold information from someone under 18 so we can investigate and address it.

We communicate material changes through an appropriate notice, such as in the app or by email. New consent-required purposes require new consent; changing this document does not itself provide it.

[Terms](https://www.morphtrack.app/v2/terms) · [Health data policy](https://www.morphtrack.app/v2/consumer-health-data) · [Account and data deletion](https://www.morphtrack.app/v2/delete-account)
