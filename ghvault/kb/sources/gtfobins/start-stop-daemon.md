---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# start-stop-daemon

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `start-stop-daemon` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/start-stop-daemon` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [start-stop-daemon](../../tools/linux/start-stop-daemon.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | start-stop-daemon |
| name | start-stop-daemon |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/start-stop-daemon/ |

## Preserved Source Material

```yaml
_body: ''
_name: start-stop-daemon
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/start-stop-daemon
functions:
  shell:
  - code: start-stop-daemon -S -x /bin/sh
    contexts:
      sudo: null
      suid:
        code: start-stop-daemon -S -x /bin/sh -- -p
        shell: false
      unprivileged: null
```
