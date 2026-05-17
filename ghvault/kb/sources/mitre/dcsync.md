---
parsed_by: focuslocust
source: mitre
type: generated
---
# DCSync

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1003.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DCSync](../../attack/techniques/T1003.006-dcsync.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1003.006 |
| name | DCSync |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1003/006 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:45:34.293Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to access credentials and other sensitive information by abusing a Windows Domain Controller''s
  application programming interface (API)(Citation: Microsoft DRSR Dec 2017) (Citation: Microsoft GetNCCChanges) (Citation:
  Samba DRSUAPI) (Citation: Wine API samlib.dll) to simulate the replication process from a remote domain controller using
  a technique called DCSync.


  Members of the Administrators, Domain Admins, and Enterprise Admin groups or computer accounts on the domain controller
  are able to run DCSync to pull password data(Citation: ADSecurity Mimikatz DCSync) from Active Directory, which may include
  current and historical hashes of potentially useful accounts such as KRBTGT and Administrators. The hashes can then in turn
  be used to create a [Golden Ticket](https://attack.mitre.org/techniques/T1558/001) for use in [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003)(Citation:
  Harmj0y Mimikatz and DCSync) or change an account''s password as noted in [Account Manipulation](https://attack.mitre.org/techniques/T1098).(Citation:
  InsiderThreat ChangeNTLM July 2017)


  DCSync functionality has been included in the "lsadump" module in [Mimikatz](https://attack.mitre.org/software/S0002).(Citation:
  GitHub Mimikatz lsadump Module) Lsadump also includes NetSync, which performs DCSync over a legacy replication protocol.(Citation:
  Microsoft NRPC Dec 2017)'
external_references:
- external_id: T1003.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1003/006
- description: Deply, B., Le Toux, V. (2016, June 5). module ~ lsadump. Retrieved August 7, 2017.
  source_name: GitHub Mimikatz lsadump Module
  url: https://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump
- description: Metcalf, S. (2015, September 25). Mimikatz DCSync Usage, Exploitation, and Detection. Retrieved August 7, 2017.
  source_name: ADSecurity Mimikatz DCSync
  url: https://adsecurity.org/?p=1729
- description: Metcalf, S. (2015, September 25). Mimikatz DCSync Usage, Exploitation, and Detection. Retrieved December 4,
    2017.
  source_name: AdSecurity DCSync Sept 2015
  url: https://adsecurity.org/?p=1729
- description: Microsoft. (2017, December 1). MS-DRSR Directory Replication Service (DRS) Remote Protocol. Retrieved December
    4, 2017.
  source_name: Microsoft DRSR Dec 2017
  url: https://msdn.microsoft.com/library/cc228086.aspx
- description: Microsoft. (2017, December 1). MS-NRPC - Netlogon Remote Protocol. Retrieved December 6, 2017.
  source_name: Microsoft NRPC Dec 2017
  url: https://msdn.microsoft.com/library/cc237008.aspx
- description: Microsoft. (n.d.). IDL_DRSGetNCChanges (Opnum 3). Retrieved December 4, 2017.
  source_name: Microsoft GetNCCChanges
  url: https://msdn.microsoft.com/library/dd207691.aspx
- description: Microsoft. (n.d.). MS-SAMR Security Account Manager (SAM) Remote Protocol (Client-to-Server) - Transport. Retrieved
    December 4, 2017.
  source_name: Microsoft SAMR
  url: https://msdn.microsoft.com/library/cc245496.aspx
- description: SambaWiki. (n.d.). DRSUAPI. Retrieved December 4, 2017.
  source_name: Samba DRSUAPI
  url: https://wiki.samba.org/index.php/DRSUAPI
- description: Schroeder, W. (2015, September 22). Mimikatz and DCSync and ExtraSids, Oh My. Retrieved December 4, 2017.
  source_name: Harmj0y DCSync Sept 2015
  url: http://www.harmj0y.net/blog/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/
- description: Schroeder, W. (2015, September 22). Mimikatz and DCSync and ExtraSids, Oh My. Retrieved September 23, 2024.
  source_name: Harmj0y Mimikatz and DCSync
  url: https://blog.harmj0y.net/redteaming/mimikatz-and-dcsync-and-extrasids-oh-my/
- description: Warren, J. (2017, July 11). Manipulating User Passwords with Mimikatz. Retrieved December 4, 2017.
  source_name: InsiderThreat ChangeNTLM July 2017
  url: https://blog.stealthbits.com/manipulating-user-passwords-with-mimikatz-SetNTLM-ChangeNTLM
- description: Wine API. (n.d.). samlib.dll. Retrieved November 17, 2024.
  source_name: Wine API samlib.dll
  url: https://strontic.github.io/xcyclopedia/library/samlib.dll-0BDF6351009F6EBA5BA7E886F23263B1.html
id: attack-pattern--f303a39a-6255-4b89-aecc-18c4d8ca7163
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:36.308Z'
name: DCSync
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- ExtraHop
- Vincent Le Toux
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.1'
```
