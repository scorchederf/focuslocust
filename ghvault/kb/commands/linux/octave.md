---
parsed_by: focuslocust
source: commands
type: generated
---
# octave Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## octave

Tool page: [octave](../../tools/linux/octave.md)

### file-read

```text
octave-cli --eval 'format none; fid = fopen("/path/to/input-file"); while(!feof(fid)); txt = fgetl(fid); disp(txt); endwhile; fclose(fid);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/octave` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
octave-cli --eval 'fid = fopen("/path/to/output-file", "w"); fputs(fid, "DATA"); fclose(fid);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/octave` |
| Evidence | Function example preserved from source parser. |

### shell

```text
octave-cli --eval 'system("/bin/sh")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/octave` |
| Evidence | Function example preserved from source parser. |
