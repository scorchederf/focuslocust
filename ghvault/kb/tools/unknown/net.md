---
parsed_by: focuslocust
source: mitre
type: generated
---
# Net

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0039` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The Net utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. 

Net has a great deal of functionality,  much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through SMB/Windows Admin Shares using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/net.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1007 - System Service Discovery](../../attack/techniques/T1007-system-service-discovery.md) | explicit | source | The <code>net start</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to find information about Windows services.(Citation: Savill 1999) |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | Commands such as <code>net view</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about available remote systems.(Citation: Savill 1999) |
| [T1021.002 - SMB／Windows Admin Shares](../../attack/techniques/T1021.002-smb-windows-admin-shares.md) | explicit | source | Lateral movement can be done with [Net](https://attack.mitre.org/software/S0039) through <code>net use</code> commands to connect to the on remote systems.(Citation: Savill 1999) |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | Commands such as <code>net use</code> and <code>net session</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about network connections from a particular host.(Citation: Savill 1999) |
| [T1069.001 - Local Groups](../../attack/techniques/T1069.001-local-groups.md) | explicit | source | Commands such as <code>net group</code> and <code>net localgroup</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate groups.(Citation: Savill 1999) |
| [T1069.002 - Domain Groups](../../attack/techniques/T1069.002-domain-groups.md) | explicit | source | Commands such as <code>net group /domain</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate groups.(Citation: Savill 1999) |
| [T1070.005 - Network Share Connection Removal](../../attack/techniques/T1070.005-network-share-connection-removal.md) | explicit | source | The <code>net use \\system\share /delete</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to remove an established connection to a network share.(Citation: Technet Net Use) |
| [T1087.001 - Local Account](../../attack/techniques/T1087.001-local-account.md) | explicit | source | Commands under <code>net user</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate user accounts.(Citation: Savill 1999) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [Net](https://attack.mitre.org/software/S0039) commands used with the <code>/domain</code> flag can be used to gather information about and manipulate user accounts on the current domain.(Citation: Microsoft Net) |
| [T1098.007 - Additional Local or Domain Groups](../../attack/techniques/T1098.007-additional-local-or-domain-groups.md) | explicit | source | The `net localgroup` and `net group` commands in [Net](https://attack.mitre.org/software/S0039) can be used to add existing users to local and domain groups.(Citation: Microsoft Net Localgroup) (Citation: Microsoft Net Group) |
| [T1124 - System Time Discovery](../../attack/techniques/T1124-system-time-discovery.md) | explicit | source | The <code>net time</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to determine the local or remote system time.(Citation: TechNet Net Time) |
| [T1135 - Network Share Discovery](../../attack/techniques/T1135-network-share-discovery.md) | explicit | source | The <code>net view \\remotesystem</code> and <code>net share</code> commands in [Net](https://attack.mitre.org/software/S0039) can be used to find shared drives and directories on remote and local systems respectively.(Citation: Savill 1999) |
| [T1136.001 - Local Account](../../attack/techniques/T1136.001-local-account.md) | explicit | source | The <code>net user username \password</code> commands in [Net](https://attack.mitre.org/software/S0039) can be used to create a local account.(Citation: Savill 1999) |
| [T1136.002 - Domain Account](../../attack/techniques/T1136.002-domain-account.md) | explicit | source | The <code>net user username \password \domain</code> commands in [Net](https://attack.mitre.org/software/S0039) can be used to create a domain account.(Citation: Savill 1999) |
| [T1201 - Password Policy Discovery](../../attack/techniques/T1201-password-policy-discovery.md) | explicit | source | The <code>net accounts</code> and <code>net accounts /domain</code> commands with [Net](https://attack.mitre.org/software/S0039) can be used to obtain password policy information.(Citation: Savill 1999) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | The <code>net start</code> and <code>net stop</code> commands can be used in [Net](https://attack.mitre.org/software/S0039) to execute or stop Windows services.(Citation: Savill 1999) |

## Source Verification

[source record](../../sources/mitre/net.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:31.601Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It
is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft
Net Utility)
[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which
is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows
Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services.
```
