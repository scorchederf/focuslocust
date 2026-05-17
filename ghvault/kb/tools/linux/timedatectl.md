---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# timedatectl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `timedatectl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/timedatectl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for timedatectl covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/timedatectl.md)
- Source verification: [source record](../../sources/gtfobins/timedatectl.md)

## Aliases

- `timedatectl`

## Source Verification

[source record](../../sources/gtfobins/timedatectl.md)

## Evidence Excerpt

```text
_body: ''
_name: timedatectl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/timedatectl
comment: This might not work if run by unprivileged users depending on the system configuration.
functions:
inherit:
- code: timedatectl list-timezones
contexts:
```
