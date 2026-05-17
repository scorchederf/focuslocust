---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Tricks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-tricks` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-tricks.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Tricks](../../topics/active-directory/active-directory-tricks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-tricks |
| name | Active Directory - Tricks |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-tricks.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Tricks\n\n## Kerberos Clock Synchronization\n\nIn Kerberos, time is used to ensure that tickets\
  \ are valid. To achieve this, the clocks of all Kerberos clients and servers in a realm must be synchronized to within a\
  \ certain tolerance. The default clock skew tolerance in Kerberos is `5 minutes`, which means that the difference in time\
  \ between the clocks of any two Kerberos entities should be no more than 5 minutes.\n\n* Detect clock skew automatically\
  \ with `nmap`\n\n  ```powershell\n  $ nmap -sV -sC 10.10.10.10\n  clock-skew: mean: -1998d09h03m04s, deviation: 4h00m00s,\
  \ median: -1998d11h03m05s\n  ```\n\n* Compute yourself the difference between the clocks\n\n  ```ps1\n  nmap -sT 10.10.10.10\
  \ -p445 --script smb2-time -vv\n  ```\n\n* Fix #1: Modify your clock\n\n  ```ps1\n  sudo date -s \"14 APR 2015 18:25:16\"\
  \ # Linux\n  net time /domain /set # Windows\n  ```\n\n* Fix #2: Fake your clock\n\n  ```ps1\n  faketime -f '+8h' date\n\
  \  ```\n\n## References\n\n* [BUILDING AND ATTACKING AN ACTIVE DIRECTORY LAB WITH POWERSHELL - @myexploit2600 & @5ub34x](https://1337red.wordpress.com/building-and-attacking-an-active-directory-lab-with-powershell/)\n\
  * [Becoming Darth Sidious: Creating a Windows Domain (Active Directory) and hacking it - @chryzsh](https://chryzsh.gitbooks.io/darthsidious/content/building-a-lab/building-a-lab/building-a-small-lab.html)\n\
  * [Chump2Trump - AD Privesc talk at WAHCKon 2017 - @l0ss](https://github.com/l0ss/Chump2Trump/blob/master/ChumpToTrump.pdf)\n\
  * [How to build a SQL Server Virtual Lab with AutomatedLab in Hyper-V - October 30, 2017 - Craig Porteous](https://www.sqlshack.com/build-sql-server-virtual-lab-automatedlab-hyper-v/)"
_relative_path: active-directory/ad-tricks.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-tricks.md
````
