---
parsed_by: focuslocust
source: commands
type: generated
---
# Tracker Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Tracker.exe

Tool page: [Tracker.exe](../../tools/windows/tracker.exe.md)

### Injection of locally stored DLL file into target process.

```text
Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
```

Description:

Use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed it can be used to bypass application whitelisting solutions.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Tracker.yml` |
| Evidence | Command preserved from source parser. |

### Injection of locally stored DLL file into target process.

```text
Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
```

Description:

Use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed it can be used to bypass application whitelisting solutions.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Tracker.yml` |
| Evidence | Command preserved from source parser. |
