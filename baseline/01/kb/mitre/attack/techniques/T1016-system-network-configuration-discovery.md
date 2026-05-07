---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1016
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1016-system-network-configuration-discovery
tactic:
    - Discovery
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include [[kb/mitre/attack/software/S0099-arp|Arp]], [[kb/mitre/attack/software/S0100-ipconfig|ipconfig]]/[[kb/mitre/attack/software/S0101-ifconfig|ifconfig]], [[kb/mitre/attack/software/S0102-nbtstat|nbtstat]], and [[kb/mitre/attack/software/S0103-route|route]].<br><br>Adversaries may also leverage a [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. `show ip route`, `show ip interface`).[^3] [^1]  On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the command `esxcli network nic list` will retrieve the MAC address, while `esxcli network ip interface ipv4 get` will retrieve the local IPv4 address.[^2] <br><br>Adversaries may use the information from [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery|System Network Configuration Discovery]] during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor has collected the MAC address of a compromised host; it can also use `GetAdaptersInfo` to identify network adapters.[^1] [^2]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has captured victim IP address details of the targeted machine.[^1] [^2]  |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe enumerates the IP address, network proxy settings, and domain name from a victim's system.[^1]  |
| [S0018](https://attack.mitre.org/software/S0018) | Sykipot | Sykipot may use `ipconfig /all` to gather system network configuration details.[^1]  |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has the ability to identify network settings on a compromised host.[^1]  |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | The reconnaissance modules used with Duqu can collect information on network configuration.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | A JHUHUGIT variant gathers network interface card information.[^1]  |
| [S0049](https://attack.mitre.org/software/S0049) | GeminiDuke | GeminiDuke collects information on network settings and Internet proxy settings from the victim.[^1]  |
| [S0060](https://attack.mitre.org/software/S0060) | Sys10 | Sys10 collects the local IP address of the victim and sends it to the C2.[^1]  |
| [S0081](https://attack.mitre.org/software/S0081) | Elise | Elise executes `ipconfig /all` after initial communication is made to the remote server.[^2] [^1]  |
| [S0082](https://attack.mitre.org/software/S0082) | Emissary | Emissary has the capability to execute the command `ipconfig /all`.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type may create a file containing the results of the command `cmd.exe /c ipconfig /all`.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | S-Type has used `ipconfig /all` on a compromised host.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy has gathered information about network IP configurations using [[kb/mitre/attack/software/S0100-ipconfig\|ipconfig]].exe and about routing tables using [[kb/mitre/attack/software/S0103-route\|route]].exe.[^1] [^2]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic uses the `nbtstat -n` and `nbtstat -s` commands on the victim’s machine.[^1]  |
| [S0092](https://attack.mitre.org/software/S0092) | Agent.btz | Agent.btz collects the network adapter’s IP and MAC address as well as IP addresses of the network adapter’s default gateway, primary/secondary WINS, DHCP, and DNS servers, and saves them into a log file.[^1]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea collects information about the Internet adapter configuration.[^1] [^2]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can gather information on the network configuration of a compromised host.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 gathers and beacons the MAC and IP addresses during installation.[^1]  |
| [[kb/mitre/attack/software/S0099-arp\|S0099]] | Arp | [[kb/mitre/attack/software/S0099-arp\|Arp]] can be used to display ARP configuration information on the host.[^1]  |
| [[kb/mitre/attack/software/S0100-ipconfig\|S0100]] | ipconfig | [[kb/mitre/attack/software/S0100-ipconfig\|ipconfig]] can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP. |
| [[kb/mitre/attack/software/S0101-ifconfig\|S0101]] | ifconfig | [[kb/mitre/attack/software/S0101-ifconfig\|ifconfig]] can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP. |
| [[kb/mitre/attack/software/S0102-nbtstat\|S0102]] | nbtstat | [[kb/mitre/attack/software/S0102-nbtstat\|nbtstat]] can be used to discover local NetBIOS domain names. |
| [[kb/mitre/attack/software/S0103-route\|S0103]] | route | [[kb/mitre/attack/software/S0103-route\|route]] can be used to discover routing configuration information. |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | A module in Prikormka collects information from the victim about its IP addresses and MAC addresses.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains a command to collect the victim MAC address and LAN IP.[^1] [^2]  |
| [S0124](https://attack.mitre.org/software/S0124) | Pisloader | Pisloader has a command to collect the victim's IP address.[^1]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec can obtain information about network configuration, including the routing table, ARP cache, and DNS cache.[^1]  |
| [S0130](https://attack.mitre.org/software/S0130) | Unknown Logger | Unknown Logger can obtain information about the victim's IP address.[^1]  |
| [S0139](https://attack.mitre.org/software/S0139) | PowerDuke | PowerDuke has a command to get the victim's domain and NetBIOS name.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon obtains the target's IP address and local network segment.[^1] [^2]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind obtains the victim IP address.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves can obtain information about network parameters.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can determine the NetBios name and  the IP addresses of targets machines including domain controllers.[^1] [^2]  |
| [S0165](https://attack.mitre.org/software/S0165) | OSInfo | OSInfo discovers the current domain information.[^1]  |
| [S0171](https://attack.mitre.org/software/S0171) | Felismus | Felismus collects the victim LAN IP address and sends it to the C2 server.[^1]  |
| [S0172](https://attack.mitre.org/software/S0172) | Reaver | Reaver collects the victim's IP address.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer can gather the IP address from the victim's machine.[^1]  |
| [S0181](https://attack.mitre.org/software/S0181) | FALLCHILL | FALLCHILL collects MAC address and local IP address information from the victim.[^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may collect network configuration data by running `ipconfig /all` on a victim.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can collect the IP address of a compromised host.[^1] [^2]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can obtain network information, including DNS, IP, and proxies.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can retrieve IP addresses of compromised machines.[^1] [^2]  |
| [S0205](https://attack.mitre.org/software/S0205) | Naid | Naid collects the domain name from a compromised host.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can retrieve IP, network adapter configuration information, and domain from compromised hosts.[^1] [^2]  |
| [S0228](https://attack.mitre.org/software/S0228) | NanHaiShu | NanHaiShu can gather information about the victim proxy server.[^1]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Orz can gather victim proxy information.[^1]  |
| [S0230](https://attack.mitre.org/software/S0230) | ZeroT | ZeroT gathers the victim's IP address and domain information, and then sends it to its C2 server.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook has a command to get the public IP address from a system.[^1]   |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects network adapter and interface information by using the commands `ipconfig /all`, `arp -a` and `route print`. It also collects the system's MAC address with `getmac` and domain configuration with `net config workstation`.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT collects the victim IP address, MAC address, as well as the victim account domain name.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc collects the network adapter information and domain/username information based on current remote sessions.[^1]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA gathers the victim’s IP address via the `ipconfig -all` command.[^1] [^2]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie uses `ipconfig /all` and `route PRINT` to identify network adapter and interface information.[^1]  |
| [S0245](https://attack.mitre.org/software/S0245) | BADCALL | BADCALL collects the network adapter information.[^1]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty runs `ipconfig /all` and collects the domain name.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can retrieve the contents of the IP routing table as well as information about the Windows domain.[^2] [^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy runs the `ipconfig /all` command.[^1]  |
| [S0252](https://attack.mitre.org/software/S0252) | Brave Prince | Brave Prince gathers network configuration information as well as the ARP cache.[^1]  |
| [S0254](https://attack.mitre.org/software/S0254) | PLAINTEE | PLAINTEE uses the `ipconfig /all` command to gather the victim’s IP address.[^1]  |
| [S0256](https://attack.mitre.org/software/S0256) | Mosquito | Mosquito uses the `ipconfig` command.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN gathers the local IP address.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole gathers information on the IP forwarding table, MAC address, configured proxy, and network SSID.[^1] [^2]  |
| [S0261](https://attack.mitre.org/software/S0261) | Catchamas | Catchamas gathers the Mac address, IP address, and the network adapter information from the victim’s machine.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar gathers information about network adapters.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot obtains the IP address, location, and other relevant network information from the victim’s machine.[^1] [^2] [^3]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT collects information about the network including the IP address and DHCP server.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal can execute `ipconfig` on the victim’s machine.[^1] [^2] [^3]   |
| [S0269](https://attack.mitre.org/software/S0269) | QUADAGENT | QUADAGENT gathers the current domain the victim system belongs to.[^1]  |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin gathers the IP address and domain from the victim’s machine.[^1]  |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE gathers the MAC address of the victim’s machine.[^1]  |
| [S0274](https://attack.mitre.org/software/S0274) | Calisto | Calisto runs the `ifconfig` command to obtain the IP address from the victim’s machine.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT has the capability to gather the victim's proxy information.[^1]  |
| [S0278](https://attack.mitre.org/software/S0278) | iKitten | iKitten will look for the current IP address.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can gather victim internal and external IPs.[^1]  |
| [S0284](https://attack.mitre.org/software/S0284) | More_eggs | More_eggs has the capability to gather the IP address from the victim's machine.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can collect the IP address of the victim machine and spawn instances of netsh.exe to enumerate wireless settings.[^1] [^2]   |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon can collect the IP address of the victims and other computers on the network using the commands: `ipconfig -all` `nbtstat -n`, and `nbtstat -s`.[^1] [^2]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore gathers the IP address from the victim’s machine.[^1]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can collect the host IP address from the victim’s machine.[^1]  |
| [S0341](https://attack.mitre.org/software/S0341) | Xbash | Xbash can collect IP addresses and local intranet information from a victim’s machine.[^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can collect host IP information from the victim’s machine.[^1]  |
| [S0346](https://attack.mitre.org/software/S0346) | OceanSalt | OceanSalt can collect the victim’s IP address.[^1]  |
| [S0350](https://attack.mitre.org/software/S0350) | zwShell | zwShell can obtain the victim IP address.[^1]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D can collect the network interface MAC address on the infected host.[^1] [^2]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI can gather information on the victim IP address.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis uses `ipconfig` to gather the IP address from the system.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI can collect the IP address from the victim’s machine.[^1]  |
| [[kb/mitre/attack/software/S0359-nltest\|S0359]] | Nltest | [[kb/mitre/attack/software/S0359-nltest\|Nltest]] may be used to enumerate the parent domain of a local machine using `/parentdomain`.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.[^2] [^1]  |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer uses API calls to enumerate the infected system's ARP table.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry will attempt to determine the local network segment it is a part of.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth collects the external IP address from the system. [^1]  |
| [S0374](https://attack.mitre.org/software/S0374) | SpeakUp | SpeakUp uses the `ifconfig -a` command. [^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate network adapter information.[^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT collects the IP address and MAC address from the system.[^1]  |
| [S0387](https://attack.mitre.org/software/S0387) | KeyBoy | KeyBoy can determine the public or WAN IP address for the system.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron gathers information about network adapters using the Win32 API call `GetAdaptersInfo`.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete collects the MAC address of the target computer and other network configuration information.[^1] [^2]  |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has executed the `ipconfig /all` command.[^1] 	 |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to identify the IP address of the compromised machine.[^1]  |
| [S0433](https://attack.mitre.org/software/S0433) | Rifdoor | Rifdoor has the ability to identify the IP address of the compromised host.[^1]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie has the ability to identify the IP of the infected host.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum can collect network information, including the host IP address, DNS, and proxy information.[^1]  |
| [S0441](https://attack.mitre.org/software/S0441) | PowerShower | PowerShower has the ability to identify the current Windows domain of the infected host.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has called `GetIpNetTable` in attempt to identify all mounted drives and hosts that have Address Resolution Protocol (ARP) entries.[^1] [^2]   |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has the ability to discover the domain name of the infected host.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun can detect network adapter and IP address information.[^1] 	 |
| [S0450](https://attack.mitre.org/software/S0450) | SHARPSTATS | SHARPSTATS has the ability to identify the domain of the compromised host.[^1]  |
| [S0451](https://attack.mitre.org/software/S0451) | LoudMiner | LoudMiner used a script to gather the IP address of the infected machine before sending to the C2.[^1]  |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can detect the infected machine's network topology using `ipconfig` and `arp`.[^1] 	 |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to identify the location, public IP address, and domain name on a compromised host.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can use [[kb/mitre/attack/software/S0100-ipconfig\|ipconfig]] and [[kb/mitre/attack/software/S0099-arp\|Arp]] to collect network configuration information, including routing information and ARP tables.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to determine the domain name and whether a proxy is configured on a compromised host.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to identify the MAC address on an infected host.[^1]  |
| [S0472](https://attack.mitre.org/software/S0472) | down_new | down_new has the ability to identify the MAC address of a compromised host.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger can identify the domain of the compromised host.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has the ability to identify the domain and the MAC and IP addresses of an infected machine.[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID used the `ipconfig /all` command and a batch script to gather network information.[^1]  |
| [S0486](https://attack.mitre.org/software/S0486) | Bonadan | Bonadan can find the external IP address of the infected host.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel has collected the DNS address of the infected host.[^1]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can collect DNS information from the targeted system.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can identify the IP address of a compromised host.[^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon can collect and send the local IP address, RDP information, and the network adapter physical address as a part of its C2 beacon.[^1]  |
| [S0504](https://attack.mitre.org/software/S0504) | Anchor | Anchor can determine the public IP and location of a compromised host.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can identify the MAC address on the target computer.[^1]  |
| [S0513](https://attack.mitre.org/software/S0513) | LiteDuke | LiteDuke has the ability to discover the proxy configuration of Firefox and/or Opera.[^1]  |
| [S0514](https://attack.mitre.org/software/S0514) | WellMess | WellMess can identify the IP address and user domain on the target machine.[^1] [^2]  |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail can identify the IP address of the victim system.[^1]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang can collect the TCP/IP, DNS, DHCP, and network adapter configuration on a compromised host via `ipconfig.exe /all`.[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN has collected the victim machine's local IP address information and MAC address.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can determine the IP and physical location of the compromised host via IPinfo.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can collect the IP address of a compromised host.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can collect the IP address and NetBIOS name of an infected machine.[^1]  |
| [[kb/mitre/attack/software/S0552-adfind\|S0552]] | AdFind | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] can extract subnet information from Active Directory.[^1] [^3] [^2]  |
| [S0556](https://attack.mitre.org/software/S0556) | Pay2Key | Pay2Key can identify the IP and MAC addresses of the compromised host.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected all network interface MAC addresses that are up and not loopback devices, as well as IP address, DHCP configuration, and domain information.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack can collect the host's IP addresses using the `ipconfig` command.[^1] [^2]  |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive |  Explosive has collected the MAC address from the victim's machine.[^1]   |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell can gather the IP address from the victim's machine using the IP config command.[^1]   |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can retrieve the ARP cache from the local system by using the `GetIpNetTable()` API call and check to ensure IP addresses it connects to are for local, non-Internet, systems.[^1]   |
| [S0583](https://attack.mitre.org/software/S0583) | Pysa | Pysa can perform network reconnaissance using the Advanced IP Scanner tool.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin can report the IP of the compromised host to attacker controlled infrastructure.[^1]  |
| [S0588](https://attack.mitre.org/software/S0588) | GoldMax | GoldMax retrieved a list of the system's network interface after execution.[^1]  |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot checked if the compromised system is configured to use proxies.[^1]  |
| [[kb/mitre/attack/software/S0590-nbtscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-nbtscan\|NBTscan]] can be used to collect MAC addresses.[^1] [^2] 	 |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has collected the domain name of the victim system.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet collects the IP address of a compromised system.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer’s 61850 payload component enumerates connected network adapters and their corresponding IP addresses.[^1]  |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS can determine the domain of a compromised host.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist has the ability to collect the domain name on a compromised host.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can identify the IP of a targeted system.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can retrieve the ARP cache from the local system by using `GetIpNetTable`.[^1]   |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent can enumerate the IP and domain of a target system.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has the ability to gather network configuration information.[^1]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon can collect the external IP address of the victim.[^1]  |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos can record the IP address of the target machine.[^1]  |
| [S0642](https://attack.mitre.org/software/S0642) | BADFLICK | BADFLICK has captured victim IP address details.[^1]  |
| [S0646](https://attack.mitre.org/software/S0646) | SpicyOmelette | SpicyOmelette can identify the IP of a compromised system.[^1]  |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian can retrieve the internal IP address of a compromised host.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can use `net config workstation`, `arp -a`, `nslookup`, and `ipconfig /all` to gather network configuration information.[^1] [^4] [^2] [^3] [^5]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon can collect the victim's MAC address by using the `GetAdaptersInfo` API.[^1]  |
| [S0653](https://attack.mitre.org/software/S0653) | xCaon | xCaon has used the GetAdaptersInfo() API call to get the victim's MAC address.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can collect IP information from the victim’s machine.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can enumerate victims' local and external IPs when registering with C2.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can enumerate the IP address of a compromised machine.[^1] [^2]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can collected the IP address and domain name of a compromised host.[^1]   |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can enumerate the IP address of a compromised host.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower has the ability to use `ipconfig` to enumerate system network settings.[^1]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma can collect the local MAC address using `GetAdaptersInfo` as well as the system's IP address.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has retrieved network information from a compromised host, such as the MAC address.[^1] [^2]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can use the Linux API `if_nameindex` to gather network interface names.[^1] [^2]  |
| [S0690](https://attack.mitre.org/software/S0690) | Green Lambert | Green Lambert can obtain proxy information from a victim's machine using system environment variables.[^1] [^2]   |
| [S0691](https://attack.mitre.org/software/S0691) | Neoichor | Neoichor can gather the IP address from an infected host.[^1]    |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has been used to execute the `ipconfig /all` command on a victim system.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan can run `C:\Windows\system32\cmd.exe /c cmd /c ipconfig /all 2>&1` to discover network settings.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa can collect IP addresses from a compromised host.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot can collect the IP address of a victim machine.[^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can collect the MAC address and other information from a victim machine using `ipconfig/all`.[^1]  |
| [S1022](https://attack.mitre.org/software/S1022) | IceApple | The IceApple [[kb/mitre/attack/software/S0101-ifconfig\|ifconfig]] module can iterate over all network interfaces on the host and retrieve the name, description, MAC address, DNS suffix, DNS servers, gateways, IPv4 addresses, and subnet masks.[^1]  |
| [S1024](https://attack.mitre.org/software/S1024) | CreepySnail | CreepySnail can use `getmac` and `Get-NetIPAddress` to enumerate network settings.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey can identify the IP address of a victim machine.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT | Action RAT has the ability to collect the MAC address of an infected host.[^1]  |
| [S1030](https://attack.mitre.org/software/S1030) | Squirrelwaffle | Squirrelwaffle has collected the victim’s external IP address.[^1]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull | PingPull can retrieve the IP address of a compromised host.[^1]  |
| [S1035](https://attack.mitre.org/software/S1035) | Small Sieve | Small Sieve can obtain the IP address of a victim host.[^1]  |
| [S1037](https://attack.mitre.org/software/S1037) | STARWHALE | STARWHALE has the ability to collect the IP address of an infected host.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can parse the `ProxyServer` string in the Registry to discover http proxies.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.[^1]  |
| [S1052](https://attack.mitre.org/software/S1052) | DEADEYE | DEADEYE can discover the DNS domain name of a targeted system.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can use the `GetAdaptersInfo` function to retrieve information about network adapters and the `GetIpNetTable` function to retrieve the IPv4 to physical network address mapping table.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can retrieve network interface and proxy information.[^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can enumerate IP addresses using `GetIpAddrTable`.[^1]  |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK can use [[kb/mitre/attack/software/S0099-arp\|Arp]] to discover a target's network configuration setttings.[^1]  |
| [S1076](https://attack.mitre.org/software/S1076) | QUIETCANARY | QUIETCANARY can identify the default proxy setting on a compromised host.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to execute the `ipconfig` command.[^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can enumerate the NetBIOS name on targeted machines.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja can enumerate the IP address on compromised systems.[^1]  |
| [S1106](https://attack.mitre.org/software/S1106) | NGLite | NGLite identifies the victim system MAC and IPv4 addresses and uses these to establish a victim identifier.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish has the ability to enumerate the domain name of a victim, as well as if the host is a member of an Active Directory domain.[^1] [^2] [^3]  |
| [S1138](https://attack.mitre.org/software/S1138) | Gootloader | Gootloader can use an embedded script to check the IP address of potential victims visiting compromised websites.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can use shell commands to discover network adapters and configuration.[^1]  |
| [S1143](https://attack.mitre.org/software/S1143) | LunarLoader | LunarLoader can verify the targeted host's DNS name which is then used in the creation of a decyrption key.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot gathers victim network information through commands such as `ipconfig` and `ipconfig /all`.[^1]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor gathers information on victim system network configuration such as MAC addresses.[^1]  |
| [S1156](https://attack.mitre.org/software/S1156) | Manjusaka | Manjusaka gathers information about current network connections, local and remote addresses associated with them, and associated processes.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can enumerate infected system network information.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus can discover the IP and MAC address of a targeted host.[^2] [^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker captures the IP address of the victim system and sends this to the attacker following encryption.[^1]  |
| [S1182](https://attack.mitre.org/software/S1182) | MagicRAT | MagicRAT collects system network information using commands such as `ipconfig /all`.[^1]  |
| [S1184](https://attack.mitre.org/software/S1184) | BOLDMOVE | BOLDMOVE enumerates network interfaces on the infected host.[^1]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer collects the MAC address of victim devices.[^1]  |
| [S1198](https://attack.mitre.org/software/S1198) | Gomir | Gomir collects network information on infected systems such as listing interface names, MAC and IP addresses, and IPv6 addresses.[^1]  |
| [S1203](https://attack.mitre.org/software/S1203) | J-magic | J-magic can compare the host and remote IPs to check if a received packet is from the infected machine.[^1]  |
| [S1204](https://attack.mitre.org/software/S1204) | cd00r | cd00r can discover the IP for the network interface on the compromised device.[^1]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex will gather system information such as MAC and IP addresses.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has obtained information about local networks through the `ipconfig /all` command.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc has a module for network enumeration including determining IP addresses.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer can enumeate information about victims’ systems including IP addresses.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can accept a command line argument identifying specific IPs.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has collected the local IP address, and external IP.[^1] [^2]  |
| [S1248](https://attack.mitre.org/software/S1248) | XORIndex Loader | XORIndex Loader has leveraged webservices to identify the public IP of the victim host.[^1]  |
| [S1249](https://attack.mitre.org/software/S1249) | HexEval Loader | HexEval Loader has leveraged server-side client configurations to identify the public IP of the victim host.[^1]  |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can capture information from each session with a victim including the public IP used to access the server and the user agent.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can enumerate the MAC address of the compromised host.[^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can enumerate network information on compromised hosts.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1016.001-internet-connection-discovery\|T1016.001]] | Internet Connection Discovery |
| [[kb/mitre/attack/techniques/T1016.002-wi-fi-discovery\|T1016.002]] | Wi-Fi Discovery |

 [^1]: [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)
 [^2]: [Trellix Rnasomhouse 2024](https://www.trellix.com/en-au/blogs/research/ransomhouse-am-see/)
 [^3]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^4]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^5]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^6]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^7]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^8]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^9]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^10]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^11]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
 [^12]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^13]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^14]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
 [^15]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^16]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^17]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^18]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^19]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^20]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
 [^21]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^22]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^23]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
 [^24]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^25]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^26]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^27]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
 [^28]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
 [^29]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^30]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^31]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^32]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)
 [^33]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^34]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^35]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^36]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
 [^37]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
 [^38]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)
 [^39]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^40]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)
 [^41]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^42]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^43]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)
 [^44]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
 [^45]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^46]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^47]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^48]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^49]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^50]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
 [^51]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^52]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^53]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)
 [^54]: [SentinelLabs Agent Tesla Aug 2020](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)
 [^55]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^56]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^57]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
 [^58]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
 [^59]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)
 [^60]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
 [^61]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^62]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^63]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^64]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^65]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
 [^66]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
 [^67]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^68]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^69]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^70]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^71]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^72]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
 [^73]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^74]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)
 [^75]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^76]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^77]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
 [^78]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
 [^79]: [GovCERT Carbon May 2016](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
 [^80]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)
 [^81]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^82]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^83]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^84]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^85]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
 [^86]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^87]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^88]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)
 [^89]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^90]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
 [^91]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
 [^92]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
 [^93]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
 [^94]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^95]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
 [^96]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
 [^97]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^98]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
 [^99]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^100]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^101]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^102]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
 [^103]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^104]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
 [^105]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^106]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^107]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
 [^108]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^109]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
 [^110]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^111]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^112]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^113]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
 [^114]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
 [^115]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^116]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)
 [^117]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^118]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)
 [^119]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)
 [^120]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^121]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^122]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^123]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^124]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
 [^125]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^126]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^127]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^128]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
 [^129]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^130]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^131]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^132]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^133]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
 [^134]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^135]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^136]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^137]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
 [^138]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
 [^139]: [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
 [^140]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^141]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^142]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
 [^143]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^144]: [GitHub Sliver Ifconfig](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/network/ifconfig.go)
 [^145]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^146]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
 [^147]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^148]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^149]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^150]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^151]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)
 [^152]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
 [^153]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
 [^154]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^155]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^156]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^157]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^158]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^159]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^160]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^161]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^162]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^163]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
 [^164]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
 [^165]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
 [^166]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^167]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^168]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^169]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^170]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^171]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
 [^172]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^173]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^174]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^175]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
 [^176]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^177]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
 [^178]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^179]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
 [^180]: [Medium Anchor DNS July 2020](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)
 [^181]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
 [^182]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)
 [^183]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
 [^184]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
 [^185]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
 [^186]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^187]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
 [^188]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^189]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)
 [^190]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
 [^191]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^192]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^193]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^194]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
 [^195]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^196]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
 [^197]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^198]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^199]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^200]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^201]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^202]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^203]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
 [^204]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^205]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^206]: [NGLite Trojan](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)
 [^207]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^208]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^209]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^210]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
 [^211]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)
 [^212]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^213]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^214]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)
 [^215]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
 [^216]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^217]: [TechNet Arp](https://technet.microsoft.com/en-us/library/bb490864.aspx)
 [^218]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
 [^219]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^220]: [Nltest Manual](https://ss64.com/nt/nltest.html)
 [^221]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^222]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
 [^223]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
 [^224]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^225]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^226]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
 [^227]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^228]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^229]: [Awake Security Avaddon](https://awakesecurity.com/blog/threat-hunting-for-avaddon-ransomware/)
 [^230]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
 [^231]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^232]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
 [^233]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
 [^234]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
 [^235]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^236]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^237]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^238]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^239]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^240]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^241]: [Bleeping Computer - Ryuk WoL](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/)
 [^242]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^243]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)
 [^244]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^245]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
 [^246]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^247]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
 [^248]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^249]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
 [^250]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^251]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
 [^252]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^253]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
 [^254]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)
 [^255]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)
 [^256]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
 [^257]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
