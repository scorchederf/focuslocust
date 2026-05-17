---
parsed_by: focuslocust
source: mitre
type: generated
---
# Winexe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0191` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Winexe is a lightweight, open source tool similar to PsExec designed to allow system administrators to execute commands on remote servers.  Winexe is unique in that it is a GNU/Linux based client.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/winexe.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | [Winexe](https://attack.mitre.org/software/S0191) installs a service on the remote system, executes the command, then uninstalls the service.(Citation: Secpod Winexe June 2017) |

## Source Verification

[source record](../../sources/mitre/winexe.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Winexe](https://attack.mitre.org/software/S0191) is a lightweight, open source tool similar to [PsExec](https://attack.mitre.org/software/S0029)
designed to allow system administrators to execute commands on remote servers. (Citation: Winexe Github Sept 2013) [Winexe](https://attack.mitre.org/software/S0191)
is unique in that it is a GNU/Linux based client. (Citation: Überwachung APT28 Forfiles June 2015)'
external_references:
- external_id: S0191
source_name: mitre-attack
```
