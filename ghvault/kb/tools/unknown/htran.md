---
parsed_by: focuslocust
source: mitre
type: generated
---
# HTRAN

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0040` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

HTRAN is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/htran.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1014 - Rootkit](../../attack/techniques/T1014-rootkit.md) | explicit | source | [HTRAN](https://attack.mitre.org/software/S0040) can install a rootkit to hide network connections from the host OS.(Citation: NCSC Joint Report Public Tools) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [HTRAN](https://attack.mitre.org/software/S0040) can inject into into running processes.(Citation: NCSC Joint Report Public Tools) |
| [T1090 - Proxy](../../attack/techniques/T1090-proxy.md) | explicit | source | [HTRAN](https://attack.mitre.org/software/S0040) can proxy TCP socket connections to obfuscate command and control infrastructure.(Citation: Operation Quantum Entanglement)(Citation: NCSC Joint Report Public Tools) |

## Source Verification

[source record](../../sources/mitre/htran.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:32.011Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[HTRAN](https://attack.mitre.org/software/S0040) is a tool that proxies connections through intermediate hops
and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when
interacting with the victim networks. (Citation: Operation Quantum Entanglement)(Citation: NCSC Joint Report Public Tools)'
external_references:
- external_id: S0040
source_name: mitre-attack
```
