---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Windows x64 Calling Convention: Stack Frame

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-windows-x64-calling-convention-stack-frame` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/windows-x64-calling-convention-stack-frame.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

When a function in a Windows x64 binary is called, the stack frame is used in the following manner:

## Preserved Body

```markdown
When a function in a Windows x64 binary is called, the stack frame is used in the following manner:

* First four integer arguments are passed to RCX, RDX, R8 and R9 registers accordingly (green)
* Arguments 5, 6, and further are pushed on to the stack (blue)
* Return address to the caller's next instruction is pushed is found at RSP + 0x0 (yellow)
* Below return address (RSP + 0x0) 32 bytes are always allocated for RCD, RDX, R8 and R9, even if the callee  uses less than 4 arguments
* Local variables and non-volatile registers are stored above the return address (red)
* RBP is not used for referencing local variables/function arguments (except for when functions use `alloca()`) as it used to be the case for X86. RSP is responsible for that, hence RSP value does not change throughout the function body (push and pop is only used for epilogue/prologue)

![](<../../_assets/image (594).png>)

As an example, let's take a look at the function `msv1_0.LsaInitializePackage` in Ghidra. \
Below shows how the first four arguments are stored in ECX (lower part of RCX), RDX, R8 and R9:

![](<../../_assets/image (595).png>)

## References
```

## Source Verification

[source record](../../sources/redteamingtactics/windows-x64-calling-convention-stack-frame.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (594).png
- image (595).png
_body: '# Windows x64 Calling Convention: Stack Frame
When a function in a Windows x64 binary is called, the stack frame is used in the following manner:
* First four integer arguments are passed to RCX, RDX, R8 and R9 registers accordingly (green)
* Arguments 5, 6, and further are pushed on to the stack (blue)
* Return address to the caller''s next instruction is pushed is found at RSP + 0x0 (yellow)
```
