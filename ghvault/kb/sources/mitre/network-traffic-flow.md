---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Traffic Flow

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0078` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Traffic Flow](../../attack/data-sources/DC0078-network-traffic-flow.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0078 |
| name | Network Traffic Flow |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0078 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Summarized network packet data that captures session-level details such as source/destination IPs, ports, protocol
  types, timestamps, and data volume, without storing full packet payloads. This is commonly used for traffic analysis, anomaly
  detection, and network performance monitoring.
external_references:
- external_id: DC0078
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0078
id: x-mitre-data-component--a7f22107-02e5-4982-9067-6625d4a1765a
modified: '2026-04-09T17:32:30.362Z'
name: Network Traffic Flow
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- mobile-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Network Traffic
- channel: socket_events
  name: macos:osquery
- channel: Unexpected flows between segmented networks or prohibited ports
  name: NSM:Flow
- channel: Configuration change traps or policy enforcement failures
  name: snmp:config
- channel: First-time outbound connections to package registries or unknown hosts immediately after restore/build
  name: NSM:Flow
- channel: First-time egress to new registries/CDNs post-install/build
  name: NSM:Flow
- channel: First-time egress to non-approved registries after dependency install
  name: NSM:Flow
- channel: Outbound connections to TCP 139,445 and HTTP/HTTPS to WebDAV endpoints from workstation subnets
  name: NSM:Flow
- channel: large outbound data flows or long-duration connections
  name: NSM:Flow
- channel: egress > 90th percentile or frequent connection reuse
  name: AWS:VPCFlowLogs
- channel: conn.log
  name: NSM:Flow
- channel: socket/connect
  name: auditd:SYSCALL
- channel: esxcli network vswitch or DNS resolver configuration updates
  name: esxi:syslog
- channel: Network Events
  name: esxi:vobd
- channel: TCP connections
  name: iptables:LOG
- channel: connection metadata
  name: NSM:Flow
- channel: DHCP Lease Granted
  name: wineventlog:dhcp
- channel: LEASE_GRANTED
  name: NSM:Flow
- channel: MAC not in allow-list acquiring IP (DHCP)
  name: NSM:Flow
- channel: SMB over high port
  name: Windows Firewall Log
- channel: Internal connection logging
  name: NSM:Connections
- channel: pf firewall logs
  name: NSM:Flow
- channel: /var/log/vmkernel.log
  name: esxi:vmkernel
- channel: Inter-segment traffic
  name: NSM:Flow
- channel: None
  name: NSM:Flow
- channel: Long-lived or hijacked SSH sessions maintained with no active user activity
  name: NSM:Flow
- channel: VPC/NSG flow logs for pod/instance egress to Internet or metadata
  name: AWS:VPCFlowLogs
- channel: Suspicious outbound traffic from browser binary to non-standard domains
  name: macos:unifiedlog
- channel: Abnormal browser traffic volume or destination
  name: NSM:Flow
- channel: Outbound requests to domains not previously resolved or associated with phishing campaigns
  name: NSM:Flow
- channel: Outbound traffic to domains/IPs not previously resolved, occurring shortly after attachment download or link click
  name: NSM:Flow
- channel: 'NetworkConnection: bytes_sent >> bytes_received anomaly'
  name: M365Defender:DeviceNetworkEvents
- channel: outbound flows with bytes_out >> bytes_in
  name: PF:Logs
- channel: 'network_flow: bytes_out >> bytes_in to external'
  name: NSX:FlowLogs
- channel: NetFlow/Zeek conn.log
  name: NSM:Flow
- channel: Outbound data flows
  name: AWS:VPCFlowLogs
- channel: Flow records with entropy signatures resembling symmetric encryption
  name: NSM:Flow
- channel: flow records
  name: NSM:Flow
- channel: flow records
  name: networkdevice:syslog
- channel: HTTPS POST to known webhook URLs
  name: macos:unifiedlog
- channel: Webhook registrations or repeated POST activity
  name: saas:api
- channel: Source/destination IP translation inconsistent with intended policy
  name: NSM:Flow
- channel: Unexpected NAT translation statistics or rule insertion events
  name: SNMP:DeviceLogs
- channel: Sudden spike in incoming flows to web service ports from single/multiple IPs
  name: NSM:Flow
- channel: Unusual volume of inbound packets from single source across short time interval
  name: AWS:VPCFlowLogs
- channel: port 5900 inbound
  name: NSM:Flow
- channel: TCP port 5900 open
  name: NSM:Flow
- channel: inbound connection to port 5900
  name: NSM:firewall
- channel: Outbound connections to 139/445 to multiple destinations
  name: NSM:Firewall
- channel: High volume internal traffic with low entropy indicating looped or malicious DoS script
  name: VPCFlowLogs:All
- channel: NetFlow/sFlow/PCAP
  name: NSM:Flow
- channel: Outbound Network Flow
  name: NSM:Flow
- channel: com.apple.network
  name: macos:unifiedlog
- channel: Device-to-Device Deployment Flows
  name: NSM:Flow
- channel: socket/connect syscalls
  name: auditd:SYSCALL
- channel: outbound TCP/UDP traffic over unexpected port
  name: macos:unifiedlog
- channel: ESXi service connections on unexpected ports
  name: esxi:vpxd
- channel: OUTBOUND
  name: iptables:LOG
- channel: tcp/udp
  name: macos:unifiedlog
- channel: CLI network calls
  name: esxi:hostd
- channel: Outbound traffic from suspicious new processes post-attachment execution
  name: NSM:Flow
- channel: Suspicious anomalies in transmitted data integrity during application network operations
  name: macos:unifiedlog
- channel: DNS resolution events leading to outbound traffic on unexpected ports
  name: esxi:syslog
- channel: Outbound traffic to mining pools or proxies
  name: NSM:Flow
- channel: Outbound flow logs to known mining pools
  name: AWS:VPCFlowLogs
- channel: Outbound network traffic to mining proxies
  name: container:cni
- channel: TLS session established by ESXi service to unapproved endpoint
  name: esxi:vpxd
- channel: Session records with TLS-like byte patterns
  name: NSM:Flow
- channel: HTTPS POST requests to pastebin.com or similar
  name: macos:unifiedlog
- channel: new outbound connections from exploited process tree
  name: NetFlow:Flow
- channel: new connections from exploited lineage
  name: NSM:Connections
- channel: Unexpected route changes or duplicate gateway advertisements
  name: NSM:Flow
- channel: EventCode=2004, 2005, 2006
  name: WinEventLog:Microsoft-Windows-Windows Firewall With Advanced Security/Firewall
- channel: 'Knock pattern: repeated REJ/S0 across ≥MinSequenceLen ports from same src_ip then SF success.'
  name: NSM:Flow
- channel: Firewall/PF anchor load or rule change events.
  name: macos:unifiedlog
- channel: Config/ACL changes, line vty transport input changes, telnet/ssh/http(s) enable, image/feature module changes.
  name: networkdevice:syslog
- channel: First-time egress to non-approved update hosts right after install/update
  name: NSM:Flow
- channel: New outbound flows to non-approved vendor hosts post install
  name: NSM:Flow
- channel: New/rare egress to non-approved update hosts after install
  name: NSM:Flow
- channel: large outbound HTTPS uploads to repo domains
  name: NSM:Flow
- channel: HTTPS traffic to repository domains
  name: esxi:vmkernel
- channel: alert log
  name: NSM:Flow
- channel: None
  name: esxi:vmkernel
- channel: Outbound flow records
  name: NSM:Flow
- channel: 'NetworkConnection: high out:in ratio, periodic beacons, protocol mismatch'
  name: m365:defender
- channel: high out:in ratio or fixed-size periodic flows
  name: PF:Logs
- channel: 'network_flow: bytes_out >> bytes_in, fixed packet sizes/intervals to non-approved CIDRs'
  name: NSM:Flow
- channel: connect or sendto system call with burst pattern
  name: auditd:SYSCALL
- channel: sudden burst in outgoing packets from same PID
  name: macos:unifiedlog
- channel: source instance sends large volume of traffic in short window
  name: AWS:VPCFlowLogs
- channel: session stats with bytes_out > bytes_in
  name: NSM:Flow
- channel: session stats with bytes_out > bytes_in
  name: NIDS:Flow
- channel: connection attempts and data transmission logs
  name: esxi:vpxa
- channel: External traffic to remote access services
  name: PF:Logs
- channel: High volumes of SYN/ACK packets with unacknowledged TCP handshakes
  name: NSM:Flow
- channel: Outbound resolution to hidden service domains (e.g., `.onion`)
  name: dns:query
- channel: conn.log + ssl.log with Tor fingerprinting
  name: NSM:Flow
- channel: forwarded encrypted traffic
  name: macos:unifiedlog
- channel: Relayed session pathing (multi-hop)
  name: NSM:Flow
- channel: Outbound TCP SYN or UDP to multiple ports/hosts
  name: NSM:Flow
- channel: container-level outbound traffic events
  name: containerd:runtime
- channel: Multiple APs advertising the same SSID but with different BSSID/MAC or encryption type
  name: WLANLogs:Association
- channel: socket_events
  name: linux:osquery
- channel: ARP cache modification attempts observed through event tracing or security baselines
  name: WinEventLog:Security
- channel: Gratuitous ARP replies with mismatched IP-MAC binding
  name: NSM:Flow
- channel: ARP table updates inconsistent with expected gateway or DHCP lease assignments
  name: macos:unifiedlog
- channel: networkd or com.apple.network
  name: macos:unifiedlog
- channel: log stream 'eventMessage contains "dns_request"'
  name: macos:unifiedlog
- channel: /var/log/syslog.log
  name: esxi:syslog
- channel: CreateTrafficMirrorSession or ModifyTrafficMirrorTarget
  name: AWS:CloudTrail
- channel: 'Config change: CLI/NETCONF/SNMP – ''monitor session'', ''mirror port'''
  name: networkdevice:syslog
- channel: Outbound UDP floods targeting common reflection services with spoofed IP headers
  name: NSM:Flow
- channel: Outbound UDP spikes to external reflector IPs
  name: macos:unifiedlog
- channel: Large outbound UDP traffic to multiple public reflector IPs
  name: AWS:VPCFlowLogs
- channel: High entropy domain queries with multiple NXDOMAINs
  name: macos:unifiedlog
- channel: Frequent DNS queries with high entropy names or NXDOMAIN results
  name: esxi:syslog
- channel: API communication
  name: vpxd.log
- channel: Outbound Connection
  name: NSM:Connections
- channel: Connection Tracking
  name: NSM:Flow
- channel: pf firewall logs
  name: NSM:Firewall
- channel: Flow Creation (NetFlow/sFlow)
  name: NSM:Flow
- channel: conn.log, icmp.log
  name: NSM:Flow
- channel: Abnormal SMB authentication attempts correlated with poisoned LLMNR/NBT-NS sessions
  name: NSM:Flow
- channel: Gratuitous or duplicate DHCP OFFER packets from non-legitimate servers
  name: NSM:Flow
- channel: Inbound on ports 5985/5986
  name: NSM:Connections
- channel: Multiple IP addresses assigned to the same domain in rapid sequence
  name: linux:syslog
- channel: Rapid domain-to-IP resolution changes for same domain
  name: macos:unifiedlog
- channel: Frequent DNS resolution of same domain with rotating IPs
  name: esxi:syslog
- channel: uncommon ports
  name: NSM:Flow
- channel: alternate ports
  name: NSM:Flow
- channel: None
  name: esxi:vpxd
- channel: conn.log or flow data
  name: NSM:Flow
- channel: egress log analysis
  name: esxi:vmkernel
- channel: egress logs
  name: esxi:vmkernel
- channel: High volume flows with incomplete TCP sessions or single-packet bursts
  name: NSM:Flow
- channel: 'Knock pattern: multiple REJ/S0 to distinct closed ports then successful connection to service_port'
  name: NSM:Flow
- channel: Firewall rule enable/disable or listen socket changes
  name: macos:unifiedlog
- channel: Config/ACL/line vty changes, service enable (telnet/ssh/http(s)), module reloads
  name: networkdevice:syslog
- channel: 'ioctl: Changes to wireless network interfaces (up, down, reassociate)'
  name: auditd:SYSCALL
- channel: 'query: Historical list of associated SSIDs compared against baseline'
  name: macos:osquery
- channel: First-time egress from host after new install to unknown update endpoints
  name: NSM:Flow
- channel: First-time egress to unknown registries/mirrors immediately after install
  name: NSM:Flow
- channel: New egress from app just installed to unknown update endpoints
  name: NSM:Flow
- channel: ESXi processes relaying traffic via SSH or unexpected ports
  name: esxi:vpxd
- channel: Outbound connection to mining pool port (3333, 4444, 5555)
  name: NSM:Flow
- channel: Outbound traffic to mining pool upon container launch
  name: NSM:Flow
- channel: Flow records with RSA key exchange on unexpected port
  name: NSM:Flow
- channel: Outbound connections from web server binaries (apache2, nginx, php-fpm) to unknown external IPs
  name: NSM:Flow
- channel: sustained outbound HTTPS sessions with high data volume
  name: NSM:Flow
- channel: Connections from IDE hosts to marketplace/tunnel domains
  name: NSM:Flow
- channel: Outbound connections from IDE processes to marketplace/tunnel domains
  name: macos:unifiedlog
- channel: large HTTPS outbound uploads
  name: NSM:Flow
- channel: network flows to external cloud services
  name: esxi:vmkernel
- channel: TCP port 22 traffic
  name: NSM:Flow
- channel: port 22 access
  name: esxi:vmkernel
- channel: Unexpected location resolution events or abnormal subscriber tracking requests
  name: TelecomLogs:MobilityEvents
- channel: Unexpected subscriber tracking or abnormal mobility/location resolution activity
  name: TelecomLogs:MobilityEvents
- channel: Application-layer protocol traffic exhibiting beacon-like periodicity, anomalous session structure, or protocol
    misuse patterns
  name: NSM:Flow
- channel: App-attributed traffic exhibits multi-destination fan-out, sustained session bridging, or SOCKS-like relay behavior
    inconsistent with normal client-only mobile communication
  name: NSM:Flow
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
