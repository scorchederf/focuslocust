---
parsed_by: focuslocust
source: mitre
type: generated
---
# Image Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0015` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Image Creation](../../attack/data-sources/DC0015-image-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0015 |
| name | Image Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0015 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Initial construction of a virtual machine image within a cloud environment. Virtual machine images are templates\
  \ containing an operating system and installed applications, which can be deployed to create new virtual machines. Monitoring\
  \ the creation of these images is important because adversaries may create custom images to include malicious software or\
  \ misconfigurations for later exploitation. Examples: \n\n- Azure Compute Service Image Creation\n    - Example: Creating\
  \ a virtual machine image in Azure using Azure CLI: `az image create --resource-group MyResourceGroup --name MyImage --source\
  \ MyVM`\n- AWS EC2 AMI (Amazon Machine Image) Creation\n    - Example: Creating an AMI from an EC2 instance: `aws ec2 create-image\
  \ --instance-id i-1234567890abcdef0 --name \"MyAMI\" --description \"An AMI for my app\"`\n- Google Cloud Compute Engine\
  \ Image Creation\n    - Example: Creating a custom image using gcloud: `gcloud compute images create my-custom-image --source-disk\
  \ my-disk --source-disk-zone us-central1-a`\n- VMware vSphere\n    - Example: Exporting a VM to create an OVF (Open Virtualization\
  \ Format) template: This could later be imported into other environments with potential tampering."
external_references:
- external_id: DC0015
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0015
id: x-mitre-data-component--b008766d-f34f-4ded-b712-659f59aaed6e
modified: '2025-11-12T22:03:39.105Z'
name: Image Creation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: Image pull from untrusted registry (name NOT IN allowlist) or new digest never seen before
  name: containerd:events
- channel: docker build or docker commit commands followed by docker push to internal registry
  name: docker:daemon
- channel: create
  name: kubernetes:audit
- channel: RegisterImage
  name: AWS:CloudTrail
- channel: docker build or POST /build API request
  name: docker:daemon
- channel: Pod spec triggering build or custom controller activity invoking image builds
  name: kubernetes:apiserver
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
