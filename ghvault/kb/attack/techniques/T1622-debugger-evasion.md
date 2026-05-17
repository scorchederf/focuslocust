---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1622 - Debugger Evasion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1622` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads.

Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to Virtualization/Sandbox Evasion, if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.

Specific checks will vary based on the target and/or adversary. On Windows, this may involve Native API function calls such as <code>IsDebuggerPresent()</code> and <code> NtQueryInformationProcess()</code>, or manually checking the <code>BeingDebugged</code> flag of the Process Environment Block (PEB). On Linux, this may involve querying `/proc/self/status` for the `TracerPID` field, which indicates whether or not the process is being traced by dynamic analysis tools. Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would “swallow” or handle the potential error).

Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler, which will automatically handle the exception and allow the program’s execution to continue.

Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping Native API function calls such as <code>OutputDebugStringW()</code>.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.(Citation: Telefonica Snip3 December 2021) |

## Source Verification

[source record](../../sources/mitre/debugger-evasion.md)

## Evidence Excerpt

```text
created: '2022-04-01T17:59:46.156Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders
to trace and/or analyze the execution of potential malware payloads.(Citation: ProcessHacker Github)
Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative
of a debugged environment. Similar to [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497), if the
adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of
the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.
```
