---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wireshark

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wireshark` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wireshark` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for wireshark covering file-write, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/wireshark.md)
- Source verification: [source record](../../sources/gtfobins/wireshark.md)

## Aliases

- `wireshark`

## Source Verification

[source record](../../sources/gtfobins/wireshark.md)

## Evidence Excerpt

```text
_body: ''
_name: wireshark
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wireshark
functions:
file-write:
- code: 'wireshark -c 1 -i lo -k -f ''udp port 12345'' &
echo DATA | nc -u 127.127.127.127 12345'
comment: 'This technique can be used to write arbitrary files, i.e., the dump of one UDP packet.
```
