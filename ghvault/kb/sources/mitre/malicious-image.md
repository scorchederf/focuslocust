---
parsed_by: focuslocust
source: mitre
type: generated
---
# Malicious Image

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1204.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Malicious Image](../../attack/techniques/T1204.003-malicious-image.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1204.003 |
| name | Malicious Image |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1204/003 |

## Preserved Source Material

```yaml
created: '2021-03-30T17:20:05.789Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may rely on a user running a malicious image to facilitate execution. Amazon Web Services (AWS)
  Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes
  such as Docker can be backdoored. Backdoored images may be uploaded to a public repository via [Upload Malware](https://attack.mitre.org/techniques/T1608/001),
  and users may then download and deploy an instance or container from the image without realizing the image is malicious,
  thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such
  as code that executes cryptocurrency mining, in the instance or container.(Citation: Summit Route Malicious AMIs)


  Adversaries may also name images a certain way to increase the chance of users mistakenly deploying an instance or container
  from the image (ex: [Match Legitimate Resource Name or Location](https://attack.mitre.org/techniques/T1036/005)).(Citation:
  Aqua Security Cloud Native Threat Report June 2021)'
external_references:
- external_id: T1204.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1204/003
- description: Piper, S.. (2018, September 24). Investigating Malicious AMIs. Retrieved March 30, 2021.
  source_name: Summit Route Malicious AMIs
  url: https://summitroute.com/blog/2018/09/24/investigating_malicious_amis/
- description: Team Nautilus. (2021, June). Attacks in the Wild on the Container Supply Chain and Infrastructure. Retrieved
    August 26, 2021.
  source_name: Aqua Security Cloud Native Threat Report June 2021
  url: https://info.aquasec.com/hubfs/Threat%20reports/AquaSecurity_Cloud_Native_Threat_Report_2021.pdf?utm_campaign=WP%20-%20Jun2021%20Nautilus%202021%20Threat%20Research%20Report&utm_medium=email&_hsmi=132931006&_hsenc=p2ANqtz-_8oopT5Uhqab8B7kE0l3iFo1koirxtyfTehxF7N-EdGYrwk30gfiwp5SiNlW3G0TNKZxUcDkYOtwQ9S6nNVNyEO-Dgrw&utm_content=132931006&utm_source=hs_automation
id: attack-pattern--b0c74ef9-c61e-4986-88cb-78da98a355ec
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:49:13.999Z'
name: Malicious Image
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Center for Threat-Informed Defense (CTID)
- Vishwas Manral, McAfee
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Containers
x_mitre_version: '1.2'
```
