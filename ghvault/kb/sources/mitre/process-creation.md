---
parsed_by: focuslocust
source: mitre
type: generated
---
# Process Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0032` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Creation](../../attack/data-sources/DC0032-process-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0032 |
| name | Process Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0032 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Refers to the event in which a new process (executable) is initialized by an operating system. This can involve
  parent-child process relationships, process arguments, and environmental variables. Monitoring process creation is crucial
  for detecting malicious behaviors, such as execution of unauthorized binaries, scripting abuse, or privilege escalation
  attempts.. '
external_references:
- external_id: DC0032
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0032
id: x-mitre-data-component--3d20385b-24ef-40e1-9f56-f39750379077
modified: '2026-04-13T15:49:16.424Z'
name: Process Creation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- mobile-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Process
- channel: execve
  name: auditd:SYSCALL
- channel: log stream 'eventMessage contains pubsub or broker'
  name: macos:unifiedlog
- channel: EventCode=1
  name: WinEventLog:Sysmon
- channel: Execution of binary resolved from $PATH not located in /usr/bin or /bin
  name: linux:osquery
- channel: Process execution path inconsistent with baseline PATH directories
  name: macos:unifiedlog
- channel: ES_EVENT_TYPE_NOTIFY_EXEC
  name: macos:endpointsecurity
- channel: EventCode=4688
  name: WinEventLog:Security
- channel: process_events
  name: linux:osquery
- channel: exec
  name: macos:endpointsecurity
- channel: processes
  name: macos:osquery
- channel: Execution of launchctl with suspicious arguments
  name: macos:unifiedlog
- channel: execve network tools
  name: auditd:SYSCALL
- channel: process_events
  name: macos:osquery
- channel: execve calls to soffice.bin with suspicious macro execution flags
  name: auditd:SYSCALL
- channel: Process execution of Microsoft Word, Excel, PowerPoint with macro execution attempts
  name: macos:unifiedlog
- channel: process reading browser configuration paths
  name: macos:osquery
- channel: exec logs
  name: macos:unifiedlog
- channel: 'execve: Processes launched with LD_PRELOAD/LD_LIBRARY_PATH pointing to non-system dirs'
  name: auditd:EXECVE
- channel: 'exec: Process execution context for loaders calling dlopen/dlsym'
  name: macos:endpointsecurity
- channel: EXECVE
  name: auditd:EXECVE
- channel: execution of unexpected binaries during user shell startup
  name: auditd:EXECVE
- channel: launch of Terminal.app or shell with non-standard environment setup
  name: macos:unifiedlog
- channel: ES_EVENT_TYPE_NOTIFY_EXEC with unusual parent-child process relationships from zsh
  name: macos:endpointsecurity
- channel: execve of systemctl or service stop
  name: auditd:SYSCALL
- channel: execve of launchctl or pkill
  name: auditd:SYSCALL
- channel: process::exec
  name: macos:unifiedlog
- channel: 'execve: Execution of klist, kinit, or tools interacting with ccache outside normal user context'
  name: auditd:SYSCALL
- channel: Execution of non-standard binaries accessing Kerberos APIs
  name: macos:osquery
- channel: 'execve: Electron-based binary spawning shell or script interpreter'
  name: auditd:SYSCALL
- channel: Electron app spawning unexpected child process
  name: macos:unifiedlog
