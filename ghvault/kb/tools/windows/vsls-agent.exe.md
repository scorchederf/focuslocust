---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vsls-agent.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsls-agent.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vsls-agent.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Agent for Visual Studio Live Share (Code Collaboration)

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/vsls-agent.md)
- Source verification: [source record](../../sources/lolbas/vsls-agent.exe.md)

## Aliases

- `vsls-agent.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/vsls-agent.exe.md)

## Source Verification

[source record](../../sources/lolbas/vsls-agent.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
Author: Jimmy (@bohops)
Commands:
- Category: Execute
Command: vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll}
Description: Load a library payload using the --agentExtensionPath parameter (32-bit)
```
