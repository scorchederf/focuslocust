---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Bcp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `bcp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bcp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bcp.exe](../../tools/windows/bcp.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bcp.exe |
| name | Bcp.exe |
| type | tool |
| source | lolbas |
| url | https://asec.ahnlab.com/en/61000/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mahiralikhan07'
  Person: Mahir Ali Khan
Author: Mahir Ali Khan
Commands:
- Category: Download
  Command: bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost
    -T -c
  Description: Export binary payload stored in SQL Server database to file system.
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Usecase: Extract malicious executable from database storage to local file system for execution.
Created: 2025-11-13
Description: Microsoft SQL Server Bulk Copy Program utility for importing and exporting data between SQL Server instances
  and data files.
Detection:
- IOC: Process creation of bcp.exe with queryout or Out parameter
- IOC: bcp.exe writing executable files to temp or users directories
- IOC: Network connections from bcp.exe to SQL Server followed by file creation
- IOC: Event ID 4688 - Process creation for bcp.exe
- IOC: Event ID 4663 - File system access by bcp.exe
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcp_export_data.yml
Full_Path:
- Path: C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe
- Path: C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\bcp.exe
- Path: C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn\bcp.exe
- Path: C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe
- Path: C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\bcp.exe
- Path: C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn\bcp.exe
- Path: C:\Program Files (x86)\Microsoft SQL Server\120\Tools\Binn\bcp.exe
Name: Bcp.exe
Resources:
- Link: https://docs.microsoft.com/en-us/sql/tools/bcp-utility
- Link: https://asec.ahnlab.com/en/61000/
- Link: https://asec.ahnlab.com/en/78944/
- Link: https://www.huntress.com/blog/attacking-mssql-servers
- Link: https://www.huntress.com/blog/attacking-mssql-servers-pt-ii
- Link: https://news.sophos.com/en-us/2024/08/07/sophos-mdr-hunt-tracks-mimic-ransomware-campaign-against-organizations-in-india/
- Link: https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bcp.yml
```

## Detection / Analysis Notes

```text
IOC: Event ID 4663 - File system access by bcp.exe
```

```text
IOC: Event ID 4688 - Process creation for bcp.exe
```

```text
IOC: Network connections from bcp.exe to SQL Server followed by file creation
```

```text
IOC: Process creation of bcp.exe with queryout or Out parameter
```

```text
IOC: bcp.exe writing executable files to temp or users directories
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcp_export_data.yml
```

```text
- IOC: Process creation of bcp.exe with queryout or Out parameter
- IOC: bcp.exe writing executable files to temp or users directories
- IOC: Network connections from bcp.exe to SQL Server followed by file creation
- IOC: Event ID 4688 - Process creation for bcp.exe
- IOC: Event ID 4663 - File system access by bcp.exe
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcp_export_data.yml
```
