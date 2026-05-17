---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mosquitto

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mosquitto` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mosquitto` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mosquitto covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mosquitto.md)
- Source verification: [source record](../../sources/gtfobins/mosquitto.md)

## Aliases

- `mosquitto`

## Source Verification

[source record](../../sources/gtfobins/mosquitto.md)

## Evidence Excerpt

```text
_body: ''
_name: mosquitto
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mosquitto
functions:
file-read:
- code: mosquitto -c /path/to/input-file
comment: The file is actually parsed and the first wrong line (ending with a newline or a null character) is returned
in an error message.
```
