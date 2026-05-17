---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1140 - Deobfuscate／Decode Files or Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1140` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use Obfuscated Files or Information to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present on the system.

One such example is the use of certutil to decode a remote access tool portable executable file that has been hidden inside a certificate file. Another example is using the Windows <code>copy /b</code> or <code>type</code> command to reassemble binary fragments into a malicious payload.

Sometimes a user's action may be required to open it for deobfuscation or decryption as part of User Execution. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to deobfuscate its payload prior to execution.(Citation: Palo Alto Brute Ratel July 2022) |
| [Certutil.exe](../../tools/windows/certutil.exe.md) | explicit | source | Command metadata lists T1140: certutil -decodehex {PATH:.hex} {PATH} |
| [Expand](../../tools/unknown/expand.md) | explicit | source | [Expand](https://attack.mitre.org/software/S0361) can be used to decompress a local or remote CAB file into an executable.(Citation: Microsoft Expand Utility) |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has decoded malware components that are then dropped to the system.(Citation: QiAnXin APT-C-36 Feb2019) |
| [IronNetInjector](../../tools/unknown/ironnetinjector.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) has the ability to decrypt embedded .NET and PE payloads.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [certutil](../../tools/unknown/certutil.md) | explicit | source | [certutil](https://attack.mitre.org/software/S0160) has been used to decode binaries hidden inside certificate files as Base64 information.(Citation: Malwarebytes Targeted Attack against Saudi Arabia) |

## Source Verification

[source record](../../sources/mitre/deobfuscate-decode-files-or-information.md)

## Evidence Excerpt

```text
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027) to hide artifacts
of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending
on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present
on the system.
One such example is the use of [certutil](https://attack.mitre.org/software/S0160) to decode a remote access tool portable
executable file that has been hidden inside a certificate file.(Citation: Malwarebytes Targeted Attack against Saudi Arabia)
```
