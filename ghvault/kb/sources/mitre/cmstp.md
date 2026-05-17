---
parsed_by: focuslocust
source: mitre
type: generated
---
# CMSTP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CMSTP](../../attack/techniques/T1218.003-cmstp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.003 |
| name | CMSTP |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/003 |

## Preserved Source Material

```yaml
created: '2020-01-23T18:27:30.656Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse CMSTP to proxy execution of malicious code. The Microsoft Connection Manager Profile Installer
  (CMSTP.exe) is a command-line program used to install Connection Manager service profiles. (Citation: Microsoft Connection
  Manager Oct 2009) CMSTP.exe accepts an installation information file (INF) as a parameter and installs a service profile
  leveraged for remote access connections.


  Adversaries may supply CMSTP.exe with INF files infected with malicious commands. (Citation: Twitter CMSTP Usage Jan 2018)
  Similar to [Regsvr32](https://attack.mitre.org/techniques/T1218/010) / ”Squiblydoo”, CMSTP.exe may be abused to load and
  execute DLLs (Citation: MSitPros CMSTP Aug 2017)  and/or COM scriptlets (SCT) from remote servers. (Citation: Twitter CMSTP
  Jan 2018) (Citation: GitHub Ultimate AppLocker Bypass List) (Citation: Endurant CMSTP July 2018) This execution may also
  bypass AppLocker and other application control defenses since CMSTP.exe is a legitimate binary that may be signed by Microsoft.


  CMSTP.exe can also be abused to [Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002) and execute
  arbitrary commands from a malicious INF through an auto-elevated COM interface. (Citation: MSitPros CMSTP Aug 2017) (Citation:
  GitHub Ultimate AppLocker Bypass List) (Citation: Endurant CMSTP July 2018)'
external_references:
- external_id: T1218.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/003
- description: Carr, N. (2018, January 31). Here is some early bad cmstp.exe... Retrieved September 12, 2024.
  source_name: Twitter CMSTP Usage Jan 2018
  url: https://x.com/ItsReallyNick/status/958789644165894146
- description: Microsoft. (2009, October 8). How Connection Manager Works. Retrieved April 11, 2018.
  source_name: Microsoft Connection Manager Oct 2009
  url: https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2003/cc786431(v=ws.10)
- description: Moe, O. (2017, August 15). Research on CMSTP.exe. Retrieved April 11, 2018.
  source_name: MSitPros CMSTP Aug 2017
  url: https://msitpros.com/?p=3960
- description: Moe, O. (2018, March 1). Ultimate AppLocker Bypass List. Retrieved April 10, 2018.
  source_name: GitHub Ultimate AppLocker Bypass List
  url: https://github.com/api0cradle/UltimateAppLockerByPassList
- description: Seetharaman, N. (2018, July 7). Detecting CMSTP-Enabled Code Execution and UAC Bypass With Sysmon.. Retrieved
    November 17, 2024.
  source_name: Endurant CMSTP July 2018
  url: https://web.archive.org/web/20190316220149/http://www.endurant.io/cmstp/detecting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/
- description: Tyrer, N. (2018, January 30). CMSTP.exe - remote .sct execution applocker bypass. Retrieved September 12, 2024.
  source_name: Twitter CMSTP Jan 2018
  url: https://x.com/NickTyrer/status/958450014111633408
id: attack-pattern--4cbc6a62-9e34-4f94-8a19-5c1a11392a49
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:37:18.154Z'
name: CMSTP
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Nik Seetharaman, Palantir
- Ye Yint Min Thu Htut, Offensive Security Team, DBS Bank
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
