---
parsed_by: focuslocust
source: mitre
type: generated
---
# SILENTTRINITY

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0692` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

SILENTTRINITY is an open source remote administration and post-exploitation framework primarily written in Python that includes stagers written in Powershell, C, and Boo. SILENTTRINITY was used in a 2019 campaign against Croatian government agencies by unidentified cyber actors.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/silenttrinity.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a memory dump of LSASS via the `MiniDumpWriteDump Win32` API call.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1007 - System Service Discovery](../../attack/techniques/T1007-system-service-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can search for modifiable services that could be used for privilege escalation.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1010 - Application Window Discovery](../../attack/techniques/T1010-application-window-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1012 - Query Registry](../../attack/techniques/T1012-query-registry.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate and collect the properties of domain computers.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1021.003 - Distributed Component Object Model](../../attack/techniques/T1021.003-distributed-component-object-model.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System` namespace methods to execute lateral movement using DCOM.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1021.006 - Windows Remote Management](../../attack/techniques/T1021.006-windows-remote-management.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) tracks `TrustedHosts` and can move laterally to these targets via WinRM.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather a list of logged on users.(Citation: GitHub SILENTTRINITY Modules July 2019)  |
| [T1041 - Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can transfer files from an infected host to the C2 server.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can scan for open ports on a compromised machine.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use WMI for lateral movement.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can inject shellcode directly into Excel.exe or a specific process.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has a keylogging capability.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1056.002 - GUI Input Capture](../../attack/techniques/T1056.002-gui-input-capture.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692)'s `credphisher.py` module can prompt a current user for their credentials.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use PowerShell to execute commands.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `cmd.exe` to enable lateral movement using DCOM.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1059.006 - Python](../../attack/techniques/T1059.006-python.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) is written in Python and can use multiple Python scripts for execution on targeted systems.(Citation: GitHub SILENTTRINITY March 2022)(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1069.001 - Local Groups](../../attack/techniques/T1069.001-local-groups.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can obtain a list of local groups and members.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1069.002 - Domain Groups](../../attack/techniques/T1069.002-domain-groups.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System.DirectoryServices` namespace to retrieve domain group information.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1070 - Indicator Removal](../../attack/techniques/T1070-indicator-removal.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can remove artifacts from the compromised host, including created Registry keys.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1070.004 - File Deletion](../../attack/techniques/T1070.004-file-deletion.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can remove files from the compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including OS version.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.(Citation: GitHub SILENTTRINITY Modules July 2019)  |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System.Security.AccessControl` namespaces to retrieve domain user information.(Citation: GitHub SILENTTRINITY Modules July 2019)   |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can load additional files and tools, including [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can take a screenshot of the current desktop.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1115 - Clipboard Data](../../attack/techniques/T1115-clipboard-data.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.(Citation: Github_SILENTTRINITY)   |
| [T1124 - System Time Discovery](../../attack/techniques/T1124-system-time-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect start time information from a compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1134.001 - Token Impersonation／Theft](../../attack/techniques/T1134.001-token-impersonation-theft.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can find a process owned by a specific user and impersonate the associated token.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1134.003 - Make and Impersonate Token](../../attack/techniques/T1134.003-make-and-impersonate-token.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can make tokens from known credentials.(Citation: Github_SILENTTRINITY)  |
| [T1135 - Network Share Discovery](../../attack/techniques/T1135-network-share-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate shares on a compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1518.001 - Security Software Discovery](../../attack/techniques/T1518.001-security-software-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can determine if an anti-virus product is installed through the resolution of the service's virtual SID.(Citation: Security Affairs SILENTTRINITY July 2019) |
| [T1543.003 - Windows Service](../../attack/techniques/T1543.003-windows-service.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can establish persistence by creating a new service.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1546.001 - Change Default File Association](../../attack/techniques/T1546.001-change-default-file-association.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can conduct an image hijack of an `.msc` file extension as part of its UAC bypass process.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1546.003 - Windows Management Instrumentation Event Subscription](../../attack/techniques/T1546.003-windows-management-instrumentation-event-subscription.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a WMI Event to execute a payload for persistence.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1546.015 - Component Object Model Hijacking](../../attack/techniques/T1546.015-component-object-model-hijacking.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can add a CLSID key for payload execution through `Registry.CurrentUser.CreateSubKey("Software\\Classes\\CLSID\\{" + clsid + "}\\InProcServer32")`.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can establish a LNK file in the startup folder for persistence.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) contains a number of modules that can bypass UAC, including through Window's Device Manager, Manage Optional Features, and an image hijack on the `.msc` file extension.(Citation: GitHub SILENTTRINITY Modules July 2019)    |
| [T1552.006 - Group Policy Preferences](../../attack/techniques/T1552.006-group-policy-preferences.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has a module that can extract cached GPP passwords.(Citation: GitHub SILENTTRINITY Modules July 2019)  |
| [T1555.003 - Credentials from Web Browsers](../../attack/techniques/T1555.003-credentials-from-web-browsers.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect clear text web credentials for Internet Explorer/Edge.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1555.004 - Windows Credential Manager](../../attack/techniques/T1555.004-windows-credential-manager.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather Windows Vault credentials.(Citation: GitHub SILENTTRINITY Modules July 2019)  |
| [T1556 - Modify Authentication Process](../../attack/techniques/T1556-modify-authentication-process.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1558.003 - Kerberoasting](../../attack/techniques/T1558.003-kerberoasting.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) contains a module to conduct Kerberoasting.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1559.001 - Component Object Model](../../attack/techniques/T1559.001-component-object-model.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can insert malicious shellcode into Excel.exe using a `Microsoft.Office.Interop` object.(Citation: Github_SILENTTRINITY)  |
| [T1564.003 - Hidden Window](../../attack/techniques/T1564.003-hidden-window.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has the ability to set its window state to hidden.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1620 - Reflective Code Loading](../../attack/techniques/T1620-reflective-code-loading.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can run a .NET executable within the memory of a sacrificial process by loading the CLR.(Citation: Github_SILENTTRINITY)   |
| [T1680 - Local Storage Discovery](../../attack/techniques/T1680-local-storage-discovery.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including a list of drives.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1685 - Disable or Modify Tools](../../attack/techniques/T1685-disable-or-modify-tools.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692)'s `amsiPatch.py` module can disable Antimalware Scan Interface (AMSI) functions.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [T1689 - Downgrade Attack](../../attack/techniques/T1689-downgrade-attack.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can downgrade NTLM to capture NTLM hashes.(Citation: Github_SILENTTRINITY)  |
| [T1690 - Prevent Command History Logging](../../attack/techniques/T1690-prevent-command-history-logging.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/silenttrinity.md)

## Evidence Excerpt

```text
created: '2022-03-23T19:34:30.486Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[SILENTTRINITY](https://attack.mitre.org/software/S0692) is an open source remote administration and post-exploitation
framework primarily written in Python that includes stagers written in Powershell, C, and Boo. [SILENTTRINITY](https://attack.mitre.org/software/S0692)
was used in a 2019 campaign against Croatian government agencies by unidentified cyber actors.(Citation: GitHub SILENTTRINITY
March 2022)(Citation: Security Affairs SILENTTRINITY July 2019)'
external_references:
- external_id: S0692
```
