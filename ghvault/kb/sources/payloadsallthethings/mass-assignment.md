---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Mass Assignment

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-mass-assignment-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Mass Assignment/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mass Assignment](../../topics/mass-assignment/mass-assignment.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-mass-assignment-readme |
| name | Mass Assignment |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Mass%20Assignment/README.md |

## Preserved Source Material

````yaml
_body: "# Mass Assignment\n\n> A mass assignment attack is a security vulnerability that occurs when a web application automatically\
  \ assigns user-supplied input values to properties or variables of a program object. This can become an issue if a user\
  \ is able to modify attributes they should not have access to, like a user's permissions or an admin flag.\n\n## Summary\n\
  \n* [Methodology](#methodology)\n* [Labs](#labs)\n* [References](#references)\n\n## Methodology\n\nMass assignment vulnerabilities\
  \ are most common in web applications that use Object-Relational Mapping (ORM) techniques or functions to map user input\
  \ to object properties, where properties can be updated all at once instead of individually. Many popular web development\
  \ frameworks such as Ruby on Rails, Django, and Laravel (PHP) offer this functionality.\n\nFor instance, consider a web\
  \ application that uses an ORM and has a user object with the attributes `username`, `email`, `password`, and `isAdmin`.\
  \ In a normal scenario, a user might be able to update their own username, email, and password through a form, which the\
  \ server then assigns to the user object.\n\nHowever, an attacker may attempt to add an `isAdmin` parameter to the incoming\
  \ data like so:\n\n```json\n{\n    \"username\": \"attacker\",\n    \"email\": \"attacker@email.com\",\n    \"password\"\
  : \"unsafe_password\",\n    \"isAdmin\": true\n}\n```\n\nIf the web application is not checking which parameters are allowed\
  \ to be updated in this way, it might set the `isAdmin` attribute based on the user-supplied input, giving the attacker\
  \ admin privileges\n\n## Labs\n\n* [PentesterAcademy - Mass Assignment I](https://attackdefense.pentesteracademy.com/challengedetailsnoauth?cid=1964)\n\
  * [PentesterAcademy - Mass Assignment II](https://attackdefense.pentesteracademy.com/challengedetailsnoauth?cid=1922)\n\
  * [Root Me - API - Mass Assignment](https://www.root-me.org/en/Challenges/Web-Server/API-Mass-Assignment)\n\n## References\n\
  \n* [Hunting for Mass Assignment - Shivam Bathla - August 12, 2021](https://blog.pentesteracademy.com/hunting-for-mass-assignment-56ed73095eda)\n\
  * [Mass Assignment Cheat Sheet - OWASP - March 15, 2021](https://web.archive.org/web/20260216020815/https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)\n\
  * [What is Mass Assignment? Attacks and Security Tips - Yoan MONTOYA - June 15, 2023](https://www.vaadata.com/blog/what-is-mass-assignment-attacks-and-security-tips/)"
_relative_path: Mass Assignment/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Mass Assignment/README.md
````
