---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# git

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `git` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for git covering file-read, file-write, inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/git.md)
- Source verification: [source record](../../sources/gtfobins/git.md)

## Aliases

- `git`

## Source Verification

[source record](../../sources/gtfobins/git.md)

## Evidence Excerpt

```text
_body: ''
_name: git
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git
functions:
file-read:
- code: git diff /dev/null /path/to/input-file
comment: The read file content is displayed in `diff` style output format.
contexts:
```
