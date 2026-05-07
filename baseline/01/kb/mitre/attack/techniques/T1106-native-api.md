---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1106
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1106-native-api
tactic:
    - Execution
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes.[^15] [^10]  These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.<br><br>Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter|Command and Scripting Interpreter]], the native API and its hierarchy of interfaces provide mechanisms to interact with and utilize various components of a victimized system.<br><br>Native API functions (such as `NtCreateProcess`) may be directed invoked via system calls / syscalls, but these features are also often exposed to user-mode applications via interfaces and libraries.[^4] [^7] [^11]  For example, functions such as the Windows API `CreateProcess()` or GNU `fork()` will allow programs and scripts to start other processes.[^12] [^6]  This may allow API callers to execute a binary, run a CLI command, load modules, etc. as thousands of similar API functions exist for various system operations.[^13] [^9] [^8] <br><br>Higher level software frameworks, such as Microsoft .NET and macOS Cocoa, are also available to interact with native APIs. These frameworks typically provide language wrappers/abstractions to API functionalities and are designed for ease-of-use/portability of code.[^14] [^2] [^1] [^3] <br><br>Adversaries may use assembly to directly or in-directly invoke syscalls in an attempt to subvert defensive sensors and detection signatures such as user mode API-hooks.[^5]  Adversaries may also attempt to tamper with sensors and defensive tools associated with API monitoring, such as unhooking monitored functions via [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools|Disable or Modify Tools]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor has the ability to use native APIs for execution including `GetProcessHeap`, `GetProcAddress`, and `LoadLibrary`.[^1] [^2]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX can use the Windows API functions `GetProcAddress`, `LoadLibrary`, and `CreateProcess` to execute another process.[^1] [^2] [^3]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can use native Windows APIs including `GetHostByName`.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has used the `InterlockedExchange`, `SeShutdownPrivilege`, and `ExitWindowsEx` Windows API functions.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL is capable of starting a process using CreateProcess.[^1]  |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | Misdat has used Windows APIs, including `ExitWindowsEx` and `GetKeyboardType`.[^1]   |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type has used Windows API calls, including `NetUserAdd` and `NetUserDel`.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | S-Type has used Windows APIs, including `GetKeyboardType`, `NetUserAdd`, and `NetUserDel`.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT can load a PE file from memory or the file system and execute it with `CreateProcessW`.[^1]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | BADNEWS has a command to download an .exe and execute it via CreateProcess API. It can also run with ShellExecute.[^1] [^2]  |
| [S0141](https://attack.mitre.org/software/S0141) | Winnti for Windows | Winnti for Windows can use Native API to create a new process and to start services.[^1]  |
| [S0147](https://attack.mitre.org/software/S0147) | Pteranodon | Pteranodon has used various API calls.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can use the `FindNextUrlCacheEntryA` and `FindFirstUrlCacheEntryA` functions to search for specific strings within browser history.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike's Beacon payload is capable of running shell commands without `cmd.exe` and PowerShell commands without `powershell.exe`[^2] [^1] [^3]  Cobalt Strike can also use `CreateThreadpoolWait`, `SetThreadpoolWait`, and `MessageBoxA` for sandbox evasion and execution of embedded payloads in memory.[^4]  |
| [S0161](https://attack.mitre.org/software/S0161) | XAgentOSX | XAgentOSX contains the execFile function to execute a specified file on the system using the NSTask:launch method.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer executes payloads using the Windows API call CreateProcessW().[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can use Native API including `CreateProcess` `GetProcessById`, and `WriteProcessMemory`.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook has used the ShellExecuteW() function call.[^1]   |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot creates processes using the Windows API calls: CreateProcessA() and CreateProcessAsUserA().[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can use a variety of API calls to execute shellcode.[^1]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck parses the export tables of system DLLs to locate and call various Windows API functions.[^1] [^2]  |
| [S0256](https://attack.mitre.org/software/S0256) | Mosquito | Mosquito leverages the CreateProcess() and LoadLibrary() calls to execute files with the .dll and .exe extensions.[^1]  |
| [S0259](https://attack.mitre.org/software/S0259) | InnaputRAT | InnaputRAT uses the API call ShellExecuteW for execution.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can use winapiexec tool for indirect execution of  `ShellExecuteW` and `CreateProcessA`.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot uses the Windows API call, CreateProcessW(), to manage execution flow.[^1]  TrickBot has also used `Nt*` API functions to perform [[kb/mitre/attack/techniques/T1055-process-injection\|Process Injection]].[^2]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has used the Windows API to communicate with the Service Control Manager to execute a thread.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis used the `IsDebuggerPresent`, `OutputDebugString`, and `SetLastError` APIs to avoid debugging. Denis used `GetProcAddress` and `LoadLibrary` to dynamically resolve APIs. Denis also used the `Wow64SetThreadContext` API as part of a process hollowing process.[^1] 	 |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has hardcoded API calls within its functions to use on the victim's machine.[^1]   |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains a variety of enumeration modules that have an option to use API calls to carry out tasks.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has used `CreateProcess` to create a new process to run its executable and `WNetEnumResourceW` to enumerate non-hidden shares.[^1]  |
| [S0384](https://attack.mitre.org/software/S0384) | Dridex | Dridex has used the `OutputDebugStringW` function to avoid malware analysis as part of its anti-debugging technique.[^1]   |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT has used the ShellExecute() function within a script.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used `CreateProcessW` to create child processes.[^1]  |
| [S0391](https://attack.mitre.org/software/S0391) | HAWKBALL | HAWKBALL has leveraged several Windows API calls to create processes, gather disk information, and detect debugger activity.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron is capable of starting a process using CreateProcess.[^1]  |
| [S0396](https://attack.mitre.org/software/S0396) | EvilBunny | EvilBunny has used various API calls as part of its checks to see if the malware is running in a sandbox.[^1] 	 |
| [S0398](https://attack.mitre.org/software/S0398) | HyperBro | HyperBro has the ability to run an application (`CreateProcessW`) or script/file (`ShellExecuteW`) via API.[^1]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can leverage native API including `RegisterServiceCtrlHandler ` to register a service.RegisterServiceCtrlHandler  |
| [S0416](https://attack.mitre.org/software/S0416) | RDFSNIFFER | RDFSNIFFER has used several Win32 API functions to interact with the victim machine.[^1]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant can perform dynamic DLL importing and API lookups using `LoadLibrary` and `GetProcAddress` on obfuscated strings.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has leveraged CreateProcessW() call to execute the debugger.[^1]  |
| [S0435](https://attack.mitre.org/software/S0435) | PLEAD | PLEAD can use `ShellExecute` to execute applications.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor's dispatcher has used CreateProcessW API for execution.[^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat has used Windows API functions to install the service and shim.[^1] 	 |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] used several Windows API functions to gather information from the infected system.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has used multiple native APIs including `ShellExecuteW` to run executables,`GetWindowsDirectoryW` to create folders, and `VirtualAlloc`, `WriteProcessMemory`, and `CreateRemoteThread` for process injection.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has used LoadLibrary(), GetProcAddress() and CreateRemoteThread() API functions to execute its shellcode.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun used dynamic API resolutions to various Windows APIs by leveraging `LoadLibrary()` and `GetProcAddress()`.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has used several Windows API functions throughout the encryption process including IsDebuggerPresent, TerminateProcess, Process32FirstW, among others.[^1] 	 |
| [S0453](https://attack.mitre.org/software/S0453) | Pony | Pony has used several Windows functions for various purposes.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has used native WINAPI calls.[^1] [^2]  |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to launch files using `ShellExecute`.[^1]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can use Windows API functions to inject the ransomware DLL.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can use Windows API functions such as `WriteFile`, `CloseHandle`, and `GetCurrentHwProfile` during its collection and file storage operations. Ramsay can execute its embedded components via `CreateProcessA` and `ShellExecute`.[^1]  |
| [S0466](https://attack.mitre.org/software/S0466) | WindTail | WindTail can invoke Apple APIs `contentsOfDirectoryAtPath`, `pathExtension`, and (string) `compare`.[^1]  |
| [S0470](https://attack.mitre.org/software/S0470) | BBK | BBK has the ability to use the `CreatePipe` API to add a sub-process for execution via [[kb/mitre/attack/software/S0106-cmd\|cmd]].[^1]  |
| [S0471](https://attack.mitre.org/software/S0471) | build_downer | build_downer has the ability to use the `WinExec` API to execute malware on a compromised host.[^1]  |
| [S0475](https://attack.mitre.org/software/S0475) | BackConfig | BackConfig can leverage API functions such as `ShellExecuteA` and `HttpOpenRequestA` in the process of downloading and executing files.[^1]  |
| [S0477](https://attack.mitre.org/software/S0477) | Goopy | Goopy has the ability to  enumerate the infected system's user name via `GetUserNameW`.[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID has called `ZwWriteVirtualMemory`, `ZwProtectVirtualMemory`, `ZwQueueApcThread`, and `NtResumeThread` to inject itself into a remote process.[^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has used the NtQueryDirectoryFile and ZwQueryDirectoryFile functions to hide files and directories.[^1]  |
| [S0493](https://attack.mitre.org/software/S0493) | GoldenSpy | GoldenSpy can execute remote commands in the Windows command shell using the `WinExec()` API.[^1] 	 |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can use Native API for execution and to retrieve active services.[^1] [^2]  |
| [S0499](https://attack.mitre.org/software/S0499) | Hancitor | Hancitor has used `CallWindowProc` and `EnumResourceTypesA` to interpret and execute shellcode.[^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon's first stage has been executed by a call to `CreateProcess` with the decryption password in an argument. PipeMon has used a call to `LoadLibrary` to load its installer.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can call `ShellExecuteW` to open the default browser on the URL localhost.[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint has used multiple native Windows APIs to execute and conduct process injections.[^1]  |
| [S0518](https://attack.mitre.org/software/S0518) | PolyglotDuke | PolyglotDuke can use `LoadLibraryW` and `CreateProcess` to load and execute code.[^1]  |
| [[kb/mitre/attack/software/S0521-bloodhound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can use .NET API calls in the SharpHound ingestor component to pull Active Directory data.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can execute through the `WinExec` API.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can use various APIs to allocate memory and facilitate code execution/injection.[^1]  |
| [S0537](https://attack.mitre.org/software/S0537) | HyperStack | HyperStack can use Windows API's `ConnectNamedPipe` and `WNetAddConnection2` to detect incoming connections and connect to remote shares.[^1]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has used the Windows API to make detection more difficult.[^1]   |
| [S0561](https://attack.mitre.org/software/S0561) | GuLoader | GuLoader can use a number of different APIs for discovery and execution.[^1]  |
| [S0562](https://attack.mitre.org/software/S0562) | SUNSPOT | SUNSPOT used Windows API functions such as `MoveFileEx` and `NtQueryInformationProcess` as part of the SUNBURST injection process.[^1]   |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive | Explosive has a function to call the OpenClipboard wrapper.[^1]    |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer has used dynamic API resolution to avoid identifiable strings within the binary, including `RegEnumKeyW`.[^1]  |
| [S0574](https://attack.mitre.org/software/S0574) | BendyBear | BendyBear can load and execute modules and Windows Application Programming (API) calls using standard shellcode API hashing.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti has used API calls during execution.[^1] [^2]   |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | After escalating privileges, MegaCortex calls `TerminateProcess()`, `CreateRemoteThread`, and other Win32 APIs.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear can leverage API functions for execution.[^1]  |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest uses various API to perform behaviors such as executing payloads and performing local enumeration.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet uses the SetSecurityDescriptorDacl API to reduce object integrity levels.[^1]  |
| [S0606](https://attack.mitre.org/software/S0606) | Bad Rabbit | Bad Rabbit has used various Windows API calls.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk has called the Windows API to retrieve the hard disk handle and shut down the machine.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist can use `GetUserNameW`, `GetComputerNameW`, and `GetComputerNameExW` to gather information.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop has used built-in API functions such as WNetOpenEnumW(), WNetEnumResourceW(), WNetCloseEnum(), GetProcAddress(), and VirtualAlloc().[^1] [^2]  |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker's custom crypter, CryptOne, leveraged the VirtualAlloc() API function to help execute the payload.[^1]  |
| [S0614](https://attack.mitre.org/software/S0614) | CostaBricks | CostaBricks has used a number of API calls, including `VirtualAlloc`, `VirtualFree`, `LoadLibraryA`, `GetProcAddress`, and `ExitProcess`.[^1]   |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT has the ability to respawn itself using `ShellExecuteW` and `CreateProcessW`.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed has the ability to use multiple dynamically resolved API calls.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape makes various native API calls.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba has used several built-in API functions for discovery like GetIpNetTable and NetShareEnum.[^1]   |
| [S0627](https://attack.mitre.org/software/S0627) | SodaMaster | SodaMaster can use `RegOpenKeyW` to access the Registry.[^1]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | The file collection tool used by RainyDay can utilize native API including `ReadDirectoryChangeW` for folder monitoring.[^1]  |
| [S0630](https://attack.mitre.org/software/S0630) | Nebulae | Nebulae has the ability to use `CreateProcess` to execute a process.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes used the `CreateFileW()` API function with read permissions to access downloaded payloads.[^1]   |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent can use Native API including `GetProcAddress` and `ShellExecuteW`.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk can use multiple Windows API calls for actions on compromised hosts including discovery and execution.[^1] [^2] [^3]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon has used the Windows Crypto API to generate an AES key.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can use `GetProcAddress` to help delete malicious strings from memory.[^1]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon has used Windows API calls to obtain information about the compromised host.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can run the ShellExecuteW API via the Windows Command Shell.[^1]  |
| [S0653](https://attack.mitre.org/software/S0653) | xCaon | xCaon has leveraged native OS function calls to retrieve  victim's network adapter's  information using GetAdapterInfo() API.[^1]   |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol has used several API calls like `GetLogicalDriveStrings`, `SleepEx`, `SystemParametersInfoAPI`, `CryptEncrypt`, and others to execute parts of its attack.[^1]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb's loader can use API functions to load the FoggyWeb backdoor into the same Application Domain within which the legitimate AD FS managed code is executed.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can use WinSock API for communication including `WSASend` and `WSARecv`.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can call the `GetNetworkParams` API as part of its C2 establishment process.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium has the ability to use various Windows API functions to perform tasks.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can use Windows API including `WinExec` for execution.[^1]  |
| [S0668](https://attack.mitre.org/software/S0668) | TinyTurla | TinyTurla has used `WinHTTP`, `CreateProcess`, and other APIs for C2 communications and other functions.[^1]  |
| [S0669](https://attack.mitre.org/software/S0669) | KOCTOPUS | KOCTOPUS can use the `LoadResource` and `CreateProcessW` APIs for execution.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can use a variety of API calls on a compromised host.[^1]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma has used various Windows API calls.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower can use various API calls.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has used various Windows API functions on a victim's machine.[^1]   |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can use various Linux API functions including those for execution and discovery.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor can use `WinAPI` to remove a victim machine from an Active Directory domain.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate has used the `ExitWindowsEx` to flush file buffers to disk and stop running processes and other API calls.[^1] [^2]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.[^1]  |
| [S0693](https://attack.mitre.org/software/S0693) | CaddyWiper | CaddyWiper has the ability to dynamically resolve and use APIs, including `SeTakeOwnershipPrivilege`.[^1]  |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can use various API calls to see if it is running in a sandbox.[^1]  |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] code modules use various API functions to load and inject code.[^1] 	 |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro can use Native API to enable obfuscation including `GetLastError` and `GetTickCount`.[^1]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can call multiple Windows API functions used for privilege escalation, service execution, and to overwrite random bites of data.[^3] [^4] [^2] [^1]  |
| [S0698](https://attack.mitre.org/software/S0698) | HermeticWizard | HermeticWizard can connect to remote shares using `WNetAddConnection2W`.[^1]  |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ has used API functions such as `Process32First`, `Process32Next`, and `ShellExecuteA`.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan can use the API `DnsQuery_A` for DNS resolution.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa has used macOS API functions to perform tasks.[^1] [^2]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot has used different API calls, including `GetProcAddress`, `VirtualAllocEx`, `WriteProcessMemory`, `CreateProcessA`, and `SetThreadContext`.[^1] [^2]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can use the `ShowWindow` API to avoid detection.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has used a variety of Windows API calls, including `GetComputerNameA`, `GetUserNameA`, and `CreateProcessA`.[^1]  |
| [S1033](https://attack.mitre.org/software/S1033) | DCSrv | DCSrv has used various Windows API functions, including `DeviceIoControl`, as part of its encryption process.[^1]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater can use a variety of APIs for execution.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can use multiple Native APIs.[^1] [^2]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can use Native API for defense evasion, discovery, and collection.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] has used a variety of Windows API functions.[^1]  |
| [S1052](https://attack.mitre.org/software/S1052) | DEADEYE | DEADEYE can execute the `GetComputerNameA` and `GetComputerNameExA` WinAPI functions.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has used a variety of Windows API calls, including `NtCurrentPeb` and `GetLogicalDrives`.[^1]  |
| [S1058](https://attack.mitre.org/software/S1058) | Prestige | Prestige has used the `Wow64DisableWow64FsRedirection()` and `Wow64RevertWow64FsRedirection()` functions to disable and restore file system redirection.[^1]   |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can execute an operator-provided Windows command by leveraging functions such as `WinExec`, `WriteFile`, and `ReadFile`.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can use a variety of API calls.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can call multiple Windows APIs for execution, to share memory, and defense evasion.[^2] [^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can use Windows API calls to gather information from an infected host.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can use multiple native APIs, including `WriteProcessMemory`, `CreateProcess`, and `CreateRemoteThread` for process injection.[^1]    |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can use a variety of API calls for persistence and defense evasion.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta has the ability to use native APIs for numerous functions including discovery and defense evasion.[^5] [^3] [^1] [^2] [^4]   |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can use multiple APIs for discovery, communication, and execution.[^1]  |
| [S1076](https://attack.mitre.org/software/S1076) | QUIETCANARY | QUIETCANARY can call `System.Net.HttpWebRequest` to identify the default proxy configured on the victim computer.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | When executing with non-root permissions, RotaJakiro uses the the `shmget` API to create shared memory between other known RotaJakiro processes. RotaJakiro also uses the `execvp` API to help its dead process "resurrect".[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can utilize Native API functions such as, `ToolHelp32` and `Rt1AdjustPrivilege` to enable `SeDebugPrivilege` on a compromised machine.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to call Win32 API functions to determine if `powershell.exe` is running.[^1]   |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.[^1]  |
| [S1089](https://attack.mitre.org/software/S1089) | SharpDisco | SharpDisco can leverage Native APIs through plugins including `GetLogicalDrives`.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can use multiple native APIs including `GetKeyState`, `GetForegroundWindow`, `GetWindowThreadProcessId`, and `GetKeyboardLayout`.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai has the ability to call Windows APIs.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | The Ninja loader can call Windows APIs for discovery, process injection, and payload decryption.[^1] [^2]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate uses the native Windows API `CallWindowProc()` to decode and launch encoded shellcode payloads during execution.[^2]  DarkGate can call kernel mode functions directly to hide the use of process hollowing methods during execution.[^1]  DarkGate has also used the `CreateToolhelp32Snapshot`, `GetFileAttributesA` and `CreateProcessA` functions to obtain a list of running processes, to check for security products and to execute its malware.[^3]   |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu has used a variety of Windows API calls, including ShellExecute and WriteProcessMemory.[^1] [^2]  |
| [S1129](https://attack.mitre.org/software/S1129) | Akira | Akira executes native Windows functions such as `GetFileAttributesW` and `GetSystemInfo`.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can use the API `DeviceIoControl` to resize the allocated space for and cause the deletion of volume shadow copy snapshots.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot uses native Windows APIs to determine if the process is being debugged and analyzed, such as `CheckRemoteDebuggerPresent`, `NtQueryInformationProcess`, `ProcessDebugPort`, and `ProcessDebugFlags`.[^1]  Other Pikabot variants populate a global list of Windows API addresses from the `NTDLL` and `KERNEL32` libraries, and references these items instead of calling the API items to obfuscate execution.[^2]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can use Windows APIs including `LoadLibrary` and `GetProcAddress`.[^1]  |
| [S1151](https://attack.mitre.org/software/S1151) | ZeroCleare | ZeroCleare can call the `GetSystemDirectoryW` API to locate the system directory.[^1]  |
| [S1152](https://attack.mitre.org/software/S1152) | IMAPLoader | IMAPLoader imports native Windows APIs such as `GetConsoleWindow` and `ShowWindow`.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus has used multiple Windows API post exploitation including `GetAdaptersInfo`, `CreateToolhelp32Snapshot`, and `CreateProcessW`.[^2] [^1]  |
| [S1169](https://attack.mitre.org/software/S1169) | Mango | Mango has the ability to use Native APIs.[^1]  |
| [S1170](https://attack.mitre.org/software/S1170) | ODAgent | ODAgent can pass commands using native APIs.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster has used the `ShowWindow` and `CreateProcessW` APIs.[^1]  |
| [S1179](https://attack.mitre.org/software/S1179) | Exbyte | Exbyte calls `ShellExecuteW` with the `IpOperation` parameter `RunAs` to launch `explorer.exe` with elevated privileges.[^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware uses the `SetThreadExecutionState` API to prevent the victim system from entering sleep.[^1]  |
| [S1190](https://attack.mitre.org/software/S1190) | Kapeka | Kapeka utilizes WinAPI calls to gather victim system information.[^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can use native APIs including `LoadLibraryExA` for execution and `NtSetInformationProcess` for defense evasion purposes.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 has the ability to directly call native Windows API items during execution.[^2] [^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader uses the native Windows API for functionality, including defense evasion.[^1]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex calls the `WaitForSingleObject` API function as part of time-check logic.[^1]  |
| [S1226](https://attack.mitre.org/software/S1226) | BOOKWORM | BOOKWORM has used various Windows API calls during execution and defense evasion.[^1]  [^2]  BOOKWORM has created a buffer on the heap using `HeapCreate` and `HeapAlloc` which allows for copying of shell code and then execution on the heap is initiated through callback function of legitimate API functions such as `EnumChildWindows` or `EnumSystemLanguageGroupsA`. [^2]  |
| [S1227](https://attack.mitre.org/software/S1227) | StarProxy | StarProxy has used native windows API calls such as `GetLocalTime()` to retrieve system data.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has used various Windows API calls during execution, when establishing persistence and defense evasion.[^1] [^2]  PUBLOAD stager leveraged Windows API functions with callback including `GrayStringW`, `EnumDateFormatsA`, and `LineDDA` to bypass anti-virus monitoring. [^3]  PUBLOAD has also utilized other native windows API functions with callback functions such as `EnumChildWindows` and `EnumSystemLanguageGroupsA`. [^4]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc can use `NtAllocateVirtualMemory` and `NtCreateThreadEx` to aid process injection.[^1]  |
| [S1232](https://attack.mitre.org/software/S1232) | SplatDropper | SplatDropper has utilized hashed Native Windows API calls.[^1]  |
| [S1233](https://attack.mitre.org/software/S1233) | PAKLOG | PAKLOG has used Windows API `SetWindowsHookExW` with `idHook` set to `WH_KEYBOARD_LL` and a custom hook procedure to support its keylogging functions.[^1]  |
| [S1234](https://attack.mitre.org/software/S1234) | SplatCloak | SplatCloak has utilized Native Windows API calls dynamically through `ZwQuerySystemInformation`.[^1]  |
| [S1236](https://attack.mitre.org/software/S1236) | CLAIMLOADER | CLAIMLOADER has used various Windows API calls during execution, when establishing persistence and defense evasion.[^1] [^2]   CLAIMLOADER has also leveraged the legitimate API functions to run its shellcode through the callback function, including `GetDC()` and `EnumFontsW()`.[^1]   CLAIMLOADER established persistence by utilizing the API `SHSetValue()`.[^1]  CLAIMLOADER has utilized APIs with callback functions such as `EnumpropsExW`, `EnumSystemLanguageGroupsA`, and `EnumCalendarInfoExW`.[^2]  |
| [S1237](https://attack.mitre.org/software/S1237) | CANONSTAGER | CANONSTAGER has leveraged Native API calls to execute code within the victim’s system including `GetCurrentDirectoryW`, `RegisterClassW` and `CreateWindowExW`.[^1]  CANONSTAGER also created a new overlapped window that initiates callback functions to a windows procedure that processes Windows messages until a designated message type of 0x0018 WM_SHOWWINDOW is observed which then initiates the deployment of a subsequent malicious payload.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has utilized Native Windows API functions such as `WriteProcessMemory` and `CreateRemoteThreadEx`.[^2]  TONESHELL has also utilized Windows API functions for creating seed values including `CoCreateGuid` and `GetTickCount`.[^1] [^4]  TONESHELL has leveraged the legitimate API function `EnumSystemLocalesA` to run its shellcode through the callback function.[^3]    |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can attempt to log on to the local computer via `LogonUserW` and use `GetLogicalDrives()` and `EnumResourceW()` for discovery.[^2] [^1]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has leveraged Windows Native API functions to execute payloads.[^1]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has leveraged Windows Native API functions to execute its operations.[^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has utilized native Windows API functions such as `EnumWindows`and `GetVolumeInformationA` during discovery activities.[^1]    |
| [S9007](https://attack.mitre.org/software/S9007) | HTTPTroy | HTTPTroy has leveraged Windows Native API calls, including `GetProcAddress` to execute functions in memory.[^1]  |
| [S9012](https://attack.mitre.org/software/S9012) | TRAILBLAZE | TRAILBLAZE has leveraged raw syscalls to execute commands.[^1] [^2]  |
| [S9016](https://attack.mitre.org/software/S9016) | Caminho | Caminho can use `System.Net.WebClient.downloadString()` for file download.[^1]  |
| [S9018](https://attack.mitre.org/software/S9018) | HeartCrypt | HeartCrypt can use Windows API functions to modify the Registry and `FindResourceW`, `LoadResource`, and `LockResource` to acquire a pointer to corresponding code resources.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can use Windows APIs such as `VirtualAllocEx()`, `WriteProcessMemory()`, `CreateRemoteThread()`, `NtAllocateVirtualMemory()`, `NtWriteVirtualMemory()`, and `RtlCreateUserThread()` to enable memory injection of shellcode.[^1]  |
| [S9021](https://attack.mitre.org/software/S9021) | DOWNIISSA | DOWNIISSA can use the `URLDownloadToFileA()` API to download from remote resources.[^1]  |
| [S9025](https://attack.mitre.org/software/S9025) | NOOPLDR | NOOPLDR can use native APIs `NtProtectVirtualMemory`, `NtWriteVirtualMemory`, and `NtCreateThreadEx` to aid process injection.[^1]  |
| [S9027](https://attack.mitre.org/software/S9027) | ANELLDR | ANELLDR can use the `ZwSetInformationThread` to enable debugger evasion.[^1] <br> |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has the ability to relaunch itself using the `CreateProcessW` API.[^1]       |
| [S9033](https://attack.mitre.org/software/S9033) | Fooder | Fooder has used the WinCrypt API for payload decryption, `DuplicateTokenEx` to duplicate the token of a specified process, and `CreateProcessAsUserA` for payload execution.[^1]          |
| [S9036](https://attack.mitre.org/software/S9036) | LP-Notes | LP-Notes has used the `ImpersonateLoggedOnUser` API to impersonate the security context of the taskhostw.exe process.[^1]  Additionally, LP-Notes has also used the `CredUIPromptForWindowsCredentialsW` API to obtain Windows credentials.[^1]  |
| [S9037](https://attack.mitre.org/software/S9037) | RustyWater | RustyWater has used `CreateObject` to instantiate a WScript.Shell Component Object Model (COM) object.[^1]   Additionally, RustyWater has used `VirtualAllocEx` and `WriteProcessMemory` to inject shellcode into explorer.exe.[^1]        |
| [S9038](https://attack.mitre.org/software/S9038) | DynoWiper | DynoWiper has used multiple native Windows functions, such as `GetLogicalDrives` and `FindNextFile` for discovery and file deletion.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Identify and block potentially malicious software executed that may be executed through this technique by using application control [^1]  tools, like Windows Defender Application Control[^3] , AppLocker, [^6]  [^5]  or Software Restriction Policies [^2]  where appropriate. [^4]  |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent Office VBA macros from calling Win32 APIs. [^1]  |

 [^1]: [MACOS Cocoa](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/CocoaApplicationLayer/CocoaApplicationLayer.html#//apple_ref/doc/uid/TP40001067-CH274-SW1)
 [^2]: [Apple Core Services](https://developer.apple.com/documentation/coreservices)
 [^3]: [macOS Foundation](https://developer.apple.com/documentation/foundation)
 [^4]: [OutFlank System Calls](https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/)
 [^5]: [Redops Syscalls](https://redops.at/en/blog/direct-syscalls-vs-indirect-syscalls)
 [^6]: [GNU Fork](https://www.gnu.org/software/libc/manual/html_node/Creating-a-Process.html)
 [^7]: [CyberBit System Calls](https://www.cyberbit.com/blog/endpoint-security/malware-mitigation-when-direct-system-calls-are-used/)
 [^8]: [GLIBC](https://www.gnu.org/software/libc/)
 [^9]: [LIBC](https://man7.org/linux/man-pages//man7/libc.7.html)
 [^10]: [Linux Kernel API](https://www.kernel.org/doc/html/v4.12/core-api/kernel-api.html)
 [^11]: [MDSec System Calls](https://www.mdsec.co.uk/2020/12/bypassing-user-mode-hooks-and-direct-invocation-of-system-calls-for-red-teams/)
 [^12]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
 [^13]: [Microsoft Win32](https://docs.microsoft.com/en-us/windows/win32/api/)
 [^14]: [Microsoft NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet-framework)
 [^15]: [NT API Windows](https://undocumented.ntinternals.net/)
 [^16]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
 [^17]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^18]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
 [^19]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
 [^20]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^21]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^22]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^23]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^24]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^25]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^26]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^27]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^28]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^29]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^30]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^31]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^32]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^33]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^34]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^35]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^36]: [Medium Babuk February 2021](https://sebdraven.medium.com/babuk-is-distributed-packed-78e2f5dd2e62)
 [^37]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^38]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^39]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
 [^40]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^41]: [Cybereason Clop Dec 2020](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
 [^42]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^43]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
 [^44]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
 [^45]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)
 [^46]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^47]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
 [^48]: [Trend Micro KillDisk 1](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
 [^49]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)
 [^50]: [FireEye Ursnif Nov 2017](https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html)
 [^51]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^52]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^53]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^54]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^55]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^56]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^57]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^58]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^59]: [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)
 [^60]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^61]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^62]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^63]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
 [^64]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^65]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^66]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
 [^67]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^68]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
 [^69]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^70]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^71]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)
 [^72]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^73]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^74]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^75]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
 [^76]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^77]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^78]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^79]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^80]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^81]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)
 [^82]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))
 [^83]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
 [^84]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)
 [^85]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
 [^86]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)
 [^87]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^88]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^89]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
 [^90]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^91]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
 [^92]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
 [^93]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
 [^94]: [FireEye Hancitor](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html)
 [^95]: [Hornet Security Avaddon June 2020](https://www.hornetsecurity.com/en/security-information/avaddon-from-seeking-affiliates-to-in-the-wild-in-2-days/)
 [^96]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^97]: [RecordedFuture WhisperGate Jan 2022](https://www.recordedfuture.com/research/whispergate-malware-corrupts-computers-ukraine)
 [^98]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^99]: [Segurança Informática URSA Sophisticated Loader 2020](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)
 [^100]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
 [^101]: [Medium Eli Salem GuLoader April 2021](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
 [^102]: [Cyble Egregor Oct 2020](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)
 [^103]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^104]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^105]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^106]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^107]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^108]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^109]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^110]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^111]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^112]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^113]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
 [^114]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^115]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^116]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
 [^117]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
 [^118]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^119]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
 [^120]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^121]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
 [^122]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)
 [^123]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^124]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^125]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^126]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^127]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^128]: [Objective-See MacMa Nov 2021](https://objective-see.org/blog/blog_0x69.html)
 [^129]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^130]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
 [^131]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
 [^132]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
 [^133]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^134]: [ESET DynoWiper Update JAN 2026](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
 [^135]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^136]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^137]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^138]: [Zscaler XLoader 2025](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)
 [^139]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^140]: [Juniper IcedID June 2020](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
 [^141]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^142]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
 [^143]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)
 [^144]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^145]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^146]: [Broadcom](https://www.broadcom.com/support/security-center/protection-bulletin/bookworm-malware-linked-to-fireant-aka-stately-tarurus-activity-observed-in-southeast-asia)
 [^147]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)
 [^148]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^149]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^150]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
 [^151]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^152]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^153]: [Lab52 MUSTANG PANDA PUBLOAD MAY 2023](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)
 [^154]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^155]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^156]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^157]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^158]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^159]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
 [^160]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^161]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^162]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^163]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^164]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^165]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
 [^166]: [Uptycs Warzone UAC Bypass November 2020](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)
 [^167]: [Donut Github](https://github.com/TheWover/donut)
 [^168]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
 [^169]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^170]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^171]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)
 [^172]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^173]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^174]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^175]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^176]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^177]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
 [^178]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^179]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^180]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^181]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^182]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^183]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^184]: [ESET Bad Rabbit](https://www.welivesecurity.com/2017/10/24/bad-rabbit-not-petya-back/)
 [^185]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
 [^186]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^187]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^188]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^189]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^190]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
 [^191]: [FireEye FIN7 Oct 2019](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)
 [^192]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^193]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^194]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^195]: [Palo Alto HeartCrypt DEC 2024](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)
 [^196]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^197]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^198]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
 [^199]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^200]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
 [^201]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
 [^202]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
 [^203]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
 [^204]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^205]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^206]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^207]: [Avertium Black Basta June 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
 [^208]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
 [^209]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^210]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
 [^211]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
 [^212]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^213]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^214]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
 [^215]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^216]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
 [^217]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^218]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
 [^219]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
 [^220]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^221]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
 [^222]: [Lastline PlugX Analysis](https://lastline3.rssing.com/chan-29044929/all_p1.html#c29044929a2)
 [^223]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^224]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^225]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^226]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^227]: [Cisco CaddyWiper March 2022](https://blog.talosintelligence.com/2022/03/threat-advisory-caddywiper.html)
 [^228]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
 [^229]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^230]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
 [^231]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^232]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^233]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^234]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)
 [^235]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
 [^236]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^237]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^238]: [Cybereason Conti Jan 2021](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
 [^239]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^240]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
 [^241]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^242]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
 [^243]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
