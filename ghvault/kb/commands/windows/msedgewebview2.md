---
parsed_by: focuslocust
source: commands
type: generated
---
# msedgewebview2 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## msedgewebview2.exe

Tool page: [msedgewebview2.exe](../../tools/windows/msedgewebview2.exe.md)

### Proxy execution of binary

```text
msedgewebview2.exe --no-sandbox --browser-subprocess-path="{PATH_ABSOLUTE:.exe}"
```

Description:

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified executable as its subprocess.

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedgewebview2.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of binary

```text
msedgewebview2.exe --utility-cmd-prefix="{CMD}"
```

Description:

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess.

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedgewebview2.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of binary

```text
msedgewebview2.exe --disable-gpu-sandbox --gpu-launcher="{CMD}"
```

Description:

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess.

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedgewebview2.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of binary

```text
msedgewebview2.exe --no-sandbox --renderer-cmd-prefix="{CMD}"
```

Description:

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess.

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedgewebview2.yml` |
| Evidence | Command preserved from source parser. |
