---
parsed_by: focuslocust
source: commands
type: generated
---
# rsyslogd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## rsyslogd

Tool page: [rsyslogd](../../tools/linux/rsyslogd.md)

### command

```text
cat >/path/to/temp-file <<EOF
module(load="imuxsock")
:msg, contains, "somerandomstring" ^/path/to/command
EOF

rsyslogd -f /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsyslogd` |
| Evidence | Function example preserved from source parser. |
