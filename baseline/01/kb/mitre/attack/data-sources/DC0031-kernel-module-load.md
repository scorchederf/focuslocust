---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0031
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0031-kernel-module-load
---

## Description

The process of loading a kernel module into the operating system kernel. Kernel modules are object files that extend the kernel’s functionality, such as adding support for device drivers, new filesystems, or additional system calls. This action can be legitimate (e.g., loading a driver) or malicious (e.g., adding a rootkit). <br><br>*Data Collection Measures:*<br><br>- Linux:<br>    - Auditd: Enable auditing of kernel module loading. Example rule: `-a always,exit -F arch=b64 -S init_module,delete_module`.<br>    - Syslog: Monitor `/var/log/syslog` or `/var/log/messages` for entries related to kernel module loads.<br>    - Systemd Journal: Use `journalctl` to query logs for module loading events: `journalctl -k | grep "Loading kernel module"`<br>- macOS:<br>    - Unified Logs: Use the `log` command to query kernel module events: `log show --predicate 'eventMessage contains "kextload"' --info`<br>    - Endpoint Security Framework (ESF): Monitor for `ES_EVENT_TYPE_AUTH_KEXTLOAD` (kernel extension loading events).<br>- Kernel-Specific Tools:<br>    - Lsmod: Use `lsmod` to list loaded kernel modules in real-time.<br>    - Kprobe/eBPF: Use extended Berkeley Packet Filter (eBPF) or Kernel Probes (kprobes) to monitor kernel events, including module loading. Example using eBPF tools like BCC:<br>`sudo python /path/to/bcc/tools/kprobe -v do_init_module`<br>- Enable EDR Monitoring:<br>    - Configure alerts for: Suspicious kernel module loads from non-standard paths (e.g., /tmp). Unexpected or unsigned kernel modules.<br>    - Review detailed telemetry data provided by the EDR for insight into who initiated the module load, the file path, and whether the module was signed.
