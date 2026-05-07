---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0677
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0677-aadinternals
---

## Description

[[kb/mitre/attack/software/S0677-aadinternals|AADInternals]] is a PowerShell-based framework for administering, enumerating, and exploiting Azure Active Directory. The tool is publicly available on GitHub.[^3] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.004-lsa-secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can dump secrets from the Local Security Authority.[^1]  |
| [[kb/mitre/attack/techniques/T1048-exfiltration-over-alternative-protocol\|T1048]] | Exfiltration Over Alternative Protocol | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can directly download cloud user data such as OneDrive files.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] is written and executed via PowerShell.[^1]  |
| [[kb/mitre/attack/techniques/T1069.003-cloud-groups\|T1069.003]] | Cloud Groups | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can enumerate Azure AD groups.[^1]  |
| [[kb/mitre/attack/techniques/T1087.004-cloud-account\|T1087.004]] | Cloud Account | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can enumerate Azure AD users.[^1]  |
| [[kb/mitre/attack/techniques/T1098.005-device-registration\|T1098.005]] | Device Registration | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can register a device to Azure AD.[^1]  |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can modify registry keys as part of setting a new pass-through authentication agent.[^1]  |
| [[kb/mitre/attack/techniques/T1136.003-cloud-account\|T1136.003]] | Cloud Account | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can create new Azure AD users.[^1]  |
| [[kb/mitre/attack/techniques/T1484.002-trust-modification\|T1484.002]] | Trust Modification | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can create a backdoor by converting a domain to a federated domain which will be able to authenticate any user across the tenant. [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can also modify DesktopSSO information.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1526-cloud-service-discovery\|T1526]] | Cloud Service Discovery | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations.[^1]  |
| [[kb/mitre/attack/techniques/T1528-steal-application-access-token\|T1528]] | Steal Application Access Token | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can steal users’ access tokens via phishing emails containing malicious links.[^1]  |
| [[kb/mitre/attack/techniques/T1530-data-from-cloud-storage\|T1530]] | Data from Cloud Storage | AADInternals can collect files from a user’s OneDrive.[^1]  |
| [[kb/mitre/attack/techniques/T1552.001-credentials-in-files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can gather unsecured credentials for Azure AD services, such as Azure AD Connect, from a local machine.[^1]  |
| [[kb/mitre/attack/techniques/T1552.004-private-keys\|T1552.004]] | Private Keys | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can gather encryption keys from Azure AD services such as ADSync and Active Directory Federated Services servers.[^1]  |
| [[kb/mitre/attack/techniques/T1556.006-multi-factor-authentication\|T1556.006]] | Multi-Factor Authentication | The [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] `Set-AADIntUserMFA` command can be used to disable MFA for a specified user. |
| [[kb/mitre/attack/techniques/T1556.007-hybrid-identity\|T1556.007]] | Hybrid Identity | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can inject a malicious DLL (`PTASpy`) into the `AzureADConnectAuthenticationAgentService` to backdoor Azure AD Pass-Through Authentication.[^1]  |
| [[kb/mitre/attack/techniques/T1558.002-silver-ticket\|T1558.002]] | Silver Ticket | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can be used to forge Kerberos tickets using the password hash of the AZUREADSSOACC account.[^1]  |
| [[kb/mitre/attack/techniques/T1566.002-spearphishing-link\|T1566.002]] | Spearphishing Link | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can send "consent phishing" emails containing malicious links designed to steal users’ access tokens.[^1]  |
| [[kb/mitre/attack/techniques/T1589.002-email-addresses\|T1589.002]] | Email Addresses | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can check for the existence of user email addresses using public Microsoft APIs.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1590.001-domain-properties\|T1590.001]] | Domain Properties | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can gather information about a tenant’s domains using public Microsoft APIs.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1598.003-spearphishing-link\|T1598.003]] | Spearphishing Link | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can send phishing emails containing malicious links designed to collect users’ credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1606.002-saml-tokens\|T1606.002]] | SAML Tokens | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can be used to create SAML tokens using the AD Federated Services token signing certificate.[^1]  |
| [[kb/mitre/attack/techniques/T1649-steal-or-forge-authentication-certificates\|T1649]] | Steal or Forge Authentication Certificates | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can create and export various authentication certificates, including those associated with Azure AD joined/registered devices.[^1]  |
| [[kb/mitre/attack/techniques/T1651-cloud-administration-command\|T1651]] | Cloud Administration Command | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can execute commands on Azure virtual machines using the VM agent.[^1]  |

 [^1]: [AADInternals](https://o365blog.com/aadinternals/)
 [^2]: [AADInternals Documentation](https://o365blog.com/aadinternals)
 [^3]: [AADInternals Github](https://github.com/Gerenios/AADInternals)
 [^4]: [AADInternals Azure AD On-Prem to Cloud](https://o365blog.com/post/on-prem_admin/)
 [^5]: [Azure AD Federation Vulnerability](https://o365blog.com/post/federation-vulnerability/)
 [^6]: [Azure AD Recon](https://o365blog.com/post/just-looking)
 [^7]: [AADInternals Root Access to Azure VMs](https://aadinternals.com/post/azurevms/)
