---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0083
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0083-cloud-service-enumeration
---

## Description

Cloud service enumeration involves listing or querying available cloud services in a cloud control plane. This activity is often performed to identify resources such as virtual machines, storage buckets, compute clusters, or other services within a cloud environment. Examples include API calls like `AWS ECS ListServices`, `Azure ListAllResources`, or `Google Cloud ListInstances`. Examples: <br><br>AWS Cloud Service Enumeration: The adversary gathers details about existing ECS services to identify opportunities for privilege escalation or exfiltration.<br>- Azure Resource Enumeration: The adversary collects information about virtual machines, resource groups, and other Azure assets for reconnaissance purposes.<br>- Google Cloud Resource Enumeration: The attacker seeks to map the environment and find misconfigured or underutilized resources for exploitation.<br>- Office 365 Service Enumeration: The attacker may look for data repositories or collaboration tools to exfiltrate sensitive information.
