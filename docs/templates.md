# Templates

Focus Locust uses Jinja2 templates. Templates are source-specific.

Current implemented template folders:

```text
templates/
├── build/
├── gtfobins/
├── hacktricks/
├── internalallthethings/
├── lolbas/
├── mitre/
├── payloadsallthethings/
└── shared/
```

```mermaid
flowchart LR
    Object[parsed object] --> SourceTemplate[source template]
    SourceTemplate --> Markdown[generated Markdown]
    Markdown --> SafeWrite[safe write marker check]
```

## MITRE Templates

```text
templates/mitre/tactic.md.j2
templates/mitre/technique.md.j2
templates/mitre/mitigation.md.j2
templates/mitre/data-source.md.j2
templates/mitre/tool.md.j2
templates/mitre/index.md.j2
```

## LOLBAS Templates

```text
templates/lolbas/tool.md.j2
templates/lolbas/index.md.j2
```

LOLBAS templates render normalized fields such as `obj.name`, `obj.commands`, and `obj.path`, and can also access preserved raw YAML through `obj.raw`.

## GTFOBins Templates

```text
templates/gtfobins/tool.md.j2
templates/gtfobins/index.md.j2
```

GTFOBins templates render normalized fields such as `obj.name`, `obj.functions`, `obj.function_examples`, and `obj.path`, and can also access preserved source frontmatter through `obj.raw`.

## PayloadsAllTheThings Templates

```text
templates/payloadsallthethings/payload-topic.md.j2
templates/payloadsallthethings/moved-reference.md.j2
templates/payloadsallthethings/index.md.j2
```

PayloadsAllTheThings templates render topic/reference pages from Markdown files. They use normalized fields such as `obj.name`, `obj.category`, `obj.relative_path`, `obj.headings`, `obj.body`, and `obj.moved_to`.

## InternalAllTheThings Templates

```text
templates/internalallthethings/topic.md.j2
templates/internalallthethings/index.md.j2
```

InternalAllTheThings templates render internal pentest topic/reference pages from Markdown files. They use normalized fields such as `obj.name`, `obj.category`, `obj.relative_path`, `obj.headings`, and `obj.body`.

## HackTricks Templates

```text
templates/hacktricks/topic.md.j2
templates/hacktricks/index.md.j2
```

HackTricks templates render topic/reference pages from Markdown files. They use normalized fields such as `obj.name`, `obj.category`, `obj.relative_path`, `obj.headings`, and `obj.body`.

## Build Templates

```text
templates/build/object-properties.md.j2
```

This template renders representative `_build` object-property examples. The example object for each group is selected by the largest number of raw datasource fields.

## Raw Field Access

The renderer provides these filters:

```jinja
{{ obj.raw | field_value("Name") }}

{% for handle in obj.raw | field_values("Acknowledgement[].Handle") %}
- {{ handle }}
{% endfor %}
```

Use `_build` pages to discover paths:

```text
vault/kb/_build/datasource-fields.md
vault/kb/_build/objects/
```

## YAML Frontmatter

Use `yaml_quote` for frontmatter values that may contain backslashes or special characters:

```jinja
paths:
{% for value in obj.raw | field_values("Full_Path[].Path") %}
  - {{ value | yaml_quote }}
{% endfor %}
```

Generated templates must include:

```yaml
parsed_by: {{ parsed_marker }}
```
