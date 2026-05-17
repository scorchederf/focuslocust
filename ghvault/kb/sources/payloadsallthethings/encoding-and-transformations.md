---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Encoding and Transformations

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-encoding-transformations-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Encoding Transformations/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Encoding and Transformations](../../topics/encoding-transformations/encoding-and-transformations.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-encoding-transformations-readme |
| name | Encoding and Transformations |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Encoding%20Transformations/README.md |

## Preserved Source Material

````yaml
_body: "# Encoding and Transformations\n\n> Encoding and Transformations are techniques that change how data is represented\
  \ or transferred without altering its core meaning. Common examples include URL encoding, Base64, HTML entity encoding,\
  \ and Unicode transformations. Attackers use these methods as gadgets to bypass input filters, evade web application firewalls,\
  \ or break out of sanitization routines.\n\n## Summary\n\n* [Unicode](#unicode)\n    * [Unicode Normalization](#unicode-normalization)\n\
  \    * [Punycode](#punycode)\n* [Base64](#base64)\n* [Labs](#labs)\n* [References](#references)\n\n## Unicode\n\nUnicode\
  \ is a universal character encoding standard used to represent text from virtually every writing system in the world. Each\
  \ character (letters, numbers, symbols, emojis) is assigned a unique code point (for example, U+0041 for \"A\"). Unicode\
  \ encoding formats like UTF-8 and UTF-16 specify how these code points are stored as bytes.\n\n### Unicode Normalization\n\
  \nUnicode normalization is the process of converting Unicode text into a standardized, consistent form so that equivalent\
  \ characters are represented the same way in memory.\n\n[Unicode Normalization reference table](https://appcheck-ng.com/wp-content/uploads/unicode_normalization.html)\n\
  \n* **NFC** (Normalization Form Canonical Composition): Combines decomposed sequences into precomposed characters where\
  \ possible.\n* **NFD** (Normalization Form Canonical Decomposition): Breaks characters into their decomposed forms (base\
  \ + combining marks).\n* **NFKC** (Normalization Form Compatibility Composition): Like NFC, but also replaces characters\
  \ with compatibility equivalents (may change appearance/format).\n* **NFKD** (Normalization Form Compatibility Decomposition):\
  \ Like NFD, but also decomposes compatibility characters.\n\n| Character    | Payload               | After Normalization\
  \   |\n| ------------ | --------------------- | --------------------- |\n| `‥` (U+2025) | `‥/‥/‥/etc/passwd` | `../../../etc/passwd`\
  \ |\n| `︰` (U+FE30) | `︰/︰/︰/etc/passwd` | `../../../etc/passwd` |\n| `＇` (U+FF07) | `＇ or ＇1＇=＇1` | `' or '1'='1` |\n|\
  \ `＂` (U+FF02) | `＂ or ＂1＂=＂1` | `\" or \"1\"=\"1` |\n| `﹣` (U+FE63) | `admin'﹣﹣` | `admin'--` |\n| `。` (U+3002) | `domain。com`\
  \ | `domain.com` |\n| `／` (U+FF0F) | `／／domain.com` | `//domain.com` |\n| `＜` (U+FF1C) | `＜img src=a＞` | `<img src=a/>`\
  \ |\n| `﹛` (U+FE5B) | `﹛﹛3+3﹜﹜` | `{{3+3}}` |\n| `［` (U+FF3B) | `［［5+5］］` | `[[5+5]]` |\n| `＆` (U+FF06) | `＆＆whoami` | `&&whoami`\
  \ |\n| `ｐ` (U+FF50) | `shell.ｐʰｐ` | `shell.php` |\n| `ʰ` (U+02B0) | `shell.ｐʰｐ` | `shell.php` |\n| `ª` (U+00AA) | `ªdmin`\
  \ | `admin` |\n\n```py\nimport unicodedata\nstring = \"ᴾᵃʸˡᵒᵃᵈˢ\U0001D4D0\U0001D4F5\U0001D4F5\U0001D54B\U0001D559\U0001D556\
  \U0001D4AF\U0001D4BD\U0001D4BE\U0001D4C3ℊ\U0001D4C8\"\nprint ('NFC: ' + unicodedata.normalize('NFC', string))\nprint ('NFD:\
  \ ' + unicodedata.normalize('NFD', string))\nprint ('NFKC: ' + unicodedata.normalize('NFKC', string))\nprint ('NFKD: ' +\
  \ unicodedata.normalize('NFKD', string))\n```\n\n### Punycode\n\nPunycode is a way to represent Unicode characters (including\
  \ non-ASCII letters, symbols, and scripts) using only the limited set of ASCII characters (letters, digits, and hyphens).\n\
  \nIt's mainly used in the Domain Name System (DNS), which traditionally supports only ASCII. Punycode allows internationalized\
  \ domain names (IDNs), so that domain names can include characters from many languages by converting them into a safe ASCII\
  \ form.\n\n| Visible in Browser (IDN support) | Actual ASCII (Punycode) |\n| -------------------------------- | -----------------------\
  \ |\n| раypal.com                       | xn--ypal-43d9g.com      |\n| paypal.com                       | paypal.com   \
  \           |\n\nIn MySQL, similar character are treated as equal. This behavior can be abused in Password Reset, Forgot\
  \ Password, and OAuth Provider sections.\n\n```sql\nSELECT 'a' = 'ᵃ';\n+-------------+\n| 'a' = 'ᵃ'   |\n+-------------+\n\
  |           1 |\n+-------------+\n```\n\nThis trick works the SQL query uses `COLLATE utf8mb4_0900_as_cs`.\n\n```sql\nSELECT\
  \ 'a' = 'ᵃ' COLLATE utf8mb4_0900_as_cs;\n+----------------------------------------+\n| 'a' = 'ᵃ' COLLATE utf8mb4_0900_as_cs\
  \   |\n+----------------------------------------+\n|                                      0 |\n+----------------------------------------+\n\
  ```\n\n## Base64\n\nBase64 encoding is a method for converting binary data (like images or files) or text with special characters\
  \ into a readable string that uses only ASCII characters (A-Z, a-z, 0-9, +, and /). Every 3 bytes of input are divided into\
  \ 4 groups of 6 bits and mapped to 4 Base64 characters. If the input isn't a multiple of 3 bytes, the output is padded with\
  \ `=` characters.\n\n```ps1\necho -n admin | base64                            \nYWRtaW4=\n\necho -n YWRtaW4= | base64 -d\n\
  admin\n```\n\n## Labs\n\n* [NahamCon - Puny-Code: 0-Click Account Takeover](https://github.com/VoorivexTeam/white-box-challenges/tree/main/punycode)\n\
  * [PentesterLab - Unicode and NFKC](https://pentesterlab.com/exercises/unicode-transform)\n\n## References\n\n* [Puny-Code,\
  \ 0-Click Account Takeover - Voorivex - June 1, 2025](https://web.archive.org/web/20251211233427/https://blog.voorivex.team/puny-code-0-click-account-takeover)\n\
  * [Unicode normalization vulnerabilities - Lazar - September 30, 2021](https://web.archive.org/web/20251224043224/https://lazarv.com/posts/unicode-normalization-vulnerabilities/)\n\
  * [Unicode Normalization Vulnerabilities & the Special K Polyglot - AppCheck - September 2, 2019](https://web.archive.org/web/20190916002602/https://appcheck-ng.com/unicode-normalization-vulnerabilities-the-special-k-polyglot/)\n\
  * [WAF Bypassing with Unicode Compatibility - Jorge Lajara - February 19, 2020](https://web.archive.org/web/20251230185141/https://jlajara.gitlab.io/Bypass_WAF_Unicode)\n\
  * [When \"Zoë\" !== \"Zoë\". Or why you need to normalize Unicode strings - Alessandro Segala - March 11, 2019](https://web.archive.org/web/20260128220322/https://withblue.ink/2019/03/11/why-you-need-to-normalize-unicode-strings.html)"
_relative_path: Encoding Transformations/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Encoding Transformations/README.md
````
