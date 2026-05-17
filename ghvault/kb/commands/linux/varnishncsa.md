---
parsed_by: focuslocust
source: commands
type: generated
---
# varnishncsa Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## varnishncsa

Tool page: [varnishncsa](../../tools/linux/varnishncsa.md)

### file-write

```text
varnishncsa -g request -q 'ReqURL ~ "/xxxxxxxxxx"' -F '%{yyy}i' -w /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/varnishncsa` |
| Evidence | Function example preserved from source parser. |
