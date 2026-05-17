---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Text Steganography

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-stego-text-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/stego/text/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Text Steganography](../../topics/stego/text-steganography.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-stego-text-readme |
| name | Text Steganography |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/stego/text/README.md |

## Preserved Source Material

````yaml
_body: "# Text Steganography\n\n{{#include ../../banners/hacktricks-training.md}}\n\nLook for:\n\n- Unicode homoglyphs\n-\
  \ Zero-width characters\n- Whitespace patterns (spaces vs tabs)\n\n## Practical path\n\nIf plain text behaves unexpectedly,\
  \ inspect codepoints and normalize carefully (do not destroy evidence).\n\n### Technique\n\nText stego frequently relies\
  \ on characters that render identically (or invisibly):\n\n- Homoglyphs: different Unicode codepoints that look the same\
  \ (Latin `a` vs Cyrillic `а`)\n- Zero-width characters: joiners, non-joiners, zero-width spaces\n- Whitespace encodings:\
  \ spaces vs tabs, trailing spaces, line-length patterns\n\nAdditional high-signal cases:\n\n- Bidirectional override/control\
  \ characters (can visually reorder text)\n- Variation selectors and combining characters used as a covert channel\n\n###\
  \ Decode helpers\n\n- Unicode homoglyph/zero-width playground: https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder\n\
  \n### Inspect codepoints\n\n```bash\npython3 - <<'PY'\nimport sys\ns=sys.stdin.read()\nfor i,ch in enumerate(s):\n  if ord(ch)\
  \ > 127 or ch.isspace():\n    print(i, hex(ord(ch)), repr(ch))\nPY\n```\n\n## CSS `unicode-range` channels\n\n`@font-face`\
  \ rules can encode bytes in `unicode-range: U+..` entries. Extract the codepoints, concatenate the hex, and decode:\n\n\
  ```bash\ngrep -o \"U+[0-9A-Fa-f]\\+\" styles.css | tr -d 'U+\\n' | xxd -r -p\n```\n\nIf ranges contain multiple bytes per\
  \ declaration, split on commas first and normalize (`tr ',+' '\\n'`). Python makes it easy to parse and emit bytes if formatting\
  \ is inconsistent.\n\n## References\n\n- [Flagvent 2025 (Medium) — pink, Santa’s Wishlist, Christmas Metadata, Captured\
  \ Noise](https://0xdf.gitlab.io/flagvent2025/medium)\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: stego/text/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/stego/text/README.md
````
