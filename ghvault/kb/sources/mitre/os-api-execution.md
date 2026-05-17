---
parsed_by: focuslocust
source: mitre
type: generated
---
# OS API Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0021` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [OS API Execution](../../attack/data-sources/DC0021-os-api-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0021 |
| name | OS API Execution |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0021 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Calls made by a process to operating system-provided Application Programming Interfaces (APIs). These calls are
  essential for interacting with system resources such as memory, files, and hardware, or for performing system-level tasks.
  Monitoring these calls can provide insight into a process's intent, especially if the process is malicious.
external_references:
- external_id: DC0021
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0021
id: x-mitre-data-component--9bde2f9d-a695-4344-bfac-f2dce13d121e
modified: '2026-04-23T18:22:40.476Z'
name: OS API Execution
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
- channel: GetLocaleInfoW, GetTimeZoneInformation API calls
  name: etw:Microsoft-Windows-Kernel-Base
- channel: GetMetadata, DescribeInstanceIdentity
  name: AWS:CloudTrail
- channel: 'open, execve: Unexpected processes accessing or modifying critical files'
  name: macos:osquery
- channel: ptrace, ioctl
  name: auditd:SYSCALL
- channel: API tracing / stack tracing via ETW or telemetry-based EDR
  name: etw:Microsoft-Windows-Kernel-Process
- channel: Behavioral API telemetry (GetProcAddress, LoadLibrary, VirtualAlloc)
  name: EDR:memory
- channel: aaa privilege_exec
  name: networkdevice:syslog
- channel: None
  name: macos:unifiedlog
- channel: APCQueueOperations
  name: etw:Microsoft-Windows-Kernel-Process
- channel: Invocation of SMLoginItemSetEnabled by non-system or recently installed application
  name: macos:unifiedlog
- channel: flock|NSDistributedLock|FileHandle.*lockForWriting
  name: macos:unifiedlog
- channel: 'api_call: Calls to DsAddSidHistory or related RPC operations'
  name: etw:Microsoft-Windows-Directory-Services-SAM
- channel: application logs referencing NSTimer, sleep, or launchd delays
  name: macos:unifiedlog
- channel: High-frequency or suspicious sequence of QueryPerformanceCounter/GetTickCount API calls from a non-standard process
    lineage
  name: etw:Microsoft-Windows-Kernel-Process
- channel: Rules capturing clock_gettime, time, gettimeofday syscalls when enabled
  name: auditd:SYSCALL
- channel: Unexpected reload, crashinfo, or boot message not tied to scheduled maintenance
  name: networkdevice:syslog
- channel: 'rpc_call: srvsvc.NetShareEnum / NetShareEnumAll from non-admin or unusual processes'
  name: etw:Microsoft-Windows-RPC
- channel: 'smb_command: TreeConnectAndX to \\*\IPC$ / srvsvc or Trans2/NT_CREATE for listing shares'
  name: NSM:Flow
- channel: EventCode=4663, 4670, 4656
  name: WinEventLog:Security
- channel: API usage MFCreateDeviceSource, IAMStreamConfig, ICaptureGraphBuilder2, DirectShow filter graph creation from uncommon
    callers
  name: EDR:memory
- channel: 'openat/read/ioctl: openat/read/ioctl on /dev/video* by uncommon user/process'
  name: auditd:SYSCALL
- channel: Access decisions to kTCCServiceCamera for unexpected binaries
  name: macos:unifiedlog
- channel: Objective‑C/Swift calls to AVCaptureDevice/AVCaptureSession by non-whitelisted processes
  name: EDR:memory
- channel: mmap, ptrace, process_vm_writev or direct memory ops
  name: auditd:SYSCALL
- channel: API call to AddMonitor invoked by non-installer process
  name: WinEventLog:Application
- channel: SetWindowLong, SetClassLong, NtUserMessageCall, SendNotifyMessage, PostMessage
  name: etw:Microsoft-Windows-Win32k
- channel: unshare, mount, keyctl, setns syscalls executed by containerized processes
  name: auditd:SYSCALL
- channel: audio APIs
  name: macos:unifiedlog
- channel: CLSID activation events where ProcessName=mmc.exe and CLSID not in allowed baseline
  name: WinEventLog:Microsoft-Windows-COM/Operational
- channel: com.apple.securityd, com.apple.tccd
  name: macos:unifiedlog
