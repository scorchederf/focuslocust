---
parsed_by: focuslocust
source: mitre
type: generated
---
# LSA Secrets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1003.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1003.004 |
| name | LSA Secrets |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1003/004 |

## Preserved Source Material

```yaml
created: '2020-02-21T16:22:09.493Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which
  can contain a variety of different credential materials, such as credentials for service accounts.(Citation: Passcape LSA
  Secrets)(Citation: Microsoft AD Admin Tier Model)(Citation: Tilbury Windows Credentials) LSA secrets are stored in the registry
  at <code>HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets</code>. LSA secrets can also be dumped from memory.(Citation: ired Dumping
  LSA Secrets)


  [Reg](https://attack.mitre.org/software/S0075) can be used to extract from the Registry. [Mimikatz](https://attack.mitre.org/software/S0002)
  can be used to extract secrets from memory.(Citation: ired Dumping LSA Secrets)'
external_references:
- external_id: T1003.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1003/004
- description: 'Chad Tilbury. (2017, August 8). 1Windows Credentials: Attack, Mitigation, Defense. Retrieved February 21,
    2020.'
  source_name: Tilbury Windows Credentials
  url: https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf
- description: Mantvydas Baranauskas. (2019, November 16). Dumping LSA Secrets. Retrieved February 21, 2020.
  source_name: ired Dumping LSA Secrets
  url: https://ired.team/offensive-security/credential-access-and-credential-dumping/dumping-lsa-secrets
- description: Microsoft. (2019, February 14). Active Directory administrative tier model. Retrieved February 21, 2020.
  source_name: Microsoft AD Admin Tier Model
  url: https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material?redirectedfrom=MSDN
- description: Passcape. (n.d.). Windows LSA secrets. Retrieved February 21, 2020.
  source_name: Passcape LSA Secrets
  url: https://www.passcape.com/index.php?section=docsys&cmd=details&id=23
- description: PowerSploit. (n.d.). Retrieved December 4, 2014.
  source_name: Powersploit
  url: https://github.com/mattifestation/PowerSploit
id: attack-pattern--1ecfdab8-7d59-4c98-95d4-dc41970f57fc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:29.945Z'
name: LSA Secrets
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Ed Williams, Trustwave, SpiderLabs
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.1'
```
