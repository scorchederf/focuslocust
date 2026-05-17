---
parsed_by: focuslocust
source: mitre
type: generated
---
# File Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0061` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [File Modification](../../attack/data-sources/DC0061-file-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0061 |
| name | File Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0061 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to a file, including updates to its contents, metadata, access permissions, or attributes. These\
  \ modifications may indicate legitimate activity (e.g., software updates) or unauthorized changes (e.g., tampering, ransomware,\
  \ or adversarial modifications). Examples: \n\n- Content Modifications: Changes to the content of a configuration file,\
  \ such as modifying `/etc/ssh/sshd_config` on Linux or `C:\\Windows\\System32\\drivers\\etc\\hosts` on Windows.\n- Permission\
  \ Changes: Altering file permissions to allow broader access, such as changing a file from `644` to `777` on Linux or modifying\
  \ NTFS permissions on Windows.\n- Attribute Modifications: Changing a file's attributes to hidden, read-only, or system\
  \ on Windows.\n- Timestamp Manipulation: Adjusting a file's creation or modification timestamp using tools like `touch`\
  \ in Linux or timestomping tools on Windows.\n- Software or System File Changes: Modifying system files such as `boot.ini`,\
  \ kernel modules, or application binaries."
external_references:
- external_id: DC0061
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0061
id: x-mitre-data-component--84572de3-9583-4c73-aabd-06ea88123dd8
modified: '2026-04-16T16:41:53.549Z'
name: File Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- enterprise-attack
- mobile-attack
x_mitre_log_sources:
- channel: None
  name: File
- channel: open/write calls modifying ~/.bashrc, ~/.profile, or /etc/paths.d
  name: auditd:SYSCALL
- channel: File modification in /etc/paths.d or user shell rc files
  name: macos:unifiedlog
- channel: /var/log/quarantine.log
  name: fs:fileevents
- channel: Modification of ~/Library/LaunchAgents or /Library/LaunchDaemons plist
  name: macos:unifiedlog
- channel: open, write
  name: auditd:SYSCALL
- channel: AUDIT_SYSCALL (open, write, rename, unlink)
  name: auditd:SYSCALL
- channel: ES_EVENT_TYPE_NOTIFY_WRITE, targeting .zshrc, .zlogin, .zprofile
  name: macos:endpointsecurity
- channel: /var/log/install.log
  name: fs:fileevents
- channel: PATH
  name: auditd:SYSCALL
- channel: file_events
  name: macos:osquery
- channel: EventCode=2
  name: WinEventLog:Sysmon
- channel: execve call for modification of /etc/sudoers or writing to /var/db/sudo
  name: auditd:SYSCALL
- channel: 'open, write: File modifications under /etc/ssl/certs, /usr/local/share/ca-certificates, or /etc/pki/ca-trust/source/anchors'
  name: auditd:SYSCALL
- channel: 'query: Enumeration of root certificates showing unexpected additions'
  name: macos:osquery
- channel: 'open, unlink, rename: Suspicious file access, deletion, or modification of sensitive paths'
  name: auditd:SYSCALL
- channel: Anomalous plist modifications or sensitive file overwrites by non-standard processes
  name: macos:unifiedlog
- channel: Modification or deletion of /etc/audit/audit.rules or /etc/audit/audit.conf
  name: auditd:FILE
- channel: open/write of .service unit files
  name: auditd:SYSCALL
- channel: open/write/unlink
  name: auditd:SYSCALL
- channel: loginwindow or desktopservices modified settings or files
  name: macos:unifiedlog
- channel: changes to /etc/motd or /etc/vmware/welcome
  name: ESXiLogs:messages
- channel: write, rename
  name: auditd:SYSCALL
- channel: file change monitoring within /etc/cron.*, /tmp, or mounted volumes
  name: containerd:runtime
- channel: manual edits to /etc/rc.local.d/local.sh or cron.d
  name: esxi:cron
- channel: /etc/passwd or /etc/group file write
  name: auditd:PATH
