---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# redis

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `redis` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/redis` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for redis covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/redis.md)
- Source verification: [source record](../../sources/gtfobins/redis.md)

## Aliases

- `redis`

## Source Verification

[source record](../../sources/gtfobins/redis.md)

## Evidence Excerpt

```text
_body: ''
_name: redis
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/redis
functions:
file-write:
- binary: false
code: 'redis-cli -h 127.0.0.1
config set dir /path/to/output-dir/
```
