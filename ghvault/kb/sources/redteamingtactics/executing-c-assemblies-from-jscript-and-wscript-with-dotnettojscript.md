---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Executing C# Assemblies from Jscript and wscript with DotNetToJscript

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-executing-csharp-assemblies-from-jscript-and-wscript-with-dotnettojscript` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/executing-csharp-assemblies-from-jscript-and-wscript-with-dotnettojscript.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Executing C# Assemblies from Jscript and wscript with DotNetToJscript](../../topics/offensive-security/executing-c-assemblies-from-jscript-and-wscript-with-dotnettojscript.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-executing-csharp-assemblies-from-jscript-and-wscript-with-dotnettojscript |
| name | Executing C# Assemblies from Jscript and wscript with DotNetToJscript |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/executing-csharp-assemblies-from-jscript-and-wscript-with-dotnettojscript.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-05-19 135204.png
- Annotation 2019-05-19 135844.png
- Annotation 2019-05-19 140645.png
- Annotation 2019-05-19 141447.png
- Annotation 2019-05-19 142153.png
- Annotation 2019-05-19 145407.png
_body: "# Executing C# Assemblies from Jscript and wscript with DotNetToJscript\n\nIt's possible to load in to memory and\
  \ execute C# compiled binaries from within javascript and vbscript by using a technique called [DotNetToJscript](https://github.com/tyranid/DotNetToJScript)\
  \ by James Forshaw.\n\nSince [SharpShooter](https://github.com/mdsecactivebreach/SharpShooter), [CactusTorch](https://github.com/mdsecactivebreach/CACTUSTORCH)\
  \ and a couple of other offensive security tools are leveraging DotNetToJscript to execute the payloads in memory using\
  \ C#, in this quick lab I wanted to simply use the DotNetToJscipt framework just to get a feel of the process and see if\
  \ there are any easy to spot artefacts this technique leaves behind on the target system that could help defenders catch\
  \ the attackers.\n\n## Compilation\n\n1. Download [DotNetToJscript](https://github.com/tyranid/DotNetToJScript)\n2. Compile\
  \ it (review the code before you do). It will spit out two binaries:\n   1. DotNetToJscript.exe - responsible for bootrstrapping\
  \ C# binaries (supplied as input) and converting them to JavaScript or VBScript\n   2. ExampleAssembly.dll - the C# assembly\
  \ that will be given to DotNetToJscript.exe. In default project configuration, the assembly just pops a message box with\
  \ the text \"test\"\n3. Execute DotNetToJscript.exe and supply it with the ExampleAssembly.dll, specify the output file\
  \ and the output type:\n\n```csharp\n\\\\VBOXSVR\\Experiments\\DotNetToJScript\\DotNetToJScript\\bin\\Debug\\DotNetToJScript.exe\
  \ \\\\VBOXSVR\\Experiments\\DotNetToJScript\\ExampleAssembly\\bin\\Debug\\ExampleAssembly.dll -l vbscript -o \\\\VBOXSVR\\\
  Experiments\\DotNetToJScript\\DotNetToJScript\\test.vbs\n```\n\n![](<../../.gitbook/assets/Annotation 2019-05-19 135204.png>)\n\
  \nWe got a test.vbs created and if we look inside it, we can see that at a high level:\n\n* the C# binary is now present\
  \ as a base64 encoded data blob&#x20;\n* the data blobob will be deserialized and invoked using `DynamicInvoke`&#x20;\n\
  * which will create a new instance of the `TestClass`&#x20;\n* which will kick off the `MessageBox` as defined in the `TestClass`\
  \ constructor\n\n![](<../../.gitbook/assets/Annotation 2019-05-19 140645.png>)\n\n```javascript\nentry_class = \"TestClass\"\
  \n\nDim fmt, al, d, o\nSet fmt = CreateObject(\"System.Runtime.Serialization.Formatters.Binary.BinaryFormatter\")\nSet al\
  \ = CreateObject(\"System.Collections.ArrayList\")\nal.Add Empty\n\nSet d = fmt.Deserialize_2(Base64ToStream(s))\nSet o\
  \ = d.DynamicInvoke(al.ToArray()).CreateInstance(entry_class)\n```\n\n![](<../../.gitbook/assets/Annotation 2019-05-19 145407.png>)\n\
  \n## Execution & Observation\n\nLet's now run the test.vbs - it pops the message box as expected:\n\n\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-05-19 135844.png>)\n\nLooking at the loaded modules of the wscript.exe, we can see a number of .NET assemblies in\
  \ the process memory, which makes sense if you think about it:\n\n![](<../../.gitbook/assets/Annotation 2019-05-19 141447.png>)\n\
  \nNow, what happens if we try executing a simple vbscript that pops a message box and inspect the loaded modules of the\
  \ wscript.exe again?  Bingo, no .NET assemlies loaded:\n\n![](<../../.gitbook/assets/Annotation 2019-05-19 142153.png>)\n\
  \nLooking from the defensive point of view, it may be worth checking the environment for machines executing wscript (or\
  \ jscript or cscript) which load .NET assemblies in their memory space and make sure the activity is benign.\n\nSince .js\
  \ or .vbs may be one of the payload delivery methods used in phishing using [file smuggling](file-smuggling-with-html-and-javascript.md)\
  \ through browsers, you may also want to check your environment for wscript (or cscript or jscript) launching files scripts\
  \ from the user's download folder which is the default browser download location.\n\nKnow of any other hlepful artefacts?\
  \ Let me know.\n\n## References\n\n{% embed url=\"https://github.com/tyranid/DotNetToJScript\" %}"
_relative_path: offensive-security/defense-evasion/executing-csharp-assemblies-from-jscript-and-wscript-with-dotnettojscript.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/executing-csharp-assemblies-from-jscript-and-wscript-with-dotnettojscript.md
````
