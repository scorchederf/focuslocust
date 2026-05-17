---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Web Attack Surface

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-web-attack-surface` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/web-attack-surface.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Attack Surface](../../topics/redteam/web-attack-surface.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-access-web-attack-surface |
| name | Web Attack Surface |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/access/web-attack-surface.md |

## Preserved Source Material

````yaml
_body: "# Web Attack Surface\n\n## Summary\n\n* [Enumerate Subdomains](#enumerate-subdomains)\n    * [Subdomains Databases](#subdomains-databases)\n\
  \    * [Bruteforce Subdomains](#bruteforce-subdomains)\n    * [Certificate Transparency Logs](#certificate-transparency-logs)\n\
  \    * [DNS Resolution](#dns-resolution)\n    * [Technology Discovery](#technology-discovery)\n* [Subdomain Takeover](#subdomain-takover)\n\
  * [References](#references)\n\n## Enumerate Subdomains\n\nSubdomain enumeration is the process of identifying all subdomains\
  \ associated with a main domain (e.g., finding `blog.example.com`, `shop.example.com`, etc., for `example.com`).\n\n###\
  \ Subdomains Databases\n\nMany databases and tools aggregate data from a variety of online sources, such as DNS databases,\
  \ certificate transparency logs, APIs (e.g., Shodan, VirusTotal), and other publicly available sources to compile a comprehensive\
  \ list of potential subdomains.\n\n* [projectdiscovery/chaos-client](https://github.com/projectdiscovery/chaos-client) -\
  \ Go client to communicate with Chaos DB API.\n\n  ```ps1\n  chaos -d hackerone.com\n  ```\n\n* [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)\
  \ - Fast passive subdomain enumeration tool.\n\n  ```ps1\n  subfinder -d hackerone.com\n  ```\n\n* [owasp-amass/amass](https://github.com/owasp-amass/amass)\
  \ - In-depth attack surface mapping and asset discovery\n\n  ```ps1\n  amass enum -d example.com\n  ```\n\n* [Findomain/Findomain](https://github.com/Findomain/Findomain)\
  \ - The complete solution for domain recognition.\n\n  ```ps1\n  findomain -t example.com -u /tmp/example.com.out\n  ```\n\
  \n### Bruteforce Subdomains\n\nSubdomain brute-forcing is a technique used to discover subdomains of a target domain by\
  \ systematically trying out potential subdomain names against it. This is done by using a predefined list of common or likely\
  \ subdomain names, known as a wordlist. Each word in the wordlist is appended to the target domain (e.g., admin.example.com,\
  \ mail.example.com) to check if it resolves to a valid subdomain.\n\n* [assetnote/wordlists](https://github.com/assetnote/wordlists)\n\
  * [danielmiessler/SecLists/Discovery/DNS](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)\n* [jhaddix/all.txt](https://gist.github.com/jhaddix/f64c97d0863a78454e44c2f7119c2a6a)\n\
  \nUnlike passive subdomain enumeration, which relies on existing data from sources, brute-forcing actively queries DNS records\
  \ to discover live subdomains that may not be listed in public databases.\n\n* [infosec-au/altdns](https://github.com/infosec-au/altdns)\
  \ - Generates permutations, alterations and mutations of subdomains and then resolves them.\n\n  ```powershell\n  altdns.py\
  \ -i /tmp/inputdomains.txt -o /tmp/out.txt -w ./words.txt\n  ```\n\n* [owasp-amass/amass](https://github.com/owasp-amass/amass)\
  \ - In-depth attack surface mapping and asset discovery.\n\n  ```ps1\n  amass enum -active -brute -o /tmp/hosts.txt -d $1\n\
  \  ```\n\n* [projectdiscovery/dnsx](https://github.com/projectdiscovery/dnsx) - A fast and multi-purpose DNS toolkit allow\
  \ to run multiple DNS queries of your choice with a list of user-supplied resolvers.\n\n  ```ps1\n  dnsx -silent -d facebook.com\
  \ -w dns_worldlist.txt\n  ```\n\n* [subfinder/goaltdns](https://github.com/subfinder/goaltdns) - A permutation generation\
  \ tool written in golang.\n\n  ```ps1\n  altdns -l ./input_domains.txt -o ./output.txt\n  ```\n\n### Certificate Transparency\
  \ Logs\n\nCertificate Transparency (CT) logs are public databases that record all SSL/TLS certificates issued by certificate\
  \ authorities (CAs). These logs are designed to improve the security and transparency of the SSL/TLS ecosystem by making\
  \ it easier to monitor and audit certificates.\n\n* [CertStream Calidog](https://certstream.calidog.io/)\n* [Meta Certificate\
  \ Transparency](https://developers.facebook.com/docs/certificate-transparency)\n* [Google Certificate Transparency](certificate.transparency.dev)\n\
  \n### DNS Resolution\n\nOnce you've generated a list of potential subdomains, the next step is to resolve them to retrieve\
  \ their DNS records (A and AAAA) to obtain their IPv4 and IPv6 addresses.\n\n* [blechschmidt/massdns](https://github.com/blechschmidt/massdns)\n\
  \n  ```ps1\n  cat /tmp/results_subfinder.txt | massdns -r ./resolvers.txt -t A -o S -w /tmp/results_subfinder_resolved.txt\n\
  \  ```\n\n* [projectdiscovery/dnsx](https://github.com/projectdiscovery/dnsx) - a fast and multi-purpose DNS toolkit allow\
  \ to run multiple DNS queries of your choice with a list of user-supplied resolvers.\n\n  ```ps1\n  subfinder -silent -d\
  \ hackerone.com | dnsx -silent -a -resp\n  subfinder -silent -d hackerone.com | dnsx -silent -cname -resp\n  subfinder -silent\
  \ -d hackerone.com | dnsx -silent  -asn\n  echo 173.0.84.0/24 | dnsx -silent -resp-only -ptr\n  echo AS17012 | dnsx -silent\
  \ -resp-only -ptr \n  ```\n\n## Technology Discovery\n\nTechnology discovery is the process of identifying the underlying\
  \ technologies, software, and frameworks used by a website or digital infrastructure. This often includes detecting web\
  \ servers, CMS platforms, programming languages, databases, JavaScript libraries, and other software components.\n\n* [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx)\
  \ - A fast and multi-purpose HTTP toolkit that allows running multiple probes using the retryablehttp library.\n\n  ```ps1\n\
  \  httpx -u 'https://example.com' -title -tech-detect -status-code -follow-redirects\n  ```\n\n* [projectdiscovery/wappalyzergo](https://github.com/projectdiscovery/wappalyzergo)\
  \ - A high performance go implementation of Wappalyzer Technology Detection Library.\n* [michenriksen/aquatone](https://github.com/michenriksen/aquatone)\
  \ - A Tool for Domain Flyovers\n\n  ```ps1\n  cat hosts.txt | aquatone -ports 80,443,3000,3001\n  ```\n\n* [rverton/webanalyze](https://github.com/rverton/webanalyze)\
  \ - Port of Wappalyzer in Go\n\n  ```ps1\n  webanalyze -host example.com -crawl 1\n  ```\n\n* [wappalyzer](https://www.wappalyzer.com/)\
  \ - Identify technologies on websites.\n\n## Subdomain Takover\n\nA subdomain takeover is a type of security vulnerability\
  \ that occurs when a subdomain (e.g., `sub.example.com`) is still live but its DNS records point to a service or platform\
  \ (like AWS S3, GitHub Pages, or Heroku) that is no longer active or properly configured. This situation can allow an attacker\
  \ to claim the unclaimed resource and take control of the subdomain, enabling them to host malicious content or impersonate\
  \ the legitimate website.\n\nFor example, if `sub.example.com` points to an AWS S3 bucket that has been deleted or abandoned,\
  \ an attacker could create a new S3 bucket with the same name, gaining control over the subdomain and potentially causing\
  \ security risks, like phishing attacks or reputational damage to the main domain.\n\nRefer to [EdOverflow/can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz)\
  \ for a list of services and guidance on claiming subdomains with dangling DNS records.\n\n* [projectdiscovery/nuclei-templates/http/takeovers](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/takeovers)\
  \ - Community curated list of templates for the nuclei engine to find security vulnerabilities.\n\n    ```powershell\n \
  \   nuclei -t nuclei-templates/http/takeovers -u https://example.com\n    ```\n\n* [anshumanbh/tko-subs](https://github.com/anshumanbh/tko-subs)\
  \ - A tool that can help detect and takeover subdomains with dead DNS records\n\n    ```powershell\n    ./bin/tko-subs -domains=./lists/domains_tkos.txt\
  \ -data=./lists/providers-data.csv  \n    ```\n\n## References\n\n* [Subdomain Takeover: Proof Creation for Bug Bounties\
  \ - Patrik Hudak (@0xpatrik) - May 21, 2018](https://0xpatrik.com/takeover-proofs/)\n* [Subdomain Takeover: Basics - Patrik\
  \ Hudak (@0xpatrik) - June 27, 2018](https://0xpatrik.com/subdomain-takeover-basics/)"
_relative_path: redteam/access/web-attack-surface.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/web-attack-surface.md
````
