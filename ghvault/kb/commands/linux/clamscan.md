---
parsed_by: focuslocust
source: commands
type: generated
---
# clamscan Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## clamscan

Tool page: [clamscan](../../tools/linux/clamscan.md)

### file-read

```text
touch x.yara
clamscan --no-summary -d x.yara -f /path/to/input-file 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clamscan` |
| Evidence | Function example preserved from source parser. |
