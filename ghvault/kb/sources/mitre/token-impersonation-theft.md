---
parsed_by: focuslocust
source: mitre
type: generated
---
# Token Impersonation／Theft

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1134.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Token Impersonation／Theft](../../attack/techniques/T1134.001-token-impersonation-theft.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1134.001 |
| name | Token Impersonation／Theft |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1134/001 |

## Preserved Source Material

```yaml
created: '2020-02-18T16:39:06.289Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may duplicate then impersonate another user''s existing token to escalate privileges and bypass
  access controls. For example, an adversary can duplicate an existing token using `DuplicateToken` or `DuplicateTokenEx`.(Citation:
  DuplicateToken function) The token can then be used with `ImpersonateLoggedOnUser` to allow the calling thread to impersonate
  a logged on user''s security context, or with `SetThreadToken` to assign the impersonated token to a thread.


  An adversary may perform [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) when they have a specific,
  existing process they want to assign the duplicated token to. For example, this may be useful for when the target user has
  a non-network logon session on the system.


  When an adversary would instead use a duplicated token to create a new process rather than attaching to an existing process,
  they can additionally [Create Process with Token](https://attack.mitre.org/techniques/T1134/002) using `CreateProcessWithTokenW`
  or `CreateProcessAsUserW`. [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) is also distinct from
  [Make and Impersonate Token](https://attack.mitre.org/techniques/T1134/003) in that it refers to duplicating an existing
  token, rather than creating a new one.'
external_references:
- external_id: T1134.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1134/001
- description: Microsoft. (2021, October 12). DuplicateToken function (securitybaseapi.h). Retrieved January 8, 2024.
  source_name: DuplicateToken function
  url: https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetoken
id: attack-pattern--86850eff-2729-40c3-b85e-c4af26da4a2d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:54:20.663Z'
name: Token Impersonation/Theft
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Jonny Johnson
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
