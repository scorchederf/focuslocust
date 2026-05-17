---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Array Indexing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-binary-exploitation-array-indexing` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/binary-exploitation/array-indexing.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Array Indexing](../../topics/binary-exploitation/array-indexing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-binary-exploitation-array-indexing |
| name | Array Indexing |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/binary-exploitation/array-indexing.md |

## Preserved Source Material

```yaml
_body: "# Array Indexing\n\n{{#include ../banners/hacktricks-training.md}}\n\n## Basic Information\n\nThis category includes\
  \ all vulnerabilities that occur because it is possible to overwrite certain data through errors in the handling of indexes\
  \ in arrays. It's a very wide category with no specific methodology as the exploitation mechanism relays completely on the\
  \ conditions of the vulnerability.\n\nHowever he you can find some nice **examples**:\n\n- [https://guyinatuxedo.github.io/11-index/swampctf19_dreamheaps/index.html](https://guyinatuxedo.github.io/11-index/swampctf19_dreamheaps/index.html)\n\
  \  - There are **2 colliding arrays**, one for **addresses** where data is stored and one with the **sizes** of that data.\
  \ It's possible to overwrite one from the other, enabling to write an arbitrary address indicating it as a size. This allows\
  \ to write the address of the `free` function in the GOT table and then overwrite it with the address to `system`, and call\
  \ free from a memory with `/bin/sh`.\n- [https://guyinatuxedo.github.io/11-index/csaw18_doubletrouble/index.html](https://guyinatuxedo.github.io/11-index/csaw18_doubletrouble/index.html)\n\
  \  - 64 bits, no nx. Overwrite a size to get a kind of buffer overflow where every thing is going to be used a double number\
  \ and sorted from smallest to biggest so it's needed to create a shellcode that fulfil that requirement, taking into account\
  \ that the canary shouldn't be moved from it's position and finally overwriting the RIP with an address to ret, that fulfil\
  \ he previous requirements and putting the biggest address a new address pointing to the start of the stack (leaked by the\
  \ program) so it's possible to use the ret to jump there.\n- [https://faraz.faith/2019-10-20-secconctf-2019-sum/](https://faraz.faith/2019-10-20-secconctf-2019-sum/)\n\
  \  - 64bits, no relro, canary, nx, no pie. There is an off-by-one in an array in the stack that allows to control a pointer\
  \ granting WWW (it write the sum of all the numbers of the array in the overwritten address by the of-by-one in the array).\
  \ The stack is controlled so the GOT `exit` address is overwritten with `pop rdi; ret`, and in the stack is added the address\
  \ to `main` (looping back to `main`). The a ROP chain to leak the address of put in the GOT using puts is used (`exit` will\
  \ be called so it will call `pop rdi; ret` therefore executing this chain in the stack). Finally a new ROP chain executing\
  \ ret2lib is used.\n- [https://guyinatuxedo.github.io/14-ret_2_system/tu_guestbook/index.html](https://guyinatuxedo.github.io/14-ret_2_system/tu_guestbook/index.html)\n\
  \  - 32 bit, no relro, no canary, nx, pie. Abuse a bad indexing to leak addresses of libc and heap from the stack. Abuse\
  \ the buffer overflow o do a ret2lib calling `system('/bin/sh')` (the heap address is needed to bypass a check).\n\n\n\n\
  \n{{#include ../banners/hacktricks-training.md}}"
_relative_path: binary-exploitation/array-indexing.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/binary-exploitation/array-indexing.md
```
