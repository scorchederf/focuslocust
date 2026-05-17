---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Tabnabbing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-tabnabbing-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Tabnabbing/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Tabnabbing](../../topics/tabnabbing/tabnabbing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-tabnabbing-readme |
| name | Tabnabbing |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Tabnabbing/README.md |

## Preserved Source Material

````yaml
_body: "# Tabnabbing\n\n> Reverse tabnabbing is an attack where a page linked from the target page is able to rewrite that\
  \ page, for example to replace it with a phishing site. As the user was originally on the correct page they are less likely\
  \ to notice that it has been changed to a phishing site, especially if the site looks the same as the target. If the user\
  \ authenticates to this new page then their credentials (or other sensitive data) are sent to the phishing site rather than\
  \ the legitimate one.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n* [Exploit](#exploit)\n* [Discover](#discover)\n\
  * [References](#references)\n\n## Tools\n\n* [PortSwigger/discovering-reversetabnabbing](https://portswigger.net/bappstore/80eb8fd46bf847b4b17861482c2f2a30)\
  \ - Discovering Reverse Tabnabbing\n\n## Methodology\n\nWhen tabnabbing, the attacker searches for links that are inserted\
  \ into the website and are under his control. Such links may be contained in a forum post, for example. Once he has found\
  \ this kind of functionality, it checks that the link's `rel` attribute does not contain the value `noopener` and the target\
  \ attribute contains the value `_blank`. If this is the case, the website is vulnerable to tabnabbing.\n\n## Exploit\n\n\
  1. Attacker posts a link to a website under his control that contains the following JS code: `window.opener.location = \"\
  http://evil.com\"`\n2. He tricks the victim into visiting the link, which is opened in the browser in a new tab.\n3. At\
  \ the same time the JS code is executed and the background tab is redirected to the website evil.com, which is most likely\
  \ a phishing website.\n4. If the victim opens the background tab again and doesn't look at the address bar, it may happen\
  \ that he thinks he is logged out, because a login page appears, for example.\n5. The victim tries to log on again and the\
  \ attacker receives the credentials\n\n## Discover\n\nSearch for the following link formats:\n\n```html\n<a href=\"...\"\
  \ target=\"_blank\" rel=\"\"> \n<a href=\"...\" target=\"_blank\">\n```\n\n## References\n\n* [Reverse Tabnabbing - OWASP\
  \ - October 20, 2020](https://web.archive.org/web/20200428035205/https://owasp.org/www-community/attacks/Reverse_Tabnabbing)\n\
  * [Tabnabbing - Wikipedia - May 25, 2010](https://web.archive.org/web/20251216150740/https://en.wikipedia.org/wiki/Tabnabbing)"
_relative_path: Tabnabbing/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Tabnabbing/README.md
````
