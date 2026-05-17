---
parsed_by: focuslocust
source: mitre
type: generated
---
# Forfiles

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0193` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Forfiles is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/forfiles.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [Forfiles](https://attack.mitre.org/software/S0193) can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).(Citation: Überwachung APT28 Forfiles June 2015) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Forfiles](https://attack.mitre.org/software/S0193) can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)(Citation: Überwachung APT28 Forfiles June 2015) |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | [Forfiles](https://attack.mitre.org/software/S0193) can be used to subvert controls and possibly conceal command execution by not directly invoking [cmd](https://attack.mitre.org/software/S0106).(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017) |

## Source Verification

[source record](../../sources/mitre/forfiles.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Forfiles](https://attack.mitre.org/software/S0193) is a Windows utility commonly used in batch jobs to execute
commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files
created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. (Citation:
Microsoft Forfiles Aug 2016)'
external_references:
- external_id: S0193
```
