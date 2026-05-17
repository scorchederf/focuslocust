---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Network Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-network-discovery` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/network-discovery.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Discovery](../../topics/cheatsheets/network-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-network-discovery |
| name | Network Discovery |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/network-discovery.md |

## Preserved Source Material

````yaml
_body: "# Network Discovery\n\n## MAC Address\n\n* [mac2vendor.com](https://mac2vendor.com/) - OUI Database Lookup\n* [oui.is](https://oui.is/)\
  \ - MAC Address Vendor Lookup\n\n| MAC Prefix | Description           |\n| ---------- | --------------------- |\n| FC:D4:F2\
  \   | Coca Cola Company     |\n| 00:9E:C8   | Xiaomi Communications |\n| 08:9E:08   | Google                |\n\n```ps1\n\
  sudo ifconfig <interface-name> down\nsudo ifconfig <interface-name> hw ether <new-mac-address> \nsudo ifconfig <interface-name>\
  \ up\n```\n\n## DHCP\n\nDHCP (Dynamic Host Configuration Protocol) is a networking protocol used to automatically assign\
  \ IP addresses and other network configuration parameters to devices on a network. DHCP allows devices to obtain necessary\
  \ network configuration information from a DHCP server, rather than having to be manually configured.\n\n```ps1\nsudo nmap\
  \ --script broadcast-dhcp-discover\nStarting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-04 11:15 CET\nPre-scan script\
  \ results:\n| broadcast-dhcp-discover: \n|   Response 1 of 1: \n|     Interface: eth0\n|     IP Offered: 192.168.1.111\n\
  |     DHCP Message Type: DHCPOFFER\n|     Server Identifier: 192.168.1.254\n|     IP Address Lease Time: 1d00h00m00s\n|\
  \     Renewal Time Value: 12h00m00s\n|     Rebinding Time Value: 21h00m00s\n|     Broadcast Address: 192.168.1.255\n|  \
  \   Hostname: Host-005\n|     Domain Name Server: 192.168.1.254\n|     Domain Name: lan\n|     Router: 192.168.1.254\n|_\
  \    Subnet Mask: 255.255.255.0\n```\n\n## DNS\n\n* AD DNS\n    * LDAP: `nslookup -type=srv _ldap._tcp.dc._msdcs.<domain\
  \ name>`\n    * KDC: `nslookup -type=srv _kerberos._tcp.<domain name>`\n    * Global catalog: `nslookup -type=srv _ldap._tcp.<domain\
  \ name>`\n\n## NBT-NS\n\nNS (Name Service) is a component of NBT that provides name resolution services for NETBIOS names.\
  \ In the context of NBT, NS is responsible for mapping NETBIOS names to IP addresses.\n\nNBT NS uses a distributed database\
  \ to store NETBIOS name-to-IP address mappings. Each computer on the network is responsible for registering its own name\
  \ and IP address in the database, and for resolving names to IP addresses when necessary. When a computer needs to resolve\
  \ a NETBIOS name to an IP address, it sends a query to the NBT NS service on another computer on the network. The NBT NS\
  \ service responds with the IP address associated with the requested name, if it is known. It works on `UDP, Port 137`.\n\
  \n* Get names:  `nbtscan -r 192.168.1.0/24`\n* Get the name for a single IP: `nmblookup -A <IP>`\n\n## MDNS\n\nMDNS (Multicast\
  \ Domain Name System) is a protocol used for zero-configuration networking, also known as \"zeroconf\". It allows devices\
  \ on a local network to automatically discover each other and resolve hostnames to IP addresses without the need for a centralized\
  \ DNS server.\n\nMDNS works by using multicast addresses to send DNS queries and responses. When a device wants to resolve\
  \ a hostname to an IP address, it sends a multicast DNS query to a special multicast address (224.0.0.251 for IPv4 and ff02::fb\
  \ for IPv6). Any device on the network that is listening for multicast DNS queries and has a matching hostname will respond\
  \ with its IP address.\n\n```ps1\nmdns-scan\n```\n\n## ARP\n\nARP (Address Resolution Protocol) is a networking protocol\
  \ used to map IP addresses to MAC (Media Access Control) addresses on a local area network (LAN).\n\n* ARP neighbors\n\n\
  \    ```ps1\n    :~$ ip neigh\n    192.168.122.1 dev enp1s0 lladdr 52:54:00:ff:0a:2c STALE\n    192.168.122.98 dev enp1s0\
  \ lladdr 52:54:00:ff:aa:bb STALE\n    ```\n\n* ARP scan with `nmap` - note, needs root privileges. Check what packets nmap\
  \ is sending with `--packet-trace`\n\n    ```ps1\n    :~# nmap -sn -n 192.168.122.0/24 \n    Starting Nmap 7.93 ( https://nmap.org\
  \ )\n    Nmap scan report for 192.168.122.1\n    Host is up (0.00032s latency).\n    MAC Address: 52:54:00:FF:0A:2C (QEMU\
  \ virtual NIC)\n    ```\n\n* ARP scan with `arp-scan`\n\n    ```ps1\n    root@kali:~# arp-scan -l\n    Interface: eth0,\
  \ datalink type: EN10MB (Ethernet)\n    Starting arp-scan 1.9 with 256 hosts (http://www.nta-monitor.com/tools/arp-scan/)\n\
  \    172.16.193.1 00:50:56:c0:00:08 VMware, Inc.\n    172.16.193.2 00:50:56:f1:18:a8 VMware, Inc.\n    172.16.193.254 00:50:56:e5:7b:87\
  \ VMware, Inc.\n    ```\n\n* ARP spoof with `arpspoof`\n\n    ```ps1\n    arpspoof [-i interface] [-c own|host|both] [-t\
  \ target] [-r] host\n    arpspoof -i wlan0 -t 10.0.0.X 10.0.0.Y\n    ```\n\n* ARP spoof with `Bettercap`\n\n    ```ps1\n\
  \    sudo bettercap -iface wlan0\n    net.probe on\n    set arp.spoof.targets <target_IP>\n    arp.spoof on\n    net.sniff\
  \ on\n    ```\n\n## Ping\n\n* Ping sweep with `nmap`: no port scan, no DNS resolution\n\n    ```powershell\n    nmap -sn\
  \ -n --disable-arp-ping 192.168.1.1-254 | grep -v \"host down\"\n    -sn : Disable port scanning. Host discovery only.\n\
  \    -n : Never do DNS resolution\n    ```\n\n## LDAP\n\n* Null bind connection: `ldapsearch -x -h <ip> -s base`\n\n## Port\
  \ Scans and Enumeration\n\n### Nmap\n\n* Basic NMAP\n\n```bash\nsudo nmap -sSV -p- 192.168.0.1 -oA OUTPUTFILE -T4\nsudo\
  \ nmap -sSV -oA OUTPUTFILE -T4 -iL INPUTFILE.csv\n\n• the flag -sSV defines the type of packet to send to the server and\
  \ tells Nmap to try and determine any service on open ports\n• the -p- tells Nmap to check all 65,535 ports (by default\
  \ it will only check the most popular 1,000)\n• 192.168.0.1 is the IP address to scan\n• -oA OUTPUTFILE tells Nmap to output\
  \ the findings in its three major formats at once using the filename \"OUTPUTFILE\"\n• -iL INPUTFILE tells Nmap to use the\
  \ provided file as inputs\n```\n\n* CTF NMAP\n\nThis configuration is enough to do a basic check for a CTF VM\n\n```bash\n\
  nmap -sV -sC -oA ~/nmap-initial 192.168.1.1\n\n-sV : Probe open ports to determine service/version info\n-sC : to enable\
  \ the script\n-oA : to save the results\n\nAfter this quick command you can add \"-p-\" to run a full scan while you work\
  \ with the previous result\n```\n\n* Aggressive NMAP\n\n```bash\nnmap -A -T4 scanme.nmap.org\n• -A: Enable OS detection,\
  \ version detection, script scanning, and traceroute\n• -T4: Defines the timing for the task (options are 0-5 and higher\
  \ is faster)\n```\n\n* Using searchsploit to detect vulnerable services\n\n```bash\nnmap -p- -sV -oX a.xml IP_ADDRESS; searchsploit\
  \ --nmap a.xml\n```\n\n* Generating nice scan report\n\n```bash\nnmap -sV IP_ADDRESS -oX scan.xml && xsltproc scan.xml -o\
  \ \"`date +%m%d%y`_report.html\"\n```\n\n* NMAP Scripts\n\n```bash\nnmap -sC : equivalent to --script=default\n\nnmap --script\
  \ 'http-enum' -v web.xxxx.com -p80 -oN http-enum.nmap\nPORT   STATE SERVICE\n80/tcp open  http\n| http-enum:\n|   /phpmyadmin/:\
  \ phpMyAdmin\n|   /.git/HEAD: Git folder\n|   /css/: Potentially interesting directory w/ listing on 'apache/2.4.10 (debian)'\n\
  |_  /image/: Potentially interesting directory w/ listing on 'apache/2.4.10 (debian)'\n\nnmap --script smb-enum-users.nse\
  \ -p 445 [target host]\nHost script results:\n| smb-enum-users:\n|   METASPLOITABLE\\backup (RID: 1068)\n|     Full name:\
  \   backup\n|     Flags:       Account disabled, Normal user account\n|   METASPLOITABLE\\bin (RID: 1004)\n|     Full name:\
  \   bin\n|     Flags:       Account disabled, Normal user account\n|   METASPLOITABLE\\msfadmin (RID: 3000)\n|     Full\
  \ name:   msfadmin,,,\n|     Flags:       Normal user account\n\nList Nmap scripts : ls /usr/share/nmap/scripts/\n```\n\n\
  ### Network Scan with nc and ping\n\nSometimes we want to perform network scan without any tools like nmap. So we can use\
  \ the commands `ping` and `nc` to check if a host is up and which port is open.\n\nTo check if hosts are up on a /24 range\n\
  \n```bash\nfor i in `seq 1 255`; do ping -c 1 -w 1 192.168.1.$i > /dev/null 2>&1; if [ $? -eq 0 ]; then echo \"192.168.1.$i\
  \ is UP\"; fi ; done\n```\n\nTo check which ports are open on a specific host\n\n```bash\nfor i in {21,22,80,139,443,445,3306,3389,8080,8443};\
  \ do nc -z -w 1 192.168.1.18 $i > /dev/null 2>&1; if [ $? -eq 0 ]; then echo \"192.168.1.18 has port $i open\"; fi ; done\n\
  ```\n\nBoth at the same time on a /24 range\n\n```bash\nfor i in `seq 1 255`; do ping -c 1 -w 1 192.168.1.$i > /dev/null\
  \ 2>&1; if [ $? -eq 0 ]; then echo \"192.168.1.$i is UP:\"; for j in {21,22,80,139,443,445,3306,3389,8080,8443}; do nc -z\
  \ -w 1 192.168.1.$i $j > /dev/null 2>&1; if [ $? -eq 0 ]; then echo \"\\t192.168.1.$i has port $j open\"; fi ; done ; fi\
  \ ; done\n```\n\nNot in one-liner version:\n\n```bash\nfor i in `seq 1 255`; \ndo \n    ping -c 1 -w 1 192.168.1.$i > /dev/null\
  \ 2>&1; \n    if [ $? -eq 0 ]; \n    then \n        echo \"192.168.1.$i is UP:\"; \n        for j in {21,22,80,139,443,445,3306,3389,8080,8443};\
  \ \n        do \n            nc -z -w 1 192.168.1.$i $j > /dev/null 2>&1; \n            if [ $? -eq 0 ]; \n            then\
  \ \n                echo \"\\t192.168.1.$i has port $j open\"; \n            fi ; \n        done ; \n    fi ; \ndone\n```\n\
  \n### Network Scan with PowerShell\n\n```powershell\n# ping scan\ntnc 8.8.8.8\n\n# port scan\ntnc 8.8.8.8 -port 443\n```\n\
  \n### Masscan\n\n```powershell\nmasscan -iL ips-online.txt --rate 10000 -p1-65535 --only-open -oL masscan.out\nmasscan -e\
  \ tun0 -p1-65535,U:1-65535 10.10.10.97 --rate 1000\n\n# find machines on the network\nsudo masscan --rate 500 --interface\
  \ tap0 --router-ip $ROUTER_IP --top-ports 100 $NETWORK -oL masscan_machines.tmp\ncat masscan_machines.tmp | grep open |\
  \ cut -d \" \" -f4 | sort -u > masscan_machines.lst\n\n# find open ports for one machine\nsudo masscan --rate 1000 --interface\
  \ tap0 --router-ip $ROUTER_IP -p1-65535,U:1-65535 $MACHINE_IP --banners -oL $MACHINE_IP/scans/masscan-ports.lst\n\n\n# TCP\
  \ grab banners and services information\nTCP_PORTS=$(cat $MACHINE_IP/scans/masscan-ports.lst| grep open | grep tcp | cut\
  \ -d \" \" -f3 | tr '\\n' ',' | head -c -1)\n[ \"$TCP_PORTS\" ] && sudo nmap -sT -sC -sV -v -Pn -n -T4 -p$TCP_PORTS --reason\
  \ --version-intensity=5 -oA $MACHINE_IP/scans/nmap_tcp $MACHINE_IP\n\n# UDP grab banners and services information\nUDP_PORTS=$(cat\
  \ $MACHINE_IP/scans/masscan-ports.lst| grep open | grep udp | cut -d \" \" -f3 | tr '\\n' ',' | head -c -1)\n[ \"$UDP_PORTS\"\
  \ ] && sudo nmap -sU -sC -sV -v -Pn -n -T4 -p$UDP_PORTS --reason --version-intensity=5 -oA $MACHINE_IP/scans/nmap_udp $MACHINE_IP\n\
  ```\n\n### Reconnoitre\n\nDependencies:\n\n* nbtscan\n* nmap\n\n```powershell\npython2.7 ./reconnoitre.py -t 192.168.1.2-252\
  \ -o ./results/ --pingsweep --hostnames --services --quick\n```\n\nIf you have a segfault with nbtscan, read the following\
  \ quote.\n> Permission is denied on the broadcast address (.0) and it segfaults on the gateway (.1) - all other addresses\
  \ seem fine here.So to mitigate the problem: nbtscan 192.168.0.2-255\n\n## Netdiscover\n\n```powershell\nnetdiscover -i\
  \ eth0 -r 192.168.1.0/24\nCurrently scanning: Finished!   |   Screen View: Unique Hosts\n\n20 Captured ARP Req/Rep packets,\
  \ from 4 hosts.   Total size: 876\n_____________________________________________________________________________\nIP   \
  \         At MAC Address     Count     Len  MAC Vendor / Hostname\n-----------------------------------------------------------------------------\n\
  192.168.1.AA    68:AA:AA:AA:AA:AA     15     630  Sagemcom\n192.168.1.XX    52:XX:XX:XX:XX:XX      1      60  Unknown vendor\n\
  192.168.1.YY    24:YY:YY:YY:YY:YY      1      60  QNAP Systems, Inc.\n192.168.1.ZZ    b8:ZZ:ZZ:ZZ:ZZ:ZZ      3     126 \
  \ HUAWEI TECHNOLOGIES CO.,LTD  \n```\n\n## Responder\n\n```powershell\nresponder -I eth0 -A # see NBT-NS, BROWSER, LLMNR\
  \ requests without responding.\nresponder.py -I eth0 -wrf\n```\n\nAlternatively you can use the [Windows version](https://github.com/lgandx/Responder-Windows)\n\
  \n## MITM\n\n* WSUS poisoning\n* ARP poisoning\n* DHCP poisoning: `responder --interface \"eth0\" --DHCP --wpad`\n\n###\
  \ Bettercap\n\n```powershell\nbettercap -X --proxy --proxy-https -T <target IP>\n# better cap in spoofing, discovery, sniffer\n\
  # intercepting http and https requests,\n# targetting specific IP only\n```\n\n### SSL MITM with OpenSSL\n\nThis code snippet\
  \ allows you to sniff/modify SSL traffic if there is a MITM vulnerability using only openssl.\nIf you can modify `/etc/hosts`\
  \ of the client:\n\n```powershell\nsudo echo \"[OPENSSL SERVER ADDRESS] [domain.of.server.to.mitm]\" >> /etc/hosts  # On\
  \ client host\n```\n\nOn our MITM server, if the client accepts self signed certificates (you can use a legit certificate\
  \ if you have the private key of the legit server):\n\n```powershell\nopenssl req -subj '/CN=[domain.of.server.to.mitm]'\
  \ -batch -new -x509 -days 365 -nodes -out server.pem -keyout server.pem\n```\n\nOn our MITM server, we setup our infra:\n\
  \n```powershell\nmkfifo response\nsudo openssl s_server -cert server.pem -accept [INTERFACE TO LISTEN TO]:[PORT] -quiet\
  \ < response | tee | openssl s_client -quiet -servername [domain.of.server.to.mitm] -connect[IP of server to MITM]:[PORT]\
  \ | tee | cat > response\n```\n\nIn this example, traffic is only displayed with `tee` but we could modify it using `sed`\
  \ for example.\n\n## References\n\n* [Pwning the Domain: Credentialess/Username - hadess - February 7, 2024](https://hadess.io/pwning-the-domain-credentialess-username/)"
_relative_path: cheatsheets/network-discovery.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/network-discovery.md
````
