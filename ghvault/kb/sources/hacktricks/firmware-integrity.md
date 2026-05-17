---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Firmware Integrity

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-hardware-physical-access-firmware-analysis-firmware-integrity` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/hardware-physical-access/firmware-analysis/firmware-integrity.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Firmware Integrity](../../topics/hardware-physical-access/firmware-integrity.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-hardware-physical-access-firmware-analysis-firmware-integrity |
| name | Firmware Integrity |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/hardware-physical-access/firmware-analysis/firmware-integrity.md |

## Preserved Source Material

```yaml
_body: '# Firmware Integrity


  {{#include ../../banners/hacktricks-training.md}}


  The **custom firmware and/or compiled binaries can be uploaded to exploit integrity or signature verification flaws**. The
  following steps can be followed for backdoor bind shell compilation:


  1. The firmware can be extracted using firmware-mod-kit (FMK).

  2. The target firmware architecture and endianness should be identified.

  3. A cross compiler can be built using Buildroot or other suitable methods for the environment.

  4. The backdoor can be built using the cross compiler.

  5. The backdoor can be copied to the extracted firmware /usr/bin directory.

  6. The appropriate QEMU binary can be copied to the extracted firmware rootfs.

  7. The backdoor can be emulated using chroot and QEMU.

  8. The backdoor can be accessed via netcat.

  9. The QEMU binary should be removed from the extracted firmware rootfs.

  10. The modified firmware can be repackaged using FMK.

  11. The backdoored firmware can be tested by emulating it with firmware analysis toolkit (FAT) and connecting to the target
  backdoor IP and port using netcat.


  If a root shell has already been obtained through dynamic analysis, bootloader manipulation, or hardware security testing,
  precompiled malicious binaries such as implants or reverse shells can be executed. Automated payload/implant tools like
  the Metasploit framework and ''msfvenom'' can be leveraged using the following steps:


  1. The target firmware architecture and endianness should be identified.

  2. Msfvenom can be used to specify the target payload, attacker host IP, listening port number, filetype, architecture,
  platform, and the output file.

  3. The payload can be transferred to the compromised device and ensured that it has execution permissions.

  4. Metasploit can be prepared to handle incoming requests by starting msfconsole and configuring the settings according
  to the payload.

  5. The meterpreter reverse shell can be executed on the compromised device.


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: hardware-physical-access/firmware-analysis/firmware-integrity.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/hardware-physical-access/firmware-analysis/firmware-integrity.md
```
