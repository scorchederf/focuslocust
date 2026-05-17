---
parsed_by: focuslocust
source: mitre
type: generated
---
# cmd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0106` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

cmd is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities. 

Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., <code>dir</code> ), deleting files (e.g., <code>del</code> ), and copying files (e.g., <code>copy</code> ).

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/cmd.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) is used to execute programs and other actions at the command-line interface.(Citation: TechNet Cmd) |
| [T1070.004 - File Deletion](../../attack/techniques/T1070.004-file-deletion.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to delete files from the file system.(Citation: TechNet Del) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to find information about the operating system.(Citation: TechNet Dir) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to find files and directories with native functionality such as <code>dir</code> commands.(Citation: TechNet Dir) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected external system.(Citation: TechNet Copy) |
| [T1570 - Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected internal system.(Citation: TechNet Copy) |

## Source Verification

[source record](../../sources/mitre/cmd.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:05.319Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[cmd](https://attack.mitre.org/software/S0106) is the Windows command-line interpreter that can be used to interact
with systems and execute other processes and utilities. (Citation: TechNet Cmd)
Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in
a directory (e.g., <code>dir</code> (Citation: TechNet Dir)), deleting files (e.g., <code>del</code> (Citation: TechNet
Del)), and copying files (e.g., <code>copy</code> (Citation: TechNet Copy)).'
external_references:
```
