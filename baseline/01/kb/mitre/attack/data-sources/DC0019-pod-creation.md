---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0019
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0019-pod-creation
---

## Description

The initial deployment or instantiation of a new pod in a containerized environment. This includes creating a pod manually, through orchestration tools (Kubernetes), or via Infrastructure-as-Code (IaC) configurations. A Pod is the smallest deployable unit in Kubernetes, typically containing one or more containers. Creation methods include:<br>- Direct pod deployment (`kubectl run`, `kubectl apply`)<br>- Automated deployment via CI/CD pipelines (e.g., ArgoCD, Jenkins, GitOps)<br>- Infrastructure-as-Code (IaC) templates (e.g., Terraform, Helm Charts)<br>- API-based deployments via Kubernetes control plane (create_pod API calls)<br>- Pods can be ephemeral (short-lived) or persistent (part of a StatefulSet or Deployment).<br><br>*Data Collection Measures:*<br><br>- Kubernetes Audit Logs<br>    - Captures all API requests, including pod `create` events.<br>- Kube-api server Logs	<br>    - Monitors API calls related to pod deployments and modifications. Related Events: `PodSandboxChanged`, `SyncLoop`, `Created pod`<br>- Container Runtime Logs	<br>    - Logs from CRI-O, containerd, or Docker capture pod creation events. Related Events: `container start`, `container create`<br>- Cloud Provider Logs	<br>    - GKE, EKS, AKS logs provide insights into Kubernetes API interactions.<br>- SIEM & Log Aggregation	<br>    - Integrates Kubernetes logs into SIEM solutions.<br>- EDR/XDR Solutions	<br>    - Monitors container-based activity for anomalous pod creations.
