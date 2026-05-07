---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1020
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1020-automated-exfiltration
tactic:
    - Exfiltration
platforms:
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after being gathered during Collection.[^1]  <br><br>When automated exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel|Exfiltration Over C2 Channel]] and [[kb/mitre/attack/techniques/T1048-exfiltration-over-alternative-protocol|Exfiltration Over Alternative Protocol]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke exfiltrates collected files automatically over FTP to remote servers.[^1]  |
| [S0090](https://attack.mitre.org/software/S0090) | Rover | Rover automatically searches for files on local drives based on a predefined list of file extensions and sends them to the command and control server every 60 minutes. Rover also automatically sends keylogger files and screenshots to the C2 server on a regular timeframe.[^1]  |
| [S0131](https://attack.mitre.org/software/S0131) | TINYTYPHON | When a document is found matching one of the extensions in the configuration, TINYTYPHON uploads it to the C2 server.[^1]  |
| [S0136](https://attack.mitre.org/software/S0136) | USBStealer | USBStealer automatically exfiltrates collected files via removable media when an infected device connects to an air-gapped victim machine after initially being connected to an internet-enabled victim machine. [^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] has the ability to automatically send collected data back to the threat actors' C2.[^1]  |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | If credentials are not collected for two weeks, Ebury encrypts the credentials using a public key and sends them via UDP to an IP address located in the DNS TXT record.[^1] [^2]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron can be configured to automatically exfiltrate files under a specified directory.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete’s collected files are exfiltrated automatically to remote servers.[^1]   |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor has a file uploader plugin that automatically exfiltrates the collected data and log files to the C2 server.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] sent collected system and network information compiled into a report to an adversary-controlled C2.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to manage an automated queue of egress files and commands sent to its C2.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can automatically exfiltrate collected documents to the C2 server.[^1] [^2]  |
| [S0538](https://attack.mitre.org/software/S0538) | Crutch | Crutch has automatically exfiltrated stolen files to Dropbox.[^1]  |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki has used a script that gathers information from a hardcoded list of IP addresses and uploads to an Ngrok URL.[^1]  |
| [S0643](https://attack.mitre.org/software/S0643) | Peppy | Peppy has the ability to automatically exfiltrate files and keylogs.[^1]  |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can automatically upload collected files to its C2 server.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer will automatically collect and exfiltrate data identified in received configuration files from command and control nodes.[^3] [^2] [^1]  |
| [S1166](https://attack.mitre.org/software/S1166) | Solar | Solar can automatically exfitrate files from compromised systems.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer automatically sends gathered email credentials following collection to command and control servers via HTTP POST.[^1] [^2]  |
| [S1211](https://attack.mitre.org/software/S1211) | Hannotog | Hannotog can upload encyrpted data for exfiltration.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1020.001-traffic-duplication\|T1020.001]] | Traffic Duplication |

 [^1]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
 [^2]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
 [^3]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
 [^4]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^5]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^6]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
 [^7]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
 [^8]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^9]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^10]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^11]: [ESET Windigo Mar 2014](https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/)
 [^12]: [ESET Ebury May 2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
 [^13]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^14]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
 [^15]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^16]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^17]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
 [^18]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^19]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
 [^20]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
 [^21]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^22]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
 [^23]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^24]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
 [^25]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^26]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
