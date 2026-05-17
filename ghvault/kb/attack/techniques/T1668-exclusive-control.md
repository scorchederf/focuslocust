---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1668 - Exclusive Control

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1668` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries who successfully compromise a system may attempt to maintain persistence by “closing the door” behind them  – in other words, by preventing other threat actors from initially accessing or maintaining a foothold on the same system. 

For example, adversaries may patch a vulnerable, compromised system to prevent other threat actors from leveraging that vulnerability in the future. They may “close the door” in other ways, such as disabling vulnerable services, stripping privileges from accounts, or removing other malware already on the compromised device.

Hindering other threat actors may allow an adversary to maintain sole access to a compromised system or network. This prevents the threat actor from needing to compete with or even being removed themselves by other threat actors. It also reduces the “noise” in the environment, lowering the possibility of being caught and evicted by defenders. Finally, in the case of Resource Hijacking, leveraging a compromised device’s full power allows the threat actor to maximize profit.

## Source Verification

[source record](../../sources/mitre/exclusive-control.md)

## Evidence Excerpt

```text
created: '2025-01-31T15:22:39.317Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries who successfully compromise a system may attempt to maintain persistence by “closing the door” behind\
\ them  – in other words, by preventing other threat actors from initially accessing or maintaining a foothold on the same\
\ system. \n\nFor example, adversaries may patch a vulnerable, compromised system(Citation: Mandiant-iab-control)(Citation:\
\ CERT AT Fortinent Ransomware 2025) to prevent other threat actors from leveraging that vulnerability in the future. They\
\ may “close the door” in other ways, such as disabling vulnerable services(Citation: sophos-multiple-attackers), stripping\
\ privileges from accounts(Citation: aquasec-postgres-processes), or removing other malware already on the compromised device.(Citation:\
```
