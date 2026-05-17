---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Instance Metadata API

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Instance Metadata API](../../attack/techniques/T1552.005-cloud-instance-metadata-api.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1552.005 |
| name | Cloud Instance Metadata API |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1552/005 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:47:46.619Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to access the Cloud Instance Metadata API to collect credentials and other sensitive
  data.


  Most cloud service providers support a Cloud Instance Metadata API which is a service provided to running virtual instances
  that allows applications to access information about the running virtual instance. Available information generally includes
  name, security group, and additional metadata including sensitive data such as credentials and UserData scripts that may
  contain additional secrets. The Instance Metadata API is provided as a convenience to assist in managing applications and
  is accessible by anyone who can access the instance.(Citation: AWS Instance Metadata API) A cloud metadata API has been
  used in at least one high profile compromise.(Citation: Krebs Capital One August 2019)


  If adversaries have a presence on the running virtual instance, they may query the Instance Metadata API directly to identify
  credentials that grant access to additional resources. Additionally, adversaries may exploit a Server-Side Request Forgery
  (SSRF) vulnerability in a public facing web proxy that allows them to gain access to the sensitive information via a request
  to the Instance Metadata API.(Citation: RedLock Instance Metadata API 2018)


  The de facto standard across cloud service providers is to host the Instance Metadata API at <code>http[:]//169.254.169.254</code>.

  '
external_references:
- external_id: T1552.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1552/005
- description: AWS. (n.d.). Instance Metadata and User Data. Retrieved July 18, 2019.
  source_name: AWS Instance Metadata API
  url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
- description: 'Higashi, Michael. (2018, May 15). Instance Metadata API: A Modern Day Trojan Horse. Retrieved July 16, 2019.'
  source_name: RedLock Instance Metadata API 2018
  url: https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse
- description: Krebs, B.. (2019, August 19). What We Can Learn from the Capital One Hack. Retrieved March 25, 2020.
  source_name: Krebs Capital One August 2019
  url: https://krebsonsecurity.com/2019/08/what-we-can-learn-from-the-capital-one-hack/
id: attack-pattern--19bf235b-8620-4997-b5b4-94e0659ed7c3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:27.965Z'
name: Cloud Instance Metadata API
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '1.4'
```
