---
parsed_by: focuslocust
source: mitre
type: generated
---
# Revert Cloud Instance

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1578.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Revert Cloud Instance](../../attack/techniques/T1578.004-revert-cloud-instance.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1578.004 |
| name | Revert Cloud Instance |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1578/004 |

## Preserved Source Material

```yaml
created: '2020-06-16T18:42:20.734Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt
  to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure,
  this may be accomplished by restoring virtual machine (VM) or data storage snapshots through the cloud management dashboard
  or cloud APIs.


  Another variation of this technique is to utilize temporary storage attached to the compute instance. Most cloud providers
  provide various types of storage including persistent, local, and/or ephemeral, with the ephemeral types often reset upon
  stop/restart of the VM.(Citation: Tech Republic - Restore AWS Snapshots)(Citation: Google - Restore Cloud Snapshot)'
external_references:
- external_id: T1578.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1578/004
- description: Google. (2019, October 7). Restoring and deleting persistent disk snapshots. Retrieved October 8, 2019.
  source_name: Google - Restore Cloud Snapshot
  url: https://cloud.google.com/compute/docs/disks/restore-and-delete-snapshots
- description: Hardiman, N.. (2012, March 20). Backing up and restoring snapshots on Amazon EC2 machines. Retrieved October
    8, 2019.
  source_name: Tech Republic - Restore AWS Snapshots
  url: https://www.techrepublic.com/blog/the-enterprise-cloud/backing-up-and-restoring-snapshots-on-amazon-ec2-machines/
id: attack-pattern--0708ae90-d0eb-4938-9a76-d0fc94f6eec1
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:52.953Z'
name: Revert Cloud Instance
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Netskope
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '2.0'
```
