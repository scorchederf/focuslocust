---
parsed_by: focuslocust
source: mitre
type: generated
---
# Application Access Token

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1550.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Application Access Token](../../attack/techniques/T1550.001-application-access-token.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1550.001 |
| name | Application Access Token |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1550/001 |

## Preserved Source Material

```yaml
created: '2020-01-30T17:37:22.261Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use stolen application access tokens to bypass the typical authentication process and access\
  \ restricted accounts, information, or services on remote systems. These tokens are typically stolen from users or services\
  \ and used in lieu of login credentials.\n\nApplication access tokens are used to make authorized API requests on behalf\
  \ of a user or service and are commonly used to access resources in cloud, container-based applications, and software-as-a-service\
  \ (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019) \n\nOAuth is one commonly\
  \ implemented framework that issues tokens to users for access to systems. These frameworks are used collaboratively to\
  \ verify the user and determine what actions the user is allowed to perform. Once identity is established, the token allows\
  \ actions to be authorized, without passing the actual credentials of the user. Therefore, compromise of the token can grant\
  \ the adversary access to resources of other sites through a malicious application.(Citation: okta)\n\nFor example, with\
  \ a cloud-based email service, once an OAuth access token is granted to a malicious application, it can potentially gain\
  \ long-term access to features of the user account if a \"refresh\" token enabling background access is awarded.(Citation:\
  \ Microsoft Identity Platform Access 2019) With an OAuth access token an adversary can use the user-granted REST API to\
  \ perform functions such as email searching and contact enumeration.(Citation: Staaldraad Phishing with OAuth 2017)\n\n\
  Compromised access tokens may be used as an initial step in compromising other services. For example, if a token grants\
  \ access to a victim’s primary email, the adversary may be able to extend access to all other services which the target\
  \ subscribes by triggering forgotten password routines. In AWS and GCP environments, adversaries can trigger a request for\
  \ a short-lived access token with the privileges of another user account.(Citation: Google Cloud Service Account Credentials)(Citation:\
  \ AWS Temporary Security Credentials) The adversary can then use this token to request data or perform actions the original\
  \ account could not. If permissions for this feature are misconfigured – for example, by allowing all users to request a\
  \ token for a particular account - an adversary may be able to gain initial access to a Cloud Account or escalate their\
  \ privileges.(Citation: Rhino Security Labs Enumerating AWS Roles)\n\nDirect API access through a token negates the effectiveness\
  \ of a second authentication factor and may be immune to intuitive countermeasures like changing passwords.  For example,\
  \ in AWS environments, an adversary who compromises a user’s AWS API credentials may be able to use the `sts:GetFederationToken`\
  \ API call to create a federated user session, which will have the same permissions as the original user but may persist\
  \ even if the original user credentials are deactivated.(Citation: Crowdstrike AWS User Federation Persistence) Additionally,\
  \ access abuse over an API channel can be difficult to detect even from the service provider end, as the access can still\
  \ align well with a legitimate workflow."
external_references:
- external_id: T1550.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1550/001
- description: ' Vaishnav Murthy and Joel Eng. (2023, January 30). How Adversaries Can Persist with AWS User Federation. Retrieved
    March 10, 2023.'
  source_name: Crowdstrike AWS User Federation Persistence
  url: https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/
- description: Auth0. (n.d.). Why You Should Always Use Access Tokens to Secure APIs. Retrieved September 12, 2019.
  source_name: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019
  url: https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/
- description: AWS. (n.d.). Requesting temporary security credentials. Retrieved April 1, 2022.
  source_name: AWS Temporary Security Credentials
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html
- description: Cai, S., Flores, J., de Guzman, C., et. al.. (2019, August 27). Microsoft identity platform access tokens.
    Retrieved October 4, 2019.
  source_name: Microsoft Identity Platform Access 2019
  url: https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens
- description: Google Cloud. (2022, March 31). Creating short-lived service account credentials. Retrieved April 1, 2022.
  source_name: Google Cloud Service Account Credentials
  url: https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials
- description: okta. (n.d.). What Happens If Your JWT Is Stolen?. Retrieved September 12, 2019.
  source_name: okta
  url: https://developer.okta.com/blog/2018/06/20/what-happens-if-your-jwt-is-stolen
- description: 'Spencer Gietzen. (2018, August 8). Assume the Worst: Enumerating AWS Roles through ‘AssumeRole’. Retrieved
    April 1, 2022.'
  source_name: Rhino Security Labs Enumerating AWS Roles
  url: https://rhinosecuritylabs.com/aws/assume-worst-aws-assume-role-enumeration
- description: Stalmans, E.. (2017, August 2). Phishing with OAuth and o365/Azure. Retrieved October 4, 2019.
  source_name: Staaldraad Phishing with OAuth 2017
  url: https://staaldraad.github.io/2017/08/02/o356-phishing-with-oauth/
id: attack-pattern--f005e783-57d4-4837-88ad-dbe7faee1c51
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2026-04-15T22:48:23.373Z'
name: Application Access Token
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Blake Strom, Microsoft Threat Intelligence
- Dylan Silva, AWS Security
- Ian Davila, Tidal Cyber
- Jack Burns, HubSpot
- Jeff Sakowicz, Microsoft Identity Developer Platform Services (IDPM Services)
- Mark Wee
- Pawel Partyka, Microsoft Threat Intelligence
- Saisha Agrawal, Microsoft Threat Intelligent Center (MSTIC)
- Shailesh Tiwary (Indian Army)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- IaaS
- Identity Provider
- Office Suite
- SaaS
x_mitre_version: '2.0'
```
