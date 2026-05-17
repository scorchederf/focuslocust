---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Rpcping.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rpcping.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rpcping.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to verify rpc connection

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/rpcping.md)
- Source verification: [source record](../../sources/lolbas/rpcping.exe.md)

## Aliases

- `Rpcping.exe`
- `rpcping.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003 - OS Credential Dumping](../../attack/techniques/T1003-os-credential-dumping.md) | explicit | source | Command metadata lists T1003: rpcping -s 127.0.0.1 -e 1234 -a privacy -u NTLM |
| [T1187 - Forced Authentication](../../attack/techniques/T1187-forced-authentication.md) | explicit | source | Command metadata lists T1187: rpcping /s 10.0.0.35 /e 9997 /a connect /u NTLM |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/rpcping.exe.md)

## Source Verification

[source record](../../sources/lolbas/rpcping.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@vysecurity'
Person: Vincent Yiu
- Handle: '@splinter_code'
Person: Antonio Cocomazzi
- Handle: '@decoder_it'
```
