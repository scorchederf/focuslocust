---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# iptables-save

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `iptables-save` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iptables-save` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for iptables-save covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/iptables-save.md)
- Source verification: [source record](../../sources/gtfobins/iptables-save.md)

## Aliases

- `iptables-save`

## Source Verification

[source record](../../sources/gtfobins/iptables-save.md)

## Evidence Excerpt

```text
_body: ''
_name: iptables-save
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iptables-save
functions:
file-write:
- binary: false
code: 'iptables -A INPUT -i lo -j ACCEPT -m comment --comment DATA
iptables -S
```
