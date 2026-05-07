---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0103
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0103-active-dns
---

## Description

"Domain Name: Active DNS" data component captures queried DNS registry data that highlights current domain-to-IP address resolutions. This data includes both direct queries to DNS servers and records that provide mappings between domain names and associated IP addresses. It serves as a critical resource for tracking active infrastructure and understanding the network footprint of an organization or adversary. Examples: <br><br>- DNS Query Example: `nslookup example.com`, `dig example.com A`<br>- PTR Record Example: `dig -x 192.168.1.1`<br>- Tracking Malicious Domains: DNS logs reveal repeated queries to suspicious domains like malicious-site.com. The IPs resolved by these domains may be indicators of compromise (IOCs).<br>- DNS Record Types<br>    - A/AAAA Record: Maps domain names to IP addresses (IPv4/IPv6).<br>    - CNAME Record: Canonical name records, often used for redirects.<br>    - MX Record: Mail exchange records, used to route emails.<br>    - TXT Record: Can include security information like SPF or DKIM policies.<br>    - SOA Record: Start of authority record for domain management.<br>    - NS Record: Lists authoritative name servers for the domain.<br><br>This data component can be collected through the following measures:<br><br>- System Utilities: Use built-in tools like `nslookup`, `dig`, or host on Linux, macOS, and Windows to perform active DNS queries.<br>- DNS Logging<br>    - Windows DNS Server: Enable DNS Analytical Logging to capture DNS queries and responses.<br>    - Bind DNS: Enable query logging in the named.conf file.<br>- Cloud Provider DNS Logging<br>    - AWS Route 53: Enable query logging through CloudWatch or S3:<br>    - Google Cloud DNS: Enable logging for Cloud DNS queries through Google Cloud Logging.<br>- Network Traffic Monitoring: Use tools like Wireshark or Zeek to analyze DNS queries within network traffic.<br>- Security Information and Event Management (SIEM) Integration: Aggregate DNS logs in a SIEM like Splunk to create alerts and monitor patterns.<br>- Public OSINT Tools: Use OSINT platforms like VirusTotal, or PassiveTotal to collect information on domains and their associated IP addresses.
