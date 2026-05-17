---
parsed_by: focuslocust
source: mitre
type: generated
---
# Access Token Manipulation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1134` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Access Token Manipulation](../../attack/techniques/T1134-access-token-manipulation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1134 |
| name | Access Token Manipulation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1134 |

## Preserved Source Material

```yaml
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify access tokens to operate under a different user or system security context to perform
  actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can
  manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to
  someone other than the user that started the process. When this occurs, the process also takes on the security context associated
  with the new token.


  An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token
  stealing. These token can then be applied to an existing process (i.e. [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001))
  or used to spawn a new process (i.e. [Create Process with Token](https://attack.mitre.org/techniques/T1134/002)). An adversary
  must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token
  stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a
  token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the
  remote system.(Citation: Pentestlab Token Manipulation)


  Any standard user can use the <code>runas</code> command, and the Windows API functions, to create impersonation tokens;
  it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields,
  that can be used to modify access tokens.'
external_references:
- external_id: T1134
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1134
- description: netbiosX. (2017, April 3). Token Manipulation. Retrieved April 21, 2017.
  source_name: Pentestlab Token Manipulation
  url: https://pentestlab.blog/2017/04/03/token-manipulation/
id: attack-pattern--dcaa092b-7de9-4a21-977f-7fcb77e89c48
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:53:44.334Z'
name: Access Token Manipulation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Tom Ueltschi @c_APT_ure
- Travis Smith, Tripwire
- Robby Winchester, @robwinchester3
- Jared Atkinson, @jaredcatkinson
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
