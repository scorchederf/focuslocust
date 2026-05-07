---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1012
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1012-query-registry
tactic:
    - Discovery
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.<br><br>The Registry contains a significant amount of information about the operating system, configuration, software, and security.[^1]  Information can easily be queried using the [[kb/mitre/attack/software/S0075-reg|Reg]] utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [[kb/mitre/attack/techniques/T1012-query-registry|Query Registry]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor can query the Registry on compromised hosts using `RegQueryValueExA`.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX can enumerate and query for information contained within the Windows Registry.[^1] [^2] [^3]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi is capable of enumerating Registry keys and values.[^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can query the Registry, typically `HKLM:\SOFTWARE\Classes\.wav\OpenWithProgIds`, to find the key and path to decrypt and load its kernel driver and kernel driver loader.[^1]  |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | CHOPSTICK provides access to the Windows Registry, which can be used to gather information.[^1]  |
| [S0030](https://attack.mitre.org/software/S0030) | Carbanak | Carbanak checks the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` for proxy configurations information.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | BACKSPACE is capable of enumerating and making modifications to an infected system's Registry.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has checked for the existence of a Service key to determine if it has already been installed on the system.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL can enumerate registry keys.[^1] [^2]  |
| [[kb/mitre/attack/software/S0075-reg\|S0075]] | Reg | [[kb/mitre/attack/software/S0075-reg\|Reg]] may be used to gather details from the Windows Registry of a local or remote system at the command-line interface.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic uses the `rem reg query` command to obtain values from Registry keys.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can check the Registry for the presence of `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\last_edate` to determine how long it has been installed on a host.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT can check the default browser by querying `HKCR\http\shell\open\command`.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon queries several Registry keys to identify hard disk partitions to overwrite.[^1]  |
| [S0145](https://attack.mitre.org/software/S0145) | POWERSOURCE | POWERSOURCE queries Registry keys in preparation for setting Run keys to achieve persistence.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can query `HKEY_CURRENT_USER\Software\Microsoft\Office\<Excel Version>\Excel\Security\AccessVBOM\`  to determine if the security setting for restricting default programmatic access is enabled.[^1] [^2]  |
| [S0155](https://attack.mitre.org/software/S0155) | WINDSHIELD | WINDSHIELD can gather Registry values.[^1]  |
| [S0165](https://attack.mitre.org/software/S0165) | OSInfo | OSInfo queries the registry to look for information about Terminal Services.[^1]  |
| [S0172](https://attack.mitre.org/software/S0172) | Reaver | Reaver queries the Registry to determine the correct Startup path to use for persistence.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer checks the system for certain Registry keys.[^1]  |
| [S0182](https://attack.mitre.org/software/S0182) | FinFisher | FinFisher queries Registry values as part of its anti-sandbox checks.[^2] [^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may query the Registry by running `reg query` on a victim.[^1]  |
| [S0186](https://attack.mitre.org/software/S0186) | DownPaper | DownPaper searches and reads the value of the Windows Update Registry Run key.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.[^1] [^2]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can enumerate Registry keys.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can retrieve system information, such as CPU speed, from Registry keys.[^1] [^2]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc gathers product names from the Registry key: `HKLM\Software\Microsoft\Windows NT\CurrentVersion ProductName` and the processor description from the Registry key `HKLM\HARDWARE\DESCRIPTION\System\CentralProcessor\0 ProcessorNameString`.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot searches for certain Registry keys to be configured before executing the payload.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can access the `HKLM\System\CurrentControlSet\Services\mssmbios\Data\SMBiosData` Registry key to obtain the System manufacturer value to identify the machine type.[^1]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA uses the command `reg query “HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\InternetSettings”`.[^1]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck enumerates Registry keys associated with event logs.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon enumerates registry keys with the command `regkeyenum` and obtains information for the Registry key `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy executes the `reg query` command to obtain information in the Registry.[^1]  |
| [S0252](https://attack.mitre.org/software/S0252) | Brave Prince | Brave Prince gathers information about the Registry.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can enumerate Registry values, keys, and data.[^1]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT queries the Registry for specific keys for potential privilege escalation and proxy information. FELIXROOT has also used WMI to query the Windows Registry.[^2] [^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has used the RegQueryValueExA function to retrieve proxy information in the Registry.[^1]  |
| [S0269](https://attack.mitre.org/software/S0269) | QUADAGENT | QUADAGENT checks if a value exists within a Registry key in the HKCU hive whose name is the same as the scheduled task it has created.[^1]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda checks for the existence of a Registry key and if it contains certain values.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can obtain Registry data from targeted systems.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon enumerates values in the Registry.[^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can check for installed software on the system under the Registry key `Software\Microsoft\Windows\CurrentVersion\Uninstall`.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT contains watchdog functionality that periodically ensures `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load` is set to point to its executable.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis queries the Registry for keys and values.[^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | A variant of HOPLIGHT hooks lsass.exe, and lsass.exe then checks the Registry for the data value 'rdpproto' under the key `SYSTEM\CurrentControlSet\Control\Lsa Name`.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill has looked in the registry to find the default browser path.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can read specific registry values.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used [[kb/mitre/attack/software/S0075-reg\|Reg]] to query the Registry for installed programs.[^1] [^2]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can query the netsvc group value data located in the svchost group Registry key.[^1]   |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has executed the `reg query` command for `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default`.[^1] 	 |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor has opened the registry and performed query searches.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun has identified the OS product name from a compromised host by searching the registry for `SOFTWARE\MICROSOFT\Windows NT\ CurrentVersion \| ProductName`.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak can use the Registry for code updates and to collect credentials.[^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has searched the Image File Execution Options registry key for "Debugger" within every subkey.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can query the Registry to get random file extensions to append to encrypted files.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can get user agent strings for the default browser from `HKCU\Software\Classes\http\shell\open\command`.[^1]  |
| [S0513](https://attack.mitre.org/software/S0513) | LiteDuke | LiteDuke can query the Registry to check for the presence of `HKCU\Software\KasperskyLab`.[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint has used shellcode which reads code stored in the registry keys `\REGISTRY\SOFTWARE\Microsoft\DRM` using the native Windows API as well as read `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Interfaces` as part of its C2.[^1] 	 |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can check for existing stratum cryptomining information in `HKLM\Software\Microsoft\Windows\CurrentVersion\spreadCpuXmr – %stratum info%`.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can query `Windows\CurrentVersion\Uninstall` for installed applications.[^1] [^2]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected the registry value `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\MachineGuid` from compromised hosts.[^1]  |
| [S0560](https://attack.mitre.org/software/S0560) | TEARDROP | TEARDROP checked that `HKU\SOFTWARE\Microsoft\CTF` existed before decoding its embedded payload.[^1] [^2]   |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack can collect the RegisteredOwner, RegisteredOrganization, and InstallDate registry values.[^1]  |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer can use the RegEnumKeyW to iterate through Registry keys.[^1]   |
| [S0574](https://attack.mitre.org/software/S0574) | BendyBear | BendyBear can query the host's Registry key at `HKEY_CURRENT_USER\Console\QuickEdit` to retrieve data.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear can query the Registry key `"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSDTC\MTxOCI"` to see if the value `OracleOcilib` exists.[^1]  |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot has queried the registry for proxy server information.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet searches the Registry for indicators of security programs.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer has a data wiper component that enumerates keys in the Registry `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`.[^1]  |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker checks for specific registry keys related to the `UCOMIEnumConnections` and `IActiveScriptParseProcedure32` interfaces.[^1]  |
| [S0627](https://attack.mitre.org/software/S0627) | SodaMaster | SodaMaster has the ability to query the Registry to detect a key specific to VMware.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling has the ability to enumerate Registry keys, including `KEY_CURRENT_USER\Software\Bitcoin\Bitcoin-Qt\strDataDir` to search for a bitcoin wallet.[^2] [^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can open random files and Registry keys to obscure malware behavior from sandbox analysis.[^1]  |
| [S0668](https://attack.mitre.org/software/S0668) | TinyTurla | TinyTurla can query the Registry for its configuration information.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can query the Registry to determine if it has already been installed on the system.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower has the ability to enumerate `Uninstall` registry values.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower can query the Registry for keys added to execute COM hijacking.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.[^1]  |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ can search the registry of a compromised host.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan can query `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography MachineGuid` to retrieve the machine GUID.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot has used `check_registry_keys` as part of its environmental checks.[^1]  |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark can query `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography MachineGuid` to retrieve the machine GUID.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can check the Registry for specific keys.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can check `Software\Microsoft\Windows\CurrentVersion\Internet Settings` to extract the `ProxyServer` string.[^1]  |
| [S1047](https://attack.mitre.org/software/S1047) | Mori | Mori can read data from the Registry including from `HKLM\Software\NFC\IPA` and<br>`HKLM\Software\NFC\`.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can search the registry files of a compromised host.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can enumerate Registry keys with all subkeys and values.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can search for the `HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System` Registry key to gather system information.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can search registry keys to identify antivirus programs on an compromised host.[^1]  |
| [S1076](https://attack.mitre.org/software/S1076) | QUIETCANARY | QUIETCANARY has the ability to retrieve information from the Registry.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai can query `SOFTWARE\Microsoft\.NETFramework\policy\v2.0` for discovery.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer queries the Windows Registry to fingerprint the infected host via the `HKLM:\SOFTWARE\Microsoft\Cryptography\MachineGuid` key.[^2] [^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can enumerate Registry items.[^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware enumerates the Registry, specifically the `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options` key.[^1]  |
| [S1190](https://attack.mitre.org/software/S1190) | Kapeka | Kapeka queries registry values for stored configuration information.[^1]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has queried the following registry key to check for installed Chrome extensions: ` HKCU\Software\Policies\Google\Chrome\ExtensionInstallForcelist `.[^1]   |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has queried Registry values to identify software using `reg query`.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer can query the Windows Registry.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can check `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control SystemStartOptions` to determine if a machine is running in safe mode.[^1]  |

 [^1]: [Wikipedia Windows Registry](https://en.wikipedia.org/wiki/Windows_Registry)
 [^2]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^3]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^4]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^5]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^6]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^7]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^8]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^9]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^10]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
 [^11]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^12]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
 [^13]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^14]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^15]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^16]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^17]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
 [^18]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^19]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
 [^20]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^21]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
 [^22]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^23]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^24]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^25]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^26]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
 [^27]: [McAfee RedLine Stealer April 2024](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)
 [^28]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
 [^29]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^30]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^31]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^32]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^33]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^34]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^35]: [Lastline PlugX Analysis](https://lastline3.rssing.com/chan-29044929/all_p1.html#c29044929a2)
 [^36]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^37]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^38]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
 [^39]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)
 [^40]: [Microsoft Reg](https://technet.microsoft.com/en-us/library/cc732643.aspx)
 [^41]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^42]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^43]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^44]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^45]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
 [^46]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^47]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^48]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^49]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^50]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^51]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^52]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^53]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^54]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^55]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
 [^56]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
 [^57]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^58]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^59]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^60]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^61]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^62]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^63]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^64]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^65]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^66]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^67]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
 [^68]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^69]: [Cisco DNSMessenger March 2017](http://blog.talosintelligence.com/2017/03/dnsmessenger.html)
 [^70]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
 [^71]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^72]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
 [^73]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
 [^74]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
 [^75]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^76]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^77]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
 [^78]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^79]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)
 [^80]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
 [^81]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^82]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^83]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
 [^84]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^85]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
 [^86]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^87]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
 [^88]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^89]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^90]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^91]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^92]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^93]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^94]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^95]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^96]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^97]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^98]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^99]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^100]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^101]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^102]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^103]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
 [^104]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^105]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^106]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^107]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^108]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
