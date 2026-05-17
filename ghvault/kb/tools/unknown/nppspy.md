---
parsed_by: focuslocust
source: mitre
type: generated
---
# NPPSPY

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1131` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them to a file on the victim system for follow-on exfiltration.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/nppspy.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) records data entered from the local system logon at Winlogon to capture credentials in cleartext.(Citation: Huntress NPPSPY 2022) |
| [T1056 - Input Capture](../../attack/techniques/T1056-input-capture.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext.(Citation: Huntress NPPSPY 2022) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) modifies the Registry to record the malicious listener for output from the Winlogon process.(Citation: Huntress NPPSPY 2022) |
| [T1119 - Automated Collection](../../attack/techniques/T1119-automated-collection.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) collection is automatically recorded to a specified file on the victim machine.(Citation: Huntress NPPSPY 2022) |
| [T1552 - Unsecured Credentials](../../attack/techniques/T1552-unsecured-credentials.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) captures credentials by recording them through an alternative network listener registered to the <code>mpnotify.exe</code> process, allowing for cleartext recording of logon information.(Citation: Huntress NPPSPY 2022) |
| [T1557 - Adversary-in-the-Middle](../../attack/techniques/T1557-adversary-in-the-middle.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) opens a new network listener for the <code>mpnotify.exe</code> process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information.(Citation: Huntress NPPSPY 2022) |
| [T1684.001 - Impersonation](../../attack/techniques/T1684.001-impersonation.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) creates a network listener using the misspelled label <code>logincontroll</code> recorded to the Registry key <code>HKLM\\SYSTEM\\CurrentControlSet\\Control\\NetworkProvider\\Order</code>.(Citation: Huntress NPPSPY 2022) |

## Source Verification

[source record](../../sources/mitre/nppspy.md)

## Evidence Excerpt

```text
created: '2024-05-17T18:49:15.318Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted
to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them
to a file on the victim system for follow-on exfiltration.(Citation: Huntress NPPSPY 2022)(Citation: Polak NPPSPY 2004)'
external_references:
- external_id: S1131
source_name: mitre-attack
```
