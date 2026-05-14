# Architecture

Focus Locust is a source-specific Markdown builder for an Obsidian security knowledge base.

```mermaid
flowchart TD
    CLI[builder.py] --> Config[load config.yml]
    Config --> Paths[ensure repo-local paths]
    Paths --> Clean[clean generated Markdown]
    Clean --> Sources[enabled sources]
    Sources --> MITRE[MITRE STIX loader/parser]
    Sources --> LOLBAS[LOLBAS YAML loader/parser]
    Sources --> GTFOBins[GTFOBins Markdown loader/parser]
    Sources --> PATT[PayloadsAllTheThings Markdown loader/parser]
    Sources --> IATT[InternalAllTheThings Markdown loader/parser]
    Sources --> HackTricks[HackTricks Markdown loader/parser]
    MITRE --> Renderer[MarkdownRenderer]
    LOLBAS --> Renderer
    GTFOBins --> Renderer
    PATT --> Renderer
    IATT --> Renderer
    HackTricks --> Renderer
    Renderer --> Templates[source-specific templates]
    Templates --> SafeWrite[safe_write_text]
    SafeWrite --> Vault[vault/kb]
    Sources --> BuildSummary[_build field references]
```

## Code Map

| Area | File | Notes |
| --- | --- | --- |
| CLI | `builder.py` | Commands: `build`, `clean`, `doctor`. |
| Config | `src/kb_builder/config.py` | Loads YAML config from inside the repo. |
| Paths | `src/kb_builder/paths.py` | Creates vault, cache, log, and source folders. |
| Safe write | `src/kb_builder/safe_write.py` | Overwrites/deletes only generated files. |
| MITRE cache | `src/kb_builder/cache.py` | Loads local/cache/remote MITRE STIX JSON. |
| MITRE parser | `src/kb_builder/sources/mitre.py` | Parses ATT&CK objects and relationships. |
| LOLBAS parser | `src/kb_builder/sources/lolbas.py` | Parses LOLBAS YAML from `.cache/lolbas/yml`. |
| GTFOBins parser | `src/kb_builder/sources/gtfobins.py` | Parses GTFOBins Markdown/YAML documents from `.cache/gtfobins/_gtfobins`. |
| PayloadsAllTheThings parser | `src/kb_builder/sources/payloadsallthethings.py` | Parses PayloadsAllTheThings Markdown topics from `.cache/payloadsallthethings`. |
| InternalAllTheThings parser | `src/kb_builder/sources/internalallthethings.py` | Parses InternalAllTheThings Markdown topics from `.cache/internalallthethings/docs`. |
| HackTricks parser | `src/kb_builder/sources/hacktricks.py` | Parses HackTricks Markdown topics from `.cache/hacktricks/src`. |
| Renderer | `src/kb_builder/render/markdown.py` | Renders Markdown and registers Jinja filters. |
| Build refs | `src/kb_builder/build_summary.py` | Writes `_build` datasource field references. |

## Current Sources

MITRE ATT&CK Enterprise generates:

- `kb/mitre/attack/tactics/`
- `kb/mitre/attack/techniques/`
- `kb/mitre/attack/mitigations/`
- `kb/mitre/attack/data-sources/`
- `kb/mitre/attack/software/`
- `kb/mitre/attack/indexes/`

LOLBAS generates:

- `kb/lolbas/tools/`
- `kb/indexes/lolbas.md`

GTFOBins generates:

- `kb/gtfobins/tools/`
- `kb/indexes/gtfobins.md`

PayloadsAllTheThings generates:

- `kb/payloads/`
- `kb/indexes/payloadsallthethings.md`

InternalAllTheThings generates:

- `kb/internal/`
- `kb/indexes/internalallthethings.md`

HackTricks generates:

- `kb/hacktricks/`
- `kb/indexes/hacktricks.md`

Build reference pages generate:

- `kb/_build/datasource-fields.md`
- `kb/_build/objects/<source>/<type>/example-*.md`

## Safety Model

Generated files contain:

```yaml
parsed_by: focuslocust
```

`clean` and `build` only delete or overwrite files containing that marker. Manual notes are skipped.
