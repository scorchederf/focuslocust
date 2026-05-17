---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Endpoint Detection and Response

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-evasion-edr-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/edr-bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Endpoint Detection and Response (EDR) is a security solution that combines real-time monitoring, data collection, and advanced analytics to detect, investigate, and respond to cyber threats at the endpoint level. Leveraging machine learning

## Preserved Body

````markdown
Endpoint Detection and Response (EDR) is a security solution that combines real-time monitoring, data collection, and advanced analytics to detect, investigate, and respond to cyber threats at the endpoint level. Leveraging machine learning algorithms and behavioral analysis, EDR tools can identify malicious activities, automate containment and remediation actions, and provide forensic insights to enhance an organization's overall security posture.

## Static Detection

**Mechanism**: Static detection is a security technique used in EDR and antivirus software that analyzes files and applications without executing them, typically based on predefined signatures or known malicious patterns.

**Bypass**:

- Obfuscate strings
- Dynamically resolving strings
- Dynamically resolving imports, reducing the `Import Address Table` (IAT)
- Custom `GetProcAddress` and `GetModuleHandle`
- API Hashing

## User Behavioural Analysis

**Mechanism**: User Behavioral Analysis (UBA) monitors and analyzes user activities and patterns to detect anomalies and potential threats.

**Bypass**:

- Learning about OPSEC methods

## Usermode Windows Function Monitoring

**Mechanism**: Usermode Windows Function Monitoring is a technique that tracks and analyzes the execution of Windows API (Application Programming Interface) calls and functions within user space processes.

**Bypass**:

- Unhooking
- Indirect syscalls

## Call Stack Analysis

**Mechanism**: Checking the origin of function calls via the Call Stack chain

**Bypass**:

- TODO
- TODO

## Process Analysis

**Mechanism**: Process analysis includes inspecting memory regions, identifying remote process access, and assessing child processes to gain insights into process relationships, uncover hidden or suspicious activities.

**Bypass**:

- Avoid RWX memory region (RW->RX)
- Break parent-child link (e.g: word.exe spawning cmd.exe)
- TODO

## Kernel Callbacks

**Mechanism**: Kernel callbacks in the context of Endpoint Detection and Response (EDR) are functions registered by kernel drivers that get triggered in response to specific events or actions within the operating system's kernel.

**Bypass**:

- TODO

## WDAC to Disable EDR Components

Place the WDAC policy `SiPolicy.p7b` inside `C:\Windows\System32\CodeIntegrity\` and reboot the machine.

```ps1
smbmap -u Administrator -p P@ssw0rd -H 192.168.4.4 --upload "/home/kali/SiPolicy.p7b" "ADMIN\$/System32/CodeIntegrity/SiPolicy.p7b"
smbmap -u Administrator -p P@ssw0rd -H 192.168.4.4 -x "shutdown /r /t 0"
```

Using Krueger a .NET post-exploitation tool.

- [logangoins/Krueger](https://github.com/logangoins/Krueger) - Proof of Concept (PoC) .NET tool for remotely killing EDR with WDAC

    ```ps1
    inlineExecute-Assembly --dotnetassembly C:\Tools\Krueger.exe --assemblyargs --host ms01
    ```

## References

- [Flying Under the Radar: Part 1: Resolving Sensitive Windows Functions with x64 Assembly - theepicpowner - Apr 24, 2024](https://theepicpowner.gitlab.io/posts/Flying-Under-the-Radar-Part-1/)
- [Malware AV/VM evasion - part 16: WinAPI GetProcAddress implementation. Simple C++ example - cocomelonc](https://cocomelonc.github.io/malware/2023/04/16/malware-av-evasion-16.html)
- [Custom GetProcAddress And GetModuleHandle Implementation (X64) - daax - December 15, 2016](https://revers.engineering/custom-getprocaddress-and-getmodulehandle-implementation-x64/)
- [Weaponizing WDAC: Killing the Dreams of EDR - Jonathan Beierle and Logan Goins - December 20, 2024](https://beierle.win/2024-12-20-Weaponizing-WDAC-Killing-the-Dreams-of-EDR/)
````

## Source Verification

[source record](../../sources/internalallthethings/endpoint-detection-and-response.md)

## Evidence Excerpt

```text
_body: "# Endpoint Detection and Response\n\nEndpoint Detection and Response (EDR) is a security solution that combines real-time\
\ monitoring, data collection, and advanced analytics to detect, investigate, and respond to cyber threats at the endpoint\
\ level. Leveraging machine learning algorithms and behavioral analysis, EDR tools can identify malicious activities, automate\
\ containment and remediation actions, and provide forensic insights to enhance an organization's overall security posture.\n\
\n## Static Detection\n\n**Mechanism**: Static detection is a security technique used in EDR and antivirus software that\
\ analyzes files and applications without executing them, typically based on predefined signatures or known malicious patterns.\n\
\n**Bypass**:\n\n- Obfuscate strings\n- Dynamically resolving strings\n- Dynamically resolving imports, reducing the `Import\
\ Address Table` (IAT)\n- Custom `GetProcAddress` and `GetModuleHandle`\n- API Hashing\n\n## User Behavioural Analysis\n\
```
