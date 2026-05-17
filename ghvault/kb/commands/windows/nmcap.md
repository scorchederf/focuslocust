---
parsed_by: focuslocust
source: commands
type: generated
---
# Nmcap Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Nmcap.exe

Tool page: [Nmcap.exe](../../tools/windows/nmcap.exe.md)

### Capture network traffic on windows to collect sensitive data.

```text
nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap}
```

Description:

Start capture on all network adapters and save to specified .cap (circular) file.
Optionally, one can add:
- `/TerminateWhen /TimeAfter 30 seconds` to auto-terminate after a relative times (e.g. 30 seconds);
- `/TerminateWhen /Time 04:52:00 AM 9/17/2025` to auto-terminate after a specific date/time;
- `/TerminateWhen /KeyPress x` to terminate when a specific key is pressed.

Related ATT&CK:

- [T1040](../../attack/techniques/T1040-network-sniffing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Nmcap.yml` |
| Evidence | Command preserved from source parser. |
