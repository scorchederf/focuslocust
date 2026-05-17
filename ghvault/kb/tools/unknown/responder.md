---
parsed_by: focuslocust
source: mitre
type: generated
---
# Responder

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0174` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/responder.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1040 - Network Sniffing](../../attack/techniques/T1040-network-sniffing.md) | explicit | source | [Responder](https://attack.mitre.org/software/S0174) captures hashes and credentials that are sent to the system after the name services have been poisoned.(Citation: GitHub Responder) |
| [T1557.001 - Name Resolution Poisoning and SMB Relay](../../attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay.md) | explicit | source | [Responder](https://attack.mitre.org/software/S0174) is used to poison name services to gather hashes and credentials from systems within a local network.(Citation: GitHub Responder) |

## Source Verification

[source record](../../sources/mitre/responder.md)

## Evidence Excerpt

```text
created: '2018-01-16T16:13:52.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP
rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. (Citation:
GitHub Responder)'
external_references:
- external_id: S0174
source_name: mitre-attack
```
