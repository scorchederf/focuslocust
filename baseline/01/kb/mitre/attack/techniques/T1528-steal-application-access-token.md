---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1528
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/identity_provider
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1528-steal-application-access-token
tactic:
    - Credential Access
platforms:
    - Containers
    - IaaS
    - Identity Provider
    - Office Suite
    - SaaS
permissions required:
    - none
---

## Description

Adversaries can steal application access tokens as a means of acquiring credentials to access remote systems and resources.<br><br>Application access tokens are used to make authorized API requests on behalf of a user or service and are commonly used as a way to access resources in cloud and container-based applications and software-as-a-service (SaaS).[^4]   Adversaries who steal account API tokens in cloud and containerized environments may be able to access data and perform actions with the permissions of these accounts, which can lead to privilege escalation and further compromise of the environment.<br><br>For example, in Kubernetes environments, processes running inside a container may communicate with the Kubernetes API server using service account tokens. If a container is compromised, an adversary may be able to steal the container’s token and thereby gain access to Kubernetes API commands.[^7]   <br><br>Similarly, instances within continuous-development / continuous-integration (CI/CD) pipelines will often use API tokens to authenticate to other services for testing and deployment.[^5]  If these pipelines are compromised, adversaries may be able to steal these tokens and leverage their privileges. <br><br>In Azure, an adversary who compromises a resource with an attached Managed Identity, such as an Azure VM, can request short-lived tokens through the Azure Instance Metadata Service (IMDS). These tokens can then facilitate unauthorized actions or further access to other Azure services, bypassing typical credential-based authentication.[^8] [^2] <br><br>Token theft can also occur through social engineering, in which case user action may be required to grant access. OAuth is one commonly implemented framework that issues tokens to users for access to systems. An application desiring access to cloud-based services or protected APIs can gain entry using OAuth 2.0 through a variety of authorization protocols. An example commonly-used sequence is Microsoft's Authorization Code Grant flow.[^12] [^11]  An OAuth access token enables a third-party application to interact with resources containing user data in the ways requested by the application without obtaining user credentials. <br> <br>Adversaries can leverage OAuth authorization by constructing a malicious application designed to be granted access to resources with the target user's OAuth token.[^1] [^6]  The adversary will need to complete registration of their application with the authorization server, for example Microsoft Identity Platform using Azure Portal, the Visual Studio IDE, the command-line interface, PowerShell, or REST API calls.[^10]  Then, they can send a [[kb/mitre/attack/techniques/T1566.002-spearphishing-link|Spearphishing Link]] to the target user to entice them to grant access to the application. Once the OAuth access token is granted, the application can gain potentially long-term access to features of the user account through [[kb/mitre/attack/techniques/T1550.001-application-access-token|Application Access Token]].[^9] <br><br>Application access tokens may function within a limited lifetime, limiting how long an adversary can utilize the stolen token. However, in some cases, adversaries can also steal application refresh tokens[^3] , allowing them to obtain new access tokens without prompting the user.  

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0677-aadinternals\|S0677]] | AADInternals | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can steal users’ access tokens via phishing emails containing malicious links.[^1]  |
| [[kb/mitre/attack/software/S0683-peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] gathers Kubernetes service account tokens using a variety of techniques.[^1]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has stolen access tokens and API tokens from with CI/CD pipeline solutions and repositories.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/software/S9009-trufflehog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has gathered access tokens and API tokens from CI/CD pipeline solutions and repositories.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Users need to be trained to not authorize third-party applications they don’t recognize. The user should pay particular attention to the redirect URL: if the URL is a misspelled or convoluted sequence of words related to an expected service or SaaS application, the website is likely trying to spoof a legitimate service. Users should also be cautious about the permissions they are granting to apps. For example, offline access and access to read emails should excite higher suspicions because adversaries can utilize SaaS APIs to discover credentials and other sensitive communications. |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Enforce role-based access control to limit accounts to the least privileges they require. A Cloud Access Security Broker (CASB) can be used to set usage policies and manage user permissions on cloud applications to prevent access to application access tokens. In Kubernetes applications, set “automountServiceAccountToken: false” in the YAML specification of pods that do not require access to service account tokens.[^1]  |
| [[kb/mitre/attack/mitigations/M1021-restrict-web-based-content\|M1021]] | Restrict Web-Based Content | Administrators can block end-user consent to OAuth applications, disabling users from authorizing third-party apps through OAuth 2.0 and forcing administrative consent for all requests. They can also block end-user registration of applications by their users, to reduce risk. A Cloud Access Security Broker can also be used to ban applications.<br><br>Azure offers a couple of enterprise policy settings in the Azure Management Portal that may help:<br><br>"Users -> User settings -> App registrations: Users can register applications" can be set to "no" to prevent users from registering new applications. <br>"Enterprise applications -> User settings -> Enterprise applications: Users can consent to apps accessing company data on their behalf" can be set to "no" to prevent users from consenting to allow third-party multi-tenant applications |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Administrators should audit all cloud and container accounts to ensure that they are necessary and that the permissions granted to them are appropriate.  Additionally, administrators should perform an audit of all OAuth applications and the permissions they have been granted to access organizational data. This should be done extensively on all applications in order to establish a baseline, followed up on with periodic audits of new or updated applications. Suspicious applications should be investigated and removed. |

 [^1]: [Amnesty OAuth Phishing Attacks, August 2019](https://www.amnesty.org/en/latest/research/2019/08/evolving-phishing-attacks-targeting-journalists-and-human-rights-defenders-from-the-middle-east-and-north-africa/)
 [^2]: [SpecterOps Managed Identity 2022](https://posts.specterops.io/managed-identity-attack-paths-part-1-automation-accounts-82667d17187a?gi=6a9daedade1c)
 [^3]: [Auth0 Understanding Refresh Tokens](https://auth0.com/learn/refresh-tokens)
 [^4]: [Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019](https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/)
 [^5]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)
 [^6]: [Trend Micro Pawn Storm OAuth 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/pawn-storm-abuses-open-authentication-advanced-social-engineering-attacks)
 [^7]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
 [^8]: [Entra Managed Identities 2025](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-use-vm-token)
 [^9]: [Microsoft - Azure AD Identity Tokens - Aug 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)
 [^10]: [Microsoft - Azure AD App Registration - May 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
 [^11]: [Microsoft - OAuth Code Authorization flow - June 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)
 [^12]: [Microsoft Identity Platform Protocols May 2019](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols)
 [^13]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^14]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
 [^15]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
 [^16]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)
 [^17]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
 [^18]: [Peirates GitHub](https://github.com/inguardians/peirates)
 [^19]: [AADInternals Documentation](https://o365blog.com/aadinternals)
 [^20]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)
