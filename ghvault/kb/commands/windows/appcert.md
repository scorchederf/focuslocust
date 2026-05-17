---
parsed_by: focuslocust
source: commands
type: generated
---
# AppCert Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## AppCert.exe

Tool page: [AppCert.exe](../../tools/windows/appcert.exe.md)

### Performs execution of specified file, can be used as a defense evasion

```text
appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml}
```

Description:

Execute an executable file via the Windows App Certification Kit command-line tool.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appcert.yml` |
| Evidence | Command preserved from source parser. |

### Execute custom made MSI file with malicious code

```text
appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.msi} -setupcommandline /q -reportoutputpath {PATH_ABSOLUTE:.xml}
```

Description:

Install an MSI file via an msiexec instance spawned via appcert.exe as parent process.

Related ATT&CK:

- [T1218.007](../../attack/techniques/T1218.007-msiexec.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appcert.yml` |
| Evidence | Command preserved from source parser. |
