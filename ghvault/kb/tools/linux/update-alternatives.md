---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# update-alternatives

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `update-alternatives` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/update-alternatives` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for update-alternatives covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/update-alternatives.md)
- Source verification: [source record](../../sources/gtfobins/update-alternatives.md)

## Aliases

- `update-alternatives`

## Source Verification

[source record](../../sources/gtfobins/update-alternatives.md)

## Evidence Excerpt

```text
_body: ''
_name: update-alternatives
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/update-alternatives
functions:
file-write:
- code: 'echo DATA >/path/to/temp-file
update-alternatives --force --install /path/to/output-file x /path/to/temp-file 0'
comment: Write in `/path/to/output-file` a symlink to `/path/to/temp-file`.
```
