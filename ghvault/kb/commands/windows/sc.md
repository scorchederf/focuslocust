---
parsed_by: focuslocust
source: commands
type: generated
---
# Sc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Sc.exe

Tool page: [Sc.exe](../../tools/windows/sc.exe.md)

### Execute binary file hidden inside an alternate data stream

```text
sc create evilservice binPath="\"c:\\ADS\\file.txt:cmd.exe\" /c echo works > \"c:\ADS\works.txt\"" DisplayName= "evilservice" start= auto\ & sc start evilservice
```

Description:

Creates a new service and executes the file stored in the ADS.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sc.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary file hidden inside an alternate data stream

```text
sc config {ExistingServiceName} binPath="\"c:\\ADS\\file.txt:cmd.exe\" /c echo works > \"c:\ADS\works.txt\"" & sc start {ExistingServiceName}
```

Description:

Modifies an existing service and executes the file stored in the ADS.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sc.yml` |
| Evidence | Command preserved from source parser. |
