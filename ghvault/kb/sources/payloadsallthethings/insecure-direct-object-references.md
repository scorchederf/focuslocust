---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Insecure Direct Object References

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-direct-object-references-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Direct Object References/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Insecure Direct Object References](../../topics/insecure-direct-object-references/insecure-direct-object-references.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-direct-object-references-readme |
| name | Insecure Direct Object References |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Direct%20Object%20References/README.md |

## Preserved Source Material

````yaml
_body: "# Insecure Direct Object References\n\n> Insecure Direct Object References (IDOR) is a security vulnerability that\
  \ occurs when an application allows users to directly access or modify objects (such as files, database records, or URLs)\
  \ based on user-supplied input, without sufficient access controls. This means that if a user changes a parameter value\
  \ (like an ID) in a URL or API request, they might be able to access or manipulate data that they aren’t authorized to see\
  \ or modify.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Numeric Value Parameter](#numeric-value-parameter)\n\
  \    * [Common Identifiers Parameter](#common-identifiers-parameter)\n    * [Weak Pseudo Random Number Generator](#weak-pseudo-random-number-generator)\n\
  \    * [Hashed Parameter](#hashed-parameter)\n    * [Wildcard Parameter](#wildcard-parameter)\n    * [IDOR Tips](#idor-tips)\n\
  * [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [PortSwigger/BApp Store > Authz](https://portswigger.net/bappstore/4316cc18ac5f434884b2089831c7d19e)\n\
  * [PortSwigger/BApp Store > AuthMatrix](https://portswigger.net/bappstore/30d8ee9f40c041b0bfec67441aad158e)\n* [PortSwigger/BApp\
  \ Store > Autorize](https://portswigger.net/bappstore/f9bbac8c4acf4aefa4d7dc92a991af2f)\n\n## Methodology\n\nIDOR stands\
  \ for Insecure Direct Object Reference. It's a type of security vulnerability that arises when an application provides direct\
  \ access to objects based on user-supplied input. As a result, attackers can bypass authorization and access resources in\
  \ the system directly, potentially leading to unauthorized information disclosure, modification, or deletion.\n\n**Example\
  \ of IDOR**:\n\nImagine a web application that allows users to view their profile by clicking a link `https://example.com/profile?user_id=123`:\n\
  \n```php\n<?php\n    $user_id = $_GET['user_id'];\n    $user_info = get_user_info($user_id);\n    ...\n```\n\nHere, `user_id=123`\
  \ is a direct reference to a specific user's profile. If the application doesn't properly check that the logged-in user\
  \ has the right to view the profile associated with `user_id=123`, an attacker could simply change the `user_id` parameter\
  \ to view other users' profiles:\n\n```ps1\nhttps://example.com/profile?user_id=124\n```\n\n![https://lh5.googleusercontent.com/VmLyyGH7dGxUOl60h97Lr57F7dcnDD8DmUMCZTD28BKivVI51BLPIqL0RmcxMPsmgXgvAqY8WcQ-Jyv5FhRiCBueX9Wj0HSCBhE-_SvrDdA6_wvDmtMSizlRsHNvTJHuy36LG47lstLpTqLK](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Insecure%20Direct%20Object%20References/Images/idor.png)\n\
  \n### Numeric Value Parameter\n\nIncrement and decrement these values to access sensitive information.\n\n* Decimal value:\
  \ `287789`, `287790`, `287791`, ...\n* Hexadecimal: `0x4642d`, `0x4642e`, `0x4642f`, ...\n* Unix epoch timestamp: `1695574808`,\
  \ `1695575098`, ...\n\n**Examples**:\n\n* [HackerOne - IDOR to view User Order Information - meals](https://hackerone.com/reports/287789)\n\
  * [HackerOne - Delete messages via IDOR - naaash](https://hackerone.com/reports/697412)\n\n### Common Identifiers Parameter\n\
  \nSome identifiers can be guessed like names and emails, they might grant you access to customer data.\n\n* Name: `john`,\
  \ `doe`, `john.doe`, ...\n* Email: `john.doe@mail.com`\n* Base64 encoded value: `am9obi5kb2VAbWFpbC5jb20=`\n\n**Examples**:\n\
  \n* [HackerOne - Insecure Direct Object Reference (IDOR) - Delete Campaigns - datph4m](https://hackerone.com/reports/1969141)\n\
  \n### Weak Pseudo Random Number Generator\n\n* UUID/GUID v1 can be predicted if you know the time they were created: `95f6e264-bb00-11ec-8833-00155d01ef00`\n\
  * MongoDB Object Ids are generated in a predictable manner: `5ae9b90a2c144b9def01ec37`\n    * a 4-byte value representing\
  \ the seconds since the Unix epoch\n    * a 3-byte machine identifier\n    * a 2-byte process id\n    * a 3-byte counter,\
  \ starting with a random value\n\n**Examples**:\n\n* [HackerOne - IDOR allowing to read another user's token on the Social\
  \ Media Ads service - a_d_a_m](https://hackerone.com/reports/1464168)\n* [IDOR through MongoDB Object IDs Prediction](https://techkranti.com/idor-through-mongodb-object-ids-prediction/)\n\
  \n### Hashed Parameter\n\nSometimes we see websites using hashed values to generate a random user id or token, like `sha1(username)`,\
  \ `md5(email)`, ...\n\n* MD5: `098f6bcd4621d373cade4e832627b4f6`\n* SHA1: `a94a8fe5ccb19ba61c4c0873d391e987982fbbd3`\n*\
  \ SHA2: `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`\n\n**Examples**:\n\n* [IDOR with Predictable\
  \ HMAC Generation - DiceCTF 2022 - CryptoCat](https://youtu.be/Og5_5tEg6M0)\n\n### Wildcard Parameter\n\nSend a wildcard\
  \ (`*`, `%`, `.`, `_`) instead of an ID, some backend might respond with the data of all the users.\n\n* `GET /api/users/*\
  \ HTTP/1.1`\n* `GET /api/users/% HTTP/1.1`\n* `GET /api/users/_ HTTP/1.1`\n* `GET /api/users/. HTTP/1.1`\n\n### IDOR Tips\n\
  \n* Change the HTTP request: `POST → PUT`\n* Change the content type: `XML → JSON`\n* Transform numerical values to arrays:\
  \ `{\"id\":19} → {\"id\":[19]}`\n* Use Parameter Pollution: `user_id=hacker_id&user_id=victim_id`\n\n## Labs\n\n* [PortSwigger\
  \ - Insecure Direct Object References](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)\n\
  \n## References\n\n* [From Christmas present in the blockchain to massive bug bounty - Jesse Lakerveld - March 21, 2018](http://web.archive.org/web/20180401130129/https://www.vicompany.nl/magazine/from-christmas-present-in-the-blockchain-to-massive-bug-bounty)\n\
  * [How-To: Find IDOR (Insecure Direct Object Reference) Vulnerabilities for large bounty rewards - Sam Houton - November\
  \ 9, 2017](https://web.archive.org/web/20260221194813/https://www.bugcrowd.com/blog/how-to-find-idor-insecure-direct-object-reference-vulnerabilities-for-large-bounty-rewards/)\n\
  * [Hunting Insecure Direct Object Reference Vulnerabilities for Fun and Profit (PART-1) - Mohammed Abdul Raheem - February\
  \ 2, 2018](https://web.archive.org/web/20190509043727/https://codeburst.io/hunting-insecure-direct-object-reference-vulnerabilities-for-fun-and-profit-part-1-f338c6a52782)\n\
  * [IDOR - how to predict an identifier? Bug bounty case study - Bug Bounty Reports Explained - September 21, 2023](https://web.archive.org/web/20231027235449/https://youtu.be/wx5TwS0Dres)\n\
  * [Insecure Direct Object Reference Prevention Cheat Sheet - OWASP - July 31, 2023](https://web.archive.org/web/20140316052400/https://www.owasp.org/index.php/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet)\n\
  * [Insecure direct object references (IDOR) - PortSwigger - December 25, 2019](https://web.archive.org/web/20260301072233/https://portswigger.net/web-security/access-control/idor)\n\
  * [Testing for IDORs - PortSwigger - October 29, 2024](https://web.archive.org/web/20230604162333/https://portswigger.net/burp/documentation/desktop/testing-workflow/access-controls/testing-for-idors)\n\
  * [Testing for Insecure Direct Object References (OTG-AUTHZ-004) - OWASP - August 8, 2014](https://web.archive.org/web/20170712205114/https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004))\n\
  * [The Rise of IDOR - HackerOne - April 2, 2021](https://web.archive.org/web/20211004153030/https://www.hackerone.com/company-news/rise-idor)\n\
  * [Web to App Phone Notification IDOR to view Everyone's Airbnb Messages - Brett Buerhaus - March 31, 2017](https://web.archive.org/web/20170408053950/http://buer.haus:80/2017/03/31/airbnb-web-to-app-phone-notification-idor-to-view-everyones-airbnb-messages)"
_relative_path: Insecure Direct Object References/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Direct Object References/README.md
````
