---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fail2ban-client

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fail2ban-client` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fail2ban-client` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for fail2ban-client covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/fail2ban-client.md)
- Source verification: [source record](../../sources/gtfobins/fail2ban-client.md)

## Aliases

- `fail2ban-client`

## Source Verification

[source record](../../sources/gtfobins/fail2ban-client.md)

## Evidence Excerpt

```text
_body: ''
_name: fail2ban-client
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fail2ban-client
functions:
command:
- blind: true
code: 'fail2ban-client add x
fail2ban-client set x addaction x
```
