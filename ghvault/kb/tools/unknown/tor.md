---
parsed_by: focuslocust
source: mitre
type: generated
---
# Tor

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0183` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Tor is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. Tor utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/tor.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1090.003 - Multi-hop Proxy](../../attack/techniques/T1090.003-multi-hop-proxy.md) | explicit | source | Traffic traversing the [Tor](https://attack.mitre.org/software/S0183) network will be forwarded to multiple nodes before exiting the [Tor](https://attack.mitre.org/software/S0183) network and continuing on to its intended destination.(Citation: Dingledine Tor The Second-Generation Onion Router) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Tor](https://attack.mitre.org/software/S0183) encapsulates traffic in multiple layers of encryption, using TLS by default.(Citation: Dingledine Tor The Second-Generation Onion Router) |

## Source Verification

[source record](../../sources/mitre/tor.md)

## Evidence Excerpt

```text
created: '2018-01-16T16:13:52.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity
on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and
routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted
with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded
on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router)'
external_references:
```
