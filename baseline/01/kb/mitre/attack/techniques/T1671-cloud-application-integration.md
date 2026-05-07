---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1671
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1671-cloud-application-integration
tactic:
    - Persistence
platforms:
    - Office Suite
    - SaaS
permissions required:
    - none
---

## Description

Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service environment. Adversaries may create a custom application, add a legitimate application into the environment, or even co-opt an existing integration to achieve malicious ends.[^2] [^6] <br><br>OAuth is an open standard that allows users to authorize applications to access their information on their behalf. In a SaaS environment such as Microsoft 365 or Google Workspace, users may integrate applications to improve their workflow and achieve tasks.  <br><br>Leveraging application integrations may allow adversaries to persist in an environment – for example, by granting consent to an application from a high-privileged adversary-controlled account in order to maintain access to its data, even in the event of losing access to the account.[^1] [^4] [^7]  In some cases, integrations may remain valid even after the original consenting user account is disabled.[^3]  Application integrations may also allow adversaries to bypass multi-factor authentication requirements through the use of [[kb/mitre/attack/techniques/T1550.001-application-access-token|Application Access Token]]s. Finally, they may enable persistent [[kb/mitre/attack/techniques/T1020-automated-exfiltration|Automated Exfiltration]] over time.[^8] <br><br>Creating or adding a new application may require the adversary to create a dedicated [[kb/mitre/attack/techniques/T1136.003-cloud-account|Cloud Account]] for the application and assign it [[kb/mitre/attack/techniques/T1098.003-additional-cloud-roles|Additional Cloud Roles]] – for example, in Microsoft 365 environments, an application can only access resources via an associated service principal.[^5]   

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Do not allow users to add new application integrations into a SaaS environment. In Entra ID environments, consider enforcing the “Do not allow user consent” option.[^1]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Periodically review SaaS integrations for unapproved or potentially malicious applications.   |

 [^1]: [Wiz Midnight Blizzard 2024](https://www.wiz.io/blog/midnight-blizzard-microsoft-breach-analysis-and-best-practices)
 [^2]: [Push Security SaaS Persistence 2022](https://pushsecurity.com/blog/maintaining-persistent-access-in-a-saas-first-world/)
 [^3]: [Push Security Slack Persistence 2023](https://pushsecurity.com/blog/phishing-slack-persistence/)
 [^4]: [Microsoft Malicious OAuth Applications 2022](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-OAuth-applications-used-to-compromise-email-servers-and-spread-spam/)
 [^5]: [Microsoft Entra ID Service Principals](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser)
 [^6]: [SaaS Attacks GitHub Evil Twin Integrations](https://github.com/pushsecurity/saas-attacks/blob/main/techniques/evil_twin_integrations/description.md)
 [^7]: [Huntress Persistence Microsoft 365 Compromise 2024](https://www.huntress.com/blog/legitimate-apps-as-traitorware-for-persistent-microsoft-365-compromise)
 [^8]: [Synes Cyber Corner Malicious Azure Application 2023](https://cybercorner.tech/malicious-azure-application-perfectdata-software-and-office365-business-email-compromise/)
 [^9]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)
