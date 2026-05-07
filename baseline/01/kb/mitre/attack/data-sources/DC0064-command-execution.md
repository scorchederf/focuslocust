---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0064
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0064-command-execution
---

## Description

Command Execution involves monitoring and capturing the execution of textual commands (including shell commands, cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution. Examples: <br><br>- Windows Command Prompt<br>    - dir – Lists directory contents.<br>    - net user – Queries or manipulates user accounts.<br>    - tasklist – Lists running processes.<br>- PowerShell<br>    - Get-Process – Retrieves processes running on a system.<br>    - Set-ExecutionPolicy – Changes PowerShell script execution policies.<br>    - Invoke-WebRequest – Downloads remote resources.<br>- Linux Shell<br>    - ls – Lists files in a directory.<br>    - cat /etc/passwd – Reads the user accounts file.<br>    - curl  – Retrieves content from a malicious URL.<br>- Container Environments<br>    - docker exec – Executes a command inside a running container.<br>    - kubectl exec – Runs commands in Kubernetes pods.<br>- macOS Terminal<br>    - open – Opens files or URLs.<br>    - dscl . -list /Users – Lists all users on the system.<br>    - osascript -e – Executes AppleScript commands.
