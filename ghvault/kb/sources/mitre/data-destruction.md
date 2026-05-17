---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data Destruction

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1485` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data Destruction](../../attack/techniques/T1485-data-destruction.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1485 |
| name | Data Destruction |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1485 |

## Preserved Source Material

```yaml
created: '2019-03-14T18:47:17.701Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability
  to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic
  techniques through overwriting files or data on local and remote drives.(Citation: Symantec Shamoon 2012)(Citation: FireEye
  Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3
  2018)(Citation: Talos Olympic Destroyer 2018) Common operating system file deletion commands such as <code>del</code> and
  <code>rm</code> often only remove pointers to files without wiping the contents of the files themselves, making the files
  recoverable by proper forensic methodology. This behavior is distinct from [Disk Content Wipe](https://attack.mitre.org/techniques/T1561/001)
  and [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) because individual files are destroyed rather than
  sections of a storage disk or the disk''s logical structure.


  Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.(Citation:
  Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) In some cases politically oriented image files have been used
  to overwrite data.(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill
  2017)


  To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware
  designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques
  like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003),
  and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Symantec Shamoon 2012)(Citation:
  FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Talos Olympic
  Destroyer 2018).


  In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances,
  and other infrastructure crucial to operations to damage an organization or their customers.(Citation: Data Destruction
  - Threat Post)(Citation: DOJ  - Cisco Insider) Similarly, they may delete virtual machines from on-prem virtualized environments.'
external_references:
- external_id: T1485
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1485
- description: DOJ. (2020, August 26). San Jose Man Pleads Guilty To Damaging Cisco’s Network. Retrieved December 15, 2020.
  source_name: DOJ  - Cisco Insider
  url: https://www.justice.gov/usao-ndca/pr/san-jose-man-pleads-guilty-damaging-cisco-s-network
- description: Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.
  source_name: Unit 42 Shamoon3 2018
  url: https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/
- description: 'Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.'
  source_name: Palo Alto Shamoon Nov 2016
  url: http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/
- description: FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved
    November 17, 2024.
  source_name: FireEye Shamoon Nov 2016
  url: https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html
- description: 'Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond.
    Retrieved March 14, 2019.'
  source_name: Kaspersky StoneDrill 2017
  url: https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf
- description: Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved
    March 14, 2019.
  source_name: Talos Olympic Destroyer 2018
  url: https://blog.talosintelligence.com/2018/02/olympic-destroyer.html
- description: Mimoso, M.. (2014, June 18). Hacker Puts Hosting Service Code Spaces Out of Business. Retrieved December 15,
    2020.
  source_name: Data Destruction - Threat Post
  url: https://threatpost.com/hacker-puts-hosting-service-code-spaces-out-of-business/106761/
- description: Symantec. (2012, August 16). The Shamoon Attacks. Retrieved March 14, 2019.
  source_name: Symantec Shamoon 2012
  url: https://www.symantec.com/connect/blogs/shamoon-attacks
id: attack-pattern--d45a3d09-b3cf-48f4-9f0f-f521ee5cb05c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-10-24T17:49:27.149Z'
name: Data Destruction
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Brent Murphy, Elastic
- David French, Elastic
- Syed Ummar Farooqh, McAfee
- Prasad Somasamudram, McAfee
- Sekhar Sarukkai, McAfee
- Varonis Threat Labs
- Joey Lei
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- IaaS
- Linux
- macOS
- Windows
x_mitre_version: '1.4'
```
