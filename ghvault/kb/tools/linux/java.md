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

## Summary

GTFOBins entry for java covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/java.md)
- Source verification: [source record](../../sources/gtfobins/java.md)

## Aliases

- `java`

## Source Verification

[source record](../../sources/gtfobins/java.md)

## Evidence Excerpt

````text
_body: ''
_name: java
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/java
functions:
shell:
- code: java Shell
comment: "The `Shell.class` class file can be compiled offline, then uploaded to the target:\n\n```\ncat >Shell.java <<EOF\n\
public class Shell {\n    public static void main(String[] args) throws Exception {\n        new ProcessBuilder(\"/bin/sh\"\
````
