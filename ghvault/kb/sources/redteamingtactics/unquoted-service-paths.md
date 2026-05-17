---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Unquoted Service Paths

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-unquoted-service-paths` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/unquoted-service-paths.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Unquoted Service Paths](../../topics/offensive-security/unquoted-service-paths.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-unquoted-service-paths |
| name | Unquoted Service Paths |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/unquoted-service-paths.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-05-20 221801.png
- Annotation 2019-05-20 222415.png
- vulnservice (1).gif
_body: '# Unquoted Service Paths


  Sometimes it is possible to escalate privileges by abusing misconfigured services. Specifically, this is possible if path
  to the service binary is not wrapped in quotes and there are spaces in the path.. This stems from the way Windows handles
  `CreateProcess` API calls:


  > If you are using a long file name that contains a space, use quoted strings to indicate where the file name ends and the
  arguments begin; otherwise, the file name is ambiguous. For example, consider the string "c:\program files\sub dir\program
  name". This string can be interpreted in a number of ways. The system tries to interpret the possibilities in the following
  order:

  >

  > **c:\program.exe** **c:\program files\sub.exe** **c:\program files\sub dir\program.exec:\program files\sub dir\program
  name.exe...**

  >

  > [https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa](https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa)


  ## Enumeration


  Let''s scan the system `ws01` for any potentially misconfigured services - those services that do not have their binary
  paths wrapped in quotes:


  {% code title="attacker@victim" %}

  ```

  cmd /c wmic service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i
  /v """

  ```

  {% endcode %}


  One service is returned:


  ![](<../../.gitbook/assets/Annotation 2019-05-20 221801.png>)


  The above suggests that if we can drop our binary to `c:\program.exe`, we may be able to stop/start the `VulnerableSvc`
  and get our binary at `c:\program.exe` to run with NT\System privileges:


  ![](<../../.gitbook/assets/Annotation 2019-05-20 222415.png>)


  ## Execution


  Let''s try exploiting the weakness in by droping a meterpreter binary to c:\program.exe and starting the vulnerable service
  `VulnerableSvc`. Doing so gives us a meterpreter session with `nt authority\system` privileges:


  ![](<../../.gitbook/assets/vulnservice (1).gif>)'
_relative_path: offensive-security/privilege-escalation/unquoted-service-paths.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/unquoted-service-paths.md
````
