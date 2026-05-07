---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1649
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1649-steal-or-forge-authentication-certificates
tactic:
    - Credential Access
platforms:
    - Windows
    - Linux
    - macOS
    - Identity Provider
permissions required:
    - none
---

## Description

Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material. For example, Entra ID device certificates and Active Directory Certificate Services (AD CS) certificates bind to an identity and can be used as credentials for domain accounts.[^5] [^2] <br><br>Authentication certificates can be both stolen and forged. For example, AD CS certificates can be stolen from encrypted storage (in the Registry or files)[^7] , misplaced certificate files (i.e. [[kb/mitre/attack/techniques/T1552-unsecured-credentials|Unsecured Credentials]]), or directly from the Windows certificate store via various crypto APIs.[^4] [^6] [^1]  With appropriate enrollment rights, users and/or machines within a domain can also request and/or manually renew certificates from enterprise certificate authorities (CA). This enrollment process defines various settings and permissions associated with the certificate. Of note, the certificate’s extended key usage (EKU) values define signing, encryption, and authentication use cases, while the certificate’s subject alternative name (SAN) values define the certificate owner’s alternate names.[^3] <br><br>Abusing certificates for authentication credentials may enable other behaviors such as [[kb/mitre/attack/tactics/TA0008-lateral-movement|Lateral Movement]]. Certificate-related misconfigurations may also enable opportunities for [[kb/mitre/attack/tactics/TA0004-privilege-escalation|Privilege Escalation]], by way of allowing users to impersonate or assume privileged accounts or permissions via the identities (SANs) associated with a certificate. These abuses may also enable [[kb/mitre/attack/tactics/TA0003-persistence|Persistence]] via stealing or forging certificates that can be used as [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]] for the duration of the certificate's validity, despite user password resets. Authentication certificates can also be stolen and forged for machine accounts.<br><br>Adversaries who have access to root (or subordinate) CA certificate private keys (or mechanisms protecting/managing these keys) may also establish [[kb/mitre/attack/tactics/TA0003-persistence|Persistence]] by forging arbitrary authentication certificates for the victim domain (known as “golden” certificates).[^3]  Adversaries may also target certificates and related services in order to access other forms of credentials, such as [[kb/mitre/attack/techniques/T1558.001-golden-ticket|Golden Ticket]] ticket-granting tickets (TGT) or NTLM plaintext.[^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0002-mimikatz\|S0002]] | Mimikatz | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]'s `CRYPTO` module can create and export various types of authentication certificates.[^1]  |
| [[kb/mitre/attack/software/S0677-aadinternals\|S0677]] | AADInternals | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can create and export various authentication certificates, including those associated with Azure AD joined/registered devices.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1015-active-directory-configuration\|M1015]] | Active Directory Configuration | Ensure certificate authorities (CA) are properly secured, including treating CA servers (and other resources hosting CA certificates) as tier 0 assets. Harden abusable CA settings and attributes.<br><br>For example, consider disabling the usage of AD CS certificate SANs within relevant authentication protocol settings to enforce strict user mappings and prevent certificates from authenticating as other identifies.[^1]  Also consider enforcing CA Certificate Manager approval for the templates that include SAN as an issuance requirement. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Ensure certificates as well as associated private keys are appropriately secured. Consider utilizing additional hardware credential protections such as trusted platform modules (TPM) or hardware security modules (HSM). Enforce HTTPS and enable Extended Protection for<br>Authentication.[^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Consider disabling old/dangerous authentication protocols (e.g. NTLM), as well as unnecessary certificate features, such as potentially vulnerable AD CS web and other enrollment server roles.[^1]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Check and remediate unneeded existing authentication certificates as well as common abusable misconfigurations of CA settings and permissions, such as AD CS certificate enrollment permissions and published overly permissive certificate templates (which define available settings for created certificates). For example, available AD CS certificate templates can be checked via the Certificate Authority MMC snap-in (`certsrv.msc`). `certutil.exe` can also be used to examine various information within an AD CS CA database.[^3] [^1] [^2]  |

 [^1]: [GitHub GhostPack Certificates](https://github.com/GhostPack/SharpDPAPI#certificates)
 [^2]: [Microsoft AD CS Overview](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831740(v=ws.11))
 [^3]: [Medium Certified Pre Owned](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
 [^4]: [SpecterOps Certified Pre Owned](https://web.archive.org/web/20220818094600/https://specterops.io/assets/resources/Certified_Pre-Owned.pdf)
 [^5]: [O365 Blog Azure AD Device IDs](https://o365blog.com/post/deviceidentity/)
 [^6]: [GitHub CertStealer](https://github.com/TheWover/CertStealer)
 [^7]: [APT29 Deep Look at Credential Roaming](https://www.mandiant.com/resources/blog/apt29-windows-credential-roaming)
 [^8]: [AADInternals Documentation](https://o365blog.com/aadinternals)
 [^9]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)
 [^10]: [GitHub Certify](https://github.com/GhostPack/Certify/)
 [^11]: [Adsecurity Mimikatz Guide](https://adsecurity.org/?page_id=1821)
