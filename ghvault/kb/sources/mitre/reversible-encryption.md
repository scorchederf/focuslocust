---
parsed_by: focuslocust
source: mitre
type: generated
---
# Reversible Encryption

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1556.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reversible Encryption](../../attack/techniques/T1556.005-reversible-encryption.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1556.005 |
| name | Reversible Encryption |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1556/005 |

## Preserved Source Material

```yaml
created: '2022-01-13T20:02:28.349Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may abuse Active Directory authentication encryption properties to gain access to credentials on
  Windows systems. The <code>AllowReversiblePasswordEncryption</code> property specifies whether reversible password encryption
  for an account is enabled or disabled. By default this property is disabled (instead storing user credentials as the output
  of one-way hashing functions) and should not be enabled unless legacy or other software require it.(Citation: store_pwd_rev_enc)


  If the property is enabled and/or a user changes their password after it is enabled, an adversary may be able to obtain
  the plaintext of passwords created/changed after the property was enabled. To decrypt the passwords, an adversary needs
  four components:


  1. Encrypted password (<code>G$RADIUSCHAP</code>) from the Active Directory user-structure <code>userParameters</code>

  2. 16 byte randomly-generated value (<code>G$RADIUSCHAPKEY</code>) also from <code>userParameters</code>

  3. Global LSA secret (<code>G$MSRADIUSCHAPKEY</code>)

  4. Static key hardcoded in the Remote Access Subauthentication DLL (<code>RASSFM.DLL</code>)


  With this information, an adversary may be able to reproduce the encryption key and subsequently decrypt the encrypted password
  value.(Citation: how_pwd_rev_enc_1)(Citation: how_pwd_rev_enc_2)


  An adversary may set this property at various scopes through Local Group Policy Editor, user properties, Fine-Grained Password
  Policy (FGPP), or via the ActiveDirectory [PowerShell](https://attack.mitre.org/techniques/T1059/001) module. For example,
  an adversary may implement and apply a FGPP to users or groups if the Domain Functional Level is set to "Windows Server
  2008" or higher.(Citation: dump_pwd_dcsync) In PowerShell, an adversary may make associated changes to user settings using
  commands similar to <code>Set-ADUser -AllowReversiblePasswordEncryption $true</code>.'
external_references:
- external_id: T1556.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1556/005
- description: Metcalf, S. (2015, November 22). Dump Clear-Text Passwords for All Admins in the Domain Using Mimikatz DCSync.
    Retrieved November 15, 2021.
  source_name: dump_pwd_dcsync
  url: https://adsecurity.org/?p=2053
- description: Microsoft. (2021, October 28). Store passwords using reversible encryption. Retrieved January 3, 2022.
  source_name: store_pwd_rev_enc
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption
- description: 'Teusink, N. (2009, August 25). Passwords stored using reversible encryption: how it works (part 1). Retrieved
    November 17, 2021.'
  source_name: how_pwd_rev_enc_1
  url: http://blog.teusink.net/2009/08/passwords-stored-using-reversible.html
- description: 'Teusink, N. (2009, August 26). Passwords stored using reversible encryption: how it works (part 2). Retrieved
    November 17, 2021.'
  source_name: how_pwd_rev_enc_2
  url: http://blog.teusink.net/2009/08/passwords-stored-using-reversible_26.html
id: attack-pattern--d50955c2-272d-4ac8-95da-10c29dda1c48
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2026-04-16T20:07:53.082Z'
name: Reversible Encryption
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