- channel: write
  name: auditd:SYSCALL
- channel: SecurityAgentPlugins modification
  name: macos:unifiedlog
- channel: 'write: File modifications to *.plist within LaunchAgents, LaunchDaemons, Application Support, or Preferences directories'
  name: macos:unifiedlog
- channel: file_events
  name: linux:osquery
- channel: boot
  name: esxi:hostd
- channel: config
  name: networkdevice:syslog
- channel: Modification of backgrounditems.btm or creation of LoginItems subdirectory in .app bundle
  name: macos:unifiedlog
- channel: Modification or creation of files matching 'com.apple.loginwindow.*.plist' in ~/Library/Preferences/ByHost
  name: fs:filesystem
- channel: write | PATH=/home/*/.ssh/authorized_keys
  name: auditd:SYSCALL
- channel: ~/.ssh/authorized_keys
  name: macos:auth
- channel: compute.instances.setMetadata
  name: gcp:audit
- channel: PATCH vm/authorized_keys
  name: azure:resource
- channel: file write or edit
  name: esxi:shell
- channel: rename
  name: linux:syslog
- channel: file_write
  name: ebpf:syscalls
- channel: Modification of plist with apple.awt.UIElement set to TRUE
  name: macos:unifiedlog
- channel: unlink, write
  name: fs:fsusage
- channel: 'open, write: Write operations targeting /dev/sda, /dev/nvme0n1, or EFI partition mounts'
  name: auditd:SYSCALL
- channel: 'write: Modification of /boot/grub/*, /boot/efi/EFI/*, or initramfs images'
  name: auditd:PATH
- channel: 'config-change: timezone or ntp server configuration change after a time query command'
  name: networkdevice:config
- channel: replace existing dylibs
  name: macos:unifiedlog
- channel: Configuration changes to boot variables, startup image paths, or checksum verification failures
  name: networkdevice:config
- channel: Unexpected or unscheduled firmware updates, image overwrites, or failed signature validation
  name: firmware:update
- channel: Checksum or hash mismatch between running image and known-good vendor-provided image
  name: IntegrityCheck:ImageValidation
- channel: File modifications in ~/Library/Preferences/
  name: macos:osquery
- channel: open/write to /etc/pam.d/*
  name: auditd:SYSCALL
- channel: Modification of /Library/Security/SecurityAgentPlugins
  name: macos:unifiedlog
- channel: Modifications to Mail.app plist files controlling message rules
  name: macos:unifiedlog
- channel: EventCode=4663, 4670, 4656
  name: WinEventLog:Security
- channel: 'write: Modification of structured stored data by suspicious processes'
  name: auditd:SYSCALL
- channel: Unexpected log entries or malformed SQL operations in databases
  name: linux:syslog
- channel: Unexpected creation or modification of stored data files in protected directories
  name: macos:unifiedlog
- channel: openat, write, rename, unlink
  name: auditd:SYSCALL
- channel: file encrypted|new file with .encrypted extension|disk write burst
  name: macos:unifiedlog
- channel: rename .vmdk to .*.locked|datastore write spike
  name: esxi:vmkernel
- channel: Mach-O binary modified or LC_LOAD_DYLIB segment inserted
  name: macos:unifiedlog
- channel: open/write syscalls targeting /etc/ld.so.preload or binaries in /usr/bin
  name: auditd:SYSCALL
- channel: Modified application plist or binary replacement in /Applications
  name: macos:unifiedlog
- channel: admin command usage
  name: esxi:shell
- channel: startup-config
  name: networkdevice:syslog
- channel: File creation or overwrite in common web-hosting folders
  name: macos:unifiedlog
- channel: Unauthorized file modifications within datastore volumes via shell access or vCLI
  name: esxi:vmkernel
- channel: Configuration changes referencing 'crypto', 'key length', 'cipher', or downgrade of encryption settings
  name: networkdevice:config
- channel: Unexpected firmware or image updates modifying cryptographic modules
  name: FirmwareLogs:Update
- channel: /var/root/Library/Preferences/com.apple.loginwindow.plist
  name: fs:plist
- channel: modification of existing .service file
  name: auditd:SYSCALL
- channel: write or create events on *.pth, sitecustomize.py, usercustomize.py in site-packages or dist-packages
  name: auditd:PATH
- channel: write of plist files in /Library/LaunchAgents or /Library/LaunchDaemons
  name: macos:unifiedlog
- channel: Unexpected modification to lsass.exe or cryptdll.dll
  name: WinEventLog:System
- channel: unexpected OS image file upload or modification events
  name: networkconfig
- channel: checksum or runtime memory verification failures
  name: network:runtime
- channel: write
  name: macos:unifiedlog
- channel: 'open, write: Modification of /boot/grub/* or /boot/efi/*'
  name: auditd:SYSCALL
- channel: Modification of /System/Library/CoreServices/boot.efi
  name: macos:unifiedlog
- channel: Modification of LaunchAgents or LaunchDaemons plist files
  name: macos:unifiedlog
- channel: chmod
  name: auditd:SYSCALL
- channel: rename,chmod
  name: auditd:SYSCALL
- channel: create/write/rename under user-writable paths
  name: fs:fsevents
- channel: Changes to LSFileQuarantineEnabled field in Info.plist
  name: macos:osquery
- channel: file access to /usr/lib/cron/tabs/ and cron output files
  name: fs:fsusage
- channel: modification of crontab or local.sh entries
  name: esxi:hostd
- channel: Configuration file modified or replaced on network device
  name: networkdevice:config
- channel: Plist modifications containing virtualization run configurations
  name: macos:unifiedlog
- channel: file access to /usr/lib/cron/at and job execution path
  name: fs:fsusage
- channel: binary modified or replaced
  name: macos:unifiedlog
- channel: binary or module replacement event
  name: esxi:hostd
- channel: Configuration change events referencing encryption, TLS/SSL, or IPSec settings
  name: networkdevice:config
- channel: Unexpected firmware update or image modification affecting crypto modules
  name: networkdevice:firmware
- channel: file system events indicating permission, ownership, or extended attribute changes on critical paths. File system
    modification events with kFSEventStreamEventFlagItemChangeOwner, kFSEventStreamEventFlagItemXattrMod flags
  name: fs:fsevents
- channel: Modification of Display Manager configuration files (/etc/gdm3/*, /etc/lightdm/*)
  name: auditd:FILE
- channel: Modification of /Library/Preferences/com.apple.loginwindow plist
  name: macos:unifiedlog
- channel: Modification of user shell profile or trap registration via echo/redirection (e.g., echo "trap 'malicious_cmd'
    INT" >> ~/.bashrc)
  name: auditd:SYSCALL
- channel: File write or append to .zshrc, .bash_profile, .zprofile, etc.
  name: macos:unifiedlog
- channel: chmod, write, create, open
  name: auditd:SYSCALL
- channel: Extensions
  name: fs:fsevents
- channel: 'open, write: File writes to application binaries or libraries at runtime'
  name: auditd:SYSCALL
- channel: 'CALCULATE: Mismatch in file integrity of critical macOS applications'
  name: macos:osquery
- channel: file write operations in /Library/WebServer/Documents
  name: auditd:SYSCALL
- channel: file_modify
  name: fs:launchdaemons
- channel: 'write: File modifications to /etc/systemd/sleep.conf or related power configuration files'
  name: auditd:PATH
- channel: 'write: File modification to com.apple.PowerManagement.plist or related system preference files'
  name: macos:unifiedlog
- channel: modification of existing LaunchAgents plist
  name: fs:fsusage
- channel: create/modify dylib in monitored directories
  name: macos:unifiedlog
- channel: EventCode=3033
  name: WinEventLog:CodeIntegrity
- channel: write operation on /etc/passwd or /etc/shadow
  name: auditd:SYSCALL
- channel: modification to /var/db/dslocal/nodes/Default/users/
  name: macos:unifiedlog
- channel: New or modified kernel object files (.ko) within /lib/modules directory
  name: linux:osquery
- channel: Modifications to /var/db/SystemPolicyConfiguration/KextPolicy or kext_policy table
  name: macos:osquery
- channel: SNMP configuration changes, such as enabling read/write access or modifying community strings
  name: networkdevice:audit
- channel: write
  name: macos:osquery
- channel: mount or losetup commands creating hidden or encrypted FS
  name: auditd:SYSCALL
- channel: Hidden volume attachment or modification events
  name: macos:unifiedlog
- channel: Suspicious plist edits for volume mounting behavior
  name: macos:unifiedlog
- channel: Configuration changes to startup image paths, boot loader parameters, or debug flags
  name: networkdevice:config
- channel: Checksum/hash mismatch between device OS image and baseline known-good version
  name: networkdevice:syslog
- channel: file writes
  name: macos:unifiedlog
- channel: OfficeTelemetry or DLP
  name: m365:defender
- channel: Filesystem Access Logging
  name: fs:fsusage
- channel: Configuration changes referencing cryptographic hardware modules or disabling hardware acceleration
  name: networkdevice:config
- channel: Unexpected firmware updates that alter encryption libraries or disable hardware crypto modules
  name: FirmwareLogs:Update
- channel: Anomalous editing of invoice or payment document templates
  name: m365:office
- channel: truncate, unlink, write
  name: fs:fsusage
- channel: Modification or replacement of /Library/Application Support/com.apple.TCC/TCC.db or ~/Library/Application Support/com.apple.TCC/TCC.db
  name: macos:unifiedlog
- channel: Changes to /etc/rc.local.d/local.sh or creation of unexpected startup files in persistent partitions (/etc/init.d,
    /store, /locker)
  name: linux:fim
- channel: write, rename
  name: macos:endpointsecurity
- channel: open/write to /proc/*/mem or /proc/*/maps
  name: auditd:SYSCALL
- channel: evt.type=write
  name: sysdig:file
- channel: rule definitions written to emond rule plists
  name: macos:unifiedlog
- channel: Configuration changes referencing older image versions or unexpected boot parameters
  name: networkdevice:config
- channel: Hash/checksum mismatch against baseline vendor-provided OS image versions
  name: FileIntegrity:ImageValidation
- channel: write or rename to /etc/systemd/system or /etc/init.d
  name: auditd:SYSCALL
- channel: file write to launchd plist paths
  name: fs:fsusage
- channel: modification of entrypoint scripts or init containers
  name: auditd:SYSCALL
- channel: /Users/*/Library/Mail/V*/MailData/RulesActiveState.plist
  name: fs:plist_monitoring
