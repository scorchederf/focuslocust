---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1486
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1486-data-encrypted-for-impact
tactic:
    - Impact
platforms:
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.[^8] [^2] [^9] [^10] <br><br>In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted (and often renamed and/or tagged with specific file markers). Adversaries may need to first employ other behaviors, such as [[kb/mitre/attack/techniques/T1222-file-and-directory-permissions-modification|File and Directory Permissions Modification]] or [[kb/mitre/attack/techniques/T1529-system-shutdown-reboot|System Shutdown/Reboot]], in order to unlock and/or gain access to manipulate these files.[^1]  In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR.[^9]  Adversaries may also encrypt virtual machines hosted on ESXi or other hypervisors.[^6]  <br><br>To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]], [[kb/mitre/attack/techniques/T1003-os-credential-dumping|OS Credential Dumping]], and [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares|SMB/Windows Admin Shares]].[^2] [^9]  Encryption malware may also leverage [[kb/mitre/attack/techniques/T1491.001-internal-defacement|Internal Defacement]], such as changing victim wallpapers or ESXi server login messages, or otherwise intimidate victims by sending ransom notes or other messages to connected printers (known as "print bombing").[^7] [^5] <br><br>In cloud environments, storage objects within compromised accounts may also be encrypted.[^3]  For example, in AWS environments, adversaries may leverage services such as AWS’s Server-Side Encryption with Customer Provided Keys (SSE-C) to encrypt data.[^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon has an operational mode for encrypting data instead of overwriting it.[^1] [^2]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck encrypts the victims machine followed by asking the victim to pay a ransom. [^1]  |
| [S0341](https://attack.mitre.org/software/S0341) | Xbash | Xbash has maliciously encrypted victim's database systems and demanded a cryptocurrency ransom be paid.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry encrypts user files and demands that a ransom be paid in Bitcoin to decrypt those files.[^3] [^1] [^2]  |
| [S0368](https://attack.mitre.org/software/S0368) | NotPetya | NotPetya encrypts user files and disk structures like the MBR with 2048-bit RSA.[^1] [^2] [^3]  |
| [S0370](https://attack.mitre.org/software/S0370) | SamSam | SamSam encrypts victim files using RSA-2048 encryption and demands a ransom be paid in Bitcoin to decrypt those files.[^1]  |
| [S0372](https://attack.mitre.org/software/S0372) | LockerGoga | LockerGoga has encrypted files, including core Windows OS files, using RSA-OAEP MGF1 and then demanded Bitcoin be paid for the decryption key.[^1] [^2] [^3]  |
| [S0389](https://attack.mitre.org/software/S0389) | JCry | JCry has encrypted files and demanded Bitcoin to decrypt those files. [^1]  |
| [S0400](https://attack.mitre.org/software/S0400) | RobbinHood | RobbinHood will search for an RSA encryption key and then perform its encryption process on the system files.[^1]   |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has used a combination of symmetric (AES) and asymmetric (RSA) encryption to encrypt files. Files have been encrypted with their own AES key and given a file extension of .RYK. Encrypted directories have had a ransom note of RyukReadMe.txt written to the directory.[^1] [^2]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has disrupted systems by encrypting files on targeted machines, claiming to decrypt files if a ransom payment is made. Maze has used the ChaCha algorithm, based on Salsa20, and an RSA algorithm to encrypt files.[^1]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can encrypt files on infected machines to extort victims.[^1] 	 |
| [S0481](https://attack.mitre.org/software/S0481) | Ragnar Locker | Ragnar Locker encrypts files on the local machine and mapped drives prior to displaying a note demanding a ransom.[^1] [^2]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can encrypt files on victim systems and demands a ransom to decrypt the files.[^5] [^3] [^1] [^7] [^4] [^6] [^2] [^8]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor can encrypt all non-system files using a hybrid AES-RSA algorithm prior to displaying a ransom note.[^1] [^2]   |
| [S0556](https://attack.mitre.org/software/S0556) | Pay2Key | Pay2Key can encrypt data on victim's machines using RSA and AES algorithms in order to extort a ransom payment for decryption.[^1] [^2]  |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer can import a hard-coded RSA 1024-bit public key, generate a 128-bit RC4 key for each file, and encrypt the file in place, appending `.locked` to the filename.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can use `CreateIoCompletionPort()`, `PostQueuedCompletionStatus()`, and `GetQueuedCompletionPort()` to rapidly encrypt files, excluding those with the extensions of .exe, .dll, and .lnk. It has used a different AES-256 encryption key per file with a bundled RAS-4096 public encryption key that is unique for each victim. Conti can use “Windows Restart Manager” to ensure files are unlocked and open for encryption.[^5] [^1] [^2] [^4] [^3]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex has used the open-source library, Mbed Crypto, and generated AES keys to carry out the file encryption process.[^1] [^2]  |
| [S0583](https://attack.mitre.org/software/S0583) | Pysa | Pysa has used RSA and AES-CBC encryption algorithm to encrypt a list of targeted file extensions.[^1]   |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest encrypts a set of file extensions on a host, deletes the original files, and provides a ransom note with no contact information.[^1]  |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS uses standard encryption library functions to encrypt files.[^1] [^2]  |
| [S0606](https://attack.mitre.org/software/S0606) | Bad Rabbit | Bad Rabbit has encrypted files and disks using AES-128-CBC and RSA-2048.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk has a ransomware component that encrypts files with an AES key that is also RSA-1028 encrypted.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop can encrypt files using AES, RSA, and RC4 and will add the ".clop" extension to encrypted files.[^1] [^2] [^3]   |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker can encrypt data and leave a ransom note.[^1] [^2] [^3]   |
| [S0616](https://attack.mitre.org/software/S0616) | DEATHRANSOM | DEATHRANSOM can use public and private key pair encryption to encrypt files for ransom payment.[^1]  |
| [S0617](https://attack.mitre.org/software/S0617) | HELLOKITTY | HELLOKITTY can use an embedded RSA-2048 public key to encrypt victim data for ransom.[^1]  |
| [S0618](https://attack.mitre.org/software/S0618) | FIVEHANDS | FIVEHANDS can use an embedded NTRU public key to encrypt data for ransom.[^1] [^2] [^3]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba has the ability to encrypt system data and add the ".cuba" extension to encrypted files.[^1]   |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk can use ChaCha8 and ECDH to encrypt data.[^1] [^2] [^3] [^4]  |
| [S0639](https://attack.mitre.org/software/S0639) | Seth-Locker | Seth-Locker can encrypt files on a targeted system, appending them with the suffix .seth.[^1]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon encrypts the victim system using a combination of AES256 and RSA encryption schemes.[^1]  |
| [S0654](https://attack.mitre.org/software/S0654) | ProLock | ProLock can encrypt files on a compromised host with RC6, and encrypts the key with RSA-1024.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET performs AES-CBC encryption on files under `~/Documents`, `~/Downloads`, and<br>`~/Desktop` with a fixed key and renames files to give them a `.enc` extension. Only files with sizes <br>less than 500MB are encrypted.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol has encrypted files using an RSA key though the `CryptEncrypt` API and has appended filenames with ".lock64". [^1]  |
| [S1033](https://attack.mitre.org/software/S1033) | DCSrv | DCSrv has encrypted drives using the core encryption mechanism from DiskCryptor.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has encrypted files and network resources using AES-256 and added an `.avos`, `.avos2`, or `.AvosLinux` extension to filenames.[^2] [^3] [^4] [^1]  |
| [S1058](https://attack.mitre.org/software/S1058) | Prestige | Prestige has leveraged the CryptoPP C++ library to encrypt files on target systems using AES and appended filenames with `.enc`.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat has the ability to encrypt Windows devices, Linux devices, and VMWare instances.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can encrypt files with the ChaCha20 cypher and using a multithreaded process to increase speed.[^10] [^1] [^3] [^6] [^7] [^9] [^4] [^8] [^2]  Black Basta has also encrypted files while the victim system is in safe mode, appending `.basta` upon completion.[^5]   |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal uses a multi-threaded encryption process that can partially encrypt targeted files with the OpenSSL library and the AES256 algorithm.[^1] [^2] [^3]  |
| [S1096](https://attack.mitre.org/software/S1096) | Cheerscrypt | Cheerscrypt can encrypt data on victim machines using a Sosemanuk stream cipher with an Elliptic-curve Diffie–Hellman (ECDH) generated key.[^2] [^1] <br> |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate can deploy follow-on ransomware payloads.[^1]  |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira can encrypt victim filesystems for financial extortion purposes including through the use of the ChaCha20 and ChaCha8 stream ciphers.[^2] [^1] [^3] <br> |
| [S1133](https://attack.mitre.org/software/S1133) | Apostle | Apostle creates new, encrypted versions of files then deletes the originals, with the new filenames consisting of a random GUID and ".lock" for an extension.[^1]  |
| [S1137](https://attack.mitre.org/software/S1137) | Moneybird | Moneybird targets a common set of file types such as documents, certificates, and database files for encryption while avoiding executable, dynamic linked libraries, and similar items.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can encrypt data on victim systems, including through the use of partial encryption and multi-threading to speed encryption.[^2] [^4] [^1] [^3] [^2]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP can RC4 encrypt content in blocks on targeted systems.[^2] [^1] [^3]  |
| [S1162](https://attack.mitre.org/software/S1162) | Playcrypt | Playcrypt encrypts files on targeted hosts with an AES-RSA hybrid encryption, encrypting every other file portion of 0x100000 bytes.[^1] [^2]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker uses the legitimate BitLocker application to encrypt victim files for ransom.[^1] [^2]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware is ransomware using a shared key across victims for encryption.[^1]  |
| [S1181](https://attack.mitre.org/software/S1181) | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware is a ransomware variant associated with BlackByte operations.[^1]  |
| [S1191](https://attack.mitre.org/software/S1191) | Megazord | Megazord can encrypt files on targeted Windows hosts leaving them with a  ".powerranges" file extension.[^1] [^2] [^3]  |
| [S1194](https://attack.mitre.org/software/S1194) | Akira _v2 | The Akira _v2 encryptor targets the `/vmfs/volumes/` path by default and can use the rust-crypto 0.2.36 library crate for the encryption processes.[^1] [^2]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can use standard AES and elliptic-curve cryptography algorithms to encrypt victim data.[^1] [^2] <br> |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can encrypt targeted data using the AES-256, ChaCha20, or RSA-2048 algorithms.[^1] [^4] [^2] [^3]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub can use Elliptic Curve Encryption to encrypt files on targeted systems.[^2]  RansomHub can also skip content at regular intervals (ex. encrypt 1 MB, skip 3 MB) to optomize performance and enable faster encryption for large files.[^1]   |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can use AES-256 or ChaCha20 for domain-wide encryption of victim servers and workstations and RSA-4096 or RSA-2048 to secure generated encryption keys.[^4] [^5] [^1] [^7] [^2] [^3] [^8] [^6]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has encrypted files using AES-256 encryption, which then appends the file extension “.medusa” to encrypted files and leaves a ransomware note named “!READ_ME_MEDUSA!!!.txt.”[^1] [^2] [^3] [^4]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has the ability to encrypt files with the ChaCha20 and Curve25519 cryptographic algorithms.[^1]  Embargo also has the ability to encrypt system data and add a random six-letter extension consisting of hexadecimal characters such as ".b58eeb" or “.3d828a” to encrypted files.[^2]   |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | <br>LODEINFO can incorporate a ransom command to encrypt specified files and folders.[^2] [^1] [^3]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable cloud-delivered protection and Attack Surface Reduction (ASR) rules to block the execution of files that resemble ransomware.[^2]  In AWS environments, create an IAM policy to restrict or block the use of SSE-C on S3 buckets.[^1]  |
| [[kb/mitre/attack/mitigations/M1053-data-backup\|M1053]] | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. Consider enabling versioning in cloud environments to maintain backup copies of storage objects.[^2]  |

 [^1]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^2]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
 [^3]: [Rhino S3 Ransomware Part 1](https://rhinosecuritylabs.com/aws/s3-ransomware-part-1-attack-vector/)
 [^4]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)
 [^5]: [Varonis](https://www.varonis.com/blog/vmware-esxi-in-the-line-of-ransomware-fire)
 [^6]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
 [^7]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
 [^8]: [US-CERT Ransomware 2016](https://www.us-cert.gov/ncas/alerts/TA16-091A)
 [^9]: [US-CERT NotPetya 2017](https://www.us-cert.gov/ncas/alerts/TA17-181A)
 [^10]: [US-CERT SamSam 2018](https://www.us-cert.gov/ncas/alerts/AA18-337A)
 [^11]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)
 [^12]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)
 [^13]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
 [^14]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
 [^15]: [Cynet Ragnar Apr 2020](https://www.cynet.com/blog/cynet-detection-report-ragnar-locker-ransomware/)
 [^16]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^17]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^18]: [Kroll Royal Deep Dive February 2023](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
 [^19]: [Trend Micro Royal Linux ESXi February 2023](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
 [^20]: [Carbon Black JCry May 2019](https://www.carbonblack.com/2019/05/14/cb-tau-threat-intelligence-notification-jcry-ransomware-pretends-to-be-adobe-flash-player-update-installer/)
 [^21]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^22]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^23]: [Medium Babuk February 2021](https://sebdraven.medium.com/babuk-is-distributed-packed-78e2f5dd2e62)
 [^24]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
 [^25]: [CheckPoint Agrius 2023](https://research.checkpoint.com/2023/agrius-deploys-moneybird-in-targeted-attacks-against-israeli-organizations/)
 [^26]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^27]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^28]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^29]: [Talos Sodinokibi April 2019](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)
 [^30]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^31]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^32]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^33]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)
 [^34]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
 [^35]: [McAfee REvil October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-crescendo/)
 [^36]: [Tetra Defense Sodinokibi March 2020](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)
 [^37]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^38]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^39]: [CISA Play Ransomware Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
 [^40]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
 [^41]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^42]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^43]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
 [^44]: [CarbonBlack LockerGoga 2019](https://www.carbonblack.com/2019/03/22/tau-threat-intelligence-notification-lockergoga-ransomware/)
 [^45]: [Unit42 LockerGoga 2019](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)
 [^46]: [Wired Lockergoga 2019](https://www.wired.com/story/lockergoga-ransomware-crippling-industrial-firms/)
 [^47]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^48]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
 [^49]: [Palo Alto Unit 42 EKANS](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)
 [^50]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^51]: [Joint CSA AvosLocker Mar 2022](https://www.ic3.gov/Media/News/2022/220318.pdf)
 [^52]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^53]: [Trend Micro AvosLocker Apr 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
 [^54]: [Cisco Talos Avos Jun 2022](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
 [^55]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^56]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)
 [^57]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
 [^58]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^59]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)
 [^60]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
 [^61]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
 [^62]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^63]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
 [^64]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^65]: [BlackBerry Black Basta May 2022](https://blogs.blackberry.com/en/2022/05/black-basta-rebrand-of-conti-or-something-new)
 [^66]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
 [^67]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^68]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
 [^69]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
 [^70]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
 [^71]: [Uptycs Black Basta ESXi June 2022](https://www.uptycs.com/blog/black-basta-ransomware-goes-cross-platform-now-targets-esxi-systems)
 [^72]: [Trend Micro Black Basta Spotlight September 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)
 [^73]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
 [^74]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
 [^75]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
 [^76]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^77]: [Sentinel Labs WastedLocker July 2020](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
 [^78]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
 [^79]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^80]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^81]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^82]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)
 [^83]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)
 [^84]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
 [^85]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^86]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^87]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
 [^88]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^89]: [SentinelOne Qilin NOV 2022](https://www.sentinelone.com/anthology/agenda-qilin/)
 [^90]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^91]: [BushidoToken Qilin RaaS JUN 2024](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)
 [^92]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
 [^93]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^94]: [mbed-crypto](https://github.com/ARMmbed/mbed-crypto)
 [^95]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^96]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^97]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
 [^98]: [Cybleinc Conti January 2020](https://cybleinc.com/2021/01/21/conti-ransomware-resurfaces-targeting-government-large-organizations/)
 [^99]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
 [^100]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
 [^101]: [Cybereason Conti Jan 2021](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
 [^102]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
 [^103]: [ClearkSky Fox Kitten February 2020](https://www.clearskysec.com/fox-kitten/)
 [^104]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
 [^105]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^106]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^107]: [CISA RansomHub AUG 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)
 [^108]: [Cybereason Egregor Nov 2020](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)
 [^109]: [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
 [^110]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)
 [^111]: [Sophos SamSam Apr 2018](https://www.sophos.com/en-us/medialibrary/PDFs/technical-papers/SamSam-ransomware-chooses-Its-targets-carefully-wpna.pdf)
 [^112]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^113]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
 [^114]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
 [^115]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^116]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^117]: [KillDisk Ransomware](https://www.bleepingcomputer.com/news/security/killdisk-disk-wiping-malware-adds-ransomware-component/)
 [^118]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^119]: [Unit42 Clop April 2021](https://unit42.paloaltonetworks.com/clop-ransomware/)
 [^120]: [Cybereason Clop Dec 2020](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
 [^121]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^122]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^123]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
 [^124]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
 [^125]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^126]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
 [^127]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
 [^128]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
 [^129]: [SentinelOne LockBit 2.0](https://www.sentinelone.com/anthology/lockbit-2-0/)
 [^130]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^131]: [CarbonBlack RobbinHood May 2019](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
 [^132]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
 [^133]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^134]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
 [^135]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
 [^136]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^137]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^138]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
 [^139]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)
 [^140]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)
 [^141]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
