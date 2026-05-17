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

## Summary

Some things that could be useful to debug/deobfuscate a malicious VBS file:

## Preserved Body

````markdown
Some things that could be useful to debug/deobfuscate a malicious VBS file:

## echo

```bash
Wscript.Echo "Like this?"
```

## Commnets

```bash
' this is a comment
```

## Test

```bash
cscript.exe file.vbs
```

## Write data to a file

```js
Function writeBinary(strBinary, strPath)

    Dim oFSO: Set oFSO = CreateObject("Scripting.FileSystemObject")

    ' below lines purpose: checks that write access is possible!
    Dim oTxtStream

    On Error Resume Next
    Set oTxtStream = oFSO.createTextFile(strPath)

    If Err.number <> 0 Then MsgBox(Err.message) : Exit Function
    On Error GoTo 0

    Set oTxtStream = Nothing
    ' end check of write access

    With oFSO.createTextFile(strPath)
        .Write(strBinary)
        .Close
    End With

End Function
```
````

## Source Verification

[source record](../../sources/hacktricks/desobfuscation-techniques-for-vbs-files.md)

## Evidence Excerpt

````text
_body: "# Desobfuscation Techniques for VBS Files\n\n{{#include ../../../banners/hacktricks-training.md}}\n\nSome things that\
\ could be useful to debug/deobfuscate a malicious VBS file:\n\n## echo\n\n```bash\nWscript.Echo \"Like this?\"\n```\n\n\
## Commnets\n\n```bash\n' this is a comment\n```\n\n## Test\n\n```bash\ncscript.exe file.vbs\n```\n\n## Write data to a\
\ file\n\n```js\nFunction writeBinary(strBinary, strPath)\n\n    Dim oFSO: Set oFSO = CreateObject(\"Scripting.FileSystemObject\"\
)\n\n    ' below lines purpose: checks that write access is possible!\n    Dim oTxtStream\n\n    On Error Resume Next\n\
\    Set oTxtStream = oFSO.createTextFile(strPath)\n\n    If Err.number <> 0 Then MsgBox(Err.message) : Exit Function\n\
\    On Error GoTo 0\n\n    Set oTxtStream = Nothing\n    ' end check of write access\n\n    With oFSO.createTextFile(strPath)\n\
\        .Write(strBinary)\n        .Close\n    End With\n\nEnd Function\n```\n\n{{#include ../../../banners/hacktricks-training.md}}"
````
