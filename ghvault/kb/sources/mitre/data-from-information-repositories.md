---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data from Information Repositories

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

## Generated Concept Page

- [Data from Information Repositories](../../attack/techniques/T1213-data-from-information-repositories.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1213 |
| name | Data from Information Repositories |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1213 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may leverage information repositories to mine valuable information. Information repositories are\
  \ tools that allow for storage of information, typically to facilitate collaboration or information sharing between users,\
  \ and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral\
  \ Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing\
  \ features to share sensitive documents with recipients outside of the organization (i.e., [Transfer Data to Cloud Account](https://attack.mitre.org/techniques/T1537)).\
  \ \n\nThe following is a brief list of example information that may hold potential value to an adversary and may also be\
  \ found on an information repository:\n\n* Policies, procedures, and standards\n* Physical / logical network diagrams\n\
  * System architecture diagrams\n* Technical system documentation\n* Testing / development credentials (i.e., [Unsecured\
  \ Credentials](https://attack.mitre.org/techniques/T1552)) \n* Work / project schedules\n* Source code snippets\n* Links\
  \ to network shares and other internal resources\n* Contact or other sensitive information about business partners and customers,\
  \ including personally identifiable information (PII) \n\nInformation stored in a repository may vary based on the specific\
  \ instance or environment. Specific common information repositories include the following:\n\n* Storage services such as\
  \ IaaS databases, enterprise databases, and more specialized platforms such as customer relationship management (CRM) databases\
  \ \n* Collaboration platforms such as SharePoint, Confluence, and code repositories\n* Messaging platforms such as Slack\
  \ and Microsoft Teams \n\nIn some cases, information repositories have been improperly secured, typically by unintentionally\
  \ allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common\
  \ with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch.(Citation:\
  \ Mitiga)(Citation: TrendMicro Exposed Redis 2020)(Citation: Cybernews Reuters Leak 2022)"
external_references:
- external_id: T1213
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1213
- description: Ariel Szarf, Doron Karmi, and Lionel Saposnik. (n.d.). Oops, I Leaked It Again — How Mitiga Found PII in Exposed
    Amazon RDS Snapshots. Retrieved September 24, 2024.
  source_name: Mitiga
  url: https://www.mitiga.io/blog/how-mitiga-found-pii-in-exposed-amazon-rds-snapshots
- description: Atlassian. (2018, January 9). How to Enable User Access Logging. Retrieved April 4, 2018.
  source_name: Atlassian Confluence Logging
  url: https://confluence.atlassian.com/confkb/how-to-enable-user-access-logging-182943.html
- description: David Fiser and Jaromir Horejsi. (2020, April 21). Exposed Redis Instances Abused for Remote Code Execution,
    Cryptocurrency Mining. Retrieved September 25, 2024.
  source_name: TrendMicro Exposed Redis 2020
  url: https://www.trendmicro.com/en_us/research/20/d/exposed-redis-instances-abused-for-remote-code-execution-cryptocurrency-mining.html
- description: Microsoft. (2017, July 19). Configure audit settings for a site collection. Retrieved April 4, 2018.
  source_name: Microsoft SharePoint Logging
  url: https://support.office.com/en-us/article/configure-audit-settings-for-a-site-collection-a9920c97-38c0-44f2-8bcb-4cf1e2ae22d2
- description: Microsoft. (n.d.). Sharepoint Sharing Events. Retrieved October 8, 2021.
  source_name: Sharepoint Sharing Events
  url: https://docs.microsoft.com/en-us/microsoft-365/compliance/use-sharing-auditing?view=o365-worldwide#sharepoint-sharing-events
- description: Vilius Petkauskas . (2022, November 3). Thomson Reuters collected and leaked at least 3TB of sensitive data.
    Retrieved September 25, 2024.
  source_name: Cybernews Reuters Leak 2022
  url: https://cybernews.com/security/thomson-reuters-leaked-terabytes-sensitive-data/
id: attack-pattern--d28ef391-8ed4-45dc-bc4a-2f43abf54416
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:49:26.262Z'
name: Data from Information Repositories
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Regina Elwell
- Praetorian
- Milos Stojadinovic
- Isif Ibrahima, Mandiant
- Obsidian Security
- Naveen Vijayaraghavan
- Nilesh Dherange (Gurucul)
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Windows
- macOS
- SaaS
- IaaS
- Office Suite
x_mitre_version: '3.4'
```
