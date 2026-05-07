---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1129
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1129-shared-modules
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

Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions (i.e., [[kb/mitre/attack/techniques/T1106-native-api|Native API]]).<br><br>Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network communications or execution of specific actions on objective.<br><br>The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides in `dlfcn.h` in functions such as `dlopen` and `dlsym`. Although macOS can execute `.so` files, common practice uses `.dylib` files.[^2] [^5] [^1] [^3] <br><br>The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in `NTDLL.dll` and is part of the Windows [[kb/mitre/attack/techniques/T1106-native-api|Native API]] which is called from functions like `LoadLibrary` at run time.[^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT can load DLLs into memory.[^1]  |
| [S0196](https://attack.mitre.org/software/S0196) | PUNCHBUGGY | PUNCHBUGGY can load a DLL using the LoadLibrary API.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can load and call DLL functions.[^1] [^2]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | For network communications, OSX_OCEANLOTUS.D loads a dynamic library (`.dylib` file) using `dlopen()` and obtains a function pointer to execute within that shared library using `dlsym()`.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth uses the LoadLibraryExW() function to load additional modules. [^1]  |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury is executed through hooking the keyutils.so file used by legitimate versions of `OpenSSH` and `libcurl`.[^1]  |
| [S0415](https://attack.mitre.org/software/S0415) | BOOSTWRITE | BOOSTWRITE has used the DWriteCreateFactory() function to load additional modules.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor's dispatcher can execute additional plugins by loading the respective DLLs.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo had used AutoIt to load and execute the DLL payload.[^1]   |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to inject the `LoadLibrary` call template DLL into running processes.[^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon has used call to `LoadLibrary` to load its installer. PipeMon loads its modules using reflective loading or custom shellcode.[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN has loaded and executed DLLs in memory during runtime on a victim machine.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack contains a function that calls `LoadLibrary` and `GetProcAddress`.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet calls LoadLibrary then executes exports from a DLL.[^1]  |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk loads and executes functions from a DLL.[^1]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb's loader can call the `load()` function to load the FoggyWeb dll into an Application Domain on a compromised AD FS server.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can load DLLs.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee |  Bumblebee can use `LoadLibrary` to attempt to execute GdiPlus.dll.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | RotaJakiro uses dynamically linked shared libraries (`.so` files) to execute additional functionality using `dlopen()` and `dlsym()`.[^1]  |
| [S1154](https://attack.mitre.org/software/S1154) | VersaMem | VersaMem relied on the Java Instrumentation API and Javassist to dynamically modify Java code existing in memory.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | LightSpy's main executable and module `.dylib` binaries are loaded using a combination of `dlopen()` to load the library, `_objc_getClass()` to retrieve the class definition, and `_objec_msgSend()` to invoke/execute the specified method in the loaded class.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Identify and block potentially malicious software executed through this technique by using application control tools capable of preventing unknown modules from being loaded. |

 [^1]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^2]: [Apple Dev Dynamic Libraries](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/OverviewOfDynamicLibraries.html)
 [^3]: [Unit42 OceanLotus 2017](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)
 [^4]: [Microsoft DLL](https://learn.microsoft.com/troubleshoot/windows-client/deployment/dynamic-link-library)
 [^5]: [Linux Shared Libraries](https://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html)
 [^6]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^7]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^8]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^9]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
 [^10]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^11]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^12]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^13]: [Trend Micro KillDisk 1](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
 [^14]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^15]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^16]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^17]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^18]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^19]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
 [^20]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^21]: [ESET Ebury May 2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
 [^22]: [FireEye FIN7 Oct 2019](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)
 [^23]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^24]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^25]: [Lumen Versa 2024](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)
