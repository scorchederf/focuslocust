---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# install

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `install` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/install` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for install covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/install.md)
- Source verification: [source record](../../sources/gtfobins/install.md)

## Aliases

- `install`

## Source Verification

[source record](../../sources/gtfobins/install.md)

## Evidence Excerpt

```text
_body: ''
_name: install
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/install
functions:
privilege-escalation:
- code: install -m 6777 /path/to/input-file /path/to/output-dir/
comment: This can be run with elevated privileges to change permissions (`6` denotes the SUID bits) and then read, write,
or execute a file.
```
