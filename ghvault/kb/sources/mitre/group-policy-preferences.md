---
parsed_by: focuslocust
source: mitre
type: generated
---
# Group Policy Preferences

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Group Policy Preferences](../../attack/techniques/T1552.006-group-policy-preferences.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1552.006 |
| name | Group Policy Preferences |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1552/006 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:43:06.253Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that
  allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local
  accounts.(Citation: Microsoft GPP 2016)


  These group policies are stored in SYSVOL on a domain controller. This means that any domain user can view the SYSVOL share
  and decrypt the password (using the AES key that has been made public).(Citation: Microsoft GPP Key)


  The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files:


  * Metasploit’s post exploitation module: <code>post/windows/gather/credentials/gpp</code>

  * Get-GPPPassword(Citation: Obscuresecurity Get-GPPPassword)

  * gpprefdecrypt.py


  On the SYSVOL share, adversaries may use the following command to enumerate potential GPP XML files: <code>dir /s * .xml</code>

  '
external_references:
- external_id: T1552.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1552/006
- description: Campbell, C. (2012, May 24). GPP Password Retrieval with PowerShell. Retrieved April 11, 2018.
  source_name: Obscuresecurity Get-GPPPassword
  url: https://obscuresecurity.blogspot.co.uk/2012/05/gpp-password-retrieval-with-powershell.html
- description: Microsoft. (2016, August 31). Group Policy Preferences. Retrieved March 9, 2020.
  source_name: Microsoft GPP 2016
  url: https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn581922(v%3Dws.11)
- description: Microsoft. (n.d.). 2.2.1.1.4 Password Encryption. Retrieved April 11, 2018.
  source_name: Microsoft GPP Key
  url: https://msdn.microsoft.com/library/cc422924.aspx
- description: Sean Metcalf. (2015, December 28). Finding Passwords in SYSVOL & Exploiting Group Policy Preferences. Retrieved
    February 17, 2020.
  source_name: ADSecurity Finding Passwords in SYSVOL
  url: https://adsecurity.org/?p=2288
id: attack-pattern--8d7bd4f5-3a89-4453-9c82-2c8894d5655e
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:05.282Z'
name: Group Policy Preferences
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.1'
```
