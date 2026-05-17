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

## Summary

GTFOBins entry for kubectl covering shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/kubectl.md)
- Source verification: [source record](../../sources/gtfobins/kubectl.md)

## Aliases

- `kubectl`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: cat >/path/to/temp-file <<EOF clusters: - cluster: server: https://x name: x contexts: - context: cluster: x user: x name: x current-context: x users: - name: x user: exec: apiV... |

## Source Verification

[source record](../../sources/gtfobins/kubectl.md)

## Evidence Excerpt

```text
_body: ''
_name: kubectl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/kubectl
functions:
shell:
- code: "cat >/path/to/temp-file <<EOF\nclusters:\n- cluster:\n    server: https://x\n  name: x\ncontexts:\n- context:\n\
\    cluster: x\n    user: x\n  name: x\ncurrent-context: x\nusers:\n- name: x\n  user:\n    exec:\n      apiVersion:\
\ client.authentication.k8s.io/v1\n      interactiveMode: Always\n      command: /bin/sh\n      args:\n        - '-c'\n\
```
