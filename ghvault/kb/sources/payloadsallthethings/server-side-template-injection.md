---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Template Injection](../../topics/server-side-template-injection/server-side-template-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-template-injection-readme |
| name | Server Side Template Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# Server Side Template Injection\n\n> Template injection allows an attacker to include template code into an existing\
  \ (or not) template. A template engine makes designing HTML pages easier by using static template files which at runtime\
  \ replaces variables/placeholders with actual values in the HTML pages.\n\n## Summary\n\n- [Tools](#tools)\n- [Methodology](#methodology)\n\
  \    - [Detection and Exploitation Techniques](#detection-and-exploitation-techniques)\n        - [Rendered](#rendered)\n\
  \        - [Error-Based](#error-based)\n        - [Boolean-Based](#boolean-based)\n        - [Time-Based](#time-based)\n\
  \        - [Out of Bounds](#out-of-bounds)\n        - [Polyglot-Based](#polyglot-based)\n    - [Universal Detection Payloads](#universal-detection-payloads)\n\
  \    - [Manual Detection and Exploitation](#manual-detection-and-exploitation)\n        - [Identify the Vulnerable Input\
  \ Field](#identify-the-vulnerable-input-field)\n        - [Inject Template Syntax](#inject-template-syntax)\n        - [Enumerate\
  \ the Template Engine](#enumerate-the-template-engine)\n        - [Escalate to Code Execution](#escalate-to-code-execution)\n\
  - [Labs](#labs)\n- [References](#references)\n\n## Tools\n\n- [Hackmanit/TInjA](https://github.com/Hackmanit/TInjA) - An\
  \ efficient SSTI + CSTI scanner which utilizes novel polyglots\n\n  ```bash\n  tinja url -u \"http://example.com/?name=Kirlia\"\
  \ -H \"Authentication: Bearer ey...\"\n  tinja url -u \"http://example.com/\" -d \"username=Kirlia\"  -c \"PHPSESSID=ABC123...\"\
  \n  ```\n\n- [epinna/tplmap](https://github.com/epinna/tplmap) - Server-Side Template Injection and Code Injection Detection\
  \ and Exploitation Tool\n\n  ```powershell\n  python2.7 ./tplmap.py -u 'http://www.target.com/page?name=John*' --os-shell\n\
  \  python2.7 ./tplmap.py -u \"http://192.168.56.101:3000/ti?user=*&comment=supercomment&link\"\n  python2.7 ./tplmap.py\
  \ -u \"http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link\" --level 5 -e jade\n  ```\n\n- [vladko312/SSTImap](https://github.com/vladko312/SSTImap)\
  \ - Automatic SSTI detection tool with interactive interface based on [epinna/tplmap](https://github.com/epinna/tplmap)\n\
  \n  ```bash\n  python3 ./sstimap.py -u 'https://example.com/page?name=John' -s\n  python3 ./sstimap.py -i -u 'https://example.com/page?name=Vulnerable*&message=My_message'\
  \ -l 5 -e jade\n  python3 ./sstimap.py -i -A -m POST -l 5 -H 'Authorization: Basic bG9naW46c2VjcmV0X3Bhc3N3b3Jk'\n  ```\n\
  \n## Methodology\n\n### Detection and Exploitation Techniques\n\nOriginal research:\n\n- Rendered, Time-Based: [Server-Side\
  \ Template Injection: RCE For The Modern Web App - James Kettle - August 05, 2015](https://portswigger.net/knowledgebase/papers/serversidetemplateinjection.pdf)\n\
  - Polyglot-Based: [Improving the Detection and Identification of Template Engines for Large-Scale Template Injection Scanning\
  \ - Maximilian Hildebrand - September 19, 2023](https://www.hackmanit.de/images/download/thesis/Improving-the-Detection-and-Identification-of-Template-Engines-for-Large-Scale-Template-Injection-Scanning-Maximilian-Hildebrand-Master-Thesis-Hackmanit.pdf)\n\
  - Error-Based, Boolean-Based: [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January\
  \ 03, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)\n\n#### Rendered\n\n![Rendered\
  \ technique workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/technique_Rendered.png?raw=true)\n\
  \n> Applicability: detection, exploitation\n\nWhen the rendered template is displayed to the attacker, Rendered technique\
  \ can be used to include the results of the injected code on the page.\n\n#### Error-Based\n\n![Error-Based technique workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/technique_Error-Based.png?raw=true)\n\
  \n> Applicability: detection, exploitation\n\nWhen the errors are verbosely displayed to the attacker, Error-Based technique\
  \ can be used to trigger the error message containing the results of the injected code.\n\n#### Boolean-Based\n\n![Boolean-Based\
  \ technique workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/technique_Boolean-Based.png?raw=true)\n\
  \n> Applicability: detection, blind exploitation, blind data exfiltration\n\nBoolean-Based technique can be used to conditionally\
  \ trigger an error to indicate success or failure of the injected code.\n\n#### Time-Based\n\n![Time-Based technique workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/technique_Time-Based.png?raw=true)\n\
  \n> Applicability: limited detection, blind exploitation, blind data exfiltration\n\nTime-Based technique can be used to\
  \ conditionally trigger the delay to indicate success or failure of the injected code.\n\nTriggering the delay often requires\
  \ guessing payloads for code evaluation or OS command execution.\n\n#### Out of Bounds\n\n> Applicability: limited detection,\
  \ exploitation\n\nOut of Bounds technique can be used to expose results of the injected code through other channels (e.g.\
  \ by connecting to an attacker-controlled server).\n\nThis technique often requires guessing payloads for code evaluation\
  \ or OS command execution.\n\n#### Polyglot-Based\n\n![Polyglot-Based technique workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/technique_Polyglot-Based.png?raw=true)\n\
  \n> Applicability: detection\n\nPolyglot-Based technique can be used to quickly determine the template engine by checking\
  \ how it transforms different payloads.\n\n### Universal Detection Payloads\n\nPolyglot to trigger an error in presence\
  \ of SSTI vulnerability:\n\n```ps1\n${{<%[%'\"}}%\\.\n```\n\nCommon tags to test for SSTI with code evaluation:\n\n```powershell\n\
  {{ ... }}\n${ ... }\n#{ ... }\n<%= ... %>\n{ ... }\n{{= ... }}\n{= ... }\n\\n= ... \\n\n*{ ... }\n@{ ... }\n@( ... )\n```\n\
  \nRendered SSTI can be checked by using mathematical expressions inside the tags:\n\n```powershell\n7 * 7\n```\n\nError-Based\
  \ SSTI can be checked by using this payload inside the tags:\n\n```powershell\n(1/0).zxy.zxy\n```\n\nIf the error caused\
  \ by that payload is displayed verbosely, it can be checked to guess the language used for code evaluation:\n\n| Error \
  \                        | Language          |\n|-------------------------------|-------------------|\n| ZeroDivisionError\
  \             | Python            |\n| java.lang.ArithmeticException | Java              |\n| ReferenceError           \
  \     | NodeJS            |\n| TypeError                     | NodeJS            |\n| Division by zero              | PHP\
  \               |\n| DivisionByZeroError           | PHP               |\n| divided by 0                  | Ruby       \
  \       |\n| Arithmetic operation failed   | Freemarker (Java) |\n\nTo test for blind injections using Boolean-Based technique,\
  \ the attacker can test pairs of similar payloads wrapped in tags, where one payload evaluates mathematical expression,\
  \ while the other triggers syntax error:\n\n| test | ok              | error           |\n|------|-----------------|-----------------|\n\
  | 1    | `(3*4/2)`       | `3*)2(/4`       |\n| 2    | `((7*8)/(2*4))` | `7)(*)8)(2/(*4` |\n\nUsing at least two pairs of\
  \ payloads avoids false positives caused by external interference.\n\n### Manual Detection and Exploitation\n\n#### Identify\
  \ the Vulnerable Input Field\n\nThe attacker first locates an input field, URL parameter, or any user-controllable part\
  \ of the application that is passed into a server-side template without proper sanitization or escaping.\n\nFor example,\
  \ the attacker might identify a web form, search bar, or template preview functionality that seems to return results based\
  \ on dynamic user input.\n\n**TIP**: Generated PDF files, invoices and emails usually use a template.\n\n#### Inject Template\
  \ Syntax\n\nThe attacker tests the identified input field by injecting template syntax specific to the template engine in\
  \ use. Different web frameworks use different template engines (e.g., Jinja2 for Python, Twig for PHP, or FreeMarker for\
  \ Java).\n\nCommon template expressions:\n\n- `{{7*7}}` for Jinja2 (Python).\n- `#{7*7}` for Thymeleaf (Java).\n\nFind more\
  \ template expressions in the page dedicated to the technology (PHP, Python, etc).\n\n![SSTI cheatsheet workflow](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Images/serverside.png?raw=true)\n\
  \nIn most cases, this polyglot payload will trigger an error in presence of a SSTI vulnerability:\n\n```ps1\n${{<%[%'\"\
  }}%\\.\n```\n\nThe [Hackmanit/Template Injection Table](https://github.com/Hackmanit/template-injection-table) is an interactive\
  \ table containing the most efficient template injection polyglots along with the expected responses of the 44 most important\
  \ template engines.\n\n#### Enumerate the Template Engine\n\nBased on the successful response, the attacker determines which\
  \ template engine is being used. This step is critical because different template engines have different syntax, features,\
  \ and potential for exploitation. The attacker may try different payloads to see which one executes, thereby identifying\
  \ the engine.\n\n- **Python**: Django, Jinja2, Mako, ...\n- **Java**: Freemarker, Jinjava, Velocity, ...\n- **Ruby**: ERB,\
  \ Slim, ...\n\n[The post \"template-engines-injection-101\" from @0xAwali](https://medium.com/@0xAwali/template-engines-injection-101-4f2fe59e5756)\
  \ summarize the syntax and detection method for most of the template engines for JavaScript, Python, Ruby, Java and PHP\
  \ and how to differentiate between engines that use the same syntax.\n\n#### Escalate to Code Execution\n\nOnce the template\
  \ engine is identified, the attacker injects more complex expressions, aiming to execute server-side commands or arbitrary\
  \ code.\n\n## Labs\n\n- [Root Me - Java - Server-side Template Injection](https://www.root-me.org/en/Challenges/Web-Server/Java-Server-side-Template-Injection)\n\
  - [Root Me - Python - Server-side Template Injection Introduction](https://www.root-me.org/en/Challenges/Web-Server/Python-Server-side-Template-Injection-Introduction)\n\
  - [Root Me - Python - Blind SSTI Filters Bypass](https://www.root-me.org/en/Challenges/Web-Server/Python-Blind-SSTI-Filters-Bypass)\n\
  \n## References\n\n- [Server-Side Template Injection: RCE For The Modern Web App - James Kettle - August 05, 2015](https://web.archive.org/web/20160311193057/https://portswigger.net/knowledgebase/papers/ServerSideTemplateInjection.pdf)\n\
  - [Improving the Detection and Identification of Template Engines for Large-Scale Template Injection Scanning - Maximilian\
  \ Hildebrand - September 19, 2023](https://web.archive.org/web/20231210014226/https://www.hackmanit.de/images/download/thesis/Improving-the-Detection-and-Identification-of-Template-Engines-for-Large-Scale-Template-Injection-Scanning-Maximilian-Hildebrand-Master-Thesis-Hackmanit.pdf)\n\
  - [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)\n\
  - [A Pentester's Guide to Server Side Template Injection (SSTI) - Busra Demir - December 24, 2020](https://web.archive.org/web/20260111213449/https://www.cobalt.io/blog/a-pentesters-guide-to-server-side-template-injection-ssti)\n\
  - [Gaining Shell using Server Side Template Injection (SSTI) - David Valles - August 22, 2018](https://web.archive.org/web/20180928123607/https://medium.com/@david.valles/gaining-shell-using-server-side-template-injection-ssti-81e29bb8e0f9)\n\
  - [Template Engines Injection 101 - Mahmoud M. Awali - November 1, 2024](https://web.archive.org/web/20251104003639/https://medium.com/@0xAwali/template-engines-injection-101-4f2fe59e5756)\n\
  - [Template Injection On Hardened Targets - Lucas 'BitK' Philippe - September 28, 2022](https://web.archive.org/web/20230314135020/https://youtu.be/M0b_KA0OMFw)\n\
  - [Limitations are just an illusion – advanced server-side template exploitation with RCE everywhere - YesWeHack, Brumens\
  \ - March 24, 2025](https://web.archive.org/web/20240906203847/https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation)"
_relative_path: Server Side Template Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/README.md
````
