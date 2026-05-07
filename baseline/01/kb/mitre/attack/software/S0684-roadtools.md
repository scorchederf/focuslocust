---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0684
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0684-roadtools
---

## Description

[[kb/mitre/attack/software/S0684-roadtools|ROADTools]] is a framework for enumerating Azure Active Directory environments. The tool is written in Python and publicly available on GitHub.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1018-remote-system-discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] can enumerate Azure AD systems and devices.[^1]  |
| [[kb/mitre/attack/techniques/T1069.003-cloud-groups\|T1069.003]] | Cloud Groups | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] can enumerate Azure AD groups.[^1] 	 |
| [[kb/mitre/attack/techniques/T1078.004-cloud-accounts\|T1078.004]] | Cloud Accounts | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] leverages valid cloud credentials to perform enumeration operations using the internal Azure AD Graph API.[^1] 	 |
| [[kb/mitre/attack/techniques/T1087.004-cloud-account\|T1087.004]] | Cloud Account | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] can enumerate Azure AD users.[^1]  |
| [[kb/mitre/attack/techniques/T1119-automated-collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] automatically gathers data from Azure AD environments using the Azure Graph API.[^1]  |
| [[kb/mitre/attack/techniques/T1526-cloud-service-discovery\|T1526]] | Cloud Service Discovery | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] can enumerate Azure AD applications and service principals.[^1] 	 |

 [^1]: [ROADtools Github](https://github.com/dirkjanm/ROADtools)
 [^2]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
