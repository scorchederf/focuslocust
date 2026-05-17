---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Virtual Host

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-virtual-hosts-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Virtual Hosts/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Virtual Host](../../topics/virtual-hosts/virtual-host.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-virtual-hosts-readme |
| name | Virtual Host |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Virtual%20Hosts/README.md |

## Preserved Source Material

````yaml
_body: "# Virtual Host\n\n> A **Virtual Host** (VHOST) is a mechanism used by web servers (e.g., Apache, Nginx, IIS) to host\
  \ multiple domains or subdomains on a single IP address. When enumerating a webserver, default requests often target the\
  \ primary or default VHOST only. **Hidden hosts** may expose extra functionality or vulnerabilities.\n\n## Summary\n\n*\
  \ [Tools](#tools)\n* [Methodology](#methodology)\n* [References](#references)\n\n## Tools\n\n* [wdahlenburg/VhostFinder](https://github.com/wdahlenburg/VhostFinder)\
  \ - Identify virtual hosts by similarity comparison.\n* [codingo/VHostScan](https://github.com/codingo/VHostScan) - A virtual\
  \ host scanner that can be used with pivot tools, detect catch-all scenarios, aliases and dynamic default pages.\n* [hakluke/hakoriginfinder](https://github.com/hakluke/hakoriginfinder)\
  \ - Tool for discovering the origin host behind a reverse proxy. Useful for bypassing cloud WAFs.\n\n    ```ps1\n    prips\
  \ 93.184.216.0/24 | hakoriginfinder -h https://example.com:443/foo\n    ```\n\n* [OJ/gobuster](https://github.com/OJ/gobuster)\
  \ - Directory/File, DNS and VHost busting tool written in Go.\n\n    ```ps1\n    gobuster vhost -u https://example.com -w\
  \ /path/to/wordlist.txt\n    ```\n\n## Methodology\n\nWhen a web server hosts multiple websites on the same IP address,\
  \ it uses **Virtual Hosting** to decide which site to serve when a request comes in.\n\nIn HTTP/1.1 and above, every request\
  \ must contain a `Host` header:\n\n```http\nGET / HTTP/1.1\nHost: example.com\n```\n\nThis header tells the server which\
  \ domain the client is trying to reach.\n\n* If the server only has one site: The `Host` header is often ignored or set\
  \ to a default.\n* If the server has multiple virtual hosts: The web server uses the `Host` header to route the request\
  \ internally to the right content.\n\nSuppose the server is configured like:\n\n```ps1\n<VirtualHost *:80>\n    ServerName\
  \ site-a.com\n    DocumentRoot /var/www/a\n</VirtualHost>\n\n<VirtualHost *:80>\n    ServerName site-b.com\n    DocumentRoot\
  \ /var/www/b\n</VirtualHost>\n```\n\nA request with the default host (\"site-a.com\") returns the content for Site A.\n\n\
  ```http\nGET / HTTP/1.1\nHost: site-a.com\n```\n\nA request with an altered host (\"site-b.com\") returns content for Site\
  \ B (possibly revealing something new).\n\n```http\nGET / HTTP/1.1\nHost: site-b.com\n```\n\n### Fingerprinting VHOSTs\n\
  \nSetting `Host` to other known or guessed domains may give **different responses**.\n\n```ps1\ncurl -H \"Host: admin.example.com\"\
  \ http://10.10.10.10/\n```\n\nCommon indicators that you're hitting a different VHOST:\n\n* Different HTML titles, meta\
  \ descriptions, or brand names\n* Different HTTP Content-Length / body size\n* Different status codes (200 vs. 403 or redirect)\n\
  * Custom error pages\n* Redirect chains to completely different domains\n* Certificates with Subject Alternative Names listing\
  \ other domains\n\n**NOTE**: Leverage DNS history records to identify old IP addresses previously associated with your target’s\
  \ domains. Then test (or \"spray\") the current domain names against those IPs. If successful, this can reveal the server’s\
  \ real address, allowing you to bypass protections like Cloudflare or other WAFs by interacting directly with the origin\
  \ server.\n\n## References\n\n* [Gobuster for directory, DNS and virtual hosts bruteforcing - erev0s - March 17, 2020](https://web.archive.org/web/20200925023215/https://erev0s.com/blog/gobuster-directory-dns-and-virtual-hosts-bruteforcing/)\n\
  * [Virtual Hosting – A Well Forgotten Enumeration Technique - Wyatt Dahlenburg - June 16, 2022](https://web.archive.org/web/20220616183823/https://wya.pl/2022/06/16/virtual-hosting-a-well-forgotten-enumeration-technique/)"
_relative_path: Virtual Hosts/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Virtual Hosts/README.md
````
