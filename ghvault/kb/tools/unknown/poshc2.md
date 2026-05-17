---
parsed_by: focuslocust
source: mitre
type: generated
---
# PoshC2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0378` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

PoshC2 is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in PowerShell. Although PoshC2 is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/poshc2.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to gather credentials from memory.(Citation: GitHub PoshC2) |
| [T1007 - System Service Discovery](../../attack/techniques/T1007-system-service-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate service and service permission information.(Citation: GitHub PoshC2) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate network adapter information.(Citation: GitHub PoshC2) |
| [T1040 - Network Sniffing](../../attack/techniques/T1040-network-sniffing.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for taking packet captures on compromised hosts.(Citation: GitHub PoshC2) |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can perform port scans from an infected host.(Citation: GitHub PoshC2) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has a number of modules that use WMI to execute tasks.(Citation: GitHub PoshC2) |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [netstat](https://attack.mitre.org/software/S0104) to enumerate TCP and UDP connections.(Citation: GitHub PoshC2) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains multiple modules for injecting into processes, such as <code>Invoke-PSInject</code>.(Citation: GitHub PoshC2) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has modules for keystroke logging and capturing credentials from spoofed Outlook authentication messages.(Citation: GitHub PoshC2) |
| [T1068 - Exploitation for Privilege Escalation](../../attack/techniques/T1068-exploitation-for-privilege-escalation.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains modules for local privilege escalation exploits such as CVE-2016-9192 and CVE-2016-0099.(Citation: GitHub PoshC2) |
| [T1069.001 - Local Groups](../../attack/techniques/T1069.001-local-groups.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as <code>Get-LocAdm</code> for enumerating permission groups.(Citation: GitHub PoshC2) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can use protocols like HTTP/HTTPS for command and control traffic.(Citation: GitHub PoshC2) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as <code>Get-ComputerInfo</code>, for enumerating common system information.(Citation: GitHub PoshC2) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate files on the local file system and includes a module for enumerating recently accessed files.(Citation: GitHub PoshC2) |
| [T1087.001 - Local Account](../../attack/techniques/T1087.001-local-account.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate local and domain user account information.(Citation: GitHub PoshC2) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate local and domain user account information.(Citation: GitHub PoshC2) |
| [T1090 - Proxy](../../attack/techniques/T1090-proxy.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains modules that allow for use of proxies in command and control.(Citation: GitHub PoshC2) |
| [T1110 - Brute Force](../../attack/techniques/T1110-brute-force.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has modules for brute forcing local administrator and AD user accounts.(Citation: GitHub PoshC2) |
| [T1119 - Automated Collection](../../attack/techniques/T1119-automated-collection.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for recursively parsing through files and directories to gather valid credit card numbers.(Citation: GitHub PoshC2) |
| [T1134 - Access Token Manipulation](../../attack/techniques/T1134-access-token-manipulation.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can use Invoke-TokenManipulation for manipulating tokens.(Citation: GitHub PoshC2) |
| [T1134.002 - Create Process with Token](../../attack/techniques/T1134.002-create-process-with-token.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can use Invoke-RunAs to make tokens.(Citation: GitHub PoshC2) |
| [T1201 - Password Policy Discovery](../../attack/techniques/T1201-password-policy-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can use <code>Get-PassPol</code> to enumerate the domain password policy.(Citation: GitHub PoshC2) |
| [T1210 - Exploitation of Remote Services](../../attack/techniques/T1210-exploitation-of-remote-services.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for exploiting SMB via EternalBlue.(Citation: GitHub PoshC2) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has modules for enumerating domain trusts.(Citation: GitHub PoshC2) |
| [T1546.003 - Windows Management Instrumentation Event Subscription](../../attack/techniques/T1546.003-windows-management-instrumentation-event-subscription.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has the ability to persist on a system using WMI events.(Citation: GitHub PoshC2) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can utilize multiple methods to bypass UAC.(Citation: GitHub PoshC2) |
| [T1550.002 - Pass the Hash](../../attack/techniques/T1550.002-pass-the-hash.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has a number of modules that leverage pass the hash for lateral movement.(Citation: GitHub PoshC2) |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains modules for searching for passwords in local and remote files.(Citation: GitHub PoshC2) |
| [T1555 - Credentials from Password Stores](../../attack/techniques/T1555-credentials-from-password-stores.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can decrypt passwords stored in the RDCMan configuration file.(Citation: SecureWorks August 2019) |
| [T1557.001 - Name Resolution Poisoning and SMB Relay](../../attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.(Citation: GitHub PoshC2) |
| [T1560.001 - Archive via Utility](../../attack/techniques/T1560.001-archive-via-utility.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains a module for compressing data using ZIP.(Citation: GitHub PoshC2) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [PsExec](https://attack.mitre.org/software/S0029) for remote execution.(Citation: GitHub PoshC2) |

## Source Verification

[source record](../../sources/mitre/poshc2.md)

## Evidence Excerpt

```text
created: '2019-04-23T12:31:58.125Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[PoshC2](https://attack.mitre.org/software/S0378) is an open source remote administration and post-exploitation
framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python,
while the implants are written in [PowerShell](https://attack.mitre.org/techniques/T1059/001). Although [PoshC2](https://attack.mitre.org/software/S0378)
is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.(Citation: GitHub PoshC2)'
external_references:
- external_id: S0378
```
