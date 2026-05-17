---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Shellcode Reflective DLL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-reflective-shellcode-dll-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/reflective-shellcode-dll-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shellcode Reflective DLL Injection](../../topics/offensive-security/shellcode-reflective-dll-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-reflective-shellcode-dll-injection |
| name | Shellcode Reflective DLL Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/reflective-shellcode-dll-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (15).png
- image (16).png
- image (21).png
- image (24).png
- image (26).png
- image (27).png
- pop-2notepads.gif
_body: '# Shellcode Reflective DLL Injection


  Shellcode reflective DLL injection (sRDI) is a technique that allows converting a given DLL into a position independent
  shellcode that can then be injected using your favourite shellcode injection and execution technique. In this lab I wanted
  to try this technique as I think it is an amazing technique to have in your arsenal.


  In this lab, I''m playing with the amazing [https://github.com/monoxgas/sRDI](https://github.com/monoxgas/sRDI) written
  by monoxgas from Silent Break Security.


  ## Execution


  Let''s compile a simple x86 DLL - in my case, an odd DLL that pops 2 notepad processes when executed:


  ![](<../../.gitbook/assets/image (24).png>)


  Convert the DLL into shellcode. We will get an array of shellcode bytes represented in decimal values:


  ```csharp

  $sc = ConvertTo-Shellcode \\VBOXSVR\Experiments\messagebox\messagebox\Debug\messagebox.dll

  ```


  ![](<../../.gitbook/assets/image (15).png>)


  Let''s convert them to hex:


  ```csharp

  $sc2 = $sc | % { write-output ([System.String]::Format(''{0:X2}'', $_)) }

  ```


  ![](<../../.gitbook/assets/image (16).png>)


  Join them all and print to a text file:


  ```

  $sc2 -join "" > shell.txt

  ```


  ![](<../../.gitbook/assets/image (21).png>)


  Create a new binary file with the shellcode we got earlier - just copy the hex string (as seen in the above screenshot)
  and paste it to a new file using HxD hex editor:


  ![](<../../.gitbook/assets/image (26).png>)


  In order to load and execute the shellcode, we will place it in the binary as a resource as described in my other lab [Loading
  and Executing Shellcode From PE Resources](loading-and-executing-shellcode-from-portable-executable-resources.md):


  ![](<../../.gitbook/assets/image (27).png>)


  Compile and run the binary. If the shellcode runs successfully, we should see two notepad.exe processes popup:


  ![](../../.gitbook/assets/pop-2notepads.gif)


  ## References


  {% embed url="https://github.com/monoxgas/sRDI/tree/master/PowerShell" %}'
_relative_path: offensive-security/code-injection-process-injection/reflective-shellcode-dll-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/reflective-shellcode-dll-injection.md
````
