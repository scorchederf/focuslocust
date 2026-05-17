---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# code

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `code` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/code` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for code covering download, reverse-shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/code.md)
- Source verification: [source record](../../sources/gtfobins/code.md)

## Aliases

- `code`

## Source Verification

[source record](../../sources/gtfobins/code.md)

## Evidence Excerpt

```text
_body: ''
_name: code
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/code
functions:
download:
- code: code tunnel --name xxxxxx
comment: 'This requires a valid GitHub account.
Run the command locally, then on the attacker box navigate to <https://github.com/login/device>, using the provided
```
