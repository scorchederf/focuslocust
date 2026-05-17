---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# stdbuf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `stdbuf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/stdbuf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [stdbuf](../../tools/linux/stdbuf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | stdbuf |
| name | stdbuf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/stdbuf/ |

## Preserved Source Material

```yaml
_body: ''
_name: stdbuf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/stdbuf
functions:
  shell:
  - code: stdbuf -i0 /bin/sh
    contexts:
      sudo: null
      suid:
        code: stdbuf -i0 /bin/sh -p
        shell: false
      unprivileged: null
```
