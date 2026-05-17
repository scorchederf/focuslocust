---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Esentutl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `esentutl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Esentutl.exe](../../tools/windows/esentutl.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | esentutl.exe |
| name | Esentutl.exe |
| type | tool |
| source | lolbas |
| url | https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@egre55'
  Person: egre55
- Handle: '@grayfold3d'
  Person: Mike Cary
Author: Oddvar Moe
Commands:
- Category: Copy
  Command: esentutl.exe /y {PATH_ABSOLUTE:.source.vbs} /d {PATH_ABSOLUTE:.dest.vbs} /o
  Description: Copies the source VBS file to the destination VBS file.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Copies files from A to B
- Category: ADS
  Command: esentutl.exe /y {PATH_ABSOLUTE:.exe} /d {PATH_ABSOLUTE}:file.exe /o
  Description: Copies the source EXE to an Alternate Data Stream (ADS) of the destination file.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Copy file and hide it in an alternate data stream as a defensive counter measure
- Category: ADS
  Command: esentutl.exe /y {PATH_ABSOLUTE}:file.exe /d {PATH_ABSOLUTE:.exe} /o
  Description: Copies the source Alternate Data Stream (ADS) to the destination EXE.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Extract hidden file within alternate data streams
- Category: ADS
  Command: esentutl.exe /y {PATH_SMB:.exe} /d {PATH_ABSOLUTE}:file.exe /o
  Description: Copies the remote source EXE to the destination Alternate Data Stream (ADS) of the destination file.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Copy file and hide it in an alternate data stream as a defensive counter measure
- Category: Download
  Command: esentutl.exe /y {PATH_SMB:.source.exe} /d {PATH_SMB:.dest.exe} /o
  Description: Copies the source EXE to the destination EXE file
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Use to copy files from one unc path to another
- Category: Copy
  Command: esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d {PATH_ABSOLUTE:.dit}
  Description: Copies a (locked) file using Volume Shadow Copy
  MitreID: T1003.003
  OperatingSystem: Windows 10, Windows 11, Windows 2016 Server, Windows 2019 Server
  Privileges: Admin
  Usecase: Copy/extract a locked file such as the AD Database
Created: 2018-05-25
Description: Binary for working with Microsoft Joint Engine Technology (JET) database
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_params.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/esentutl_sam_copy.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_copy_ntds_sam_volshadowcp_cmdline.toml
Full_Path:
- Path: C:\Windows\System32\esentutl.exe
- Path: C:\Windows\SysWOW64\esentutl.exe
Name: Esentutl.exe
Resources:
- Link: https://twitter.com/egre55/status/985994639202283520
- Link: https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/
- Link: https://twitter.com/bohops/status/1094810861095534592
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_copy_ntds_sam_volshadowcp_cmdline.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_params.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/esentutl_sam_copy.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_params.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/esentutl_sam_copy.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_copy_ntds_sam_volshadowcp_cmdline.toml
```
