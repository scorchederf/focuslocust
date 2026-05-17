---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rustup

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rustup` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustup` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rustup covering command, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rustup.md)
- Source verification: [source record](../../sources/gtfobins/rustup.md)

## Aliases

- `rustup`

## Source Verification

[source record](../../sources/gtfobins/rustup.md)

## Evidence Excerpt

```text
_body: ''
_name: rustup
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustup
functions:
command:
- code: 'mkdir /path/to/temp-dir/bin/
mkdir /path/to/temp-dir/lib/
echo ''/path/to/command'' >/path/to/temp-dir/bin/rustc
```
