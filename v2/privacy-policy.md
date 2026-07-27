# Privacy Policy

_Last updated: 2026-07-27_

Читать по-русски: [Политика конфиденциальности](ru/privacy-policy)

This Privacy Policy describes how Morph (also referred to as MorphTrack, "we", "us", "the app") collects, uses, and protects your information when you use the app.

## 0. Who we are (data controller)

The data controller responsible for your personal data is **Raisat Ramazanova, an individual developer based in Serbia**. Morph / MorphTrack is the app's trade name, not a legal entity.

Contact for all privacy matters: **morphtrack.app@gmail.com**.

## 1. What we collect

- **Account information**: email address and authentication credentials. Passwords are stored in hashed form and are not stored in plain text. We also store whether your email address has been verified.
- **Photos**: images that you upload to the app, and the notes you optionally attach to them.
- **Trackers and routine data**: the trackers you create (their names and goal descriptions), the routine factors you log (for example skincare steps, supplements, sleep), and the links between them and your photos.
- **Optional profile details**: if you choose to fill in your profile, we store attributes such as age, gender, skin type, activity level, typical sleep, and smoking habits. Providing them is voluntary and they can be removed at any time.
- **AI analysis results**: when you run an AI analysis (see section 4), we store the resulting observations in your account.
- **Subscription status**: if you purchase a subscription, we receive and store your entitlement status and a purchase receipt from Apple or Google for validation. To link the purchase to your account and prevent misuse, the app attaches a pseudonymous account identifier (your Morph account ID) to the store transaction; Apple or Google stores it with the purchase and returns it to us with the receipt. We also keep the store's purchase token and use it to re-verify your subscription status with the store. We never receive or store your card or payment details.
- **Server logs**: when the app communicates with our servers, we record technical request information (the endpoint called, result status, timing, and your account ID) to secure the service and diagnose errors. Your IP address is processed transiently for rate limiting and may appear in short-lived infrastructure logs of our hosting provider; we do not store it in your account or profile.

**Photo metadata.** Photos from your camera may contain embedded metadata such as the capture date, device model, or GPS location. **We automatically remove all such metadata from every photo during upload** — the files we store contain no camera metadata and no location data. Photos that cannot be safely re-encoded are rejected rather than stored with metadata.

## 2. Health-related data and your explicit consent

Morph is a body/skin change tracker, so some of the data you choose to add — photos of your skin or body, notes about them, and optional profile details such as skin type, sleep, or smoking — may reveal information related to your health.

We process this data **only** to provide the features you use: storing and showing your photos and trackers, and generating the AI analyses you explicitly request. By uploading such photos, adding such details, and starting an AI analysis, you give your **explicit consent** to this processing. You can withdraw it at any time by deleting the relevant data or your account (see sections 11–12); withdrawal does not affect processing that already happened.

## 3. Why we collect it, and what we do NOT do

We use your information:

- to create and maintain your account;
- to store and display your photos, trackers, and routine data to you;
- to generate AI analyses that you explicitly request;
- to provide and validate subscriptions;
- to secure your account and protect against abuse;
- to provide customer support;
- to diagnose errors and maintain app security and reliability.

We **do not**:

- analyze the content of your photos, **except when you explicitly run an AI analysis** (see section 4);
- use your photos or any of your content to train AI models, or permit our AI provider to do so (see section 4);
- use your photos for advertising;
- sell your photos or your personal information;
- share your photos with other users;
- use analytics or advertising SDKs, or collect crash reports from your device.

## 4. AI analysis of your photos

The app can generate observations about visible changes between your photos ("AI analysis"). This happens **only when you explicitly start an analysis** — never automatically in the background.

When you run an analysis, the following is sent to our AI provider for processing:

- the photos selected for the analysis (with metadata already removed) and their dates;
- the name, goal / description text, and photo-capture settings (angle, framing, frequency) of the tracker being analyzed;
- the routine factors you logged for the analyzed period (their names and dates), and ongoing factors linked to the tracker (their names and start/end dates);
- a short summary (headline and date) of your most recent previous analysis of the same tracker, so results can reference earlier observations;
- a photo note **only if** you marked that note as "share with AI" — notes without this mark are never sent;
- the app language, so the result comes back in your language.

Your optional profile details (age, gender, skin type, and similar) and your email address are **not** sent to the AI provider.

Our AI provider is **OpenAI** (USA), acting as our data processor. Under OpenAI's API terms, data submitted through the API is not used to train their models. Analysis results are stored in your account until you delete the analysis, delete the tracker it belongs to (its analyses are erased together with the tracker, see section 10), or delete your account. Deleting individual photos does not automatically delete analyses that referenced them — you can delete each analysis separately in the app.

