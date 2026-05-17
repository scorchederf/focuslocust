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

## Summary

- Tools

## Preserved Body

````markdown
## Tools

- [NetSPI/PowerUpSQL](https://github.com/NetSPI/PowerUpSQL) - A PowerShell Toolkit for Attacking SQL Server
- [skahwah/SQLRecon](https://github.com/skahwah/SQLRecon/) - A C# MS SQL toolkit designed for offensive reconnaissance and post-exploitation.

## Identify Instances and Databases

### Discover Local SQL Server Instances

```ps1
Get-SQLInstanceLocal
```

### Discover Domain SQL Server Instances

```ps1
Get-SQLInstanceDomain -Verbose
# Get Server Info for Found Instances
Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
# Get Database Names
Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
```

### Discover Remote SQL Server Instances

```ps1
Get-SQLInstanceBroadcast -Verbose
Get-SQLInstanceScanUDPThreaded -Verbose -ComputerName SQLServer1
```

### Identify Encrypted databases

Note: These are automatically decrypted for admins

```ps1
Get-SQLDatabase -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Verbose | Where-Object {$_.is_encrypted -eq "True"}
```

### Version Query

```ps1
Get-SQLInstanceDomain | Get-Query "select @@version"
```

## Identify Users and Roles

- Query Current User & determine if the user is a sysadmin

    ```sql
    select suser_sname()
    Select system_user
    select is_srvrolemember('sysadmin')
    ```

- Current Role

    ```sql
    select user
    ```

- All Logins on Server

    ```sql
    Select * from sys.server_principals where type_desc != 'SERVER_ROLE'
    ```

- All Database Users for a Database

    ```sql
    Select * from sys.database_principals where type_desc != 'database_role';
    ```

- List All Sysadmins

    ```sql
    SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1
    ```

- List All Database Roles

    ```sql
    SELECT DB1.name AS DatabaseRoleName,
    isnull (DB2.name, 'No members') AS DatabaseUserName
    FROM sys.database_role_members AS DRM
    RIGHT OUTER JOIN sys.database_principals AS DB1
    ON DRM.role_principal_id = DB1.principal_id
    LEFT OUTER JOIN sys.database_principals AS DB2
    ON DRM.member_principal_id = DB2.principal_id
    WHERE DB1.type = 'R'
    ORDER BY DB1.name;
    ```

## Identify Sensitive Information

### Get Tables from a Specific Database

```ps1
Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DBNameFromGet-SQLDatabaseCommand> -NoDefaults
Get Column Details from a Table
Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName <DBName> -TableName <TableName>
```

- Current database

    ```sql
    select db_name()
    ```

- List all tables

    ```sql
    select table_name from information_schema.tables
    ```

- List all databases

    ```sql
    select name from master..sysdatabases
    ```

- List server informations

    ```sql
    SELECT * FROM sys.configurations
    ```

### Gather 5 Entries from Each Column

```ps1
Get-SQLInstanceDomain | Get-SQLColumnSampleData -Keywords "<columnname1,columnname2,columnname3,columnname4,columnname5>" -Verbose -SampleSize 5
```

### Gather 5 Entries from a Specific Table

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query 'select TOP 5 * from <DatabaseName>.dbo.<TableName>'
```

### Dump common information from server to files

```ps1
Invoke-SQLDumpInfo -Verbose -Instance SQLSERVER1\Instance1 -csv
```

## References

- [PowerUpSQL Cheat Sheet & SQL Server Queries - Leo Pitt](https://medium.com/@D00MFist/powerupsql-cheat-sheet-sql-server-queries-40e1c418edc3)
- [PowerUpSQL Cheat Sheet - Scott Sutherland](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet)
````

## Source Verification

[source record](../../sources/internalallthethings/mssql-database-enumeration.md)

## Evidence Excerpt

```text
_body: "# MSSQL - Database Enumeration\n\n## Summary\n\n- [Tools](#tools)\n- [Identify Instances and Databases](#identify-instances-and-databases)\n\
\    - [Discover Local SQL Server Instances](#discover-local-sql-server-instances)\n    - [Discover Domain SQL Server Instances](#discover-domain-sql-server-instances)\n\
\    - [Discover Remote SQL Server Instances](#discover-remote-sql-server-instances)\n    - [Identify Encrypted databases](#identify-encrypted-databases)\n\
\    - [Version Query](#version-query)\n- [Identify Users and Roles](#identify-users-and-roles)\n- [Identify Sensitive Information](#identify-sensitive-information)\n\
\    - [Get Tables from a Specific Database](#get-tables-from-a-specific-database)\n    - [Gather 5 Entries from Each Column](#gather-5-entries-from-each-column)\n\
\    - [Gather 5 Entries from a Specific Table](#gather-5-entries-from-a-specific-table)\n    - [Dump common information\
\ from server to files](#dump-common-information-from-server-to-files)\n\n## Tools\n\n- [NetSPI/PowerUpSQL](https://github.com/NetSPI/PowerUpSQL)\
\ - A PowerShell Toolkit for Attacking SQL Server\n- [skahwah/SQLRecon](https://github.com/skahwah/SQLRecon/) - A C# MS\
```
