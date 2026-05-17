---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# octave

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `octave` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/octave` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for octave covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/octave.md)
- Source verification: [source record](../../sources/gtfobins/octave.md)

## Aliases

- `octave`

## Source Verification

[source record](../../sources/gtfobins/octave.md)

## Evidence Excerpt

```text
_body: ''
_name: octave
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/octave
comment: The payloads are compatible with GUI mode.
functions:
file-read:
- binary: false
code: octave-cli --eval 'format none; fid = fopen("/path/to/input-file"); while(!feof(fid)); txt = fgetl(fid); disp(txt);
```
