---
parsed_by: focuslocust
source: commands
type: generated
---
# Control Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Control.exe

Tool page: [Control.exe](../../tools/windows/control.exe.md)

### Can be used to evade defensive countermeasures or to hide as a persistence mechanism

```text
control.exe {PATH_ABSOLUTE}:evil.dll
```

Description:

Execute evil.dll which is stored in an Alternate Data Stream (ADS).

Related ATT&CK:

- [T1218.002](../../attack/techniques/T1218.002-control-panel.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Control.yml` |
| Evidence | Command preserved from source parser. |

### Use to execute code and bypass application whitelisting

```text
control.exe {PATH_ABSOLUTE:.cpl}
```

Description:

Execute .cpl file. A CPL is a DLL file with CPlApplet export function)

Related ATT&CK:

- [T1218.002](../../attack/techniques/T1218.002-control-panel.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Control.yml` |
| Evidence | Command preserved from source parser. |
