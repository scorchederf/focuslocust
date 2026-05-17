---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# DDexec / EverythingExec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-linux-hardening-bypass-bash-restrictions-bypass-fs-protections-read-only-no-exec-distroless-ddexec` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/bypass-bash-restrictions/bypass-fs-protections-read-only-no-exec-distroless/ddexec.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DDexec / EverythingExec](../../topics/linux-hardening/ddexec-everythingexec.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-linux-hardening-bypass-bash-restrictions-bypass-fs-protections-read-only-no-exec-distroless-ddexec |
| name | DDexec / EverythingExec |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/linux-hardening/bypass-bash-restrictions/bypass-fs-protections-read-only-no-exec-distroless/ddexec.md |

## Preserved Source Material

````yaml
_body: "# DDexec / EverythingExec\n\n{{#include ../../../banners/hacktricks-training.md}}\n\n## Context\n\nIn Linux in order\
  \ to run a program it must exist as a file, it must be accessible in some way through the file system hierarchy (this is\
  \ just how `execve()` works). This file may reside on disk or in ram (tmpfs, memfd) but you need a filepath. This has made\
  \ very easy to control what is run on a Linux system, it makes easy to detect threats and attacker's tools or to prevent\
  \ them from trying to execute anything of theirs at all (_e. g._ not allowing unprivileged users to place executable files\
  \ anywhere).\n\nBut this technique is here to change all of this. If you can not start the process you want... **then you\
  \ hijack one already existing**.\n\nThis technique allows you to **bypass common protection techniques such as read-only,\
  \ noexec, file-name whitelisting, hash whitelisting...**\n\n## Dependencies\n\nThe final script depends on the following\
  \ tools to work, they need to be accessible in the system you are attacking (by default you will find all of them everywhere):\n\
  \n```\ndd\nbash | zsh | ash (busybox)\nhead\ntail\ncut\ngrep\nod\nreadlink\nwc\ntr\nbase64\n```\n\n## The technique\n\n\
  If you are able to modify arbitrarily the memory of a process then you can take over it. This can be used to hijack an already\
  \ existing process and replace it with another program. We can achieve this either by using the `ptrace()` syscall (which\
  \ requires you to have the ability to execute syscalls or to have gdb available on the system) or, more interestingly, writing\
  \ to `/proc/$pid/mem`.\n\nThe file `/proc/$pid/mem` is a one-to-one mapping of the entire address space of a process (_e.\
  \ g._ from `0x0000000000000000` to `0x7ffffffffffff000` in x86-64). This means that reading from or writing to this file\
  \ at an offset `x` is the same as reading from or modifying the contents at the virtual address `x`.\n\nNow, we have four\
  \ basic problems to face:\n\n- In general, only root and the program owner of the file may modify it.\n- ASLR.\n- If we\
  \ try to read or write to an address not mapped in the address space of the program we will get an I/O error.\n\nThis problems\
  \ have solutions that, although they are not perfect, are good:\n\n- Most shell interpreters allow the creation of file\
  \ descriptors that will then be inherited by child processes. We can create a fd pointing to the `mem` file of the sell\
  \ with write permissions... so child processes that use that fd will be able to modify the shell's memory.\n- ASLR isn't\
  \ even a problem, we can check the shell's `maps` file or any other from the procfs in order to gain information about the\
  \ address space of the process.\n- So we need to `lseek()` over the file. From the shell this cannot be done unless using\
  \ the infamous `dd`.\n\n### In more detail\n\nThe steps are relatively easy and do not require any kind of expertise to\
  \ understand them:\n\n- Parse the binary we want to run and the loader to find out what mappings they need. Then craft a\
  \ \"shell\"code that will perform, broadly speaking, the same steps that the kernel does upon each call to `execve()`:\n\
  \  - Create said mappings.\n  - Read the binaries into them.\n  - Set up permissions.\n  - Finally initialize the stack\
  \ with the arguments for the program and place the auxiliary vector (needed by the loader).\n  - Jump into the loader and\
  \ let it do the rest (load libraries needed by the program).\n- Obtain from the `syscall` file the address to which the\
  \ process will return after the syscall it is executing.\n- Overwrite that place, which will be executable, with our shellcode\
  \ (through `mem` we can modify unwritable pages).\n- Pass the program we want to run to the stdin of the process (will be\
  \ `read()` by said \"shell\"code).\n- At this point it is up to the loader to load the necessary libraries for our program\
  \ and jump into it.\n\n**Check out the tool in** [**https://github.com/arget13/DDexec**](https://github.com/arget13/DDexec)\n\
  \n## EverythingExec\n\nThere are several alternatives to `dd`, one of which, `tail`, is currently the default program used\
  \ to `lseek()` through the `mem` file (which was the sole purpose for using `dd`). Said alternatives are:\n\n```bash\ntail\n\
  hexdump\ncmp\nxxd\n```\n\nSetting the variable `SEEKER` you may change the seeker used, _e. g._:\n\n```bash\nSEEKER=cmp\
  \ bash ddexec.sh ls -l <<< $(base64 -w0 /bin/ls)\n```\n\nIf you find another valid seeker not implemented in the script\
  \ you may still use it setting the `SEEKER_ARGS` variable:\n\n```bash\nSEEKER=xxd SEEKER_ARGS='-s $offset' zsh ddexec.sh\
  \ ls -l <<< $(base64 -w0 /bin/ls)\n```\n\nBlock this, EDRs.\n\n## References\n\n- [https://github.com/arget13/DDexec](https://github.com/arget13/DDexec)\n\
  \n{{#include ../../../banners/hacktricks-training.md}}"
_relative_path: linux-hardening/bypass-bash-restrictions/bypass-fs-protections-read-only-no-exec-distroless/ddexec.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/bypass-bash-restrictions/bypass-fs-protections-read-only-no-exec-distroless/ddexec.md
````
