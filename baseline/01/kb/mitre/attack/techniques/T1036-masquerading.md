---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1036
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1036-masquerading
tactic:
    - Stealth
platforms:
    - Containers
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.<br><br>Renaming abusable system utilities to evade security monitoring is also a form of [[kb/mitre/attack/techniques/T1036-masquerading|Masquerading]].[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM has been delivered as archived Windows executable files masquerading as PDF documents.[^1] 	 |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | The TrickBot downloader has used an icon to appear as a Microsoft Word document.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal |  Bisonal dropped a decoy payload with a .jpg extension that contained a malicious Visual Basic script.[^1]   |
| [S0368](https://attack.mitre.org/software/S0368) | NotPetya | NotPetya drops [[kb/mitre/attack/software/S0029-psexec\|PsExec]] with the filename dllhost.dat.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk can create .dll files that actually contain a Rich Text File format document.[^1]  |
| [S0453](https://attack.mitre.org/software/S0453) | Pony | Pony has used the Adobe Reader icon for the downloaded file to look more trustworthy.[^1] 	 |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay has masqueraded as a JPG image file.[^1]  |
| [S0466](https://attack.mitre.org/software/S0466) | WindTail | WindTail has used icons mimicking MS Office files to mask payloads.[^1]  |
| [S0497](https://attack.mitre.org/software/S0497) | Dacls | The Dacls Mach-O binary has been disguised as a .nib file.[^1]  |
| [S0565](https://attack.mitre.org/software/S0565) | Raindrop | Raindrop was built to include a modified version of 7-Zip source code (including associated export names) and Far Manager source code.[^1] [^2]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can use a legitimate process name to hide itself.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can disguise JavaScript files as PDFs.[^1]  |
| [S0634](https://attack.mitre.org/software/S0634) | EnvyScout | EnvyScout has used folder icons for malicious files to lure victims into opening them.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox has the ability to mask malicious data strings as PDF files.[^1]  |
| [S0637](https://attack.mitre.org/software/S0637) | NativeZone | NativeZone has, upon execution, displayed a message box that appears to be related to a Ukrainian electronic document management system.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET installs malicious application bundles that mimic native macOS apps, such as Safari, by using the legitimate app’s icon and customizing the `Info.plist` to match expected metadata.[^1] [^2]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb can masquerade the output of C2 commands as a fake, but legitimately formatted WebP file.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession has used a file named English.rtf to appear benign on victim hosts.[^1] [^2]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman has used an icon mimicking a text file to mask a malicious executable.[^1]  |
| [S0682](https://attack.mitre.org/software/S0682) | TrailBlazer | TrailBlazer has used filenames that match the name of the compromised system in attempt to avoid detection.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate has been disguised as a JPG extension to avoid detection as a malicious PE file.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro can download malicious files with a .tmp extension and append them with .exe prior to execution.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan has used an executable named `companycatalogue` to appear benign.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot has renamed malicious binaries as `wallpaper.mp4` and `slideshow.mp4` to avoid detection.[^1] [^2]  |
| [S1046](https://attack.mitre.org/software/S1046) | PowGoop | PowGoop has disguised a PowerShell script as a .dat file (goopdate.dat).[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla's payload has been renamed `PowerShellInfo.exe`.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate can masquerade as pirated media content for initial delivery to victims.[^1]  |
| [S1164](https://attack.mitre.org/software/S1164) | UPSTYLE | UPSTYLE has masqueraded filenames using examples such as `update.py`.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer PE executable payloads have used uncommon but legitimate extensions such as `.com` instead of `.exe`.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer malware has masqueraded as legitimate software such as "PDF Converter Software" which has been distributed through poisoned search engine results often resembling legitimate software lures with the combination of typo squatted domains.[^1]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has masqueraded as MiroTalk installation packages: “MiroTalk.dmg” for macOS and “MiroTalk.msi” for Windows, and has included login GUIs with MiroTalk themes.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has masqueraded as legitimate VSCode extensions.[^1] [^2]   GlassWorm has also impersonated Github projects.[^1]  |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has been named after well-known files schtask.exe, schtask2.exe, and <redacted>_update.exe.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Train users not to open email attachments or click unknown links (URLs). Such training fosters more secure habits within your organization and will limit many of the risks.   |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Consider defining and enforcing a naming convention for user accounts to more easily spot generic account names that do not fit the typical schema. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Use file system access controls to protect folders such as C:\\Windows\\System32. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | Implement security controls on the endpoint, such as a Host Intrusion Prevention System (HIPS), to identify and prevent execution of potentially malicious files (such as those with mismatching file signatures). |
| [[kb/mitre/attack/mitigations/M1045-code-signing\|M1045]] | Code Signing | Require signed binaries. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Audit user accounts to ensure that each one has a defined purpose. |
| [[kb/mitre/attack/mitigations/M1049-antivirus-antimalware\|M1049]] | Antivirus/Antimalware | Anti-virus can be used to automatically quarantine suspicious files. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1036.007-double-file-extension\|T1036.007]] | Double File Extension |
| [[kb/mitre/attack/techniques/T1036.005-match-legitimate-resource-name-or-location\|T1036.005]] | Match Legitimate Resource Name or Location |
| [[kb/mitre/attack/techniques/T1036.008-masquerade-file-type\|T1036.008]] | Masquerade File Type |
| [[kb/mitre/attack/techniques/T1036.009-break-process-trees\|T1036.009]] | Break Process Trees |
| [[kb/mitre/attack/techniques/T1036.011-overwrite-process-arguments\|T1036.011]] | Overwrite Process Arguments |
| [[kb/mitre/attack/techniques/T1036.002-right-to-left-override\|T1036.002]] | Right-to-Left Override |
| [[kb/mitre/attack/techniques/T1036.004-masquerade-task-or-service\|T1036.004]] | Masquerade Task or Service |
| [[kb/mitre/attack/techniques/T1036.012-browser-fingerprint\|T1036.012]] | Browser Fingerprint |
| [[kb/mitre/attack/techniques/T1036.001-invalid-code-signature\|T1036.001]] | Invalid Code Signature |
| [[kb/mitre/attack/techniques/T1036.003-rename-legitimate-utilities\|T1036.003]] | Rename Legitimate Utilities |
| [[kb/mitre/attack/techniques/T1036.010-masquerade-account-name\|T1036.010]] | Masquerade Account Name |
| [[kb/mitre/attack/techniques/T1036.006-space-after-filename\|T1036.006]] | Space after Filename |

 [^1]: [LOLBAS Main Site](https://lolbas-project.github.io/)
 [^2]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
 [^3]: [Symantec RAINDROP January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)
 [^4]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
 [^5]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^6]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^7]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^8]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^9]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
 [^10]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^11]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^12]: [Aikido GlassWorm October 2025](https://www.aikido.dev/blog/the-return-of-the-invisible-threat-hidden-pua-unicode-hits-github-repositorties)
 [^13]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
 [^14]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^15]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^16]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^17]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^18]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^19]: [objective-see windtail1 dec 2018](https://objective-see.com/blog/blog_0x3B.html)
 [^20]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^21]: [Volexity UPSTYLE 2024](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
 [^22]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^23]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^24]: [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
 [^25]: [SentinelOne NobleBaron June 2021](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)
 [^26]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^27]: [ESET DynoWiper Update JAN 2026](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
 [^28]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
 [^29]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
 [^30]: [ANSSI RYUK RANSOMWARE](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-006.pdf)
 [^31]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^32]: [Secureworks BRONZE PRESIDENT December 2019](https://www.secureworks.com/research/bronze-president-targets-ngos)
 [^33]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^34]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
 [^35]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
 [^36]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^37]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^38]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^39]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
