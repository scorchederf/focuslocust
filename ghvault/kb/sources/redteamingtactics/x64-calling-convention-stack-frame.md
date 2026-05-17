---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# x64 Calling Convention: Stack Frame

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-x64-calling-convention-stack-frame` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/x64-calling-convention-stack-frame.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [x64 Calling Convention: Stack Frame](../../topics/miscellaneous-reversing-forensics/x64-calling-convention-stack-frame.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-x64-calling-convention-stack-frame |
| name | x64 Calling Convention: Stack Frame |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/x64-calling-convention-stack-frame.md |

## Preserved Source Material

```yaml
_asset_filenames:
- image (590).png
- image (733).png
_body: "# x64 Calling Convention: Stack Frame\n\nWhen a function in a Windows x64 binary is called, the stack frame is used\
  \ in the following manner:\n\n* First four integer arguments are passed to RCX, RDX, R8 and R9 registers accordingly \\\
  (green\\)\n* Arguments 5, 6, and further are pushed on to the stack \\(blue\\)\n* Return address to the caller's next instruction\
  \ is pushed is found at RSP + 0x0 \\(yellow\\)\n* Below return address \\(RSP + 0x0\\) 32 bytes are always allocated for\
  \ RCD, RDX, R8 and R9, even if the callee  uses less than 4 arguments\n* Local variables and non-volatile registers are\
  \ stored above the return address \\(red\\)\n* RBP is not used for referencing local variables/function arguments \\(except\
  \ for when functions use `alloca()`\\) as it used to be the case for X86. RSP is responsible for that, hence RSP value does\
  \ not change throughout the function body \\(push and pop is only used for epilogue/prologue\\)\n\n![](../../.gitbook/assets/image%20%28590%29.png)\n\
  \nAs an example, let's take a look at the function `msv1_0.LsaInitializePackage` in Ghidra.   \nBelow shows how the first\
  \ four arguments are stored in ECX \\(lower part of RCX\\), RDX, R8 and R9:\n\n![](../../.gitbook/assets/image%20%28733%29.png)\n\
  \n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/cpp/build/stack-usage?view=vs-2019\" %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/x64-calling-convention-stack-frame.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/x64-calling-convention-stack-frame.md
```
