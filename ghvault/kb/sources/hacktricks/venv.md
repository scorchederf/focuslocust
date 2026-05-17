---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# venv

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-python-venv` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/python/venv.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [venv](../../topics/generic-methodologies-and-resources/venv.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-python-venv |
| name | venv |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/python/venv.md |

## Preserved Source Material

````yaml
_body: '# venv


  {{#include ../../banners/hacktricks-training.md}}



  ```bash

  sudo apt-get install python3-venv

  #Now, go to the folder you want to create the virtual environment

  python3 -m venv <Dirname>

  python3 -m venv pvenv #In this case the folder "pvenv" is going to be created

  source <Dirname>/bin/activate

  source pvenv/bin/activate #Activate the environment

  #You can now install whatever python library you need

  deactivate #To deactivate the virtual environment

  ```


  ```bash

  The error

  error: invalid command ''bdist_wheel''

  is fixed running

  pip3 install wheel

  inside the virtual environment

  ```


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: generic-methodologies-and-resources/python/venv.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/python/venv.md
````
