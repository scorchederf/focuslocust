---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# loginctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `loginctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/loginctl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for loginctl covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/loginctl.md)
- Source verification: [source record](../../sources/gtfobins/loginctl.md)

## Aliases

- `loginctl`

## Source Verification

[source record](../../sources/gtfobins/loginctl.md)

## Evidence Excerpt

```text
_body: ''
_name: loginctl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/loginctl
comment: This might not work if run by unprivileged users depending on the system configuration.
functions:
shell:
- code: 'loginctl user-status
!/bin/sh'
```
