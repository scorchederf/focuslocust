---
parsed_by: focuslocust
source: mitre
type: generated
---
# Regsvcs／Regasm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Regsvcs／Regasm](../../attack/techniques/T1218.009-regsvcs-regasm.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.009 |
| name | Regsvcs／Regasm |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/009 |

## Preserved Source Material

```yaml
created: '2020-01-23T19:42:16.439Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Regsvcs and Regasm to proxy execution of code through a trusted Windows utility. Regsvcs
  and Regasm are Windows command-line utilities that are used to register .NET [Component Object Model](https://attack.mitre.org/techniques/T1559/001)
  (COM) assemblies. Both are binaries that may be digitally signed by Microsoft. (Citation: MSDN Regsvcs) (Citation: MSDN
  Regasm)


  Both utilities may be used to bypass application control through use of attributes within the binary to specify code that
  should be run before registration or unregistration: <code>[ComRegisterFunction]</code> or <code>[ComUnregisterFunction]</code>
  respectively. The code with the registration and unregistration attributes will be executed even if the process is run under
  insufficient privileges and fails to execute. (Citation: LOLBAS Regsvcs)(Citation: LOLBAS Regasm)'
external_references:
- external_id: T1218.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/009
- description: LOLBAS. (n.d.). Regasm.exe. Retrieved July 31, 2019.
  source_name: LOLBAS Regasm
  url: https://lolbas-project.github.io/lolbas/Binaries/Regasm/
- description: LOLBAS. (n.d.). Regsvcs.exe. Retrieved July 31, 2019.
  source_name: LOLBAS Regsvcs
  url: https://lolbas-project.github.io/lolbas/Binaries/Regsvcs/
- description: Microsoft. (n.d.). Regasm.exe (Assembly Registration Tool). Retrieved July 1, 2016.
  source_name: MSDN Regasm
  url: https://msdn.microsoft.com/en-us/library/tzat5yw6.aspx
- description: Microsoft. (n.d.). Regsvcs.exe (.NET Services Installation Tool). Retrieved July 1, 2016.
  source_name: MSDN Regsvcs
  url: https://msdn.microsoft.com/en-us/library/04za0hca.aspx
id: attack-pattern--c48a67ee-b657-45c1-91bf-6cdbe27205f8
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:41:42.115Z'
name: Regsvcs/Regasm
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Casey Smith
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
