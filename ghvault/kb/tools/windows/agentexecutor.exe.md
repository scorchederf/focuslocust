---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AgentExecutor.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `agentexecutor.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Agentexecutor.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Intune Management Extension included on Intune Managed Devices

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/agentexecutor.md)
- Source verification: [source record](../../sources/lolbas/agentexecutor.exe.md)

## Aliases

- `AgentExecutor.exe`
- `agentexecutor.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "{PATH_ABSOLUTE:folder}" 0 1 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/agentexecutor.exe.md)

## Source Verification

[source record](../../sources/lolbas/agentexecutor.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@lefterispan'
Person: Eleftherios Panos
Author: Eleftherios Panos
Commands:
- Category: Execute
Command: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}"
60000 "C:\Windows\SysWOW64\WindowsPowerShell\v1.0" 0 1
```
