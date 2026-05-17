---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0064 - Command Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0064` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command Execution involves monitoring and capturing the execution of textual commands (including shell commands, cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution. Examples: 

- Windows Command Prompt
    - dir – Lists directory contents.
    - net user – Queries or manipulates user accounts.
    - tasklist – Lists running processes.
- PowerShell
    - Get-Process – Retrieves processes running on a system.
    - Set-ExecutionPolicy – Changes PowerShell script execution policies.
    - Invoke-WebRequest – Downloads remote resources.
- Linux Shell
    - ls – Lists files in a directory.
    - cat /etc/passwd – Reads the user accounts file.
    - curl http://malicious-site.com – Retrieves content from a malicious URL.
- Container Environments
    - docker exec – Executes a command inside a running container.
    - kubectl exec – Runs commands in Kubernetes pods.
- macOS Terminal
    - open – Opens files or URLs.
    - dscl . -list /Users – Lists all users on the system.
    - osascript -e – Executes AppleScript commands.

## Source Verification

[source record](../../sources/mitre/command-execution.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Command Execution involves monitoring and capturing the execution of textual commands (including shell commands,\
\ cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and\
\ are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution.\
\ Examples: \n\n- Windows Command Prompt\n    - dir – Lists directory contents.\n    - net user – Queries or manipulates\
\ user accounts.\n    - tasklist – Lists running processes.\n- PowerShell\n    - Get-Process – Retrieves processes running\
\ on a system.\n    - Set-ExecutionPolicy – Changes PowerShell script execution policies.\n    - Invoke-WebRequest – Downloads\
```
