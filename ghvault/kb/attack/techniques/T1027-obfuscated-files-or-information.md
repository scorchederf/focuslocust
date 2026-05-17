---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1027 - Obfuscated Files or Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. 

Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action may be required to open and Deobfuscate/Decode Files or Information for User Execution. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary. Adversaries may also use compressed or archived scripts, such as JavaScript. 

Portions of files can also be encoded to hide the plain-text strings that would otherwise help defenders with discovery. Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.

Adversaries may also abuse Command Obfuscation to obscure commands executed from payloads or directly via Command and Scripting Interpreter. Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature based detections and application control mechanisms.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used encrypted payload files and maintains an encrypted configuration structure in memory.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022) |
| [CARROTBALL](../../tools/unknown/carrotball.md) | explicit | source | [CARROTBALL](https://attack.mitre.org/software/S0465) has used a custom base64 alphabet to decode files.(Citation: Unit 42 CARROTBAT January 2020) |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2.(Citation: QiAnXin APT-C-36 Feb2019) |
| [MCMD](../../tools/unknown/mcmd.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can Base64 encode output strings prior to sending to C2.(Citation: Secureworks MCMD July 2019) |
| [Out1](../../tools/unknown/out1.md) | explicit | source | [Out1](https://attack.mitre.org/software/S0594) has the ability to encode data.(Citation: Trend Micro Muddy Water March 2021) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) uses RC4 and base64 to obfuscate data, including Registry entries and file paths.(Citation: Talos Remcos Aug 2018) [Remcos](https://attack.mitre.org/software/S0332) can also employ control flow flattening to hinder analysis.(Citation: Check Point Blind Eagle MAR 2025) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) encrypted gathered information with a combination of shifting and XOR using a static key.(Citation: FOX-IT May 2016 Mofang) |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.(Citation: Microsoft Sliver 2022) |

## Source Verification

[source record](../../sources/mitre/obfuscated-files-or-information.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:32.662Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding,\
\ or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different\
\ platforms and the network to evade defenses. \n\nPayloads may be compressed, archived, or encrypted in order to avoid\
\ detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action\
\ may be required to open and [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) for [User\
\ Execution](https://attack.mitre.org/techniques/T1204). The user may also be required to input a password to open a password\
```
