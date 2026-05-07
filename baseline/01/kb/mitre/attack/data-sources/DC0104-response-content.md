---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0104
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0104-response-content
---

## Description

Captured network traffic that provides details about responses received during an internet scan. This data includes both protocol header values (e.g., HTTP status codes, IP headers, or DNS response codes) and response body content (e.g., HTML, JSON, or raw data). Examples:<br><br>- HTTP Scan: A web server responds to a probe with an HTTP 200 status code and an HTML body indicating the default page is accessible.<br>- DNS Scan: A DNS server replies to a query with a resolved IP address for a domain, along with details like Time-To-Live (TTL) and authoritative information.<br>- TCP Banner Grab: A service listening on a port (e.g., SSH or FTP) responds with a banner containing service name, version, or other metadata.
