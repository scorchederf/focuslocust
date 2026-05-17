---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Cloning a Website

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-phishing-methodology-clone-a-website` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/clone-a-website.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloning a Website](../../topics/generic-methodologies-and-resources/cloning-a-website.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-phishing-methodology-clone-a-website |
| name | Cloning a Website |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/phishing-methodology/clone-a-website.md |

## Preserved Source Material

````yaml
_body: '# Cloning a Website


  {{#include ../../banners/hacktricks-training.md}}



  For a phishing assessment sometimes it might be useful to completely **clone/dump a website**.


  Note that you can add also some payloads to the cloned website like a BeEF hook to "control" the tab of the user.


  There are different tools you can use for this purpose:


  ## wget


  ```bash

  wget --mirror --page-requisites --convert-links --adjust-extension <URL>

  cd <URL>

  python3 -m http.server 8000

  ```


  ## goclone


  ```bash

  #https://github.com/imthaghost/goclone

  goclone <url>

  ```


  ## Social Engineering Toolit


  ```bash

  #https://github.com/trustedsec/social-engineer-toolkit

  ```



  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: generic-methodologies-and-resources/phishing-methodology/clone-a-website.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/clone-a-website.md
````
