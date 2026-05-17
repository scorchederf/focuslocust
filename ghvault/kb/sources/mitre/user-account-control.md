---
parsed_by: focuslocust
source: mitre
type: generated
---
# User Account Control

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1052` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [User Account Control](../../attack/mitigations/M1052-user-account-control.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1052 |
| name | User Account Control |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1052 |

## Preserved Source Material

```yaml
created: '2019-06-11T17:14:35.170Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'User Account Control (UAC) is a security feature in Microsoft Windows that prevents unauthorized changes to
  the operating system. UAC prompts users to confirm or provide administrator credentials when an action requires elevated
  privileges. Proper configuration of UAC reduces the risk of privilege escalation attacks. This mitigation can be implemented
  through the following measures:


  Enable UAC Globally:


  - Ensure UAC is enabled through Group Policy by setting `User Account Control: Run all administrators in Admin Approval
  Mode` to `Enabled`.


  Require Credential Prompt:


  - Use Group Policy to configure UAC to prompt for administrative credentials instead of just confirmation (`User Account
  Control: Behavior of the elevation prompt`).


  Restrict Built-in Administrator Account:


  Set `Admin Approval Mode` for the built-in Administrator account to `Enabled` in Group Policy.


  Secure the UAC Prompt:


  - Configure UAC prompts to display on the secure desktop (`User Account Control: Switch to the secure desktop when prompting
  for elevation`).


  Prevent UAC Bypass:


  - Block untrusted applications from triggering UAC prompts by configuring `User Account Control: Only elevate executables
  that are signed and validated`.

  - Use EDR tools to detect and block known UAC bypass techniques.


  Monitor UAC-Related Events:


  - Use Windows Event Viewer to monitor for event ID 4688 (process creation) and look for suspicious processes attempting
  to invoke UAC elevation.


  *Tools for Implementation*


  Built-in Windows Tools:


  - Group Policy Editor: Configure UAC settings centrally for enterprise environments.

  - Registry Editor: Modify UAC-related settings directly, such as `EnableLUA` and `ConsentPromptBehaviorAdmin`.


  Endpoint Security Solutions:


  - Microsoft Defender for Endpoint: Detects and blocks UAC bypass techniques.

  - Sysmon: Logs process creations and monitors UAC elevation attempts for suspicious activity.


  Third-Party Security Tools:


  - Process Monitor (Sysinternals): Tracks real-time processes interacting with UAC.

  - EventSentry: Monitors Windows Event Logs for UAC-related alerts.'
external_references:
- external_id: M1052
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1052
id: course-of-action--2c2ad92a-d710-41ab-a996-1db143bb4808
modified: '2024-12-24T14:26:43.340Z'
name: User Account Control
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
x_mitre_version: '1.2'
```
