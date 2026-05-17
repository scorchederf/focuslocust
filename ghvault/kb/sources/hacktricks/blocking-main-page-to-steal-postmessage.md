---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Blocking main page to steal postmessage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-postmessage-vulnerabilities-blocking-main-page-to-steal-postmessage` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/postmessage-vulnerabilities/blocking-main-page-to-steal-postmessage.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Blocking main page to steal postmessage](../../topics/pentesting-web/blocking-main-page-to-steal-postmessage.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-postmessage-vulnerabilities-blocking-main-page-to-steal-postmessage |
| name | Blocking main page to steal postmessage |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/postmessage-vulnerabilities/blocking-main-page-to-steal-postmessage.md |

## Preserved Source Material

````yaml
_body: "# Blocking main page to steal postmessage\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Winning RCs with\
  \ Iframes\n\nAccording to this [**Terjanq writeup**](https://gist.github.com/terjanq/7c1a71b83db5e02253c218765f96a710) blob\
  \ documents created from null origins are isolated for security benefits, which means that if you maintain busy the main\
  \ page, the iframe page is going to be executed.\n\nBasically in that challenge an **isolated iframe is executed** and right\
  \ **after** it's **loaded** the **parent** page is going to **send a post** message with the **flag**.\\\nHowever, that\
  \ postmessage communication is **vulnerable to XSS** (the **iframe** can execute JS code).\n\nTherefore, the goal of the\
  \ attacker is to **let the parent create the iframe**, but **before** let the **parent** page **send** the sensitive data\
  \ (**flag**) **keep it busy** and send the **payload to the iframe**. While the **parent is busy** the **iframe executes\
  \ the payload** which will be some JS that will listen for the **parent postmessage message and leak the flag**.\\\nFinally,\
  \ the iframe has executed the payload and the parent page stops being busy, so it sends the flag and the payload leaks it.\n\
  \nBut how could you make the parent be **busy right after it generated the iframe and just while it's waiting for the iframe\
  \ to be ready to send the sensitive data?** Basically, you need to find **async** **action** you could make the parent **execute**.\
  \ For example, in that challenge the parent was **listening** to **postmessages** like this:\n\n```javascript\nwindow.addEventListener(\"\
  message\", (e) => {\n  if (e.data == \"blob loaded\") {\n    $(\"#previewModal\").modal()\n  }\n})\n```\n\nso it was possible\
  \ to send a **big integer in a postmessage** that will be **converted to string** in that comparison, which will take some\
  \ time:\n\n```bash\nconst buffer = new Uint8Array(1e7);\nwin?.postMessage(buffer, '*', [buffer.buffer]);\n```\n\nAnd in\
  \ order to be precise and **send** that **postmessage** just **after** the **iframe** is created but **before** it's **ready**\
  \ to receive the data from the parent, you will need to **play with the miliseconds of a `setTimeout`**.\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/postmessage-vulnerabilities/blocking-main-page-to-steal-postmessage.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/postmessage-vulnerabilities/blocking-main-page-to-steal-postmessage.md
````
