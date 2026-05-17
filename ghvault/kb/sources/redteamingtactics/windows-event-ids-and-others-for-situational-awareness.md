---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Windows Event IDs and Others for Situational Awareness

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-windows-event-ids-for-situational-awareness` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/windows-event-ids-for-situational-awareness.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Event IDs and Others for Situational Awareness](../../topics/offensive-security/windows-event-ids-and-others-for-situational-awareness.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-enumeration-and-discovery-windows-event-ids-for-situational-awareness |
| name | Windows Event IDs and Others for Situational Awareness |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/enumeration-and-discovery/windows-event-ids-for-situational-awareness.md |

## Preserved Source Material

```yaml
_asset_filenames: []
_body: "# Windows Event IDs and Others for Situational Awareness\n\nBelow is a living list of Windows event IDs and other\
  \ miscellaenous snippets, that may be useful for  situational awareness, once you are on a box:\n\n| Activity          \
  \                     | Powershell to read event logs for the                                                          \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                |\n| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
  \ |\n| **Lock/screensaver**                   |                                                                        \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                        |\n| Workstation was locked   \
  \              | Get-WinEvent -FilterHashtable @{ LogName='security'; Id='4800' }                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                         |\n| Workstation was unlocked               | Get-WinEvent -FilterHashtable\
  \ @{ LogName='security'; Id='4801' }                                                                                   \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \            |\n| Screensaved invoked                    | Get-WinEvent -FilterHashtable @{ LogName='security'; Id='4802'\
  \ }                                                                                                                    \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                 |\n| Screensaver dismissed\
  \                  | Get-WinEvent -FilterHashtable @{ LogName='security'; Id='4803' }                                  \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                             |\n|                                        |            \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                              |\n| **System ON/OFF**                      |                                           \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                     |\n\
  | Windows is starting up                 | Get-WinEvent -FilterHashtable @{ LogName='security'; Id='4608' }            \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                   |\n| System uptime                 \
  \         | Get-WinEvent -FilterHashtable @{ LogName='system'; Id='6013' }                                             \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                    |\n| Windows is shutting down               | Get-WinEvent -FilterHashtable\
  \ @{ LogName='security'; Id='4609' }                                                                                   \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \            |\n| System has been shut down              | Get-WinEvent -FilterHashtable @{ LogName='system'; Id='1074'\
  \ }                                                                                                                    \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                   |\n|               \
  \                         |                                                                                            \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                    |\n| **System sleep/awake**                 |     \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                     |\n| System entering sleep mode             | Get-WinEvent -FilterHashtable @{ LogName='system';\
  \ Id=42 }                                                                                                              \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                             |\n| System\
  \ returning from sleep            | Get-WinEvent -FilterHashtable @{ LogName='system'; Id='1'; ProviderName = \"Microsoft-Windows-Power-Troubleshooter\"\
  \ }                                                                                                                    \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                             |\n|                                        |                            \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \              |\n| **Logons**                             |                                                           \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                     |\n| Successful logons\
  \                      | Get-WinEvent -FilterHashtable @{ LogName='Security'; Id='4624' }                              \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                 |\n| Logons with explicit credentials       | Get-WinEvent\
  \ -FilterHashtable @{ LogName='Security'; Id='4648' }                                                                  \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                             |\n| Account logoffs                        | Get-WinEvent -FilterHashtable @{ LogName='security';\
  \ Id='4634' }                                                                                                          \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                           |\n|       \
  \                                 |                                                                                    \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                            |\n| **Access**                           \
  \  |                                                                                                                   \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                             |\n| Outbound RDP                           | Get-WinEvent -FilterHashtable\
  \ @{ LogName='Microsoft-Windows-TerminalServices-RDPClient/Operational'; id='1024' } \\| select timecreated, message \\\
  | ft -AutoSize -Wrap                                                                                                   \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \             |\n| Inbound RDP                            | <p>Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-TerminalServices-LocalSessionManager/Operational';\
  \ id='21' } | select timecreated, message | ft -AutoSize -Wrap</p><p></p><p>Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational';\
  \ id=131 } | select timecreated, message | ft -AutoSize -Wrap\n</p><p>\n</p><p>Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational';\
  \ id='1149' } | ft -AutoSize -Wrap</p>                                                                                 \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                              |\n| Outbound WinRM                         | <p>Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-WinRM/Operational';\
  \ id=6 }</p><p></p><p>Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-WinRM/Operational'; id=80 }</p>      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                             |\n| Inbound WinRM                       \
  \   | <p>Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-WinRM/Operational'; id=91 }</p><p></p><p>Get-WinEvent\
  \ -FilterHashtable @{ LogName='Microsoft-Windows-WMI-Activity/Operational'; id=5857 } | ? {$_.message -match 'Win32_WIN32_TERMINALSERVICE_Prov|CIMWin32'}</p>\
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \     |\n| Inbound Network and Interactive Logons | <p>$events = New-Object System.Collections.ArrayList</p><p></p><p>Get-WinEvent\
  \ -FilterHashtable @{ LogName='Security'; id=(4624); starttime=(get-date).AddMinutes(-60*24*2) } | % {</p><p>    $event\
  \ = New-Object psobject</p><p>    $subjectUser = $_.properties[2].value + \"\\\" + $_.properties[1].value</p><p>    $targetUser\
  \ = $_.properties[6].value + \"\\\" + $_.properties[5].value</p><p>    $logonType = $_.properties[8].value</p><p>    $subjectComputer\
  \ = $_.properties[18].value</p><p>    if ($logonType -in 3,7,8,9,10,11 -and $subjectComputer -notmatch \"::1|-|^127.0.0.1\"\
  )</p><p>    {</p><p>        switch ($logonType) {</p><p>            3 { $logonType = \"Network\" }</p><p>            7 {\
  \ $logonType = \"Screen Unlock\" }</p><p>            8 { $logonType = \"Network Cleartext\" }</p><p>            9 { $logonType\
  \ = \"New Credentials\" }</p><p>            10 { $logonType = \"Remote Interactive\" }</p><p>            11 { $logonType\
  \ = \"Cached Interactive\" }</p><p>        }</p><p>        $event | Add-Member \"Time\" $_.TimeCreated</p><p>        $event\
  \ | Add-Member \"Subject\" $subjectUser</p><p>        $event | Add-Member \"LogonFrom\" $subjectComputer</p><p>        $event\
  \ | Add-Member \"LoggedAs\" $targetUser</p><p>        $event | Add-Member \"Type\" $logonType</p><p>        $events.Add($event)\
  \ | out-null</p><p>    }</p><p>}</p><p></p><p>$events</p> |\n| Outbound Network Logons                | <p>$events = New-Object\
  \ System.Collections.ArrayList\n</p><p> \n</p><p>Get-WinEvent -FilterHashtable @{ LogName='Security'; id=(4648); starttime=(get-date).AddMinutes(-60*24*2)\
  \ } | % {\n</p><p>    $event = New-Object psobject\n</p><p>    $subjecUser = $_.Properties[2].Value + \"\\\" + $_.Properties[1].Value\n\
  </p><p>    $targetUser = $_.Properties[6].Value + \"\\\" + $_.Properties[5].Value\n</p><p>    $targetInfo = $_.Properties[9].Value\n\
  </p><p>    $process = $_.Properties[11].Value\n</p><p> \n</p><p>    $event | Add-Member \"Time\" $_.timecreated\n</p><p>\
  \    $event | Add-Member \"SubjectUser\" $subjecUser\n</p><p>    $event | Add-Member \"TargetUser\" $targetUser\n</p><p>\
  \    $event | Add-Member \"Target\" $targetInfo\n</p><p>    $event | Add-Member \"Process\" $process\n</p><p> \n</p><p>\
  \    if ($targetInfo -notmatch 'localhost')\n</p><p>    {\n</p><p>        $events.add($event) | out-null\n</p><p>    }\n\
  </p><p>}\n</p><p> \n</p><p>$events</p>                                                                                 \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                       |\n|           \
  \                             |                                                                                        \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                        |\n| **Activity**                           | \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                         |\n| Attempt to install a service           | Get-WinEvent -FilterHashtable @{\
  \ LogName='Security'; Id='4697' }                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \         |\n| Scheduled task created                 | Get-WinEvent -FilterHashtable @{ LogName='security'; Id='4698' }\
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                               |\n| Scheduled task updated\
  \                 | Get-WinEvent -FilterHashtable @{ LogName='security'; Id='4702' }                                   \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                            |\n| Sysinternals usage?                    | Get-ItemProperty\
  \ 'HKCU:\\SOFTWARE\\Sysinternals\\\\\\*' \\| select PSChildName, EulaAccepted                                          \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                               |\n|                                        |                                          \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      |\n\
  | **Security**                           |                                                                             \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                   |\n| LSASS started as a protected process\
  \   | Get-WinEvent -FilterHashtable @{ LogName='system'; Id='12' ; ProviderName='Microsoft-Windows-Wininit' }          \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                                                                                                      \
  \                                              |"
_relative_path: offensive-security/enumeration-and-discovery/windows-event-ids-for-situational-awareness.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/windows-event-ids-for-situational-awareness.md
```
