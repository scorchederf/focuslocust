---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Regular Expression

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-regular-expression-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Regular Expression/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Regular Expression](../../topics/regular-expression/regular-expression.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-regular-expression-readme |
| name | Regular Expression |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Regular%20Expression/README.md |

## Preserved Source Material

````yaml
_body: "# Regular Expression\n\n> Regular Expression Denial of Service (ReDoS) is a type of attack that exploits the fact\
  \ that certain regular expressions can take an extremely long time to process, causing applications or services to become\
  \ unresponsive or crash.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Evil Regex](#evil-regex)\n\
  \    * [Backtrack Limit](#backtrack-limit)\n* [References](#references)\n\n## Tools\n\n* [tjenkinson/redos-detector](https://github.com/tjenkinson/redos-detector)\
  \ - A CLI and library which tests with certainty if a regex pattern is safe from ReDoS attacks. Supported in the browser,\
  \ Node and Deno.\n* [doyensec/regexploit](https://github.com/doyensec/regexploit) - Find regular expressions which are vulnerable\
  \ to ReDoS (Regular Expression Denial of Service)\n* [devina.io/redos-checker](https://devina.io/redos-checker) - Examine\
  \ regular expressions for potential Denial of Service vulnerabilities\n\n## Methodology\n\n### Evil Regex\n\nEvil Regex\
  \ contains:\n\n* Grouping with repetition\n* Inside the repeated group:\n    * Repetition\n    * Alternation with overlapping\n\
  \n**Examples**:\n\n* `(a+)+`\n* `([a-zA-Z]+)*`\n* `(a|aa)+`\n* `(a|a?)+`\n* `(.*a){x}` for x \\> 10\n\nThese regular expressions\
  \ can be exploited with `aaaaaaaaaaaaaaaaaaaaaaaa!` (20 'a's followed by a '!').\n\n```ps1\naaaaaaaaaaaaaaaaaaaa! \n```\n\
  \nFor this input, the regex engine will try all possible ways to group the `a` characters before realizing that the match\
  \ ultimately fails because of the `!`. This results in an explosion of backtracking attempts.\n\n### Backtrack Limit\n\n\
  Backtracking in regular expressions occurs when the regex engine tries to match a pattern and encounters a mismatch. The\
  \ engine then backtracks to the previous matching position and tries an alternative path to find a match. This process can\
  \ be repeated many times, especially with complex patterns and large input strings.  \n\n**PHP PCRE configuration options**:\n\
  \n| Name                 | Default | Note |\n|----------------------|---------|---------|\n| pcre.backtrack_limit | 1000000\
  \ | 100000 for `PHP < 5.3.7`|\n| pcre.recursion_limit | 100000  | / |\n| pcre.jit             | 1       | / |\n\nSometimes\
  \ it is possible to force the regex to exceed more than 100 000 recursions which will cause a ReDOS and make `preg_match`\
  \ returning false:\n\n```php\n$pattern = '/(a+)+$/';\n$subject = str_repeat('a', 1000) . 'b';\n\nif (preg_match($pattern,\
  \ $subject)) {\n    echo \"Match found\";\n} else {\n    echo \"No match\";\n}\n```\n\n## References\n\n* [Intigriti Challenge\
  \ 1223 - Hackbook Of A Hacker - December 21, 2023](https://web.archive.org/web/20260210185049/https://simones-organization-4.gitbook.io/hackbook-of-a-hacker/ctf-writeups/intigriti-challenges/1223)\n\
  * [MyBB Admin Panel RCE CVE-2023-41362 - SorceryIE - September 11, 2023](https://web.archive.org/web/20251115110845/https://blog.sorcery.ie/posts/mybb_acp_rce/)\n\
  * [OWASP Validation Regex Repository - OWASP - March 14, 2018](https://web.archive.org/web/20241005224013/https://wiki.owasp.org/index.php/OWASP_Validation_Regex_Repository)\n\
  * [PCRE > Installing/Configuring - PHP Manual - May 3, 2008](https://web.archive.org/web/20260219065508/https://www.php.net/manual/en/pcre.configuration.php)\n\
  * [Regular expression Denial of Service - ReDoS - Adar Weidman - December 4, 2019](https://web.archive.org/web/20200309080846/https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)"
_relative_path: Regular Expression/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Regular Expression/README.md
````
