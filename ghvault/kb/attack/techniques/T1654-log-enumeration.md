---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1654 - Log Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1654` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records (Account Discovery), security or vulnerable software (Software Discovery), or hosts within a compromised network (Remote System Discovery).

Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or PowerShell on Windows to access and/or export security event information. In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s `CollectGuestLogs.exe` to collect security logs from cloud hosted infrastructure.

Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis.

In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can collect CloudTrail event histories and CloudWatch logs.(Citation: GitHub Pacu) |

## Source Verification

[source record](../../sources/mitre/log-enumeration.md)

## Evidence Excerpt

```text
created: '2023-07-10T16:50:57.587Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types
of valuable insights for an adversary, such as user authentication records ([Account Discovery](https://attack.mitre.org/techniques/T1087)),
security or vulnerable software ([Software Discovery](https://attack.mitre.org/techniques/T1518)), or hosts within a compromised
network ([Remote System Discovery](https://attack.mitre.org/techniques/T1018)).
Host binaries may be leveraged to collect system logs. Examples include using `wevtutil.exe` or [PowerShell](https://attack.mitre.org/techniques/T1059/001)
on Windows to access and/or export security event information.(Citation: WithSecure Lazarus-NoPineapple Threat Intel Report
```
