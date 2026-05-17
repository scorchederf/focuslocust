---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1559 - Inter-Process Communication

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1559` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. 

Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows Dynamic Data Exchange or Component Object Model. Linux environments support several different IPC mechanisms, two of which being sockets and pipes. Higher level execution mediums, such as those of Command and Scripting Interpreters, may also leverage underlying IPC mechanisms. Adversaries may also use Remote Services such as Distributed Component Object Model to facilitate remote IPC execution.

## Source Verification

[source record](../../sources/mitre/inter-process-communication.md)

## Evidence Excerpt

```text
created: '2020-02-12T14:08:48.689Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC\
\ is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly\
\ used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. \n\nAdversaries\
\ may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in\
\ a form accessible through programming languages/libraries or native interfaces such as Windows [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002)\
\ or [Component Object Model](https://attack.mitre.org/techniques/T1559/001). Linux environments support several different\
```
