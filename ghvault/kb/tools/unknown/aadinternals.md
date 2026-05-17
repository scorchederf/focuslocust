---
parsed_by: focuslocust
source: mitre
type: generated
---
# AADInternals

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0677` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

AADInternals is a PowerShell-based framework for administering, enumerating, and exploiting Azure Active Directory. The tool is publicly available on GitHub.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/aadinternals.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.004 - LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can dump secrets from the Local Security Authority.(Citation: AADInternals Documentation) |
| [T1048 - Exfiltration Over Alternative Protocol](../../attack/techniques/T1048-exfiltration-over-alternative-protocol.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can directly download cloud user data such as OneDrive files.(Citation: AADInternals Documentation) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) is written and executed via PowerShell.(Citation: AADInternals Documentation) |
| [T1069.003 - Cloud Groups](../../attack/techniques/T1069.003-cloud-groups.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can enumerate Azure AD groups.(Citation: AADInternals Documentation) |
| [T1087.004 - Cloud Account](../../attack/techniques/T1087.004-cloud-account.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can enumerate Azure AD users.(Citation: AADInternals Documentation) |
| [T1098.005 - Device Registration](../../attack/techniques/T1098.005-device-registration.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can register a device to Azure AD.(Citation: AADInternals Documentation) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can modify registry keys as part of setting a new pass-through authentication agent.(Citation: AADInternals Documentation) |
| [T1136.003 - Cloud Account](../../attack/techniques/T1136.003-cloud-account.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can create new Azure AD users.(Citation: AADInternals Documentation) |
| [T1484.002 - Trust Modification](../../attack/techniques/T1484.002-trust-modification.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can create a backdoor by converting a domain to a federated domain which will be able to authenticate any user across the tenant. [AADInternals](https://attack.mitre.org/software/S0677) can also modify DesktopSSO information.(Citation: AADInternals Documentation)(Citation: Azure AD Federation Vulnerability) |
| [T1526 - Cloud Service Discovery](../../attack/techniques/T1526-cloud-service-discovery.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations.(Citation: AADInternals Documentation) |
| [T1528 - Steal Application Access Token](../../attack/techniques/T1528-steal-application-access-token.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can steal users’ access tokens via phishing emails containing malicious links.(Citation: AADInternals Documentation) |
| [T1530 - Data from Cloud Storage](../../attack/techniques/T1530-data-from-cloud-storage.md) | explicit | source | AADInternals can collect files from a user’s OneDrive.(Citation: AADInternals) |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can gather unsecured credentials for Azure AD services, such as Azure AD Connect, from a local machine.(Citation: AADInternals Documentation) |
| [T1552.004 - Private Keys](../../attack/techniques/T1552.004-private-keys.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can gather encryption keys from Azure AD services such as ADSync and Active Directory Federated Services servers.(Citation: AADInternals Documentation) |
| [T1556.006 - Multi-Factor Authentication](../../attack/techniques/T1556.006-multi-factor-authentication.md) | explicit | source | The [AADInternals](https://attack.mitre.org/software/S0677) `Set-AADIntUserMFA` command can be used to disable MFA for a specified user. |
| [T1556.007 - Hybrid Identity](../../attack/techniques/T1556.007-hybrid-identity.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can inject a malicious DLL (`PTASpy`) into the `AzureADConnectAuthenticationAgentService` to backdoor Azure AD Pass-Through Authentication.(Citation: AADInternals Azure AD On-Prem to Cloud) |
| [T1558.002 - Silver Ticket](../../attack/techniques/T1558.002-silver-ticket.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can be used to forge Kerberos tickets using the password hash of the AZUREADSSOACC account.(Citation: AADInternals Documentation) |
| [T1566.002 - Spearphishing Link](../../attack/techniques/T1566.002-spearphishing-link.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can send "consent phishing" emails containing malicious links designed to steal users’ access tokens.(Citation: AADInternals Documentation) |
| [T1589.002 - Email Addresses](../../attack/techniques/T1589.002-email-addresses.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can check for the existence of user email addresses using public Microsoft APIs.(Citation: AADInternals Documentation)(Citation: Azure AD Recon) |
| [T1590.001 - Domain Properties](../../attack/techniques/T1590.001-domain-properties.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can gather information about a tenant’s domains using public Microsoft APIs.(Citation: AADInternals Documentation)(Citation: Azure AD Recon) |
| [T1598.003 - Spearphishing Link](../../attack/techniques/T1598.003-spearphishing-link.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can send phishing emails containing malicious links designed to collect users’ credentials.(Citation: AADInternals Documentation) |
| [T1606.002 - SAML Tokens](../../attack/techniques/T1606.002-saml-tokens.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can be used to create SAML tokens using the AD Federated Services token signing certificate.(Citation: AADInternals Documentation) |
| [T1649 - Steal or Forge Authentication Certificates](../../attack/techniques/T1649-steal-or-forge-authentication-certificates.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can create and export various authentication certificates, including those associated with Azure AD joined/registered devices.(Citation: AADInternals Documentation) |
| [T1651 - Cloud Administration Command](../../attack/techniques/T1651-cloud-administration-command.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can execute commands on Azure virtual machines using the VM agent.(Citation: AADInternals Root Access to Azure VMs) |

## Source Verification

[source record](../../sources/mitre/aadinternals.md)

## Evidence Excerpt

```text
created: '2022-02-01T15:08:45.007Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[AADInternals](https://attack.mitre.org/software/S0677) is a PowerShell-based framework for administering, enumerating,
and exploiting Azure Active Directory. The tool is publicly available on GitHub.(Citation: AADInternals Github)(Citation:
AADInternals Documentation)'
external_references:
- external_id: S0677
source_name: mitre-attack
```
