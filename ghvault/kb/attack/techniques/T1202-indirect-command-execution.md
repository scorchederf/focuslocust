---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1202 - Indirect Command Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1202` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking cmd. For example, Forfiles, the Program Compatibility Assistant (`pcalua.exe`), components of the Windows Subsystem for Linux (WSL), `Scriptrunner.exe`, as well as other utilities may invoke the execution of programs and commands from a Command and Scripting Interpreter, Run window, or via scripts. Adversaries may also abuse the `ssh.exe` binary to execute malicious commands via the `ProxyCommand` and `LocalCommand` options, which can be invoked via the `-o` flag or by modifying the SSH config file.

Adversaries may abuse these features for Stealth, specifically to perform arbitrary execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of cmd or file extensions more commonly associated with malicious payloads.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Bash.exe](../../tools/windows/bash.exe.md) | explicit | source | Command metadata lists T1202: bash.exe -c "{CMD}" |
| [Conhost.exe](../../tools/windows/conhost.exe.md) | explicit | source | Command metadata lists T1202: conhost.exe --headless {CMD} |
| [Diskshadow.exe](../../tools/windows/diskshadow.exe.md) | explicit | source | Command metadata lists T1202: diskshadow> exec {PATH:.exe} |
| [Explorer.exe](../../tools/windows/explorer.exe.md) | explicit | source | Command metadata lists T1202: explorer.exe {PATH_ABSOLUTE:.exe} |
| [Forfiles](../../tools/unknown/forfiles.md) | explicit | source | [Forfiles](https://attack.mitre.org/software/S0193) can be used to subvert controls and possibly conceal command execution by not directly invoking [cmd](https://attack.mitre.org/software/S0106).(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017) |
| [Forfiles.exe](../../tools/windows/forfiles.exe.md) | explicit | source | Command metadata lists T1202: forfiles /p c:\windows\system32 /m notepad.exe /c "{CMD}" |
| [Ftp.exe](../../tools/windows/ftp.exe.md) | explicit | source | Command metadata lists T1202: echo !{CMD} > ftpcommands.txt && ftp -s:ftpcommands.txt |
| [Logger.exe](../../tools/windows/logger.exe.md) | explicit | source | Command metadata lists T1202: logger.exe "{CMD}" |
| [Msdt.exe](../../tools/windows/msdt.exe.md) | explicit | source | Command metadata lists T1202: msdt.exe /id PCWDiagnostic /skip force /param "IT_LaunchMethod=ContextMenu IT_BrowseForFile=/../../$(calc).exe" |
| [OpenConsole.exe](../../tools/windows/openconsole.exe.md) | explicit | source | Command metadata lists T1202: OpenConsole.exe {PATH:.exe} |
| [Pcalua.exe](../../tools/windows/pcalua.exe.md) | explicit | source | Command metadata lists T1202: pcalua.exe -a {PATH_ABSOLUTE:.cpl} -c Java |
| [Pcwrun.exe](../../tools/windows/pcwrun.exe.md) | explicit | source | Command metadata lists T1202: Pcwrun.exe /../../$(calc).exe |
| [Procdump.exe](../../tools/windows/procdump.exe.md) | explicit | source | Command metadata lists T1202: procdump.exe -md {PATH:.dll} foobar |
| [Scriptrunner.exe](../../tools/windows/scriptrunner.exe.md) | explicit | source | Command metadata lists T1202: Scriptrunner.exe -appvscript {PATH:.exe} |
| [Sftp.exe](../../tools/windows/sftp.exe.md) | explicit | source | Command metadata lists T1202: sftp -o ProxyCommand="{CMD}" . |
| [Unregmp2.exe](../../tools/windows/unregmp2.exe.md) | explicit | source | Command metadata lists T1202: rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player" & copy C:\Windows\System32\calc.exe "%temp%\lolbin\Windows Media Player\wmpnscfg.exe" >nul && cmd /V... |
| [Vshadow.exe](../../tools/windows/vshadow.exe.md) | explicit | source | Command metadata lists T1202: vshadow.exe -nw -exec={PATH_ABSOLUTE:.exe} C: |
| [Wlrmdr.exe](../../tools/windows/wlrmdr.exe.md) | explicit | source | Command metadata lists T1202: wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u {PATH:.exe} |
| [Wsl.exe](../../tools/windows/wsl.exe.md) | explicit | source | Command metadata lists T1202: wsl.exe --exec bash -c "{CMD}" |
| [XBootMgr.exe](../../tools/windows/xbootmgr.exe.md) | explicit | source | Command metadata lists T1202: xbootmgr.exe -trace "{boot\|hibernate\|standby\|shutdown\|rebootCycle}" -preTraceCmd {PATH:.exe} |
| [XBootMgrSleep.exe](../../tools/windows/xbootmgrsleep.exe.md) | explicit | source | Command metadata lists T1202: xbootmgrsleep.exe 1000 {PATH:.exe} |
| [ssh.exe](../../tools/windows/ssh.exe.md) | explicit | source | Command metadata lists T1202: ssh -o ProxyCommand="{CMD}" . |
| [winfile.exe](../../tools/windows/winfile.exe.md) | explicit | source | Command metadata lists T1202: winfile.exe {PATH:.exe} |
| [wt.exe](../../tools/windows/wt.exe.md) | explicit | source | Command metadata lists T1202: wt.exe {CMD} |

## Source Verification

[source record](../../sources/mitre/indirect-command-execution.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit
the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking
[cmd](https://attack.mitre.org/software/S0106). For example, [Forfiles](https://attack.mitre.org/software/S0193), the Program
Compatibility Assistant (`pcalua.exe`), components of the Windows Subsystem for Linux (WSL), `Scriptrunner.exe`, as well
as other utilities may invoke the execution of programs and commands from a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059),
Run window, or via scripts.(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017)(Citation: Secure
```
