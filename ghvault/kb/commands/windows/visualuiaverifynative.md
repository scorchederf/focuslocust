---
parsed_by: focuslocust
source: commands
type: generated
---
# VisualUiaVerifyNative Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## VisualUiaVerifyNative.exe

Tool page: [VisualUiaVerifyNative.exe](../../tools/windows/visualuiaverifynative.exe.md)

### Execute proxied payload with Microsoft signed binary to bypass WDAC policies

```text
VisualUiaVerifyNative.exe
```

Description:

Generate Serialized gadget and save to - `C:\Users\%USERNAME%\AppData\Roaminguiverify.config` before executing.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VisualUiaVerifyNative.yml` |
| Evidence | Command preserved from source parser. |