- channel: /root/.ash_history or /etc/init.d/*
  name: esxi:shell
- channel: execve calls with high-frequency or known bandwidth-intensive tools
  name: auditd:SYSCALL
- channel: exec or spawn calls to proxy tools or torrent clients
  name: macos:unifiedlog
- channel: bandwidth-intensive command execution from within a container namespace
  name: containers:osquery
- channel: process launch
  name: macos:unifiedlog
- channel: log stream --info --predicate 'subsystem == "com.apple.cfprefsd"'
  name: macos:unifiedlog
- channel: execution of security, sqlite3, or unauthorized binaries
  name: macos:unifiedlog
- channel: Unexpected applications generating outbound DNS queries
  name: macos:unifiedlog
- channel: EventCode=1
  name: linux:Sysmon
- channel: execve
  name: macos:osquery
- channel: Unexpected child process of Safari or Chrome
  name: macos:unifiedlog
- channel: execve or syscall invoking vm artifact check commands (e.g., dmidecode, lspci, dmesg)
  name: auditd:SYSCALL
- channel: execution of system_profiler, ioreg, kextstat with argument patterns related to VM/sandbox checks
  name: macos:unifiedlog
- channel: process writes or modifies files in excluded paths
  name: macos:unifiedlog
- channel: process
  name: macos:unifiedlog
- channel: com.apple.mail.* exec.*
  name: macos:unifiedlog
- channel: execution of memory inspection tools (lldb, gdb, osqueryi)
  name: macos:unifiedlog
- channel: /var/log/vobd.log
  name: esxi:vobd
- channel: kubectl exec or kubelet API calls targeting running pods
  name: kubernetes:apiserver
- channel: Process execution events within container namespace context
  name: docker:audit
- channel: process persists beyond parent shell termination
  name: auditd:SYSCALL
- channel: background process persists beyond user logout
  name: macos:unifiedlog
- channel: 'execve: Execution of scripts or binaries sourced from mail directories (/var/mail, ~/Maildir)'
  name: auditd:SYSCALL
- channel: Preview.app, Safari.app, or Mail.app spawning new processes outside normal patterns
  name: macos:unifiedlog
- channel: process execution across cloud VM
  name: esxi:hostd
- channel: systemctl spawning managed processes
  name: auditd:EXECVE
- channel: None
  name: macos:unifiedlog
- channel: /var/log/shell.log
  name: esxi:shell
- channel: Execution of processes linked to hijacked sessions (e.g., anomalous parent-child process lineage)
  name: macos:unifiedlog
- channel: exec events where web process starts a shell/tooling
  name: macos:unifiedlog
- channel: Docker/Kubernetes audit of exec/attach (kubectl exec) or unexpected child processes inside container
  name: docker:events
- channel: exec of osascript, bash, curl with suspicious parameters
  name: macos:unifiedlog
- channel: 'execve: Execution of container management CLIs (docker, crictl, kubectl) or interpreted shells (sh, bash, python)
    within container context'
  name: auditd:SYSCALL
- channel: es_event_exec
  name: macos:endpointsecurity
- channel: 'execve: Execution of discovery commands targeting backup binaries, processes, or config paths'
  name: auditd:SYSCALL
- channel: Process execution logs showing discovery commands like mdfind, system_profiler, or launchctl list
  name: macos:unifiedlog
- channel: process_events OR launchd
  name: macos:osquery
- channel: execve
  name: auditd:EXECVE
- channel: launchd or process_events
  name: macos:osquery
- channel: process and file events via log stream
  name: macos:unifiedlog
- channel: 'execve: Execution of scripts or binaries spawned from browser processes'
  name: auditd:SYSCALL
- channel: Browser processes launching unexpected interpreters (osascript, bash)
  name: macos:unifiedlog
- channel: 'exec: Execution of defaults, plutil, or common editors (vim/nano) targeting plist files'
  name: macos:unifiedlog
- channel: EXECVE
  name: auditd:SYSCALL
- channel: process:exec
  name: macos:unifiedlog
- channel: 'execve: Execution of bash, python, or perl processes spawned by browser/email client'
  name: auditd:SYSCALL
- channel: Execution of osascript, bash, or Terminal initiated from Mail.app or Safari
  name: macos:unifiedlog
- channel: execve of /bin/sh,/bin/bash,/usr/bin/curl,/usr/bin/python by service accounts (e.g., apache, mysql, nobody) immediately
    after inbound network activity.
  name: auditd:SYSCALL
- channel: parent_name in ('sshd','httpd','screensharingd') spawning shells or scripting runtimes.
  name: macos:osquery
- channel: process activity stream
  name: macos:unifiedlog
- channel: SYSCALL record where exe contains passwd/userdel/chage and auid != root
  name: auditd:SYSCALL
- channel: Post-login execution of unrecognized child process from launchd or loginwindow
  name: macos:unifiedlog
- channel: execve of base64|openssl|xxd|python|perl with arguments matching Base64 flags
  name: auditd:SYSCALL
- channel: process command line contains base64, -enc, openssl enc -base64
  name: macos:unifiedlog
- channel: 'exec: arguments contain Base64-like strings'
  name: macos:endpointsecurity
- channel: commands containing base64, openssl enc -base64, xxd -p
  name: esxi:shell
- channel: Execution of process launched via loginwindow session restore
  name: macos:unifiedlog
- channel: 'process: exec + filewrite: ~/.ssh/authorized_keys'
  name: macos:unifiedlog
- channel: /var/log/containers/*.log
  name: containerd:runtime
- channel: Execution of Java apps or other processes with hidden window attributes
  name: macos:unifiedlog
- channel: Process Execution
  name: macos:unifiedlog
- channel: execve on code or jetbrains-gateway with remote flags
  name: auditd:SYSCALL
- channel: 'process: code or jetbrains-gateway launching with --tunnel or --remote'
  name: macos:unifiedlog
- channel: log stream --predicate 'processImagePath CONTAINS "curl" OR "osascript"'
  name: macos:unifiedlog
- channel: Execution of dd, shred, wipe targeting block devices
  name: auditd:EXECVE
- channel: execve of sleep or ping command within script interpreted by bash/python
  name: auditd:SYSCALL
- channel: execve or socket/connect system calls from processes using crypto libraries
  name: auditd:SYSCALL
- channel: Process using AES/RC4 routines unexpectedly
  name: macos:unifiedlog
- channel: execution of known firewall binaries
  name: linux:osquery
- channel: type=EXECVE or SYSCALL for /bin/date, /usr/bin/timedatectl, /sbin/hwclock, /bin/cat /etc/timezone, /bin/cat /proc/uptime
  name: auditd:SYSCALL
- channel: 'execve: command like ''date'', ''timedatectl'', ''hwclock'', ''cat /etc/timezone'''
  name: linux:osquery
- channel: process exec events of systemsetup, date, ioreg with command_line parameters indicating time discovery
  name: macos:unifiedlog
- channel: 'exec: binary == "/usr/sbin/systemsetup" and args contains "-gettimezone"'
  name: macos:endpointsecurity
- channel: 'execve: command LIKE ''%systemsetup -gettimezone%'' OR ''%date%'''
  name: macos:osquery
- channel: execution of osascript, curl, or unexpected automation
  name: macos:unifiedlog
- channel: exec /usr/bin/pwpolicy
  name: macos:unifiedlog
- channel: socket(AF_PACKET|AF_INET, SOCK_RAW, *), setsockopt(… SO_ATTACH_FILTER|SO_ATTACH_BPF …), bpf(cmd=BPF_PROG_LOAD),
    open/openat path="/dev/bpf*" (BSD/macOS-like) or setcap cap_net_raw.
  name: auditd:SYSCALL
- channel: KERN messages about eBPF program load/verify or LSM denials related to bpf.
  name: linux:syslog
- channel: open/openat of /dev/bpf*; ioctl BIOCSETF-like operations.
  name: OpenBSM:AuditTrail
- channel: Exec of tcpdump, rvictl, custom tools linked to libpcap.A.dylib; sysextd/systemextensionsctl events for NetworkExtension
    content filters.
  name: macos:unifiedlog
- channel: /usr/sbin/postfix, /usr/sbin/exim, /usr/sbin/sendmail
  name: auditd:EXECVE
- channel: execution of known flash tools (e.g., flashrom, fwupd)
  name: auditd:SYSCALL
- channel: com.apple.firmwareupdater activity or update-firmware binary invoked
  name: macos:unifiedlog
- channel: execve of system tools like dmidecode, lspci, lscpu, dmesg, systemd-detect-virt
  name: auditd:SYSCALL
- channel: exec or spawn of 'system_profiler', 'ioreg', 'kextstat', 'sysctl', or calls to sysctl API
  name: macos:unifiedlog
- channel: ES_EVENT_TYPE_NOTIFY_EXEC
  name: macos:endpointSecurity
- channel: 'execve: Suspicious binaries or scripts interacting with authentication binaries (sshd, gdm, login)'
  name: auditd:SYSCALL
- channel: 'execve: Processes unexpectedly invoking Keychain or authentication APIs'
  name: macos:osquery
- channel: 'execve: execve calls where a browser/webview process is parent and child is interpreter (python, sh, ruby) or
    downloader (curl, wget)'
  name: auditd:SYSCALL
- channel: 'process_create: Process creation where parent is Safari/Google Chrome and child is script interpreter or signed-but-unusual
    helper binary'
  name: macos:unifiedlog
- channel: None
  name: auditd:EXECVE
- channel: process:launch
  name: macos:unifiedlog
- channel: Shell commands invoked by SQL process such as postgres, mysqld, or mariadbd
  name: auditd:EXECVE
- channel: execve of smbclient, smbmap, rpcclient, nmblookup, crackmapexec smb
  name: auditd:SYSCALL
- channel: 'ES_EVENT_TYPE_NOTIFY_EXEC: Process execution of "sharing -l", "smbutil view", "mount_smbfs"'
  name: macos:endpointsecurity
- channel: Execution of scp, rsync, curl with remote destination
  name: macos:unifiedlog
- channel: logMessage contains pbpaste or osascript
  name: macos:unifiedlog
- channel: execve call with argv matching known disk enumeration commands (lsblk, parted, fdisk)
  name: auditd:SYSCALL
- channel: process launch of diskutil or system_profiler with SPStorageDataType
  name: macos:unifiedlog
- channel: execution of esxcli with args matching 'storage', 'filesystem', 'core device list'
  name: esxi:hostd
- channel: Mail.app executing with parameters updating rules state
  name: macos:unifiedlog
- channel: /var/log/vmkernel.log, /var/log/vmkwarning.log
  name: esxi:shell
- channel: 'exec: Exec of ffmpeg, avfoundation-based binaries, or custom signed apps accessing camera'
  name: macos:endpointsecurity
- channel: exec into pod followed by secret retrieval via API
  name: kubernetes:apiserver
- channel: process_name IN ("VBoxManage", "prlctl") AND command CONTAINS ("list", "show")
  name: macos:unifiedlog
- channel: exec srm|exec openssl|exec gpg
  name: macos:unifiedlog
- channel: Process execution with LD_PRELOAD or modified library path
  name: linux:osquery
- channel: Execution of process with DYLD_INSERT_LIBRARIES set
  name: macos:unifiedlog
- channel: process creation events linked to container namespaces executing host-level binaries
  name: linux:Sysmon
- channel: process and signing chain events
  name: macos:unifiedlog
- channel: launchservices events for misleading extensions
  name: macos:unifiedlog
- channel: Execution of disguised binaries
  name: fs:fsusage
- channel: process listening or connecting on non-standard ports
  name: linux:osquery
- channel: launchd services binding to non-standard ports
  name: macos:unifiedlog
- channel: execve, connect
  name: auditd:SYSCALL
- channel: process or cron activity
  name: esxi:cron
- channel: Execution of binaries with unsigned or anomalously signed certificates
  name: macos:unifiedlog
- channel: execve logging for /usr/bin/systemctl and systemd-run
  name: auditd:SYSCALL
- channel: Invocation of osascript or dylib injection
  name: macos:osquery
- channel: 'execve: Execution of files saved in mail or download directories'
  name: auditd:SYSCALL
- channel: Execution of Terminal, osascript, or other interpreters originating from Mail or Preview
  name: macos:unifiedlog
- channel: process events
  name: macos:unifiedlog
- channel: Unauthorized sudo or shell access, especially leading to file changes in /var/www or /srv/http
  name: linux:syslog
- channel: Execution of unexpected terminal or web scripts modifying /Library/WebServer/Documents
  name: macos:unifiedlog
- channel: 'execve: Execution of CLI tools like psql, mysql, mongo, sqlite3'
  name: auditd:SYSCALL
- channel: Process start of Java or native DB client tools
  name: macos:unifiedlog
- channel: loginwindow or tccd-related entries
  name: macos:unifiedlog
- channel: 'query: process_events, launchd, and tcc.db access'
  name: macos:osquery
- channel: process execution or network connect from just-created container PID namespace
  name: ebpf:syscalls
- channel: 'execve: Execution of pip, npm, gem, or similar package managers'
  name: auditd:SYSCALL
- channel: Command line invocation of pip3, brew install, npm install from interactive Terminal
  name: macos:unifiedlog
- channel: fork/exec of service via PID 1 (systemd)
  name: auditd:SYSCALL
- channel: Execution of ssh/scp/sftp without corresponding authentication log
  name: auditd:EXECVE
- channel: Execution of ssh or sftp without corresponding login event
  name: macos:unifiedlog
- channel: 'execve: execve where exe=/usr/bin/python3 or similar interpreter'
  name: auditd:SYSCALL
- channel: launch of remote desktop app or helper binary
  name: macos:unifiedlog
- channel: Unexpected processes making network calls based on DNS-derived ports
  name: macos:unifiedlog
- channel: launchctl spawning new processes
  name: macos:unifiedlog
- channel: launchctl activity and process creation
  name: macos:unifiedlog
- channel: New container with suspicious image name or high resource usage
  name: containerd:events
- channel: Execution of Python, Swift, or other binaries invoking archiving libraries
  name: macos:unifiedlog
- channel: Processes linked with libssl or crypto libraries making outbound connections
  name: linux:osquery
- channel: Process invoking SSL routines from Security framework
  name: macos:unifiedlog
- channel: Execution of binaries located in /etc/init.d/ or systemd service paths
  name: auditd:SYSCALL
- channel: Execution of binary listed in newly modified LaunchAgent plist
  name: macos:unifiedlog
- channel: Execution of bless or nvram modifying boot parameters
  name: macos:unifiedlog
- channel: Unexpected processes registered with launchd
  name: macos:unifiedlog
- channel: Process launch
  name: macos:unifiedlog
- channel: execution of curl, osascript, or unexpected Office processes
  name: macos:unifiedlog
- channel: exec
  name: macos:osquery
- channel: Trust validation failures or bypass attempts during notarization and code signing checks
  name: macos:unifiedlog
- channel: spawned shell or execution environment activity
  name: esxi:vmkernel
- channel: 'process_exec: image in {/bin/bash,/bin/zsh,/usr/bin/osascript,/usr/bin/python*,/usr/bin/curl,/usr/bin/ssh,/usr/bin/open}
    AND parent in {Preview, TextEdit, Microsoft Word, Microsoft Excel, AdobeReader, Archive Utility, Finder}'
  name: macos:unifiedlog
- channel: 'execve: exe in {/bin/bash,/bin/sh,/usr/bin/python*,/usr/bin/perl,/usr/bin/php,/usr/bin/node,/usr/bin/curl,/usr/bin/wget,/usr/bin/xdg-open,/usr/bin/ssh,/usr/bin/rundll32
    (wine)} AND ppid process is a document viewer/browser'
  name: auditd:SYSCALL
- channel: Execution of dd/sgdisk with arguments writing to sector 0 or partition table
  name: auditd:EXECVE
- channel: Execution of zip, ditto, hdiutil, or openssl by processes not normally associated with archiving
  name: macos:unifiedlog
- channel: process execution events for chmod, chown, chflags with unusual parameters or targets
  name: macos:unifiedlog
- channel: AdvancedHunting(DeviceEvents, ProcessCreate, ImageLoad, AMSI/ETW derived signals)
  name: m365:defender
- channel: execve or dylib load from memory without backing file
  name: macos:unifiedlog
- channel: 'execve: Commands that alter firewall or start listeners: iptables|nft|ufw|firewall-cmd|pfctl|systemctl start sshd/telnet/dropbear;
    raw-socket/libpcap tools (tcpdump, tshark, nmap --raw).'
  name: auditd:SYSCALL
- channel: 'exec: Execution of pfctl, socketfilterfw, launchctl start ssh/telnet, libpcap consumers.'
  name: macos:unifiedlog
- channel: Shell Execution
  name: esxi:shell
- channel: Unusual child process tree indicating attempted recovery after crash
  name: macos:unifiedlog
- channel: 'execve: Execution of binaries/scripts presenting false health messages for security daemons'
  name: auditd:SYSCALL
- channel: Execution of processes mimicking Apple Security & Privacy GUIs
  name: macos:unifiedlog
- channel: execve, setifflags
  name: auditd:SYSCALL
- channel: process_events where path like '%tcpdump%'
  name: macos:osquery
- channel: Execution of dd, shred, or wipe with arguments targeting block devices
  name: auditd:EXECVE
- channel: systemctl stop auditd, kill -9 <pid>, or modifications to /etc/selinux/config
  name: auditd:EXECVE
- channel: execution of curl, git, or Office processes with network connections
  name: macos:unifiedlog
- channel: log stream - process subsystem
  name: macos:unifiedlog
- channel: execve calls for qemu-system*, kvm, or VBoxHeadless
  name: auditd:SYSCALL
- channel: Process execution for VBoxHeadless, prl_vm_app, vmware-vmx
  name: macos:unifiedlog
- channel: process logs
  name: macos:unifiedlog
- channel: None
  name: esxi:shell
- channel: execve of interpreters (python, perl), custom binaries, or shell utilities with long arguments containing non-standard
    tokens
  name: auditd:SYSCALL
- channel: 'ES_EVENT_TYPE_NOTIFY_EXEC: arguments contain long, non-standard tokens / custom alphabets'
  name: macos:endpointsecurity
- channel: command line or log output shows non-standard encoding routines
  name: macos:unifiedlog
- channel: commands containing long non-standard tokens or custom lookup tables
  name: esxi:shell
- channel: Execution of /usr/sbin/installer spawning child process from within /private/tmp or package contents
  name: macos:unifiedlog
- channel: Execution of dpkg or rpm followed by fork/execve from within postinst, prerm, etc.
  name: auditd:SYSCALL
- channel: 'execve: Helper tools invoked through XPC executing unexpected binaries'
  name: macos:unifiedlog
- channel: execution of modified binary without valid signature
  name: macos:unifiedlog
- channel: 'execve: exe in (/usr/bin/bash,/usr/bin/sh,/usr/bin/zsh,/usr/bin/python*) AND cmdline matches ''(curl|wget).*(\||\|\s*sh|bash)|base64\s*-d|python\s*-c'''
  name: auditd:SYSCALL
- channel: 'exec: ParentImage in (Terminal, iTerm2) AND Image in (/bin/zsh,/bin/bash,/usr/bin/python*) AND CommandLine matches
    ''(curl|wget).*(\||\|\s*sh|bash)|base64 -D|python -c'''
  name: macos:unifiedlog
- channel: process created with repeated ICMP or UDP flood behavior
  name: macos:unifiedlog
- channel: binary execution of security_authtrampoline
  name: fs:fsusage
- channel: 'process: exec'
  name: macos:unifiedlog
- channel: Exec
  name: esxi:vmkernel
- channel: Child processes of Safari, Chrome, or Firefox executing scripting interpreters
  name: macos:unifiedlog
- channel: Execution of older or non-standard interpreters
  name: macos:unifiedlog
- channel: process execution events for permission modification utilities with command-line analysis
  name: linux:osquery
- channel: process execution events for chmod, chown, chflags with parameter analysis and target path examination
  name: macos:unifiedlog
- channel: process execution monitoring for permission modification utilities with command-line argument analysis
  name: macos:osquery
- channel: Invocation of packet generation tools (e.g., hping3, nping) or fork bombs
  name: auditd:SYSCALL
- channel: Execution of flooding tools or compiled packet generators
  name: macos:osquery
- channel: process
  name: esxi:hostd
- channel: execve for proxy tools
  name: auditd:SYSCALL
- channel: process, socket, and DNS logs
  name: macos:unifiedlog
- channel: process_events table
  name: macos:osquery
- channel: Command line containing `trap` or `echo 'trap` written to login shell files
  name: macos:unifiedlog
- channel: log collect --predicate
  name: macos:unifiedlog
- channel: execve or nanosleep with no stdout/stderr I/O
  name: auditd:SYSCALL
- channel: launchd or osascript spawns process with delay command
  name: macos:unifiedlog
- channel: systemd-udevd spawning user-defined action from RUN+=
  name: linux:syslog
- channel: execve
  name: ebpf:syscalls
- channel: process:spawn
  name: macos:unifiedlog
- channel: log stream --predicate 'eventMessage contains "exec"'
  name: macos:unifiedlog
- channel: cat|less|grep accessing .bash_history from a non-shell process
  name: auditd:EXECVE
- channel: Process execution via .desktop Exec path from /etc/xdg/autostart or ~/.config/autostart
  name: auditd:EXECVE
- channel: Execution of dpkg, rpm, or other package manager with list flag
  name: auditd:SYSCALL
- channel: Execution of system_profiler or osascript invoking enumeration
  name: macos:unifiedlog
- channel: apache2 or nginx spawning sh, bash, or python interpreter
  name: auditd:SYSCALL
- channel: httpd spawning bash, zsh, python, or osascript
  name: macos:unifiedlog
- channel: Execution of /usr/libexec/security_authtrampoline or child processes originating from non-trusted binaries triggering
    credential prompts
  name: macos:unifiedlog
- channel: execution of security or osascript
  name: macos:unifiedlog
- channel: launchd spawning processes tied to new or modified LaunchDaemon .plist entries
  name: macos:unifiedlog
- channel: Execution of ping, nping, or crafted network packets via bash or python to reflection services
  name: macos:unifiedlog
- channel: 'execve: Execution of commands modifying iptables/nftables to block selective IPs'
  name: auditd:SYSCALL
- channel: System process modifications altering DNS/proxy settings
  name: macos:unifiedlog
- channel: unusual process spawned from container image context
  name: containerd:Events
- channel: curl, python scripts, rsync with internal share URLs
  name: macos:osquery
- channel: 'process: spawn, exec'
  name: macos:unifiedlog
- channel: Rapid spawning of resource-heavy applications (e.g., Preview, Safari, Office)
  name: macos:osquery
- channel: Process creation events where command line = pmset with arguments affecting sleep, hibernatemode, displaysleep
  name: macos:unifiedlog
- channel: Unexpected apps performing repeated DNS lookups
  name: macos:unifiedlog
- channel: launchservices or loginwindow events
  name: macos:unifiedlog
- channel: execve with LD_PRELOAD or linker-related environment variables set
  name: auditd:SYSCALL
- channel: execution of process with DYLD_INSERT_LIBRARIES set
  name: macos:unifiedlog
- channel: Suspicious Swift/Objective-C or scripting processes writing archive-like outputs
  name: macos:unifiedlog
- channel: execve of re-parented process
  name: auditd:SYSCALL
- channel: Anomalous parent PID change
  name: linux:osquery
- channel: Process creation with parent PID of 1 (launchd)
  name: macos:unifiedlog
- channel: child process invoking dynamic linker post-ptrace
  name: linux:osquery
- channel: Processes executing kextload, spctl, or modifying kernel extension directories
  name: macos:osquery
- channel: Unsigned or ad-hoc signed process executions in user contexts
  name: macos:osquery
- channel: Execution of diskutil or hdiutil attaching hidden partitions
  name: macos:unifiedlog
- channel: process execution events for discovery utilities (system_profiler, sw_vers, dscl, networksetup) with command-line
    parameter analysis
  name: macos:unifiedlog
- channel: process event monitoring with focus on discovery utilities and cryptographic framework usage correlation
  name: macos:osquery
- channel: Unexpected apps generating frequent DNS queries
  name: macos:unifiedlog
- channel: process exec
  name: macos:unifiedlog
- channel: 'socket: Suspicious creation of AF_UNIX sockets outside expected daemons'
  name: auditd:SYSCALL
- channel: Non-standard processes invoking financial applications or payment APIs
  name: macos:unifiedlog
- channel: 'execve: Agent/headless flags (listen/connect/reverse/tunnel) or remote-control binaries spawning shells'
  name: auditd:SYSCALL
- channel: 'systemctl enable/start: Creation/enablement of custom .service units in /etc/systemd/system'
  name: auditd:SYSCALL
- channel: Process exec of remote-control apps or binaries with headless/connect flags
  name: macos:unifiedlog
- channel: 'execve: systemctl stop, service stop, or kill -9 on security daemons (e.g., falcon-sensor, auditd)'
  name: auditd:SYSCALL
- channel: Execution of launchctl unload, kill, or removal of security agent daemons
  name: macos:unifiedlog
- channel: process activity, exec events
  name: macos:unifiedlog
- channel: log stream process subsystem
  name: macos:unifiedlog
- channel: process:exec and kext load events
  name: macos:unifiedlog
- channel: log stream --info --predicate 'eventMessage CONTAINS "exec"'
  name: macos:unifiedlog
- channel: Unexpected AppDomain creation events or anomalous AppDomainManager assembly load behavior
  name: WinEventLog:Microsoft-Windows-DotNETRuntime
- channel: Execution of network stress tools or anomalies in socket/syscall behavior
  name: auditd:SYSCALL
- channel: Unsigned binary execution following SIP change
  name: macos:unifiedlog
- channel: 'execve: Commands altering firewall or enabling listeners (iptables, nft, ufw, firewall-cmd, systemctl start *ssh*/*telnet*,
    ip route add, tcpdump, tshark)'
  name: auditd:SYSCALL
