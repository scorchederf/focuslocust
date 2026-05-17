---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ldconfig

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ldconfig` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ldconfig` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ldconfig](../../tools/linux/ldconfig.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ldconfig |
| name | ldconfig |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ldconfig/ |

## Preserved Source Material

````yaml
_body: ''
_name: ldconfig
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ldconfig
functions:
  library-load:
  - code: 'echo /path/to/temp-dir/ >/path/to/temp-file

      ldconfig -f /path/to/temp-file

      ping'
    comment: "This allows to override one or more shared libraries (e.g., `libpcap`) globally, then triggers the execution\
      \ by running a program that uses it, e.g., `ping`. This is particularly useful if the target binary is SUID. Beware\
      \ though that it is easy to end up with a broken target system.\n\nFirst identify the shared libraries used by the target\
      \ program, for example:\n\n```\n$ ldd /bin/ping | grep libcap\n        libcap.so.2 => /path/to/temp-dir/libcap.so.2\
      \ (0x00007f8417eef000)\n```\n\nThen create the shared library override, named `libcap.so.2`, and put in in `/path/to/temp-dir/`.\
      \ The program might require some exported symbols from the library override, in that case make sure to add them (e.g.,\
      \ `void cap_get_flag() {}`)."
    contexts:
      sudo: null
      suid: null
      unprivileged: null
````
