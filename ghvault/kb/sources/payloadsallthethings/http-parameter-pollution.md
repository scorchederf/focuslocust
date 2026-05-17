---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# HTTP Parameter Pollution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-http-parameter-pollution-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/HTTP Parameter Pollution/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [HTTP Parameter Pollution](../../topics/http-parameter-pollution/http-parameter-pollution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-http-parameter-pollution-readme |
| name | HTTP Parameter Pollution |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/HTTP%20Parameter%20Pollution/README.md |

## Preserved Source Material

````yaml
_body: "# HTTP Parameter Pollution\n\n> HTTP Parameter Pollution (HPP) is a Web attack evasion technique that allows an attacker\
  \ to craft a HTTP request in order to manipulate web logics or retrieve hidden information. This evasion technique is based\
  \ on splitting an attack vector between multiple instances of a parameter with the same name (?param1=value&param1=value).\
  \ As there is no formal way of parsing HTTP parameters, individual web technologies have their own unique way of parsing\
  \ and reading URL parameters with the same name. Some taking the first occurrence, some taking the last occurrence, and\
  \ some reading it as an array. This behavior is abused by the attacker in order to bypass pattern-based security mechanisms.\n\
  \n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Parameter Pollution Table](#parameter-pollution-table)\n\
  \    * [Parameter Pollution Payloads](#parameter-pollution-payloads)\n* [References](#references)\n\n## Tools\n\n* **Burp\
  \ Suite**: Manually modify requests to test duplicate parameters.\n* **OWASP ZAP**: Intercept and manipulate HTTP parameters.\n\
  \n## Methodology\n\nHTTP Parameter Pollution (HPP) is a web security vulnerability where an attacker injects multiple instances\
  \ of the same HTTP parameter into a request. The server's behavior when processing duplicate parameters can vary, potentially\
  \ leading to unexpected or exploitable behavior.\n\nHPP can target two levels:\n\n* Client-Side HPP: Exploits JavaScript\
  \ code running on the client (browser).\n* Server-Side HPP: Exploits how the server processes multiple parameters with the\
  \ same name.\n\n**Examples**:\n\n```ps1\n/app?debug=false&debug=true\n/transfer?amount=1&amount=5000\n```\n\n### Parameter\
  \ Pollution Table\n\nWhen ?par1=a&par1=b\n\n| Technology                                      | Parsing Result         \
  \  | outcome (par1=) |\n| ----------------------------------------------- | ------------------------ | --------------- |\n\
  | ASP.NET/IIS                                     | All occurrences          | a,b             |\n| ASP/IIS            \
  \                             | All occurrences          | a,b             |\n| Golang net/http - `r.URL.Query().Get(\"\
  param\")`  | First occurrence         | a               |\n| Golang net/http - `r.URL.Query()[\"param\"]`      | All occurrences\
  \ in array | ['a','b']       |\n| IBM HTTP Server                                 | First occurrence         | a       \
  \        |\n| IBM Lotus Domino                                | First occurrence         | a               |\n| JSP,Servlet/Tomcat\
  \                              | First occurrence         | a               |\n| mod_wsgi (Python)/Apache              \
  \          | First occurrence         | a               |\n| Nodejs                                          | All occurrences\
  \          | a,b             |\n| Perl CGI/Apache                                 | First occurrence         | a       \
  \        |\n| Perl CGI/Apache                                 | First occurrence         | a               |\n| PHP/Apache\
  \                                      | Last occurrence          | b               |\n| PHP/Zues                      \
  \                  | Last occurrence          | b               |\n| Python Django                                   | Last\
  \ occurrence          | b               |\n| Python Flask                                    | First occurrence        \
  \ | a               |\n| Python/Zope                                     | All occurrences in array | ['a','b']       |\n\
  | Ruby on Rails                                   | Last occurrence          | b               |\n\n### Parameter Pollution\
  \ Payloads\n\n* Duplicate Parameters:\n\n    ```ps1\n    param=value1&param=value2\n    ```\n\n* Array Injection:\n\n  \
  \  ```ps1\n    param[]=value1\n    param[]=value1&param[]=value2\n    param[]=value1&param=value2\n    param=value1&param[]=value2\n\
  \    ```\n\n* Encoded Injection:\n\n    ```ps1\n    param=value1%26other=value2\n    ```\n\n* Nested Injection:\n\n    ```ps1\n\
  \    param[key1]=value1&param[key2]=value2\n    ```\n\n* JSON Injection:\n\n    ```ps1\n    {\n        \"test\": \"user\"\
  ,\n        \"test\": \"admin\"\n    }\n    ```\n\n## References\n\n* [How to Detect HTTP Parameter Pollution Attacks - Acunetix\
  \ - January 9, 2024](https://web.archive.org/web/20260112091623/https://www.acunetix.com/blog/whitepaper-http-parameter-pollution/)\n\
  * [HTTP Parameter Pollution - Itamar Verta - December 20, 2023](https://web.archive.org/web/20190721110154/https://www.imperva.com/learn/application-security/http-parameter-pollution/)\n\
  * [HTTP Parameter Pollution in 11 minutes - PwnFunction - January 28, 2019](https://web.archive.org/web/20190212095035/https://www.youtube.com/watch?v=QVZBl8yxVX0)"
_relative_path: HTTP Parameter Pollution/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/HTTP Parameter Pollution/README.md
````
