---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1690
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1690-prevent-command-history-logging
tactic:
    - Defense Impairment
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they have done.<br><br>On Linux and macOS, command history is tracked in a file pointed to by the environment variable `HISTFILE`. When a user logs off a system, this information is flushed to a file in the user's home directory called `~/.bash_history`. The `HISTCONTROL` environment variable keeps track of what should be saved by the history command and eventually into the `~/.bash_history` file when a user logs out. `HISTCONTROL` does not exist by default on macOS, but can be set by the user and will be respected. The `HISTFILE` environment variable is also used in some ESXi systems.[^1] <br><br>Adversaries may clear the history environment variable (`unset HISTFILE`) or set the command history size to zero (`export HISTFILESIZE=0`) to prevent logging of commands. Additionally, `HISTCONTROL` can be configured to ignore commands that start with a space by simply setting it to "ignorespace". `HISTCONTROL` can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that " ls" will not be saved, but "ls" would be saved by history. Adversaries can abuse this to operate without leaving traces by simply prepending a space to all of their terminal commands.<br><br>On Windows systems, the `PSReadLine` module tracks commands used in all PowerShell sessions and writes them to a file (`$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt` by default). Adversaries may change where these logs are saved using `Set-PSReadLineOption -HistorySavePath {File Path}`. This will cause `ConsoleHost_history.txt` to stop receiving logs. Additionally, it is possible to turn off logging to this file using the PowerShell command `Set-PSReadlineOption -HistorySaveStyle SaveNothing`.[^2] [^3] <br><br>Adversaries may also leverage a [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] on network devices to disable historical command logging (e.g. `no logging`).

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory.[^1]  |
| [S1161](https://attack.mitre.org/software/S1161) | BPFDoor | BPFDoor sets the `MYSQL_HISTFILE` and `HISTFILE` to `/dev/null` preventing the shell and MySQL from logging history in `/proc/<PID>/environ`.[^1]   |
| [S1186](https://attack.mitre.org/software/S1186) | Line Dancer | Line Dancer can disable syslog on compromised devices.[^1]  |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA can impair logging by setting the `HISTFILE` environmental variable to `0` and stopping the `vmsyslogd` service.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has impaired command logging through the use of `dev/null` which prevents generating output from the command and does not wait for input.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has disabled logging and log forwarding on Ivanti devices targeting the `dslogserver` process.[^1] [^2] [^3] [^4]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Make sure that the `HISTCONTROL` environment variable is set to “ignoredups” instead of “ignoreboth” or “ignorespace”. |
| [[kb/mitre/attack/mitigations/M1039-environment-variable-permissions\|M1039]] | Environment Variable Permissions | Prevent users from changing the `HISTCONTROL`, `HISTFILE`, and `HISTFILESIZE` environment variables. [^1]  |

 [^1]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
 [^2]: [Microsoft about_History prevent command history](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7.6&viewFallbackFrom=powershell-7)
 [^3]: [Sophos PowerShell Command History Forensics](https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics)
 [^4]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
 [^5]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)
 [^6]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^7]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^8]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
 [^9]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
 [^10]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^11]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^12]: [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
