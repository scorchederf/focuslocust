---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1027
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1027-obfuscated-files-or-information
tactic:
    - Stealth
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. <br><br>Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action may be required to open and [[kb/mitre/attack/techniques/T1140-deobfuscate-decode-files-or-information|Deobfuscate/Decode Files or Information]] for [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]]. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.[^1]  Adversaries may also use compressed or archived scripts, such as JavaScript. <br><br>Portions of files can also be encoded to hide the plain-text strings that would otherwise help defenders with discovery.[^4]  Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.[^5] <br><br>Adversaries may also abuse [[kb/mitre/attack/techniques/T1027.010-command-obfuscation|Command Obfuscation]] to obscure commands executed from payloads or directly via [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter|Command and Scripting Interpreter]]. Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature based detections and application control mechanisms.[^2] [^3] [^6]  

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0012](https://attack.mitre.org/software/S0012) | PoisonIvy | PoisonIvy hides any strings related to its own indicators of compromise.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX can use API hashing and modify the names of strings to evade detection.[^1] [^2]  |
| [S0030](https://attack.mitre.org/software/S0030) | Carbanak | Carbanak encrypts strings to make analysis more difficult.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | Most of the strings in ADVSTORESHELL are encrypted with an XOR-based algorithm; some strings are also encrypted with 3DES and reversed. API function names are also reversed, presumably to avoid detection in memory.[^1] [^2]  |
| [S0051](https://attack.mitre.org/software/S0051) | MiniDuke | MiniDuke can use control flow flattening to obscure code.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | The DustySky dropper uses a function to obfuscate the name of functions and other parts of the malware.[^1]  |
| [S0063](https://attack.mitre.org/software/S0063) | SHOTPUT | SHOTPUT is obscured using XOR encoding and appended to a valid GIF file.[^1] [^2]  |
| [S0070](https://attack.mitre.org/software/S0070) | HTTPBrowser | HTTPBrowser's code may be obfuscated through structured exception handling and return-oriented programming.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic heavily obfuscates its code to make analysis more difficult.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can base64 encode and AES-128-CBC encrypt data prior to transmission.[^1]  |
| [S0117](https://attack.mitre.org/software/S0117) | XTunnel | A version of XTunnel introduced in July 2015 obfuscated the binary using opaque predicates and other techniques in a likely attempt to obfuscate it and bypass security products.[^1]  |
| [S0124](https://attack.mitre.org/software/S0124) | Pisloader | Pisloader obfuscates files by splitting strings into smaller sub-strings and including "garbage" strings that are never used. The malware also uses return-oriented programming (ROP) technique and single-byte XOR to obfuscate data.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT has encrypted its virtual file system using AES-256 in XTS mode.[^2] [^1]   |
| [S0132](https://attack.mitre.org/software/S0132) | H1N1 | H1N1 uses multiple techniques to obfuscate strings, including XOR.[^1]  |
| [S0137](https://attack.mitre.org/software/S0137) | CORESHELL | CORESHELL obfuscates strings using a custom stream cipher.[^1]  |
| [S0138](https://attack.mitre.org/software/S0138) | OLDBAIT | OLDBAIT obfuscates internal strings and unpacks them at startup.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon contains base64-encoded strings.[^1]  |
| [S0142](https://attack.mitre.org/software/S0142) | StreamEx | StreamEx obfuscates some commands by using statically programmed fragments of strings when starting a DLL. It also uses a one-byte xor against 0x91 to encode configuration data.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM strings, network data, configuration, and modules are encrypted with a modified RC4 algorithm.[^2] [^1]  |
| [S0150](https://attack.mitre.org/software/S0150) | POSHSPY | POSHSPY appends a file signature header (randomly selected from six file types) to encrypted data prior to upload or download.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can hash functions to obfuscate calls to the Windows API and use a public/private key pair to encrypt Beacon session metadata.[^1] [^2]  |
| [S0167](https://attack.mitre.org/software/S0167) | Matryoshka | Matryoshka obfuscates API function names using a substitute cipher combined with Base64 encoding.[^1]  |
| [S0182](https://attack.mitre.org/software/S0182) | FinFisher | FinFisher is heavily obfuscated in many ways, including through the use of spaghetti code in its functions in an effort to confuse disassembly programs. It also uses a custom XOR algorithm to obfuscate code.[^2] [^1]  |
| [S0187](https://attack.mitre.org/software/S0187) | Daserf | Daserf uses encrypted Windows APIs and also encrypts data using the alternative base64+RC4 or the Caesar cipher.[^1]  |
| [S0189](https://attack.mitre.org/software/S0189) | ISMInjector | ISMInjector is obfuscated with the off-the-shelf SmartAssembly .NET obfuscator created by red-gate.com.[^1]  |
| [S0196](https://attack.mitre.org/software/S0196) | PUNCHBUGGY | PUNCHBUGGY has hashed most its code's functions and encrypted payloads with base64 and XOR.[^1]  |
| [S0197](https://attack.mitre.org/software/S0197) | PUNCHTRACK | PUNCHTRACK is loaded and executed by a highly obfuscated launcher.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE has used a custom obfuscation algorithm to hide strings including Registry keys, APIs, and DLL names.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | A JPIN uses a encrypted and compressed payload that is disguised as a bitmap within the resource section of the installer.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq uses basic obfuscation in the form of spaghetti code.[^1] [^2]  |
| [S0229](https://attack.mitre.org/software/S0229) | Orz | Some Orz strings are base64 encoded, such as the embedded DLL known as MockDll.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can encrypt data prior to exfiltration by using an RSA public key.[^1] [^2]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck payloads are obfuscated prior to compilation to inhibit analysis and/or reverse engineering.[^1] [^2]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie uses RC4 and Base64 to obfuscate strings.[^1]  |
| [S0259](https://attack.mitre.org/software/S0259) | InnaputRAT | InnaputRAT uses an 8-byte XOR key to obfuscate API names and other strings contained in the payload.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole avoids analysis by encrypting all strings, internal files, configuration data and by using a custom executable format.[^1] [^2]  |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE uses the Confuser protector to obfuscate an embedded .Net Framework assembly used for C2. OopsIE also encodes collected data in hexadecimal format before writing to files on disk and obfuscates strings.[^1] [^2]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar is obfuscated using the open source ConfuserEx protector. Kazuar also obfuscates the name of created files/folders/mutexes and encrypts debug messages written to log files using the Rijndael cipher.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot uses non-descriptive names to hide functionality.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT’s Java payload is encrypted with AES.[^1]  Additionally, backdoor files are encrypted using DES as a stream cipher. Later variants of jRAT also incorporated AV evasion methods such as Java bytecode obfuscation via the commercial Allatori obfuscation tool.[^2]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla has had its code obfuscated in an apparent attempt to make analysis difficult.[^1]  Agent Tesla has used the Rijndael symmetric encryption algorithm to encrypt strings.[^2]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] uses RC4 and base64 to obfuscate data, including Registry entries and file paths.[^1]  [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can also employ control flow flattening to hinder analysis.[^2]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon encrypts configuration files and tasks for the malware to complete using CAST-128 algorithm.[^2] [^1]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore’s plugins were obfuscated with Eazfuscater.NET 3.3.[^1]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI uses Base64 encoding for strings.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis obfuscates its code and encrypts the API names.[^1]  |
| [S0355](https://attack.mitre.org/software/S0355) | Final1stspy | Final1stspy obfuscates strings with base64 encoding.[^1]  |
| [S0369](https://attack.mitre.org/software/S0369) | CoinTicker | CoinTicker initially downloads a hidden encoded file.[^1]  |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury has obfuscated its strings with a simple XOR encryption with a static key.[^1]  |
| [S0384](https://attack.mitre.org/software/S0384) | Dridex | Dridex's strings are obfuscated using RC4.[^1]   |
| [S0393](https://attack.mitre.org/software/S0393) | PowerStallion | PowerStallion uses a XOR cipher to encrypt command output written to its OneDrive C2 server.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has used a custom encryption scheme for communication between scripts.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] encrypted gathered information with a combination of shifting and XOR using a static key.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk can use anti-disassembly and code transformation obfuscation techniques.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has obfuscated strings with base64 encoding.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has decrypted strings and other important information during the encryption process. Maze also calls certain functions dynamically to hinder analysis.[^1] 	 |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay has base64-encoded its portable executable and hidden itself under a JPG header. Ramsay can also embed information within document footers.[^1] 	 |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to XOR the strings for its installer component with a hardcoded 128 byte key.[^1]  |
| [[kb/mitre/attack/software/S0465-carrotball\|S0465]] | CARROTBALL | [[kb/mitre/attack/software/S0465-carrotball\|CARROTBALL]] has used a custom base64 alphabet to decode files.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has used an encrypted Virtual File System to store plugins.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has the ability to base64 encode and XOR encrypt strings.[^3] [^1] [^2]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore has obfuscated data with base64, AES, RC4, and bz2.[^1]  |
| [S0499](https://attack.mitre.org/software/S0499) | Hancitor | Hancitor has used Base64 to encode malicious links.[^1]  |
| [[kb/mitre/attack/software/S0500-mcmd\|S0500]] | MCMD | [[kb/mitre/attack/software/S0500-mcmd\|MCMD]] can Base64 encode output strings prior to sending to C2.[^1]  |
| [S0502](https://attack.mitre.org/software/S0502) | Drovorub | Drovorub has used XOR encrypted payloads in WebSocket client to server messages.[^1]  |
| [S0504](https://attack.mitre.org/software/S0504) | Anchor | Anchor has obfuscated code with stack strings and string encryption.[^1]  |
| [S0511](https://attack.mitre.org/software/S0511) | RegDuke | RegDuke can use control-flow flattening or the commercially available .NET Reactor for obfuscation.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can use base64 encoding, string stacking, and opaque predicates for obfuscation.[^1]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang has the ability to encode and RC6 encrypt data sent to C2.[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint has obfuscated the AES key used for encryption.[^1] 	 |
| [S0518](https://attack.mitre.org/software/S0518) | PolyglotDuke | PolyglotDuke can custom encrypt strings.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST obfuscated collected system information using a FNV-1a + XOR algorithm.[^1]  |
| [S0560](https://attack.mitre.org/software/S0560) | TEARDROP | TEARDROP created and read from a file with a fake JPG header, and its payload was encrypted with a simple rotating XOR cipher.[^1] [^2] [^3]  |
| [S0562](https://attack.mitre.org/software/S0562) | SUNSPOT | SUNSPOT encrypted log entries it collected with the stream cipher RC4 using a hard-coded key. It also uses AES128-CBC encrypted blobs for SUNBURST source code and data extracted from the SolarWinds Orion <MsBuild.exe` process.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can use compiler-based obfuscation for its code, encrypt DLLs, and hide Windows API calls.[^1] [^2] [^3]  |
| [S0584](https://attack.mitre.org/software/S0584) | AppleJeus | AppleJeus has XOR-encrypted collected system information prior to sending to a C2. AppleJeus has also used the open source ADVObfuscation library for its components.[^1]  |
| [S0593](https://attack.mitre.org/software/S0593) | ECCENTRICBANDWAGON | ECCENTRICBANDWAGON has encrypted strings with RC4.[^1]  |
| [[kb/mitre/attack/software/S0594-out1\|S0594]] | Out1 | [[kb/mitre/attack/software/S0594-out1\|Out1]] has the ability to encode data.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has encrypted its payload, a virtual file system, and various files.[^2] [^1]  |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell can use encryption and base64 encoding to hide strings and to enforce access control once deployed.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer uses heavily obfuscated code in its Windows Notepad backdoor.[^1]  |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS uses encoded strings in its process kill list.[^1]   |
| [S0607](https://attack.mitre.org/software/S0607) | KillDisk | KillDisk uses VMProtect to make reverse engineering the malware more difficult.[^1]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker has obfuscated its code to prevent its removal from host machines.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can encrypt strings with XOR-based routines and use a custom AES storage format for plugins, configuration, C2 domains, and harvested data.[^1] [^2] [^3]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed has the ability to Base64 encode its payload and custom encrypt API calls.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape itself is obfuscated and uses obfuscated API calls.[^1]  |
| [S0624](https://attack.mitre.org/software/S0624) | Ecipekac | Ecipekac can use XOR, AES, and DES to encrypt loader shellcode.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba has used multiple layers of obfuscation to avoid analysis, including its Base64 encoded payload.[^1]   |
| [S0627](https://attack.mitre.org/software/S0627) | SodaMaster | SodaMaster can use "stackstrings" for obfuscation.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent has used Rotate on Right (RoR) and Rotate on Left (RoL) functionality to encrypt strings.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox can encrypt data using AES prior to exfiltration.[^1]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon has used encrypted strings.[^1]  |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos encrypts all strings using RC4 and bundles all functionality into a single function call.[^1]   |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian can use VMProtect for obfuscation.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has hidden code within Excel spreadsheets by turning the font color to white and splitting it across multiple cells.[^1]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon used the "StackStrings" obfuscation technique to hide malicious functionalities.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol has Base64 encoded the RSA public key used for encrypting files.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | The Clambling executable has been obfuscated when dropped on a compromised host.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has obfuscated the fingerprint of the victim system, the local IP address, and the Fowler-Noll-V 1 (FNV-1) hash of the local IP address using an XOR operation. The data is then sent to the C2 server.[^1]   |
| [S0690](https://attack.mitre.org/software/S0690) | Green Lambert | Green Lambert has encrypted strings.[^1] [^2]   |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can be partly encrypted with XOR.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has been delivered within ZIP or RAR password-protected archived files.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot has been obfuscated to help avoid detection.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has obfuscated strings such as antivirus vendor names, domains, files, and others.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT |  Action RAT's commands, strings, and domains can be Base64 encoded within the payload.[^1]  |
| [S1035](https://attack.mitre.org/software/S1035) | Small Sieve | Small Sieve has the ability to use a custom hex byte swapping encoding scheme combined with an obfuscated Base64 function to protect program strings and Telegram credentials.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee has been delivered as password-protected zipped ISO files and used control-flow-flattening to obfuscate the flow of functions.[^2] [^1] [^3]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has used XOR-encoded strings.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has used encrypted payload files and maintains an encrypted configuration structure in memory.[^2] [^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can encrypt victim data with an RC4 cipher.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla has been obfuscated with the DeepSea .NET and ConfuserEx code obfuscators.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic can use certain ConfuserEx features for obfuscation and can be encoded in a base64 string.[^1]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 has the ability to obfuscate strings using XOR encryption.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can obfuscate strings using the congruential generator `(LCG): staten+1 = (690069 × staten + 1) mod 232`.[^1] <br> |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai can encrypt the names of requested APIs.[^1]  |
| [S1104](https://attack.mitre.org/software/S1104) | SLOWPULSE | SLOWPULSE can hide malicious code in the padding regions between legitimate functions in the Pulse Secure `libdsplibs.so` file.[^1]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER can store obfuscated configuration information in the last 56 bytes of the file `/date/.bd.key/preload.so`.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate uses a hard-coded string as a seed, along with the victim machine hardware identifier and input text, to generate a unique string used as an internal mutex value to evade static detection based on mutexes.[^1]  |
| [S1118](https://attack.mitre.org/software/S1118) | BUSHWALK | BUSHWALK can encrypt the resulting data generated from C2 commands with RC4.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin uses mixed-case letters for filenames and commands to evade detection.[^1]  |
| [S1138](https://attack.mitre.org/software/S1138) | Gootloader | <br>The Gootloader first stage script is obfuscated using random alpha numeric strings.[^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can use a custom Base64 alphabet to encode an API decryption key.[^1]  |
| [S1161](https://attack.mitre.org/software/S1161) | BPFDoor | BPFDoor can require a password to activate the backdoor and uses RC4 encryption or static library encryption `libtomcrypt`.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer has been distributed in ISO archives.[^1]  StrelaStealer has been delivered in encrypted, password-protected ZIP archives.[^2]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has used SmartAssembly to obfuscate .NET payloads.[^1]  |
| [S1226](https://attack.mitre.org/software/S1226) | BOOKWORM | BOOKWORM has been delivered using self-extracting RAR archives.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has obfuscated DLL names using the ror13AddHash32 algorithm.[^1]  |
| [S9007](https://attack.mitre.org/software/S9007) | HTTPTroy | HTTPTroy has obfuscated strings using Single Instruction Multiple Data (SIMD) instructions to hinder analysis and detection.[^1]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has utilized double-base64 encoding to store stolen secrets within the Github Action Logs within the victim account.[^1] [^2] [^3] [^5]  Shai-Hulud has also leveraged three layers of base64 encoding of exfiltrated data for anti-forensic purposes.[^4]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has utilized Go libraries to include Garble to obfuscate code.[^1] [^2]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO has used control flow flattening to obfuscate code.[^1]  |
| [S9025](https://attack.mitre.org/software/S9025) | NOOPLDR | NOOPLDR can use control flow flattening to help hide malicious code.[^2] [^1]  |
| [S9027](https://attack.mitre.org/software/S9027) | ANELLDR | ANELLDR code implements anti-analysis techniques including control flow flattening and Mixed Boolean Arithmetic (MBA).[^1]  |
| [S9033](https://attack.mitre.org/software/S9033) | Fooder | Fooder has stored its embedded payload in encrypted form within the binary, using a hardcoded key modified at runtime to produce the AES decryption key.[^1]  |
| [S9037](https://attack.mitre.org/software/S9037) | RustyWater | RustyWater has an obfuscated function (i.e. love_me__()) that dynamically reconstructs the string WScript.Shell using hard-coded ASCII values and the Chr() function.[^1]       |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Ensure that a finite amount of ingress points to a software deployment system exist with restricted access for those required to allow and enable newly deployed software. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10+, enable Attack Surface Reduction (ASR) rules to prevent execution of potentially obfuscated payloads. [^1]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Consider periodic review of common fileless storage locations (such as the Registry or WMI repository) to potentially identify abnormal and malicious data. |
| [[kb/mitre/attack/mitigations/M1049-antivirus-antimalware\|M1049]] | Antivirus/Antimalware | Anti-virus can be used to automatically detect and quarantine suspicious files. Consider utilizing the Antimalware Scan Interface (AMSI) on Windows 10+ to analyze commands after being processed/interpreted. [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1027.011-fileless-storage\|T1027.011]] | Fileless Storage |
| [[kb/mitre/attack/techniques/T1027.009-embedded-payloads\|T1027.009]] | Embedded Payloads |
| [[kb/mitre/attack/techniques/T1027.013-encrypted-encoded-file\|T1027.013]] | Encrypted／Encoded File |
| [[kb/mitre/attack/techniques/T1027.008-stripped-payloads\|T1027.008]] | Stripped Payloads |
| [[kb/mitre/attack/techniques/T1027.001-binary-padding\|T1027.001]] | Binary Padding |
| [[kb/mitre/attack/techniques/T1027.016-junk-code-insertion\|T1027.016]] | Junk Code Insertion |
| [[kb/mitre/attack/techniques/T1027.017-svg-smuggling\|T1027.017]] | SVG Smuggling |
| [[kb/mitre/attack/techniques/T1027.012-lnk-icon-smuggling\|T1027.012]] | LNK Icon Smuggling |
| [[kb/mitre/attack/techniques/T1027.005-indicator-removal-from-tools\|T1027.005]] | Indicator Removal from Tools |
| [[kb/mitre/attack/techniques/T1027.014-polymorphic-code\|T1027.014]] | Polymorphic Code |
| [[kb/mitre/attack/techniques/T1027.003-steganography\|T1027.003]] | Steganography |
| [[kb/mitre/attack/techniques/T1027.004-compile-after-delivery\|T1027.004]] | Compile After Delivery |
| [[kb/mitre/attack/techniques/T1027.006-html-smuggling\|T1027.006]] | HTML Smuggling |
| [[kb/mitre/attack/techniques/T1027.010-command-obfuscation\|T1027.010]] | Command Obfuscation |
| [[kb/mitre/attack/techniques/T1027.002-software-packing\|T1027.002]] | Software Packing |
| [[kb/mitre/attack/techniques/T1027.018-invisible-unicode\|T1027.018]] | Invisible Unicode |
| [[kb/mitre/attack/techniques/T1027.007-dynamic-api-resolution\|T1027.007]] | Dynamic API Resolution |
| [[kb/mitre/attack/techniques/T1027.015-compression\|T1027.015]] | Compression |

 [^1]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^2]: [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)
 [^3]: [FireEye Revoke-Obfuscation July 2017](https://www.blackhat.com/docs/us-17/thursday/us-17-Bohannon-Revoke-Obfuscation-PowerShell-Obfuscation-Detection-And%20Evasion-Using-Science-wp.pdf)
 [^4]: [Linux/Cdorked.A We Live Security Analysis](https://www.welivesecurity.com/2013/04/26/linuxcdorked-new-apache-backdoor-in-the-wild-serves-blackhole/)
 [^5]: [Carbon Black Obfuscation Sept 2016](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)
 [^6]: [PaloAlto EncodedCommand March 2017](https://researchcenter.paloaltonetworks.com/2017/03/unit42-pulling-back-the-curtains-on-encodedcommand-powershell-attacks/)
 [^7]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
 [^8]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^9]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
 [^10]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)
 [^11]: [Socket Shai-Hulud Trufflehog September 2025](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages)
 [^12]: [Microsoft Sliver 2022](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)
 [^13]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
 [^14]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^15]: [Infoblox Lokibot January 2019](https://insights.infoblox.com/threat-intelligence-reports/threat-intelligence--22)
 [^16]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^17]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
 [^18]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
 [^19]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^20]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^21]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
 [^22]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^23]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^24]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^25]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^26]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)
 [^27]: [CISA EB Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-239a)
 [^28]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
 [^29]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^30]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
 [^31]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^32]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
 [^33]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^34]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
 [^35]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
 [^36]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
 [^37]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^38]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^39]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
 [^40]: [FireEye Clandestine Wolf](https://www.fireeye.com/blog/threat-research/2015/06/operation-clandestine-wolf-adobe-flash-zero-day.html)
 [^41]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
 [^42]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^43]: [CoinTicker 2019](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)
 [^44]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^45]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^46]: [CISA ComRAT Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
 [^47]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
 [^48]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
 [^49]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^50]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
 [^51]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^52]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^53]: [Cisco H1N1 Part 1](http://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities)
 [^54]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^55]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
 [^56]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^57]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^58]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^59]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
 [^60]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
 [^61]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^62]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
 [^63]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^64]: [Check Point Sunburst Teardrop December 2020](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)
 [^65]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
 [^66]: [CopyKittens Nov 2015](https://cdn2.hubspot.net/hubfs/1903456/Whitepapers/CopyKittens.pdf)
 [^67]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^68]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
 [^69]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^70]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
 [^71]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)
 [^72]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^73]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)
 [^74]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^75]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^76]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^77]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
 [^78]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
 [^79]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^80]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
 [^81]: [Talos Remcos Aug 2018](https://blog.talosintelligence.com/2018/08/picking-apart-remcos.html)
 [^82]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
 [^83]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
 [^84]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^85]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
 [^86]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^87]: [Trend Micro KillDisk 1](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
 [^88]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
 [^89]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^90]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^91]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
 [^92]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^93]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^94]: [Trend Micro Daserf Nov 2017](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)
 [^95]: [ESET Ebury Feb 2014](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)
 [^96]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^97]: [Cybereason Conti Jan 2021](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
 [^98]: [ESET Kobalos Feb 2021](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)
 [^99]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^100]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^101]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
 [^102]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^103]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^104]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
 [^105]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^106]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
 [^107]: [OilRig New Delivery Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-oilrig-group-steps-attacks-new-delivery-documents-new-injector-trojan/)
 [^108]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)
 [^109]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
 [^110]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
 [^111]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
 [^112]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
 [^113]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^114]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)
 [^115]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^116]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^117]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)
 [^118]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
 [^119]: [Trend Micro Conficker](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
 [^120]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^121]: [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
 [^122]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
 [^123]: [Securelist ShadowPad Aug 2017](https://securelist.com/shadowpad-in-corporate-networks/81432/)
 [^124]: [FireEye Ransomware Feb 2020](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
 [^125]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^126]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^127]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^128]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^129]: [Threatpost Hancitor](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)
 [^130]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
 [^131]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^132]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^133]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
 [^134]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^135]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^136]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^137]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
 [^138]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
 [^139]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
 [^140]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^141]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
 [^142]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^143]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^144]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^145]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^146]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)
 [^147]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^148]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^149]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
 [^150]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
 [^151]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^152]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
 [^153]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^154]: [jRAT Symantec Aug 2018](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
 [^155]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
 [^156]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
 [^157]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
 [^158]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^159]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^160]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
 [^161]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^162]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
 [^163]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^164]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^165]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
 [^166]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
 [^167]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^168]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^169]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
 [^170]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^171]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^172]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^173]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^174]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
 [^175]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)
