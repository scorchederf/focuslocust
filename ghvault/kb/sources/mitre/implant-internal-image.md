---
parsed_by: focuslocust
source: mitre
type: generated
---
# Implant Internal Image

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1525` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Implant Internal Image](../../attack/techniques/T1525-implant-internal-image.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1525 |
| name | Implant Internal Image |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1525 |

## Preserved Source Material

```yaml
created: '2019-09-04T12:04:03.552Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may implant cloud or container images with malicious code to establish persistence after gaining
  access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and
  Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike [Upload Malware](https://attack.mitre.org/techniques/T1608/001),
  this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how
  the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed
  to always use the latest image.(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)


  A tool has been developed to facilitate planting backdoors in cloud container images.(Citation: Rhino Labs Cloud Backdoor
  September 2019) If an adversary has access to a compromised AWS instance, and permissions to list the available container
  images, they may implant a backdoor such as a [Web Shell](https://attack.mitre.org/techniques/T1505/003).(Citation: Rhino
  Labs Cloud Image Backdoor Technique Sept 2019)'
external_references:
- external_id: T1525
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1525
- description: Rhino Labs. (2019, August). Exploiting AWS ECR and ECS with the Cloud Container Attack Tool (CCAT). Retrieved
    September 12, 2019.
  source_name: Rhino Labs Cloud Image Backdoor Technique Sept 2019
  url: https://rhinosecuritylabs.com/aws/cloud-container-attack-tool/
- description: Rhino Labs. (2019, September). Cloud Container Attack Tool (CCAT). Retrieved September 12, 2019.
  source_name: Rhino Labs Cloud Backdoor September 2019
  url: https://github.com/RhinoSecurityLabs/ccat
id: attack-pattern--4fd8a28b-4b3a-4cd6-a8cf-85ba5f824a7f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:48:45.786Z'
name: Implant Internal Image
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Yossi Weizman, Azure Defender Research Team
- Vishwas Manral, McAfee
- Praetorian
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Containers
x_mitre_version: '2.2'
```
