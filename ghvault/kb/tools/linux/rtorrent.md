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

## Summary

GTFOBins entry for rtorrent covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rtorrent.md)
- Source verification: [source record](../../sources/gtfobins/rtorrent.md)

## Aliases

- `rtorrent`

## Source Verification

[source record](../../sources/gtfobins/rtorrent.md)

## Evidence Excerpt

```text
_body: ''
_name: rtorrent
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rtorrent
functions:
shell:
- code: 'echo ''execute = /bin/sh,-c,"/bin/sh </dev/tty >/dev/tty 2>/dev/tty"'' >~/.rtorrent.rc
rtorrent'
comment: After the shell, exit with `Ctrl-Q`.
```
