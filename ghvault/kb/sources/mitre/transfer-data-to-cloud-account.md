---
parsed_by: focuslocust
source: mitre
type: generated
---
# Transfer Data to Cloud Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1537` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Transfer Data to Cloud Account](../../attack/techniques/T1537-transfer-data-to-cloud-account.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1537 |
| name | Transfer Data to Cloud Account |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1537 |

## Preserved Source Material

```yaml
created: '2019-08-30T13:03:04.038Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backups
  of cloud environments, to another cloud account they control on the same service.


  A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over
  command and control channels may not be watching for data transfers to another account within the same cloud provider. Such
  transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal
  traffic or avoid data transfers over external network interfaces.(Citation: TLDRSec AWS Attacks)


  Adversaries may also use cloud-native mechanisms to share victim data with adversary-controlled cloud accounts, such as
  creating anonymous file sharing links or, in Azure, a shared access signature (SAS) URI.(Citation: Microsoft Azure Storage
  Shared Access Signature)


  Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate
  accounts.(Citation: DOJ GRU Indictment Jul 2018) '
external_references:
- external_id: T1537
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1537
- description: Amazon Web Services. (n.d.). Share an Amazon EBS snapshot. Retrieved March 2, 2022.
  source_name: AWS EBS Snapshot Sharing
  url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html
- description: Clint Gibler and Scott Piper. (2021, January 4). Lesser Known Techniques for Attacking AWS Environments. Retrieved
    March 4, 2024.
  source_name: TLDRSec AWS Attacks
  url: https://tldrsec.com/p/blog-lesser-known-aws-attacks
- description: Delegate access with a shared access signature. (2019, December 18). Delegate access with a shared access signature.
    Retrieved March 2, 2022.
  source_name: Azure Shared Access Signature
  url: https://docs.microsoft.com/en-us/rest/api/storageservices/delegate-access-with-shared-access-signature
- description: Microsoft Azure. (2021, December 29). Blob snapshots. Retrieved March 2, 2022.
  source_name: Azure Blob Snapshots
  url: https://docs.microsoft.com/en-us/azure/storage/blobs/snapshots-overview
- description: Microsoft. (2023, June 7). Grant limited access to Azure Storage resources using shared access signatures (SAS).
    Retrieved March 4, 2024.
  source_name: Microsoft Azure Storage Shared Access Signature
  url: https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview
- description: Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved
    November 17, 2024.
  source_name: DOJ GRU Indictment Jul 2018
  url: https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf
id: attack-pattern--d4bdbdea-eaec-4071-b4f9-5105e12ea4b6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:27.409Z'
name: Transfer Data to Cloud Account
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
- Darin Smith, Cisco
- ExtraHop
- Gabriel Currie
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Office Suite
- SaaS
x_mitre_version: '1.5'
```
