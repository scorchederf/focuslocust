---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1615 - Group Policy Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1615` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.

Adversaries may use commands such as <code>gpresult</code> or various publicly available PowerShell functions, such as <code>Get-DomainGPO</code> and <code>Get-DomainGPOLocalGroup</code>, to gather information on Group Policy settings. Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. Domain or Tenant Policy Modification) for their benefit.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [BloodHound](../../tools/unknown/bloodhound.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) has the ability to collect local admin information via GPO.(Citation: GitHub Bloodhound) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) includes various modules for enumerating Group Policy.(Citation: Github PowerShell Empire) |

## Source Verification

[source record](../../sources/mitre/group-policy-discovery.md)

## Evidence Excerpt

```text
created: '2021-08-06T13:10:12.916Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security
measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in
the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD).
Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network
path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence
2016)
```
