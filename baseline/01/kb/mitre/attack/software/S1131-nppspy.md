---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S1131
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S1131-nppspy
---

## Description

NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them to a file on the victim system for follow-on exfiltration.[^1] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] records data entered from the local system logon at Winlogon to capture credentials in cleartext.[^1]  |
| [[kb/mitre/attack/techniques/T1056-input-capture\|T1056]] | Input Capture | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext.[^1]  |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] modifies the Registry to record the malicious listener for output from the Winlogon process.[^1]  |
| [[kb/mitre/attack/techniques/T1119-automated-collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] collection is automatically recorded to a specified file on the victim machine.[^1]  |
| [[kb/mitre/attack/techniques/T1552-unsecured-credentials\|T1552]] | Unsecured Credentials | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] captures credentials by recording them through an alternative network listener registered to the `mpnotify.exe` process, allowing for cleartext recording of logon information.[^1]  |
| [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle\|T1557]] | Adversary-in-the-Middle | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] opens a new network listener for the `mpnotify.exe` process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information.[^1]  |
| [[kb/mitre/attack/techniques/T1684.001-impersonation\|T1684.001]] | Impersonation | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] creates a network listener using the misspelled label `logincontroll` recorded to the Registry key `HKLM\\SYSTEM\\CurrentControlSet\\Control\\NetworkProvider\\Order`.[^1]  |

 [^1]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
 [^2]: [Polak NPPSPY 2004](https://www.blackhat.com/presentations/win-usa-04/bh-win-04-polak/bh-win-04-polak2.pdf)
