---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0692
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0692-silenttrinity
---

## Description

[[kb/mitre/attack/software/S0692-silenttrinity|SILENTTRINITY]] is an open source remote administration and post-exploitation framework primarily written in Python that includes stagers written in Powershell, C, and Boo. [[kb/mitre/attack/software/S0692-silenttrinity|SILENTTRINITY]] was used in a 2019 campaign against Croatian government agencies by unidentified cyber actors.[^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can create a memory dump of LSASS via the `MiniDumpWriteDump Win32` API call.[^1]  |
| [[kb/mitre/attack/techniques/T1007-system-service-discovery\|T1007]] | System Service Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can search for modifiable services that could be used for privilege escalation.[^1]  |
| [[kb/mitre/attack/techniques/T1010-application-window-discovery\|T1010]] | Application Window Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.[^1]  |
| [[kb/mitre/attack/techniques/T1012-query-registry\|T1012]] | Query Registry | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.[^1]  |
| [[kb/mitre/attack/techniques/T1018-remote-system-discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate and collect the properties of domain computers.[^1]  |
| [[kb/mitre/attack/techniques/T1021.003-distributed-component-object-model\|T1021.003]] | Distributed Component Object Model | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use `System` namespace methods to execute lateral movement using DCOM.[^1]  |
| [[kb/mitre/attack/techniques/T1021.006-windows-remote-management\|T1021.006]] | Windows Remote Management | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] tracks `TrustedHosts` and can move laterally to these targets via WinRM.[^1]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can gather a list of logged on users.[^1]   |
| [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can transfer files from an infected host to the C2 server.[^1]  |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can scan for open ports on a compromised machine.[^1]  |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use WMI for lateral movement.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can inject shellcode directly into Excel.exe or a specific process.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] has a keylogging capability.[^1]  |
| [[kb/mitre/attack/techniques/T1056.002-gui-input-capture\|T1056.002]] | GUI Input Capture | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]]'s `credphisher.py` module can prompt a current user for their credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use PowerShell to execute commands.[^1]  |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use `cmd.exe` to enable lateral movement using DCOM.[^1]  |
| [[kb/mitre/attack/techniques/T1059.006-python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] is written in Python and can use multiple Python scripts for execution on targeted systems.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1069.001-local-groups\|T1069.001]] | Local Groups | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can obtain a list of local groups and members.[^1]  |
| [[kb/mitre/attack/techniques/T1069.002-domain-groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use `System.DirectoryServices` namespace to retrieve domain group information.[^1]  |
| [[kb/mitre/attack/techniques/T1070-indicator-removal\|T1070]] | Indicator Removal | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can remove artifacts from the compromised host, including created Registry keys.[^1]  |
| [[kb/mitre/attack/techniques/T1070.004-file-deletion\|T1070.004]] | File Deletion | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can remove files from the compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can collect information related to a compromised host, including OS version.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.[^1]   |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can use `System.Security.AccessControl` namespaces to retrieve domain user information.[^1]    |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can load additional files and tools, including [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]].[^1]  |
| [[kb/mitre/attack/techniques/T1106-native-api\|T1106]] | Native API | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.[^1]  |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).[^1]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can take a screenshot of the current desktop.[^1]  |
| [[kb/mitre/attack/techniques/T1115-clipboard-data\|T1115]] | Clipboard Data | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.[^1]    |
| [[kb/mitre/attack/techniques/T1124-system-time-discovery\|T1124]] | System Time Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can collect start time information from a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1134.001-token-impersonation-theft\|T1134.001]] | Token Impersonation/Theft | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can find a process owned by a specific user and impersonate the associated token.[^1]  |
| [[kb/mitre/attack/techniques/T1134.003-make-and-impersonate-token\|T1134.003]] | Make and Impersonate Token | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can make tokens from known credentials.[^1]   |
| [[kb/mitre/attack/techniques/T1135-network-share-discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate shares on a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1518.001-security-software-discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can determine if an anti-virus product is installed through the resolution of the service's virtual SID.[^1]  |
| [[kb/mitre/attack/techniques/T1543.003-windows-service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can establish persistence by creating a new service.[^1]  |
| [[kb/mitre/attack/techniques/T1546.001-change-default-file-association\|T1546.001]] | Change Default File Association | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can conduct an image hijack of an `.msc` file extension as part of its UAC bypass process.[^1]  |
| [[kb/mitre/attack/techniques/T1546.003-windows-management-instrumentation-event-subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can create a WMI Event to execute a payload for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1546.015-component-object-model-hijacking\|T1546.015]] | Component Object Model Hijacking | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can add a CLSID key for payload execution through `Registry.CurrentUser.CreateSubKey("Software\\Classes\\CLSID\\{" + clsid + "}\\InProcServer32")`.[^1]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can establish a LNK file in the startup folder for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] contains a number of modules that can bypass UAC, including through Window's Device Manager, Manage Optional Features, and an image hijack on the `.msc` file extension.[^1]     |
| [[kb/mitre/attack/techniques/T1552.006-group-policy-preferences\|T1552.006]] | Group Policy Preferences | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] has a module that can extract cached GPP passwords.[^1]   |
| [[kb/mitre/attack/techniques/T1555.003-credentials-from-web-browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can collect clear text web credentials for Internet Explorer/Edge.[^1]  |
| [[kb/mitre/attack/techniques/T1555.004-windows-credential-manager\|T1555.004]] | Windows Credential Manager | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can gather Windows Vault credentials.[^1]   |
| [[kb/mitre/attack/techniques/T1556-modify-authentication-process\|T1556]] | Modify Authentication Process | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.[^1]  |
| [[kb/mitre/attack/techniques/T1558.003-kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] contains a module to conduct Kerberoasting.[^1]  |
| [[kb/mitre/attack/techniques/T1559.001-component-object-model\|T1559.001]] | Component Object Model | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can insert malicious shellcode into Excel.exe using a `Microsoft.Office.Interop` object.[^1]   |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] has the ability to set its window state to hidden.[^1]  |
| [[kb/mitre/attack/techniques/T1620-reflective-code-loading\|T1620]] | Reflective Code Loading | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can run a .NET executable within the memory of a sacrificial process by loading the CLR.[^1]    |
| [[kb/mitre/attack/techniques/T1680-local-storage-discovery\|T1680]] | Local Storage Discovery | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can collect information related to a compromised host, including a list of drives.[^1]  |
| [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools\|T1685]] | Disable or Modify Tools | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]]'s `amsiPatch.py` module can disable Antimalware Scan Interface (AMSI) functions.[^1]  |
| [[kb/mitre/attack/techniques/T1689-downgrade-attack\|T1689]] | Downgrade Attack | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can downgrade NTLM to capture NTLM hashes.[^1]   |
| [[kb/mitre/attack/techniques/T1690-prevent-command-history-logging\|T1690]] | Prevent Command History Logging | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory.[^1]  |

 [^1]: [Security Affairs SILENTTRINITY July 2019](https://securityaffairs.co/wordpress/88021/apt/croatia-government-silenttrinity-malware.html)
 [^2]: [GitHub SILENTTRINITY March 2022](https://github.com/byt3bl33d3r/SILENTTRINITY)
 [^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^4]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)
