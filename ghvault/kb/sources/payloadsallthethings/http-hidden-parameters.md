---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# HTTP Hidden Parameters

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-hidden-parameters-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Hidden Parameters/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [HTTP Hidden Parameters](../../topics/hidden-parameters/http-hidden-parameters.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-hidden-parameters-readme |
| name | HTTP Hidden Parameters |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Hidden%20Parameters/README.md |

## Preserved Source Material

````yaml
_body: "# HTTP Hidden Parameters\n\n> Web applications often have hidden or undocumented parameters that are not exposed in\
  \ the user interface. Fuzzing can help discover these parameters, which might be vulnerable to various attacks.\n\n## Summary\n\
  \n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Bruteforce Parameters](#bruteforce-parameters)\n    * [Old Parameters](#old-parameters)\n\
  * [References](#references)\n\n## Tools\n\n* [PortSwigger/param-miner](https://github.com/PortSwigger/param-miner) - Burp\
  \ extension to identify hidden, unlinked parameters.\n* [s0md3v/Arjun](https://github.com/s0md3v/Arjun) - HTTP parameter\
  \ discovery suite\n* [Sh1Yo/x8](https://github.com/Sh1Yo/x8) - Hidden parameters discovery suite\n* [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls)\
  \ - Fetch all the URLs that the Wayback Machine knows about for a domain\n* [devanshbatham/ParamSpider](https://github.com/devanshbatham/ParamSpider)\
  \ - Mining URLs from dark corners of Web Archives for bug hunting/fuzzing/further probing\n\n## Methodology\n\n### Bruteforce\
  \ Parameters\n\n* Use wordlists of common parameters and send them, look for unexpected behavior from the backend.\n\n \
  \   ```ps1\n    x8 -u \"https://example.com/\" -w <wordlist>\n    x8 -u \"https://example.com/\" -X POST -w <wordlist>\n\
  \    ```\n\nWordlist examples:\n\n* [Arjun/large.txt](https://github.com/s0md3v/Arjun/blob/master/arjun/db/large.txt)\n\
  * [Arjun/medium.txt](https://github.com/s0md3v/Arjun/blob/master/arjun/db/medium.txt)\n* [Arjun/small.txt](https://github.com/s0md3v/Arjun/blob/master/arjun/db/small.txt)\n\
  * [samlists/sam-cc-parameters-lowercase-all.txt](https://github.com/the-xentropy/samlists/blob/main/sam-cc-parameters-lowercase-all.txt)\n\
  * [samlists/sam-cc-parameters-mixedcase-all.txt](https://github.com/the-xentropy/samlists/blob/main/sam-cc-parameters-mixedcase-all.txt)\n\
  \n### Old Parameters\n\nExplore all the URL from your targets to find old parameters.\n\n* Browse the [Wayback Machine](http://web.archive.org/)\n\
  * Look through the JS files to discover unused parameters\n\n## References\n\n* [Hacker tools: Arjun – The parameter discovery\
  \ tool - Intigriti - May 17, 2021](https://web.archive.org/web/20230930093635/https://blog.intigriti.com/2021/05/17/hacker-tools-arjun-the-parameter-discovery-tool/)\n\
  * [Parameter Discovery: A quick guide to start - YesWeHack - April 20, 2022](http://web.archive.org/web/20220420123306/https://blog.yeswehack.com/yeswerhackers/parameter-discovery-quick-guide-to-start)"
_relative_path: Hidden Parameters/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Hidden Parameters/README.md
````
