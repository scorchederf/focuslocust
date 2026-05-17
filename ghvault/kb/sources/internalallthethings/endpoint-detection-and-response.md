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

## Generated Concept Page

- [Endpoint Detection and Response](../../topics/redteam/endpoint-detection-and-response.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-evasion-edr-bypass |
| name | Endpoint Detection and Response |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/evasion/edr-bypass.md |

## Preserved Source Material

````yaml
_body: "# Endpoint Detection and Response\n\nEndpoint Detection and Response (EDR) is a security solution that combines real-time\
  \ monitoring, data collection, and advanced analytics to detect, investigate, and respond to cyber threats at the endpoint\
  \ level. Leveraging machine learning algorithms and behavioral analysis, EDR tools can identify malicious activities, automate\
  \ containment and remediation actions, and provide forensic insights to enhance an organization's overall security posture.\n\
  \n## Static Detection\n\n**Mechanism**: Static detection is a security technique used in EDR and antivirus software that\
  \ analyzes files and applications without executing them, typically based on predefined signatures or known malicious patterns.\n\
  \n**Bypass**:\n\n- Obfuscate strings\n- Dynamically resolving strings\n- Dynamically resolving imports, reducing the `Import\
  \ Address Table` (IAT)\n- Custom `GetProcAddress` and `GetModuleHandle`\n- API Hashing\n\n## User Behavioural Analysis\n\
  \n**Mechanism**: User Behavioral Analysis (UBA) monitors and analyzes user activities and patterns to detect anomalies and\
  \ potential threats.\n\n**Bypass**:\n\n- Learning about OPSEC methods\n\n## Usermode Windows Function Monitoring\n\n**Mechanism**:\
  \ Usermode Windows Function Monitoring is a technique that tracks and analyzes the execution of Windows API (Application\
  \ Programming Interface) calls and functions within user space processes.\n\n**Bypass**:\n\n- Unhooking\n- Indirect syscalls\n\
  \n## Call Stack Analysis\n\n**Mechanism**: Checking the origin of function calls via the Call Stack chain\n\n**Bypass**:\n\
  \n- TODO\n- TODO\n\n## Process Analysis\n\n**Mechanism**: Process analysis includes inspecting memory regions, identifying\
  \ remote process access, and assessing child processes to gain insights into process relationships, uncover hidden or suspicious\
  \ activities.\n\n**Bypass**:\n\n- Avoid RWX memory region (RW->RX)\n- Break parent-child link (e.g: word.exe spawning cmd.exe)\n\
  - TODO\n\n## Kernel Callbacks\n\n**Mechanism**: Kernel callbacks in the context of Endpoint Detection and Response (EDR)\
  \ are functions registered by kernel drivers that get triggered in response to specific events or actions within the operating\
  \ system's kernel.\n\n**Bypass**:\n\n- TODO\n\n## WDAC to Disable EDR Components\n\nPlace the WDAC policy `SiPolicy.p7b`\
  \ inside `C:\\Windows\\System32\\CodeIntegrity\\` and reboot the machine.\n\n```ps1\nsmbmap -u Administrator -p P@ssw0rd\
  \ -H 192.168.4.4 --upload \"/home/kali/SiPolicy.p7b\" \"ADMIN\\$/System32/CodeIntegrity/SiPolicy.p7b\"\nsmbmap -u Administrator\
  \ -p P@ssw0rd -H 192.168.4.4 -x \"shutdown /r /t 0\"\n```\n\nUsing Krueger a .NET post-exploitation tool.\n\n- [logangoins/Krueger](https://github.com/logangoins/Krueger)\
  \ - Proof of Concept (PoC) .NET tool for remotely killing EDR with WDAC\n\n    ```ps1\n    inlineExecute-Assembly --dotnetassembly\
  \ C:\\Tools\\Krueger.exe --assemblyargs --host ms01\n    ```\n\n## References\n\n- [Flying Under the Radar: Part 1: Resolving\
  \ Sensitive Windows Functions with x64 Assembly - theepicpowner - Apr 24, 2024](https://theepicpowner.gitlab.io/posts/Flying-Under-the-Radar-Part-1/)\n\
  - [Malware AV/VM evasion - part 16: WinAPI GetProcAddress implementation. Simple C++ example - cocomelonc](https://cocomelonc.github.io/malware/2023/04/16/malware-av-evasion-16.html)\n\
  - [Custom GetProcAddress And GetModuleHandle Implementation (X64) - daax - December 15, 2016](https://revers.engineering/custom-getprocaddress-and-getmodulehandle-implementation-x64/)\n\
  - [Weaponizing WDAC: Killing the Dreams of EDR - Jonathan Beierle and Logan Goins - December 20, 2024](https://beierle.win/2024-12-20-Weaponizing-WDAC-Killing-the-Dreams-of-EDR/)"
_relative_path: redteam/evasion/edr-bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/edr-bypass.md
````
