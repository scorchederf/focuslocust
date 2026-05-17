---
parsed_by: focuslocust
source: commands
type: generated
---
# vstest.console Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## vstest.console.exe

Tool page: [vstest.console.exe](../../tools/windows/vstest.console.exe.md)

### Proxy Execution and AWL bypass, Adversaries may run malicious code embedded inside the test methods of crafted dll/exe

```text
vstest.console.exe {PATH:.dll}
```

Description:

VSTest functionality may allow an adversary to executes their malware by wrapping it as a test method then build it to a .exe or .dll file to be later run by vstest.console.exe. This may both allow AWL bypass or defense bypass in general

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vstest.console.yml` |
| Evidence | Command preserved from source parser. |
