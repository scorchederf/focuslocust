---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tmux

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tmux` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tmux` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tmux covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tmux.md)
- Source verification: [source record](../../sources/gtfobins/tmux.md)

## Aliases

- `tmux`

## Source Verification

[source record](../../sources/gtfobins/tmux.md)

## Evidence Excerpt

```text
_body: ''
_name: tmux
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tmux
functions:
file-read:
- binary: false
code: tmux -f /path/to/input-file
comment: The file is read and parsed as a `tmux` configuration file, part of the first invalid line is returned in an
```
