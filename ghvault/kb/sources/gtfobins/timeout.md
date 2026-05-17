---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# timeout

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `timeout` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/timeout` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [timeout](../../tools/linux/timeout.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | timeout |
| name | timeout |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/timeout/ |

## Preserved Source Material

```yaml
_body: ''
_name: timeout
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/timeout
functions:
  shell:
  - code: timeout 0 /bin/sh
    contexts:
      sudo: null
      suid:
        code: timeout 0 /bin/sh -p
        shell: false
      unprivileged: null
```
