---
parsed_by: focuslocust
source: commands
type: generated
---
# ffmpeg Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ffmpeg

Tool page: [ffmpeg](../../tools/linux/ffmpeg.md)

### library-load

```text
ffmpeg -f lavfi -i anullsrc -af ladspa=file=/path/to/lib.so /path/to/temp-file.wav
reset^J
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ffmpeg` |
| Evidence | Function example preserved from source parser. |
