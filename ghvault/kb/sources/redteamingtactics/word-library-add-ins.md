---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Word Library Add-Ins

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-word-library-add-ins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/word-library-add-ins.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Word Library Add-Ins](../../topics/offensive-security/word-library-add-ins.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-word-library-add-ins |
| name | Word Library Add-Ins |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/word-library-add-ins.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-06-22 121402.png
- Annotation 2019-06-22 121426.png
- Annotation 2019-06-22 121537.png
- Annotation 2019-06-22 143432.png
- Annotation 2019-06-22 143558.png
- Annotation 2019-06-22 144024.png
- Annotation 2019-06-22 144128.png
- Annotation 2019-06-22 144219.png
_body: "# Word Library Add-Ins\n\nIt' possible to persist in the userland by abusing word library add-ins by putting your\
  \ malicious DLL into a Word's trusted location. Once the DLL is there, the Word will load it next time it is run.\n\n##\
  \ Execution\n\nGet Word's trusted locations where library add-ins can be dropped:\n\n{% tabs %}\n{% tab title=\"attacker@target\"\
  \ %}\n```csharp\n Get-ChildItem \"hkcu:\\Software\\Microsoft\\Office\\16.0\\Word\\Security\\Trusted Locations\"\n```\n{%\
  \ endtab %}\n{% endtabs %}\n\n![](<../../.gitbook/assets/Annotation 2019-06-22 121402.png>)\n\nThose trusted locations are\
  \ actually defined in Word's Security Center if you have access to the GUI:\n\n![](<../../.gitbook/assets/Annotation 2019-06-22\
  \ 121426.png>)\n\nLet's create a simple DLL that will launch a notepad.exe once the DLL addin is loaded:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-06-22 143558.png>)\n\nCompile the DLL and copy it over to `Startup` folder and rename it to `evilm64.wll`:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-06-22 121537.png>)\n\n```\nmv .\\evilm64.dll .\\evilm64.wll\n```\n\n![](<../../.gitbook/assets/Annotation 2019-06-22\
  \ 144024.png>)\n\nNext time the victim opens up Word, `evilm64.wll` will be loaded and executed:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-06-22 143432.png>)\n\nInteresting to note that Process Explorer does not see the evilm64.wll loaded in any of the\
  \ currently running processes:\n\n![](<../../.gitbook/assets/Annotation 2019-06-22 144128.png>)\n\n...although we can definitely\
  \ see that the add-in is now recognized by Word:\n\n![](<../../.gitbook/assets/Annotation 2019-06-22 144219.png>)\n\n{%\
  \ hint style=\"info\" %}\nThis technique did not work for me on Office 365 version, but worked on Office Professional. Not\
  \ sure if there's a bug in the 365 version or it's just a limitation of that version.\n{% endhint %}\n\n## References\n\n\
  {% embed url=\"https://www.mdsec.co.uk/2019/05/persistence-the-continued-or-prolonged-existence-of-something-part-1-microsoft-office/\"\
  \ %}\n\n{% embed url=\"https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/\" %}"
_relative_path: offensive-security/persistence/word-library-add-ins.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/word-library-add-ins.md
````
