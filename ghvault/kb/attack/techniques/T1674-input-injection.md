---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1674 - Input Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1674` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may simulate keystrokes on a victim’s computer by various means to perform any type of action on behalf of the user, such as launching the command interpreter using keyboard shortcuts,  typing an inline script to be executed, or interacting directly with a GUI-based application.  These actions can be preprogrammed into adversary tooling or executed through physical devices such as Human Interface Devices (HIDs).

For example, adversaries have used tooling that monitors the Windows message loop to detect when a user visits bank-specific URLs. If detected, the tool then simulates keystrokes to open the developer console or select the address bar, pastes malicious JavaScript from the clipboard, and executes it - enabling manipulation of content within the browser, such as replacing bank account numbers during transactions.

Adversaries have also used malicious USB devices to emulate keystrokes that launch PowerShell, leading to the download and execution of malware from adversary-controlled servers.

## Source Verification

[source record](../../sources/mitre/input-injection.md)

## Evidence Excerpt

```text
created: '2025-03-27T18:14:06.330Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may simulate keystrokes on a victim’s computer by various means to perform any type of action on
behalf of the user, such as launching the command interpreter using keyboard shortcuts,  typing an inline script to be executed,
or interacting directly with a GUI-based application.  These actions can be preprogrammed into adversary tooling or executed
through physical devices such as Human Interface Devices (HIDs).
For example, adversaries have used tooling that monitors the Windows message loop to detect when a user visits bank-specific
URLs. If detected, the tool then simulates keystrokes to open the developer console or select the address bar, pastes malicious
```
