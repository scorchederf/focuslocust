---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1102
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1102-web-service
tactic:
    - Command And Control
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise.[^1]  Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.<br><br>Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE has used web services including Paste.ee to host payloads.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon can use Pastebin to receive C2 commands.[^1]  |
| [[kb/mitre/attack/software/S0508-ngrok\|S0508]] | ngrok | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] has been used by threat actors to proxy C2 connections to ngrok service subdomains.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar downloads have been hosted on Google Docs.[^1] [^2]  |
| [S0546](https://attack.mitre.org/software/S0546) | SharpStage | SharpStage has used a legitimate web service for evading detection.[^1]   |
| [S0547](https://attack.mitre.org/software/S0547) | DropBook | DropBook can communicate with its operators by exploiting the Simplenote, DropBox, and the social media platform, Facebook, where it can create fake accounts to control the backdoor and receive instructions.[^1] [^2]  |
| [S0561](https://attack.mitre.org/software/S0561) | GuLoader | GuLoader has the ability to download malware from Google Drive.[^1]  |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot has used a legitimate compromised website to download DLLs to the victim's machine.[^1]  |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki has used the dogechain.info API to generate a C2 address.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has downloaded scripts from GitHub.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox can download files from Dropbox using a hardcoded access token.[^1]  |
| [S0649](https://attack.mitre.org/software/S0649) | SMOKEDHAM | SMOKEDHAM has used Google Drive and Dropbox to host files downloaded by victims via malicious links.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can download additional modules from actor-controlled Amazon S3 buckets.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can download additional payloads hosted on a Discord channel.[^2] [^3] [^4] [^1] [^5]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee has been downloaded to victim's machines from OneDrive.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use legitimate websites for external C2 channels including Slack, Discord, and MS Teams.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can retrieve its primary payload from public sites such as Pastebin and Textbin.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can be utilized to abuse `sslip.io`, a free IP to domain mapping service, as part of actor-controlled C2 channels.[^1]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 can download additional payloads from web services including Pastebin and top4top.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish has used Amazon Web Services to host second-stage servers.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin second stage payloads can be hosted as RAR files, containing a malicious EXE and DLL, on Discord servers.[^1]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor can utilize Microsoft OneDrive or Google Drive for command and control purposes.[^1] [^2]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP has the ability to use use Telegram channels to return a list of commands to be executed, to download additional payloads, or to create a reverse shell.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus has used Google Firebase to download malicious installation scripts.[^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker uses a subdomain on the legitimate Cloudflare resource "trycloudflare[.]com" to obfuscate the threat actor's actual address and to tunnel information sent from victim systems.[^1]  |
| [S1221](https://attack.mitre.org/software/S1221) | MOPSLED | MOPSLED can use third-party web services such as GitHub and Google Drive for C2.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has leveraged legitimate file sharing web services to host malicious payloads.[^1] [^2]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has leveraged DNS web services to resolve C2 IP addresses including sslip.io and nip.io.[^1]   BRICKSTORM has also utilized Cloudflare Workers for C2 communications.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can use Telegram or Discord to send infection status messages.[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | AshTag can download malicious payloads from file sharing services.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Web proxies can be used to enforce external network communication policy that prevents use of unauthorized external services. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1102.003-one-way-communication\|T1102.003]] | One-Way Communication |
| [[kb/mitre/attack/techniques/T1102.002-bidirectional-communication\|T1102.002]] | Bidirectional Communication |
| [[kb/mitre/attack/techniques/T1102.001-dead-drop-resolver\|T1102.001]] | Dead Drop Resolver |

 [^1]: [Broadcom BirdyClient Microsoft Graph API 2024](https://www.broadcom.com/support/security-center/protection-bulletin/birdyclient-malware-leverages-microsoft-graph-api-for-c-c-communication)
 [^2]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^3]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^4]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
 [^5]: [Palo Alto Latrodectus Activity June 2024](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2024-06-25-IOCs-from-Latrodectus-activity.txt)
 [^6]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^7]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^8]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
 [^9]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^10]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^11]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^12]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
 [^13]: [FireEye Shining A Light on DARKSIDE May 2021](https://www.fireeye.com/blog/threat-research/2021/05/shining-a-light-on-darkside-ransomware-operations.html)
 [^14]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^15]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^16]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^17]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^18]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^19]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^20]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^21]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^22]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
 [^23]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^24]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^25]: [Crowdstrike WhisperGate January 2022](https://www.crowdstrike.com/blog/technical-analysis-of-whispergate-malware)
 [^26]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
 [^27]: [Microsoft WhisperGate January 2022](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
 [^28]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
 [^29]: [Zdnet Ngrok September 2018](https://www.zdnet.com/article/sly-malware-author-hides-cryptomining-botnet-behind-ever-shifting-proxy-service/)
 [^30]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^31]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
 [^32]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^33]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^34]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^35]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^36]: [Medium Eli Salem GuLoader April 2021](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
 [^37]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^38]: [Zscaler Bazar September 2020](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)
 [^39]: [SentinelOne SocGholish Infrastructure November 2022](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/)
