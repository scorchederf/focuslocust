---
parsed_by: focuslocust
source: mitre
type: generated
---
# Credentials in Registry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Credentials in Registry](../../attack/techniques/T1552.002-credentials-in-registry.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1552.002 |
| name | Credentials in Registry |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1552/002 |

## Preserved Source Material

```yaml
created: '2020-02-04T12:58:40.678Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search the Registry on compromised systems for insecurely stored credentials. The Windows Registry
  stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking
  for credentials and passwords that have been stored for use by other programs or services. Sometimes these credentials are
  used for automatic logons.


  Example commands to find Registry keys related to password information: (Citation: Pentestlab Stored Credentials)


  * Local Machine Hive: <code>reg query HKLM /f password /t REG_SZ /s</code>

  * Current User Hive: <code>reg query HKCU /f password /t REG_SZ /s</code>'
external_references:
- external_id: T1552.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1552/002
- description: netbiosX. (2017, April 19). Stored Credentials. Retrieved April 6, 2018.
  source_name: Pentestlab Stored Credentials
  url: https://pentestlab.blog/2017/04/19/stored-credentials/
id: attack-pattern--341e222a-a6e3-4f6f-b69c-831d792b1580
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:37.378Z'
name: Credentials in Registry
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Sudhanshu Chauhan, @Sudhanshu_C
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.2'
```
