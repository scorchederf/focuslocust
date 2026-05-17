---
parsed_by: focuslocust
source: commands
type: generated
---
# dtutil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## dtutil.exe

Tool page: [dtutil.exe](../../tools/windows/dtutil.exe.md)

### Use to copies the source file to the destination file

```text
dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext}
```

Description:

Copy file from source to destination

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dtutil.yml` |
| Evidence | Command preserved from source parser. |
