---
parsed_by: focuslocust
source: mitre
type: generated
---
# Rootkit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1014` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Rootkit](../../attack/techniques/T1014-rootkit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1014 |
| name | Rootkit |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1014 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:26.496Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers,\
  \ and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying\
  \ operating system API calls that supply system information. (Citation: Symantec Windows Rootkits) \n\nRootkits or rootkit\
  \ enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor\
  \ or [System Firmware](https://attack.mitre.org/techniques/T1542/001). (Citation: Wikipedia Rootkit) Rootkits have been\
  \ seen for Windows, Linux, and Mac OS X systems. (Citation: CrowdStrike Linux Rootkit) (Citation: BlackHat Mac OSX Rootkit)\n\
  \nRootkits that reside or modify boot sectors are known as [Bootkit](https://attack.mitre.org/techniques/T1542/003)s and\
  \ specifically target the boot process of the operating system."
external_references:
- external_id: T1014
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1014
- description: Kurtz, G. (2012, November 19). HTTP iframe Injecting Linux Rootkit. Retrieved December 21, 2017.
  source_name: CrowdStrike Linux Rootkit
  url: https://www.crowdstrike.com/blog/http-iframe-injecting-linux-rootkit/
- description: 'Pan, M., Tsai, S. (2014). You can’t see me: A Mac OS X Rootkit uses the tricks you haven''t known yet. Retrieved
    December 21, 2017.'
  source_name: BlackHat Mac OSX Rootkit
  url: http://www.blackhat.com/docs/asia-14/materials/Tsai/WP-Asia-14-Tsai-You-Cant-See-Me-A-Mac-OS-X-Rootkit-Uses-The-Tricks-You-Havent-Known-Yet.pdf
- description: Symantec. (n.d.). Windows Rootkit Overview. Retrieved December 21, 2017.
  source_name: Symantec Windows Rootkits
  url: https://www.symantec.com/avcenter/reference/windows.rootkit.overview.pdf
- description: Wikipedia. (2016, June 1). Rootkit. Retrieved June 2, 2016.
  source_name: Wikipedia Rootkit
  url: https://en.wikipedia.org/wiki/Rootkit
id: attack-pattern--0f20e3cb-245b-4a61-8a91-2d93f7cb0e9b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:32:28.874Z'
name: Rootkit
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
