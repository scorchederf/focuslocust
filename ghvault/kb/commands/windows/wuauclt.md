---
parsed_by: focuslocust
source: commands
type: generated
---
# wuauclt Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## wuauclt.exe

Tool page: [wuauclt.exe](../../tools/windows/wuauclt.exe.md)

### Execute dll via attach/detach methods

```text
wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer
```

Description:

Loads and executes DLL code on attach.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wuauclt.yml` |
| Evidence | Command preserved from source parser. |
