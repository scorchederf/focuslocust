---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1674
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1674-input-injection
tactic:
    - Execution
platforms:
    - Windows
    - macOS
    - Linux
permissions required:
    - none
---

## Description

Adversaries may simulate keystrokes on a victim’s computer by various means to perform any type of action on behalf of the user, such as launching the command interpreter using keyboard shortcuts,  typing an inline script to be executed, or interacting directly with a GUI-based application.  These actions can be preprogrammed into adversary tooling or executed through physical devices such as Human Interface Devices (HIDs).<br><br>For example, adversaries have used tooling that monitors the Windows message loop to detect when a user visits bank-specific URLs. If detected, the tool then simulates keystrokes to open the developer console or select the address bar, pastes malicious JavaScript from the clipboard, and executes it - enabling manipulation of content within the browser, such as replacing bank account numbers during transactions.[^1] [^3] <br><br>Adversaries have also used malicious USB devices to emulate keystrokes that launch PowerShell, leading to the download and execution of malware from adversary-controlled servers.[^2] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1034-limit-hardware-installation\|M1034]] | Limit Hardware Installation | Limit the use of USB devices and removable media within a network. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Denylist scripting and use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^1]  |

 [^1]: [BleepingComputer BackSwap](https://www.bleepingcomputer.com/news/security/backswap-banking-trojan-uses-never-before-seen-techniques/)
 [^2]: [BleepingComputer USB](https://www.bleepingcomputer.com/news/security/fbi-hackers-sending-malicious-usb-drives-and-teddy-bears-via-usps/)
 [^3]: [welivesecurity BackSwap](https://www.welivesecurity.com/2018/05/25/backswap-malware-empty-bank-accounts/)
 [^4]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)
