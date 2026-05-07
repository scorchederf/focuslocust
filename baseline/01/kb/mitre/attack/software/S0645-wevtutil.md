---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0645
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0645-wevtutil
---

## Description

[[kb/mitre/attack/software/S0645-wevtutil|Wevtutil]] is a Windows command-line utility that enables administrators to retrieve information about event logs and publishers.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0645-wevtutil\|Wevtutil]] can be used to export events from a specific log.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1685.001-disable-or-modify-windows-event-log\|T1685.001]] | Disable or Modify Windows Event Log | [[kb/mitre/attack/software/S0645-wevtutil\|Wevtutil]] can be used to disable specific event logs on the system.[^1]  |
| [[kb/mitre/attack/techniques/T1685.005-clear-windows-event-logs\|T1685.005]] | Clear Windows Event Logs | [[kb/mitre/attack/software/S0645-wevtutil\|Wevtutil]] can be used to clear system and security event logs from the system.[^1] [^2]  |

 [^1]: [Wevtutil Microsoft Documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)
 [^2]: [F-Secure Lazarus Cryptocurrency Aug 2020](https://web.archive.org/web/20200901113617/https://labs.f-secure.com/assets/BlogFiles/f-secureLABS-tlp-white-lazarus-threat-intel-report2.pdf)
 [^3]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)
