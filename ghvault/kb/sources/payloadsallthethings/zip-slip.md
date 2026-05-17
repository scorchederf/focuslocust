---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Zip Slip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-zip-slip-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Zip Slip/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Zip Slip](../../topics/zip-slip/zip-slip.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-zip-slip-readme |
| name | Zip Slip |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Zip%20Slip/README.md |

## Preserved Source Material

````yaml
_body: "# Zip Slip\n\n> The vulnerability is exploited using a specially crafted archive that holds directory traversal filenames\
  \ (e.g. ../../shell.php). The Zip Slip vulnerability can affect numerous archive formats, including tar, jar, war, cpio,\
  \ apk, rar and 7z. The attacker can then overwrite executable files and either invoke them remotely or wait for the system\
  \ or user to call them, thus achieving remote command execution on the victim’s machine.\n\n## Summary\n\n* [Tools](#tools)\n\
  * [Methodology](#methodology)\n* [References](#references)\n\n## Tools\n\n* [ptoomey3/evilarc](https://github.com/ptoomey3/evilarc)\
  \ - Create tar/zip archives that can exploit directory traversal vulnerabilities\n* [usdAG/slipit](https://github.com/usdAG/slipit)\
  \ - Utility for creating ZipSlip archives\n\n## Methodology\n\nThe Zip Slip vulnerability is a critical security flaw that\
  \ affects the handling of archive files, such as ZIP, TAR, or other compressed file formats. This vulnerability allows an\
  \ attacker to write arbitrary files outside of the intended extraction directory, potentially overwriting critical system\
  \ files, executing malicious code, or gaining unauthorized access to sensitive information.\n\n**Example**: Suppose an attacker\
  \ creates a ZIP file with the following structure:\n\n```ps1\nmalicious.zip\n  ├── ../../../../etc/passwd\n  ├── ../../../../usr/local/bin/malicious_script.sh\n\
  ```\n\nWhen a vulnerable application extracts `malicious.zip`, the files are written to `/etc/passwd` and /`usr/local/bin/malicious_script.sh`\
  \ instead of being contained within the extraction directory. This can have severe consequences, such as corrupting system\
  \ files or executing malicious scripts.\n\n* Using [ptoomey3/evilarc](https://github.com/ptoomey3/evilarc):\n\n    ```python\n\
  \    python evilarc.py shell.php -o unix -f shell.zip -p var/www/html/ -d 15\n    ```\n\n* Creating a ZIP archive containing\
  \ a symbolic link:\n\n    ```ps1\n    ln -s ../../../index.php symindex.txt\n    zip --symlinks test.zip symindex.txt\n\
  \    ```\n\nFor a list of affected libraries and projects, visit [snyk/zip-slip-vulnerability](https://github.com/snyk/zip-slip-vulnerability)\n\
  \n## References\n\n* [Zip Slip - Snyk - June 5, 2018](https://web.archive.org/web/20260307012319/https://github.com/snyk/zip-slip-vulnerability)\n\
  * [Zip Slip Vulnerability - Snyk - April 15, 2018](https://web.archive.org/web/20180605125813/https://snyk.io/research/zip-slip-vulnerability)"
_relative_path: Zip Slip/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Zip Slip/README.md
````