- channel: 'send, recv, write: Abnormal interception or alteration of transmitted data'
  name: auditd:SYSCALL
- channel: 'CALCULATE: Integrity validation of transmitted data via hash checks'
  name: macos:osquery
- channel: 'token_analysis: API calls such as DuplicateTokenEx or ImpersonateLoggedOnUser'
  name: ETW:Token
- channel: API Calls
  name: etw:Microsoft-Windows-Kernel-Process
- channel: AssemblyLoad/ModuleLoad (Loader keyword) from Microsoft-Windows-DotNETRuntime
  name: etw:Microsoft-Windows-DotNETRuntime
- channel: VirtualAlloc/VirtualProtect/MapViewOfFile indicators via stack/heap activity and ImageLoad
  name: EDR:memory
- channel: memory region with RWX permissions allocated
  name: auditd:MMAP
- channel: management queries
  name: snmp:trap
- channel: Describe* or List* API calls
  name: AWS:CloudTrail
- channel: SendMessage, PostMessage, LVM_*
  name: etw:Microsoft-Windows-Win32k
- channel: sudo or pkexec invocation
  name: auditd:SYSCALL
- channel: authorization execute privilege requests
  name: macos:unifiedlog
- channel: NtQueryInformationProcess
  name: etw:Microsoft-Windows-Kernel-Process
- channel: 'ptrace: Processes invoking ptrace with PTRACE_TRACEME flag'
  name: macos:unifiedlog
- channel: Remote access API calls and file uploads
  name: esxi:hostd
- channel: NtUnmapViewOfSection, VirtualAllocEx, WriteProcessMemory, SetThreadContext, ResumeThread
  name: etw:Microsoft-Windows-Kernel-Process
- channel: Execution of modified binaries or abnormal library load sequences
  name: linux:syslog
- channel: Calls to AuthorizationExecuteWithPrivileges() observed via Apple System Logger or security_auditing tools
  name: macos:unifiedlog
- channel: access or unlock attempt to keychain database
  name: macos:unifiedlog
- channel: Execution of input detection APIs (e.g., CGEventSourceKeyState)
  name: macos:unifiedlog
- channel: mount system call with bind or remap flags
  name: auditd:SYSCALL
- channel: Decrypt
  name: AWS:CloudTrail
- channel: ZwSetEaFile or ZwQueryEaFile function calls
  name: etw:Microsoft-Windows-Kernel-File
- channel: fork/clone/daemon syscall tracing
  name: auditd:SYSCALL
- channel: Detached process execution with no associated parent
  name: fs:fsusage
- channel: ptrace, mmap, mprotect, open, dlopen
  name: auditd:SYSCALL
- channel: 'api_call: CreateProcessWithTokenW, CreateProcessAsUserW'
  name: ETW:ProcThread
- channel: MemoryWriteToExecutable
  name: EDR:memory
- channel: 'api_call: DuplicateTokenEx, ImpersonateLoggedOnUser, SetThreadToken'
  name: ETW:Token
- channel: 'api_call: UpdateProcThreadAttribute (PROC_THREAD_ATTRIBUTE_PARENT_PROCESS) and CreateProcess* with EXTENDED_STARTUPINFO_PRESENT
    / StartupInfoEx'
  name: etw:Microsoft-Windows-Kernel-Process
- channel: 'api_call: LogonUser(A|W), LsaLogonUser, SetThreadToken, ImpersonateLoggedOnUser'
  name: etw:Microsoft-Windows-Security-Auditing
- channel: API calls
  name: etw:Microsoft-Windows-Kernel-Process
- channel: ptrace, mmap, process_vm_writev
  name: auditd:SYSCALL
