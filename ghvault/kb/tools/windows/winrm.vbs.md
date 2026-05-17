---
parsed_by: focuslocust
source: lolbas
type: generated
---
# winrm.vbs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winrm.vbs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Winrm.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Script used for manage Windows RM settings

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/winrm.vbs.md)
- Source verification: [source record](../../sources/lolbas/winrm.vbs.md)

## Aliases

- `winrm.vbs`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: winrm invoke Create wmicimv2/Win32_Process @{CommandLine="{CMD}"} -r:http://target:5985 |
| [T1216 - System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md) | explicit | source | Command metadata lists T1216: winrm invoke Create wmicimv2/Win32_Service @{Name="Evil";DisplayName="Evil";PathName="{CMD}"} -r:http://acmedc:5985 && winrm invoke StartService wmicimv2/Win32_Service?Name=Evil... |
| [T1220 - XSL Script Processing](../../attack/techniques/T1220-xsl-script-processing.md) | explicit | source | Command metadata lists T1220: %SystemDrive%\BypassDir\cscript //nologo %windir%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:pretty |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/winrm.vbs.md)

## Source Verification

[source record](../../sources/lolbas/winrm.vbs.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mattifestation'
Person: Matt Graeber
- Handle: '@enigma0x3'
Person: Matt Nelson
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@bohops'
```
