---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Bruteforce Hash Few Chars

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-python-bruteforce-hash-few-chars` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/python/bruteforce-hash-few-chars.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bruteforce Hash Few Chars](../../topics/generic-methodologies-and-resources/bruteforce-hash-few-chars.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-python-bruteforce-hash-few-chars |
| name | Bruteforce Hash Few Chars |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/python/bruteforce-hash-few-chars.md |

## Preserved Source Material

````yaml
_body: "# Bruteforce Hash Few Chars\n\n{{#include ../../banners/hacktricks-training.md}}\n\n```python\nimport hashlib\n\n\
  target = '2f2e2e' #/..\ncandidate = 0\nwhile True:\n    plaintext = str(candidate)\n    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()\n\
  \    if hash[-1*(len(target)):] == target: #End in target\n        print('plaintext:\"' + plaintext + '\", md5:' + hash)\n\
  \        break\n    candidate = candidate + 1\n```\n\n```python\n#From isHaacK\nimport hashlib\nfrom multiprocessing import\
  \ Process, Queue, cpu_count\n\n\ndef loose_comparison(queue, num):\n\ttarget = '0e'\n\tplaintext = f\"a_prefix{str(num)}a_suffix\"\
  \n\thash = hashlib.md5(plaintext.encode('ascii')).hexdigest()\n\n\tif hash[:len(target)] == target and not any(x in \"abcdef\"\
  \ for x in hash[2:]):\n\t\tprint('plaintext: ' + plaintext + ', md5: ' + hash)\n\t\tqueue.put(\"done\") # triggers program\
  \ exit\n\ndef worker(queue, thread_i, threads):\n\tfor num in range(thread_i, 100**50, threads):\n\t\tloose_comparison(queue,\
  \ num)\n\ndef main():\n\tprocs = []\n\tqueue = Queue()\n\tthreads = cpu_count() # 2\n\n\tfor thread_i in range(threads):\n\
  \t\tproc = Process(target=worker, args=(queue, thread_i, threads ))\n\t\tproc.daemon = True # kill all subprocess when main\
  \ process exits.\n\t\tprocs.append(proc)\n\t\tproc.start()\n\n\twhile queue.empty(): # exits when a subprocess is done\n\
  \t\tpass\n\treturn 0\n\nmain()\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: generic-methodologies-and-resources/python/bruteforce-hash-few-chars.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/python/bruteforce-hash-few-chars.md
````
