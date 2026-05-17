---
parsed_by: focuslocust
source: mitre
type: generated
---
# CrackMapExec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0488` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

CrackMapExec, or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. CrackMapExec collects Active Directory information to conduct lateral movement through targeted networks.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/crackmapexec.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can dump usernames and hashed passwords from the SAM.(Citation: CME Github September 2018) |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can dump hashed passwords associated with Active Directory using Windows' Directory Replication Services API (DRSUAPI), or Volume Shadow Copy.(Citation: CME Github September 2018) |
| [T1003.004 - LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can dump hashed passwords from LSA secrets for the targeted system.(Citation: CME Github September 2018) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can collect DNS information from the targeted system.(Citation: CME Github September 2018) |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active IP addresses, along with the machine name, within a targeted network.(Citation: CME Github September 2018) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can execute remote commands using Windows Management Instrumentation.(Citation: CME Github September 2018)	 |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active sessions for a targeted system.(Citation: CME Github September 2018) |
| [T1053.002 - At](../../attack/techniques/T1053.002-at.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can set a scheduled task on the target system to execute commands remotely using [at](https://attack.mitre.org/software/S0110).(Citation: CME Github September 2018) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can execute PowerShell commands via WMI.(Citation: CME Github September 2018) |
| [T1069.002 - Domain Groups](../../attack/techniques/T1069.002-domain-groups.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can gather the user accounts within domain groups.(Citation: CME Github September 2018) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover specified filetypes and log files on a targeted system.(Citation: CME Github September 2018) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the domain user accounts on a targeted system.(Citation: CME Github September 2018) |
| [T1110 - Brute Force](../../attack/techniques/T1110-brute-force.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force supplied user credentials across a network range.(Citation: CME Github September 2018) |
| [T1110.001 - Password Guessing](../../attack/techniques/T1110.001-password-guessing.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force passwords for a specified user on a single target system or across an entire network.(Citation: CME Github September 2018) |
| [T1110.003 - Password Spraying](../../attack/techniques/T1110.003-password-spraying.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force credential authentication by using a supplied list of usernames and a single password.(Citation: CME Github September 2018) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can create a registry key using wdigest.(Citation: CME Github September 2018) |
| [T1135 - Network Share Discovery](../../attack/techniques/T1135-network-share-discovery.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the shared folders and associated permissions for a targeted network.(Citation: CME Github September 2018) |
| [T1201 - Password Policy Discovery](../../attack/techniques/T1201-password-policy-discovery.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover the password policies applied to the target system.(Citation: CME Github September 2018) |
| [T1550.002 - Pass the Hash](../../attack/techniques/T1550.002-pass-the-hash.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can pass the hash to authenticate via SMB.(Citation: CME Github September 2018) |
| [T1680 - Local Storage Discovery](../../attack/techniques/T1680-local-storage-discovery.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the system drives and associated system name.(Citation: CME Github September 2018) |

## Source Verification

[source record](../../sources/mitre/crackmapexec.md)

## Evidence Excerpt

```text
created: '2020-07-17T14:23:05.958Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[CrackMapExec](https://attack.mitre.org/software/S0488), or CME, is a post-exploitation tool developed in Python
and designed for penetration testing against networks. [CrackMapExec](https://attack.mitre.org/software/S0488) collects
Active Directory information to conduct lateral movement through targeted networks.(Citation: CME Github September 2018)'
external_references:
- external_id: S0488
source_name: mitre-attack
```
