---
parsed_by: focuslocust
source: mitre
type: generated
---
# Compiled HTML File

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Compiled HTML File](../../attack/techniques/T1218.001-compiled-html-file.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.001 |
| name | Compiled HTML File |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/001 |

## Preserved Source Material

```yaml
created: '2020-01-23T18:53:54.377Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Compiled HTML files (.chm) to conceal malicious code. CHM files are commonly distributed
  as part of the Microsoft HTML Help system. CHM files are compressed compilations of various content such as HTML documents,
  images, and scripting/web related programming languages such VBA, JScript, Java, and ActiveX. (Citation: Microsoft HTML
  Help May 2018) CHM content is displayed using underlying components of the Internet Explorer browser (Citation: Microsoft
  HTML Help ActiveX) loaded by the HTML Help executable program (hh.exe). (Citation: Microsoft HTML Help Executable Program)


  A custom CHM file containing embedded payloads could be delivered to a victim then triggered by [User Execution](https://attack.mitre.org/techniques/T1204).
  CHM execution may also bypass application application control on older and/or unpatched systems that do not account for
  execution of binaries through hh.exe. (Citation: MsitPros CHM Aug 2017) (Citation: Microsoft CVE-2017-8625 Aug 2017)'
external_references:
- external_id: T1218.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/001
- description: Microsoft. (2017, August 8). CVE-2017-8625 - Internet Explorer Security Feature Bypass Vulnerability. Retrieved
    October 3, 2018.
  source_name: Microsoft CVE-2017-8625 Aug 2017
  url: https://web.archive.org/web/20250419140549/https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2017-8625
- description: Microsoft. (2018, May 30). Microsoft HTML Help 1.4. Retrieved October 3, 2018.
  source_name: Microsoft HTML Help May 2018
  url: https://docs.microsoft.com/previous-versions/windows/desktop/htmlhelp/microsoft-html-help-1-4-sdk
- description: Microsoft. (n.d.). About the HTML Help Executable Program. Retrieved October 3, 2018.
  source_name: Microsoft HTML Help Executable Program
  url: https://msdn.microsoft.com/windows/desktop/ms524405
- description: Microsoft. (n.d.). HTML Help ActiveX Control Overview. Retrieved October 3, 2018.
  source_name: Microsoft HTML Help ActiveX
  url: https://msdn.microsoft.com/windows/desktop/ms644670
- description: Moe, O. (2017, August 13). Bypassing Device guard UMCI using CHM – CVE-2017-8625. Retrieved October 3, 2018.
  source_name: MsitPros CHM Aug 2017
  url: https://oddvar.moe/2017/08/13/bypassing-device-guard-umci-using-chm-cve-2017-8625/
id: attack-pattern--a6937325-9321-4e2e-bb2b-3ed2d40b2a9d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:37:42.151Z'
name: Compiled HTML File
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Rahmat Nurfauzi, @infosecn1nja, PT Xynexis International
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
