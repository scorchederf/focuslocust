---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Machine Account Quota

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-machineaccountquota` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-machineaccountquota.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Machine Account Quota](../../topics/active-directory/active-directory-machine-account-quota.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-machineaccountquota |
| name | Active Directory - Machine Account Quota |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-machineaccountquota.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Machine Account Quota\n\nIn Active Directory (AD), the `MachineAccountQuota` is a limit set on\
  \ how many computer accounts a specific user or group can create in the domain.\n\nWhen a user attempts to create a new\
  \ computer account, AD checks the current number of computer accounts that the user has already created against the defined\
  \ quota for that user or group.\n\nHowever, Active Directory does not store the current count of created machine accounts\
  \ directly in a user attribute. Instead, you would need to perform a query to count the machine accounts that were created\
  \ by a specific user.\n\n## Machine Account Quota Process\n\n1. **Quota Definition**: The `MachineAccountQuota` is defined\
  \ at the domain level and can be set for individual users or groups. By default, it is set to **10** for the \"Domain Admins\"\
  \ group and to 0 for standard users, limiting their capability to create computer accounts.\n\n    ```powershell\n    nxc\
  \ ldap <ip> -u user -p pass -M maq\n    ```\n\n2. **Creation Process**: When a user attempts to create a new computer account\
  \ (for example, by using the \"Add Computer\" option in Active Directory Users and Computers or via PowerShell), the account\
  \ creation request is made to the domain controllers (DCs).\n\n    ```powershell\n    impacket@linux> addcomputer.py -computer-name\
  \ 'ControlledComputer$' -computer-pass 'ComputerPassword' -dc-host DC01 -domain-netbios domain 'domain.local/user1:complexpassword'\n\
  \    ```\n\n3. **Quota Evaluation**: Before the account is created, Active Directory checks the current count of computer\
  \ accounts created by that user. This is done by querying the `msDS-CreatorSID` attribute, which holds the SID of the user\
  \ who created that object.\nThe system compares this count to the `MachineAccountQuota` value set for that user. If the\
  \ count is less than the quota, the creation proceeds; if it equals or exceeds the quota, the creation is denied, and an\
  \ error is returned.\n\n    ```powershell\n    # Replace DOMAIN\\username with the actual domain and user name\n    $user\
  \ = \"DOMAIN\\username\"\n\n    # Get the user's SID\n    $userSID = (Get-ADUser -Identity $user).SID\n\n    # Count the\
  \ number of computer accounts created by this user\n    $computerCount = (Get-ADComputer -Filter { msDS-CreatorSID -eq $userSID\
  \ }).Count\n\n    # Display the count\n    $computerCount\n    ```\n\n4. **Failure Handling**: If the quota is exceeded,\
  \ the user attempting to create the account will receive an error message indicating that they cannot create a new computer\
  \ account because they have reached their quota limit.\n\n## References\n\n* [MachineAccountQuota - The Hacker Recipes -\
  \ 24/10/2024](https://www.thehacker.recipes/ad/movement/builtins/machineaccountquota)\n* [MachineAccountQuota is USEFUL\
  \ Sometimes: Exploiting One of Active Directory's Oddest Settings - Kevin Robertson - March 6, 2019](https://www.netspi.com/blog/technical-blog/network-penetration-testing/machineaccountquota-is-useful-sometimes/)\n\
  * [Machine Account Quota - NetExec - 13/09/2023](https://www.netexec.wiki/ldap-protocol/machine-account-quota)"
_relative_path: active-directory/ad-adds-machineaccountquota.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-machineaccountquota.md
````
