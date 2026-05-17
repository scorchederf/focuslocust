---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# RDP Hijacking for Lateral Movement with tscon

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-t1076-rdp-hijacking-for-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1076-rdp-hijacking-for-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [RDP Hijacking for Lateral Movement with tscon](../../topics/offensive-security/rdp-hijacking-for-lateral-movement-with-tscon.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-t1076-rdp-hijacking-for-lateral-movement |
| name | RDP Hijacking for Lateral Movement with tscon |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/t1076-rdp-hijacking-for-lateral-movement.md |

## Preserved Source Material

````yaml
_asset_filenames:
- rdp-admin.png
- rdp-hijack-no-password.png
- rdp-login.png
- rdp-logon-sessions.png
- rdp-logs (1).png
- rdp-password.png
- rdp-session-disconnect.png
- rdp-session-reconnect.png
- rdp-sessions.png
- rdp-spotless-with-system.png
- rdp-spotless.png
- rdp-system.png
_body: "---\ndescription: >-\n  This lab explores a technique that allows a SYSTEM account to move laterally\n  through the\
  \ network using RDP without the need for credentials.\n---\n\n# RDP Hijacking for Lateral Movement with tscon\n\n## Execution\n\
  \nIt is possible by design to switch from one user's desktop session to another through the Task Manager (one of the ways).\n\
  \nBelow shows that there are two users on the system and currently the administrator session is in active:\n\n![](../../.gitbook/assets/rdp-admin.png)\n\
  \nLet's switch to the `spotless` session - this requires knowing the user's password, which for this exercise is known,\
  \ so lets enter it:\n\n![](../../.gitbook/assets/rdp-login.png)\n\n![](../../.gitbook/assets/rdp-password.png)\n\nWe are\
  \ now reconnected to the `spotless` session:\n\n![](../../.gitbook/assets/rdp-spotless.png)\n\nNow this is where it gets\
  \ interesting. It is possible to reconnect to a users session without knowing their password if you have `SYSTEM` level\
  \ privileges on the system. \\\nLet's elevate to `SYSTEM` using psexec (privilege escalation exploits, service creation\
  \ or any other technique will also do):\n\n```\npsexec -s cmd\n```\n\n![](../../.gitbook/assets/rdp-system.png)\n\nEnumerate\
  \ available sessions on the host with `query user`:\n\n![](../../.gitbook/assets/rdp-sessions.png)\n\nSwitch to the `spotless`\
  \ session without getting requested for a password by using the native windows binary `tscon.exe`that enables users to connect\
  \ to other desktop sessions by specifying which session ID (`2` in this case for the `spotless` session) should be connected\
  \ to which session (`console` in this case, where the active `administator` session originates from):\n\n```csharp\ncmd\
  \ /k tscon 2 /dest:console\n```\n\n![](../../.gitbook/assets/rdp-hijack-no-password.png)\n\nImmediately after that, we are\
  \ presented with the desktop session for `spotless`:\n\n![](../../.gitbook/assets/rdp-spotless-with-system.png)\n\n## Observations\n\
  \nLooking at the logs, `tscon.exe` being executed as a `SYSTEM` user is something you may want to investigate further to\
  \ make sure this is not a lateral movement attempt:\n\n![](<../../.gitbook/assets/rdp-logs (1).png>)\n\nAlso, note how `event_data.LogonID`\
  \ and event\\_ids `4778` (logon) and `4779` (logoff) events can be used to figure out which desktop sessions got disconnected/reconnected:\n\
  \n![Administrator session disconnected](../../.gitbook/assets/rdp-session-disconnect.png)\n\n![Spotless session reconnected\
  \ (hijacked)](../../.gitbook/assets/rdp-session-reconnect.png)\n\nJust reinforcing the above - note the usernames and logon\
  \ session IDs:\n\n![](../../.gitbook/assets/rdp-logon-sessions.png)\n\n## References\n\n{% embed url=\"http://blog.gentilkiwi.com/securite/vol-de-session-rdp\"\
  \ %}\n\n{% embed url=\"http://www.korznikov.com/2017/03/0-day-or-feature-privilege-escalation.html\" %}\n\n{% embed url=\"\
  https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4778\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/tscon\"\
  \ %}"
_relative_path: offensive-security/lateral-movement/t1076-rdp-hijacking-for-lateral-movement.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1076-rdp-hijacking-for-lateral-movement.md
````
