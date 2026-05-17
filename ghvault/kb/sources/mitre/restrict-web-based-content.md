---
parsed_by: focuslocust
source: mitre
type: generated
---
# Restrict Web-Based Content

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1021` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Restrict Web-Based Content](../../attack/mitigations/M1021-restrict-web-based-content.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1021 |
| name | Restrict Web-Based Content |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1021 |

## Preserved Source Material

```yaml
created: '2019-06-06T20:52:59.206Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Restricting web-based content involves enforcing policies and technologies that limit access to potentially
  malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions,
  script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation
  can be implemented through the following measures:


  Deploy Web Proxy Filtering:


  - Use solutions to filter web traffic based on categories, reputation, and content types.

  - Enforce policies that block unsafe websites or file types at the gateway level.


  Enable DNS-Based Filtering:


  - Implement tools to restrict access to domains associated with malware or phishing campaigns.

  - Use public DNS filtering services to enhance protection.


  Enforce Content Security Policies (CSP):


  - Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin
  requests.


  Control Browser Features:


  - Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting.

  - Enforce policies through tools like Group Policy Management to control browser settings.


  Monitor and Alert on Web-Based Threats:


  - Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity.

  - Configure alerts for access attempts to blocked domains or repeated file download failures.'
external_references:
- external_id: M1021
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1021
id: course-of-action--21da4fd4-27ad-4e9c-b93d-0b9b14d02c96
modified: '2024-12-24T13:40:41.043Z'
name: Restrict Web-Based Content
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.1'
```
