---
parsed_by: focuslocust
source: mitre
type: generated
---
# Application Isolation and Sandboxing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1048` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Application Isolation and Sandboxing](../../attack/mitigations/M1048-application-isolation-and-sandboxing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1048 |
| name | Application Isolation and Sandboxing |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1048 |

## Preserved Source Material

```yaml
created: '2019-06-11T17:06:56.230Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Application Isolation and Sandboxing refers to the technique of restricting the execution of code to a controlled
  and isolated environment (e.g., a virtual environment, container, or sandbox). This method prevents potentially malicious
  code from affecting the rest of the system or network by limiting access to sensitive resources and critical operations.
  The goal is to contain threats and minimize their impact. This mitigation can be implemented through the following measures:


  Browser Sandboxing:


  - Use Case: Implement browser sandboxing to isolate untrusted web content and prevent malicious web pages or scripts from
  accessing sensitive system resources or initiating unauthorized downloads.

  - Implementation: Use browsers with built-in sandboxing features (e.g., Google Chrome, Microsoft Edge) or deploy enhanced
  browser security frameworks that limit the execution scope of active content. Consider controls that monitor or restrict
  script-based file generation and downloads commonly abused in evasion techniques like HTML smuggling.


  Application Virtualization:


  - Use Case: Deploy critical or high-risk applications in a virtualized environment to ensure any compromise does not affect
  the host system.

  - Implementation: Use application virtualization platforms to run applications in isolated environments.


  Email Attachment Sandboxing:


  - Use Case: Route email attachments to a sandbox environment to detect and block malware before delivering emails to end-users.

  - Implementation: Integrate security solutions with sandbox capabilities to analyze email attachments.


  Endpoint Sandboxing:


  - Use Case: Run all downloaded files and applications in a restricted environment to monitor their behavior for malicious
  activity.

  - Implementation: Use endpoint protection tools for sandboxing at the endpoint level.'
external_references:
- external_id: M1048
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1048
id: course-of-action--b9f0c069-abbe-4a07-a245-2481219a1463
modified: '2025-05-09T16:23:40.086Z'
name: Application Isolation and Sandboxing
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
x_mitre_version: '1.3'
```
