---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mosh-server

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mosh-server` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mosh-server` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mosh-server](../../tools/linux/mosh-server.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mosh-server |
| name | mosh-server |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mosh-server/ |

## Preserved Source Material

```yaml
_body: ''
_name: mosh-server
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mosh-server
functions:
  shell:
  - code: mosh --server=mosh-server localhost /bin/sh
    comment: This requires a valid SSH access.
    contexts:
      sudo:
        comment: The `mosh-server` is executed via `sudo`.
```
