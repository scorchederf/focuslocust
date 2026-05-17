---
parsed_by: focuslocust
source: lolbas
type: generated
---
# devtunnel.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `devtunnel.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/devtunnels.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [devtunnel.exe](../../tools/windows/devtunnel.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | devtunnel.exe |
| name | devtunnel.exe |
| type | tool |
| source | lolbas |
| url | https://code.visualstudio.com/docs/editor/port-forwarding |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@deFr0ggy'
  Person: Kamran Saifullah
Author: Kamran Saifullah
Commands:
- Category: Download
  Command: devtunnel.exe host -p 8080
  Description: Enabling a forwarded port for locally hosted service at port 8080 to be exposed on the internet.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11, MacOS
  Privileges: User
  Usecase: Download Files, Upload Files, Data Exfiltration
Created: 2023-09-16
Description: Binary to enable forwarded ports on windows operating systems.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml
- IOC: devtunnel.exe binary spawned
- IOC: '*.devtunnels.ms'
- IOC: '*.*.devtunnels.ms'
- Analysis: https://cydefops.com/vscode-data-exfiltration
Full_Path:
- Path: C:\Users\<username>\AppData\Local\Temp\.net\devtunnel\devtunnel.exe
- Path: C:\Users\<username>\AppData\Local\Temp\DevTunnels\devtunnel.exe
Name: devtunnel.exe
Resources:
- Link: https://code.visualstudio.com/docs/editor/port-forwarding
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/devtunnels.yml
```

## Detection / Analysis Notes

```text
Analysis: https://cydefops.com/vscode-data-exfiltration
```

```text
IOC: *.*.devtunnels.ms
```

```text
IOC: *.devtunnels.ms
```

```text
IOC: devtunnel.exe binary spawned
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml
- IOC: devtunnel.exe binary spawned
- IOC: '*.devtunnels.ms'
- IOC: '*.*.devtunnels.ms'
- Analysis: https://cydefops.com/vscode-data-exfiltration
```
