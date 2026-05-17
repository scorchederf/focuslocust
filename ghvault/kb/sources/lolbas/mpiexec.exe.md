---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mpiexec.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mpiexec.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mpiexec.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mpiexec.exe](../../tools/windows/mpiexec.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mpiexec.exe |
| name | Mpiexec.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/powershell/high-performance-computing/mpiexec |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: mpiexec.exe {CMD}
  Description: Executes a command via MPI command-line tool.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes commands under a trusted, Microsoft signed binary.
Created: 2025-09-25
Description: Command-line tool for running Message Passing Interface (MPI) applications.
Full_Path:
- Path: C:\Program Files\Microsoft MPI\Bin\mpiexec.exe
- Path: C:\Program Files (x86)\Microsoft MPI\Bin\mpiexec.exe
Name: Mpiexec.exe
Resources:
- Link: https://learn.microsoft.com/en-us/powershell/high-performance-computing/mpiexec
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mpiexec.yml
```
