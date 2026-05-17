---
parsed_by: focuslocust
source: mitre
type: generated
---
# Serverless Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1648` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Serverless Execution](../../attack/techniques/T1648-serverless-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1648 |
| name | Serverless Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1648 |

## Preserved Source Material

```yaml
created: '2022-05-27T13:19:51.112Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse serverless computing, integration, and automation services to execute arbitrary code in\
  \ cloud environments. Many cloud providers offer a variety of serverless resources, including compute engines, application\
  \ integration services, and web servers. \n\nAdversaries may abuse these resources in various ways as a means of executing\
  \ arbitrary commands. For example, adversaries may use serverless functions to execute malicious code, such as crypto-mining\
  \ malware (i.e. [Resource Hijacking](https://attack.mitre.org/techniques/T1496)).(Citation: Cado Security Denonia) Adversaries\
  \ may also create functions that enable further compromise of the cloud environment. For example, an adversary may use the\
  \ `IAM:PassRole` permission in AWS or the `iam.serviceAccounts.actAs` permission in Google Cloud to add [Additional Cloud\
  \ Roles](https://attack.mitre.org/techniques/T1098/003) to a serverless cloud function, which may then be able to perform\
  \ actions the original user cannot.(Citation: Rhino Security Labs AWS Privilege Escalation)(Citation: Rhingo Security Labs\
  \ GCP Privilege Escalation)\n\nServerless functions can also be invoked in response to cloud events (i.e. [Event Triggered\
  \ Execution](https://attack.mitre.org/techniques/T1546)), potentially enabling persistent execution over time. For example,\
  \ in AWS environments, an adversary may create a Lambda function that automatically adds [Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001)\
  \ to a user and a corresponding CloudWatch events rule that invokes that function whenever a new user is created.(Citation:\
  \ Backdooring an AWS account) This is also possible in many cloud-based office application suites. For example, in Microsoft\
  \ 365 environments, an adversary may create a Power Automate workflow that forwards all emails a user receives or creates\
  \ anonymous sharing links whenever a user is granted access to a document in SharePoint.(Citation: Varonis Power Automate\
  \ Data Exfiltration)(Citation: Microsoft DART Case Report 001) In Google Workspace environments, they may instead create\
  \ an Apps Script that exfiltrates a user's data when they open a file.(Citation: Cloud Hack Tricks GWS Apps Script)(Citation:\
  \ OWN-CERT Google App Script 2024)"
external_references:
- external_id: T1648
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1648
- description: Berk Veral. (2020, March 9). Real-life cybercrime stories from DART, the Microsoft Detection and Response Team.
    Retrieved May 27, 2022.
  source_name: Microsoft DART Case Report 001
  url: https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team
- description: Daniel Grzelak. (2016, July 9). Backdooring an AWS account. Retrieved May 27, 2022.
  source_name: Backdooring an AWS account
  url: https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9
- description: Eric Saraga. (2022, February 2). Using Power Automate for Covert Data Exfiltration in Microsoft 365. Retrieved
    May 27, 2022.
  source_name: Varonis Power Automate Data Exfiltration
  url: https://www.varonis.com/blog/power-automate-data-exfiltration
- description: HackTricks Cloud. (n.d.). GWS - App Scripts. Retrieved July 1, 2024.
  source_name: Cloud Hack Tricks GWS Apps Script
  url: https://cloud.hacktricks.xyz/pentesting-cloud/workspace-security/gws-google-platforms-phishing/gws-app-scripts
- description: L'Hutereau Arnaud. (n.d.). Google Workspace Malicious App Script analysis. Retrieved October 2, 2024.
  source_name: OWN-CERT Google App Script 2024
  url: https://www.own.security/ressources/blog/google-workspace-malicious-app-script-analysis
- description: 'Matt Muir. (2022, April 6). Cado Discovers Denonia: The First Malware Specifically Targeting Lambda. Retrieved
    May 27, 2022.'
  source_name: Cado Security Denonia
  url: https://www.cadosecurity.com/cado-discovers-denonia-the-first-malware-specifically-targeting-lambda/
- description: Rhino Security Labs. (n.d.). AWS IAM Privilege Escalation – Methods and Mitigation. Retrieved May 27, 2022.
  source_name: Rhino Security Labs AWS Privilege Escalation
  url: https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/
- description: Spencer Gietzen. (n.d.). Privilege Escalation in Google Cloud Platform – Part 1 (IAM). Retrieved May 27, 2022.
  source_name: Rhingo Security Labs GCP Privilege Escalation
  url: https://rhinosecuritylabs.com/gcp/privilege-escalation-google-cloud-platform-part-1/
id: attack-pattern--e848506b-8484-4410-8017-3d235a52f5b3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-04-15T19:59:17.861Z'
name: Serverless Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Shailesh Tiwary (Indian Army)
- Praetorian
- Oleg Kolesnikov, Securonix
- Cisco
- Varonis Threat Labs
- Alex Soler, AttackIQ
- Vectra AI
- OWN
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- SaaS
- IaaS
- Office Suite
x_mitre_version: '1.2'
```