- channel: 'exec: Execution of /sbin/pfctl, /usr/libexec/ApplicationFirewall/socketfilterfw, ifconfig, tcpdump, npcap/libpcap
    consumers'
  name: macos:unifiedlog
- channel: Execution of zip, ditto, hdiutil, or openssl by non-terminal parent processes
  name: macos:unifiedlog
- channel: Execution of binaries with TCC protected access under unexpected parent processes such as Finder.app, SystemUIServer,
    or nsurlsessiond
  name: macos:unifiedlog
- channel: EventCode=8003, 8004
  name: WinEventLog:AppLocker
- channel: execve, unlink
  name: auditd:SYSCALL
- channel: launchd, processes
  name: macos:osquery
- channel: socat, ssh, or nc processes opening unexpected ports
  name: linux:osquery
- channel: process execution of ssh with -L/-R forwarding flags
  name: macos:unifiedlog
- channel: launchd or cron spawning mining binaries
  name: macos:unifiedlog
- channel: execve or socket/connect system calls for processes using RSA handshake
  name: auditd:SYSCALL
- channel: Process invoking SecKeyCreateRandomKey or asymmetric crypto APIs
  name: macos:unifiedlog
- channel: Unexpected execution of cloud agent processes (e.g., WindowsAzureGuestAgent.exe, ssm-agent) followed by arbitrary
    script or binary execution
  name: azure:vmguest
