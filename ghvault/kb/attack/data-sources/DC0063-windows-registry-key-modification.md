---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0063 - Windows Registry Key Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0063` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Changes made to an existing registry key or its values. These modifications can include altering permissions, modifying stored data, or updating configuration settings.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4657 - Registry Value Modified: Logs changes to registry values, including modifications to startup entries, security settings, or system configurations.
- Sysmon (System Monitor) for Windows
    - Sysmon Event ID 13 - Registry Value Set: Captures changes to specific registry values.
    - Sysmon Event ID 14 - Registry Key & Value Renamed: Logs renaming of registry keys, which may indicate evasion attempts.
- Endpoint Detection and Response (EDR) Solutions
    - Monitor registry modifications for suspicious behavior.

## Source Verification

[source record](../../sources/mitre/windows-registry-key-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to an existing registry key or its values. These modifications can include altering permissions,\
\ modifying stored data, or updating configuration settings.\n\n*Data Collection Measures:*\n\n- Windows Event Logs\n  \
\  - Event ID 4657 - Registry Value Modified: Logs changes to registry values, including modifications to startup entries,\
\ security settings, or system configurations.\n- Sysmon (System Monitor) for Windows\n    - Sysmon Event ID 13 - Registry\
\ Value Set: Captures changes to specific registry values.\n    - Sysmon Event ID 14 - Registry Key & Value Renamed: Logs\
\ renaming of registry keys, which may indicate evasion attempts.\n- Endpoint Detection and Response (EDR) Solutions\n \
```
