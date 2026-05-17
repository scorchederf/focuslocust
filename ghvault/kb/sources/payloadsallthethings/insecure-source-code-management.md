---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Insecure Source Code Management

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-source-code-management-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Source Code Management/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Insecure Source Code Management](../../topics/insecure-source-code-management/insecure-source-code-management.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-source-code-management-readme |
| name | Insecure Source Code Management |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Source%20Code%20Management/README.md |

## Preserved Source Material

````yaml
_body: "# Insecure Source Code Management\n\n> Insecure Source Code Management (SCM) can lead to several critical vulnerabilities\
  \ in web applications and services. Developers often rely on SCM systems like Git and Subversion (SVN) to manage their source\
  \ code versions. However, poor security practices, such as leaving .git and .svn folders in production environments exposed\
  \ to the internet, can pose significant risks.\n\n## Summary\n\n* [Methodology](#methodology)\n    * [Bazaar](./Bazaar.md)\n\
  \    * [Git](./Git.md)\n    * [Mercurial](./Mercurial.md)\n    * [Subversion](./Subversion.md)\n* [Labs](#labs)\n* [References](#references)\n\
  \n## Methodology\n\nExposing the version control system folders on a web server can lead to severe security risks, including:\n\
  \n* **Source Code Leaks** : Attackers can download the entire source code repository, gaining access to the application's\
  \ logic.\n* **Sensitive Information Exposure** : Embedded secrets, configuration files, and credentials might be present\
  \ within the codebase.\n* **Commit History Exposure** : Attackers can view past changes, revealing sensitive information\
  \ that might have been previously exposed and later mitigated.\n\nThe first step is to gather information about the target\
  \ application. This can be done using various web reconnaissance tools and techniques.\n\n* **Manual Inspection** : Check\
  \ URLs manually by navigating to common SCM paths.\n    * Git: `http://target.com/.git/`\n    * SVN: `http://target.com/.svn/`\n\
  \n* **Automated Tools** : Refer to the page related to the specific technology.\n\nOnce a potential SCM folder is identified,\
  \ check the HTTP response codes and contents. You might need to bypass `.htaccess` or Reverse Proxy rules.\n\nThe NGINX\
  \ rule below returns a `403 (Forbidden)` response instead of `404 (Not Found)` when hitting the `/.git` endpoint.\n\n```ps1\n\
  location /.git {\n  deny all;\n}\n```\n\nFor example in Git, the exploitation technique doesn't require to list the content\
  \ of the `.git` folder (`http://target.com/.git/`), the data extraction can still be conducted when files can be read.\n\
  \n## Labs\n\n* [Root Me - Insecure Code Management](https://www.root-me.org/fr/Challenges/Web-Serveur/Insecure-Code-Management)\n\
  \n## References\n\n* [Hidden directories and files as a source of sensitive information about web application - bl4de -\
  \ April 30, 2017](https://github.com/bl4de/research/tree/master/hidden_directories_leaks)"
_relative_path: Insecure Source Code Management/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Source Code Management/README.md
````
