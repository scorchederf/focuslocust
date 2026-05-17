---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Hash Cracking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-hash-cracking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/hash-cracking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hash Cracking](../../topics/cheatsheets/hash-cracking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-hash-cracking |
| name | Hash Cracking |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/hash-cracking.md |

## Preserved Source Material

````yaml
_body: "# Hash Cracking\n\n## Summary\n\n* [Hashcat](https://hashcat.net/hashcat/)\n    * [Hashcat Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)\n\
  \    * [Hashcat Install](#hashcat-install)\n    * [Mask attack](#mask-attack)\n    * [Dictionary](#dictionary)\n* [John](https://github.com/openwall/john)\n\
  \    * [Usage](#john-usage)\n* [Rainbow tables](#rainbow-tables)\n* [Tips and Tricks](#tips-and-tricks)\n* [Online Cracking\
  \ Resources](#online-cracking-resources)\n* [References](#references)\n\n## Hashcat\n\n### Hashcat Install\n\n```powershell\n\
  apt install cmake build-essential -y\napt install checkinstall git -y\ngit clone https://github.com/hashcat/hashcat.git\
  \ && cd hashcat && make -j 8 && make install\n```\n\n1. Extract the hash\n2. Get the hash format: [hashcat.net/example_hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)\n\
  3. Establish a cracking stratgy based on hash format (ex: wordlist -> wordlist + rules -> mask -> combinator mode -> prince\
  \ attack -> ...)\n4. Enjoy plains\n5. Review strategy\n6. Start over\n\n### Dictionary\n\n> Every word of a given list (a.k.a.\
  \ dictionary) is hashed and compared against the target hash.\n\n```powershell\nhashcat --attack-mode 0 --hash-type $number\
  \ $hashes_file $wordlist_file -r $my_rules\n```\n\n* Wordlists\n    * [packetstorm](https://packetstormsecurity.com/Crackers/wordlists/)\n\
  \    * [weakpass_3a](https://download.weakpass.com/wordlists/1948/weakpass_3a.7z)\n    * [weakpass_3](https://download.weakpass.com/wordlists/1947/weakpass_3.7z)\n\
  \    * [Hashes.org](https://download.weakpass.com/wordlists/1931/Hashes.org.7z)\n    * [kerberoast_pws](https://gist.github.com/edermi/f8b143b11dc020b854178d3809cf91b5/raw/b7d83af6a8bbb43013e04f78328687d19d0cf9a7/kerberoast_pws.xz)\n\
  \    * [hashmob.net](https://hashmob.net/research/wordlists)\n    * [clem9669/wordlists](https://github.com/clem9669/wordlists)\n\
  \n* Rules\n    * [One Rule to Rule Them All](https://notsosecure.com/one-rule-to-rule-them-all/)\n    * [nsa-rules](https://github.com/NSAKEY/nsa-rules)\n\
  \    * [hob064](https://raw.githubusercontent.com/praetorian-inc/Hob0Rules/master/hob064.rule)\n    * [d3adhob0](https://raw.githubusercontent.com/praetorian-inc/Hob0Rules/master/d3adhob0.rule)\n\
  \    * [clem9669/hashcat-rule](https://github.com/clem9669/hashcat-rule)\n\n### Mask attack\n\nMask attack is an attack\
  \ mode which optimize brute-force.\n\n> Every possibility for a given character set and a given length (i.e. aaa, aab, aac,\
  \ ...) is hashed and compared against the target hash.\n\n```powershell\n# Mask: upper*1+lower*5+digit*2 and upper*1+lower*6+digit*2\
  \ \nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?l?d?d\nhashcat -m 1000 --status\
  \ --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?l?l?d?d \nhashcat -m 1000 --status --status-timer 300 -w 4\
  \ -O /content/*.ntds -a 3 -1 \"*+!??\" ?u?l?l?l?l?l?d?d?1\nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds\
  \ -a 3 -1 \"*+!??\" ?u?l?l?l?l?l?l?d?d?1 \n\n# Mask: upper*1+lower*3+digit*4 and upper*1+lower*3+digit*4\nhashcat -m 1000\
  \ --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?d?d?d?d\nhashcat -m 1000 --status --status-timer 300\
  \ -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?d?d?d?d\nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a\
  \ 3 ?u?l?l?l?l?l?d?d?d?d\nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 \"*+!??\" ?u?l?l?l?d?d?d?d?1\n\
  hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 \"*+!??\" ?u?l?l?l?l?d?d?d?d?1\n\n# Mask: lower*6\
  \ + digit*2 + special digit(+!?*)\nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 \"*+!??\"\
  \ ?l?l?l?l?l?l?d?d?1\nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 \"*+!??\" ?l?l?l?l?l?l?d?d?1?1\n\
  \n# Mask: lower*6 + digit*2\nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 /content/hashcat/masks/8char-1l-1u-1d-1s-compliant.hcmask\n\
  hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 ?l?d?u ?1?1?1?1?1?1?1?1\n\n# Other examples\n\
  hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?a?a?a?a?a?a?a?a?a\nhashcat -m 1000 --status --status-timer\
  \ 300 -w 4 -O /content/*.ntds -a 3 ?a?a?a?a?a?a?a?a \nhashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds\
  \ -a 3 ?u?l?l?l?l?l?l?d?d?d?d\nhashcat --attack-mode 3 --increment --increment-min 4 --increment-max 8 --hash-type $number\
  \ $hashes_file \"?a?a?a?a?a?a?a?a?a?a?a?a\"\nhashcat --attack-mode 3 --hash-type $number $hashes_file \"?u?l?l?l?d?d?d?d?s\"\
  \nhashcat --attack-mode 3 --hash-type $number $hashes_file \"?a?a?a?a?a?a?a?a\"\nhashcat --attack-mode 3 --custom-charset1\
  \ \"?u\" --custom-charset2 \"?l?u?d\" --custom-charset3 \"?d\" --hash-type $number $hashes_file \"?1?2?2?2?3\"\n```\n\n\
  | Shortcut  | Characters  |\n|----|----------------------------|\n| ?l | abcdefghijklmnopqrstuvwxyz |\n| ?u | ABCDEFGHIJKLMNOPQRSTUVWXYZ\
  \ |\n| ?d | 0123456789 |\n| ?s | !\"#$%&'()*+,-./:;<=>?@[\\]^_`{}~ |\n| ?a | ?l?u?d?s |\n| ?b | 0x00 - 0xff |\n\n## John\n\
  \n### John Usage\n\n```bash\n# Run on password file containing hashes to be cracked\njohn passwd\n\n# Use a specific wordlist\n\
  john --wordlist=<wordlist> passwd\n\n# Use a specific wordlist with rules\njohn --wordlist=<wordlist> passwd --rules=Jumbo\n\
  \n# Show cracked passwords\njohn --show passwd\n\n# Restore interrupted sessions\njohn --restore\n```\n\n## Rainbow tables\n\
  \n> The hash is looked for in a pre-computed table. It is a time-memory trade-off that allows cracking hashes faster, but\
  \ costing a greater amount of memory than traditional brute-force of dictionary attacks. This attack cannot work if the\
  \ hashed value is salted (i.e. hashed with an additional random value as prefix/suffix, making the pre-computed table irrelevant)\n\
  \n## Tips and Tricks\n\n* Cloud GPU\n    * [penglab - Abuse of Google Colab for cracking hashes. \U0001F427](https://github.com/mxrch/penglab)\n\
  \    * [google-colab-hashcat - Google colab hash cracking](https://github.com/ShutdownRepo/google-colab-hashcat)\n    *\
  \ [Cloudtopolis - Zero Infrastructure Password Cracking](https://github.com/JoelGMSec/Cloudtopolis)\n    * [Nephelees -\
  \ also a NTDS cracking tool abusing Google Colab](https://github.com/swisskyrepo/Nephelees)\n* Build a rig on premise\n\
  \    * [Pentester's Portable Cracking Rig - $1000](https://www.netmux.com/blog/portable-cracking-rig)\n    * [How To Build\
  \ A Password Cracking Rig - 5000$](https://www.netmux.com/blog/how-to-build-a-password-cracking-rig)\n* Online cracking\n\
  \    * [Hashes.com](https://hashes.com/en/decrypt/hash)\n    * [hashmob.net](https://hashmob.net/): great community with\
  \ Discord\n* Use the `loopback` in combination with rules and dictionary to keep cracking until you don't find new passsword:\
  \ `hashcat --loopback --attack-mode 0 --rules-file $rules_file --hash-type $number $hashes_file $wordlist_file`\n* PACK\
  \ (Password Analysis and Cracking Kit)\n    * [iphelix/pack](https://github.com/iphelix/pack/blob/master/README)\n    *\
  \ Can produce custom hcmask files to use with hashcat, based on statistics and rules applied on an input dataset\n* Use\
  \ Deep Learning\n    * [brannondorsey/PassGAN](https://github.com/brannondorsey/PassGAN)\n\n## Online Cracking Resources\n\
  \n* [hashes.com](https://hashes.com)\n* [crackstation.net](https://crackstation.net)\n* [hashmob.net](https://hashmob.net/)\n\
  \n## References\n\n* [Cracking - The Hacker Recipes](https://www.thehacker.recipes/ad-ds/movement/credentials/cracking)\n\
  * [Using Hashcat to Crack Hashes on Azure](https://durdle.com/2017/04/23/using-hashcat-to-crack-hashes-on-azure/)\n* [miloserdov.org\
  \ hashcat](https://miloserdov.org/?p=5426&PageSpeed=noscript)\n* [miloserdov.org john](https://miloserdov.org/?p=4961&PageSpeed=noscript)\n\
  * [DeepPass — Finding Passwords With Deep Learning - Will Schroeder - Jun 1](https://posts.specterops.io/deeppass-finding-passwords-with-deep-learning-4d31c534cd00)"
_relative_path: cheatsheets/hash-cracking.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/hash-cracking.md
````
