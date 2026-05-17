---
parsed_by: focuslocust
source: mitre
type: generated
---
# Impacket

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0357` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Impacket is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. Impacket contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/impacket.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.(Citation: Impacket Tools) |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.(Citation: Impacket Tools) |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information from NTDS.dit.(Citation: Impacket Tools) |
| [T1003.004 - LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md) | explicit | source | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.(Citation: Impacket Tools) |
| [T1040 - Network Sniffing](../../attack/techniques/T1040-network-sniffing.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) can be used to sniff network traffic via an interface or raw socket.(Citation: Impacket Tools) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357)'s `wmiexec` module can be used to execute commands through WMI.(Citation: Impacket Tools)(Citation: Sygnia VelvetAnt 2024A) |
| [T1557.001 - Name Resolution Poisoning and SMB Relay](../../attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) modules like ntlmrelayx and smbrelayx can be used in conjunction with [Network Sniffing](https://attack.mitre.org/techniques/T1040) and [Name Resolution Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001) to gather NetNTLM credentials for [Brute Force](https://attack.mitre.org/techniques/T1110) or relay attacks that can gain code execution.(Citation: Impacket Tools) |
| [T1558.003 - Kerberoasting](../../attack/techniques/T1558.003-kerberoasting.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) modules like GetUserSPNs can be used to get Service Principal Names (SPNs) for user accounts. The output is formatted to be compatible with cracking tools like John the Ripper and Hashcat.(Citation: Impacket Tools) |
| [T1558.005 - Ccache Files](../../attack/techniques/T1558.005-ccache-files.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) tools – such as <code>getST.py</code> or <code>ticketer.py</code> – can be used to steal or forge Kerberos tickets using ccache files given a password, hash, aesKey, or TGT.(Citation: Kerberos GNU/Linux)(Citation: on security kerberos linux) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) contains various modules emulating other service execution tools such as [PsExec](https://attack.mitre.org/software/S0029).(Citation: Impacket Tools) |
| [T1570 - Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) has used its `wmiexec` command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks.(Citation: Sygnia VelvetAnt 2024A) |

## Source Verification

[source record](../../sources/mitre/impacket.md)

## Evidence Excerpt

```text
created: '2019-01-31T01:39:56.283Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python
for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357)
contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing,
and relay attacks.(Citation: Impacket Tools)'
external_references:
- external_id: S0357
```
