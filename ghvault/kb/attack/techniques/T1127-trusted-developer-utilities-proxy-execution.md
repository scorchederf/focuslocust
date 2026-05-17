---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1127 - Trusted Developer Utilities Proxy Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1127` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering. These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application control solutions.

Smart App Control is a feature of Windows that blocks applications it considers potentially malicious from running by verifying unsigned applications against a known safe list from a Microsoft cloud service before executing them. However, adversaries may leverage "reputation hijacking" to abuse an operating system’s trust of safe, signed applications that support the execution of arbitrary code. By leveraging Trusted Developer Utilities Proxy Execution to run their malicious code, adversaries may bypass Smart App Control protections.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AppCert.exe](../../tools/windows/appcert.exe.md) | explicit | source | Command metadata lists T1127: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml} |
| [AppLauncher.exe](../../tools/windows/applauncher.exe.md) | explicit | source | Command metadata lists T1127: AppLauncher.exe {PATH_ABSOLUTE:.exe} |
| [Aspnet_Compiler.exe](../../tools/windows/aspnet-compiler.exe.md) | explicit | source | Command metadata lists T1127: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe -v none -p C:\users\cpl.internal\desktop\asptest\ -f C:\users\cpl.internal\desktop\asptest\none -u |
| [Cdb.exe](../../tools/windows/cdb.exe.md) | explicit | source | Command metadata lists T1127: cdb.exe -c {PATH:.txt} "{CMD}" |
| [Csc.exe](../../tools/windows/csc.exe.md) | explicit | source | Command metadata lists T1127: csc -target:library {PATH:.cs} |
| [Devtoolslauncher.exe](../../tools/windows/devtoolslauncher.exe.md) | explicit | source | Command metadata lists T1127: devtoolslauncher.exe LaunchForDebug {PATH_ABSOLUTE:.exe} "{CMD:args}" test |
| [Dxcap.exe](../../tools/windows/dxcap.exe.md) | explicit | source | Command metadata lists T1127: dxcap.exe -usage |
| [Ilasm.exe](../../tools/windows/ilasm.exe.md) | explicit | source | Command metadata lists T1127: ilasm.exe {PATH_ABSOLUTE:.txt} /dll |
| [IntelliTrace.exe](../../tools/windows/intellitrace.exe.md) | explicit | source | Command metadata lists T1127: IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe" |
| [Jsc.exe](../../tools/windows/jsc.exe.md) | explicit | source | Command metadata lists T1127: jsc.exe /t:library {PATH:.js} |
| [Mftrace.exe](../../tools/windows/mftrace.exe.md) | explicit | source | Command metadata lists T1127: Mftrace.exe {PATH:.exe} |
| [Microsoft.NodejsTools.PressAnyKey.exe](../../tools/windows/microsoft.nodejstools.pressanykey.exe.md) | explicit | source | Command metadata lists T1127: Microsoft.NodejsTools.PressAnyKey.exe normal 1 {PATH:.exe} |
| [Microsoft.Workflow.Compiler.exe](../../tools/windows/microsoft.workflow.compiler.exe.md) | explicit | source | Command metadata lists T1127: Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log} |
| [Mpiexec.exe](../../tools/windows/mpiexec.exe.md) | explicit | source | Command metadata lists T1127: mpiexec.exe {CMD} |
| [Ntsd.exe](../../tools/windows/ntsd.exe.md) | explicit | source | Command metadata lists T1127: ntsd.exe -g {CMD} |
| [Pixtool.exe](../../tools/windows/pixtool.exe.md) | explicit | source | Command metadata lists T1127: pixtool.exe launch {PATH_ABSOLUTE:.exe} |
| [Remote.exe](../../tools/windows/remote.exe.md) | explicit | source | Command metadata lists T1127: Remote.exe /s {PATH_SMB:.exe} anythinghere |
| [Tracker.exe](../../tools/windows/tracker.exe.md) | explicit | source | Command metadata lists T1127: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe |
| [Ttdinject.exe](../../tools/windows/ttdinject.exe.md) | explicit | source | Command metadata lists T1127: ttdinject.exe /ClientScenario TTDRecorder /ddload 0 /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /launch "{PATH:.exe}" |
| [Tttracer.exe](../../tools/windows/tttracer.exe.md) | explicit | source | Command metadata lists T1127: tttracer.exe {PATH_ABSOLUTE:.exe} |
| [VSDiagnostics.exe](../../tools/windows/vsdiagnostics.exe.md) | explicit | source | Command metadata lists T1127: VSDiagnostics.exe start 2 /launch:{PATH:.exe} /launchArgs:"{CMD:args}" |
| [VSLaunchBrowser.exe](../../tools/windows/vslaunchbrowser.exe.md) | explicit | source | Command metadata lists T1127: VSLaunchBrowser.exe .exe {PATH_SMB} |
| [WFMFormat.exe](../../tools/windows/wfmformat.exe.md) | explicit | source | Command metadata lists T1127: WFMFormat.exe |
| [Wfc.exe](../../tools/windows/wfc.exe.md) | explicit | source | Command metadata lists T1127: wfc.exe {PATH_ABSOLUTE:.xoml} |
| [WinDbg.exe](../../tools/windows/windbg.exe.md) | explicit | source | Command metadata lists T1127: windbg.exe -g {CMD} |
| [adplus.exe](../../tools/windows/adplus.exe.md) | explicit | source | Command metadata lists T1127: adplus.exe -crash -o "{PATH_ABSOLUTE:folder}" -sc {PATH:.exe} |
| [csi.exe](../../tools/windows/csi.exe.md) | explicit | source | Command metadata lists T1127: csi.exe {PATH:.cs} |
| [dnx.exe](../../tools/windows/dnx.exe.md) | explicit | source | Command metadata lists T1127: dnx.exe {PATH_ABSOLUTE:folder} |
| [rcsi.exe](../../tools/windows/rcsi.exe.md) | explicit | source | Command metadata lists T1127: rcsi.exe {PATH:.csx} |
| [te.exe](../../tools/windows/te.exe.md) | explicit | source | Command metadata lists T1127: te.exe {PATH:.dll} |
| [vbc.exe](../../tools/windows/vbc.exe.md) | explicit | source | Command metadata lists T1127: vbc -reference:Microsoft.VisualBasic.dll {PATH_ABSOLUTE:.vb} |
| [vsjitdebugger.exe](../../tools/windows/vsjitdebugger.exe.md) | explicit | source | Command metadata lists T1127: Vsjitdebugger.exe {PATH:.exe} |
| [vstest.console.exe](../../tools/windows/vstest.console.exe.md) | explicit | source | Command metadata lists T1127: vstest.console.exe {PATH:.dll} |

## Source Verification

[source record](../../sources/mitre/trusted-developer-utilities-proxy-execution.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:39.262Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There
are many utilities used for software development related tasks that can be used to execute code in various forms to assist
in development, debugging, and reverse engineering.(Citation: engima0x3 DNX Bypass)(Citation: engima0x3 RCSI Bypass)(Citation:
Exploit Monday WinDbg)(Citation: LOLBAS Tracker) These utilities may often be signed with legitimate certificates that allow
them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application
control solutions.
```
