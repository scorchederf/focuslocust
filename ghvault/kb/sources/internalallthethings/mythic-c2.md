---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Mythic C2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-command-control-mythic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/mythic.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mythic C2](../../topics/command-control/mythic-c2.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-command-control-mythic |
| name | Mythic C2 |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/command-control/mythic.md |

## Preserved Source Material

````yaml
_body: "# Mythic C2\n\n## Summary\n\n* [Installation](#installation)\n* [Agents](#agents)\n* [Profiles](#profiles)\n* [References](#references)\n\
  \n## Installation\n\n```ps1\nsudo apt-get install build-essential\ngit clone https://github.com/its-a-feature/Mythic --depth\
  \ 1\n./install_docker_ubuntu.sh\n./install_docker_debian.sh\ncd Mythic\nsudo make\nsudo ./mythic-cli start\n```\n\n## Agents\n\
  \n* [Mythic Community Agent Feature Matrix](https://mythicmeta.github.io/overview/agent_matrix.html)\n\nAgents can be found\
  \ at: [https://github.com/MythicAgents](https://github.com/MythicAgents)\n\n```ps1\n./mythic-cli install github https://github.com/MythicAgents/Medusa\
  \ # A Mythic Agent compatible Python 2.7 and 3.8\n./mythic-cli install github https://github.com/MythicAgents/Hannibal #\
  \ A Mythic Agent written in PIC C\n./mythic-cli install github https://github.com/MythicAgents/thanatos # A Mythic C2 agent\
  \ targeting Linux and Windows hosts written in Rust\n./mythic-cli install github https://github.com/MythicAgents/poseidon\
  \ # A Mythic Agent written in Golang for Linux/MacOS\n./mythic-cli install github https://github.com/MythicAgents/Apollo\
  \ # # A Mythic Agent written in C# using the 4.0 .NET Framework \n./mythic-cli install github https://github.com/MythicAgents/Athena\
  \ # A Mythic Agent written in .NET\n./mythic-cli install github https://github.com/MythicAgents/Xenon # A Mythic Agent written\
  \ in C, compatible with httpx profiles\n```\n\n## Profiles\n\nC2 Profiles can be found at: [https://github.com/MythicC2Profiles](https://github.com/MythicC2Profiles)\n\
  \n```ps1\n./mythic-cli install github https://github.com/MythicC2Profiles/httpx\n./mythic-cli install github https://github.com/MythicC2Profiles/http\n\
  ./mythic-cli install github https://github.com/MythicC2Profiles/websocket\n./mythic-cli install github https://github.com/MythicC2Profiles/dns\n\
  ./mythic-cli install github https://github.com/MythicC2Profiles/dynamichttp\n./mythic-cli install github https://github.com/MythicC2Profiles/smb\n\
  ./mythic-cli install github https://github.com/MythicC2Profiles/tcp\n```\n\n## SSL\n\nIf you want to use SSL, put your key\
  \ and cert in the `C2_Profiles/HTTP/c2_code` folder and update the `key_path` and `cert_path` variables to have the `names`\
  \ of those files.\n\nUse Let's Encrypt certbot to get both the key and certificate for your domain:\n\n```ps1\nsudo apt\
  \ install certbot\ncertbot certonly --standalone -d \"example.com\" --register-unsafely-without-email --non-interactive\
  \ --agree-tos\n```\n\nAdd the file in the Agent container:\n\n```ps1\ndocker cp /etc/letsencrypt/archive/example.com/fullchain1.pem\
  \ http:/Mythic/http/c2_code/fullchain.pem\ndocker cp /etc/letsencrypt/archive/example.com/privkey1.pem http:/Mythic/http/c2_code/privkey.pem\n\
  ```\n\nAlternatively, if you specify `use_ssl` as true and you don't have any certs already placed on disk, then the profile\
  \ will automatically generate some self-signed certs for you to use.\n\n## References\n\n* [Mythic Documentation](https://docs.mythic-c2.net)"
_relative_path: command-control/mythic.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/command-control/mythic.md
````
