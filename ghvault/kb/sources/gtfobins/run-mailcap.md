---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# run-mailcap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `run-mailcap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-mailcap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [run-mailcap](../../tools/linux/run-mailcap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | run-mailcap |
| name | run-mailcap |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/run-mailcap/ |

## Preserved Source Material

```yaml
_body: ''
_name: run-mailcap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/run-mailcap
functions:
  inherit:
  - code: run-mailcap --action=view text/plain:/etc/hosts
    contexts:
      sudo: null
      unprivileged: null
    from: less
  - code: run-mailcap --action=edit text/plain:/path/to/output-file
    comment: The file must exist and be not empty.
    contexts:
      sudo: null
      unprivileged: null
    from: vi
```
