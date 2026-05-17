---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Sniff Leak

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-xss-cross-site-scripting-sniff-leak` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xss-cross-site-scripting/sniff-leak.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Sniff Leak](../../topics/pentesting-web/sniff-leak.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-xss-cross-site-scripting-sniff-leak |
| name | Sniff Leak |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/xss-cross-site-scripting/sniff-leak.md |

## Preserved Source Material

```yaml
_body: '# Sniff Leak


  {{#include ../../banners/hacktricks-training.md}}


  ## Leak script content by converting it to UTF16


  [**This writeup**](https://blog.huli.tw/2022/08/01/en/uiuctf-2022-writeup/#modernism21-solves) leaks a text/plain because
  there is no `X-Content-Type-Options: nosniff` header by adding some initial characters that will make javascript think that
  the content is in UTF-16 so th script doesn''t breaks.


  ## Leak script content by treating it as an ICO


  [**The next writeup**](https://blog.huli.tw/2022/08/01/en/uiuctf-2022-writeup/#precisionism3-solves) leaks the script content
  by loading it as if it was an ICO image accessing the `width` parameter.


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: pentesting-web/xss-cross-site-scripting/sniff-leak.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/xss-cross-site-scripting/sniff-leak.md
```
