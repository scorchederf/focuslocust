---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1679 - Selective Exclusion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1679` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may intentionally exclude certain files, folders, directories, file types, or system components from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries may avoid encrypting include `.dll`, `.exe`, and `.lnk`.  

Adversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts, or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. 

Exclusions may target files and components whose corruption would cause instability, break core services, or immediately expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators that could trigger alarms or otherwise inhibit achieving their goals.

## Source Verification

[source record](../../sources/mitre/selective-exclusion.md)

## Evidence Excerpt

```text
created: '2025-09-25T14:45:54.760Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may intentionally exclude certain files, folders, directories, file types, or system components\
\ from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries\
\ may avoid encrypting include `.dll`, `.exe`, and `.lnk`.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January\
\ 2024)  \n\nAdversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts,\
\ or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. \n\n\
Exclusions may target files and components whose corruption would cause instability, break core services, or immediately\
```
