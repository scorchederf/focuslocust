---
parsed_by: focuslocust
source: mitre
type: generated
---
# BITS Jobs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1197` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [BITS Jobs](../../attack/techniques/T1197-bits-jobs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1197 |
| name | BITS Jobs |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1197 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks. Windows Background
  Intelligent Transfer Service (BITS) is a low-bandwidth, asynchronous file transfer mechanism exposed through [Component
  Object Model](https://attack.mitre.org/techniques/T1559/001) (COM).(Citation: Microsoft COM)(Citation: Microsoft BITS) BITS
  is commonly used by updaters, messengers, and other applications preferred to operate in the background (using available
  idle bandwidth) without interrupting other networked applications. File transfer tasks are implemented as BITS jobs, which
  contain a queue of one or more file operations.


  The interface to create and manage BITS jobs is accessible through [PowerShell](https://attack.mitre.org/techniques/T1059/001)
  and the [BITSAdmin](https://attack.mitre.org/software/S0190) tool.(Citation: Microsoft BITS)(Citation: Microsoft BITSAdmin)


  Adversaries may abuse BITS to download (e.g. [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)), execute,
  and even clean up after running malicious code (e.g. [Indicator Removal](https://attack.mitre.org/techniques/T1070)). BITS
  tasks are self-contained in the BITS job database, without new files or registry modifications, and often permitted by host
  firewalls.(Citation: CTU BITS Malware June 2016)(Citation: Mondok Windows PiggyBack BITS May 2007)(Citation: Symantec BITS
  May 2007) BITS enabled execution may also enable persistence by creating long-standing jobs (the default maximum lifetime
  is 90 days and extendable) or invoking an arbitrary program when a job completes or errors (including after system reboots).(Citation:
  PaloAlto UBoatRAT Nov 2017)(Citation: CTU BITS Malware June 2016)


  BITS upload functionalities can also be used to perform [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048).(Citation:
  CTU BITS Malware June 2016)'
external_references:
- external_id: T1197
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1197
- description: Counter Threat Unit Research Team. (2016, June 6). Malware Lingers with BITS. Retrieved January 12, 2018.
  source_name: CTU BITS Malware June 2016
  url: https://www.secureworks.com/blog/malware-lingers-with-bits
- description: Florio, E. (2007, May 9). Malware Update with Windows Update. Retrieved January 12, 2018.
  source_name: Symantec BITS May 2007
  url: https://www.symantec.com/connect/blogs/malware-update-windows-update
- description: Hayashi, K. (2017, November 28). UBoatRAT Navigates East Asia. Retrieved January 12, 2018.
  source_name: PaloAlto UBoatRAT Nov 2017
  url: https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/
- description: Microsoft. (n.d.). Background Intelligent Transfer Service. Retrieved January 12, 2018.
  source_name: Microsoft BITS
  url: https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx
- description: Microsoft. (n.d.). BITSAdmin Tool. Retrieved January 12, 2018.
  source_name: Microsoft BITSAdmin
  url: https://msdn.microsoft.com/library/aa362813.aspx
- description: Microsoft. (n.d.). Component Object Model (COM). Retrieved November 22, 2017.
  source_name: Microsoft COM
  url: https://msdn.microsoft.com/library/windows/desktop/ms680573.aspx
- description: Mondok, M. (2007, May 11). Malware piggybacks on Windows’ Background Intelligent Transfer Service. Retrieved
    January 12, 2018.
  source_name: Mondok Windows PiggyBack BITS May 2007
  url: https://arstechnica.com/information-technology/2007/05/malware-piggybacks-on-windows-background-intelligent-transfer-service/
id: attack-pattern--c8e87b83-edbb-48d4-9295-4974897525b7
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T19:57:02.003Z'
name: BITS Jobs
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Brent Murphy, Elastic
- David French, Elastic
- Red Canary
- Ricardo Dias
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
