---
parsed_by: focuslocust
source: mitre
type: generated
---
# KernelCallbackTable

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574.013` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [KernelCallbackTable](../../attack/techniques/T1574.013-kernelcallbacktable.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574.013 |
| name | KernelCallbackTable |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574/013 |

## Preserved Source Material

```yaml
created: '2022-02-25T15:27:44.927Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse the <code>KernelCallbackTable</code> of a process to hijack its execution flow in order
  to run their own payloads.(Citation: Lazarus APT January 2022)(Citation: FinFisher exposed ) The <code>KernelCallbackTable</code>
  can be found in the Process Environment Block (PEB) and is initialized to an array of graphic functions available to a GUI
  process once <code>user32.dll</code> is loaded.(Citation: Windows Process Injection KernelCallbackTable)


  An adversary may hijack the execution flow of a process using the <code>KernelCallbackTable</code> by replacing an original
  callback function with a malicious payload. Modifying callback functions can be achieved in various ways involving related
  behaviors such as [Reflective Code Loading](https://attack.mitre.org/techniques/T1620) or [Process Injection](https://attack.mitre.org/techniques/T1055)
  into another process.


  A pointer to the memory address of the <code>KernelCallbackTable</code> can be obtained by locating the PEB (ex: via a call
  to the <code>NtQueryInformationProcess()</code> [Native API](https://attack.mitre.org/techniques/T1106) function).(Citation:
  NtQueryInformationProcess) Once the pointer is located, the <code>KernelCallbackTable</code> can be duplicated, and a function
  in the table (e.g., <code>fnCOPYDATA</code>) set to the address of a malicious payload (ex: via <code>WriteProcessMemory()</code>).
  The PEB is then updated with the new address of the table. Once the tampered function is invoked, the malicious payload
  will be triggered.(Citation: Lazarus APT January 2022)


  The tampered function is typically invoked using a Windows message. After the process is hijacked and malicious code is
  executed, the <code>KernelCallbackTable</code> may also be restored to its original state by the rest of the malicious payload.(Citation:
  Lazarus APT January 2022) Use of the <code>KernelCallbackTable</code> to hijack execution flow may evade detection from
  security products since the execution can be masked under a legitimate process.'
external_references:
- external_id: T1574.013
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574/013
- description: 'Microsoft Defender Security Research Team. (2018, March 1). FinFisher exposed: A researcher’s tale of defeating
    traps, tricks, and complex virtual machines. Retrieved January 27, 2022.'
  source_name: 'FinFisher exposed '
  url: https://www.microsoft.com/security/blog/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/
- description: Microsoft. (2021, November 23). NtQueryInformationProcess function (winternl.h). Retrieved February 4, 2022.
  source_name: NtQueryInformationProcess
  url: https://docs.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntqueryinformationprocess
- description: 'odzhan. (2019, May 25). Windows Process Injection: KernelCallbackTable used by FinFisher / FinSpy. Retrieved
    February 4, 2022.'
  source_name: Windows Process Injection KernelCallbackTable
  url: https://modexp.wordpress.com/2019/05/25/windows-injection-finspy/
- description: Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub
    in latest campaign. Retrieved January 27, 2022.
  source_name: Lazarus APT January 2022
  url: https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/
id: attack-pattern--a4657bc9-d22f-47d2-a7b7-dd6ec33f3dde
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T23:01:58.951Z'
name: KernelCallbackTable
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
