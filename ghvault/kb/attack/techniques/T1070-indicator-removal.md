---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1070 - Indicator Removal

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1070` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal system behavior.

Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific, allowing adversaries to tailor modifications that minimize suspicion.

These actions may not prevent detection entirely but can delay recognition of malicious activity or reduce the fidelity of alerts by making events appear benign or consistent with routine operations. Additionally, selectively removed or modified artifacts may still be recoverable through deeper forensic analysis, though their absence or alteration can complicate timeline reconstruction and attribution.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [CSPY Downloader](../../tools/unknown/cspy-downloader.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) has the ability to remove values it writes to the Registry.(Citation: Cybereason Kimsuky November 2020) |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can erase file references to payloads in-memory after being reflectively loaded and executed.(Citation: Donut Github) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can clean saved cookies and logins from the web browser.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can remove artifacts from the compromised host, including created Registry keys.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [Update.exe](../../tools/windows/update.exe.md) | explicit | source | Command metadata lists T1070: Update.exe --removeShortcut={PATH:.exe}-l=Startup |

## Source Verification

[source record](../../sources/mitre/indicator-removal.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:55.892Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and
blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that
appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal
system behavior.
Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user
or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific,
```
