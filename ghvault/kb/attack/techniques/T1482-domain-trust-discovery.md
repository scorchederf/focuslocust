---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1482 - Domain Trust Discovery

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

## Summary

Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain. Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct SID-History Injection, Pass the Ticket, and Kerberoasting. Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP. The Windows utility Nltest is known to be used by adversaries to enumerate domain trusts.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AdFind](../../tools/unknown/adfind.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) can gather information about organizational units (OUs) and domain trusts from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Symantec Bumblebee June 2022) |
| [BloodHound](../../tools/unknown/bloodhound.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) has the ability to map domain trusts and identify misconfigurations for potential abuse.(Citation: CrowdStrike BloodHound April 2018) |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use LDAP queries and `nltest /domain_trusts` for domain trust discovery.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has modules for enumerating domain trusts.(Citation: Github PowerShell Empire) |
| [Nltest](../../tools/unknown/nltest.md) | explicit | source | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate trusted domains by using commands such as <code>nltest /domain_trusts</code>.(Citation: Nltest Manual)(Citation: Fortinet TrickBot) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) has modules for enumerating domain trusts.(Citation: GitHub PoshC2) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) has modules such as <code>Get-NetDomainTrust</code> and <code>Get-NetForestTrust</code> to enumerate domain and forest trusts.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [Rubeus](../../tools/unknown/rubeus.md) | explicit | source | [Rubeus](https://attack.mitre.org/software/S1071) can gather information about domain trusts.(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) |
| [dsquery](../../tools/unknown/dsquery.md) | explicit | source | [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on domain trusts with <code>dsquery * -filter "(objectClass=trustedDomain)" -attr *</code>.(Citation: Harmj0y Domain Trusts) |

## Source Verification

[source record](../../sources/mitre/domain-trust-discovery.md)

## Evidence Excerpt

```text
created: '2019-02-14T16:15:05.974Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral
movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow
access to resources based on the authentication procedures of another domain.(Citation: Microsoft Trusts) Domain trusts
allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the
adversary conduct [SID-History Injection](https://attack.mitre.org/techniques/T1134/005), [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003),
and [Kerberoasting](https://attack.mitre.org/techniques/T1558/003).(Citation: AdSecurity Forging Trust Tickets)(Citation:
```
