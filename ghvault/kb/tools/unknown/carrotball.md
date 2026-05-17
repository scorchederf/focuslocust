---
parsed_by: focuslocust
source: mitre
type: generated
---
# CARROTBALL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0465` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

CARROTBALL is an FTP downloader utility that has been in use since at least 2019. CARROTBALL has been used as a downloader to install SYSCON.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/carrotball.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [CARROTBALL](https://attack.mitre.org/software/S0465) has used a custom base64 alphabet to decode files.(Citation: Unit 42 CARROTBAT January 2020) |
| [T1071.002 - File Transfer Protocols](../../attack/techniques/T1071.002-file-transfer-protocols.md) | explicit | source | [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to use FTP in C2 communications.(Citation: Unit 42 CARROTBAT January 2020) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to download and install a remote payload.(Citation: Unit 42 CARROTBAT January 2020) |
| [T1204.002 - Malicious File](../../attack/techniques/T1204.002-malicious-file.md) | explicit | source | [CARROTBALL](https://attack.mitre.org/software/S0465) has been executed through users being lured into opening malicious e-mail attachments.(Citation: Unit 42 CARROTBAT January 2020) |

## Source Verification

[source record](../../sources/mitre/carrotball.md)

## Evidence Excerpt

```text
created: '2020-06-02T19:10:29.513Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[CARROTBALL](https://attack.mitre.org/software/S0465) is an FTP downloader utility that has been in use since
at least 2019. [CARROTBALL](https://attack.mitre.org/software/S0465) has been used as a downloader to install [SYSCON](https://attack.mitre.org/software/S0464).(Citation:
Unit 42 CARROTBAT January 2020)'
external_references:
- external_id: S0465
source_name: mitre-attack
```
