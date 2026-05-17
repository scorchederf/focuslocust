---
parsed_by: focuslocust
source: commands
type: generated
---
# coregen Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## coregen.exe

Tool page: [coregen.exe](../../tools/windows/coregen.exe.md)

### Execute DLL code

```text
coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
```

Description:

Loads the target .DLL in arbitrary path specified with /L.

Related ATT&CK:

- [T1055](../../attack/techniques/T1055-process-injection.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Coregen.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL code

```text
coregen.exe dummy_assembly_name
```

Description:

Loads the coreclr.dll in the corgen.exe directory (e.g. C:\Program Files\Microsoft Silverlight\5.1.50918.0).

Related ATT&CK:

- [T1055](../../attack/techniques/T1055-process-injection.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Coregen.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL code

```text
coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
```

Description:

Loads the target .DLL in arbitrary path specified with /L. Since binary is signed it can also be used to bypass application whitelisting solutions.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Coregen.yml` |
| Evidence | Command preserved from source parser. |
