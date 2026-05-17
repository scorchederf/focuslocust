---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Brute Force & Rate Limit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-brute-force-rate-limit-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Brute Force Rate Limit/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Brute Force & Rate Limit](../../topics/brute-force-rate-limit/brute-force-and-rate-limit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-brute-force-rate-limit-readme |
| name | Brute Force & Rate Limit |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Brute%20Force%20Rate%20Limit/README.md |

## Preserved Source Material

````yaml
_body: "# Brute Force & Rate Limit\n\n## Summary\n\n* [Tools](#tools)\n* [Bruteforce](#bruteforce)\n    * [Burp Suite Intruder](#burp-suite-intruder)\n\
  \    * [FFUF](#ffuf)\n* [Rate Limit](#rate-limit)\n    * [TLS Stack - JA3](#tls-stack---ja3)\n    * [Network IPv4](#network-ipv4)\n\
  \    * [Network IPv6](#network-ipv6)\n* [References](#references)\n\n## Tools\n\n* [ZephrFish/OmniProx](https://github.com/ZephrFish/OmniProx)\
  \ - IP Rotation from different providers - Like FireProx but for GCP, Azure, Alibaba and CloudFlare.\n* [ddd/gpb](https://github.com/ddd/gpb)\
  \ - Bruteforcing the phone number of any Google user while rotating IPv6 addresses.\n* [ffuf/ffuf](https://github.com/ffuf/ffuf)\
  \ - Fast web fuzzer written in Go.\n* [PortSwigger/Burp Suite](https://portswigger.net/burp) - The class-leading vulnerability\
  \ scanning, penetration testing, and web app security platform.\n* [lwthiker/curl-impersonate](https://github.com/lwthiker/curl-impersonate)\
  \ - A special build of curl that can impersonate Chrome & Firefox.\n\n## Bruteforce\n\nIn a web context, brute-forcing refers\
  \ to the method of attempting to gain unauthorized access to web applications, particularly through login forms or other\
  \ user input fields. Attackers systematically input numerous combinations of credentials or other values (e.g., iterating\
  \ through numeric ranges) to exploit weak passwords or inadequate security measures.\n\nFor instance, they might submit\
  \ thousands of username and password combinations or guess security tokens by iterating through a range, such as 0 to 10,000.\
  \ This method can lead to unauthorized access and data breaches if not mitigated effectively.\n\nCountermeasures like rate\
  \ limiting, account lockout policies, CAPTCHA, and strong password requirements are essential to protect web applications\
  \ from such brute-force attacks.\n\n### Burp Suite Intruder\n\n* **Sniper attack**: target a single position (one variable)\
  \ while cycling through one payload set.\n\n    ```ps1\n\n    Username: password\n    Username1:Password1\n    Username1:Password2\n\
  \    Username1:Password3\n    Username1:Password4\n    ```\n\n* **Battering ram attack**: send the same payload to all marked\
  \ positions at once by using a single payload set.\n\n    ```ps1\n    Username1:Username1\n    Username2:Username2\n   \
  \ Username3:Username3\n    Username4:Username4\n    ```\n\n* **Pitchfork attack**: use different payload lists in parallel,\
  \ combining the nth entry from each list into one request.\n\n    ```ps1\n    Username1:Password1\n    Username2:Password2\n\
  \    Username3:Password3\n    Username4:Password4\n    ```\n\n* **Cluster bomb attack**: iterate through all combinations\
  \ of multiple payload sets.\n\n    ```ps1\n    Username1:Password1\n    Username1:Password2\n    Username1:Password3\n \
  \   Username1::Password4\n\n    Username2:Password1\n    Username2:Password2\n    Username2:Password3\n    Username2:Password4\n\
  \    ```\n\n### FFUF\n\n```bash\nffuf -w usernames.txt:USER -w passwords.txt:PASS \\\n     -u https://target.tld/login \\\
  \n     -X POST -d \"username=USER&password=PASS\" \\\n     -H \"Content-Type: application/x-www-form-urlencoded\" \\\n \
  \    -H \"X-Forwarded-For: FUZZ\" -w ipv4-list.txt:FUZZ \\\n     -mc all\n```\n\n## Rate Limit\n\n### HTTP Pipelining\n\n\
  HTTP pipelining is a feature of HTTP/1.1 that lets a client send multiple HTTP requests on a single persistent TCP connection\
  \ without waiting for the corresponding responses first. The client \"pipes\" requests one after another over the same connection.\n\
  \n### TLS Stack - JA3\n\nJA3 is a method for fingerprinting TLS clients (and JA3S for TLS servers) by hashing the contents\
  \ of the TLS \"hello\" messages. It gives a compact identifier you can use to detect, classify, and track clients on the\
  \ network even when higher-level protocol fields (like HTTP user-agent) are hidden or faked.\n\n> JA3 gathers the decimal\
  \ values of the bytes for the following fields in the Client Hello packet; SSL Version, Accepted Ciphers, List of Extensions,\
  \ Elliptic Curves, and Elliptic Curve Formats. It then concatenates those values together in order, using a \",\" to delimit\
  \ each field and a \"-\" to delimit each value in each field.\n\n* Burp Suite JA3: `53d67b2a806147a7d1d5df74b54dd049`, `62f6a6727fda5a1104d5b147cd82e520`\n\
  * Tor Client JA3: `e7d705a3286e19ea42f587b344ee6865`\n\n**Countermeasures:**\n\n* Use browser-driven automation (Puppeteer\
  \ / Playwright)\n* Spoof TLS handshakes with [lwthiker/curl-impersonate](https://github.com/lwthiker/curl-impersonate)\n\
  * JA3 randomization plugins for browsers/libraries\n\n### Network IPv4\n\nUse multiple proxies to simulate multiple clients.\n\
  \n```bash\nproxychains ffuf -w wordlist.txt -u https://target.tld/FUZZ\n```\n\n* Use `random_chain` to rotate each request\n\
  \n    ```ps1\n    random_chain\n    ```\n\n* Set the number of proxies to chain per connection to 1.\n\n    ```ps1\n   \
  \ chain_len = 1\n    ```\n\n* Finally, specify the proxies in a configuration file:\n\n    ```ps1\n    # type  host    \
  \  port\n    socks5  127.0.0.1 1080\n    socks5  192.168.1.50 1080\n    http    proxy1.example.com 8080\n    http    proxy2.example.com\
  \ 8080\n    ```\n\n### Network IPv6\n\nMany cloud providers, such as Vultr, offer /64 IPv6 ranges, which provide a vast\
  \ number of addresses (18 446 744 073 709 551 616). This allows for extensive IP rotation during brute-force attacks.\n\n\
  ## References\n\n* [Bruteforcing the phone number of any Google user - brutecat - June 9, 2025](https://web.archive.org/web/20250609141236/https://brutecat.com/articles/leaking-google-phones)\n\
  * [Burp Intruder attack types - PortSwigger - August 19, 2025](https://web.archive.org/web/20260124024947/https://portswigger.net/burp/documentation/desktop/tools/intruder/configure-attack/attack-types)\n\
  * [Detecting and annoying Burp users - Julien Voisin -  May 3, 2021](https://web.archive.org/web/20260102160139/https://dustri.org/b/detecting-and-annoying-burp-users.html)\n\
  * [OmniProx: Multi-Cloud IP Rotation Made Simple - Andy Gill - September 28, 2025](https://web.archive.org/web/20260215082718/https://blog.zsec.uk/omniprox/)"
_relative_path: Brute Force Rate Limit/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Brute Force Rate Limit/README.md
````