AI analyses are generated only at your request, are informational observations only, and are not used to make any automated decision about you that produces legal or similarly significant effects. They can be incomplete or wrong, and they are not medical advice (see the [Terms of Use](terms)).

## 5. Legal basis for processing

If you are located in the European Economic Area or the United Kingdom, we process your information under the following legal bases:

- **Contract**: to create your account and provide the app's functionality, including photo storage, trackers, analyses you request, and subscriptions you purchase.
- **Explicit consent**: for health-related data described in section 2, and for optional features such as optional profile details or sharing a photo note with the AI provider. You can withdraw consent at any time (section 12).
- **Legitimate interests**: to secure the app, prevent abuse, diagnose errors, and maintain reliability.
- **Legal obligation**: where we are required to comply with applicable laws.

## 6. Where your data is stored

Your photos and account data are stored on secure servers located in Germany (Frankfurt region).

When you run an AI analysis, the data described in section 4 is processed by OpenAI, which may process it in the United States (see section 14).

The app also keeps a local cache of your data (including downloaded photos) on your device so it loads faster; it lives in the app's private storage and is cleared when you sign out or uninstall the app. Sign-in tokens are kept in your device's secure storage (Keychain / Keystore).

## 7. Service providers

We use third-party service providers to operate the app:

- **Cloud hosting and storage** — DigitalOcean (servers in Frankfurt, Germany): application hosting and private photo storage.
- **AI processing** — OpenAI (USA): only for analyses you explicitly request, as described in section 4.
- **Email delivery** — a transactional email provider used to send account verification and password reset emails.
- **Payment processing** — Apple App Store, Google Play: subscription purchases are processed entirely by the stores.

These providers process information only on our behalf and only as necessary to provide their services to us. We do not allow these providers to use your photos or content for their own purposes.

## 8. Who has access

Your uploaded photos, trackers, notes, and analyses are private to your account and are not visible to other users.

We restrict internal access to user content to the minimum necessary to operate, secure, troubleshoot, or support the app. We do not access your content except when necessary for security, support requested by you, legal compliance, or troubleshooting a technical issue.

## 9. Device permissions

The app requests access to your camera or photo library only when you choose to take or upload photos. The app will ask for permission to show notifications the first time a photo reminder is due; you can turn reminders off in the app or in your device settings at any time. You can change any of these permissions in your device settings.

## 10. Retention

We store your photos, notes, and analysis results until you delete them or delete your account.

When you delete a tracker or a routine factor in the app, it is hidden from your account immediately and permanently erased from our servers within 30 days.

Server logs are retained for up to 90 days, unless a longer period is required for security, fraud prevention, or legal compliance.

## 11. Deletion

You can delete individual photos, notes, trackers, factors, and analyses at any time from within the app.

You may also delete your entire account from within the app (Profile → Delete account), which permanently removes your photos, trackers, routine data, analyses, and account data. Deleted data may remain in encrypted backups for up to 30 days before being permanently removed.

Deleting your account does **not** cancel an active store subscription — manage subscriptions in your Apple or Google account settings.

See also: [account deletion details](delete-account) — including how to request deletion by email, without the app.

## 12. Your rights

Depending on your location, you may have rights to access, correct, delete, export, or object to the processing of your personal information.

Where processing is based on your consent, you may **withdraw it at any time** — for example by removing profile details, unmarking a note's "share with AI" setting, deleting the relevant data, or deleting your account. Withdrawal does not affect processing that happened before it.

You can delete your content and account in the app. For other requests, contact us at morphtrack.app@gmail.com.

You also have the right to **lodge a complaint with a supervisory authority**: in Serbia, the Commissioner for Information of Public Importance and Personal Data Protection (Poverenik); in the EEA or the UK, the data-protection authority of your country of residence.

## 13. Security

We use reasonable technical and organizational measures to protect your information, including encryption in transit, access controls, and private storage for uploaded photos. However, no method of transmission or storage is completely secure.

## 14. International transfers

Depending on your location, your information may be processed in countries other than your country of residence — in particular, data is stored in Germany (EU), and AI analyses are processed by OpenAI in the United States. Transfers to OpenAI are protected by appropriate safeguards, including the standard contractual clauses incorporated into our data processing agreement with OpenAI.

## 15. Children

The app is not intended for use by anyone under the age of 18. We do not knowingly collect personal information from anyone under 18.

## 16. Changes to this policy

We may update this Privacy Policy from time to time. The "Last updated" date at the top reflects the most recent revision. Material changes will be communicated within the app or by email.

## 17. Contact

For questions, requests, or concerns related to your data, contact us at morphtrack.app@gmail.com.
