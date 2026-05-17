---
parsed_by: focuslocust
source: mitre
type: generated
---
# IronNetInjector

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0581` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

IronNetInjector is a Turla toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including ComRAT.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/ironnetinjector.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1027.013 - Encrypted／Encoded File](../../attack/techniques/T1027.013-encrypted-encoded-file.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) can obfuscate variable names, encrypt strings, as well as base64 encode and Rijndael encrypt payloads.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [T1036.004 - Masquerade Task or Service](../../attack/techniques/T1036.004-masquerade-task-or-service.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) has been disguised as a legitimate service using the name PythonUpdateSrvc.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) has used a task XML file named <code>mssch.xml</code> to run an IronPython script when a user logs in or when specific system events are created.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [T1055.001 - Dynamic-link Library Injection](../../attack/techniques/T1055.001-dynamic-link-library-injection.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) has the ability to inject a DLL into running processes, including the [IronNetInjector](https://attack.mitre.org/software/S0581) DLL into explorer.exe.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) can identify processes via C# methods such as <code>GetProcessesByName</code> and running [Tasklist](https://attack.mitre.org/software/S0057) with the Python <code>os.popen</code> function.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [T1059.006 - Python](../../attack/techniques/T1059.006-python.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) can use IronPython scripts to load payloads with the help of a .NET injector.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [T1140 - Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) has the ability to decrypt embedded .NET and PE payloads.(Citation: Unit 42 IronNetInjector February 2021 ) |

## Source Verification

[source record](../../sources/mitre/ironnetinjector.md)

## Evidence Excerpt

```text
created: '2021-02-24T21:28:44.175Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[IronNetInjector](https://attack.mitre.org/software/S0581) is a [Turla](https://attack.mitre.org/groups/G0010)
toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one
or more payloads including [ComRAT](https://attack.mitre.org/software/S0126).(Citation: Unit 42 IronNetInjector February
2021 )'
external_references:
- external_id: S0581
```
