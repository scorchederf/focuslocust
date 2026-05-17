---
parsed_by: focuslocust
source: mitre
type: generated
---
# Credentials In Files

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1552.001 |
| name | Credentials In Files |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1552/001 |

## Preserved Source Material

```yaml
created: '2020-02-04T12:52:13.006Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials.
  These can be files created by users to store their own credentials, shared credential stores for a group of individuals,
  configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.


  It is possible to extract passwords from backups or saved virtual machines through [OS Credential Dumping](https://attack.mitre.org/techniques/T1003).(Citation:
  CG 2014) Passwords may also be obtained from Group Policy Preferences stored on the Windows Domain Controller.(Citation:
  SRD GPP)


  In cloud and/or containerized environments, authenticated user and service account credentials are often stored in local
  configuration and credential files.(Citation: Unit 42 Hildegard Malware) They may also be found as parameters to deployment
  commands in container logs.(Citation: Unit 42 Unsecured Docker Daemons) In some cases, these files can be copied and reused
  on another machine or the contents can be read and then used to authenticate without needing to copy any files.(Citation:
  Specter Ops - Cloud Credential Storage)'
external_references:
- external_id: T1552.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1552/001
- description: CG. (2014, May 20). Mimikatz Against Virtual Machine Memory Part 1. Retrieved November 12, 2014.
  source_name: CG 2014
  url: http://carnal0wnage.attackresearch.com/2014/05/mimikatz-against-virtual-machine-memory.html
- description: 'Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved
    April 5, 2021.'
  source_name: Unit 42 Hildegard Malware
  url: https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/
- description: Chen, J.. (2020, January 29). Attacker's Tactics and Techniques in Unsecured Docker Daemons Revealed. Retrieved
    March 31, 2021.
  source_name: Unit 42 Unsecured Docker Daemons
  url: https://unit42.paloaltonetworks.com/attackers-tactics-and-techniques-in-unsecured-docker-daemons-revealed/
- description: Maddalena, C.. (2018, September 12). Head in the Clouds. Retrieved October 4, 2019.
  source_name: Specter Ops - Cloud Credential Storage
  url: https://posts.specterops.io/head-in-the-clouds-bd038bb69e48
- description: 'Security Research and Defense. (2014, May 13). MS14-025: An Update for Group Policy Preferences. Retrieved
    January 28, 2015.'
  source_name: SRD GPP
  url: http://blogs.technet.com/b/srd/archive/2014/05/13/ms14-025-an-update-for-group-policy-preferences.aspx
id: attack-pattern--837f9164-50af-4ac0-8219-379d8a74cefc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:03.000Z'
name: Credentials In Files
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Rory McCune, Aqua Security
- Jay Chen, Palo Alto Networks
- Yossi Weizman, Azure Defender Research Team
- Vishwas Manral, McAfee
- Microsoft Threat Intelligence Center (MSTIC)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- IaaS
- Linux
- macOS
- Windows
x_mitre_version: '1.3'
```
