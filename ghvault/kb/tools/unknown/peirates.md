---
parsed_by: focuslocust
source: mitre
type: generated
---
# Peirates

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0683` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Peirates is a post-exploitation Kubernetes exploitation framework with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang and publicly available on GitHub.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/peirates.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can initiate a port scan against a given IP address.(Citation: Peirates GitHub) |
| [T1078.004 - Cloud Accounts](../../attack/techniques/T1078.004-cloud-accounts.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can use stolen service account tokens to perform its operations.(Citation: Peirates GitHub) |
| [T1528 - Steal Application Access Token](../../attack/techniques/T1528-steal-application-access-token.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) gathers Kubernetes service account tokens using a variety of techniques.(Citation: Peirates GitHub) |
| [T1530 - Data from Cloud Storage](../../attack/techniques/T1530-data-from-cloud-storage.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3.(Citation: Peirates GitHub) |
| [T1550.001 - Application Access Token](../../attack/techniques/T1550.001-application-access-token.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can use stolen service account tokens to perform its operations. It also enables adversaries to switch between valid service accounts.(Citation: Peirates GitHub) |
| [T1552.005 - Cloud Instance Metadata API](../../attack/techniques/T1552.005-cloud-instance-metadata-api.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can query the query AWS and GCP metadata APIs for secrets.(Citation: Peirates GitHub) |
| [T1552.007 - Container API](../../attack/techniques/T1552.007-container-api.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can query the Kubernetes API for secrets.(Citation: Peirates GitHub) |
| [T1609 - Container Administration Command](../../attack/techniques/T1609-container-administration-command.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can use `kubectl` or the Kubernetes API to run commands.(Citation: Peirates GitHub) |
| [T1610 - Deploy Container](../../attack/techniques/T1610-deploy-container.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can deploy a pod that mounts its node’s root file system, then execute a command to create a reverse shell on the node.(Citation: Peirates GitHub) |
| [T1611 - Escape to Host](../../attack/techniques/T1611-escape-to-host.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can gain a reverse shell on a host node by mounting the Kubernetes hostPath.(Citation: Peirates GitHub) |
| [T1613 - Container and Resource Discovery](../../attack/techniques/T1613-container-and-resource-discovery.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can enumerate Kubernetes pods in a given namespace.(Citation: Peirates GitHub) |
| [T1619 - Cloud Storage Object Discovery](../../attack/techniques/T1619-cloud-storage-object-discovery.md) | explicit | source | [Peirates](https://attack.mitre.org/software/S0683) can list AWS S3 buckets.(Citation: Peirates GitHub) |

## Source Verification

[source record](../../sources/mitre/peirates.md)

## Evidence Excerpt

```text
created: '2022-02-08T16:11:38.528Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Peirates](https://attack.mitre.org/software/S0683) is a post-exploitation Kubernetes exploitation framework
with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang
and publicly available on GitHub.(Citation: Peirates GitHub)'
external_references:
- external_id: S0683
source_name: mitre-attack
```
