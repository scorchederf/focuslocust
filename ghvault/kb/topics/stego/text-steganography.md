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

## Summary

Look for:

## Preserved Body

````markdown
Look for:

- Unicode homoglyphs
- Zero-width characters
- Whitespace patterns (spaces vs tabs)

## Practical path

If plain text behaves unexpectedly, inspect codepoints and normalize carefully (do not destroy evidence).

### Technique

Text stego frequently relies on characters that render identically (or invisibly):

- Homoglyphs: different Unicode codepoints that look the same (Latin `a` vs Cyrillic `а`)
- Zero-width characters: joiners, non-joiners, zero-width spaces
- Whitespace encodings: spaces vs tabs, trailing spaces, line-length patterns

Additional high-signal cases:

- Bidirectional override/control characters (can visually reorder text)
- Variation selectors and combining characters used as a covert channel

### Decode helpers

- Unicode homoglyph/zero-width playground: https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder

### Inspect codepoints

```bash
python3 - <<'PY'
import sys
s=sys.stdin.read()
for i,ch in enumerate(s):
  if ord(ch) > 127 or ch.isspace():
    print(i, hex(ord(ch)), repr(ch))
PY
```

## CSS `unicode-range` channels

`@font-face` rules can encode bytes in `unicode-range: U+..` entries. Extract the codepoints, concatenate the hex, and decode:

```bash
grep -o "U+[0-9A-Fa-f]\+" styles.css | tr -d 'U+\n' | xxd -r -p
```

If ranges contain multiple bytes per declaration, split on commas first and normalize (`tr ',+' '\n'`). Python makes it easy to parse and emit bytes if formatting is inconsistent.

## References

- [Flagvent 2025 (Medium) — pink, Santa’s Wishlist, Christmas Metadata, Captured Noise](https://0xdf.gitlab.io/flagvent2025/medium)
````

## Source Verification

[source record](../../sources/hacktricks/text-steganography.md)

## Evidence Excerpt

```text
_body: "# Text Steganography\n\n{{#include ../../banners/hacktricks-training.md}}\n\nLook for:\n\n- Unicode homoglyphs\n-\
\ Zero-width characters\n- Whitespace patterns (spaces vs tabs)\n\n## Practical path\n\nIf plain text behaves unexpectedly,\
\ inspect codepoints and normalize carefully (do not destroy evidence).\n\n### Technique\n\nText stego frequently relies\
\ on characters that render identically (or invisibly):\n\n- Homoglyphs: different Unicode codepoints that look the same\
\ (Latin `a` vs Cyrillic `а`)\n- Zero-width characters: joiners, non-joiners, zero-width spaces\n- Whitespace encodings:\
\ spaces vs tabs, trailing spaces, line-length patterns\n\nAdditional high-signal cases:\n\n- Bidirectional override/control\
\ characters (can visually reorder text)\n- Variation selectors and combining characters used as a covert channel\n\n###\
\ Decode helpers\n\n- Unicode homoglyph/zero-width playground: https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder\n\
```
