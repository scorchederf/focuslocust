---
parsed_by: focuslocust
source: commands
type: generated
---
# Pixtool Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pixtool.exe

Tool page: [Pixtool.exe](../../tools/windows/pixtool.exe.md)

### Executes an executable under a trusted, Microsoft signed binary.

```text
pixtool.exe launch {PATH_ABSOLUTE:.exe}
```

Description:

Launches an executable via PIX command-line utility.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Pixtool.yml` |
| Evidence | Command preserved from source parser. |
