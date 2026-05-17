---
parsed_by: focuslocust
source: mitre
type: generated
---
# ftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0095` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ftp is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/ftp.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol](../../attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol.md) | explicit | source | [ftp](https://attack.mitre.org/software/S0095) may be used to exfiltrate data separate from the main command and control protocol.(Citation: Microsoft FTP)(Citation: Linux FTP) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files from an external system into a compromised environment.(Citation: Microsoft FTP)(Citation: Linux FTP) |
| [T1570 - Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md) | explicit | source | [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files between systems within a compromised environment.(Citation: Microsoft FTP)(Citation: Linux FTP) |

## Source Verification

[source record](../../sources/mitre/ftp.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:00.565Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer
information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate
data.(Citation: Microsoft FTP)(Citation: Linux FTP)'
external_references:
- external_id: S0095
source_name: mitre-attack
```
