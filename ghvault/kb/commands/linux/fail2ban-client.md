---
parsed_by: focuslocust
source: commands
type: generated
---
# fail2ban-client Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## fail2ban-client

Tool page: [fail2ban-client](../../tools/linux/fail2ban-client.md)

### command

```text
fail2ban-client add x
fail2ban-client set x addaction x
fail2ban-client set x action x actionban /path/to/command
fail2ban-client start x
fail2ban-client set x banip 999.999.999.999
fail2ban-client set x unbanip 999.999.999.999
fail2ban-client stop x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fail2ban-client` |
| Evidence | Function example preserved from source parser. |

### command

```text
cat >/path/to/temp-dir/fail2ban.conf <<EOF
[Definition]
EOF

cat >/path/to/temp-dir/jail.local <<EOF
[x]
enabled = true
action = x
EOF

mkdir -p /path/to/temp-dir/action.d/
cat >/path/to/temp-dir/action.d/x.conf <<EOF
[Definition]
actionstart = /path/to/command
EOF

mkdir -p /path/to/temp-dir/filter.d/
cat >/path/to/temp-dir/filter.d/x.conf <<EOF
[Definition]
EOF

fail2ban-client -c /path/to/temp-dir/ -v restart
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fail2ban-client` |
| Evidence | Function example preserved from source parser. |
