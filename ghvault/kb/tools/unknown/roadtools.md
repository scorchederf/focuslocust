---
parsed_by: focuslocust
source: mitre
type: generated
---
# ROADTools

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0684` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ROADTools is a framework for enumerating Azure Active Directory environments. The tool is written in Python and publicly available on GitHub.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/roadtools.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD systems and devices.(Citation: Roadtools) |
| [T1069.003 - Cloud Groups](../../attack/techniques/T1069.003-cloud-groups.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD groups.(Citation: Roadtools)	 |
| [T1078.004 - Cloud Accounts](../../attack/techniques/T1078.004-cloud-accounts.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) leverages valid cloud credentials to perform enumeration operations using the internal Azure AD Graph API.(Citation: Roadtools)	 |
| [T1087.004 - Cloud Account](../../attack/techniques/T1087.004-cloud-account.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD users.(Citation: Roadtools) |
| [T1119 - Automated Collection](../../attack/techniques/T1119-automated-collection.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) automatically gathers data from Azure AD environments using the Azure Graph API.(Citation: Roadtools) |
| [T1526 - Cloud Service Discovery](../../attack/techniques/T1526-cloud-service-discovery.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD applications and service principals.(Citation: Roadtools)	 |

## Source Verification

[source record](../../sources/mitre/roadtools.md)

## Evidence Excerpt

```text
created: '2022-02-18T13:29:23.577Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[ROADTools](https://attack.mitre.org/software/S0684) is a framework for enumerating Azure Active Directory environments.
The tool is written in Python and publicly available on GitHub.(Citation: ROADtools Github)'
external_references:
- external_id: S0684
source_name: mitre-attack
url: https://attack.mitre.org/software/S0684
```
