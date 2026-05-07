---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1140
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1140-deobfuscate-decode-files-or-information
tactic:
    - Stealth
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information|Obfuscated Files or Information]] to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present on the system.<br><br>One such example is the use of [[kb/mitre/attack/software/S0160-certutil|certutil]] to decode a remote access tool portable executable file that has been hidden inside a certificate file.[^3]  Another example is using the Windows `copy /b` or `type` command to reassemble binary fragments into a malicious payload.[^4] [^2] <br><br>Sometimes a user's action may be required to open it for deobfuscation or decryption as part of [[kb/mitre/attack/techniques/T1204-user-execution|User Execution]]. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor can use a stream cipher to decrypt stings used by the malware.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX decompresses and decrypts itself using the Microsoft API call RtlDecompressBuffer.[^3] [^5] [^6]  PlugX has also decrypted its payloads in memory.[^1] [^2] [^4] [^7]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can decrypt command parameters sent through C2 and use unpacking code to extract its packed executable.[^1]  |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre decrypts resources needed for targeting the victim.[^1] [^2]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has decrypted and loaded the gh0st RAT DLL into memory, once the initial dropper executable is launched.[^1]  |
| [S0052](https://attack.mitre.org/software/S0052) | OnionDuke | OnionDuke can use a custom decryption algorithm to decrypt strings.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can decode its encoded PE file prior to execution.[^1]  |
| [S0126](https://attack.mitre.org/software/S0126) | ComRAT | ComRAT has used unique per machine passwords to decrypt the orchestrator payload and a hardcoded XOR key to decrypt its communications module. ComRAT has also used a unique password to decrypt the file used for its hidden file system.[^1] [^2]  |
| [S0127](https://attack.mitre.org/software/S0127) | BBSRAT | BBSRAT uses [[kb/mitre/attack/software/S0361-expand\|Expand]] to decompress a CAB file into executable content.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon decrypts ciphertext using an XOR cipher and a base64-encoded string.[^1] 	 |
| [S0141](https://attack.mitre.org/software/S0141) | Winnti for Windows | The Winnti for Windows dropper can decrypt and decompresses a data blob.[^1]  |
| [S0147](https://attack.mitre.org/software/S0147) | Pteranodon | Pteranodon can decrypt encrypted data strings prior to using them.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can deobfuscate shellcode using a rolling XOR and decrypt metadata from Beacon sessions.[^1] [^2]  The Cobalt Strike loader component can also decrypt the .bss section of the Beacon binary prior to execution.[^3]  |
| [[kb/mitre/attack/software/S0160-certutil\|S0160]] | certutil | [[kb/mitre/attack/software/S0160-certutil\|certutil]] has been used to decode binaries hidden inside certificate files as Base64 information.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer deobfuscates its strings and APIs once its executed.[^1]  |
| [S0182](https://attack.mitre.org/software/S0182) | FinFisher | FinFisher extracts and decrypts stage 3 malware, which is stored in encrypted resources.[^2] [^1]  |
| [S0188](https://attack.mitre.org/software/S0188) | Starloader | Starloader decrypts and executes shellcode from a file called Stars.jps.[^1]  |
| [S0189](https://attack.mitre.org/software/S0189) | ISMInjector | ISMInjector uses the `certutil` command to decode a payload file.[^1]  |
| [S0196](https://attack.mitre.org/software/S0196) | PUNCHBUGGY | PUNCHBUGGY has used [[kb/mitre/attack/techniques/T1059.001-powershell\|PowerShell]] to decode base64-encoded assembly.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can deobfuscate the main backdoor code.[^1]  |
| [S0226](https://attack.mitre.org/software/S0226) | Smoke Loader | Smoke Loader deobfuscates its code.[^1]  |
| [S0230](https://attack.mitre.org/software/S0230) | ZeroT | ZeroT shellcode decrypts and decompresses its RC4-encrypted payload.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook has decoded its PowerShell script.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs decrypts and extracts a copy of its main DLL payload when executing.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot decodes embedded XOR strings.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can decrypt strings using the victim's hostname as the key.[^1] [^2]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy decodes its secondary payload and writes it to the victim’s machine. Zebrocy also uses AES and XOR to decrypt strings and payloads.[^1] [^2]  |
| [S0255](https://attack.mitre.org/software/S0255) | DDKONG | DDKONG decodes an embedded configuration using XOR.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN decrypts code, strings, and commands to use once it's on the victim's machine.[^1]  |
| [S0258](https://attack.mitre.org/software/S0258) | RGDoor | RGDoor decodes Base64 strings and decrypts strings using a custom XOR algorithm.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can decrypt, unpack and load a DLL from its resources, or from blobs encrypted with Data Protection API, two-key triple DES, and variations of the XOR cipher.[^1] [^2]  |
| [S0263](https://attack.mitre.org/software/S0263) | TYPEFRAME | One TYPEFRAME variant decrypts an archive using an RC4 key, then decompresses and installs the decrypted malicious DLL module. Another variant decodes the embedded file by XORing it with the value "0x35".[^1]  |
| [S0264](https://attack.mitre.org/software/S0264) | OopsIE | OopsIE concatenates then decompresses multiple resources to load an embedded .Net Framework assembly.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot decodes the configuration data and modules.[^1] [^2] [^3]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has decoded strings in the malware using XOR and RC4.[^1] [^2]   |
| [S0269](https://attack.mitre.org/software/S0269) | QUADAGENT | QUADAGENT uses AES and a preshared key to decrypt the custom Base64 routine used to encode strings and scripts.[^1]  |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin decodes an embedded executable using base64 and decompresses it.[^1]  |
| [S0279](https://attack.mitre.org/software/S0279) | Proton | Proton uses an encrypted file to store commands and configuration values.[^1]  |
| [S0280](https://attack.mitre.org/software/S0280) | MirageFox | MirageFox has a function for decrypting data containing C2 configuration information.[^1]  |
| [S0284](https://attack.mitre.org/software/S0284) | More_eggs | More_eggs will decode malware components that are then dropped to the system.[^1]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda decrypts strings in the code during the execution process.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla has the ability to decrypt strings encrypted with the Rijndael symmetric encryption algorithm.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon decrypts task and configuration files for execution.[^2] [^1]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult uses an XOR key to decrypt content and uses Base64 to decode the C2 address.[^1] [^2]  |
| [S0347](https://attack.mitre.org/software/S0347) | AuditCred | AuditCred uses XOR and RC4 to perform decryption on the code functions.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT decodes many of its artifacts and is decrypted (AES-128) after being downloaded.[^1]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D uses a decode routine combining bit shifting and XOR operations with a variable key that depends on the length of the string that was encoded. If the computation for the variable XOR key turns out to be 0, the default XOR key of 0x1B is used. This routine is also referenced as the `rotate` function in reporting.[^1]  |
| [S0353](https://attack.mitre.org/software/S0353) | NOKKI | NOKKI uses a unique, custom de-obfuscation technique.[^1]  |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis will decrypt important strings used for C&C communication.[^1]  |
| [S0355](https://attack.mitre.org/software/S0355) | Final1stspy | Final1stspy uses Python code to deobfuscate base64-encoded strings.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has used certutil to download and decode base64 encoded strings and has also devoted a custom section to performing all the components of the deobfuscation process.[^1] [^2]  |
| [[kb/mitre/attack/software/S0361-expand\|S0361]] | Expand | [[kb/mitre/attack/software/S0361-expand\|Expand]] can be used to decompress a local or remote CAB file into an executable.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has used a self-extracting RAR file to deliver modules to victims. Emotet has also extracted embedded executables from files using hard-coded buffer offsets.[^1]  |
| [S0369](https://attack.mitre.org/software/S0369) | CoinTicker | CoinTicker decodes the initially-downloaded hidden encoded file using OpenSSL.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth uses a fromCharCode() deobfuscation method to avoid explicitly writing execution commands and to hide its code. [^1] [^2]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi decrypts the configuration data using XOR with 25-character keys.[^1]  |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury has verified C2 domain ownership by decrypting the TXT record using an embedded RSA public key.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used crypto key information stored in the Registry to decrypt Tor clients dropped to disk.[^1]  |
| [S0388](https://attack.mitre.org/software/S0388) | YAHOYAH | YAHOYAH decrypts downloaded files before execution.[^1]  |
| [S0390](https://attack.mitre.org/software/S0390) | SQLRat | SQLRat has scripts that are responsible for deobfuscating additional scripts.[^1]  |
| [S0394](https://attack.mitre.org/software/S0394) | HiddenWasp | HiddenWasp uses a cipher to implement a decoding function.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron has used AES and XOR to decrypt configuration files and commands.[^1]  |
| [S0398](https://attack.mitre.org/software/S0398) | HyperBro | HyperBro can unpack and decrypt its payload prior to execution.[^1] [^2]  |
| [S0401](https://attack.mitre.org/software/S0401) | Exaramel for Linux | Exaramel for Linux can decrypt its configuration file.[^1]  |
| [S0402](https://attack.mitre.org/software/S0402) | OSX/Shlayer | OSX/Shlayer can base64-decode and AES-decrypt downloaded payloads.[^1]  Versions of OSX/Shlayer pass encrypted and password-protected code to `openssl` and then write the payload to the `/tmp` folder.[^2] [^3]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete’s downloaded data is decrypted using AES.[^1]  |
| [S0414](https://attack.mitre.org/software/S0414) | BabyShark | BabyShark has the ability to decode downloaded files prior to execution.[^1]  |
| [S0415](https://attack.mitre.org/software/S0415) | BOOSTWRITE | BOOSTWRITE has used a a 32-byte long multi-XOR key to decode data inside its payload.[^1] 	 |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has used LZMA and base64 libraries to decode obfuscated scripts.[^1]  |
| [S0430](https://attack.mitre.org/software/S0430) | Winnti for Linux | Winnti for Linux has decoded XOR encoded strings holding its configuration upon execution.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has decoded malware components that are then dropped to the system.[^1]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie has the ability to decrypt, load, and execute a DLL and its resources.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum's loader can decrypt the backdoor code, embedded within the loader or within a legitimate PNG file. A custom XOR cipher or RC4 is used for decryption.[^1]  |
| [S0443](https://attack.mitre.org/software/S0443) | MESSAGETAP | After checking for the existence of two files, keyword_parm.txt and parm.txt, MESSAGETAP XOR decodes and read the contents of the files. [^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat has decompressed its core DLL using shellcode once an impersonated antivirus component was running on a system.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has decoded and decrypted its stages multiple times using hard-coded keys to deliver the final payload, and has decoded its server response hex string using XOR.[^1]  |
| [S0448](https://attack.mitre.org/software/S0448) | Rising Sun | Rising Sun has decrypted itself using a single-byte XOR scheme. Additionally, Rising Sun can decrypt its configuration data at runtime.[^1] 	 |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Upon execution, Metamorfo has unzipped itself after being downloaded to the system and has performed string decryption.[^1] [^2] [^3]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to decrypt the loader configuration and payload DLL.[^1]  |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker's PowerShell script can decode and decrypt multiple layers of obfuscation, leading to the Netwalker DLL being loaded into memory.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can extract its agent from the body of a malicious document.[^1] 	 |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to decrypt and decompress its payload to enable code execution.[^2] [^1]  |
| [S0466](https://attack.mitre.org/software/S0466) | WindTail | WindTail has the ability to decrypt strings using hard-coded AES keys.[^1]  |
| [S0468](https://attack.mitre.org/software/S0468) | Skidmap | Skidmap has the ability to download, unpack, and decrypt tar.gz files .[^1]   |
| [S0469](https://attack.mitre.org/software/S0469) | ABK | ABK has the ability to decrypt AES encrypted payloads.[^1]  |
| [S0470](https://attack.mitre.org/software/S0470) | BBK | BBK has the ability to decrypt AES encrypted payloads.[^1]  |
| [S0473](https://attack.mitre.org/software/S0473) | Avenger | Avenger has the ability to decrypt files downloaded from C2.[^1]  |
| [S0475](https://attack.mitre.org/software/S0475) | BackConfig | BackConfig has used a custom routine to decrypt strings.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has the ability to decode and decrypt downloaded files.[^1] [^2]  |
| [S0477](https://attack.mitre.org/software/S0477) | Goopy | Goopy has used a polymorphic decryptor to decrypt itself at runtime.[^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore has used `openssl` to decrypt AES encrypted payload data. Bundlore has also used base64 and RC4 with a hardcoded key to deobfuscate data.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel has decrypted the binary's configuration once the `main` function was launched.[^1]  |
| [S0492](https://attack.mitre.org/software/S0492) | CookieMiner | CookieMiner has used Google Chrome's decryption and extraction operations.[^1]  |
| [S0495](https://attack.mitre.org/software/S0495) | RDAT | RDAT can deobfuscate the base64-encoded and AES-encrypted files downloaded from the C2 server.[^1] 	 |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can decode encrypted strings to enable execution of commands and payloads.[^1] [^2] [^3] [^4] [^5] [^6]  |
| [S0499](https://attack.mitre.org/software/S0499) | Hancitor | Hancitor has decoded Base64 encoded URLs to insert a recipient’s name into the filename of the Word document. Hancitor has also extracted executables from ZIP files.[^1] [^2]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon can decrypt password-protected executables.[^1]  |
| [S0502](https://attack.mitre.org/software/S0502) | Drovorub | Drovorub has de-obsfuscated XOR encrypted payloads in WebSocket messages.[^1]  |
| [S0511](https://attack.mitre.org/software/S0511) | RegDuke | RegDuke can decrypt strings with a key either stored in the Registry or hardcoded in the code.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke can decrypt AES encrypted C2 communications.[^1]  |
| [S0513](https://attack.mitre.org/software/S0513) | LiteDuke | LiteDuke has the ability to decrypt and decode multiple layers of obfuscation.[^1]  |
| [S0514](https://attack.mitre.org/software/S0514) | WellMess | WellMess can decode and decrypt data received from C2.[^1] [^2] [^3]  |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail can decompress scripts received from C2.[^1]  |
| [S0516](https://attack.mitre.org/software/S0516) | SoreFang | SoreFang can decode and decrypt exfiltrated data sent to C2.[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint has been decompressed by included shellcode prior to being launched.[^1] 	 |
| [S0518](https://attack.mitre.org/software/S0518) | PolyglotDuke | PolyglotDuke can use a custom algorithm to decrypt strings used by the malware.[^1]  |
| [S0520](https://attack.mitre.org/software/S0520) | BLINDINGCAN | BLINDINGCAN has used AES and XOR to decrypt its DLLs.[^1]  |
| [S0526](https://attack.mitre.org/software/S0526) | KGH_SPY | KGH_SPY can decrypt encrypted strings and write them to a newly created folder.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can decrypt its encrypted internal strings.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can decrypt its C2 address upon execution.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can decrypt downloaded payloads. Bazar also resolves strings and other artifacts at runtime.[^1] [^2]  |
| [S0543](https://attack.mitre.org/software/S0543) | Spark | Spark has used a custom XOR algorithm to decrypt the payload.[^1]   |
| [S0546](https://attack.mitre.org/software/S0546) | SharpStage | SharpStage has decompressed data received from the C2 server.[^1]  |
| [S0547](https://attack.mitre.org/software/S0547) | DropBook | DropBook can unarchive data downloaded from the C2 to obtain the payload and persistence modules.[^1]   |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has been decrypted before execution.[^1] [^2]   |
| [S0560](https://attack.mitre.org/software/S0560) | TEARDROP | TEARDROP was decoded using a custom rolling XOR algorithm to execute a customized Cobalt Strike payload.[^1] [^2] [^3]  |
| [S0562](https://attack.mitre.org/software/S0562) | SUNSPOT | SUNSPOT decrypts SUNBURST, which was stored in AES128-CBC encrypted blobs.[^1]    |
| [S0565](https://attack.mitre.org/software/S0565) | Raindrop | Raindrop decrypted its Cobalt Strike payload using an AES-256 encryption algorithm in CBC mode with a unique key per sample.[^1] [^2]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack has used a decryption routine that is part of an executable physical patch.[^1]  |
| [S0574](https://attack.mitre.org/software/S0574) | BendyBear | BendyBear has decrypted function blocks using a XOR key during runtime to evade detection.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti has decrypted its payload using a hardcoded AES-256 key.[^1] [^2]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex has used a Base64 key to decode its components.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear has the ability to decrypt its RC4 encrypted payload for execution.[^1]  |
| [[kb/mitre/attack/software/S0581-ironnetinjector\|S0581]] | IronNetInjector | [[kb/mitre/attack/software/S0581-ironnetinjector\|IronNetInjector]] has the ability to decrypt embedded .NET and PE payloads.[^1]  |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack has a function that decrypts malicious data.[^1]  |
| [S0584](https://attack.mitre.org/software/S0584) | AppleJeus | AppleJeus has decoded files received from a C2.[^1]  |
| [S0585](https://attack.mitre.org/software/S0585) | Kerrdown | Kerrdown can decode, decrypt, and decompress multiple layers of shellcode.[^1]  |
| [S0588](https://attack.mitre.org/software/S0588) | GoldMax | GoldMax has decoded and decrypted the configuration file when executed.[^1] [^2]  |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot can decrypt data received from a C2 and save to a file.[^1]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has decrypted a binary blob to start execution.[^1]  |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell can use a decryption mechanism to process a user supplied password and allow execution.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has decrypted ELF files with AES.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet decrypts resources that are loaded into memory and executed.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer decrypts code to connect to a remote C2 server.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist can decode and decrypt messages received from C2.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop has used a simple XOR operation to decrypt strings.[^1]  |
| [S0612](https://attack.mitre.org/software/S0612) | WastedLocker | WastedLocker's custom cryptor, CryptOne, used an XOR based algorithm to decrypt the payload.[^1]  |
| [S0613](https://attack.mitre.org/software/S0613) | PS1 | PS1 can use an XOR key to decrypt a PowerShell loader and payload binary.[^1]  |
| [S0614](https://attack.mitre.org/software/S0614) | CostaBricks | CostaBricks has the ability to use bytecode to decrypt embedded payloads.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can run `upload` to decrypt and upload files from storage.[^1] [^2]  |
| [S0618](https://attack.mitre.org/software/S0618) | FIVEHANDS | FIVEHANDS has the ability to decrypt its payload prior to execution.[^1] [^2] [^3]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can decode its payload prior to execution.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape has decrypted the password of the C2 server with a simple byte by byte XOR. Siloscape also writes both an archive of [[kb/mitre/attack/software/S0183-tor\|Tor]] and the `unzip` binary to disk from data embedded within the payload using Visual Studio’s Resource Manager.[^1]  |
| [S0624](https://attack.mitre.org/software/S0624) | Ecipekac | Ecipekac has the ability to decrypt fileless loader modules.[^1]  |
| [S0628](https://attack.mitre.org/software/S0628) | FYAnti | FYAnti has the ability to decrypt an embedded .NET module.[^1]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can decrypt its payload via a XOR key.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has decrypted an AES encrypted binary file to trigger the download of other files.[^1]   |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent can use a decryption algorithm for strings based on Rotate on Right (RoR) and Rotate on Left (RoL) functionality.[^1]  |
| [S0634](https://attack.mitre.org/software/S0634) | EnvyScout | EnvyScout can deobfuscate and write malicious ISO files to disk.[^1]  |
| [S0635](https://attack.mitre.org/software/S0635) | BoomBox | BoomBox can decrypt AES-encrypted files downloaded from C2.[^1]  |
| [S0636](https://attack.mitre.org/software/S0636) | VaporRage | VaporRage can deobfuscate XOR-encoded shellcode prior to execution.[^1]  |
| [S0637](https://attack.mitre.org/software/S0637) | NativeZone | NativeZone can decrypt and decode embedded  Cobalt Strike beacon stage shellcode.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk has the ability to unpack itself into memory using XOR.[^1] [^2]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon has decrypted encrypted strings.[^1]  |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos decrypts strings right after the initial communication, but before the authentication process.[^1]   |
| [S0642](https://attack.mitre.org/software/S0642) | BADFLICK | BADFLICK can decode shellcode using a custom rotating XOR cipher.[^1]  |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian has the ability to use a XOR decryption key to extract C2 server domains and IP addresses.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can deobfuscate and re-assemble code strings for execution.[^1] [^2] [^3]  |
| [S0653](https://attack.mitre.org/software/S0653) | xCaon | xCaon has decoded strings from the C2 server before executing commands.[^1]   |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can deobfuscate its payload prior to execution.[^1] [^2]  |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb can be decrypted in memory using a Lightweight Encryption Algorithm (LEA)-128 key and decoded using a XOR key.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can deobfuscate packed binaries in memory.[^1]  |
| [S0665](https://attack.mitre.org/software/S0665) | ThreatNeedle | ThreatNeedle can decrypt its payload using RC4, AES, or one-byte XORing.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can decompress and decrypt DLLs and shellcode.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can decrypt its encrypted internal code.[^1]  |
| [S0669](https://attack.mitre.org/software/S0669) | KOCTOPUS | KOCTOPUS has deobfuscated itself before executing its commands.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can use XOR 0x45 to decrypt obfuscated code.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman has the ability to self-extract as a RAR archive.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can decrypt downloaded modules prior to execution.[^1]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma has used XOR and Base64 to decode C2 data.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has decrypted its configuration data, such as the C2 IP address, ports and other network communication.[^1] [^2]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can decrypt and parse instructions sent from C2.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can deobfuscate downloaded files stored in reverse byte order and decrypt embedded resources using multiple XOR operations.[^1] [^2]  |
| [S0690](https://attack.mitre.org/software/S0690) | Green Lambert | Green Lambert can use multiple custom routines to decrypt strings prior to execution.[^1] [^2]  |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper can decompress and copy driver files using `LZCopy`.[^1]  |
| [S1012](https://attack.mitre.org/software/S1012) | PowerLess | PowerLess can use base64 and AES ECB decryption prior to execution of downloaded modules.[^1]  |
| [S1013](https://attack.mitre.org/software/S1013) | ZxxZ | ZxxZ has used a XOR key to decrypt strings.[^1]  |
| [S1014](https://attack.mitre.org/software/S1014) | DanBot | DanBot can use a VBA macro to decode its payload prior to installation and execution.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa decrypts a downloaded file using AES-128-EBC with a custom delta.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot can deobfuscate strings and files for execution.[^1]  |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark can extract and decrypt downloaded .zip files.[^1]  |
| [S1022](https://attack.mitre.org/software/S1022) | IceApple | IceApple can use a Base64-encoded AES key to decrypt tasking.[^1]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey has decoded antivirus name strings.[^1]  |
| [S1026](https://attack.mitre.org/software/S1026) | Mongall | Mongall has the ability to decrypt its payload prior to execution.[^1]  |
| [S1027](https://attack.mitre.org/software/S1027) | Heyoka Backdoor | Heyoka Backdoor can decrypt its payload prior to execution.[^1]  |
| [S1028](https://attack.mitre.org/software/S1028) | Action RAT | Action RAT can use Base64 to decode actor-controlled C2 server communications.[^1]  |
| [S1030](https://attack.mitre.org/software/S1030) | Squirrelwaffle | Squirrelwaffle has decrypted files and payloads using a XOR-based algorithm.[^1] [^2]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull | PingPull can decrypt received data from its C2 server by using AES.[^1]  |
| [S1032](https://attack.mitre.org/software/S1032) | PyDCrypt | PyDCrypt has decrypted and dropped the DCSrv payload to disk.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can deobfuscate C2 server responses and unpack its code on targeted hosts.[^1] [^2]  |
| [S1041](https://attack.mitre.org/software/S1041) | Chinoxy | The Chinoxy dropping function can initiate decryption of its config file.[^1]  |
| [S1046](https://attack.mitre.org/software/S1046) | PowGoop | PowGoop can decrypt PowerShell scripts for execution.[^2] [^1]  |
| [S1047](https://attack.mitre.org/software/S1047) | Mori | Mori can resolve networking APIs from strings that are ADD-encrypted.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm.[^1]  |
| [S1051](https://attack.mitre.org/software/S1051) | KEYPLUG | KEYPLUG can decode its configuration file to determine C2 protocols.[^1]  |
| [S1052](https://attack.mitre.org/software/S1052) | DEADEYE | DEADEYE has the ability to combine multiple sections of a binary which were broken up to evade detection into a single .dll prior to execution.[^1]  |
| [S1053](https://attack.mitre.org/software/S1053) | AvosLocker | AvosLocker has deobfuscated XOR-encoded strings.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can decrypt and load other modules.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can decrypt files and data.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to deobfuscate its payload prior to execution.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT can deobfuscate Base64-encoded strings and scripts.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can decrypt its payload and associated configuration elements using the Rijndael cipher.[^1]  |
| [S1076](https://attack.mitre.org/software/S1076) | QUIETCANARY | QUIETCANARY can use a custom parsing routine to decode the command codes and additional parameters from the C2 before executing them.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | RotaJakiro uses the AES algorithm, bit shifts in a function called `rotate`, and an XOR cipher to decrypt resources required for persistence, process guarding, and file locking. It also performs this same function on encrypted stack strings and the `head` and `key` sections in the network packet structure used for C2 communications.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic can first decrypt with the RC4 algorithm using a hardcoded decryption key before decompressing.[^1]  |
| [S1086](https://attack.mitre.org/software/S1086) | Snip3 | Snip3 can decode its second-stage PowerShell script prior to execution.[^1]  |
| [S1097](https://attack.mitre.org/software/S1097) | HUI Loader | HUI Loader can decrypt and load files containing malicious payloads.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | The Ninja loader component can decrypt and decompress the payload.[^1] [^2]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER decodes configuration items from a bundled file for command and control activity.[^1]  |
| [S1110](https://attack.mitre.org/software/S1110) | SLIGHTPULSE | SLIGHTPULSE can deobfuscate base64 encoded and RC4 encrypted C2 messages.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate installation includes binary code stored in a file located in a hidden directory, such as `shell.txt`, that is decrypted then executed.[^1]  DarkGate uses hexadecimal-encoded shellcode payloads during installation that are called via Windows API `CallWindowProc()` to decode and then execute.[^2]  |
| [S1112](https://attack.mitre.org/software/S1112) | STEADYPULSE | STEADYPULSE can URL decode key/value pairs sent over C2.[^1]  |
| [S1113](https://attack.mitre.org/software/S1113) | RAPIDPULSE | RAPIDPULSE listens for specific HTTP query parameters in received communications. If specific parameters match, a hard-coded RC4 key is used to decrypt the HTTP query paremter `hmacTime`. This decrypts to a filename that is then open, read, encrypted with the same RC4 key, base64-encoded, written to standard out, then passed as a response to the HTTP request.[^1]  |
| [S1115](https://attack.mitre.org/software/S1115) | WIREFIRE | WIREFIRE can decode, decrypt, and decompress data received in C2 HTTP `POST` requests.[^1]  |
| [S1117](https://attack.mitre.org/software/S1117) | GLASSTOKEN | GLASSTOKEN has the ability to decode hexadecimal and Base64 C2 requests.[^1]  |
| [S1118](https://attack.mitre.org/software/S1118) | BUSHWALK | BUSHWALK can Base64 decode and RC4 decrypt malicious payloads sent through a web request’s command parameter.[^2] [^1]  |
| [S1119](https://attack.mitre.org/software/S1119) | LIGHTWIRE | LIGHTWIRE can RC4 decrypt and Base64 decode C2 commands.[^1]  |
| [S1120](https://attack.mitre.org/software/S1120) | FRAMESTING | FRAMESTING can decompress data received within `POST` requests.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu decrypts its encrypted configuration files prior to execution.[^2] [^1]  |
| [S1123](https://attack.mitre.org/software/S1123) | PITSTOP | PITSTOP can deobfuscate base64 encoded and AES encrypted commands.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin contains several layers of obfuscation to hide malicious code from detection and analysis.[^1]  |
| [S1133](https://attack.mitre.org/software/S1133) | Apostle | Apostle compiled code is obfuscated in an unspecified fashion prior to delivery to victims.[^1]  |
| [S1134](https://attack.mitre.org/software/S1134) | DEADWOOD | DEADWOOD XORs some strings within the binary using the value `0xD5`, and deobfuscates these items at runtime.[^1]  |
| [S1138](https://attack.mitre.org/software/S1138) | Gootloader | Gootloader has the ability to decode and decrypt malicious payloads prior to execution.[^2] [^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can run `CryptStringToBinaryA` to decrypt base64 content containing its ransom note.[^1]  |
| [S1140](https://attack.mitre.org/software/S1140) | Spica | Upon execution Spica can decode an embedded .pdf and write it to the desktop as a decoy document.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can decrypt strings related to communication configuration using RC4 with a static key.[^1]  |
| [S1142](https://attack.mitre.org/software/S1142) | LunarMail | LunarMail can decrypt strings to retrieve configuration settings.[^1]  |
| [S1143](https://attack.mitre.org/software/S1143) | LunarLoader | LunarLoader can deobfuscate files containing the next stages in the infection chain.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot decrypts command and control URIs using ADVobfuscator, and decrypts IP addresses and port numbers with a custom algorithm.[^1]  Other versions of Pikabot decode chunks of stored stage 2 payload content in the initial payload `.text` section before consolidating them for further execution.[^2]  Overall LunarMail is associated with multiple encoding and encryption mechanisms to obfuscate the malware's presence and avoid analysis or detection.[^3]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor stores network configuration data in a file XOR encoded with the key value of `0x7A`.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer uses RC4-encrypted, base64-encoded strings to obfuscate functionality and command and control servers.[^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can use an embedded RC4 key to decrypt Windows API function strings.[^1]  |
| [S1150](https://attack.mitre.org/software/S1150) | ROADSWEEP | ROADSWEEP can decrypt embedded scripts prior to execution.[^2] [^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer strings are deobfuscated prior to execution.[^1] [^2]  |
| [S1158](https://attack.mitre.org/software/S1158) | DUSTPAN | DUSTPAN decodes and decrypts embedded payloads.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP deobfuscates embedded payloads.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus has the ability to deobfuscate encrypted strings.[^2] [^3] [^1]  |
| [S1164](https://attack.mitre.org/software/S1164) | UPSTYLE | UPSTYLE encodes its main content prior to loading via Python as base64-encoded blobs.[^2] [^1]  |
| [S1168](https://attack.mitre.org/software/S1168) | SampleCheck5000 | SampleCheck5000 can decode and decrypt command line strings and files received through C2.[^2] [^1]  |
| [S1170](https://attack.mitre.org/software/S1170) | ODAgent | ODAgent can Base64-decode and XOR decrypt received C2 commands.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster can Base64-decode and XOR-decrypt C2 commands taken from JSON files.[^1]  |
| [S1173](https://attack.mitre.org/software/S1173) | PowerExchange | PowerExchange can decode and decrypt C2 commands received via email.[^1]  |
| [S1179](https://attack.mitre.org/software/S1179) | Exbyte | Exbyte decodes and decrypts data stored in the configuration file with a key provided on the command line during execution.[^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware is distributed as an obfuscated JavaScript launcher file.[^1]  |
| [S1182](https://attack.mitre.org/software/S1182) | MagicRAT | MagicRAT stores command and control URLs using base64 encoding in the malware's configuration file.[^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer payloads have included strings encrypted via XOR.[^2]  StrelaStealer JavaScript payloads utilize Base64-encoded payloads that are decoded via [[kb/mitre/attack/software/S0160-certutil\|certutil]] to create a malicious DLL file.[^1] [^3]  |
| [S1186](https://attack.mitre.org/software/S1186) | Line Dancer | Line Dancer shellcode payloads are base64 encoded when transmitted to compromised devices.[^1]  |
| [S1190](https://attack.mitre.org/software/S1190) | Kapeka | Kapeka utilizes obfuscated JSON structures for various data storage and configuration management items.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can decode scripts and strings in loaded modules.[^2] [^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can deobfuscate loaded modules prior to execution.[^2] [^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | The LockBit 3.0 payload is decrypted at runtime.[^3] [^1] [^2]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader uses XOR and RC4 algorithms to decrypt payloads and functions.[^2]  XLoader can be distributed as a self-extracting RAR archive that launches an AutoIT loader.[^1]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex uses a custom decryption routine to unpack itself during installation.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub can use a provided passphrase to decrypt its configuration file.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has used Base64-encoded content during execution, decoded via PowerShell.[^1]  |
| [S1219](https://attack.mitre.org/software/S1219) | REPTILE | The REPTILE launcher component can decrypt kernel module code from a file and load it into memory.[^1]  |
| [S1221](https://attack.mitre.org/software/S1221) | MOPSLED | MOPSLED can decrypt obfuscated configuration files.[^1]  |
| [S1222](https://attack.mitre.org/software/S1222) | RIFLESPINE | RIFLESPINE can deobfuscate encrypted files prior to execution on targeted hosts.[^1]  |
| [S1223](https://attack.mitre.org/software/S1223) | THINCRUST | THINCRUST can deobfuscate RSA encrypted C2 commands received through the DEVICEID cookie.[^1]  |
| [S1224](https://attack.mitre.org/software/S1224) | CASTLETAP | CASTLETAP can filter and deobfuscate an XOR encrypted activation string in the payload of an ICMP echo request.[^1]  |
| [S1226](https://attack.mitre.org/software/S1226) | BOOKWORM | BOOKWORM has decoded its Base64 encoded payload prior to execution.[^2]   BOOKWORM has also encrypted files with RC4 and has decrypted its payload prior to execution.[^1]  |
| [S1227](https://attack.mitre.org/software/S1227) | StarProxy | StarProxy has decrypted network packets using a custom algorithm.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has decoded its payload prior to execution.[^1] [^2] [^3] [^4] [^5]  |
| [S1232](https://attack.mitre.org/software/S1232) | SplatDropper | SplatDropper has decoded XOR encrypted payload.[^1]  |
| [S1235](https://attack.mitre.org/software/S1235) | CorKLOG | CorKLOG has decoded XOR encrypted strings.[^1]  |
| [S1236](https://attack.mitre.org/software/S1236) | CLAIMLOADER | CLAIMLOADER has decoded its payload prior to execution.[^1] [^2]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has decoded its payload prior to execution.[^1] [^2] [^3] [^4] [^5]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has decoded its payload prior to execution.[^1]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has decoded XOR encrypted strings prior to execution in memory.[^1] [^2]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has decoded XOR-encrypted and Base-64-encoded payloads prior to execution.[^1]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has utilized MDeployer to decrypt two payloads that contain MS4Killer toolkit b.cache and the Embargo ransomware executable a.cache with a hardcoded RC4 key `wlQYLoPCil3niI7x8CvR9EtNtL/aeaHrZ23LP3fAsJogVTIzdnZ5Pi09ZVeHFkiB`.[^1]  |
| [S1248](https://attack.mitre.org/software/S1248) | XORIndex Loader | XORIndex Loader can decode its payload prior to execution.[^1]  |
| [S1249](https://attack.mitre.org/software/S1249) | HexEval Loader | HexEval Loader has decoded its payload prior to execution.[^1] [^2] [^3]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has the ability to decrypt RC4 encrypted packets and to decode obfuscated data before C2 communication.[^1]  Additionally, SystemBC has decrypted its config file that was encoded with XOR and a hardcoded 40-byte key.[^2]  |
| [S9007](https://attack.mitre.org/software/S9007) | HTTPTroy | HTTPTroy has decoded strings encoded with Base64 and XOR prior to execution.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has decoded its Base64 instructions.[^2]   GlassWorm has also decrypted its AES protected payloads.[^1] [^2] [^3]  |
| [S9011](https://attack.mitre.org/software/S9011) | BRUSHFIRE | BRUSHFIRE has decrypted XOR strings prior to execution.[^1]  |
| [S9014](https://attack.mitre.org/software/S9014) | PHASEJAM | PHASEJAM has the ability to decode Base64 commands and data.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has decoded its encrypted C2 traffic prior to execution.[^1] [^2] [^3] [^4] [^5]  BRICKSTORM also has the ability to decode its obfuscated payload before execution.[^3]  |
| [S9016](https://attack.mitre.org/software/S9016) | Caminho | Caminho can deobfuscate downloaded files prior to execution.[^1]  |
| [S9018](https://attack.mitre.org/software/S9018) | HeartCrypt | HeartCrypt can decrypt payloads prior to execution.[^2] [^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can decrypt downloaded resources and parse internal files to determine its settings.[^2] [^1]  |
| [S9021](https://attack.mitre.org/software/S9021) | DOWNIISSA | DOWNIISSA can decode strings prior to execution.[^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace has the ability to decrypt its payload prior to execution.[^1] [^2]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has decoded a XOR encoded private key.[^1]  |
| [S9025](https://attack.mitre.org/software/S9025) | NOOPLDR | NOOPLDR can decrypt its payload prior to execution.[^1]  |
| [S9026](https://attack.mitre.org/software/S9026) | ROAMINGHOUSE | ROAMINGHOUSE can decode and drop a malicious ZIP file prior to execution.[^1]  |
| [S9027](https://attack.mitre.org/software/S9027) | ANELLDR | ANELLDR can decrypt encrypted payload data using AES-256-CBC and subsequently execute the payload in memory.[^1] <br> |
| [S9028](https://attack.mitre.org/software/S9028) | PHPsert | PHPsert has the ability to decode and decrypt obfuscated strings prior to execution.[^1]  |
| [S9029](https://attack.mitre.org/software/S9029) | IronWind | IronWind can deobfuscate the next stage payload using Base64 and XOR operations with the key "53".[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | The AshTag stager compoment can decode and decrypt Base64 and XOR-encrypted payloads.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has decrypted the embedded HackBrowserData tool prior to execution.[^1]      |
| [S9033](https://attack.mitre.org/software/S9033) | Fooder | Fooder has decrypted payloads using the WinCrypt API and the AES key.[^1]      |
| [S9034](https://attack.mitre.org/software/S9034) | Tsundere Botnet | Tsundere Botnet’s loader has decrypted obfuscated JavaScript files using the AES-256 CBC algorithm, a build-specific key, and initialization vector.[^2] [^1]     |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can decode and drop a decoy file attached to spearphishing emails.[^1]  |
| [S9036](https://attack.mitre.org/software/S9036) | LP-Notes | LP-Notes has decrypted strings with lengths ranging from 15 to 19 characters using the same decryption key for each string.[^1]  |
| [S9037](https://attack.mitre.org/software/S9037) | RustyWater | RustyWater has used the WriteHexToFile function to transform an embedded hex string to the payload CertificationKit.ini.[^1]     |

 [^1]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
 [^2]: [Sentinel One Tainted Love 2023](https://www.sentinelone.com/labs/operation-tainted-love-chinese-apts-target-telcos-in-new-attacks/)
 [^3]: [Malwarebytes Targeted Attack against Saudi Arabia](https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/)
 [^4]: [Carbon Black Obfuscation Sept 2016](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)
 [^5]: [sentinelone operationDigitalEye Dec 2024](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
 [^6]: [JPCERT SPAWNCHIMERA Ivanti February 2025](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)
 [^7]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
 [^8]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
 [^9]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^10]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^11]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^12]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
 [^13]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^14]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^15]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
 [^16]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^17]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^18]: [FireEye FIN7 Oct 2019](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)
 [^19]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^20]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
 [^21]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
 [^22]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^23]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
 [^24]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^25]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^26]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^27]: [Talos Smoke Loader July 2018](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)
 [^28]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^29]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
 [^30]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
 [^31]: [IBM TA505 April 2020](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)
 [^32]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^33]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^34]: [Medium Babuk February 2021](https://sebdraven.medium.com/babuk-is-distributed-packed-78e2f5dd2e62)
 [^35]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
 [^36]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^37]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
 [^38]: [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)
 [^39]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
 [^40]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
 [^41]: [Palo Alto MidnightEclipse APR 2024](https://unit42.paloaltonetworks.com/cve-2024-3400/)
 [^42]: [Volexity UPSTYLE 2024](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
 [^43]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^44]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
 [^45]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^46]: [CCCS ArcaneDoor 2024](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
 [^47]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^48]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^49]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^50]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^51]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^52]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^53]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^54]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^55]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
 [^56]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^57]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^58]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^59]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)
 [^60]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^61]: [Cybereason Conti Jan 2021](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
 [^62]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^63]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^64]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^65]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
 [^66]: [Microsoft Expand Utility](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/expand)
 [^67]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^68]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^69]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^70]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
 [^71]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
 [^72]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^73]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^74]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
 [^75]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^76]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
 [^77]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)
 [^78]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
 [^79]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^80]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^81]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^82]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
 [^83]: [Netskope LummaStealer 2025](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)
 [^84]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
 [^85]: [Koi Glassworm InvisibleCode October 2025](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
 [^86]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^87]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^88]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
 [^89]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)
 [^90]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^91]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^92]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
 [^93]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
 [^94]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
 [^95]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^96]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^97]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^98]: [AhnLab_SystemBC_Apr2022](https://asec.ahnlab.com/en/33600/)
 [^99]: [Lumen_SystemBC_Sept2025](https://blog.lumen.com/systembc-bringing-the-noise/)
 [^100]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
 [^101]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
 [^102]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^103]: [ESET Ebury Oct 2017](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
 [^104]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^105]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
 [^106]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^107]: [Unit42 OceanLotus 2017](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)
 [^108]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^109]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
 [^110]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^111]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^112]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^113]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^114]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^115]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^116]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^117]: [Volexity Ivanti Zero-Day Exploitation January 2024](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
 [^118]: [OilRig New Delivery Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-oilrig-group-steps-attacks-new-delivery-documents-new-injector-trojan/)
 [^119]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
 [^120]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
 [^121]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^122]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
 [^123]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^124]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^125]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
 [^126]: [Lab52 MUSTANG PANDA PUBLOAD MAY 2023](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)
 [^127]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^128]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^129]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)
 [^130]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^131]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^132]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^133]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
 [^134]: [Palo Alto HeartCrypt DEC 2024](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)
 [^135]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
 [^136]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
 [^137]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^138]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
 [^139]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
 [^140]: [Cybereason Egregor Nov 2020](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)
 [^141]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
 [^142]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^143]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^144]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^145]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^146]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^147]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^148]: [Symantec Dyre June 2015](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/dyre-emerging-threat.pdf)
 [^149]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^150]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^151]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
 [^152]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
 [^153]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
 [^154]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
 [^155]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
 [^156]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^157]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
 [^158]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
 [^159]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^160]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^161]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^162]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^163]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
 [^164]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)
 [^165]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^166]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
 [^167]: [Resecurity UNC5221 BRICKSTORM F5 Big-IP October 2025](https://www.resecurity.com/blog/article/f5-big-ip-source-code-leak-tied-to-state-linked-campaigns-using-brickstorm-backdoor)
 [^168]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^169]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^170]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
 [^171]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^172]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^173]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
 [^174]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
 [^175]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^176]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^177]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^178]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)
 [^179]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
 [^180]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^181]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
 [^182]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
 [^183]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^184]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^185]: [CISA AA20-301A Kimsuky](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)
 [^186]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
 [^187]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
 [^188]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^189]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^190]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^191]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^192]: [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)
 [^193]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
 [^194]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^195]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
 [^196]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^197]: [Unit42 Chinese VSCode 06 September 2024](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)
 [^198]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
 [^199]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
 [^200]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
 [^201]: [SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)
 [^202]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
 [^203]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
 [^204]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^205]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^206]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
 [^207]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^208]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
 [^209]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^210]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
 [^211]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^212]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^213]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^214]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^215]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^216]: [G Data Sodinokibi June 2019](https://www.gdatasoftware.com/blog/2019/06/31724-strange-bits-sodinokibi-spam-cinarat-and-fake-g-data)
 [^217]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)
 [^218]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^219]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
 [^220]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^221]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
 [^222]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^223]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
 [^224]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^225]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^226]: [CoinTicker 2019](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)
 [^227]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^228]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^229]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^230]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^231]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)
 [^232]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^233]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^234]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
 [^235]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^236]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
 [^237]: [CISA ComRAT Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
 [^238]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^239]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^240]: [Fidelis TrickBot Oct 2016](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
 [^241]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^242]: [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)
 [^243]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^244]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
 [^245]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
 [^246]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^247]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^248]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^249]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^250]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^251]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)
 [^252]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
 [^253]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^254]: [objective-see windtail1 dec 2018](https://objective-see.com/blog/blog_0x3B.html)
 [^255]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^256]: [Zscaler XLoader 2025](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)
 [^257]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^258]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^259]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
 [^260]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)
 [^261]: [Flashpoint FIN 7 March 2019](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)
 [^262]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
 [^263]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^264]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^265]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^266]: [Check Point Sunburst Teardrop December 2020](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)
 [^267]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
 [^268]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)
 [^269]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
 [^270]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
 [^271]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^272]: [Logpoint Pikabot 2024](https://www.logpoint.com/wp-content/uploads/2024/02/logpoint-etpr-pikabot.pdf)
 [^273]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)
 [^274]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^275]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
 [^276]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^277]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
 [^278]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)
 [^279]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^280]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
 [^281]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^282]: [CYBERCOM Iranian Intel Cyber January 2022](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)
 [^283]: [PaloAlto StrelaStealer 2024](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
 [^284]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
 [^285]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
 [^286]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
 [^287]: [PWC WellMess C2 August 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/wellmess-analysis-command-control.html)
 [^288]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
 [^289]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^290]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^291]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
 [^292]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^293]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^294]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)
 [^295]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
 [^296]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
 [^297]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^298]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)
 [^299]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
 [^300]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^301]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
 [^302]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^303]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^304]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^305]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)
 [^306]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
 [^307]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
 [^308]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^309]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
 [^310]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
 [^311]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^312]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^313]: [CAL_MuddyWater_Mar2026](https://ctrlaltintel.com/research/MuddyWater/)
 [^314]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
 [^315]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
 [^316]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^317]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)
 [^318]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
 [^319]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^320]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^321]: [Talos Zeus Panda Nov 2017](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)
 [^322]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
 [^323]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^324]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
 [^325]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^326]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
 [^327]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
 [^328]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
 [^329]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
 [^330]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^331]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^332]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
 [^333]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^334]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)
 [^335]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^336]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^337]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^338]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^339]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
 [^340]: [Unit42 DarkHydrus Jan 2019](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)
 [^341]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^342]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^343]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
 [^344]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
 [^345]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
 [^346]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^347]: [Symantec RAINDROP January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)
 [^348]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^349]: [Threatpost Hancitor](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)
 [^350]: [FireEye Hancitor](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html)
