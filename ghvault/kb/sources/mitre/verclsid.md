---
parsed_by: focuslocust
source: mitre
type: generated
---
# Verclsid

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.012` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Verclsid](../../attack/techniques/T1218.012-verclsid.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.012 |
| name | Verclsid |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/012 |

## Preserved Source Material

```yaml
created: '2020-08-10T13:59:38.443Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse verclsid.exe to proxy execution of malicious code. Verclsid.exe is known as the Extension
  CLSID Verification Host and is responsible for verifying each shell extension before they are used by Windows Explorer or
  the Windows Shell.(Citation: WinOSBite verclsid.exe)


  Adversaries may abuse verclsid.exe to execute malicious payloads. This may be achieved by running <code>verclsid.exe /S
  /C {CLSID}</code>, where the file is referenced by a Class ID (CLSID), a unique identification number used to identify COM
  objects. COM payloads executed by verclsid.exe may be able to perform various malicious actions, such as loading and executing
  COM scriptlets (SCT) from remote servers (similar to [Regsvr32](https://attack.mitre.org/techniques/T1218/010)). Since the
  binary may be signed and/or native on Windows systems, proxying execution via verclsid.exe may bypass application control
  solutions that do not account for its potential abuse.(Citation: LOLBAS Verclsid)(Citation: Red Canary Verclsid.exe)(Citation:
  BOHOPS Abusing the COM Registry)(Citation: Nick Tyrer GitHub) '
external_references:
- external_id: T1218.012
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/012
- description: 'BOHOPS. (2018, August 18). Abusing the COM Registry Structure (Part 2): Hijacking & Loading Techniques. Retrieved
    August 10, 2020.'
  source_name: BOHOPS Abusing the COM Registry
  url: https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/
- description: 'Haag, M., Levan, K. (2017, April 6). Old Phishing Attacks Deploy a New Methodology: Verclsid.exe. Retrieved
    August 10, 2020.'
  source_name: Red Canary Verclsid.exe
  url: https://redcanary.com/blog/verclsid-exe-threat-detection/
- description: LOLBAS. (n.d.). Verclsid.exe. Retrieved August 10, 2020.
  source_name: LOLBAS Verclsid
  url: https://lolbas-project.github.io/lolbas/Binaries/Verclsid/
- description: Tyrer, N. (n.d.). Instructions. Retrieved August 10, 2020.
  source_name: Nick Tyrer GitHub
  url: https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5
- description: verclsid-exe. (2019, December 17). verclsid.exe File Information - What is it & How to Block . Retrieved November
    17, 2024.
  source_name: WinOSBite verclsid.exe
  url: https://winosbite.com/verclsid-exe/
id: attack-pattern--808e6329-ca91-4b87-ac2d-8eadc5f8f327
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:42:21.088Z'
name: Verclsid
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Rodrigo Garcia, Red Canary
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
