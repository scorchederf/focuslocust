---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1560 - Archive Collected Data

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1560` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network. Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [BloodHound](../../tools/unknown/bloodhound.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk.(Citation: GitHub Bloodhound)(Citation: Trend Micro Black Basta October 2022) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can ZIP directories on the target system.(Citation: Github PowerShell Empire) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) used LZ compression to compress initial reconnaissance reports before sending to the C2.(Citation: FOX-IT May 2016 Mofang)	 |

## Source Verification

[source record](../../sources/mitre/archive-collected-data.md)

## Evidence Excerpt

```text
created: '2020-02-20T20:53:45.725Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data
can help to obfuscate the collected data and minimize the amount of data sent over the network.(Citation: DOJ GRU Indictment
Jul 2018) Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less
conspicuous upon inspection by a defender.
Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library,
or custom method.'
```
