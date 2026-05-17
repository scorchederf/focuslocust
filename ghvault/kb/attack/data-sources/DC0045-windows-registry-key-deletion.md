---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0045 - Windows Registry Key Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0045` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The removal of a registry key within the Windows operating system.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which may indicate deletion.
    - Event ID 4660 - Object Deleted: Logs when a registry key is deleted.
- Sysmon (System Monitor) for Windows
    - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed.
    - Sysmon Event ID 13 - Registry Value Deleted: Captures removal of specific registry values.
- Endpoint Detection and Response (EDR) Solutions
    - Monitor registry deletions for suspicious behavior.

## Source Verification

[source record](../../sources/mitre/windows-registry-key-deletion.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The removal of a registry key within the Windows operating system.\n\n*Data Collection Measures:*\n\n- Windows\
\ Event Logs\n    - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which\
\ may indicate deletion.\n    - Event ID 4660 - Object Deleted: Logs when a registry key is deleted.\n- Sysmon (System Monitor)\
\ for Windows\n    - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed.\n    - Sysmon Event\
\ ID 13 - Registry Value Deleted: Captures removal of specific registry values.\n- Endpoint Detection and Response (EDR)\
\ Solutions\n    - Monitor registry deletions for suspicious behavior."
```
