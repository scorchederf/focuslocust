---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1537 - Transfer Data to Cloud Account

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

## Summary

Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backups of cloud environments, to another cloud account they control on the same service.

A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over command and control channels may not be watching for data transfers to another account within the same cloud provider. Such transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal traffic or avoid data transfers over external network interfaces.

Adversaries may also use cloud-native mechanisms to share victim data with adversary-controlled cloud accounts, such as creating anonymous file sharing links or, in Azure, a shared access signature (SAS) URI.

Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate accounts.

## Source Verification

[source record](../../sources/mitre/transfer-data-to-cloud-account.md)

## Evidence Excerpt

```text
created: '2019-08-30T13:03:04.038Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backups
of cloud environments, to another cloud account they control on the same service.
A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over
command and control channels may not be watching for data transfers to another account within the same cloud provider. Such
transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal
traffic or avoid data transfers over external network interfaces.(Citation: TLDRSec AWS Attacks)
```
