---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# procmail

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `procmail` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/procmail` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for procmail covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/procmail.md)
- Source verification: [source record](../../sources/gtfobins/procmail.md)

## Aliases

- `procmail`

## Source Verification

[source record](../../sources/gtfobins/procmail.md)

## Evidence Excerpt

```text
_body: ''
_name: procmail
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/procmail
functions:
command:
- blind: false
code: 'echo -e '':0\n| /path/to/command >/path/to/temp-file
procmail -m /path/to/temp-file'
```
