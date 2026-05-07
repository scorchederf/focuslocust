---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1558
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1558-steal-or-forge-kerberos-tickets
tactic:
    - Credential Access
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable [[kb/mitre/attack/techniques/T1550.003-pass-the-ticket|Pass the Ticket]]. Kerberos is an authentication protocol widely used in modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants: client, service, and Key Distribution Center (KDC).[^9]  Clients request access to a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos by stealing tickets or forging tickets to enable unauthorized access.<br><br>On Windows, the built-in `klist` utility can be used to list and analyze cached Kerberos tickets.[^8] <br>

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1015-active-directory-configuration\|M1015]] | Active Directory Configuration | For containing the impact of a previously generated golden ticket, reset the built-in KRBTGT account password twice, which will invalidate any existing golden tickets that have been created with the KRBTGT hash and other Kerberos tickets derived from it. For each domain, change the KRBTGT account password once, force replication, and then change the password a second time. Consider rotating the KRBTGT account password every 180 days.[^1]  |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Limit domain admin account permissions to domain controllers and limited servers. Delegate other admin functions to separate accounts.<br><br>Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators.[^1]  |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire.[^1]  Also consider using Group Managed Service Accounts or another third party product such as password vaulting.[^1]  |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.[^1]  |
| [[kb/mitre/attack/mitigations/M1043-credential-access-protection\|M1043]] | Credential Access Protection | On Linux systems, protect resources with Security Enhanced Linux (SELinux) by defining entry points, process types, and file labels.[^1]   |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1558.005-ccache-files\|T1558.005]] | Ccache Files |
| [[kb/mitre/attack/techniques/T1558.004-as-rep-roasting\|T1558.004]] | AS-REP Roasting |
| [[kb/mitre/attack/techniques/T1558.001-golden-ticket\|T1558.001]] | Golden Ticket |
| [[kb/mitre/attack/techniques/T1558.002-silver-ticket\|T1558.002]] | Silver Ticket |
| [[kb/mitre/attack/techniques/T1558.003-kerberoasting\|T1558.003]] | Kerberoasting |

 [^1]: [CERT-EU Golden Ticket Protection](https://cert.europa.eu/static/WhitePapers/UPDATED%20-%20CERT-EU_Security_Whitepaper_2014-007_Kerberos_Golden_Ticket_Protection_v1_4.pdf)
 [^2]: [Microsoft Detecting Kerberoasting Feb 2018](https://blogs.technet.microsoft.com/motiba/2018/02/23/detecting-kerberoasting-activity-using-azure-security-center/)
 [^3]: [Medium Detecting Attempts to Steal Passwords from Memory](https://medium.com/threatpunter/detecting-attempts-to-steal-passwords-from-memory-558f16dce4ea)
 [^4]: [Stealthbits Detect PtT 2019](https://blog.stealthbits.com/detect-pass-the-ticket-attacks)
 [^5]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)
 [^6]: [ADSecurity Detecting Forged Tickets](https://adsecurity.org/?p=1515)
 [^7]: [Microsoft Kerberos Golden Ticket](https://gallery.technet.microsoft.com/scriptcenter/Kerberos-Golden-Ticket-b4814285)
 [^8]: [Microsoft Klist](https://docs.microsoft.com/windows-server/administration/windows-commands/klist)
 [^9]: [ADSecurity Kerberos Ring Decoder](https://adsecurity.org/?p=227)
 [^10]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)
 [^11]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)
