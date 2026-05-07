---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1657
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1657-financial-theft
tactic:
    - Impact
platforms:
    - Linux
    - macOS
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware,[^6]  business email compromise (BEC) and fraud,[^5]  "pig butchering,"[^10]  bank hacking,[^4]  and exploiting cryptocurrency networks.[^9]  <br><br>Adversaries may [[kb/mitre/attack/techniques/T1586-compromise-accounts|Compromise Accounts]] to conduct unauthorized transfers of funds.[^8]  In the case of business email compromise or email fraud, an adversary may utilize [[kb/mitre/attack/techniques/T1684.001-impersonation|Impersonation]] of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary.[^5]  This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft.[^1] <br><br>Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after [[kb/mitre/attack/techniques/T1486-data-encrypted-for-impact|Data Encrypted for Impact]] [^11]  and [[kb/mitre/attack/tactics/TA0010-exfiltration|Exfiltration]] of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary.[^3]  Adversaries may use dedicated leak sites to distribute victim data.[^2] <br><br>Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as [[kb/mitre/attack/techniques/T1485-data-destruction|Data Destruction]] and business disruption.[^7] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate can deploy payloads capable of capturing credentials related to cryptocurrency wallets.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has collected data from cryptocurrency wallets and harvested credit cards details from browsers.[^1] [^2] [^3] [^4] [^5]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has searched the victim device credentials and files commonly associated with cryptocurrency wallets.[^1] [^2] [^3] [^4]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has searched the victim device for browser extensions commonly associated with cryptocurrency wallets.[^1] [^2] [^3] [^4] [^5]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has been leveraged in double-extortion ransomware, exfiltrating files then encrypting them, to prompt victims to pay a ransom.[^1] [^2]  |
| [S9004](https://attack.mitre.org/software/S9004) | Crocodilus | Crocodilus has stolen cryptocurrency wallet details from victim devices.[^2] [^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has the ability to steal credentials for cryptocurrency wallets.[^1] [^2] [^3]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Train and encourage users to identify social engineering techniques used to enable financial theft. Also consider training users on procedures to prevent and respond to swatting and doxing, acts increasingly deployed by financially motivated groups to further coerce victims into satisfying ransom/extortion demands.[^1] [^2]  |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit access/authority to execute sensitive transactions, and switch to systems and procedures designed to authenticate/approve payments and purchase requests outside of insecure communication lines such as email. |

 [^1]: [VEC](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/#:~:text=Vendor%20email%20compromise%2C%20also%20referred,steal%20from%20that%20vendor%27s%20customers.)
 [^2]: [Crowdstrike-leaks](https://www.crowdstrike.com/blog/double-trouble-ransomware-data-leak-extortion-part-1/)
 [^3]: [Mandiant-leaks](https://www.mandiant.com/resources/blog/ransomware-extortion-ot-docs)
 [^4]: [DOJ-DPRK Heist](https://www.justice.gov/usao-cdca/pr/3-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyber-attacks-and)
 [^5]: [FBI-BEC](https://www.fbi.gov/file-repository/fy-2022-fbi-congressional-report-business-email-compromise-and-real-estate-wire-fraud-111422.pdf/view)
 [^6]: [FBI-ransomware](https://www.cisa.gov/sites/default/files/Ransomware_Trifold_e-version.pdf)
 [^7]: [AP-NotPetya](https://apnews.com/article/russia-ukraine-technology-business-europe-hacking-ce7a8aca506742ab8e8873e7f9f229c2)
 [^8]: [Internet crime report 2022](https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf)
 [^9]: [BBC-Ronin](https://www.bbc.com/news/technology-60933174)
 [^10]: [wired-pig butchering](https://www.wired.com/story/pig-butchering-fbi-ic3-2022-report/)
 [^11]: [NYT-Colonial](https://www.nytimes.com/2021/05/13/technology/colonial-pipeline-ransom.html)
 [^12]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^13]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
 [^14]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^15]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^16]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^17]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^18]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
 [^19]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^20]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^21]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^22]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
 [^23]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
 [^24]: [Koi Glassworm InvisibleCode October 2025](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
 [^25]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^26]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)
 [^27]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)
 [^28]: [ThreatFabric_Crocodilus_June2025](https://www.threatfabric.com/blogs/crocodilus-mobile-malware-evolving-fast-going-global)
 [^29]: [ThreatFabric_Crocodilus_March2025](https://www.threatfabric.com/blogs/exposing-crocodilus-new-device-takeover-malware-targeting-android-devices)
 [^30]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^31]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
 [^32]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
