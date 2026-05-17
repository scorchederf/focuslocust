---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# puppet

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `puppet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/puppet` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for puppet covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/puppet.md)
- Source verification: [source record](../../sources/gtfobins/puppet.md)

## Aliases

- `puppet`

## Source Verification

[source record](../../sources/gtfobins/puppet.md)

## Evidence Excerpt

```text
_body: ''
_name: puppet
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/puppet
functions:
file-read:
- code: puppet filebucket -l diff /dev/null /path/to/input-file
comment: The read file content is corrupted by the `diff` output format. The actual `diff` command is executed.
contexts:
```
