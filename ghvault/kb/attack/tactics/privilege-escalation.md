---
parsed_by: focuslocust
source: mitre
type: generated
---
# TA0004 - Privilege Escalation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tactic` |
| Record ID | `TA0004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: 

* SYSTEM/root level
* local administrator
* user account with admin-like access 
* user accounts with access to specific system or perform specific function

These techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.

## Source Verification

[source record](../../sources/mitre/privilege-escalation.md)

## Evidence Excerpt

```text
created: '2018-10-17T00:14:20.652Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The adversary is trying to gain higher-level permissions.\n\nPrivilege Escalation consists of techniques that\
\ adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network\
\ with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are\
\ to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: \n\
\n* SYSTEM/root level\n* local administrator\n* user account with admin-like access \n* user accounts with access to specific\
\ system or perform specific function\n\nThese techniques often overlap with Persistence techniques, as OS features that\
```
