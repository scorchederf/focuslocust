---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Desobfuscation Techniques for VBS Files

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-specific-software-file-type-tricks-desofuscation-vbs-cscript.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/desofuscation-vbs-cscript.exe.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Desobfuscation Techniques for VBS Files](../../topics/generic-methodologies-and-resources/desobfuscation-techniques-for-vbs-files.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-specific-software-file-type-tricks-desofuscation-vbs-cscript.exe |
| name | Desobfuscation Techniques for VBS Files |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/desofuscation-vbs-cscript.exe.md |

## Preserved Source Material

````yaml
_body: "# Desobfuscation Techniques for VBS Files\n\n{{#include ../../../banners/hacktricks-training.md}}\n\nSome things that\
  \ could be useful to debug/deobfuscate a malicious VBS file:\n\n## echo\n\n```bash\nWscript.Echo \"Like this?\"\n```\n\n\
  ## Commnets\n\n```bash\n' this is a comment\n```\n\n## Test\n\n```bash\ncscript.exe file.vbs\n```\n\n## Write data to a\
  \ file\n\n```js\nFunction writeBinary(strBinary, strPath)\n\n    Dim oFSO: Set oFSO = CreateObject(\"Scripting.FileSystemObject\"\
  )\n\n    ' below lines purpose: checks that write access is possible!\n    Dim oTxtStream\n\n    On Error Resume Next\n\
  \    Set oTxtStream = oFSO.createTextFile(strPath)\n\n    If Err.number <> 0 Then MsgBox(Err.message) : Exit Function\n\
  \    On Error GoTo 0\n\n    Set oTxtStream = Nothing\n    ' end check of write access\n\n    With oFSO.createTextFile(strPath)\n\
  \        .Write(strBinary)\n        .Close\n    End With\n\nEnd Function\n```\n\n{{#include ../../../banners/hacktricks-training.md}}"
_relative_path: generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/desofuscation-vbs-cscript.exe.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/desofuscation-vbs-cscript.exe.md
````
