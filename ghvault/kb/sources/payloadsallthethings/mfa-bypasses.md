---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# MFA Bypasses

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-account-takeover-mfa-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Account Takeover/mfa-bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MFA Bypasses](../../topics/account-takeover/mfa-bypasses.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-account-takeover-mfa-bypass |
| name | MFA Bypasses |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Account%20Takeover/mfa-bypass.md |

## Preserved Source Material

````yaml
_body: "# MFA Bypasses\n\n> Multi-Factor Authentication (MFA) is a security measure that requires users to provide two or\
  \ more verification factors to gain access to a system, application, or network. It combines something the user knows (like\
  \ a password), something they have (like a phone or security token), and/or something they are (biometric verification).\
  \ This layered approach enhances security by making unauthorized access more difficult, even if a password is compromised.\n\
  > MFA Bypasses are techniques attackers use to circumvent MFA protections. These methods can include exploiting weaknesses\
  \ in MFA implementations, intercepting authentication tokens, leveraging social engineering to manipulate users or support\
  \ staff, or exploiting session-based vulnerabilities.\n\n## Summary\n\n* [Response Manipulation](#response-manipulation)\n\
  * [Status Code Manipulation](#status-code-manipulation)\n* [2FA Code Leakage in Response](#2fa-code-leakage-in-response)\n\
  * [JS File Analysis](#js-file-analysis)\n* [2FA Code Reusability](#2fa-code-reusability)\n* [Lack of Brute-Force Protection](#lack-of-brute-force-protection)\n\
  * [Missing 2FA Code Integrity Validation](#missing-2fa-code-integrity-validation)\n* [CSRF on 2FA Disabling](#csrf-on-2fa-disabling)\n\
  * [Password Reset Disable 2FA](#password-reset-disable-2fa)\n* [Backup Code Abuse](#backup-code-abuse)\n* [Clickjacking\
  \ on 2FA Disabling Page](#clickjacking-on-2fa-disabling-page)\n* [Enabling 2FA doesn't expire Previously active Sessions](#enabling-2fa-doesnt-expire-previously-active-sessions)\n\
  * [Bypass 2FA by Force Browsing](#bypass-2fa-by-force-browsing)\n* [Bypass 2FA with null or 000000](#bypass-2fa-with-null-or-000000)\n\
  * [Bypass 2FA with array](#bypass-2fa-with-array)\n\n## 2FA Bypasses\n\n### Response Manipulation\n\nIf response is `\"\
  success\":false`\nChange it to `\"success\":true`\n\n### Status Code Manipulation\n\nIf Status Code is **4xx**\nTry changing\
  \ it to **200 OK** and see if it bypass restrictions\n\n### 2FA Code Leakage in Response\n\nCheck the response of the 2FA\
  \ Code Triggering Request for leaked code.\n\n### JS File Analysis\n\nRare but some JS Files may contain info about the\
  \ 2FA Code, worth giving a shot\n\n### 2FA Code Reusability\n\nSame code can be reused\n\n### Lack of Brute-Force Protection\n\
  \nPossible to brute-force any length 2FA Code\n\n### Missing 2FA Code Integrity Validation\n\nCode for any user account\
  \ can be used to bypass the 2FA\n\n### CSRF on 2FA Disabling\n\nNo CSRF Protection on disabling 2FA, also there is no auth\
  \ confirmation\n\n### Password Reset Disable 2FA\n\n2FA gets disabled on password change/email change\n\n### Backup Code\
  \ Abuse\n\nBypassing 2FA by abusing the Backup code feature\nUse the above-mentioned techniques to bypass the Backup Code\
  \ to remove/reset 2FA restrictions\n\n### Clickjacking on 2FA Disabling Page\n\nIframing the 2FA Disabling page and social\
  \ engineering victim to disable the 2FA\n\n### Enabling 2FA doesn't expire Previously active Sessions\n\nIf the session\
  \ is already hijacked and there is a session timeout vulnerability\n\n### Bypass 2FA by Force Browsing\n\nIf the application\
  \ redirects to `/my-account` url upon login while 2FA is disabled, try replacing `/2fa/verify` with `/my-account` while\
  \ 2FA is enabled to bypass verification.\n\n### Bypass 2FA with null or 000000\n\nEnter the code **000000** or **null**\
  \ to bypass 2FA protection.\n\n### Bypass 2FA with array\n\n```json\n{\n    \"otp\":[\n        \"1234\",\n        \"1111\"\
  ,\n        \"1337\", // GOOD OTP\n        \"2222\",\n        \"3333\",\n        \"4444\",\n        \"5555\"\n    ]\n}\n\
  ```"
_relative_path: Account Takeover/mfa-bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Account Takeover/mfa-bypass.md
````