- channel: Script interpreter invoked by nginx/apache worker process
  name: macos:unifiedlog
- channel: execution of Office binaries with network activity
  name: macos:unifiedlog
- channel: launch of bash/zsh/python/osascript targeting key file locations
  name: macos:unifiedlog
- channel: execution of /sbin/emond with child processes launched
  name: macos:unifiedlog
- channel: 'provider: ETW CreateProcess events linking msbuild.exe to suspicious children where standard logs are incomplete'
  name: etw:Microsoft-Windows-Kernel-Process
- channel: shutdown -h now or reboot
  name: macos:unifiedlog
- channel: Execution of Code.app, idea, JetBrainsToolbox, eclipse with install/extension flags
  name: macos:unifiedlog
- channel: process execution events for system discovery utilities (system_profiler, sysctl, networksetup, ioreg) with parameter
    analysis
  name: macos:unifiedlog
- channel: BSM audit events for process execution and system call monitoring during reconnaissance
  name: OpenBSM:AuditTrail
- channel: host daemon events related to VM operations and configuration queries during reconnaissance
  name: esxi:hostd
- channel: VMware kernel events for hardware and system configuration access during environmental validation
  name: esxi:vmkernel
- channel: processes modifying environment variables related to history logging
  name: linux:osquery
- channel: 'execve: parent process is usb/hid device handler, child process bash/python invoked'
  name: auditd:SYSCALL
