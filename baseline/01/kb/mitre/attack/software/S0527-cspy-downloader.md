---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0527
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0527-cspy-downloader
---

## Description

[[kb/mitre/attack/software/S0527-cspy-downloader|CSPY Downloader]] is a tool designed to evade analysis and download additional payloads used by Kimsuky.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027.002-software-packing\|T1027.002]] | Software Packing | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] has been packed with UPX.[^1]  |
| [[kb/mitre/attack/techniques/T1036.004-masquerade-task-or-service\|T1036.004]] | Masquerade Task or Service | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] has attempted to appear as a legitimate Windows service with a fake description claiming it is used to support packed applications.[^1]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can use the schtasks utility to bypass UAC.[^1]  |
| [[kb/mitre/attack/techniques/T1070-indicator-removal\|T1070]] | Indicator Removal | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] has the ability to remove values it writes to the Registry.[^1]  |
| [[kb/mitre/attack/techniques/T1070.004-file-deletion\|T1070.004]] | File Deletion | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] has the ability to self delete.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can use GET requests to download additional payloads from C2.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can download additional tools to a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can write to the Registry under the `%windir%` variable to execute tasks.[^1]  |
| [[kb/mitre/attack/techniques/T1204.002-malicious-file\|T1204.002]] | Malicious File | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] has been delivered via malicious documents with embedded macros.[^1]  |
| [[kb/mitre/attack/techniques/T1497.001-system-checks\|T1497.001]] | System Checks | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can search loaded modules, PEB structure, file paths, Registry keys, and memory to determine if it is being debugged or running in a virtual environment.[^1]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can bypass UAC using the SilentCleanup task to execute the binary with elevated privileges.[^1]  |
| [[kb/mitre/attack/techniques/T1553.002-code-signing\|T1553.002]] | Code Signing | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] has come signed with revoked certificates.[^1]  |

 [^1]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
