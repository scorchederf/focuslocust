---
parsed_by: focuslocust
source: commands
type: generated
---
# zic Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## zic

Tool page: [zic](../../tools/linux/zic.md)

### command

```text
echo 'Rule Jordan 0 1 xxx Jan lastSun 2 1:00d -' >/path/to/temp-file
echo 'Zone Test 2:00 Jordan CE%sT' >>/path/to/temp-file
zic -d . -y /path/to/command /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zic` |
| Evidence | Function example preserved from source parser. |
