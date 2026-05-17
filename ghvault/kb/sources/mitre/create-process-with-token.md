---
parsed_by: focuslocust
source: mitre
type: generated
---
# Create Process with Token

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1134.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Create Process with Token](../../attack/techniques/T1134.002-create-process-with-token.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1134.002 |
| name | Create Process with Token |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1134/002 |

## Preserved Source Material

```yaml
created: '2020-02-18T16:48:56.582Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create a new process with an existing token to escalate privileges and bypass access controls.
  Processes can be created with the token and resulting security context of another user using features such as <code>CreateProcessWithTokenW</code>
  and <code>runas</code>.(Citation: Microsoft RunAs)


  Creating processes with a token not associated with the current user may require the credentials of the target user, specific
  privileges to impersonate that user, or access to the token to be used. For example, the token could be duplicated via [Token
  Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) or created via [Make and Impersonate Token](https://attack.mitre.org/techniques/T1134/003)
  before being used to create a process.


  While this technique is distinct from [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001), the techniques
  can be used in conjunction where a token is duplicated and then used to create a new process.'
external_references:
- external_id: T1134.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1134/002
- description: Microsoft. (2016, August 31). Runas. Retrieved October 1, 2021.
  source_name: Microsoft RunAs
  url: https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11)
id: attack-pattern--677569f9-a8b0-459e-ab24-7f18091fa7bf
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:55:37.484Z'
name: Create Process with Token
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Jonny Johnson
- Vadim Khrykov
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
