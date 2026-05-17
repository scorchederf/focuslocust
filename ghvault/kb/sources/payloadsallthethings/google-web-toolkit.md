---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Google Web Toolkit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-google-web-toolkit-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Google Web Toolkit/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Google Web Toolkit](../../topics/google-web-toolkit/google-web-toolkit.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-google-web-toolkit-readme |
| name | Google Web Toolkit |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Google%20Web%20Toolkit/README.md |

## Preserved Source Material

````yaml
_body: "# Google Web Toolkit\n\n> Google Web Toolkit (GWT), also known as GWT Web Toolkit, is an open-source set of tools\
  \ that allows web developers to create and maintain JavaScript front-end applications using Java. It was originally developed\
  \ by Google and had its initial release on May 16, 2006.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n\
  * [References](#references)\n\n## Tools\n\n* [FSecureLABS/GWTMap](https://github.com/FSecureLABS/GWTMap) - GWTMap is a tool\
  \ to help map the attack surface of Google Web Toolkit (GWT) based applications.\n* [GDSSecurity/GWT-Penetration-Testing-Toolset](https://github.com/GDSSecurity/GWT-Penetration-Testing-Toolset)\
  \ - A set of tools made to assist in penetration testing GWT applications.\n\n## Methodology\n\n* Enumerate the methods\
  \ of a remote application via it's bootstrap file and create a local backup of the code (selects permutation at random):\n\
  \n    ```ps1\n    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --backup\n    ```\n\n* Enumerate the methods\
  \ of a remote application via a specific code permutation\n\n    ```ps1\n    ./gwtmap.py -u http://10.10.10.10/olympian/C39AB19B83398A76A21E0CD04EC9B14C.cache.js\n\
  \    ```\n\n* Enumerate the methods whilst routing traffic through an HTTP proxy:\n\n    ```ps1\n    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js\
  \ --backup -p http://127.0.0.1:8080\n    ```\n\n* Enumerate the methods of a local copy (a file) of any given permutation:\n\
  \n    ```ps1\n    ./gwtmap.py -F test_data/olympian/C39AB19B83398A76A21E0CD04EC9B14C.cache.js\n    ```\n\n* Filter output\
  \ to a specific service or method:\n\n    ```ps1\n    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter\
  \ AuthenticationService.login\n    ```\n\n* Generate RPC payloads for all methods of the filtered service, with coloured\
  \ output\n\n    ```ps1\n    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter AuthenticationService\
  \ --rpc --color\n    ```\n\n* Automatically test (probe) the generate RPC request for the filtered service method\n\n  \
  \  ```ps1\n    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter AuthenticationService.login --rpc\
  \ --probe\n    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter TestService.testDetails --rpc --probe\n\
  \    ```\n\n## References\n\n* [From Serialized to Shell :: Exploiting Google Web Toolkit with EL Injection - Stevent Seeley\
  \ - May 22, 2017](https://web.archive.org/web/20260220100658/https://srcincite.io/blog/2017/05/22/from-serialized-to-shell-auditing-google-web-toolkit-with-el-injection.html)\n\
  * [Hacking a Google Web Toolkit application - thehackerish - April 22, 2021](https://web.archive.org/web/20210227222455/https://thehackerish.com/hacking-a-google-web-toolkit-application/)"
_relative_path: Google Web Toolkit/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Google Web Toolkit/README.md
````
