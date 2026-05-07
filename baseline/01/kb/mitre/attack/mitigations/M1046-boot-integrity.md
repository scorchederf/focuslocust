---
parsed_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1046
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1046-boot-integrity
---

## Description

Boot Integrity ensures that a system starts securely by verifying the integrity of its boot process, operating system, and associated components. This mitigation focuses on leveraging secure boot mechanisms, hardware-rooted trust, and runtime integrity checks to prevent tampering during the boot sequence. It is designed to thwart adversaries attempting to modify system firmware, bootloaders, or critical OS components. This mitigation can be implemented through the following measures:<br><br>Implementation of Secure Boot:<br><br>- Implementation: Enable UEFI Secure Boot on all systems and configure it to allow only signed bootloaders and operating systems.<br>- Use Case: An adversary attempts to replace the system’s bootloader with a malicious version to gain persistence. Secure Boot prevents the untrusted bootloader from executing, halting the attack.<br><br>Utilization of TPMs:<br><br>- Implementation: Configure systems to use TPM-based attestation for boot integrity, ensuring that any modification to the firmware, bootloader, or OS is detected.<br>- Use Case: A compromised firmware component alters the boot sequence. The TPM detects the change and triggers an alert, allowing the organization to respond before further damage.<br><br>Enable Bootloader Passwords:<br><br>- Implementation: Protect BIOS/UEFI settings with a strong password and limit physical access to devices.<br>- Use Case: An attacker with physical access attempts to disable Secure Boot or modify the boot sequence. The password prevents unauthorized changes.<br><br>Runtime Integrity Monitoring:<br><br>- Implementation: Deploy solutions to verify the integrity of critical files and processes after boot.<br>- Use Case: A malware infection modifies kernel modules post-boot. Runtime integrity monitoring detects the modification and prevents the malicious module from loading.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1195-supply-chain-compromise\|T1195]] | Supply Chain Compromise | Use secure methods to boot a system and verify the integrity of the operating system and loading mechanisms. |
| [[kb/mitre/attack/techniques/T1195.003-compromise-hardware-supply-chain\|T1195.003]] | Compromise Hardware Supply Chain | Use Trusted Platform Module technology and a secure or trusted boot process to prevent system integrity from being compromised. Check the integrity of the existing BIOS or EFI to determine if it is vulnerable to modification. [^1]  [^2]  |
| [[kb/mitre/attack/techniques/T1495-firmware-corruption\|T1495]] | Firmware Corruption | Check the integrity of the existing BIOS and device firmware to determine if it is vulnerable to modification. |
| [[kb/mitre/attack/techniques/T1505-server-software-component\|T1505]] | Server Software Component | Enabling secure boot allows validation of software and drivers during initial system boot. |
| [[kb/mitre/attack/techniques/T1505.006-vsphere-installation-bundles\|T1505.006]] | vSphere Installation Bundles | Enabling secure boot allows ESXi to validate software and drivers during initial system boot.[^1]  |
| [[kb/mitre/attack/techniques/T1542-pre-os-boot\|T1542]] | Pre-OS Boot | Use Trusted Platform Module technology and a secure or trusted boot process to prevent system integrity from being compromised. Check the integrity of the existing BIOS or EFI to determine if it is vulnerable to modification. [^1]  [^2]  |
| [[kb/mitre/attack/techniques/T1542.001-system-firmware\|T1542.001]] | System Firmware | Check the integrity of the existing BIOS or EFI to determine if it is vulnerable to modification. Use Trusted Platform Module technology. [^1]  Move system's root of trust to hardware to prevent tampering with the SPI flash memory.[^2]  Technologies such as Intel Boot Guard can assist with this. [^3]  |
| [[kb/mitre/attack/techniques/T1542.003-bootkit\|T1542.003]] | Bootkit | Use Trusted Platform Module technology and a secure or trusted boot process to prevent system integrity from being compromised.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1542.004-rommonkit\|T1542.004]] | ROMMONkit | Enable secure boot features to validate the digital signature of the boot environment and system image using a special purpose hardware device. If the validation check fails, the device will fail to boot preventing loading of unauthorized software. [^1]   |
| [[kb/mitre/attack/techniques/T1542.005-tftp-boot\|T1542.005]] | TFTP Boot | Enable secure boot features to validate the digital signature of the boot environment and system image using a special purpose hardware device. If the validation check fails, the device will fail to boot preventing loading of unauthorized software. [^1]   |
| [[kb/mitre/attack/techniques/T1553.006-code-signing-policy-modification\|T1553.006]] | Code Signing Policy Modification | Use of Secure Boot may prevent some implementations of modification to code signing policies.[^1]  |
| [[kb/mitre/attack/techniques/T1601-modify-system-image\|T1601]] | Modify System Image | Some vendors of embedded network devices provide cryptographic signing to ensure the integrity of operating system images at boot time.  Implement where available, following vendor guidelines. [^1]  |
| [[kb/mitre/attack/techniques/T1601.001-patch-system-image\|T1601.001]] | Patch System Image | Some vendors of embedded network devices provide cryptographic signing to ensure the integrity of operating system images at boot time.  Implement where available, following vendor guidelines. [^1]  |
| [[kb/mitre/attack/techniques/T1601.002-downgrade-system-image\|T1601.002]] | Downgrade System Image | Some vendors of embedded network devices provide cryptographic signing to ensure the integrity of operating system images at boot time.  Implement where available, following vendor guidelines. [^1]  |

 [^1]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)
 [^2]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)
 [^3]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)
 [^4]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)
 [^5]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)
 [^6]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)
 [^7]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)
