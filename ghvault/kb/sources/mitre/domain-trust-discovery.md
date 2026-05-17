---
parsed_by: focuslocust
source: mitre
type: generated
---
# Domain Trust Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1482` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1482 |
| name | Domain Trust Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1482 |

## Preserved Source Material

```yaml
created: '2019-02-14T16:15:05.974Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral
  movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow
  access to resources based on the authentication procedures of another domain.(Citation: Microsoft Trusts) Domain trusts
  allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the
  adversary conduct [SID-History Injection](https://attack.mitre.org/techniques/T1134/005), [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003),
  and [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).(Citation: AdSecurity Forging Trust Tickets)(Citation:
  Harmj0y Domain Trusts) Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods,
  and LDAP.(Citation: Harmj0y Domain Trusts) The Windows utility [Nltest](https://attack.mitre.org/software/S0359) is known
  to be used by adversaries to enumerate domain trusts.(Citation: Microsoft Operation Wilysupply)'
external_references:
- external_id: T1482
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1482
- description: Florio, E.. (2017, May 4). Windows Defender ATP thwarts Operation WilySupply software supply chain cyberattack.
    Retrieved February 14, 2019.
  source_name: Microsoft Operation Wilysupply
  url: https://www.microsoft.com/security/blog/2017/05/04/windows-defender-atp-thwarts-operation-wilysupply-software-supply-chain-cyberattack/
- description: Metcalf, S. (2015, July 15). It’s All About Trust – Forging Kerberos Trust Tickets to Spoof Access across Active
    Directory Trusts. Retrieved February 14, 2019.
  source_name: AdSecurity Forging Trust Tickets
  url: https://adsecurity.org/?p=1588
- description: Microsoft. (2009, October 7). Trust Technologies. Retrieved February 14, 2019.
  source_name: Microsoft Trusts
  url: https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759554(v=ws.10)
- description: Microsoft. (n.d.). Domain.GetAllTrustRelationships Method. Retrieved February 14, 2019.
  source_name: Microsoft GetAllTrustRelationships
  url: https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectory.domain.getalltrustrelationships?redirectedfrom=MSDN&view=netframework-4.7.2#System_DirectoryServices_ActiveDirectory_Domain_GetAllTrustRelationships
- description: Schroeder, W. (2017, October 30). A Guide to Attacking Domain Trusts. Retrieved February 14, 2019.
  source_name: Harmj0y Domain Trusts
  url: https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944
id: attack-pattern--767dbf9e-df3f-45cb-8998-4903ab5f80c0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:58.061Z'
name: Domain Trust Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Dave Westgard
- Elia Florio, Microsoft
- Mnemonic
- RedHuntLabs, @redhuntlabs
- ExtraHop
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.2'
```
