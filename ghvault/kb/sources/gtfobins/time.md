---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# time

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `time` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/time` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [time](../../tools/linux/time.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | time |
| name | time |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/time/ |

## Preserved Source Material

```yaml
_body: ''
_name: time
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/time
functions:
  shell:
  - code: time /bin/sh
    comment: Note that the shell might have its own builtin `time` implementation, which may behave differently than the binary,
      which is often located at `/usr/bin/time`.
    contexts:
      sudo: null
      suid:
        code: time /bin/sh -p
        shell: false
      unprivileged: null
```
