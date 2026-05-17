---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1044 - Restrict Library Loading

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1044` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Restricting library loading involves implementing security controls to ensure that only trusted and verified libraries (DLLs, shared objects, etc.) are loaded into processes. Adversaries often abuse Dynamic-Link Library (DLL) Injection, DLL Search Order Hijacking, or LD_PRELOAD mechanisms to execute malicious code by forcing the operating system to load untrusted libraries. This mitigation can be implemented through the following measures: 

Enforce Safe Library Loading Practices:

- Enable `SafeDLLSearchMode` on Windows.
- Restrict `LD_PRELOAD` and `LD_LIBRARY_PATH` usage on Linux systems.

Code Signing Enforcement:

- Require digital signatures for all libraries loaded into processes.
- Use tools like Signtool, and WDAC to enforce signed DLL execution.

Environment Hardening:

- Secure library paths and directories to prevent adversaries from placing rogue libraries.
- Monitor user-writable directories and system configurations for unauthorized changes.

Audit and Monitor Library Loading:

- Enable `Sysmon` on Windows to monitor for suspicious library loads.
- Use `auditd` on Linux to monitor shared library paths and configuration file changes.

Use Application Control Solutions:

- Implement AppLocker, WDAC, or SELinux to allow only trusted libraries.

*Tools for Implementation*

Windows-Specific Tools:

- AppLocker: Application whitelisting for DLLs.
- Windows Defender Application Control (WDAC): Restrict unauthorized library execution.
- Signtool: Verify and enforce code signing.
- Sysmon: Monitor DLL load events (Event ID 7).

Linux-Specific Tools:

- auditd: Monitor changes to library paths and critical files.
- SELinux/AppArmor: Define policies to restrict library loading.
- ldconfig and chattr: Secure LD configuration files and prevent unauthorized modifications.

Cross-Platform Solutions:

- Wazuh or OSSEC: File integrity monitoring for library changes.
- Tripwire: Detect and alert on unauthorized library modifications.

## Source Verification

[source record](../../sources/mitre/restrict-library-loading.md)

## Evidence Excerpt

```text
created: '2019-06-11T17:00:01.740Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Restricting library loading involves implementing security controls to ensure that only trusted and verified\
\ libraries (DLLs, shared objects, etc.) are loaded into processes. Adversaries often abuse Dynamic-Link Library (DLL) Injection,\
\ DLL Search Order Hijacking, or LD_PRELOAD mechanisms to execute malicious code by forcing the operating system to load\
\ untrusted libraries. This mitigation can be implemented through the following measures: \n\nEnforce Safe Library Loading\
\ Practices:\n\n- Enable `SafeDLLSearchMode` on Windows.\n- Restrict `LD_PRELOAD` and `LD_LIBRARY_PATH` usage on Linux systems.\n\
\nCode Signing Enforcement:\n\n- Require digital signatures for all libraries loaded into processes.\n- Use tools like Signtool,\
```
