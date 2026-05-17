---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0104 - Response Content

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0104` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Captured network traffic that provides details about responses received during an internet scan. This data includes both protocol header values (e.g., HTTP status codes, IP headers, or DNS response codes) and response body content (e.g., HTML, JSON, or raw data). Examples:

- HTTP Scan: A web server responds to a probe with an HTTP 200 status code and an HTML body indicating the default page is accessible.
- DNS Scan: A DNS server replies to a query with a resolved IP address for a domain, along with details like Time-To-Live (TTL) and authoritative information.
- TCP Banner Grab: A service listening on a port (e.g., SSH or FTP) responds with a banner containing service name, version, or other metadata.

## Source Verification

[source record](../../sources/mitre/response-content.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Captured network traffic that provides details about responses received during an internet scan. This data includes
both protocol header values (e.g., HTTP status codes, IP headers, or DNS response codes) and response body content (e.g.,
HTML, JSON, or raw data). Examples:
- HTTP Scan: A web server responds to a probe with an HTTP 200 status code and an HTML body indicating the default page
is accessible.
- DNS Scan: A DNS server replies to a query with a resolved IP address for a domain, along with details like Time-To-Live
```
