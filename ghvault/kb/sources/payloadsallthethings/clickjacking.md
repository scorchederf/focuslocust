---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Clickjacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-clickjacking-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Clickjacking/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Clickjacking](../../topics/clickjacking/clickjacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-clickjacking-readme |
| name | Clickjacking |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Clickjacking/README.md |

## Preserved Source Material

````yaml
_body: "# Clickjacking\n\n> Clickjacking is a type of web security vulnerability where a malicious website tricks a user into\
  \ clicking on something different from what the user perceives, potentially causing the user to perform unintended actions\
  \ without their knowledge or consent. Users are tricked into performing all sorts of unintended actions as such as typing\
  \ in the password, clicking on ‘Delete my account' button, liking a post, deleting a post, commenting on a blog. In other\
  \ words all the actions that a normal user can do on a legitimate website can be done using clickjacking.\n\n## Summary\n\
  \n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [UI Redressing](#ui-redressing)\n    * [Invisible Frames](#invisible-frames)\n\
  \    * [Button/Form Hijacking](#buttonform-hijacking)\n    * [Execution Methods](#execution-methods)\n* [Preventive Measures](#preventive-measures)\n\
  \    * [Implement X-Frame-Options Header](#implement-x-frame-options-header)\n    * [Content Security Policy (CSP)](#content-security-policy-csp)\n\
  \    * [Disabling JavaScript](#disabling-javascript)\n* [OnBeforeUnload Event](#onbeforeunload-event)\n* [XSS Filter](#xss-filter)\n\
  \    * [IE8 XSS filter](#ie8-xss-filter)\n    * [Chrome 4.0 XSSAuditor filter](#chrome-40-xssauditor-filter)\n* [Challenge](#challenge)\n\
  * [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [portswigger/burp](https://portswigger.net/burp)\n* [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)\n\
  * [machine1337/clickjack](https://github.com/machine1337/clickjack)\n\n## Methodology\n\n### UI Redressing\n\nUI Redressing\
  \ is a Clickjacking technique where an attacker overlays a transparent UI element on top of a legitimate website or application.\n\
  The transparent UI element contains malicious content or actions that are visually hidden from the user. By manipulating\
  \ the transparency and positioning of elements,\nthe attacker can trick the user into interacting with the hidden content,\
  \ believing they are interacting with the visible interface.\n\n* **How UI Redressing Works:**\n    * Overlaying Transparent\
  \ Element: The attacker creates a transparent HTML element (usually a `<div>`) that covers the entire visible area of a\
  \ legitimate website. This element is made transparent using CSS properties like `opacity: 0;`.\n    * Positioning and Layering:\
  \ By setting the CSS properties such as `position: absolute; top: 0; left: 0;`, the transparent element is positioned to\
  \ cover the entire viewport. Since it's transparent, the user doesn't see it.\n    * Misleading User Interaction: The attacker\
  \ places deceptive elements within the transparent container, such as fake buttons, links, or forms. These elements perform\
  \ actions when clicked, but the user is unaware of their presence due to the overlaying transparent UI element.\n    * User\
  \ Interaction: When the user interacts with the visible interface, they are unknowingly interacting with the hidden elements\
  \ due to the transparent overlay. This interaction can lead to unintended actions or unauthorized operations.\n\n```html\n\
  <div style=\"opacity: 0; position: absolute; top: 0; left: 0; height: 100%; width: 100%;\">\n  <a href=\"malicious-link\"\
  >Click me</a>\n</div>\n```\n\n### Invisible Frames\n\nInvisible Frames is a Clickjacking technique where attackers use hidden\
  \ iframes to trick users into interacting with content from another website unknowingly.\nThese iframes are made invisible\
  \ by setting their dimensions to zero (height: 0; width: 0;) and removing their borders (border: none;).\nThe content inside\
  \ these invisible frames can be malicious, such as phishing forms, malware downloads, or any other harmful actions.\n\n\
  * **How Invisible Frames Work:**\n    * Hidden IFrame Creation: The attacker includes an `<iframe>` element in a webpage,\
  \ setting its dimensions to zero and removing its border, making it invisible to the user.\n\n      ```html\n      <iframe\
  \ src=\"malicious-site\" style=\"opacity: 0; height: 0; width: 0; border: none;\"></iframe>\n      ```\n\n    * Loading\
  \ Malicious Content: The src attribute of the iframe points to a malicious website or resource controlled by the attacker.\
  \ This content is loaded silently without the user's knowledge because the iframe is invisible.\n    * User Interaction:\
  \ The attacker overlays enticing elements on top of the invisible iframe, making it seem like the user is interacting with\
  \ the visible interface. For instance, the attacker might position a transparent button over the invisible iframe. When\
  \ the user clicks the button, they are essentially clicking on the hidden content within the iframe.\n    * Unintended Actions:\
  \ Since the user is unaware of the invisible iframe, their interactions can lead to unintended actions, such as submitting\
  \ forms, clicking on malicious links, or even performing financial transactions without their consent.\n\n### Button/Form\
  \ Hijacking\n\nButton/Form Hijacking is a Clickjacking technique where attackers trick users into interacting with invisible\
  \ or hidden buttons/forms, leading to unintended actions on a legitimate website. By overlaying deceptive elements on top\
  \ of visible buttons or forms, attackers can manipulate user interactions to perform malicious actions without the user's\
  \ knowledge.\n\n* **How Button/Form Hijacking Works:**\n    * Visible Interface: The attacker presents a visible button\
  \ or form to the user, encouraging them to click or interact with it.\n\n    ```html\n    <button onclick=\"submitForm()\"\
  >Click me</button>\n    ```\n\n    * Invisible Overlay: The attacker overlays this visible button or form with an invisible\
  \ or transparent element that contains a malicious action, such as submitting a hidden form.\n\n    ```html\n    <form action=\"\
  malicious-site\" method=\"POST\" id=\"hidden-form\" style=\"display: none;\">\n    <!-- Hidden form fields -->\n    </form>\n\
  \    ```\n\n    * Deceptive Interaction: When the user clicks the visible button, they are unknowingly interacting with\
  \ the hidden form due to the invisible overlay. The form is submitted, potentially causing unauthorized actions or data\
  \ leakage.\n\n    ```html\n    <button onclick=\"submitForm()\">Click me</button>\n    <form action=\"legitimate-site\"\
  \ method=\"POST\" id=\"hidden-form\">\n      <!-- Hidden form fields -->\n    </form>\n    <script>\n      function submitForm()\
  \ {\n        document.getElementById('hidden-form').submit();\n      }\n    </script>\n    ```\n\n### Execution Methods\n\
  \n* Creating Hidden Form: The attacker creates a hidden form containing malicious input fields, targeting a vulnerable action\
  \ on the victim's website. This form remains invisible to the user.\n\n```html\n  <form action=\"malicious-site\" method=\"\
  POST\" id=\"hidden-form\" style=\"display: none;\">\n  <input type=\"hidden\" name=\"username\" value=\"attacker\">\n  <input\
  \ type=\"hidden\" name=\"action\" value=\"transfer-funds\">\n  </form>\n```\n\n* Overlaying Visible Element: The attacker\
  \ overlays a visible element (button or form) on their malicious page, encouraging users to interact with it. When the user\
  \ clicks the visible element, they unknowingly trigger the hidden form's submission.\n\n```js\n  function submitForm() {\n\
  \    document.getElementById('hidden-form').submit();\n  }\n```\n\n## Preventive Measures\n\n### Implement X-Frame-Options\
  \ Header\n\nImplement the X-Frame-Options header with the DENY or SAMEORIGIN directive to prevent your website from being\
  \ embedded within an iframe without your consent.\n\n```apache\nHeader always append X-Frame-Options SAMEORIGIN\n```\n\n\
  ### Content Security Policy (CSP)\n\nUse CSP to control the sources from which content can be loaded on your website, including\
  \ scripts, styles, and frames.\nDefine a strong CSP policy to prevent unauthorized framing and loading of external resources.\n\
  Example in HTML meta tag:\n\n```html\n<meta http-equiv=\"Content-Security-Policy\" content=\"frame-ancestors 'self';\">\n\
  ```\n\n### Disabling JavaScript\n\n* Since these type of client side protections relies on JavaScript frame busting code,\
  \ if the victim has JavaScript disabled or it is possible for an attacker to disable JavaScript code, the web page will\
  \ not have any protection mechanism against clickjacking.\n* There are three deactivation techniques that can be used with\
  \ frames:\n    * Restricted frames with Internet Explorer: Starting from IE6, a frame can have the \"security\" attribute\
  \ that, if it is set to the value \"restricted\", ensures that JavaScript code, ActiveX controls, and re-directs to other\
  \ sites do not work in the frame.\n\n    ```html\n    <iframe src=\"http://target site\" security=\"restricted\"></iframe>\n\
  \    ```\n\n    * Sandbox attribute: with HTML5 there is a new attribute called “sandbox”. It enables a set of restrictions\
  \ on content loaded into the iframe. At this moment this attribute is only compatible with Chrome and Safari.\n\n    ```html\n\
  \    <iframe src=\"http://target site\" sandbox></iframe>\n    ```\n\n## OnBeforeUnload Event\n\n* The `onBeforeUnload`\
  \ event could be used to evade frame busting code. This event is called when the frame busting code wants to destroy the\
  \ iframe by loading the URL in the whole web page and not only in the iframe. The handler function returns a string that\
  \ is prompted to the user asking confirm if he wants to leave the page. When this string is displayed to the user is likely\
  \ to cancel the navigation, defeating target's frame busting attempt.\n\n* The attacker can use this attack by registering\
  \ an unload event on the top page using the following example code:\n\n```html\n<h1>www.fictitious.site</h1>\n<script>\n\
  \    window.onbeforeunload = function()\n    {\n        return \" Do you want to leave fictitious.site?\";\n    }\n</script>\n\
  <iframe src=\"http://target site\">\n```\n\n* The previous technique requires the user interaction but, the same result,\
  \ can be achieved without prompting the user. To do this the attacker have to automatically cancel the incoming navigation\
  \ request in an onBeforeUnload event handler by repeatedly submitting (for example every millisecond) a navigation request\
  \ to a web page that responds with a _\"HTTP/1.1 204 No Content\"_ header.\n\n204 page:\n\n```php\n<?php\n    header(\"\
  HTTP/1.1 204 No Content\");\n?>\n```\n\nAttacker's Page:\n\n```js\n<script>\n    var prevent_bust = 0;\n    window.onbeforeunload\
  \ = function() {\n        prevent_bust++;\n    };\n    setInterval(\n        function() {\n            if (prevent_bust\
  \ > 0) {\n                prevent_bust -= 2;\n                window.top.location = \"http://attacker.site/204.php\";\n\
  \            }\n        }, 1);\n</script>\n<iframe src=\"http://target site\">\n```\n\n## XSS Filter\n\n### IE8 XSS filter\n\
  \nThis filter has visibility into all parameters of each request and response flowing through the web browser and it compares\
  \ them to a set of regular expressions in order to look for reflected XSS attempts. When the filter identifies a possible\
  \ XSS attacks; it disables all inline scripts within the page, including frame busting scripts (the same thing could be\
  \ done with external scripts). For this reason an attacker could induce a false positive by inserting the beginning of the\
  \ frame busting script into a request's parameters.\n\n```html\n<script>\n    if ( top != self )\n    {\n        top.location=self.location;\n\
  \    }\n</script>\n```\n\nAttacker View:\n\n```html\n<iframe src=”http://target site/?param=<script>if”>\n```\n\n### Chrome\
  \ 4.0 XSSAuditor filter\n\nIt has a little different behaviour compared to IE8 XSS filter, in fact with this filter an attacker\
  \ could deactivate a “script” by passing its code in a request parameter. This enables the framing page to specifically\
  \ target a single snippet containing the frame busting code, leaving all the other codes intact.\n\nAttacker View:\n\n```html\n\
  <iframe src=”http://target site/?param=if(top+!%3D+self)+%7B+top.location%3Dself.location%3B+%7D”>\n```\n\n## Challenge\n\
  \nInspect the following code:\n\n```html\n<div style=\"position: absolute; opacity: 0;\">\n  <iframe src=\"https://legitimate-site.com/login\"\
  \ width=\"500\" height=\"500\"></iframe>\n</div>\n<button onclick=\"document.getElementsByTagName('iframe')[0].contentWindow.location='malicious-site.com';\"\
  >Click me</button>\n```\n\nDetermine the Clickjacking vulnerability within this code snippet. Identify how the hidden iframe\
  \ is being used to exploit the user's actions when they click the button, leading them to a malicious website.\n\n## Labs\n\
  \n* [OWASP WebGoat](https://owasp.org/www-project-webgoat/)\n* [OWASP Client Side Clickjacking Test](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/09-Testing_for_Clickjacking)\n\
  \n## References\n\n* [Clickjacker.io - Saurabh Banawar - May 10, 2020](https://web.archive.org/web/20200510214313/https://clickjacker.io/)\n\
  * [Clickjacking - Gustav Rydstedt - April 28, 2020](https://web.archive.org/web/20200428022051/https://owasp.org/www-community/attacks/Clickjacking)\n\
  * [Synopsys Clickjacking - BlackDuck - November 29, 2019](https://web.archive.org/web/20240917212838/https://www.synopsys.com/glossary/what-is-clickjacking.html)\n\
  * [Web-Security Clickjacking - PortSwigger - October 12, 2019](https://web.archive.org/web/20260215062230/https://portswigger.net/web-security/clickjacking)"
_relative_path: Clickjacking/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Clickjacking/README.md
````