- channel: execution of curl, rclone, or Office apps invoking network sessions
  name: macos:unifiedlog
- channel: 'exec: Execution of kextstat, kextfind, or ioreg targeting driver information'
  name: macos:unifiedlog
- channel: exec events
  name: macos:endpointsecurity
- channel: Process creation involving binaries interacting with resource fork data
  name: macos:unifiedlog
- channel: process event
  name: macos:unifiedlog
- channel: 'execve: Execution of suspicious exploit binaries targeting security daemons'
  name: auditd:SYSCALL
- channel: 'execve: Unsigned or unnotarized processes launched with high privileges'
  name: macos:osquery
- channel: security OR injection attempts into 1Password OR LastPass
  name: macos:unifiedlog
- channel: init or zygote process executing scripts or binaries from non-standard data or sdcard locations during early boot
  name: AndroidLogs:Kernel
- channel: launchd invocation of binary from non-Apple, non-AppStore, or sideloaded location during boot or shortly after
    unlock
  name: iOS:unifiedlog
- channel: Creation of a new process running as system or root UID whose executable path resides under an app container path
    (for example, /data/app or /data/user/0/<pkg>), or whose parent process originates from an app sandbox
  name: AndroidLogs:Framework
- channel: Creation of a new process with elevated UID or sensitive entitlements whose binary path is associated with an app
    container or whose parent/caller is a low-privileged app/webcontent process
  name: iOS:unifiedlog
