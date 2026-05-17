---
parsed_by: focuslocust
source: commands
type: generated
---
# Atbroker Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Atbroker.exe

Tool page: [Atbroker.exe](../../tools/windows/atbroker.exe.md)

### Executes code defined in registry for a new AT. Modifications must be made to the system registry to either register or modify an existing Assistive Technology (AT) service entry.

```text
ATBroker.exe /start malware
```

Description:

Start a registered Assistive Technology (AT).

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Atbroker.yml` |
| Evidence | Command preserved from source parser. |
