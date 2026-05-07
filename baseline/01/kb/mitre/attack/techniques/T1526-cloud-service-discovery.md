---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1526
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1526-cloud-service-discovery
tactic:
    - Discovery
platforms:
    - IaaS
    - Identity Provider
    - Office Suite
    - SaaS
permissions required:
    - none
---

## Description

An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD), Lambda Functions, Entra ID, etc. They may also include security services, such as AWS GuardDuty and Microsoft Defender for Cloud, and logging services, such as AWS CloudTrail and Google Cloud Audit Logs.<br><br>Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs, such as the Microsoft Graph API and Azure Resource Manager API, can enumerate resources and services, including applications, management groups, resources and policy definitions, and their relationships that are accessible by an identity.[^2] [^1] <br><br>For example, Stormspotter is an open source tool for enumerating and constructing a graph for Azure resources and services, and Pacu is an open source AWS exploitation framework that supports several methods for discovering cloud services.[^3] [^4] <br><br>Adversaries may use the information gained to shape follow-on behaviors, such as targeting data or credentials from enumerated services or evading identified defenses through [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools|Disable or Modify Tools]] or [[kb/mitre/attack/techniques/T1685.002-disable-or-modify-cloud-log|Disable or Modify Cloud Log]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0677-aadinternals\|S0677]] | AADInternals | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations.[^1]  |
| [[kb/mitre/attack/software/S0684-roadtools\|S0684]] | ROADTools | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] can enumerate Azure AD applications and service principals.[^1] 	 |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate AWS services, such as CloudTrail and CloudWatch.[^1]  |
| [[kb/mitre/attack/software/S9009-trufflehog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has the ability to scan code repositories and CI/CD platforms.[^1] [^2]  |

 [^1]: [Azure AD Graph API](https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/howto/azure-ad-graph-api-operations-overview)
 [^2]: [Azure - Resource Manager API](https://docs.microsoft.com/en-us/rest/api/resources/)
 [^3]: [Azure - Stormspotter](https://github.com/Azure/Stormspotter)
 [^4]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^5]: [AADInternals Documentation](https://o365blog.com/aadinternals)
 [^6]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
 [^7]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
 [^8]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)
