---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1213 - Data from Information Repositories

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1213` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing features to share sensitive documents with recipients outside of the organization (i.e., Transfer Data to Cloud Account). 

The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository:

* Policies, procedures, and standards
* Physical / logical network diagrams
* System architecture diagrams
* Technical system documentation
* Testing / development credentials (i.e., Unsecured Credentials) 
* Work / project schedules
* Source code snippets
* Links to network shares and other internal resources
* Contact or other sensitive information about business partners and customers, including personally identifiable information (PII) 

Information stored in a repository may vary based on the specific instance or environment. Specific common information repositories include the following:

* Storage services such as IaaS databases, enterprise databases, and more specialized platforms such as customer relationship management (CRM) databases 
* Collaboration platforms such as SharePoint, Confluence, and code repositories
* Messaging platforms such as Slack and Microsoft Teams 

In some cases, information repositories have been improperly secured, typically by unintentionally allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch.

## Source Verification

[source record](../../sources/mitre/data-from-information-repositories.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may leverage information repositories to mine valuable information. Information repositories are\
\ tools that allow for storage of information, typically to facilitate collaboration or information sharing between users,\
\ and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral\
\ Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing\
\ features to share sensitive documents with recipients outside of the organization (i.e., [Transfer Data to Cloud Account](https://attack.mitre.org/techniques/T1537)).\
\ \n\nThe following is a brief list of example information that may hold potential value to an adversary and may also be\
```