- channel: dlopen of a recently created .so OR short-lived child (/system/bin/sh,toybox,linker) spawned by app_process
  name: android:logcat
- channel: startActivity on top of <target_pkg> (launchMode/singleTop), task switch immediately after focus
  name: android:logcat
- channel: unexpected spikes in fork/exec/app process start events for helper utilities used for enumeration (ps, toybox/toolbox
    variants) from same UID
  name: android:logcat
- channel: Application writes audio buffer or recorded audio file into application storage directories
  name: MobileEDR:telemetry
- channel: Browser or WebView-hosting application brought to foreground and navigates to external content, followed by abnormal
    state transition, crash, restart, or process spawn behavior
  name: MobileEDR:telemetry
- channel: application installed from adb, sideload, or unknown USB source
  name: MobileEDR:telemetry
- channel: Application invokes Runtime.exec, ProcessBuilder, JNI-backed command launcher, or equivalent command-execution
    bridge immediately before shell or command process creation
  name: MobileEDR:telemetry
- channel: Managed app invokes lower-level OS process-launch or command-execution behavior before file or network effects,
    including interpreter-like execution flow where visible to sensor
  name: MobileEDR:telemetry
- channel: application execution triggered with unexpected parent context or via indirect invocation (intent redirection or
    component hijack)
  name: MobileEDR:telemetry
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
