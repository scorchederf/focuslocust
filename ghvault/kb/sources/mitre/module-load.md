---
parsed_by: focuslocust
source: mitre
type: generated
---
# Module Load

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0016` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Module Load](../../attack/data-sources/DC0016-module-load.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0016 |
| name | Module Load |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0016 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.272Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: When a process or program dynamically attaches a shared library, module, or plugin into its memory space. This
  action is typically performed to extend the functionality of an application, access shared system resources, or interact
  with kernel-mode components.
external_references:
- external_id: DC0016
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0016
id: x-mitre-data-component--c0a4a086-cc20-4e1e-b7cb-29d99dfa3fb1
modified: '2026-01-29T17:21:27.873Z'
name: Module Load
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
  name: Module
- channel: EventCode=7
  name: WinEventLog:Sysmon
- channel: 'provider: ETW LoadImage events for images from user-writable/UNC paths'
  name: ETW:LoadImage
- channel: 'openat/read/mmap: Open/mmap .so files from non-standard paths'
  name: auditd:SYSCALL
- channel: 'select: Open files path LIKE ''/tmp/%.so'' OR ''/dev/shm/%.so'''
  name: linux:osquery
- channel: dyld/unified log entries indicating image load from non-system paths
  name: macos:unifiedlog
- channel: 'select: path LIKE ''%/Library/%/*.dylib'' OR ''/tmp/*.dylib'''
  name: macos:osquery
- channel: dynamic loading of sleep-related functions or sandbox detection libraries
  name: macos:unifiedlog
- channel: LD_PRELOAD Logging
  name: auditd:SYSCALL
- channel: Dynamic Linking State
  name: linux:osquery
- channel: DYLD event subsystem
  name: macos:unifiedlog
- channel: Process linked with libcrypto.so making external connections
  name: linux:osquery
- channel: process execution events with dylib load activity
  name: macos:unifiedlog
- channel: EventCode=7
  name: linux:Sysmon
- channel: CLR Assembly creation, loading, or modification logs via MSSQL CLR integration
  name: WinEventLog:Application
- channel: Process memory maps new dylib (dylib_load event)
  name: macos:unifiedlog
- channel: Dylib loaded from abnormal location
  name: macos:unifiedlog
- channel: EventCode=3033
  name: WinEventLog:Security
- channel: EventCode=3063
  name: WinEventLog:Security
- channel: 'load: Loading of libzip.so, libz.so, or libbz2.so by processes not normally associated with archiving'
  name: auditd:MMAP
- channel: Loading of libz.dylib, libarchive.dylib by non-standard applications
  name: macos:unifiedlog
- channel: suspicious dlopen/dlsym usage in non-development processes
  name: macos:unifiedlog
- channel: Non-standard Office startup component detected (e.g., unexpected DLL path)
  name: m365:unified
- channel: mmap
  name: auditd:SYSCALL
- channel: unexpected module load
  name: esxi:vmkernel
- channel: Status change in cryptographic hardware modules (enabled -> disabled)
  name: snmp:status
- channel: module load
  name: esxi:vmkernel
- channel: delay/sleep library usage in user context
  name: macos:unifiedlog
- channel: kmod
  name: linux:syslog
- channel: subsystem=com.apple.kextd
  name: macos:unifiedlog
- channel: loading of unexpected dylibs compared to historical baselines
  name: macos:unifiedlog
- channel: open of suspicious .so from non-standard paths
  name: auditd:file-events
- channel: DYLD_INSERT_LIBRARIES anomalies
  name: macos:syslog
- channel: dmesg
  name: auditd:SYSCALL
- channel: ES_EVENT_TYPE_NOTIFY_KEXTLOAD
  name: macos:endpointsecurity
- channel: module load or memory map path
  name: auditd:SYSCALL
- channel: launch and dylib load
  name: macos:unifiedlog
- channel: Processes linked with libssl/libcrypto performing network activity
  name: linux:osquery
- channel: 'provider: Unsigned/user-writable image loads into msbuild.exe'
  name: etw:Microsoft-Windows-Kernel-ImageLoad
- channel: DexClassLoader/PathClassLoader load attempt from non-standard path or recently created file
  name: android:logcat
- channel: Short burst of file I/O followed by JNI/dlopen of a newly created .so
  name: android:logcat
- channel: 'dyld: dlopen/dyld_cache load from non-standard app-writable path'
  name: iOS:unifiedlog
- channel: DexClassLoader/PathClassLoader loading from app-writable path OR reflective defineClass on byte[] payload
  name: android:logcat
- channel: dlopen/image load from app-writable path (tmp, Caches) outside bundled resources
  name: iOS:unifiedlog
- channel: DexClassLoader|PathClassLoader load from app-writable path OR dlopen of a freshly created .so
  name: android:logcat
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '3.0'
```
