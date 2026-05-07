---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1538
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1538-cloud-service-dashboard
tactic:
    - Discovery
platforms:
    - IaaS
    - SaaS
    - Office Suite
    - Identity Provider
permissions required:
    - none
---

## Description

An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public IP addresses and open ports.[^2] <br><br>Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This also allows the adversary to gain information without manually making any API requests.

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Enforce the principle of least-privilege by limiting dashboard visibility to only the resources required. This may limit the discovery value of the dashboard in the event of a compromised account. |

 [^1]: [AWS Console Sign-in Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html)
 [^2]: [Google Command Center Dashboard](https://cloud.google.com/security-command-center/docs/quickstart-scc-dashboard)
