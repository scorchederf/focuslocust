---
parsed_by: focuslocust
source: commands
type: generated
---
# iptables-save Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## iptables-save

Tool page: [iptables-save](../../tools/linux/iptables-save.md)

### file-write

```text
iptables -A INPUT -i lo -j ACCEPT -m comment --comment DATA
iptables -S
iptables-save -f /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iptables-save` |
| Evidence | Function example preserved from source parser. |
