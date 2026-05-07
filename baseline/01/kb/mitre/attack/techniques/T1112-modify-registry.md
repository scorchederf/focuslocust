---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1112
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/tactic/persistence
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1112-modify-registry
tactic:
    - Defense Impairment
    - Persistence
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.<br><br>Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility [[kb/mitre/attack/software/S0075-reg|Reg]] may be used for local or remote Registry modification.[^5]  Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.<br><br>The Registry may be modified in order to hide configuration information or malicious payloads via [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information|Obfuscated Files or Information]].[^10] [^3] [^4] [^1]  The Registry may also be modified to impair defenses, such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory.[^2] [^10] <br><br>The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system.[^6]  Often [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]] are required, along with access to the remote system's [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares|SMB/Windows Admin Shares]] for RPC communication.<br><br>Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via [[kb/mitre/attack/software/S0075-reg|Reg]] or other utilities using the Win32 API.[^8]  Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence.[^9] [^7] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor has the ability to modify the Registry on compromised hosts using `RegDeleteValueA` and `RegCreateKeyExA`.[^1]  |
| [S0012](https://attack.mitre.org/software/S0012) | PoisonIvy | PoisonIvy creates a Registry subkey that registers a new system device.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has a module to create, delete, or modify Registry keys.[^1] [^2] [^3]  |
| [S0019](https://attack.mitre.org/software/S0019) | Regin | Regin appears to have functionality to modify remote Registry information.[^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can store configuration information in the Registry including the initialization vector and AES key needed to find and decrypt other Uroburos components.[^1]  |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | CHOPSTICK may modify Registry keys to store RC4 encrypted configuration information.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | BACKSPACE is capable of deleting Registry keys, sub-keys, and values on a victim system.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has altered the InstallTime subkey.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL is capable of setting and deleting Registry values.[^1]  |
| [[kb/mitre/attack/software/S0075-reg\|S0075]] | Reg | [[kb/mitre/attack/software/S0075-reg\|Reg]] may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface.[^1]  |
| [S0090](https://attack.mitre.org/software/S0090) | Rover | Rover has functionality to remove Registry Run key persistence as a cleanup procedure.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can set a Registry key to determine how long it has been installed and possibly to indicate the version number.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT has modified Registry values to store encrypted orchestrator code and payloads.[^2] [^1]   |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Once Shamoon has access to a network share, it enables the RemoteRegistry service on the target system. It will then connect to the system with RegConnectRegistryW and modify the Registry to disable UAC remote restrictions by setting `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy` to 1.[^2] [^1] [^3]  |
| [S0142](https://attack.mitre.org/software/S0142) | StreamEx | StreamEx has the ability to modify the Registry.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can delete all Registry entries created during its execution.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can modify Registry values within `HKEY_CURRENT_USER\Software\Microsoft\Office\<Excel Version>\Excel\Security\AccessVBOM\` to enable the execution of additional code.[^1]  |
| [S0157](https://attack.mitre.org/software/S0157) | SOUNDBITE | SOUNDBITE is capable of modifying the Registry.[^1]  |
| [S0158](https://attack.mitre.org/software/S0158) | PHOREAL | PHOREAL is capable of manipulating the Registry.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer modifies the Registry to store an encoded configuration file in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Security`.[^1] [^2]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can modify the Registry to store its configuration information.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a Registry subkey to register its created service, and can also uninstall itself later by deleting this value. Hydraq's backdoor also enables remote attackers to modify and delete subkeys.[^1] [^2]  |
| [S0205](https://attack.mitre.org/software/S0205) | Naid | Naid creates Registry entries that store information about a created service and point to a malicious DLL dropped to disk.[^1]  |
| [S0210](https://attack.mitre.org/software/S0210) | Nerex | Nerex creates a Registry subkey that registers a new service.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can perform Registry operations.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot writes data into the Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Pniumj`.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can modify the `HKEY_CURRENT_USER\Software\Microsoft\Office\` registry key so it can bypass the VB object model (VBOM) on a compromised host.[^1]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck can manipulate Registry keys.[^1]  |
| [S0245](https://attack.mitre.org/software/S0245) | BADCALL | BADCALL modifies the firewall Registry key `SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfileGloballyOpenPorts\\List`.[^1]  |
| [S0254](https://attack.mitre.org/software/S0254) | PLAINTEE | PLAINTEE uses `reg add` to add a Registry Run key for persistence.[^1]  |
| [S0256](https://attack.mitre.org/software/S0256) | Mosquito | Mosquito can modify Registry keys under `HKCU\Software\Microsoft\[dllname]` to store configuration values. Mosquito also modifies Registry keys under `HKCR\CLSID\...\InprocServer32` with a path to the launcher.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole has a command to create, set, copy, or delete a specified Registry key or value.[^1] [^2]  |
| [S0261](https://attack.mitre.org/software/S0261) | Catchamas | Catchamas creates three Registry keys to establish persistence by adding a [[kb/mitre/attack/techniques/T1543.003-windows-service\|Windows Service]].[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] has a command to edit the Registry on the victim’s machine.[^2] [^1]  |
| [S0263](https://attack.mitre.org/software/S0263) | TYPEFRAME | TYPEFRAME can install encrypted configuration data under the Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellCompatibility\Applications\laxhost.dll` and `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PrintConfigs`.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can modify registry entries.[^1]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT deletes the Registry key `HKCU\Software\Classes\Applications\rundll32.exe\shell\open`.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has deleted Registry keys to clean up its prior activity.[^1]   |
| [S0269](https://attack.mitre.org/software/S0269) | QUADAGENT | QUADAGENT modifies an HKCU Registry key to store a session identifier unique to the compromised system as well as a pre-shared key used for encrypting and decrypting C2 communications.[^1]  |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE has a command to create Registry entries for storing data under `HKEY_CURRENT_USER\SOFTWARE\Microsoft\WABE\DataPath`.[^1]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda modifies several Registry keys under `HKCU\Software\Microsoft\Internet Explorer\ PhishingFilter\` to disable phishing filters.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can achieve persistence by modifying Registry key entries.[^1]   |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has full control of the Registry, including the ability to modify it.[^1] [^2]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet adds a Registry value for its installation routine to the Registry Key `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System Enable LUA=”0”` and `HKEY_CURRENT_USER\Software\DC3_FEXEC`.[^1] [^2]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore has the capability to edit the Registry.[^1] [^2]  |
| [S0342](https://attack.mitre.org/software/S0342) | GreyEnergy | GreyEnergy modifies conditions in the Registry and adds keys.[^1]  |
| [S0343](https://attack.mitre.org/software/S0343) | Exaramel for Windows | Exaramel for Windows adds the configuration to the Registry in XML format.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT sets `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load` to point to its executable.[^1]  |
| [S0350](https://attack.mitre.org/software/S0350) | zwShell | zwShell can modify the Registry.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has modified registry keys of ComSysApp, Svchost, and xmlProv on the machine to gain persistence.[^1] [^2]   |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has modified Managed Object Format (MOF) files within the Registry to run specific commands and create persistence on the system.[^1] 	 |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can create, delete, or modify a specified Registry key or value.[^1] [^2]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used Registry modifications as part of its installation routine.[^1] [^2]  |
| [S0397](https://attack.mitre.org/software/S0397) | LoJax | LoJax has modified the Registry key `‘HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute’` from `‘autocheck autochk *’` to `‘autocheck autoche *’`.[^1]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can create Registry entries to enable services to run.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has made registry modifications to alter its behavior upon execution.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor's dispatcher can modify the Run registry key.[^1]  |
| [S0441](https://attack.mitre.org/software/S0441) | PowerShower | PowerShower has added a registry key so future powershell.exe instances are spawned off-screen by default, and has removed all registry entries that are left behind during the dropper process.[^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat has registered two registry keys for shim databases.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has modified the Registry as part of its UAC bypass process.[^1]   |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has written process names to the Registry, disabled IE browser features, deleted Registry keys, and changed the ExtendedUIHoverTime key.[^1] [^2] [^3] [^4]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can add the following registry entry: `HKEY_CURRENT_USER\SOFTWARE\{8 random characters}`.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal can set the `KeepPrintedJobs` attribute for configured printers in `SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Print\\Printers` to enable document stealing.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has the ability to modify the Registry key `HKCU\Software\ApplicationContainer\Appsw64` to store information regarding the C2 server and downloads.[^3] [^1] [^2]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can create a registry key using wdigest.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can modify the Registry to save encryption parameters and system information.[^2] [^5] [^4] [^3] [^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon has modified the Registry to store its encrypted payload.[^1]  |
| [S0511](https://attack.mitre.org/software/S0511) | RegDuke | RegDuke can create seemingly legitimate Registry key to store its encryption key.[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint has modified the Registry key `HKLM\SOFTWARE\Microsoft\DRM` to store a malicious payload.[^1]  |
| [S0518](https://attack.mitre.org/software/S0518) | PolyglotDuke | PolyglotDuke can write encrypted JSON configuration files to the Registry.[^1]  |
| [[kb/mitre/attack/software/S0527-cspy-downloader\|S0527]] | CSPY Downloader | [[kb/mitre/attack/software/S0527-cspy-downloader\|CSPY Downloader]] can write to the Registry under the `%windir%` variable to execute tasks.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can modify the Registry to store its configuration at `HKCU\Software\` under frequently changing names including `%USERNAME%` and `ToolTech-RM`.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA can add, modify, and/or delete registry keys. It has changed the proxy configuration of a victim system by modifying the `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` registry.[^1]  |
| [S0537](https://attack.mitre.org/software/S0537) | HyperStack | HyperStack can add the name of its communication pipe to `HKLM\SYSTEM\\CurrentControlSet\\Services\\lanmanserver\\parameters\NullSessionPipes`.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST had commands that allow an attacker to write or delete registry keys, and was observed stopping services by setting their `HKLM\SYSTEM\CurrentControlSet\services\\[service_name]\\Start` registry entries to value 4.[^1] [^2]  It also deleted previously-created Image File Execution Options (IFEO) Debugger registry values and registry keys related to HTTP proxy to clean up traces of its activity.[^3]  |
| [S0560](https://attack.mitre.org/software/S0560) | TEARDROP | TEARDROP modified the Registry to create a Windows service for itself on a compromised host.[^1]  |
| [S0568](https://attack.mitre.org/software/S0568) | EVILNUM | EVILNUM can make modifications to the Regsitry for persistence.[^1]  |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive | Explosive has a function to write itself to Registry values.[^1]   |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer can set values in the Registry to help in execution.[^1]   |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell has a command to modify a Registry key.[^1]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex has added entries to the Registry for ransom contact information.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear has deleted certain values from the Registry to load a malicious DLL.[^1]   |
| [S0583](https://attack.mitre.org/software/S0583) | Pysa | Pysa has modified the registry key “SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System” and added the ransom note.[^1]   |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot has modified the Registry to install a second-stage script in the `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\sibot`.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad can modify the Registry to store and maintain a configuration block and virtual file system.[^2] [^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet can create registry keys to load driver files.[^1]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker adds keys to the Registry at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services` and various other Registry locations.[^1] [^2]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop can make modifications to Registry keys.[^1]   |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker can modify registry values within the `Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` registry key.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes can modify Registry values to stored information and establish persistence.[^1]   |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon modifies several registry keys for persistence and UAC bypass.[^1]  |
| [S0649](https://attack.mitre.org/software/S0649) | SMOKEDHAM | SMOKEDHAM has modified registry keys for persistence, to enable credential caching for credential access, and to facilitate lateral movement via RDP.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can modify the Registry to store its configuration information in a randomly named subkey under `HKCU\Software\Microsoft`.[^2] [^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can set and delete Registry keys.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can write its configuration file to the Registry.[^2] [^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can write its configuration file to `Software\Classes\scConfig` in either `HKEY_LOCAL_MACHINE` or `HKEY_CURRENT_USER`.[^1]  |
| [S0664](https://attack.mitre.org/software/S0664) | Pandora | Pandora can write an encrypted token to the Registry to enable processing of remote commands.[^1]  |
| [S0665](https://attack.mitre.org/software/S0665) | ThreatNeedle | ThreatNeedle can modify the Registry to save its configuration data as the following RC4-encrypted Registry key: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\GameCon`.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can modify the Registry to store its components.[^1]  |
| [S0668](https://attack.mitre.org/software/S0668) | TinyTurla | TinyTurla can set its configuration parameters in the Registry.[^1]  |
| [S0669](https://attack.mitre.org/software/S0669) | KOCTOPUS | KOCTOPUS has added and deleted keys from the Registry.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can create `HKCU\Software\Classes\Folder\shell\open\command` as a new registry key during privilege escalation.[^2] [^1]   |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can modify Registry values to store configuration strings, keylogger, and output of components.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can remove persistence-related artifacts from the Registry.[^1]  |
| [[kb/mitre/attack/software/S0677-aadinternals\|S0677]] | AADInternals | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can modify registry keys as part of setting a new pass-through authentication agent.[^1]  |
| [S0679](https://attack.mitre.org/software/S0679) | Ferocious | Ferocious has the ability to add a Class ID in the current user Registry hive to enable persistence mechanisms.[^1]  |
| [S0691](https://attack.mitre.org/software/S0691) | Neoichor | Neoichor has the ability to configure browser settings by modifying Registry entries under `HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer`.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper has the ability to modify Registry keys to disable crash dumps, colors for compressed files, and pop-up information about folders and desktop items.[^1] [^2] [^3]  |
| [S1011](https://attack.mitre.org/software/S1011) | Tarrask | Tarrask is able to delete the Security Descriptor (`SD`) registry subkey in order to “hide” scheduled tasks.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has overwritten registry keys for persistence.[^1]  |
| [S1033](https://attack.mitre.org/software/S1033) | DCSrv | DCSrv has created Registry keys for persistence.[^1]  |
| [S1047](https://attack.mitre.org/software/S1047) | Mori | Mori can write data to `HKLM\Software\NFC\IPA` and `HKLM\Software\NFC\` and delete Registry values.[^2] [^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can delete its persistence mechanisms from the registry.[^1]  |
| [S1058](https://attack.mitre.org/software/S1058) | Prestige | Prestige has the ability to register new registry keys for a new extension handler via `HKCR\.enc` and `HKCR\enc\shell\open\command`.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can write the process ID of a target process into the `HKEY_LOCAL_MACHINE\SOFTWARE\DDE\tpid` Registry value as part of its reflective loading activity.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can manipulate the system registry on a compromised host.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla has modified registry keys for persistence.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat has the ability to add the following registry key on compromised networks to maintain persistence: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services \LanmanServer\Paramenters`[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta has modified the Registry to enable itself to run in safe mode, to change the icons and file extensions for encrypted files, and to add the malware path for persistence.[^6] [^1] [^3] [^4] [^5] [^2]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can modify the Registry to set the ServiceDLL for a service created by the malware for persistence.[^1] <br> |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | The Samurai loader component can create multiple Registry keys to force the svchost.exe process to load the final backdoor.[^1]  |
| [[kb/mitre/attack/software/S1131-nppspy\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] modifies the Registry to record the malicious listener for output from the Winlogon process.[^1]  |
| [S1132](https://attack.mitre.org/software/S1132) | IPsec Helper | IPsec Helper can make arbitrary changes to registry keys based on provided input.[^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can use the Windows Registry Environment key to change the `%windir%` variable to point to `c:\Windows` to enable payload execution.[^1] <br> |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker modifies various registry keys associated with system logon and BitLocker functionality to effectively lock-out users following disk encryption.[^1] [^2]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware modifies the victim Registry to prevent system recovery.[^1]  |
| [S1181](https://attack.mitre.org/software/S1181) | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware modifies the victim Registry to allow for elevated execution.[^1]  |
| [S1190](https://attack.mitre.org/software/S1190) | Kapeka | Kapeka writes persistent configuration information to the victim host registry.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can create Registry keys to bypass UAC and for persistence.[^1]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has modified the following registry key to install itself as the value, granting permission to install specified extensions: ` HKCU\Software\Policies\Google\Chrome\ExtensionInstallForcelist`.[^1]   |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can change the Registry values for Group Policy refresh time, to disable SmartScreen, and to disable Windows Defender.[^1] [^2] <br><br> |
| [S1226](https://attack.mitre.org/software/S1226) | BOOKWORM | BOOKWORM has modified Registry key values as part of its created service `DeviceSync`. [^1]  |
| [S1230](https://attack.mitre.org/software/S1230) | HIUPAN | HIUPAN has modified registry keys to ensure hidden files and extensions are not visible through the modification of `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced`.[^1] [^2]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can make Registry modifications to share networked drives between elevated and non-elevated processes and to increase the number of outstanding network requests per client.[^2] [^1]  Qilin can also modify `HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper` to enable posting of ransom messages.[^3] <br> |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has modified and deleted Registry keys to add services, and to disable Security Solutions such as Windows Defender.[^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can store its configuration file in the Registry.[^1]  |
| [S9025](https://attack.mitre.org/software/S9025) | NOOPLDR | NOOPLDR can store its payload in the Registry using a random hex string in `HKCU\SOFTWARE\Microsoft\COM3`.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has the ability to clear the Registry values in the Windows Startup folder that were previously set for persistence.[^1]       |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1024-restrict-registry-permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |

 [^1]: [CISA Russian Gov Critical Infra 2018](https://www.cisa.gov/news-events/alerts/2018/03/15/russian-government-cyber-activity-targeting-energy-and-other-critical-infrastructure-sectors)
 [^2]: [CISA LockBit 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a)
 [^3]: [Avaddon Ransomware 2021](https://arxiv.org/pdf/2102.04796)
 [^4]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^5]: [Microsoft Reg](https://technet.microsoft.com/en-us/library/cc732643.aspx)
 [^6]: [Microsoft Remote](https://technet.microsoft.com/en-us/library/cc754820.aspx)
 [^7]: [SpectorOps Hiding Reg Jul 2017](https://posts.specterops.io/hiding-registry-keys-with-psreflect-b18ec5ac8353)
 [^8]: [Microsoft Reghide NOV 2006](https://docs.microsoft.com/sysinternals/downloads/reghide)
 [^9]: [TrendMicro POWELIKS AUG 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/poweliks-malware-hides-in-windows-registry/)
 [^10]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
 [^11]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^12]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^13]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^14]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)
 [^15]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
 [^16]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^17]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^18]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^19]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
 [^20]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^21]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^22]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^23]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
 [^24]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^25]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^26]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^27]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
 [^28]: [Trend Micro Conficker](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
 [^29]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^30]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^31]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
 [^32]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
 [^33]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^34]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^35]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
 [^36]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^37]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^38]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
 [^39]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)
 [^40]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^41]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^42]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^43]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^44]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^45]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^46]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^47]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^48]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^49]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^50]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^51]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^52]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^53]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^54]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)
 [^55]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
 [^56]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
 [^57]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^58]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^59]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^60]: [FireEye APT28](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^61]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^62]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
 [^63]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^64]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^65]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^66]: [Uptycs Warzone UAC Bypass November 2020](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)
 [^67]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^68]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
 [^69]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^70]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^71]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^72]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^73]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^74]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
 [^75]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
 [^76]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)
 [^77]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^78]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^79]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
 [^80]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^81]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
 [^82]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
 [^83]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
 [^84]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
 [^85]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
 [^86]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
 [^87]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^88]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^89]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
 [^90]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^91]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^92]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
 [^93]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^94]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^95]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^96]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^97]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^98]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^99]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^100]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
 [^101]: [Check Point Sunburst Teardrop December 2020](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)
 [^102]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
 [^103]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^104]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^105]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^106]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^107]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^108]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
 [^109]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^110]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
 [^111]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^112]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
 [^113]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
 [^114]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^115]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
 [^116]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^117]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
 [^118]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
 [^119]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)
 [^120]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^121]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^122]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^123]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
 [^124]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^125]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^126]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^127]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^128]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^129]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
 [^130]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^131]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
 [^132]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
 [^133]: [Cybereason Clop Dec 2020](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
 [^134]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)
 [^135]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
 [^136]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
 [^137]: [Unit 42 Inception November 2018](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)
 [^138]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
 [^139]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
 [^140]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^141]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)
 [^142]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)
 [^143]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^144]: [FireEye Shamoon Nov 2016](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
 [^145]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)
 [^146]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^147]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^148]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^149]: [CYBERCOM Iranian Intel Cyber January 2022](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)
 [^150]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^151]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^152]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^153]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
 [^154]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
 [^155]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
 [^156]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^157]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^158]: [Red Canary Qbot](https://redcanary.com/threat-detection-report/threats/qbot/)
 [^159]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^160]: [CISA ComRAT Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
 [^161]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
 [^162]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^163]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^164]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^165]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
 [^166]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
 [^167]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^168]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
 [^169]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^170]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^171]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^172]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^173]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^174]: [SentinelLabs Agent Tesla Aug 2020](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)
 [^175]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^176]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
 [^177]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^178]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^179]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^180]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^181]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^182]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^183]: [Symantec Nerex May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3445-99)
 [^184]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^185]: [AADInternals Documentation](https://o365blog.com/aadinternals)
 [^186]: [Kaspersky Regin](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070305/Kaspersky_Lab_whitepaper_Regin_platform_eng.pdf)
