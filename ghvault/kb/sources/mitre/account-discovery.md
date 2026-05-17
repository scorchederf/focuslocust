---
parsed_by: focuslocust
source: mitre
type: generated
---
# Account Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1087` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Account Discovery](../../attack/techniques/T1087-account-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1087 |
| name | Account Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1087 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:06.988Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within
  a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on
  behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [Valid Accounts](https://attack.mitre.org/techniques/T1078)).


  Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential
  misconfigurations that leak account names and roles or permissions in the targeted environment.


  For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.(Citation: AWS List
  Users)(Citation: Google Cloud - IAM Servie Accounts List API) On hosts, adversaries can use default [PowerShell](https://attack.mitre.org/techniques/T1059/001)
  and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted
  by searching an infected system’s files.'
external_references:
- external_id: T1087
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1087
- description: Amazon. (n.d.). List Users. Retrieved August 11, 2020.
  source_name: AWS List Users
  url: https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html
- description: Google. (2020, June 23). gcloud iam service-accounts list. Retrieved August 4, 2020.
  source_name: Google Cloud - IAM Servie Accounts List API
  url: https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list
- description: 'Stepanic, D.. (2020, January 13). Embracing offensive tooling: Building detections against Koadic using EQL.
    Retrieved November 17, 2024.'
  source_name: Elastic - Koadiac Detection with EQL
  url: https://www.elastic.co/security-labs/embracing-offensive-tooling-building-detections-against-koadic-using-eql
id: attack-pattern--72b74d71-8169-42aa-92e0-e7b04b9f5a08
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:57.239Z'
name: Account Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Daniel Stepanic, Elastic
- Microsoft Threat Intelligence Center (MSTIC)
- Travis Smith, Tripwire
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows
x_mitre_version: '2.6'
```
