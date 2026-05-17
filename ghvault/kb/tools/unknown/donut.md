---
parsed_by: focuslocust
source: mitre
type: generated
---
# Donut

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0695` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Donut is an open source framework used to generate position-independent shellcode. Donut generated code has been used by multiple threat actors to inject and load malicious payloads into memory.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/donut.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1027.002 - Software Packing](../../attack/techniques/T1027.002-software-packing.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate packed code modules.(Citation: Donut Github)	 |
| [T1027.013 - Encrypted／Encoded File](../../attack/techniques/T1027.013-encrypted-encoded-file.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.(Citation: Donut Github) |
| [T1027.015 - Compression](../../attack/techniques/T1027.015-compression.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.(Citation: Donut Github) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) includes a subproject <code>DonutTest</code> to inject shellcode into a target process.(Citation: Donut Github)	 |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) includes subprojects that enumerate and identify information about [Process Injection](https://attack.mitre.org/techniques/T1055) candidates.(Citation: Donut Github)	 |
| [T1059 - Command and Scripting Interpreter](../../attack/techniques/T1059-command-and-scripting-interpreter.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via Ruby.(Citation: Donut Github)	 |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via PowerShell.(Citation: Donut Github)	 |
| [T1059.005 - Visual Basic](../../attack/techniques/T1059.005-visual-basic.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via VBScript.(Citation: Donut Github)	 |
| [T1059.006 - Python](../../attack/techniques/T1059.006-python.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via Python.(Citation: Donut Github)	 |
| [T1059.007 - JavaScript](../../attack/techniques/T1059.007-javascript.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via JavaScript or JScript.(Citation: Donut Github)	 |
| [T1070 - Indicator Removal](../../attack/techniques/T1070-indicator-removal.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can erase file references to payloads in-memory after being reflectively loaded and executed.(Citation: Donut Github) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can use HTTP to download previously staged shellcode payloads.(Citation: Donut Github) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can download and execute previously staged shellcode payloads.(Citation: Donut Github) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) code modules use various API functions to load and inject code.(Citation: Donut Github)	 |
| [T1620 - Reflective Code Loading](../../attack/techniques/T1620-reflective-code-loading.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.(Citation: Donut Github) |
| [T1685 - Disable or Modify Tools](../../attack/techniques/T1685-disable-or-modify-tools.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related [Native API](https://attack.mitre.org/techniques/T1106) functions to avoid process termination.(Citation: Donut Github)	 |

## Source Verification

[source record](../../sources/mitre/donut.md)

## Evidence Excerpt

```text
created: '2022-03-25T13:35:46.781Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Donut](https://attack.mitre.org/software/S0695) is an open source framework used to generate position-independent
shellcode.(Citation: Donut Github)(Citation: Introducing Donut) [Donut](https://attack.mitre.org/software/S0695) generated
code has been used by multiple threat actors to inject and load malicious payloads into memory.(Citation: NCC Group WastedLocker
June 2020)'
external_references:
- external_id: S0695
```
