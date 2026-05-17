---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# hashcat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `hashcat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hashcat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for hashcat covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/hashcat.md)
- Source verification: [source record](../../sources/gtfobins/hashcat.md)

## Aliases

- `hashcat`

## Source Verification

[source record](../../sources/gtfobins/hashcat.md)

## Evidence Excerpt

```text
_body: ''
_name: hashcat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hashcat
functions:
file-write:
- code: 'echo -n DATA | tee /path/to/wordlist | md5sum | awk ''{print $1}'' >/path/to/hash
hashcat -m 0 --quiet --potfile-disable -o /path/to/output-file --outfile-format=2 --outfile-autohex-disable /path/to/hash
/path/to/wordlist'
```