- channel: execve of dd or sed targeting /proc/*/mem
  name: auditd:SYSCALL
- channel: CreateTransaction, CreateFileTransacted, RollbackTransaction, NtCreateProcessEx, NtCreateThreadEx
  name: etw:Microsoft-Windows-Kernel-Process
- channel: Calls to GetUserDefaultUILanguage, GetSystemDefaultUILanguage, GetKeyboardLayoutList
  name: ETW
- channel: 'WriteProcessMemory: WriteProcessMemory targeting regions containing KernelCallbackTable addresses'
  name: etw:Microsoft-Windows-Kernel-Process
- channel: SetFileTime
  name: EDR:file
- channel: Unprivileged app process (app UID, non-system) invoking sensitive syscalls or device interfaces associated with
    privilege escalation (setuid, ptrace, perf_event_open, vulnerable drivers)
  name: AndroidLogs:Kernel
- channel: SELinux AVC for execmem/execute_no_trans/mprotect following recent writes by same UID
  name: android:logcat
- channel: mmap/mprotect transitions to PROT_EXEC for pages associated with recently written files
  name: iOS:unifiedlog
- channel: QUERY on exported ContentProviders of other packages (content://<other.pkg>/*) or MediaStore scoped queries immediately
    preceding file reads
  name: android:logcat
- channel: ClipboardManager (addOnPrimaryClipChangedListener|getPrimaryClip|getPrimaryClipDescription) invoked by <pkg>
  name: android:logcat
- channel: AccessibilityService connected|TYPE_VIEW_TEXT_CHANGED|TYPE_VIEW_FOCUSED events for other packages
  name: android:logcat
- channel: TYPE_WINDOW_STATE_CHANGED / TYPE_VIEW_FOCUSED shows foreign target package in foreground
  name: android:logcat
- channel: PackageManager getInstalledApplications|getInstalledPackages|getPackagesHoldingPermissions burst for <pkg>. TYPE_WINDOW_STATE_CHANGED
    shows foreground app then immediate package queries by <pkg>
  name: android:logcat
- channel: LSApplicationWorkspace or canOpenURL probe bursts for many URL schemes
  name: iOS:unifiedlog
- channel: getInstalledPackages/getPackagesHoldingPermissions with filters for known security/MDM/VPN package names. Queries
    to isDeviceOwnerApp/isProfileOwnerApp/getActiveAdmins/getPermissionGrantState. Requests list of enabled services or monitors
    TYPE_WINDOW_STATE_CHANGED to time checks
  name: android:logcat
- channel: Queries indicating MDM profile presence, supervised state, restrictions read. LSApplicationWorkspace enumeration
    or app proxy queries referencing security vendors
  name: iOS:unifiedlog
- channel: ACTION_VIEW redirect_uri handled by unexpected package
  name: android:logcat
- channel: canOpenURL/LSApplicationWorkspace resolved to unexpected bundle for redirect_uri
  name: android:logcat
- channel: query() against MediaStore/DocumentsContract URIs (Images/Video/Audio/Downloads/DocumentTree)
  name: android:logcat
- channel: enumeratorForContainerItemIdentifier / itemForIdentifier across multiple containers/providers
  name: iOS:unifiedlog
- channel: wifiservice startScan / scanResults retrieved repeatedly or by unexpected package
  name: android:logcat
- channel: bluetoothmanager startDiscovery / getBondedDevices / scan callback bursts by package
  name: android:logcat
- channel: telephony cell info enumeration bursts (neighboring/all cell info) by package
  name: android:logcat
- channel: repeated queries or dumps related to running tasks/services/process state by same package/UID (e.g., getRunningAppProcesses,
    running services/task inspection)
  name: android:logcat
- channel: Application accesses android.os.Build fields or device configuration APIs (MODEL, MANUFACTURER, VERSION.SDK_INT,
    HARDWARE)
  name: android:logcat
- channel: Application invokes UIDevice queries (model, systemVersion, name)
  name: iOS:unifiedlog
- channel: Invocation of MediaRecorder.start(), AudioRecord.startRecording(), or VOICE_CALL audio source
  name: android:logcat
- channel: Invocation of AVAudioRecorder, AVCaptureSession, or related audio capture framework calls
  name: iOS:unifiedlog
- channel: Application invokes LocationManager, FusedLocationProviderClient, or GPS/location sensor APIs
  name: android:logcat
- channel: Application activates CoreLocation services or CLLocationManager APIs
  name: iOS:unifiedlog
- channel: Framework-based networking usage spikes or uncommon networking stacks observed by agent telemetry (e.g., repeated
    URLSession/OkHttp-like patterns) without corresponding foreground/user interaction
  name: MobileEDR:telemetry
- channel: 'Agent-observable telephony subscription/state API signals indicating SIM/eSIM subscription change (vendor-agnostic:
    ''telephony subscription changed'')'
  name: MobileEDR:telemetry
- channel: Accessibility framework usage patterns such as event subscription, performAction invocation, node traversal, text
    change observation, or overlay/window presentation correlated to app identity
  name: MobileEDR:telemetry
- channel: Browser/WebView framework usage indicating external URL load, script execution enablement, file download initiation,
    intent handoff, or package install prompt sequence
  name: MobileEDR:telemetry
- channel: Observed device-service, trust-service, backup/service interaction, or other privileged framework activity associated
    with physical host access
  name: MobileEDR:telemetry
- channel: Connectivity manager, telephony, Wi-Fi, network callback, or location-provider framework reports repeated unavailable,
    disconnected, suspended, or degraded state transitions
  name: MobileEDR:telemetry
- channel: Observed network-path, reachability, DNS, transport, or location-provider framework reports repeated unavailable
    or failed state near active device use
  name: MobileEDR:telemetry
- channel: Content resolver, document provider, media store, storage access framework, bulk stream processing, or repeated
    crypto-adjacent framework use observed during multi-file transformation
  name: MobileEDR:telemetry
- channel: Known application begins first-seen or expanded use of content providers, account services, accessibility, package
    services, cryptographic routines, dynamic loading, or other framework interactions after update/install
  name: MobileEDR:telemetry
- channel: Known application begins first-seen or expanded use of protected frameworks, account services, background task
    APIs, crypto/network service APIs, or other runtime behaviors after update/install
  name: MobileEDR:telemetry
- channel: Known application begins first-seen or expanded use of account services, accessibility, content providers, dynamic
    loading, package services, WebView bridges, crypto/network APIs, or advertising/telemetry-adjacent framework behavior
    after install or update
  name: MobileEDR:telemetry
- channel: Privileged or OEM-context framework/API use tied to telephony, device policy, accessibility, overlay, input injection,
    package visibility, or protected settings modification from an identity not expected for the device model or approved
    image
  name: MobileEDR:telemetry
- channel: Invocation of Calendar.set() and Calendar.add()
  name: android:logcat
- channel: Supplemental anomaly in baseband, IOKit, accessory, security, or activation-related subsystem logging temporally
    adjacent to suspicious posture or network behavior
  name: iOS:unifiedlog
- channel: Recently installed or updated trusted app invokes Android framework paths or special access patterns inconsistent
    with its role, including accessibility-like behavior, overlay behavior, package visibility expansion, protected settings
    access, device policy interaction, or unusual IPC/provider access
  name: MobileEDR:telemetry
- channel: Supplemental managed app or system subsystem anomalies near install/update, launch services, extension handling,
    app activation, or background execution temporally adjacent to suspicious network or lifecycle behavior
  name: iOS:unifiedlog
- channel: App uses Android framework behaviors associated with background work scheduling, network job execution, IPC/provider
    access, overlay or accessibility-like interaction, or unusual package visibility immediately adjacent to web-service communication
  name: MobileEDR:telemetry
- channel: Supplemental launch, background task, networking, or extension-handling anomalies occur temporally adjacent to
    suspicious web-service communication from a managed app or supervised device
  name: iOS:unifiedlog
- channel: Background work scheduler, job execution, or persistent service triggered network request to public web-service
    followed by second outbound connection within TimeWindow
  name: MobileEDR:telemetry
- channel: Background task or networking subsystem event occurred immediately before resolver retrieval and pivot connection
    sequence
  name: iOS:unifiedlog
- channel: Background work scheduler, job execution, foreground-service start, or persistent service activation immediately
    preceded retrieve-then-write exchange with public web-service platform
  name: MobileEDR:telemetry
- channel: Background task, networking, or app-activation subsystem event occurred immediately before or during retrieve-then-write
    exchange with public web-service platform
  name: iOS:unifiedlog
- channel: Background work scheduler, job execution, foreground-service start, or persistent service activation immediately
    preceded outbound session using non-standard protocol-to-port pairing
  name: MobileEDR:telemetry
- channel: Invocation of CallLogs.getLastOutgoingCall()
  name: android:logcat
- channel: Invocation of ContactsContract.Contacts.getLookupUri() and/or ContactsContract.Contacts.lookupContact()
  name: android:logcat
- channel: Camera, media capture, app-activation, or background-task subsystem event occurred immediately before or during
    sustained camera session from same managed-app or device context
  name: iOS:unifiedlog
- channel: Invocation of AccountManager.getAccounts()
  name: android:logcat
- channel: MediaProjection-style screen capture session began from app identity while a different app was foregrounded and
    capture path was not mapped to approved recording workflow
  name: MobileEDR:telemetry
- channel: Accessibility-service activity from app identity coincided with foreground content observation and subsequent screenshot,
    frame buffer, or screenrecord artifact behavior within TimeWindow
  name: MobileEDR:telemetry
- channel: Privileged screencap, screenrecord, adb-driven capture, or root-context screen acquisition behavior occurred from
    app, shell, or elevated identity while foreground app context changed or sensitive app remained active
  name: MobileEDR:telemetry
- channel: Accessibility-enabled app invoked programmatic click or action on behalf of user while a different app was foregrounded
    and injected action was not mapped to approved accessibility or autofill workflow
  name: MobileEDR:telemetry
- channel: Accessibility-enabled app invoked global action such as back, home, recents, or navigation control while target
    foreground app context changed within TimeWindow
  name: MobileEDR:telemetry
- channel: Accessibility-enabled app inserted text into active field of different foreground app without user keyboard activity
    or approved autofill relationship
  name: MobileEDR:telemetry
- channel: App intercepts notification content from external package (e.g., messaging/auth apps) while in background OR without
    recent user interaction
  name: MobileEDR:telemetry
- channel: App invokes cryptographic functions (e.g., AES/RSA/KeyStore usage) on buffer data followed by encode/transform
    operations not tied to normal app workflows
  name: MobileEDR:telemetry
- channel: App invokes symmetric encryption routines (e.g., AES/RC4 cipher initialization + encrypt operations) with repeated
    key usage across multiple data buffers
  name: MobileEDR:telemetry
- channel: Symmetric key material reused across multiple encryption operations within short interval OR derived locally without
    secure hardware-backed storage
  name: MobileEDR:telemetry
- channel: App invokes asymmetric cryptographic operations (e.g., RSA/ECC keypair generation OR public key encryption OR signature
    operations) on outbound data buffers
  name: MobileEDR:telemetry
- channel: Keypair generation, import, or access events (public/private key usage) occurring prior to network communication
  name: MobileEDR:telemetry
- channel: Application invokes custom TLS trust evaluation logic or pin validation routines (e.g., custom TrustManager, HostnameVerifier
    override, certificate/public key comparison) immediately before outbound TLS session establishment
  name: MobileEDR:telemetry
- channel: Application invokes archive, compression, or bulk-buffer packaging routines on previously accessed local data within
    the same execution chain
  name: MobileEDR:telemetry
- channel: Application encrypts newly created archive or staged data blob after collection and before storage or outbound
    transfer
  name: MobileEDR:telemetry
- channel: Application performs bulk data transformation or packaging-like processing on collected records prior to file creation
    or upload
  name: MobileEDR:telemetry
- channel: Application queries or opens multiple local SQLite or app-associated database stores containing records unrelated
    to the app's declared function during the collection phase
  name: MobileEDR:telemetry
- channel: Application performs repeated record access, container traversal, or local data extraction processing against local
    stores before staging or transmission
  name: MobileEDR:telemetry
- channel: Application calls startForegroundService() or startForeground() / ServiceCompat.startForeground() and transitions
    to persistent foreground-service execution at the start of the chain
  name: MobileEDR:telemetry
- channel: Application invokes direct file retrieval, DownloadManager usage, or streaming write from network response to local
    storage immediately after remote session establishment
  name: MobileEDR:telemetry
- channel: Managed app performs post-download unpacking, dynamic resource handling, or module preparation immediately after
    local payload creation
  name: MobileEDR:telemetry
- channel: Application loads or resolves native shared library (.so) or JNI bridge immediately before suspicious native execution
    phase
  name: MobileEDR:telemetry
- channel: Application transitions from managed code into JNI/native function execution or attaches native thread to runtime
    during the execution phase
  name: MobileEDR:telemetry
- channel: Existing application is replaced, updated, or reinstalled and the resulting package metadata, code sections, or
    executable-supporting artifacts diverge from known-good baseline during the persistence-establishment phase
  name: MobileEDR:telemetry
- channel: Application invokes SMS send, intercept, delete, or provider-write behavior, including handling SMS_DELIVER or
    interacting with SMS content provider during unauthorized message-control phase
  name: MobileEDR:telemetry
- channel: Application enqueues WorkManager work request or schedules JobScheduler or AlarmManager task with delay, periodic
    interval, or execution constraints during the persistence/execution setup phase
  name: MobileEDR:telemetry
- channel: Application creates or executes NSBackgroundActivityScheduler activity with repeating or deferred invocation semantics
    during the scheduling and trigger phases
  name: MobileEDR:telemetry
- channel: Application initializes proxy-capable or raw-socket networking constructs, including SOCKS-capable Proxy API usage
    or direct socket listener/setup immediately before traffic relay phase
  name: MobileEDR:telemetry
- channel: Application invokes call placement, answer, redirect, block, screening, or ConnectionService call-handling APIs
    during unauthorized call-control phase
  name: MobileEDR:telemetry
- channel: application process loads external code modules or injects into runtime (zygote/app_process) + abnormal library
    loading or method interception behavior
  name: MobileEDR:telemetry
- channel: Application registers broadcast receiver, WorkManager job, JobScheduler task, or intent filter tied to system event
    such as BOOT_COMPLETED, SMS_RECEIVED, CONNECTIVITY_CHANGE during persistence setup phase
  name: MobileEDR:telemetry
- channel: application registers or invokes broadcast receiver via registerReceiver() or manifest-declared receiver + intent
    filter tied to system or app events
  name: MobileEDR:telemetry
- channel: application launches or executes code where loaded library or component path does not match application package
    path or expected signing context
  name: MobileEDR:telemetry
- channel: multiple applications invoking core system APIs (e.g., sensor, permission, telephony) with abnormal or inconsistent
    return values across apps within short interval
  name: MobileEDR:telemetry
- channel: device integrity degradation + root detected or system partition modification affecting runtime libraries (e.g.,
    /system/lib*, /vendor/lib*)
  name: MobileEDR:telemetry
- channel: application invokes privileged framework APIs (Accessibility events, UI automation, package install flows) immediately
    following permission grant
  name: MobileEDR:telemetry
- channel: application invokes DevicePolicyManager APIs (e.g., resetPassword, lockNow, setCameraDisabled) immediately following
    admin activation
  name: MobileEDR:telemetry
- channel: application queries target-selection attributes (e.g., location, SIM/operator, locale, device state, network identity)
    and then conditionally invokes sensitive framework APIs only after expected value is observed
  name: MobileEDR:telemetry
- channel: application exhibits repeated environment-context evaluation followed by delayed privileged framework use only
    after target-specific match
  name: MobileEDR:telemetry
- channel: application invokes geolocation or geofencing framework operations (e.g., location polling or geofence registration/evaluation)
    and sensitive framework activity begins only after region match or location threshold condition
  name: MobileEDR:telemetry
- channel: application exhibits repeated location-context evaluation followed by delayed privileged framework use or feature
    activation only after target region match
  name: MobileEDR:telemetry
- channel: application invokes package or component state changes affecting launcher-facing activity availability and subsequently
    continues operational framework activity after icon suppression
  name: MobileEDR:telemetry
- channel: application invokes motion-sensor or device-activity framework operations followed by conditional execution of
    sensitive framework activity only after inferred user absence
  name: MobileEDR:telemetry
- channel: application invokes system framework operations that alter monitoring, accessibility, or execution visibility followed
    by reduction in expected telemetry generation
  name: MobileEDR:telemetry
- channel: application invokes accessibility global actions (back/home/recents) or observes package-management UI immediately
    after uninstall/settings screen becomes foreground
  name: MobileEDR:telemetry
- channel: application invokes lock-related or UI-denial framework operations, including DevicePolicyManager lock actions,
    persistent overlay behavior, or accessibility-driven navigation interference immediately before device enters locked or
    unusable state
  name: MobileEDR:telemetry
- channel: application invokes package, settings, or privileged framework operations capable of disabling security software,
    altering security enforcement, or interfering with reporting before telemetry loss
  name: MobileEDR:telemetry
- channel: application invokes uninstall-related package-management operations, accessibility-driven uninstall confirmation
    actions, or privileged file-removal operations immediately before installed-state loss
  name: MobileEDR:telemetry
- channel: application invokes file-management, package, storage, or administrative wipe operations immediately before loss
    of expected local files or file collections
  name: MobileEDR:telemetry
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
