---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tcpdump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tcpdump` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcpdump` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tcpdump covering command, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tcpdump.md)
- Source verification: [source record](../../sources/gtfobins/tcpdump.md)

## Aliases

- `tcpdump`

## Source Verification

[source record](../../sources/gtfobins/tcpdump.md)

## Evidence Excerpt

```text
_body: ''
_name: tcpdump
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcpdump
functions:
command:
- code: 'echo /path/to/command >/path/to/temp-file
chmod +x /path/to/temp-file
tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z /path/to/temp-file'
```
