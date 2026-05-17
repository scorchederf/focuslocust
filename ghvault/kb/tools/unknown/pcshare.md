---
parsed_by: focuslocust
source: mitre
type: generated
---
# PcShare

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1050` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

PcShare is an open source remote access tool that has been modified and used by Chinese threat actors, most notably during the FunnyDream campaign since late 2018.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/pcshare.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can collect files and information from a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1012 - Query Registry](../../attack/techniques/T1012-query-registry.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can search the registry files of a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1027.013 - Encrypted／Encoded File](../../attack/techniques/T1027.013-encrypted-encoded-file.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has been encrypted with XOR using different 32-long Base16 strings.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1027.015 - Compression](../../attack/techniques/T1027.015-compression.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has been compressed with LZW algorithm.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1036.001 - Invalid Code Signature](../../attack/techniques/T1036.001-invalid-code-signature.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has used an invalid certificate in attempt to appear legitimate.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1036.005 - Match Legitimate Resource Name or Location](../../attack/techniques/T1036.005-match-legitimate-resource-name-or-location.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has been named `wuauclt.exe` to appear as the legitimate Windows Update AutoUpdate Client.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1041 - Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can upload files and information from a compromised host to its C2 servers.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | The [PcShare](https://attack.mitre.org/software/S1050) payload has been injected into the `logagent.exe` and `rdpclip.exe` processes.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has the ability to capture keystrokes.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can obtain a list of running processes on a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can execute `cmd` commands on a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1070.004 - File Deletion](../../attack/techniques/T1070.004-file-deletion.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has deleted its files and components from a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has used HTTP for C2 communication.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has used a variety of Windows API functions.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can delete its persistence mechanisms from the registry.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can take screen shots of a compromised machine.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can capture camera video as part of its collection process.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1140 - Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has used `rundll32.exe` for execution.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [T1546.015 - Component Object Model Hijacking](../../attack/techniques/T1546.015-component-object-model-hijacking.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has created the `HKCU\\Software\\Classes\\CLSID\\{42aedc87-2188-41fd-b9a3-0c966feabec1}\\InprocServer32` Registry key for persistence.(Citation: Bitdefender FunnyDream Campaign November 2020) |

## Source Verification

[source record](../../sources/mitre/pcshare.md)

## Evidence Excerpt

```text
created: '2022-10-13T14:07:52.541Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[PcShare](https://attack.mitre.org/software/S1050) is an open source remote access tool that has been modified
and used by Chinese threat actors, most notably during the FunnyDream campaign since late 2018.(Citation: Bitdefender FunnyDream
Campaign November 2020)(Citation: GitHub PcShare 2014)'
external_references:
- external_id: S1050
source_name: mitre-attack
```
