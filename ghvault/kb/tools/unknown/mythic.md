---
parsed_by: focuslocust
source: mitre
type: generated
---
# Mythic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0699` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Mythic is an open source, cross-platform post-exploitation/command and control platform. Mythic is designed to "plug-n-play" with various agents and communication channels. Deployed Mythic C2 servers have been observed as part of potentially malicious infrastructure.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/mythic.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1008 - Fallback Channels](../../attack/techniques/T1008-fallback-channels.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked.(Citation: Mythc Documentation)	 |
| [T1030 - Data Transfer Size Limits](../../attack/techniques/T1030-data-transfer-size-limits.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports custom chunk sizes used to upload/download files.(Citation: Mythc Documentation)	 |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports HTTP-based C2 profiles.(Citation: Mythc Documentation)	 |
| [T1071.002 - File Transfer Protocols](../../attack/techniques/T1071.002-file-transfer-protocols.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports SMB-based peer-to-peer C2 profiles.(Citation: Mythc Documentation)	 |
| [T1071.004 - DNS](../../attack/techniques/T1071.004-dns.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports DNS-based C2 profiles.(Citation: Mythc Documentation)	 |
| [T1090.001 - Internal Proxy](../../attack/techniques/T1090.001-internal-proxy.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) can leverage a peer-to-peer C2 profile between agents.(Citation: Mythc Documentation)		 |
| [T1090.002 - External Proxy](../../attack/techniques/T1090.002-external-proxy.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) can leverage a modified SOCKS5 proxy to tunnel egress C2 traffic.(Citation: Mythc Documentation) |
| [T1090.004 - Domain Fronting](../../attack/techniques/T1090.004-domain-fronting.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports domain fronting via custom request headers.(Citation: Mythc Documentation)	 |
| [T1095 - Non-Application Layer Protocol](../../attack/techniques/T1095-non-application-layer-protocol.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports WebSocket and TCP-based C2 profiles.(Citation: Mythc Documentation)	 |
| [T1119 - Automated Collection](../../attack/techniques/T1119-automated-collection.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports scripting of file downloads from agents.(Citation: Mythc Documentation)	 |
| [T1132 - Data Encoding](../../attack/techniques/T1132-data-encoding.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) provides various transform functions to encode and/or randomize C2 data.(Citation: Mythc Documentation)	 |
| [T1572 - Protocol Tunneling](../../attack/techniques/T1572-protocol-tunneling.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) can use SOCKS proxies to tunnel traffic through another protocol.(Citation: Mythc Documentation) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Mythic](https://attack.mitre.org/software/S0699) supports SSL encrypted C2.(Citation: Mythc Documentation)	 |

## Source Verification

[source record](../../sources/mitre/mythic.md)

## Evidence Excerpt

```text
created: '2022-03-26T01:38:12.966Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Mythic](https://attack.mitre.org/software/S0699) is an open source, cross-platform post-exploitation/command
and control platform. [Mythic](https://attack.mitre.org/software/S0699) is designed to "plug-n-play" with various agents
and communication channels.(Citation: Mythic Github)(Citation: Mythic SpecterOps)(Citation: Mythc Documentation) Deployed
[Mythic](https://attack.mitre.org/software/S0699) C2 servers have been observed as part of potentially malicious infrastructure.(Citation:
RecordedFuture 2021 Ad Infra)'
external_references:
```
