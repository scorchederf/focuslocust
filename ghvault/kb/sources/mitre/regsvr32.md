---
parsed_by: focuslocust
source: mitre
type: generated
---
# Regsvr32

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.010` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Regsvr32](../../attack/techniques/T1218.010-regsvr32.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.010 |
| name | Regsvr32 |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/010 |

## Preserved Source Material

```yaml
created: '2020-01-23T19:52:17.414Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Regsvr32.exe to proxy execution of malicious code. Regsvr32.exe is a command-line program
  used to register and unregister object linking and embedding controls, including dynamic link libraries (DLLs), on Windows
  systems. The Regsvr32.exe binary may also be signed by Microsoft. (Citation: Microsoft Regsvr32)


  Malicious usage of Regsvr32.exe may avoid triggering security tools that may not monitor execution of, and modules loaded
  by, the regsvr32.exe process because of allowlists or false positives from Windows using regsvr32.exe for normal operations.
  Regsvr32.exe can also be used to specifically bypass application control using functionality to load COM scriptlets to execute
  DLLs under user permissions. Since Regsvr32.exe is network and proxy aware, the scripts can be loaded by passing a uniform
  resource locator (URL) to file on an external Web server as an argument during invocation. This method makes no changes
  to the Registry as the COM object is not actually registered, only executed. (Citation: LOLBAS Regsvr32) This variation
  of the technique is often referred to as a "Squiblydoo" and has been used in campaigns targeting governments. (Citation:
  Carbon Black Squiblydoo Apr 2016) (Citation: FireEye Regsvr32 Targeting Mongolian Gov)


  Regsvr32.exe can also be leveraged to register a COM Object used to establish persistence via [Component Object Model Hijacking](https://attack.mitre.org/techniques/T1546/015).
  (Citation: Carbon Black Squiblydoo Apr 2016)'
external_references:
- external_id: T1218.010
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/010
- description: Anubhav, A., Kizhakkinan, D. (2017, February 22). Spear Phishing Techniques Used in Attacks Targeting the Mongolian
    Government. Retrieved February 24, 2017.
  source_name: FireEye Regsvr32 Targeting Mongolian Gov
  url: https://www.fireeye.com/blog/threat-research/2017/02/spear_phishing_techn.html
- description: LOLBAS. (n.d.). Regsvr32.exe. Retrieved July 31, 2019.
  source_name: LOLBAS Regsvr32
  url: https://lolbas-project.github.io/lolbas/Binaries/Regsvr32/
- description: Microsoft. (2015, August 14). How to use the Regsvr32 tool and troubleshoot Regsvr32 error messages. Retrieved
    June 22, 2016.
  source_name: Microsoft Regsvr32
  url: https://support.microsoft.com/en-us/kb/249873
- description: 'Nolen, R. et al.. (2016, April 28). Threat Advisory: “Squiblydoo” Continues Trend of Attackers Using Native
    OS Tools to “Live off the Land”. Retrieved April 9, 2018.'
  source_name: Carbon Black Squiblydoo Apr 2016
  url: https://www.carbonblack.com/2016/04/28/threat-advisory-squiblydoo-continues-trend-of-attackers-using-native-os-tools-to-live-off-the-land/
id: attack-pattern--b97f1d35-4249-4486-a6b5-ee60ccf24fab
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:41:58.327Z'
name: Regsvr32
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Casey Smith
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
