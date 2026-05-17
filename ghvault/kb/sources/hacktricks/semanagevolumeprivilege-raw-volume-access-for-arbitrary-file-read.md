---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# SeManageVolumePrivilege: Raw volume access for arbitrary file read

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-windows-local-privilege-escalation-semanagevolume-perform-volume-maintenance-tasks` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/windows-local-privilege-escalation/semanagevolume-perform-volume-maintenance-tasks.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SeManageVolumePrivilege: Raw volume access for arbitrary file read](../../topics/windows-hardening/semanagevolumeprivilege-raw-volume-access-for-arbitrary-file-read.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-windows-hardening-windows-local-privilege-escalation-semanagevolume-perform-volume-maintenance-tasks |
| name | SeManageVolumePrivilege: Raw volume access for arbitrary file read |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/windows-hardening/windows-local-privilege-escalation/semanagevolume-perform-volume-maintenance-tasks.md |

## Preserved Source Material

````yaml
_body: "# SeManageVolumePrivilege: Raw volume access for arbitrary file read\n\n{{#include ../../banners/hacktricks-training.md}}\n\
  \n## Overview\n\nWindows user right: Perform volume maintenance tasks (constant: SeManageVolumePrivilege).\n\nHolders can\
  \ perform low-level volume operations such as defragmentation, creating/removing volumes, and maintenance IO. Critically\
  \ for attackers, this right allows opening raw volume device handles (e.g., \\\\.\\C:) and issuing direct disk I/O that\
  \ bypasses NTFS file ACLs. With raw access you can copy bytes of any file on the volume even if denied by DACL, by parsing\
  \ the filesystem structures offline or leveraging tools that read at the block/cluster level.\n\nDefault: Administrators\
  \ on servers and domain controllers.\n\n## Abuse scenarios\n\n- Arbitrary file read bypassing ACLs by reading the disk device\
  \ (e.g., exfiltrate sensitive system-protected material such as machine private keys under %ProgramData%\\Microsoft\\Crypto\\\
  RSA\\MachineKeys and %ProgramData%\\Microsoft\\Crypto\\Keys, registry hives, DPAPI masterkeys, SAM, ntds.dit via VSS, etc.).\n\
  - Bypass locked/privileged paths (C:\\Windows\\System32\\…) by copying bytes directly from the raw device.\n- In AD CS environments,\
  \ exfiltrate the CA’s key material (machine key store) to mint “Golden Certificates” and impersonate any domain principal\
  \ via PKINIT. See link below.\n\nNote: You still need a parser for NTFS structures unless you rely on helper tools. Many\
  \ off-the-shelf tools abstract the raw access.\n\n## Practical techniques\n\n- Open a raw volume handle and read clusters:\n\
  \n<details>\n<summary>Click to expand</summary>\n\n```powershell\n# PowerShell – read first MB from C: raw device (requires\
  \ SeManageVolumePrivilege)\n$fs = [System.IO.File]::Open(\"\\\\.\\\\C:\",[System.IO.FileMode]::Open,[System.IO.FileAccess]::Read,[System.IO.FileShare]::ReadWrite)\n\
  $buf = New-Object byte[] (1MB)\n$null = $fs.Read($buf,0,$buf.Length)\n$fs.Close()\n[IO.File]::WriteAllBytes(\"C:\\\\temp\\\
  \\c_first_mb.bin\", $buf)\n```\n\n```csharp\n// C# (compile with Add-Type) – read an arbitrary offset of \\\\.\\nusing System;\n\
  using System.IO;\nclass R {\n  static void Main(string[] a){\n    using(var fs = new FileStream(\"\\\\\\\\.\\\\C:\", FileMode.Open,\
  \ FileAccess.Read, FileShare.ReadWrite)){\n      fs.Position = 0x100000; // seek\n      var buf = new byte[4096];\n    \
  \  fs.Read(buf,0,buf.Length);\n      File.WriteAllBytes(\"C:\\\\temp\\\\blk.bin\", buf);\n    }\n  }\n}\n```\n\n</details>\n\
  \n- Use an NTFS-aware tool to recover specific files from raw volume:\n  - RawCopy/RawCopy64 (sector-level copy of in-use\
  \ files)\n  - FTK Imager or The Sleuth Kit (read-only imaging, then carve files)\n  - vssadmin/diskshadow + shadow copy,\
  \ then copy target file from the snapshot (if you can create VSS; often requires admin but commonly available to the same\
  \ operators that hold SeManageVolumePrivilege)\n\nTypical sensitive paths to target:\n- %ProgramData%\\Microsoft\\Crypto\\\
  RSA\\MachineKeys\\\n- %ProgramData%\\Microsoft\\Crypto\\Keys\\\n- C:\\Windows\\System32\\config\\SAM, SYSTEM, SECURITY (local\
  \ secrets)\n- C:\\Windows\\NTDS\\ntds.dit (domain controllers – via shadow copy)\n- C:\\Windows\\System32\\CertSrv\\CertEnroll\\\
  \ (CA certs/CRLs; private keys live in the machine key store above)\n\n## AD CS tie‑in: Forging a Golden Certificate\n\n\
  If you can read the Enterprise CA’s private key from the machine key store, you can forge client‑auth certificates for arbitrary\
  \ principals and authenticate via PKINIT/Schannel. This is often referred to as a Golden Certificate. See:\n\n{{#ref}}\n\
  ../active-directory-methodology/ad-certificates/domain-persistence.md\n{{#endref}}\n\n(Section: “Forging Certificates with\
  \ Stolen CA Certificates (Golden Certificate) – DPERSIST1”).\n\n## Detection and hardening\n\n- Strongly limit assignment\
  \ of SeManageVolumePrivilege (Perform volume maintenance tasks) to only trusted admins.\n- Monitor Sensitive Privilege Use\
  \ and process handle opens to device objects like \\\\.\\C:, \\\\.\\PhysicalDrive0.\n- Prefer HSM/TPM-backed CA keys or\
  \ DPAPI-NG so that raw file reads cannot recover key material in usable form.\n- Keep uploads, temp, and extraction paths\
  \ non-executable and separated (web context defense that often pairs with this chain post‑exploitation).\n\n## References\n\
  \n- Microsoft – Perform volume maintenance tasks (SeManageVolumePrivilege): https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/perform-volume-maintenance-tasks\n\
  - 0xdf – HTB: Certificate (SeManageVolumePrivilege used to read CA key → Golden Certificate): https://0xdf.gitlab.io/2025/10/04/htb-certificate.html\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: windows-hardening/windows-local-privilege-escalation/semanagevolume-perform-volume-maintenance-tasks.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/windows-local-privilege-escalation/semanagevolume-perform-volume-maintenance-tasks.md
````
