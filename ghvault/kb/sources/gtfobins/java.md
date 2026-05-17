---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# java

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `java` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/java` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [java](../../tools/linux/java.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | java |
| name | java |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/java/ |

## Preserved Source Material

````yaml
_body: ''
_name: java
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/java
functions:
  shell:
  - code: java Shell
    comment: "The `Shell.class` class file can be compiled offline, then uploaded to the target:\n\n```\ncat >Shell.java <<EOF\n\
      public class Shell {\n    public static void main(String[] args) throws Exception {\n        new ProcessBuilder(\"/bin/sh\"\
      ).inheritIO().start().waitFor();\n    }\n}\nEOF\n\njavac Shell.java\n```"
    contexts:
      sudo: null
      unprivileged: null
````
