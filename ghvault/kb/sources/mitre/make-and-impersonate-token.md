---
parsed_by: focuslocust
source: mitre
type: generated
---
# Make and Impersonate Token

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1134.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Make and Impersonate Token](../../attack/techniques/T1134.003-make-and-impersonate-token.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1134.003 |
| name | Make and Impersonate Token |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1134/003 |

## Preserved Source Material

```yaml
created: '2020-02-18T18:03:37.481Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may make new tokens and impersonate users to escalate privileges and bypass access controls. For
  example, if an adversary has a username and password but the user is not logged onto the system the adversary can then create
  a logon session for the user using the `LogonUser` function.(Citation: LogonUserW function) The function will return a copy
  of the new session''s access token and the adversary can use `SetThreadToken` to assign the token to a thread.


  This behavior is distinct from [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) in that this refers
  to creating a new user token instead of stealing or duplicating an existing one.'
external_references:
- external_id: T1134.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1134/003
- description: Microsoft. (2023, March 10). LogonUserW function (winbase.h). Retrieved January 8, 2024.
  source_name: LogonUserW function
  url: https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-logonuserw
id: attack-pattern--8cdeb020-e31e-4f88-a582-f53dcfbda819
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:56:16.233Z'
name: Make and Impersonate Token
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
