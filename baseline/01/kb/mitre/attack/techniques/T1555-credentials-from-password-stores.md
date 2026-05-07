---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1555
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1555-credentials-from-password-stores
tactic:
    - Credential Access
platforms:
    - IaaS
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may search for common password storage locations to obtain user credentials.[^1]  Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0002-mimikatz\|S0002]] | Mimikatz | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the credential vault and DPAPI.[^1] [^2] [^3] [^4] [^5] 	 |
| [S0048](https://attack.mitre.org/software/S0048) | PinchDuke | PinchDuke steals credentials from compromised hosts. PinchDuke's credential stealing functionality is believed to be based on the source code of the Pinch credential stealing malware (also known as LdPinch). Credentials targeted by PinchDuke include ones associated with many sources such as The Bat!, Yahoo!, Mail.ru, Passport.Net, Google Talk, and Microsoft Outlook.[^1]  |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke collects user credentials, including passwords, for various programs including popular instant messaging applications and email clients as well as WLAN keys.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | A module in Prikormka collects passwords stored in applications installed on the victim.[^1]  |
| [S0138](https://attack.mitre.org/software/S0138) | OLDBAIT | OLDBAIT collects credentials from several email clients.[^1]  |
| [S0167](https://attack.mitre.org/software/S0167) | Matryoshka | Matryoshka is capable of stealing Outlook passwords.[^1] [^2]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can retrieve passwords from messaging and mail client applications.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can obtain passwords from common FTP clients.[^1] [^2]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla has the ability to steal credentials from FTP clients and wireless profiles.[^1]  |
| [[kb/mitre/attack/software/S0349-lazagne\|S0349]] | LaZagne | [[kb/mitre/attack/software/S0349-lazagne\|LaZagne]] can obtain credentials from databases, mail, and WiFi across multiple platforms.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth uses an external software known as NetPass to recover passwords. [^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can decrypt passwords stored in the RDCMan configuration file.[^1]  |
| [S0435](https://attack.mitre.org/software/S0435) | PLEAD | PLEAD has the ability to steal saved passwords from Microsoft Outlook.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has stolen credentials from multiple applications and data sources including Windows OS credentials, email clients, FTP, and SFTP clients.[^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp's passw.plug plugin can gather account information from multiple instant messaging, email, and social media services, as well as FTP, VNC, and VPN clients.[^1]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY can collect credentials from WINSCP.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate use Nirsoft Network Password Recovery or NetPass tools to steal stored RDP credentials in some malware versions.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu has obtained credentials from mail clients via NirSoft MailPassView.[^3] [^2] [^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules for stealing stored credentials from Outlook and Foxmail email client software.[^1] [^2]  |
| [S1156](https://attack.mitre.org/software/S1156) | Manjusaka | Manjusaka extracts credentials from the Windows Registry associated with Premiumsoft Navicat, a utility used to facilitate access to various database types.[^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can collect credentials stored in email clients.[^2] [^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has obtained credentials from VPN services, FTP clients and Instant Messenger (IM)/Chat clients.[^1] [^2] [^3]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has collected keys stored for Solana stored in `.config/solana/id.json` and other login details associated with macOS within `/Library/Keychains/login.keychain` or for Linux within `/.local/share/keyrings`.[^1]  |
| [S9022](https://attack.mitre.org/software/S9022) | MirrorStealer | MirrorStealer has the ability to steal credentials from email clients.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Limit the number of accounts and services with permission to query information from password stores to only those required. Ensure that accounts and services with permissions to query password stores only have access to the secrets they require. |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | The password for the user's login keychain can be changed from the user's login password. This increases the complexity for an adversary because they need to know an additional password.<br><br>Organizations may consider weighing the risk of storing credentials in password stores and web browsers. If system, software, or web browser credential disclosure is a significant concern, technical controls, policy, and user training may be used to prevent storage of credentials in improper locations. |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Perform regular software updates to mitigate exploitation risk. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1555.002-securityd-memory\|T1555.002]] | Securityd Memory |
| [[kb/mitre/attack/techniques/T1555.001-keychain\|T1555.001]] | Keychain |
| [[kb/mitre/attack/techniques/T1555.005-password-managers\|T1555.005]] | Password Managers |
| [[kb/mitre/attack/techniques/T1555.003-credentials-from-web-browsers\|T1555.003]] | Credentials from Web Browsers |
| [[kb/mitre/attack/techniques/T1555.006-cloud-secrets-management-stores\|T1555.006]] | Cloud Secrets Management Stores |
| [[kb/mitre/attack/techniques/T1555.004-windows-credential-manager\|T1555.004]] | Windows Credential Manager |

 [^1]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^2]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^3]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^4]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^5]: [Deply Mimikatz](https://github.com/gentilkiwi/mimikatz)
 [^6]: [GitHub Mimikatz lsadump Module](https://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump)
 [^7]: [Directory Services Internals DPAPI Backup Keys Oct 2015](https://www.dsinternals.com/en/retrieving-dpapi-backup-keys-from-active-directory/)
 [^8]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^9]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^10]: [Netskope XLoader 2022](https://www.netskope.com/blog/new-formbook-campaign-delivered-through-phishing-emails)
 [^11]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^12]: [Infoblox Lokibot January 2019](https://insights.infoblox.com/threat-intelligence-reports/threat-intelligence--22)
 [^13]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
 [^14]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^15]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
 [^16]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)
 [^17]: [CopyKittens Nov 2015](https://cdn2.hubspot.net/hubfs/1903456/Whitepapers/CopyKittens.pdf)
 [^18]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^19]: [ESET PLEAD Malware July 2018](https://www.welivesecurity.com/2018/07/09/certificates-stolen-taiwanese-tech-companies-plead-malware-campaign/)
 [^20]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^21]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^22]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^23]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)
 [^24]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)
 [^25]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^26]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^27]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^28]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^29]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
 [^30]: [GitHub LaZagne Dec 2018](https://github.com/AlessandroZ/LaZagne)
 [^31]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^32]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^33]: [Segurança Informática URSA Sophisticated Loader 2020](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)
 [^34]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
 [^35]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^36]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
 [^37]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
