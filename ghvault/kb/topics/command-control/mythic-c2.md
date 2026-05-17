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

## Summary

Installation

## Preserved Body

````markdown
## Installation

```ps1
sudo apt-get install build-essential
git clone https://github.com/its-a-feature/Mythic --depth 1
./install_docker_ubuntu.sh
./install_docker_debian.sh
cd Mythic
sudo make
sudo ./mythic-cli start
```

## Agents

* [Mythic Community Agent Feature Matrix](https://mythicmeta.github.io/overview/agent_matrix.html)

Agents can be found at: [https://github.com/MythicAgents](https://github.com/MythicAgents)

```ps1
./mythic-cli install github https://github.com/MythicAgents/Medusa # A Mythic Agent compatible Python 2.7 and 3.8
./mythic-cli install github https://github.com/MythicAgents/Hannibal # A Mythic Agent written in PIC C
./mythic-cli install github https://github.com/MythicAgents/thanatos # A Mythic C2 agent targeting Linux and Windows hosts written in Rust
./mythic-cli install github https://github.com/MythicAgents/poseidon # A Mythic Agent written in Golang for Linux/MacOS
./mythic-cli install github https://github.com/MythicAgents/Apollo # # A Mythic Agent written in C# using the 4.0 .NET Framework 
./mythic-cli install github https://github.com/MythicAgents/Athena # A Mythic Agent written in .NET
./mythic-cli install github https://github.com/MythicAgents/Xenon # A Mythic Agent written in C, compatible with httpx profiles
```

## Profiles

C2 Profiles can be found at: [https://github.com/MythicC2Profiles](https://github.com/MythicC2Profiles)

```ps1
./mythic-cli install github https://github.com/MythicC2Profiles/httpx
./mythic-cli install github https://github.com/MythicC2Profiles/http
./mythic-cli install github https://github.com/MythicC2Profiles/websocket
./mythic-cli install github https://github.com/MythicC2Profiles/dns
./mythic-cli install github https://github.com/MythicC2Profiles/dynamichttp
./mythic-cli install github https://github.com/MythicC2Profiles/smb
./mythic-cli install github https://github.com/MythicC2Profiles/tcp
```

## SSL

If you want to use SSL, put your key and cert in the `C2_Profiles/HTTP/c2_code` folder and update the `key_path` and `cert_path` variables to have the `names` of those files.

Use Let's Encrypt certbot to get both the key and certificate for your domain:

```ps1
sudo apt install certbot
certbot certonly --standalone -d "example.com" --register-unsafely-without-email --non-interactive --agree-tos
```

Add the file in the Agent container:

```ps1
docker cp /etc/letsencrypt/archive/example.com/fullchain1.pem http:/Mythic/http/c2_code/fullchain.pem
docker cp /etc/letsencrypt/archive/example.com/privkey1.pem http:/Mythic/http/c2_code/privkey.pem
```

Alternatively, if you specify `use_ssl` as true and you don't have any certs already placed on disk, then the profile will automatically generate some self-signed certs for you to use.

## References

* [Mythic Documentation](https://docs.mythic-c2.net)
````

## Source Verification

[source record](../../sources/internalallthethings/mythic-c2.md)

## Evidence Excerpt

````text
_body: "# Mythic C2\n\n## Summary\n\n* [Installation](#installation)\n* [Agents](#agents)\n* [Profiles](#profiles)\n* [References](#references)\n\
\n## Installation\n\n```ps1\nsudo apt-get install build-essential\ngit clone https://github.com/its-a-feature/Mythic --depth\
\ 1\n./install_docker_ubuntu.sh\n./install_docker_debian.sh\ncd Mythic\nsudo make\nsudo ./mythic-cli start\n```\n\n## Agents\n\
\n* [Mythic Community Agent Feature Matrix](https://mythicmeta.github.io/overview/agent_matrix.html)\n\nAgents can be found\
\ at: [https://github.com/MythicAgents](https://github.com/MythicAgents)\n\n```ps1\n./mythic-cli install github https://github.com/MythicAgents/Medusa\
\ # A Mythic Agent compatible Python 2.7 and 3.8\n./mythic-cli install github https://github.com/MythicAgents/Hannibal #\
\ A Mythic Agent written in PIC C\n./mythic-cli install github https://github.com/MythicAgents/thanatos # A Mythic C2 agent\
\ targeting Linux and Windows hosts written in Rust\n./mythic-cli install github https://github.com/MythicAgents/poseidon\
````
