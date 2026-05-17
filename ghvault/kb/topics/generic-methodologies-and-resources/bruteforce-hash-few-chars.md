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

## Summary

python

## Preserved Body

````markdown
```python
import hashlib

target = '2f2e2e' #/..
candidate = 0
while True:
    plaintext = str(candidate)
    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()
    if hash[-1*(len(target)):] == target: #End in target
        print('plaintext:"' + plaintext + '", md5:' + hash)
        break
    candidate = candidate + 1
```

```python
#From isHaacK
import hashlib
from multiprocessing import Process, Queue, cpu_count


def loose_comparison(queue, num):
	target = '0e'
	plaintext = f"a_prefix{str(num)}a_suffix"
	hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()

	if hash[:len(target)] == target and not any(x in "abcdef" for x in hash[2:]):
		print('plaintext: ' + plaintext + ', md5: ' + hash)
		queue.put("done") # triggers program exit

def worker(queue, thread_i, threads):
	for num in range(thread_i, 100**50, threads):
		loose_comparison(queue, num)

def main():
	procs = []
	queue = Queue()
	threads = cpu_count() # 2

	for thread_i in range(threads):
		proc = Process(target=worker, args=(queue, thread_i, threads ))
		proc.daemon = True # kill all subprocess when main process exits.
		procs.append(proc)
		proc.start()

	while queue.empty(): # exits when a subprocess is done
		pass
	return 0

main()
```
````

## Source Verification

[source record](../../sources/hacktricks/bruteforce-hash-few-chars.md)

## Evidence Excerpt

````text
_body: "# Bruteforce Hash Few Chars\n\n{{#include ../../banners/hacktricks-training.md}}\n\n```python\nimport hashlib\n\n\
target = '2f2e2e' #/..\ncandidate = 0\nwhile True:\n    plaintext = str(candidate)\n    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()\n\
\    if hash[-1*(len(target)):] == target: #End in target\n        print('plaintext:\"' + plaintext + '\", md5:' + hash)\n\
\        break\n    candidate = candidate + 1\n```\n\n```python\n#From isHaacK\nimport hashlib\nfrom multiprocessing import\
\ Process, Queue, cpu_count\n\n\ndef loose_comparison(queue, num):\n\ttarget = '0e'\n\tplaintext = f\"a_prefix{str(num)}a_suffix\"\
\n\thash = hashlib.md5(plaintext.encode('ascii')).hexdigest()\n\n\tif hash[:len(target)] == target and not any(x in \"abcdef\"\
\ for x in hash[2:]):\n\t\tprint('plaintext: ' + plaintext + ', md5: ' + hash)\n\t\tqueue.put(\"done\") # triggers program\
\ exit\n\ndef worker(queue, thread_i, threads):\n\tfor num in range(thread_i, 100**50, threads):\n\t\tloose_comparison(queue,\
````
