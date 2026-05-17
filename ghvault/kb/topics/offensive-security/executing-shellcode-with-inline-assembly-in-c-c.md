---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Executing Shellcode with Inline Assembly in C/C++

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-executing-shellcode-with-inline-assembly-in-c-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/executing-shellcode-with-inline-assembly-in-c-c++.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It's possible to execute shellcode inline in a C/C++ program. The reason why it's good to have this technique in your arsenal is because it does not require you to allocate new RWX memory to copy your shellcode over to by using VirtualAlloc

## Preserved Body

````markdown
It's possible to execute shellcode inline in a C/C++ program. The reason why it's good to have this technique in your arsenal is because it does not require you to allocate new `RWX` memory to copy your shellcode over to by using `VirtualAlloc` API which is heavily monitored by EDRs and can get you caught. Instead, the code will get embedded into the PE's `.TEXT` section which is executable by default as this is where the rest of your application's code resides.

## Execution

Install mingw - I'm doing it via chocolatey pacakge manager:

```csharp
choco install mingw
```

Create a simple C program that includes the shellcode. In my case, I'm simply adding 4 NOP instructions and prior to that, I am printing out the string `spotless`, so I can easily identify the shellcode location when debugging the program:
```cpp
#include <Windows.h>
#include <stdio.h>

int main() {
	printf("spotless");
    asm(".byte 0x90,0x90,0x90,0x90\n\t"
		"ret\n\t");
	return 0;
}
```
Let's compile and link the code:

```csharp
gcc -c .\inline-shellcode.c -o main.o; g++.exe .\main.o -o .\main.exe
```

Debugging the code via xdbg, we can see where the string `spotless` is going to be printed out and straight after it, we have the 4 NOP instructions:

![](<../../_assets/image (107).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/executing-shellcode-with-inline-assembly-in-c-c.md)

## Evidence Excerpt

````text
_asset_filenames:
- image (107).png
_body: "# Executing Shellcode with Inline Assembly in C/C++\n\nIt's possible to execute shellcode inline in a C/C++ program.\
\ The reason why it's good to have this technique in your arsenal is because it does not require you to allocate new `RWX`\
\ memory to copy your shellcode over to by using `VirtualAlloc` API which is heavily monitored by EDRs and can get you caught.\
\ Instead, the code will get embedded into the PE's `.TEXT` section which is executable by default as this is where the\
\ rest of your application's code resides.\n\n## Execution\n\nInstall mingw - I'm doing it via chocolatey pacakge manager:\n\
\n```csharp\nchoco install mingw\n```\n\nCreate a simple C program that includes the shellcode. In my case, I'm simply adding\
````
