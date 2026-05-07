---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1083
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1083-file-and-directory-discovery
tactic:
    - Discovery
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery|File and Directory Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Many command shell utilities can be used to obtain this information. Examples include `dir`, `tree`, `ls`, `find`, and `locate`.[^1]  Custom tools may also be used to gather file and directory information and interact with the [[kb/mitre/attack/techniques/T1106-native-api|Native API]]. Adversaries may also leverage a [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] on network devices to gather file and directory information (e.g. `dir`, `show flash`, and/or `nvram`).[^2] <br><br>Some files and directories may require elevated or specific user permissions to access.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor can search for specific files.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has a module to enumerate drives and find files recursively.[^1] [^2] [^3] [^5]  PlugX has also checked the path from which it is running for specific parameters prior to execution. [^1] [^4] [^6]  |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe can list file and directory information.[^1]  |
| [S0020](https://attack.mitre.org/software/S0020) | China Chopper | China Chopper's server component can list directory contents.[^2] [^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi is capable of obtaining directory, file, and drive listings.[^1] [^2]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can search for specific files on a compromised system.[^1]  |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | An older version of CHOPSTICK has a module that monitors all mounted volumes for files with the extensions .doc, .docx, .pgp, .gpg, .m2f, or .m2o.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | BACKSPACE allows adversaries to search for files.[^1]  |
| [S0034](https://attack.mitre.org/software/S0034) | NETEAGLE | NETEAGLE allows adversaries to enumerate and modify the infected host's file system. It supports searching for directories, creating directories, listing directory contents, reading and writing to files, retrieving file attributes, and retrieving volume information.[^1]  |
| [S0035](https://attack.mitre.org/software/S0035) | SPACESHIP | SPACESHIP identifies files and directories for collection by searching for specific file extensions or file modification time.[^1]  |
| [S0036](https://attack.mitre.org/software/S0036) | FLASHFLOOD | FLASHFLOOD searches for interesting files (either a default or customized set of file extensions) on the local system and removable media.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL can list files and directories.[^1] [^2]  |
| [S0048](https://attack.mitre.org/software/S0048) | PinchDuke | PinchDuke searches for files created within a certain timeframe and whose file extension matches a predefined list.[^1]  |
| [S0049](https://attack.mitre.org/software/S0049) | GeminiDuke | GeminiDuke collects information from the victim, including installed drivers, programs previously executed by users, programs and services configured to automatically run at startup, files and folders present in any user's home folder, files and folders present in any user's My Documents, programs installed to the Program Files folder, and recently accessed files, folders, and programs.[^1]  |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke searches attached and mounted drives for file extensions and keywords that match a predefined list.[^1]  |
| [S0051](https://attack.mitre.org/software/S0051) | MiniDuke | MiniDuke can enumerate local drives.[^1]  |
| [S0055](https://attack.mitre.org/software/S0055) | RARSTONE | RARSTONE obtains installer properties from Uninstall Registry Key entries to obtain information about installed applications and how to uninstall certain applications.[^1]  |
| [S0059](https://attack.mitre.org/software/S0059) | WinMM | WinMM sets a WH_CBT Windows hook to search for and capture files on the victim.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky scans the victim for files that contain certain keywords and document types including PDF, DOC, DOCX, XLS, and XLSX, from a list that is obtained from the C2 as a text file. It can also identify logical drives for the infected machine.[^1] [^2]  |
| [S0063](https://attack.mitre.org/software/S0063) | SHOTPUT | SHOTPUT has a command to obtain a directory listing.[^1]  |
| [S0064](https://attack.mitre.org/software/S0064) | ELMER | ELMER is capable of performing directory listings.[^1]  |
| [S0065](https://attack.mitre.org/software/S0065) | 4H RAT | 4H RAT has the capability to obtain file and directory listings.[^1]  |
| [S0066](https://attack.mitre.org/software/S0066) | 3PARA RAT | 3PARA RAT has a command to retrieve metadata for files on disk as well as a command to list the current working directory.[^1]  |
| [S0069](https://attack.mitre.org/software/S0069) | BLACKCOFFEE | BLACKCOFFEE has the capability to enumerate files.[^1]  |
| [S0070](https://attack.mitre.org/software/S0070) | HTTPBrowser | HTTPBrowser is capable of listing files, folders, and drives on a victim.[^1] [^2]  |
| [S0072](https://attack.mitre.org/software/S0072) | OwaAuth | OwaAuth has a command to list its directory and logical drives.[^1]  |
| [S0078](https://attack.mitre.org/software/S0078) | Psylo | Psylo has commands to enumerate all storage devices and to find all files that start with a particular string.[^1]  |
| [S0079](https://attack.mitre.org/software/S0079) | MobileOrder | MobileOrder has a command to upload to its C2 server information about files on the victim mobile device, including SD card size, installed app list, SMS content, contacts, and calling history.[^1]  |
| [S0081](https://attack.mitre.org/software/S0081) | Elise | A variant of Elise executes `dir C:\progra~1` when initially run.[^2] [^1]  |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | Misdat is capable of running commands to obtain a list of files and directories, as well as enumerating logical drives.[^1]  |
| [S0086](https://attack.mitre.org/software/S0086) | ZLib | ZLib has the ability to enumerate files and drives.[^1]  |
| [S0088](https://attack.mitre.org/software/S0088) | Kasidet | Kasidet has the ability to search for a given filename on a victim.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy gathers a list of installed apps from the uninstall program Registry. It also gathers registered mail, browser, and instant messaging clients from the Registry. BlackEnergy has searched for given file types.[^1] [^2]  |
| [S0090](https://attack.mitre.org/software/S0090) | Rover | Rover automatically searches for files on local drives based on a predefined list of file extensions.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic recursively searches for all .doc files on the system and collects a directory listing of the Desktop, %TEMP%, and %WINDOWS%\Temp directories.[^1] [^2]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea collects information about available drives, default browser, desktop file list, My Documents, Internet history, program files, and root of available drives. It also searches for ICS-related software files.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can enumerate files and directories on a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0106-cmd\|S0106]] | cmd | [[kb/mitre/attack/software/S0106-cmd\|cmd]] can be used to find files and directories with native functionality such as `dir` commands.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | A module in Prikormka collects information about the paths, size, and creation time of files with specific file extensions, but not the actual content of the file.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains commands to list files and directories, as well as search for files matching certain extensions from a defined list.[^2] [^1] [^3]  |
| [S0124](https://attack.mitre.org/software/S0124) | Pisloader | Pisloader has commands to list drives on the victim machine and to list file information for a given directory.[^1]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec is capable of listing contents of folders on the victim. Remsec also searches for custom network encryption software on victims.[^1] [^2] [^3]  |
| [S0127](https://attack.mitre.org/software/S0127) | BBSRAT | BBSRAT can list file and directory information.[^1]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | BADNEWS identifies files with certain extensions from USB devices, then copies them to a predefined directory.[^1]  |
| [S0129](https://attack.mitre.org/software/S0129) | AutoIt backdoor | AutoIt backdoor is capable of identifying documents on the victim with the following extensions: .doc; .pdf, .csv, .ppt, .docx, .pst, .xls, .xlsx, .pptx, and .jpeg.[^1]  |
| [S0131](https://attack.mitre.org/software/S0131) | TINYTYPHON | TINYTYPHON searches through the drive containing the OS, then all drive letters C through to Z, for documents matching certain extensions.[^1]  |
| [S0136](https://attack.mitre.org/software/S0136) | USBStealer | USBStealer searches victim drives for files matching certain extensions (“.skr”,“.pkr” or “.key”) or names.[^1] [^2]  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has commands to get the current directory name as well as the size of a file. It also has commands to obtain information about logical drives, drive type, and free space.[^1]  |
| [S0141](https://attack.mitre.org/software/S0141) | Winnti for Windows | Winnti for Windows can check for the presence of specific files prior to moving to the next phase of execution.[^1]  |
| [S0142](https://attack.mitre.org/software/S0142) | StreamEx | StreamEx has the ability to enumerate drive types.[^1]  |
| [S0144](https://attack.mitre.org/software/S0144) | ChChes | ChChes collects the victim's %TEMP% directory path and version of Internet Explorer.[^1]  |
| [S0147](https://attack.mitre.org/software/S0147) | Pteranodon | Pteranodon identifies files matching certain file extension and copies them to subdirectories it created.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can check for specific files and directories associated with virtualization and malware analysis.[^1]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind has a command to return a directory listing for a specified directory.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves can enumerate and search for files and directories.[^2] [^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can explore files on a compromised system.[^1]  |
| [S0157](https://attack.mitre.org/software/S0157) | SOUNDBITE | SOUNDBITE is capable of enumerating and manipulating files and directories.[^1]  |
| [S0161](https://attack.mitre.org/software/S0161) | XAgentOSX | XAgentOSX contains the readFiles function to return a detailed listing (sometimes recursive) of a specified directory.[^1]  XAgentOSX contains the showBackupIosFolder function to check for IOS device backups by running `ls -la ~/Library/Application\ Support/MobileSync/Backup/`.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer can list directories on a victim.[^1]  |
| [S0181](https://attack.mitre.org/software/S0181) | FALLCHILL | FALLCHILL can search files on a victim.[^1]  |
| [S0182](https://attack.mitre.org/software/S0182) | FinFisher | FinFisher enumerates directories and scans for certain files.[^2] [^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may enumerate user directories on a victim.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can walk through directories and recursively search for strings in files.[^1]  |
| [[kb/mitre/attack/software/S0193-forfiles\|S0193]] | Forfiles | [[kb/mitre/attack/software/S0193-forfiles\|Forfiles]] can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE has the ability to search for files on the compromised host.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can enumerate drives and their types. It can also change file permissions using cacls.exe.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can check for the existence of files, including its own components, as well as retrieve a list of logical drives.[^1] [^2]  |
| [S0208](https://attack.mitre.org/software/S0208) | Pasam | Pasam creates a backdoor through which remote attackers can retrieve lists of files.[^1]  |
| [S0211](https://attack.mitre.org/software/S0211) | Linfo | Linfo creates a backdoor through which remote attackers can list contents of drives and search for files.[^1]  |
| [S0212](https://attack.mitre.org/software/S0212) | CORALDECK | CORALDECK searches for specified files.[^1]  |
| [S0216](https://attack.mitre.org/software/S0216) | POORAIM | POORAIM can conduct file browsing.[^1]  |
| [S0219](https://attack.mitre.org/software/S0219) | WINERACK | WINERACK can enumerate files and directories.[^1]  |
| [S0226](https://attack.mitre.org/software/S0226) | Smoke Loader | Smoke Loader recursively searches through directories for files.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can gather victim drive information.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook has a command to list files on a system.[^1]  |
| [S0235](https://attack.mitre.org/software/S0235) | CrossRAT | CrossRAT can list all files on a system.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects a list of files and directories in C:\ with the command `dir /s /a c:\ >> "C:\windows\TEMP\[RANDOM].tmp"`.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT collects the volumes mapped on the system, and also steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc lists files in directories.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot searches for files on the victim's machine.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT has the ability to gather a list of files and directories on the infected system.[^1] [^2] [^3]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck checks its directory location in an attempt to avoid launching in a sandbox.[^1] [^2]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty gathers information on victim’s drives and has a plugin for document listing.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon lists the directories for Desktop, program files, and the user’s recently accessed files.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can obtain a list of directories.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy searches for files that are 60mb and less and contain the following extensions: .doc, .docx, .xls, .xlsx, .ppt, .pptx, .exe, .zip, and .rar. Zebrocy also runs the `echo %APPDATA%` command to list the contents of the directory.[^1] [^2] [^3]  Zebrocy can obtain the current execution path as well as perform drive enumeration.[^4] [^5]   |
| [S0252](https://attack.mitre.org/software/S0252) | Brave Prince | Brave Prince gathers file and directory information from the victim’s machine.[^1]  |
| [S0255](https://attack.mitre.org/software/S0255) | DDKONG | DDKONG lists files on the victim’s machine.[^1]  |
| [S0259](https://attack.mitre.org/software/S0259) | InnaputRAT | InnaputRAT enumerates directories and obtains file attributes on a system.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can list information about files in a directory and recently opened or used documents. InvisiMole can also search for specific files by supplied file mask.[^1]  |
| [S0263](https://attack.mitre.org/software/S0263) | TYPEFRAME | TYPEFRAME can search directories for files on the victim’s machine.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar finds a specified directory, lists the files and metadata about those files.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot searches the system for all of the following file extensions: .avi, .mov, .mkv, .mpeg, .mpeg4, .mp4, .mp3, .wav, .ogg, .jpeg, .jpg, .png, .bmp, .gif, .tiff, .ico, .xlsx, and .zip. It can also obtain browsing history, cookies, and plug-in information.[^1] [^2]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal can retrieve a file listing from the system.[^1] [^2]   |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE has a command to search for files on the victim’s machine.[^1]  |
| [S0272](https://attack.mitre.org/software/S0272) | NDiskMonitor | NDiskMonitor can obtain a list of all files and directories as well as logical drives.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT has the capability to gather the victim's current directory.[^1]  |
| [S0277](https://attack.mitre.org/software/S0277) | FruitFly | FruitFly looks for specific files and file types.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can browse file systems.[^1] [^2]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda searches for specific directories on the victim’s machine.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can search for files on the infected machine.[^1] [^2]  |
| [S0337](https://attack.mitre.org/software/S0337) | BadPatch | BadPatch searches for files with specific file extensions.[^1]  |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia can perform a recursive directory listing for all volume drives available on the victim's machine and can also fetch specific files by their paths.[^1]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can collect information on the Windows directory and searches for compressed RAR files on the host.[^1] [^2] [^3]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can recursively search for files in folders and collects files from the desktop with certain extensions.[^1]  |
| [S0345](https://attack.mitre.org/software/S0345) | Seasalt | Seasalt has the capability to identify the drive type on a victim.[^1]  |
| [S0346](https://attack.mitre.org/software/S0346) | OceanSalt | OceanSalt can extract drive information from the endpoint and search files on the system.[^1]  |
| [S0347](https://attack.mitre.org/software/S0347) | AuditCred | AuditCred can search through folders and files on the system.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT checks its current working directory upon execution and also contains watchdog functionality that ensures its executable is located in the correct path (else it will rewrite the payload).[^1]  |
| [S0350](https://attack.mitre.org/software/S0350) | zwShell | zwShell can browse the file system.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can obtain victim drive information as well as a list of folders in C:\Program Files.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis has several commands to search directories for files.[^1] [^2]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | A version of KONNI searches for filenames created with a previous version of the malware, suggesting different versions targeted the same victims and the versions may work together.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] includes various modules for finding files of interest on hosts and network shares.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry searches for variety of user files by file extension before encrypting them using RSA and AES, including Office, PDF, image, audio, video, source code, archive/compression format, and key and certificate files.[^2] [^1]  |
| [S0368](https://attack.mitre.org/software/S0368) | NotPetya | NotPetya searches for files ending with dozens of different file extensions prior to encryption.[^1]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi searches for files on the system. [^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has been observed enumerating system drives and partitions.[^1] 	 |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate files on the local file system and includes a module for enumerating recently accessed files.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can browse file systems using a file manager module.[^1]  |
| [S0387](https://attack.mitre.org/software/S0387) | KeyBoy | KeyBoy has a command to launch a file browser or explorer on the system.[^1]  |
| [S0402](https://attack.mitre.org/software/S0402) | OSX/Shlayer | OSX/Shlayer has used the command `appDir="$(dirname $(dirname "$currentDir"))"` and `$(dirname "$(pwd -P)")` to construct installation paths.[^1] [^2]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete produces file listings in order to search for files to be exfiltrated.[^1] [^2] [^3]  |
| [S0410](https://attack.mitre.org/software/S0410) | Fysbis | Fysbis has the ability to search for files.[^1]   |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell has a command to open a file manager and explorer on the system.[^1]   |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has used `dir` to search for "programfiles" and "appdata".[^1] 	 |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has the ability to list files upon receiving the `ls` command from C2.[^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to retrieve a list of files in a given directory as well as drives and drive types.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.[^1]  |
| [S0435](https://attack.mitre.org/software/S0435) | PLEAD | PLEAD has the ability to list drives and files on the compromised host.[^1] [^2]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie has the ability to discover drive information on the infected host.[^1]  |
| [S0437](https://attack.mitre.org/software/S0437) | Kivars | Kivars has the ability to list drives on the infected host.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor has a plugin that enumerates files with specific extensions on all hard disk drives and stores file information in encrypted log files.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum has used DriveLetterView to enumerate drive information.[^1]  |
| [S0443](https://attack.mitre.org/software/S0443) | MESSAGETAP | MESSAGETAP checks for the existence of two configuration files (keyword_parm.txt and parm.txt) and attempts to read the files every 30 seconds.[^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat can list directories.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has enumerated files and folders on all mounted drives.[^1] 	 |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot can search for specific files on an infected host.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can enumerate information about files from the infected system, including file size, attributes, creation time, last access time, and write time. Rising Sun can enumerate the compilation timestamp of Windows executable files.[^1] 	 |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can detect the victim's file or folder list.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has searched the Program Files directories for specific folders and has searched for strings related to its mutexes.[^1] [^2] [^3]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to gather metadata from a file and to search for file and directory names.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can collect directory and file lists.[^1] [^2] 	 |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to get directory listings or drive information on a compromised host.[^1]  |
| [S0466](https://attack.mitre.org/software/S0466) | WindTail | WindTail has the ability to enumerate the users home directory and the path to its own application bundle.[^1] [^2]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to index files from drives, user profiles, and removable drives.[^1]  |
| [S0468](https://attack.mitre.org/software/S0468) | Skidmap | Skidmap has checked for the existence of specific files including `/usr/sbin/setenforce` and ` /etc/selinux/config`. It also has the ability to monitor the cryptocurrency miner file and process. [^1]   |
| [S0472](https://attack.mitre.org/software/S0472) | down_new | down_new has the ability to list the directories on a compromised host.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger has the ability to browse files in directories such as Program Files and the Desktop.[^1]   |
| [S0475](https://attack.mitre.org/software/S0475) | BackConfig | BackConfig has the ability to identify folders and files related to previous infections.[^1] 	 |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover specified filetypes and log files on a targeted system.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can parse the hard drive on a compromised host to identify specific file extensions.[^1]  |
| [S0492](https://attack.mitre.org/software/S0492) | CookieMiner | CookieMiner has looked for files in the user's home directory with "wallet" in their name using `find`.[^1]  |
| [S0493](https://attack.mitre.org/software/S0493) | GoldenSpy | GoldenSpy has included a program "ExeProtector", which monitors for the existence of GoldenSpy on the infected system and redownloads if necessary.[^1] 	 |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil has the ability to identify specific files and directories that are not to be encrypted.[^1] [^2] [^3] [^4] [^5] [^6]  |
| [S0497](https://attack.mitre.org/software/S0497) | Dacls | Dacls can scan directories on a compromised host.[^1]  |
| [S0498](https://attack.mitre.org/software/S0498) | Cryptoistic | Cryptoistic can scan a directory to identify files for deletion.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can enumerate directories on target machines.[^1]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang has the ability to list directories.[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN can search, read, write, move, and execute files.[^1] [^2]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY can enumerate files and directories on a compromised host.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA can enumerate files and directories.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can enumerate the victim's desktop.[^1] [^2]  |
| [S0547](https://attack.mitre.org/software/S0547) | DropBook | DropBook can collect the names of all files and folders in the Program Files directories.[^1] [^2]   |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST had commands to enumerate files and directories.[^1] [^2]  |
| [S0562](https://attack.mitre.org/software/S0562) | SUNSPOT | SUNSPOT enumerated the Orion software Visual Studio solution directory path.[^1]  |
| [S0564](https://attack.mitre.org/software/S0564) | BlackMould | BlackMould has the ability to find files on the targeted system.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack can list files on available disk volumes.[^1] [^2]  |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell can search for files in directories.[^1]   |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can discover files on a local system.[^1]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex can parse the available drives and directories to determine which files to encrypt.[^1]   |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack can retrieve file listings from the victim machine.[^1]  |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | TAINTEDSCRIBE can use `DirectoryList` to enumerate files in a specified directory.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin can use the command code `do_vslist` to send file names, size, and status to C2.[^1]  |
| [[kb/mitre/attack/software/S0592-remoteutilities\|S0592]] | RemoteUtilities | [[kb/mitre/attack/software/S0592-remoteutilities\|RemoteUtilities]] can enumerate files and directories on a target machine.[^1]  |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell has the ability to list files and file characteristics including extension, size, ownership, and permissions.[^1]  |
| [S0599](https://attack.mitre.org/software/S0599) | Kinsing | Kinsing has used the find command to search for specific files.[^1]  |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki has resolved the path of a process PID to use as a script argument.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet uses a driver to scan for specific filesystem driver objects.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer’s data wiper component enumerates specific files on all the Windows drives.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk has used the `FindNextFile` command as part of its file deletion process.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist has the ability to search for specific files.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop has searched folders and subfolders for files to encrypt.[^1]  |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker can enumerate files and directories just prior to encryption.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can execute `enum` to enumerate files in storage on a compromised system.[^1]  |
| [S0616](https://attack.mitre.org/software/S0616) | DEATHRANSOM | DEATHRANSOM can use loop operations to enumerate directories on a compromised host.[^1]  |
| [S0618](https://attack.mitre.org/software/S0618) | FIVEHANDS | FIVEHANDS has the ability to enumerate files on a compromised host in order to encrypt files with specific extensions.[^1] [^2]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed has the ability to search for .txt, .ppt, .hwp, .pdf, and .doc files in specified directories.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape |  Siloscape searches for the Kubernetes config file and other related files using a regular expression.[^1]   |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can enumerate files by using a variety of functions.[^1]  |
| [S0628](https://attack.mitre.org/software/S0628) | FYAnti | FYAnti can search the `C:\Windows\Microsoft.NET\` directory for files of a specified size.[^1]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can use a file exfiltration tool to collect recently changed files with specific extensions.[^1]  |
| [S0630](https://attack.mitre.org/software/S0630) | Nebulae | Nebulae can list files and directories on a compromised host.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent has the ability to enumerate files and directories on a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can enumerate files on a target system.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox can search for specific files and directories on a machine.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk has the ability to enumerate files on a targeted system.[^1] [^2]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon has searched for specific files prior to encryption.[^1]  |
| [S0642](https://attack.mitre.org/software/S0642) | BADFLICK | BADFLICK has searched for files on the infected host.[^1]  |
| [S0643](https://attack.mitre.org/software/S0643) | Peppy | Peppy can identify specific files for exfiltration.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT has the ability to recursively enumerate files on an infected endpoint.[^1]  |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian can search for specific files and list directories.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can identify whether it has been run previously on a host by checking for a specified folder.[^1]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon has searched for files on the system, such as documents located in the desktop folder.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can look for files carrying specific extensions such as: .rtf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pps, .ppsx, .txt, .gpg, .pkr, .kdbx, .key, and .jpb.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can enumerate files and collect associated metadata.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET has used `mdfind` to enumerate a list of apps known to grant screen sharing permissions and leverages a module to run the command `ls -la ~/Desktop`.[^1] [^2] <br> |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol has a command to traverse the files and directories in a given path.[^1]   |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can browse directories on a compromised host.[^1] [^2]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb's loader can check for the FoggyWeb backdoor .pri file on a compromised AD FS server.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can search files on a compromised host.[^2] [^1]  |
| [S0665](https://attack.mitre.org/software/S0665) | ThreatNeedle | ThreatNeedle can obtain file and directory information.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can retrieve data from specific Windows directories, as well as open random files as part of [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion\|Virtualization/Sandbox Evasion]].[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can enumerate directories on a compromise host.[^1]  |
| [S0672](https://attack.mitre.org/software/S0672) | Zox | Zox can enumerate files on a compromised host.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman has the ability to enumerate file and folder names.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can enumerate drives and list the contents of the C: drive on a victim's computer.[^1]  |
| [S0686](https://attack.mitre.org/software/S0686) | QuietSieve | QuietSieve can search files on the target host by extension, including doc, docx, xls, rtf, odt, txt, jpg, pdf, rar, zip, and 7z.[^1]   |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can use the Linux API `statvfs` to enumerate the current working directory.[^1] [^2]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can locate files based on hardcoded file extensions.[^3] [^2] [^1] [^4]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.[^1]   |
| [S0693](https://attack.mitre.org/software/S0693) | CaddyWiper | CaddyWiper can enumerate all files and directories on a compromised host.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can enumerate common folders such as My Documents, Desktop, and AppData.[^1] [^2]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can search for a specific file on the compromised computer and can enumerate files in Desktop, Downloads, and Documents folders.[^1]  |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can search for specific file extensions, including zipped files.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot can search a compromised host for specific files.[^1]  |
| [S1022](https://attack.mitre.org/software/S1022) | IceApple | The IceApple Directory Lister module can list information about files and directories including creation time, last write time, name, and size.[^1]  |
| [S1023](https://attack.mitre.org/software/S1023) | CreepyDrive | CreepyDrive can specify the local file path to upload files from.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has searched for folders associated with antivirus software.[^1]  |
| [S1027](https://attack.mitre.org/software/S1027) | Heyoka Backdoor | Heyoka Backdoor has the ability to search the compromised host for files.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT | Action RAT has the ability to collect drive and file information on an infected machine.[^1]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull | PingPull can enumerate storage volumes and folder contents of a compromised host.[^1]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can enumerate files on a compromised host.[^1]  |
| [[kb/mitre/attack/software/S1040-rclone\|S1040]] | Rclone | [[kb/mitre/attack/software/S1040-rclone\|Rclone]] can list files and directories with the `ls`, `lsd`, and `lsl` commands.[^1]  |
| [S1042](https://attack.mitre.org/software/S1042) | SUGARDUMP | SUGARDUMP can search for and collect data from specific Chrome, Opera, Microsoft Edge, and Firefox files, including any folders that have the string `Profile` in its name.[^1]  |
| [S1043](https://attack.mitre.org/software/S1043) | ccf32 | ccf32 can parse collected files to identify specific file extensions.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can identify files with .doc, .docx, .ppt, .pptx, .xls, .xlsx, and .pdf extensions and specific timestamps for collection.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has searched for files and directories on a compromised network.[^1] [^2]  |
| [S1058](https://attack.mitre.org/software/S1058) | Prestige | Prestige can traverse the file system to discover files to encrypt by identifying specific extensions defined in a hardcoded list.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can recursively enumerate files in an operator-provided directory.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can search for files and directories.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can list all files and their associated attributes, including filename, type, owner, creation time, last access time, last write time, size, and permissions.[^1]   |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can enumerate files for encryption.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can enumerate specific files for encryption.[^3] [^1] [^5] [^6] [^8] [^4] [^7] [^2]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can identify specific files and directories to exclude from the encryption process.[^1] [^2] [^3]  |
| [S1089](https://attack.mitre.org/software/S1089) | SharpDisco | SharpDisco can identify recently opened files by using an LNK format parser to extract the original file path from LNK files found in either `%USERPROFILE%\Recent` (Windows XP) or `%APPDATA%\Microsoft\Windows\Recent` (newer Windows versions) .[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can use a file monitor to identify .lnk, .doc, .docx, .xls, .xslx, and .pdf files.[^1]  |
| [S1096](https://attack.mitre.org/software/S1096) | Cheerscrypt | Cheerscrypt can search for log and VMware-related files with .log, .vmdk, .vmem, .vswp, and .vmsn extensions.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai can use a specific module for file enumeration.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja has the ability to enumerate directory content.[^1] [^2]  |
| [S1101](https://attack.mitre.org/software/S1101) | LoFiSe | LoFiSe can monitor the file system to identify files less than 6.4 MB in size with file extensions including .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pdf, .rtf, .tif, .odt, .ods, .odp, .eml, and .msg.[^1]  |
| [S1102](https://attack.mitre.org/software/S1102) | Pcexter | Pcexter has the ability to search for files in specified directories.[^1]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER will survey the contents of system files during installation.[^1]  |
| [S1109](https://attack.mitre.org/software/S1109) | PACEMAKER | PACEMAKER can parse `/proc/"process_name"/cmdline` to look for the string `dswsd` within the command line.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | Some versions of DarkGate search for the hard-coded folder `C:\Program Files\e Carte Bleue`.[^1]  |
| [S1114](https://attack.mitre.org/software/S1114) | ZIPLINE | ZIPLINE can find and append specific files on Ivanti Connect Secure VPNs based upon received commands.[^1]  |
| [S1121](https://attack.mitre.org/software/S1121) | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can monitor for system upgrade events by checking for the presence of `/tmp/data/root/dev`.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu searches for various filesystem paths to determine what banking applications are installed on the victim’s machine.[^1]  |
| [S1125](https://attack.mitre.org/software/S1125) | AcidRain | AcidRain identifies specific files and directories in the Linux operating system associated with storage devices.[^1]  |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira examines files prior to encryption to determine if they meet requirements for encryption and can be encrypted by the ransomware. These checks are performed through native Windows functions such as `GetFileAttributesW`.[^1] [^2]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin will check to see if the initial executing script is located on the user's Desktop as an anti-analysis check.[^1]  |
| [S1135](https://attack.mitre.org/software/S1135) | MultiLayer Wiper | MultiLayer Wiper generates a list of all files and paths on the fixed drives of an infected system, enumerating all files on the system except specific folders defined in a hardcoded list.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can receive command line arguments to encrypt specific files and directories.[^1] [^2]  |
| [S1140](https://attack.mitre.org/software/S1140) | Spica | Spica can list filesystem contents on targeted systems.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb has the ability to retrieve directory listings.[^1]  |
| [S1142](https://attack.mitre.org/software/S1142) | LunarMail | LunarMail can search its staging directory for output files it has produced.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer identifies target files and directories for collection based on a configuration file.[^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP has the ability to enumerate directories for files that match a set list.[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP can enumerate files on infected devices and avoid encrypting files with .exe, .dll, 	.sys, .lnk, or . lck extensions.[^2] [^1] [^3]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can search for files associated with specific applications.[^1] [^2]  |
| [S1156](https://attack.mitre.org/software/S1156) | Manjusaka | Manjusaka can gather information about specific files on the victim system.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can enumerate files and directories.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus can collect desktop filenames.[^2] [^1] [^3]  |
| [S1162](https://attack.mitre.org/software/S1162) | Playcrypt | Playcrypt can avoid encrypting files with a .PLAY, .exe, .msi, .dll, .lnk, or .sys file extension.[^1]  |
| [S1167](https://attack.mitre.org/software/S1167) | AcidPour | AcidPour can identify specific files and directories within the Linux operating system corresponding with storage devices for follow-on wiping activity, similar to AcidRain.[^1]  |
| [S1169](https://attack.mitre.org/software/S1169) | Mango | Mango can enumerate the contents of current working or other specified directories.[^1]  |
| [S1170](https://attack.mitre.org/software/S1170) | ODAgent | ODAgent can identify the current working directory.[^1]  |
| [S1179](https://attack.mitre.org/software/S1179) | Exbyte | Exbyte enumerates all document files on an infected machine, then creates a summary of these items including filename and directory location prior to exfiltration to cloud hosting services.[^1]  |
| [S1184](https://attack.mitre.org/software/S1184) | BOLDMOVE | BOLDMOVE can list information of all files in the system recursively from the root directory or from a specified directory.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | LightSpy uses the `NSFileManager` to move, create and delete files. LightSpy can also use the assembly `bt` instruction to determine a file's executable permissions.[^1]  |
| [S1191](https://attack.mitre.org/software/S1191) | Megazord | Megazord can ignore specified directories for encryption.[^1] <br> |
| [S1194](https://attack.mitre.org/software/S1194) | Akira _v2 | Akira _v2 can target specific files and folders for encryption.[^1] [^2] [^3]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer can enumerate and collect items from local drives and folders.[^1]  |
| [S1198](https://attack.mitre.org/software/S1198) | Gomir | Gomir collects information about directory and file structures, including total number of subdirectories, total number of files, and total size of files on infected systems.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can exclude files associated with core system functions from encryption.[^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can be configured to exfiltrate specific file types.[^2] [^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can exclude files associated with core system functions from encryption.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub has the ability to only encrypt specific files.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | The Havoc interface can display a file explorer view of the compromised host.[^1]  |
| [S1234](https://attack.mitre.org/software/S1234) | SplatCloak | SplatCloak has used Windows API to identify files associated with Windows Defender and Kaspersky.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can exclude specific directories and files from encryption.[^1] [^2]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has searched for files within the victim environment for encryption and exfiltration.[^1] [^2] [^3]   Medusa Ransomware has also identified files associated with remote management services.[^1] [^2]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has identified specific directories and files for exfiltration using the `ssh_upload` command which contains subcommands of `.sdira`, `sdir`, `sfile`, `sfinda`, `sfindr`, `sfind`.[^2] [^3]  InvisibleFerret also has the capability to scan and upload files of interest from multiple OS systems through the use of scripts that check file names, file extensions, and avoids certain path names.[^1] [^4]  InvisibleFerret has utilized the `findstr` on Windows or the macOS `find` commands to search for files of interest.[^5]   |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has searched for .ldb and .log files stored in browser extension directories for collection and exfiltration.[^1] [^2] [^3]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has searched for folders, subfolders and other networked or mounted drives for follow on encryption actions.[^1]  Embargo has also iterated device volumes using `FindFirstVolumeW()` and `FindNextVolumeW()` functions and then calls the `GetVolumePathNamesForVolumeNameW()` function to retrieve a list of drive letters and mounted folder paths for each specified volume.[^1]  |
| [[kb/mitre/attack/software/S9002-diskpart\|S9002]] | Diskpart | If executed with elevated privileges, [[kb/mitre/attack/software/S9002-diskpart\|Diskpart]] can list all volumes, including virtual disks.[^1]     |
| [[kb/mitre/attack/software/S9009-trufflehog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has can browse and scan individual files and directories.[^1] [^2] [^3]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has identified specific files and directories within targeted hosts and systems for modification, execution, collection and exfiltration.[^1] [^2] [^3] [^4] [^5] [^6]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | <br>LODEINFO has the ability to designate specific files and folders to encryption.[^1] [^2]  |
| [S9027](https://attack.mitre.org/software/S9027) | ANELLDR | ANELLDR can enumerate files in the current directory to search for encrypted payload files.[^1]  |
| [S9030](https://attack.mitre.org/software/S9030) | SameCoin | SameCoin can list all system files and can avoid wiping specific directories such as Program Files, Windows, and Users.[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | The AshTag AshenOrchestrator component can enumerate files on victim hosts.[^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can target directories on victim machines for file collection.[^1] [^2]  |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has used the Microsoft Windows native `FindFirstFile()` and `FindNextFile()` to recursively enumerate directories and files on the system.[^1]  |
| [S9039](https://attack.mitre.org/software/S9039) | LazyWiper | LazyWiper can specifically target multiple files by extension including: .rar, .tar.gz, .zip, .7z, .json, .bcp, .bak, .gho, .erf, .edb, .onepkg, .pst, and .ldiff.[^1]  |

 [^1]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)
 [^2]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^3]: [FireEye APT17](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)
 [^4]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^5]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^6]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
 [^7]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)
 [^8]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^9]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
 [^10]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^11]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^12]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^13]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
 [^14]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^15]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)
 [^16]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
 [^17]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
 [^18]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
 [^19]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
 [^20]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)
 [^21]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^22]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^23]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^24]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^25]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^26]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^27]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^28]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^29]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
 [^30]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^31]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^32]: [FireEye EPS Awakens Part 2](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)
 [^33]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
 [^34]: [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)
 [^35]: [Symantec Remsec IOCs](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)
 [^36]: [Kaspersky ProjectSauron Full Report](https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf)
 [^37]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^38]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
 [^39]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^40]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^41]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^42]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^43]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
 [^44]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^45]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^46]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^47]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^48]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
 [^49]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^50]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
 [^51]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^52]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^53]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^54]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^55]: [objective-see windtail1 dec 2018](https://objective-see.com/blog/blog_0x3B.html)
 [^56]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)
 [^57]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
 [^58]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^59]: [GitHub Sliver File System August 2021](https://github.com/BishopFox/sliver/tree/master/client/command/filesystem)
 [^60]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^61]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
 [^62]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^63]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^64]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)
 [^65]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)
 [^66]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^67]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^68]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
 [^69]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^70]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^71]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^72]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^73]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
 [^74]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^75]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^76]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
 [^77]: [Microsoft WhisperGate January 2022](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
 [^78]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
 [^79]: [TechNet Dir](https://technet.microsoft.com/en-us/library/cc755121.aspx)
 [^80]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
 [^81]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^82]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
 [^83]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^84]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
 [^85]: [Camba RARSTONE](http://blog.trendmicro.com/trendlabs-security-intelligence/bkdr_rarstone-new-rat-to-watch-out-for/)
 [^86]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^87]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
 [^88]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
 [^89]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^90]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^91]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^92]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
 [^93]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
 [^94]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^95]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^96]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^97]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^98]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^99]: [Rclone](https://rclone.org)
 [^100]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^101]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^102]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
 [^103]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
 [^104]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^105]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^106]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
 [^107]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^108]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^109]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^110]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^111]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^112]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^113]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^114]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
 [^115]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^116]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^117]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
 [^118]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^119]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^120]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^121]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^122]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^123]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^124]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
 [^125]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^126]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^127]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^128]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
 [^129]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
 [^130]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
 [^131]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)
 [^132]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^133]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
 [^134]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^135]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
 [^136]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
 [^137]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^138]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
 [^139]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
 [^140]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
 [^141]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^142]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
 [^143]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
 [^144]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^145]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^146]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
 [^147]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^148]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
 [^149]: [Avertium Black Basta June 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
 [^150]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
 [^151]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^152]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
 [^153]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
 [^154]: [Uptycs Black Basta ESXi June 2022](https://www.uptycs.com/blog/black-basta-ransomware-goes-cross-platform-now-targets-esxi-systems)
 [^155]: [Trend Micro Black Basta Spotlight September 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)
 [^156]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
 [^157]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^158]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^159]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^160]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^161]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^162]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)
 [^163]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
 [^164]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^165]: [Security Affairs DustSquad Oct 2018](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)
 [^166]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)
 [^167]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
 [^168]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
 [^169]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
 [^170]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
 [^171]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
 [^172]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^173]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^174]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^175]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^176]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^177]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
 [^178]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
 [^179]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
 [^180]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
 [^181]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^182]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^183]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)
 [^184]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^185]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
 [^186]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^187]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^188]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^189]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^190]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^191]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^192]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^193]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^194]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^195]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^196]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^197]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^198]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^199]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^200]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)
 [^201]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)
 [^202]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^203]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^204]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
 [^205]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^206]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
 [^207]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^208]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^209]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
 [^210]: [Malwarebytes IssacWiper CaddyWiper March 2022 ](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)
 [^211]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^212]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)
 [^213]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^214]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^215]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
 [^216]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^217]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^218]: [Trend Micro AvosLocker Apr 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
 [^219]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^220]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^221]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^222]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
 [^223]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
 [^224]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^225]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^226]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
 [^227]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
 [^228]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
 [^229]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^230]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^231]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^232]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^233]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
 [^234]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^235]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^236]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
 [^237]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
 [^238]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^239]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
 [^240]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^241]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^242]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
 [^243]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)
 [^244]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^245]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^246]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)
 [^247]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
 [^248]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^249]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^250]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)
 [^251]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
 [^252]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^253]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^254]: [ZScaler Hacking Team](http://research.zscaler.com/2015/08/chinese-cyber-espionage-apt-group.html)
 [^255]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^256]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
 [^257]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^258]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^259]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)
 [^260]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
 [^261]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^262]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^263]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^264]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^265]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
 [^266]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^267]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^268]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^269]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^270]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^271]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^272]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^273]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^274]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^275]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
 [^276]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^277]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)
 [^278]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
 [^279]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
 [^280]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^281]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
 [^282]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^283]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^284]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^285]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^286]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^287]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^288]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^289]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
 [^290]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^291]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^292]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
 [^293]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^294]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^295]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^296]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
 [^297]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
 [^298]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^299]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^300]: [NHS UK BLINDINGCAN Aug 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)
 [^301]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^302]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^303]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^304]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
 [^305]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
 [^306]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^307]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^308]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^309]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^310]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^311]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^312]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
 [^313]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^314]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^315]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
 [^316]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^317]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^318]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^319]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^320]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
 [^321]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
 [^322]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
 [^323]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
 [^324]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^325]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^326]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^327]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^328]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
 [^329]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)
 [^330]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^331]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
 [^332]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^333]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
 [^334]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^335]: [AcidRain JAGS 2022](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)
 [^336]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^337]: [Application Bundle Manipulation Brandon Dalton](https://redcanary.com/blog/mac-application-bundles/)
 [^338]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
 [^339]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^340]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
 [^341]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^342]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^343]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
 [^344]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
 [^345]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^346]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^347]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^348]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)
 [^349]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^350]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^351]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
 [^352]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^353]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
 [^354]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^355]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^356]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^357]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^358]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^359]: [Kroll Royal Deep Dive February 2023](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
 [^360]: [Trend Micro Royal Linux ESXi February 2023](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
 [^361]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^362]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^363]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^364]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^365]: [Talos Smoke Loader July 2018](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)
 [^366]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
 [^367]: [Halcyon_CloakRansomware_Dec2024](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)
 [^368]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^369]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
 [^370]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
 [^371]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^372]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
 [^373]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
 [^374]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^375]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
 [^376]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
