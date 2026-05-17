---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# clisp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `clisp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clisp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for clisp covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/clisp.md)
- Source verification: [source record](../../sources/gtfobins/clisp.md)

## Aliases

- `clisp`

## Source Verification

[source record](../../sources/gtfobins/clisp.md)

## Evidence Excerpt

```text
_body: ''
_name: clisp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/clisp
functions:
shell:
- code: clisp -x '(ext:run-shell-command "/bin/sh")(ext:exit)'
contexts:
sudo: null
```
