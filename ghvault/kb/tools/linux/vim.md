---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# vim

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `vim` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for vim covering file-read, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/vim.md)
- Source verification: [source record](../../sources/gtfobins/vim.md)

## Aliases

- `vim`

## Source Verification

[source record](../../sources/gtfobins/vim.md)

## Evidence Excerpt

```text
_body: ''
_name: vim
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim
functions:
file-read:
- binary: false
code: vim -c ':redir! >/path/to/output-file | echo "DATA" | redir END | q'
contexts:
```
