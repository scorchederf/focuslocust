---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1555 - Credentials from Password Stores

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1555` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may search for common password storage locations to obtain user credentials. Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [LaZagne](../../tools/unknown/lazagne.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from databases, mail, and WiFi across multiple platforms.(Citation: GitHub LaZagne Dec 2018) |
| [Mimikatz](../../tools/unknown/mimikatz.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the credential vault and DPAPI.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)(Citation: Cobalt Strike Manual 4.3 November 2020)	 |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can decrypt passwords stored in the RDCMan configuration file.(Citation: SecureWorks August 2019) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from common FTP clients.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |

## Source Verification

[source record](../../sources/mitre/credentials-from-password-stores.md)

## Evidence Excerpt

```text
created: '2020-02-11T18:48:28.456Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search for common password storage locations to obtain user credentials.(Citation: F-Secure
The Dukes) Passwords are stored in several places on a system, depending on the operating system or application holding
the credentials. There are also specific applications and services that store passwords to make them easier for users to
manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used
to perform lateral movement and access restricted information.'
external_references:
```
