---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# unzip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `unzip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unzip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for unzip covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/unzip.md)
- Source verification: [source record](../../sources/gtfobins/unzip.md)

## Aliases

- `unzip`

## Source Verification

[source record](../../sources/gtfobins/unzip.md)

## Evidence Excerpt

````text
_body: ''
_name: unzip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unzip
comment: 'Certain `unzip` versions allows to preserve the SUID bit. For example, prepare an archive beforehand with the following
commands as root:
```
cp /bin/sh .
chmod +s sh
````
