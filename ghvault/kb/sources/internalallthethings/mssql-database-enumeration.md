---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# MSSQL - Database Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-databases-mssql-enumeration` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-enumeration.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MSSQL - Database Enumeration](../../topics/databases/mssql-database-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-databases-mssql-enumeration |
| name | MSSQL - Database Enumeration |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/databases/mssql-enumeration.md |

## Preserved Source Material

````yaml
_body: "# MSSQL - Database Enumeration\n\n## Summary\n\n- [Tools](#tools)\n- [Identify Instances and Databases](#identify-instances-and-databases)\n\
  \    - [Discover Local SQL Server Instances](#discover-local-sql-server-instances)\n    - [Discover Domain SQL Server Instances](#discover-domain-sql-server-instances)\n\
  \    - [Discover Remote SQL Server Instances](#discover-remote-sql-server-instances)\n    - [Identify Encrypted databases](#identify-encrypted-databases)\n\
  \    - [Version Query](#version-query)\n- [Identify Users and Roles](#identify-users-and-roles)\n- [Identify Sensitive Information](#identify-sensitive-information)\n\
  \    - [Get Tables from a Specific Database](#get-tables-from-a-specific-database)\n    - [Gather 5 Entries from Each Column](#gather-5-entries-from-each-column)\n\
  \    - [Gather 5 Entries from a Specific Table](#gather-5-entries-from-a-specific-table)\n    - [Dump common information\
  \ from server to files](#dump-common-information-from-server-to-files)\n\n## Tools\n\n- [NetSPI/PowerUpSQL](https://github.com/NetSPI/PowerUpSQL)\
  \ - A PowerShell Toolkit for Attacking SQL Server\n- [skahwah/SQLRecon](https://github.com/skahwah/SQLRecon/) - A C# MS\
  \ SQL toolkit designed for offensive reconnaissance and post-exploitation.\n\n## Identify Instances and Databases\n\n###\
  \ Discover Local SQL Server Instances\n\n```ps1\nGet-SQLInstanceLocal\n```\n\n### Discover Domain SQL Server Instances\n\
  \n```ps1\nGet-SQLInstanceDomain -Verbose\n# Get Server Info for Found Instances\nGet-SQLInstanceDomain | Get-SQLServerInfo\
  \ -Verbose\n# Get Database Names\nGet-SQLInstanceDomain | Get-SQLDatabase -NoDefaults\n```\n\n### Discover Remote SQL Server\
  \ Instances\n\n```ps1\nGet-SQLInstanceBroadcast -Verbose\nGet-SQLInstanceScanUDPThreaded -Verbose -ComputerName SQLServer1\n\
  ```\n\n### Identify Encrypted databases\n\nNote: These are automatically decrypted for admins\n\n```ps1\nGet-SQLDatabase\
  \ -Username sa -Password Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\" -Verbose | Where-Object {$_.is_encrypted\
  \ -eq \"True\"}\n```\n\n### Version Query\n\n```ps1\nGet-SQLInstanceDomain | Get-Query \"select @@version\"\n```\n\n## Identify\
  \ Users and Roles\n\n- Query Current User & determine if the user is a sysadmin\n\n    ```sql\n    select suser_sname()\n\
  \    Select system_user\n    select is_srvrolemember('sysadmin')\n    ```\n\n- Current Role\n\n    ```sql\n    select user\n\
  \    ```\n\n- All Logins on Server\n\n    ```sql\n    Select * from sys.server_principals where type_desc != 'SERVER_ROLE'\n\
  \    ```\n\n- All Database Users for a Database\n\n    ```sql\n    Select * from sys.database_principals where type_desc\
  \ != 'database_role';\n    ```\n\n- List All Sysadmins\n\n    ```sql\n    SELECT name,type_desc,is_disabled FROM sys.server_principals\
  \ WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1\n    ```\n\n- List All Database Roles\n\n    ```sql\n    SELECT DB1.name\
  \ AS DatabaseRoleName,\n    isnull (DB2.name, 'No members') AS DatabaseUserName\n    FROM sys.database_role_members AS DRM\n\
  \    RIGHT OUTER JOIN sys.database_principals AS DB1\n    ON DRM.role_principal_id = DB1.principal_id\n    LEFT OUTER JOIN\
  \ sys.database_principals AS DB2\n    ON DRM.member_principal_id = DB2.principal_id\n    WHERE DB1.type = 'R'\n    ORDER\
  \ BY DB1.name;\n    ```\n\n## Identify Sensitive Information\n\n### Get Tables from a Specific Database\n\n```ps1\nGet-SQLInstanceDomain\
  \ | Get-SQLTable -DatabaseName <DBNameFromGet-SQLDatabaseCommand> -NoDefaults\nGet Column Details from a Table\nGet-SQLInstanceDomain\
  \ | Get-SQLColumn -DatabaseName <DBName> -TableName <TableName>\n```\n\n- Current database\n\n    ```sql\n    select db_name()\n\
  \    ```\n\n- List all tables\n\n    ```sql\n    select table_name from information_schema.tables\n    ```\n\n- List all\
  \ databases\n\n    ```sql\n    select name from master..sysdatabases\n    ```\n\n- List server informations\n\n    ```sql\n\
  \    SELECT * FROM sys.configurations\n    ```\n\n### Gather 5 Entries from Each Column\n\n```ps1\nGet-SQLInstanceDomain\
  \ | Get-SQLColumnSampleData -Keywords \"<columnname1,columnname2,columnname3,columnname4,columnname5>\" -Verbose -SampleSize\
  \ 5\n```\n\n### Gather 5 Entries from a Specific Table\n\n```ps1\nGet-SQLQuery -Instance \"<DBSERVERNAME\\DBInstance>\"\
  \ -Query 'select TOP 5 * from <DatabaseName>.dbo.<TableName>'\n```\n\n### Dump common information from server to files\n\
  \n```ps1\nInvoke-SQLDumpInfo -Verbose -Instance SQLSERVER1\\Instance1 -csv\n```\n\n## References\n\n- [PowerUpSQL Cheat\
  \ Sheet & SQL Server Queries - Leo Pitt](https://medium.com/@D00MFist/powerupsql-cheat-sheet-sql-server-queries-40e1c418edc3)\n\
  - [PowerUpSQL Cheat Sheet - Scott Sutherland](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet)"
_relative_path: databases/mssql-enumeration.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-enumeration.md
````
