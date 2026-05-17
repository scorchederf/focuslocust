---
parsed_by: focuslocust
source: mitre
type: generated
---
# Covenant

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1155` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Covenant is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as HAFNIUM during operations. Covenant functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/covenant.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can utilize WMI to install new Grunt listeners through XSL files or command one-liners.(Citation: Github Covenant) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can create PowerShell-based launchers for Grunt installation.(Citation: Github Covenant) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) provides access to a Command Shell in Windows environments for follow-on command execution and tasking.(Citation: Github Covenant) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can establish command and control via HTTP.(Citation: Github Covenant) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) implants can gather basic information on infected systems.(Citation: Github Covenant) |
| [T1218.004 - InstallUtil](../../attack/techniques/T1218.004-installutil.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can create launchers via an InstallUtil XML file to install new Grunt listeners.(Citation: Github Covenant) |
| [T1218.005 - Mshta](../../attack/techniques/T1218.005-mshta.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can create HTA files to install Grunt listeners.(Citation: Github Covenant) |
| [T1218.010 - Regsvr32](../../attack/techniques/T1218.010-regsvr32.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can create SCT files for installation via `Regsvr32` to deploy new Grunt listeners.(Citation: Github Covenant) |
| [T1571 - Non-Standard Port](../../attack/techniques/T1571-non-standard-port.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) listeners and controllers can be configured to use non-standard ports.(Citation: Github Covenant) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) can utilize SSL to encrypt command and control traffic.(Citation: Github Covenant) |

## Source Verification

[source record](../../sources/mitre/covenant.md)

## Evidence Excerpt

```text
created: '2024-09-04T17:08:08.985Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Covenant](https://attack.mitre.org/software/S1155) is a multi-platform command and control framework written
in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such
as [HAFNIUM](https://attack.mitre.org/groups/G0125) during operations. [Covenant](https://attack.mitre.org/software/S1155)
functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.(Citation:
Github Covenant)(Citation: Microsoft HAFNIUM March 2020)'
external_references:
```