- channel: chmod/chown to /etc/passwd or /etc/shadow
  name: auditd:SYSCALL
- channel: open/write syscalls targeting web directory files
  name: auditd:SYSCALL
- channel: Terminal/Editor processes modifying web folder
  name: macos:unifiedlog
- channel: /var/log/vmkernel.log
  name: esxi:vmkernel
- channel: Modification to /system/etc/init/ or /vendor/etc/init/ boot-time scripts
  name: AndroidLogs:FileSystem
- channel: Creation or modification of LaunchDaemon or LaunchAgent plist in /System/Library/LaunchDaemons, /Library/LaunchDaemons,
    or /Library/LaunchAgents
  name: iOS:unifiedlog
- channel: INSERT or UPDATE of image/*, audio/*, video/* via ContentResolver with same URI re-written within short window;
    abnormal MIME/container change
  name: android:logcat
- channel: Application inserts, updates, deletes, hides, or marks message records in SMS store or messaging database immediately
    after SMS receive or send event
  name: MobileEDR:telemetry
- channel: Application inserts, updates, deletes, or rewrites call-log records immediately after call-control action to conceal,
    alter, or synthesize call history
  name: MobileEDR:telemetry
- channel: odification of ~/.ssh/authorized_keys or credential files
  name: auditd:PATH
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '3.0'
```
