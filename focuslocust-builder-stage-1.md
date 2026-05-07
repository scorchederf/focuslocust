# Codex Build Instructions — Obsidian Security Knowledge Base Builder

## Purpose

Build a simple, repeatable Python tool that generates an Obsidian security knowledge base from structured and semi-structured security datasets.

The first implementation stage is **MITRE ATT&CK only**.

Future stages will add:

- LOLBAS / LOLBins
- GTFOBins
- Sigma
- Atomic Red Team
- PayloadsAllTheThings
- InternalAllTheThings / HackTricks-style Markdown repositories
- CSV / XLSX / JSON / YAML / Markdown / GitHub data sources

The project should stay simple. Do not build a graph database, SQLite layer, AI layer, dashboard engine, plugin framework, or complex manifest system in stage one.

The immediate goal is:

```text
MITRE ATT&CK STIX JSON
    → parsed Python objects
    → Obsidian Markdown notes
    → wikilinks
    → simple indexes
    → safe repeatable rebuilds
```

---

# 1. Reference repository setup

The existing repository to use as a reference is:

```bash
https://github.com/vincenzocaputo/obsidian-mitre-attack.git
```

This repository should **not** become the new project directly.

Clone it into a separate subdirectory and use it as a reference implementation to verify behaviour, data handling, and general coding style.

## Required local directory layout

Create a new parent working directory:

```bash
mkdir obsidian-security-kb-workspace
cd obsidian-security-kb-workspace
```

Clone the reference repo into a dedicated reference directory:

```bash
mkdir reference
git clone https://github.com/vincenzocaputo/obsidian-mitre-attack.git reference/obsidian-mitre-attack
```

Create the new project separately:

```bash
mkdir focuslocust
cd focuslocust
git init
```

The final workspace should look like this:

```text
obsidian-security-kb-workspace/
├── reference/
│   └── obsidian-mitre-attack/
└── focuslocust/
```

## Reference repo inspection tasks

Before writing code, inspect the reference repository.

Read these files:

```text
reference/obsidian-mitre-attack/README.md
reference/obsidian-mitre-attack/run.py
reference/obsidian-mitre-attack/config.yml
reference/obsidian-mitre-attack/requirements.txt
reference/obsidian-mitre-attack/src/stix_parser.py
reference/obsidian-mitre-attack/src/markdown_generator.py
reference/obsidian-mitre-attack/src/models.py
reference/obsidian-mitre-attack/src/markdown_reader.py
reference/obsidian-mitre-attack/src/view.py
```

Use the reference repository to understand:

- how it retrieves or loads MITRE ATT&CK STIX data
- how it separates parser logic from Markdown generation
- how its CLI options are structured
- how it uses configuration
- how it writes Obsidian-compatible Markdown
- how it handles ATT&CK domains
- how it generates links between ATT&CK objects

## Important license boundary

The reference repository is GPL-3.0 licensed.

For this new project:

- Do **not** copy large blocks of code blindly.
- Do **not** vendor the reference source directly.
- Use it as an implementation reference and behavioural baseline.
- If code is copied or substantially derived, preserve the licence obligations.
- Prefer writing clean new code that follows the same simple style and architecture pattern.

The desired style is:

- simple Python
- small modules
- direct CLI
- YAML config
- clear parser/generator separation
- readable code over clever abstractions

---

# 2. New project goal

Build a new project called:

```text
focuslocust
```

The tool generates an Obsidian vault knowledge base from datasets.

Stage one only needs MITRE ATT&CK.

The tool must:

1. Read configuration from `config.yml`.
2. Download or read MITRE ATT&CK STIX JSON.
3. Cache the source JSON in `.cache/`.
4. Parse tactics, techniques, sub-techniques, mitigations, and data sources.
5. Generate Markdown files under `kb/`.
6. Generate simple index pages.
7. Use deterministic filenames.
8. Use Obsidian wikilinks.
9. Never overwrite human-written notes.
10. Only delete or overwrite files that contain the generated marker:

```yaml
parsed_by: focuslocust
```

---

# 3. Design decisions already made

These are fixed requirements.

## 3.1 Keep it simple

Do not build these in stage one:

```text
SQLite
graph database
AI summaries
plugin system
complex manifest
advanced dashboards
fuzzy matching
overlay system
manual/curated split
dataview
dataviewjs
```

Stage one is:

```text
parse → normalise → render Markdown → generate indexes
```

## 3.2 Use Python

Use Python 3.

Prefer the same general style as the reference repo:

- CLI entry point
- YAML config
- small source modules
- separate parser and Markdown renderer
- readable functions/classes

Acceptable dependencies:

```text
pyyaml
requests
jinja2
loguru
python-frontmatter optional
```

Keep dependencies minimal.

## 3.3 No Dataview

Generated Markdown must use normal Markdown and Obsidian wikilinks only.

No Dataview.

No DataviewJS.

## 3.4 Vault folder structure

Stage one output structure:

```text
vault/
├── kb/
│   ├── mitre/
│   │   ├── tactics/
│   │   ├── techniques/
│   │   ├── mitigations/
│   │   ├── data-sources/
│   │   └── indexes/
│   ├── tools/
│   │   ├── windows/
│   │   ├── linux/
│   │   ├── indexes/
│   │   ├── nmap.md
│   │   ├── ftp.md
│   │   ├── curl.md
│   │   ├── wget.md
│   │   ├── python.md
│   │   └── openssl.md
│   ├── detections/
│   │   ├── sigma/
│   │   └── indexes/
│   ├── tests/
│   │   ├── atomic/
│   │   └── indexes/
│   ├── payloads/
│   │   ├── web/
│   │   ├── methodology/
│   │   └── indexes/
│   └── indexes/
├── ws/
│   ├── dashboards/
│   └── maps/
├── .cache/
└── .logs/
```

For stage one, only these folders need real content:

```text
kb/mitre/tactics/
kb/mitre/techniques/
kb/mitre/mitigations/
kb/mitre/data-sources/
kb/mitre/indexes/
kb/indexes/
.cache/
.logs/
```

The other folders can be created empty or deferred.

## 3.5 Tool directory decision

There must eventually be a central tool directory.

Platform-specific tools:

```text
kb/tools/windows/certutil.exe.md
kb/tools/windows/powershell.exe.md
kb/tools/linux/grep.md
kb/tools/linux/awk.md
```

Multi-platform or generic tools go directly under `kb/tools/`.

Do **not** create a `cross-platform/` folder.

Correct:

```text
kb/tools/nmap.md
kb/tools/ftp.md
kb/tools/python.md
kb/tools/openssl.md
kb/tools/netcat.md
```

Incorrect:

```text
kb/tools/cross-platform/nmap.md
```

Stage one does not need to generate tool pages yet, but the folder decision must be reflected in the structure and README.

## 3.6 PayloadsAllTheThings decision

PayloadsAllTheThings must eventually live under:

```text
kb/payloads/
```

It must not be treated as a tool dataset.

It should eventually be ingested as topic/reference Markdown, not one payload per note.

Future structure:

```text
kb/payloads/web/sql-injection.md
kb/payloads/web/xss-injection.md
kb/payloads/web/command-injection.md
kb/payloads/web/ssrf.md
kb/payloads/methodology/reverse-shells.md
```

For stage one, document this future decision but do not implement PayloadsAllTheThings ingestion.

---

# 4. Naming convention

This is mandatory.

Use this format for generated object notes:

```text
<canonical-id>-<lowercase-kebab-slug>.md
```

Example:

```text
T1003.002-security-account-manager.md
```

## MITRE examples

```text
kb/mitre/techniques/T1059-command-and-scripting-interpreter.md
kb/mitre/techniques/T1059.001-powershell.md
kb/mitre/techniques/T1003.002-security-account-manager.md
kb/mitre/tactics/TA0006-credential-access.md
kb/mitre/mitigations/M1027-password-policies.md
```

## Slug rules

Implement one global slug function.

Rules:

- lowercase
- trim leading/trailing whitespace
- replace `&` with `and`
- replace spaces and unsafe characters with `-`
- collapse duplicate hyphens
- strip leading/trailing hyphens
- preserve dots so IDs and filenames like `T1003.002` and `certutil.exe` remain readable

Example implementation:

```python
import re

def slugify(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("&", "and")
    value = re.sub(r"[^a-z0-9.]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")
```

## Filename helper

Implement a helper:

```python
def make_id_slug_filename(canonical_id: str, name: str) -> str:
    return f"{canonical_id}-{slugify(name)}.md"
```

For:

```python
canonical_id = "T1003.002"
name = "Security Account Manager"
```

The output must be:

```text
T1003.002-security-account-manager.md
```

---

# 5. Templates

Each datasource must have its own templates.

Use this structure:

```text
templates/
├── mitre/
│   ├── tactic.md.j2
│   ├── technique.md.j2
│   ├── mitigation.md.j2
│   ├── data-source.md.j2
│   └── index.md.j2
├── tools/
│   ├── windows-tool.md.j2
│   ├── linux-tool.md.j2
│   ├── generic-tool.md.j2
│   └── index.md.j2
├── lolbas/
│   ├── tool.md.j2
│   └── index.md.j2
├── sigma/
│   ├── rule.md.j2
│   └── index.md.j2
├── atomic/
│   ├── test.md.j2
│   └── index.md.j2
├── payloadsallthethings/
│   ├── payload-topic.md.j2
│   ├── moved-reference.md.j2
│   └── index.md.j2
└── shared/
    ├── frontmatter.md.j2
    ├── references.md.j2
    └── links.md.j2
```

Stage one only needs the MITRE templates plus optional shared partials.

## Template selection rule

Each parsed object should have:

```yaml
source: mitre
type: technique
```

Template lookup:

```text
templates/<source>/<type>.md.j2
```

Examples:

```text
source=mitre type=technique    → templates/mitre/technique.md.j2
source=mitre type=tactic       → templates/mitre/tactic.md.j2
source=mitre type=mitigation   → templates/mitre/mitigation.md.j2
source=mitre type=data-source  → templates/mitre/data-source.md.j2
```

Fallback rule:

```text
1. Use templates/<source>/<type>.md.j2 if it exists.
2. Otherwise use templates/shared/<type>.md.j2 if it exists.
3. Otherwise fail with a clear error.
```

---

# 6. Generated file safety

The builder must never freely delete all Markdown files in `kb/` or `ws/`.

Before rebuilding, it may remove or overwrite only files that include:

```yaml
parsed_by: focuslocust
```

This must be checked by reading the file contents.

Simple safe rebuild algorithm:

```text
For each .md file under kb/ and ws/:
    read file as text
    if "parsed_by: focuslocust" appears in the file:
        delete it
    else:
        leave it alone
```

When writing a file:

```text
If target file does not exist:
    write it

If target file exists and contains "parsed_by: focuslocust":
    overwrite it

If target file exists and does not contain "parsed_by: focuslocust":
    skip it and log a warning
```

Log example:

```text
Skipped kb/mitre/techniques/T1059-command-and-scripting-interpreter.md because it does not contain generated_by marker
```

This is enough for stage one. Do not build a manifest system yet.

---

# 7. Config file

Create `config.yml`:

```yaml
vault_path: "./vault"

logging:
  verbose: false
  log_dir: ".logs"

cache:
  dir: ".cache"
  refresh: false

sources:
  mitre:
    enabled: true
    domain: "enterprise-attack"
    url: "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json"
    local_path: null
    include_tactics: true
    include_techniques: true
    include_subtechniques: true
    include_mitigations: true
    include_data_sources: true
    include_groups: false
    include_software: false
    include_malware: false

rendering:
  use_full_path_wikilinks: true
  alias_wikilinks: true
  title_in_body: false
  generated_marker: "focuslocust"

naming:
  style: "id-slug"
  lowercase: true
  separator: "-"
  preserve_dots: true
```

Stage one must respect:

- `vault_path`
- `cache.dir`
- `cache.refresh`
- `sources.mitre.enabled`
- `sources.mitre.domain`
- `sources.mitre.url`
- `sources.mitre.local_path`
- MITRE include flags
- `logging.verbose`
- `rendering.use_full_path_wikilinks`
- `rendering.alias_wikilinks`

---

# 8. CLI requirements

Create a CLI entry point.

Acceptable simple form:

```bash
python builder.py build
```

Also support:

```bash
python builder.py build --config config.yml
python builder.py build --vault ./vault
python builder.py clean
python builder.py doctor
```

Minimum commands:

## `build`

Runs the full build.

```bash
python builder.py build --config config.yml
```

Steps:

1. Load config.
2. Create required directories.
3. Configure logging.
4. Clear previously generated Markdown files only.
5. Fetch/load MITRE STIX JSON.
6. Parse MITRE objects.
7. Build internal link maps.
8. Render Markdown pages.
9. Render index pages.
10. Write build summary log.

## `clean`

Deletes generated Markdown files only.

```bash
python builder.py clean --config config.yml
```

Do not delete `.cache/`.

## `doctor`

Checks the environment.

```bash
python builder.py doctor --config config.yml
```

Should verify:

- Python version
- config file exists
- vault path is writable or can be created
- templates exist
- cache directory exists or can be created
- MITRE source URL or local file is configured

---

# 9. Project structure to create

Use this structure:

```text
focuslocust/
├── README.md
├── config.yml
├── requirements.txt
├── builder.py
├── src/
│   └── kb_builder/
│       ├── __init__.py
│       ├── config.py
│       ├── logging_setup.py
│       ├── paths.py
│       ├── naming.py
│       ├── safe_write.py
│       ├── cache.py
│       ├── models.py
│       ├── sources/
│       │   ├── __init__.py
│       │   └── mitre.py
│       └── render/
│           ├── __init__.py
│           ├── markdown.py
│           └── links.py
├── templates/
│   ├── mitre/
│   │   ├── tactic.md.j2
│   │   ├── technique.md.j2
│   │   ├── mitigation.md.j2
│   │   ├── data-source.md.j2
│   │   └── index.md.j2
│   └── shared/
│       ├── frontmatter.md.j2
│       ├── references.md.j2
│       └── links.md.j2
└── tests/
    ├── test_naming.py
    ├── test_safe_write.py
    └── test_mitre_parser.py
```

Keep this simple. Do not introduce packaging complexity unless required.

---

# 10. Internal models

Use dataclasses.

Do not over-engineer.

Example:

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass
class KBObject:
    id: str
    source: str
    type: str
    name: str
    description: str = ""
    path: str = ""
    url: str = ""
    aliases: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)
```

For MITRE, add fields if useful:

```python
@dataclass
class MitreObject(KBObject):
    tactics: list[str] = field(default_factory=list)
    platforms: list[str] = field(default_factory=list)
    data_sources: list[str] = field(default_factory=list)
    mitigations: list[str] = field(default_factory=list)
    external_references: list[dict[str, str]] = field(default_factory=list)
```

Avoid Pydantic in stage one unless there is a strong reason.

---

# 11. MITRE parser requirements

The parser must read MITRE ATT&CK STIX 2.1 JSON.

It must support:

- `attack-pattern` as techniques/sub-techniques
- `x-mitre-tactic` as tactics
- `course-of-action` as mitigations
- `x-mitre-data-source` as data sources
- relationships between techniques and tactics
- relationships between mitigations and techniques where present
- external references, especially ATT&CK IDs and URLs

## Required functions

Create:

```python
class MitreSource:
    def __init__(self, config: dict): ...

    def load(self) -> dict: ...
    def parse(self) -> list[KBObject]: ...
```

Or similar.

## External ATT&CK ID extraction

MITRE STIX objects include external references.

Find the external reference where:

```text
source_name == "mitre-attack"
```

Extract:

```text
external_id
url
```

Examples:

```text
T1059
T1003.002
TA0006
M1027
```

If no ATT&CK external ID exists, skip the object or generate a stable fallback ID and log a warning.

For stage one, prefer skipping unsupported objects rather than generating bad pages.

## Revoked/deprecated objects

Skip revoked or deprecated objects by default.

If STIX object contains:

```json
"x_mitre_deprecated": true
```

or:

```json
"revoked": true
```

do not generate a note.

Log skipped counts.

---

# 12. MITRE output paths

Required output paths:

## Tactics

```text
kb/mitre/tactics/<TA-id>-<slug>.md
```

Example:

```text
kb/mitre/tactics/TA0006-credential-access.md
```

## Techniques and sub-techniques

Both techniques and sub-techniques go under:

```text
kb/mitre/techniques/
```

Examples:

```text
kb/mitre/techniques/T1059-command-and-scripting-interpreter.md
kb/mitre/techniques/T1059.001-powershell.md
kb/mitre/techniques/T1003.002-security-account-manager.md
```

Do not create a separate `subtechniques/` directory in stage one.

## Mitigations

```text
kb/mitre/mitigations/<M-id>-<slug>.md
```

Example:

```text
kb/mitre/mitigations/M1027-password-policies.md
```

## Data sources

```text
kb/mitre/data-sources/<slug>.md
```

If the data source has a usable MITRE ID in the dataset, use:

```text
<id>-<slug>.md
```

Otherwise use:

```text
<slug>.md
```

---

# 13. Wikilink requirements

Generate Obsidian wikilinks.

Prefer full-path links to avoid ambiguity.

Example:

```markdown
[[kb/mitre/techniques/T1003.002-security-account-manager|T1003.002 - Security Account Manager]]
```

If `use_full_path_wikilinks: false`, use:

```markdown
[[T1003.002-security-account-manager|T1003.002 - Security Account Manager]]
```

## Link helper

Implement a helper:

```python
def wikilink(path_without_md: str, alias: str | None = None) -> str:
    if alias:
        return f"[[{path_without_md}|{alias}]]"
    return f"[[{path_without_md}]]"
```

Do not include `.md` in wikilinks.

---

# 14. MITRE technique page template

Create `templates/mitre/technique.md.j2`.

It must produce this shape:

```markdown
---
parsed_by: focuslocust
source: mitre
type: {{ obj.type }}
id: {{ obj.id }}
name: {{ obj.name }}
---

## Summary

{{ obj.description }}

{% if obj.tactics %}
## Tactics

{% for tactic in obj.tactics %}
- {{ tactic }}
{% endfor %}
{% endif %}

{% if obj.platforms %}
## Platforms

{% for platform in obj.platforms %}
- {{ platform }}
{% endfor %}
{% endif %}

{% if obj.data_sources %}
## Data sources

{% for data_source in obj.data_sources %}
- {{ data_source }}
{% endfor %}
{% endif %}

{% if obj.mitigations %}
## Mitigations

{% for mitigation in obj.mitigations %}
- {{ mitigation }}
{% endfor %}
{% endif %}

{% if obj.links %}
## Links

{% for link in obj.links %}
- {{ link }}
{% endfor %}
{% endif %}

{% if obj.external_references %}
## References

{% for ref in obj.external_references %}
- [{{ ref.source_name }}]({{ ref.url }})
{% endfor %}
{% endif %}
```

Do not repeat the page title as a top-level `# Heading`.

The filename already acts as the Obsidian title.

---

# 15. MITRE tactic template

Create `templates/mitre/tactic.md.j2`.

Must include:

- frontmatter
- summary
- related techniques
- references

Example structure:

```markdown
---
parsed_by: focuslocust
source: mitre
type: tactic
id: {{ obj.id }}
name: {{ obj.name }}
---

## Summary

{{ obj.description }}

{% if obj.links %}
## Techniques

{% for link in obj.links %}
- {{ link }}
{% endfor %}
{% endif %}

{% if obj.external_references %}
## References

{% for ref in obj.external_references %}
- [{{ ref.source_name }}]({{ ref.url }})
{% endfor %}
{% endif %}
```

---

# 16. MITRE mitigation template

Create `templates/mitre/mitigation.md.j2`.

Must include:

- frontmatter
- summary
- related techniques if available
- references

---

# 17. MITRE data source template

Create `templates/mitre/data-source.md.j2`.

Must include:

- frontmatter
- summary
- related techniques if available
- references

---

# 18. Index generation

Generate simple Markdown indexes.

Required index files:

```text
kb/mitre/indexes/all-tactics.md
kb/mitre/indexes/all-techniques.md
kb/mitre/indexes/all-mitigations.md
kb/mitre/indexes/all-data-sources.md
kb/mitre/indexes/by-tactic.md
kb/mitre/indexes/by-platform.md
kb/indexes/mitre.md
```

Every generated index must include frontmatter:

```yaml
---
parsed_by: focuslocust
source: mitre
type: index
---
```

## `all-techniques.md`

Sort by ATT&CK ID.

Example:

```markdown
---
parsed_by: focuslocust
source: mitre
type: index
---

## Techniques

- [[kb/mitre/techniques/T1003-os-credential-dumping|T1003 - OS Credential Dumping]]
- [[kb/mitre/techniques/T1003.002-security-account-manager|T1003.002 - Security Account Manager]]
```

## `by-tactic.md`

Group techniques under tactic headings.

Example:

```markdown
## Credential Access

- [[kb/mitre/techniques/T1003-os-credential-dumping|T1003 - OS Credential Dumping]]
- [[kb/mitre/techniques/T1003.002-security-account-manager|T1003.002 - Security Account Manager]]
```

## `by-platform.md`

Group techniques by platform.

Example:

```markdown
## Windows

- [[kb/mitre/techniques/T1003.002-security-account-manager|T1003.002 - Security Account Manager]]
```

---

# 19. Cache behaviour

The MITRE source JSON must be cached in:

```text
.cache/mitre/enterprise-attack.json
```

If `cache.refresh: false` and the cache file exists, use the cached file.

If `cache.refresh: true`, fetch again and overwrite the cache.

If `sources.mitre.local_path` is set, use that file instead of downloading.

Do not fetch source data repeatedly when a cache exists.

---

# 20. Logging

Use `loguru` or Python logging.

Create logs under:

```text
.logs/
```

Log file name:

```text
focuslocust.log
```

Logs must include timestamps.

Log at least:

- config loaded
- vault path
- cache path
- source loaded from cache/local/download
- number of STIX objects loaded
- number of tactics parsed
- number of techniques parsed
- number of mitigations parsed
- number of data sources parsed
- number of files written
- number of generated files deleted
- number of manual files skipped
- build completed

Support verbose console output with:

```bash
python builder.py build --verbose
```

or from config:

```yaml
logging:
  verbose: true
```

---

# 21. README requirements

Write a clear `README.md`.

It must explain:

1. What the project does.
2. What it does not do yet.
3. How to install dependencies.
4. How to run the first MITRE build.
5. How cache works.
6. How generated file safety works.
7. The naming convention.
8. The vault structure.
9. How templates work.
10. How future data sources will be added.

README should include:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python builder.py doctor
python builder.py build --config config.yml
```

Also explain that generated files contain:

```yaml
parsed_by: focuslocust
```

and that manual files without that marker are not overwritten.

---

# 22. Tests

Add basic tests.

At minimum:

## `test_naming.py`

Test:

```text
"Security Account Manager" → "security-account-manager"
"Command and Scripting Interpreter" → "command-and-scripting-interpreter"
"T1003.002" preserved in filename
"certutil.exe" preserves dot
```

## `test_safe_write.py`

Test:

- generated file can be overwritten
- manual file cannot be overwritten
- generated files are detected by marker
- manual files are skipped

## `test_mitre_parser.py`

Use small fixture STIX snippets.

Test:

- external ATT&CK ID extraction
- revoked object skipped
- deprecated object skipped
- technique object parsed
- tactic object parsed
- mitigation object parsed

---

# 23. Acceptance criteria for stage one

Stage one is complete when all of the following are true.

## Functional acceptance

Running:

```bash
python builder.py build --config config.yml
```

creates a vault structure like:

```text
vault/
├── kb/
│   ├── mitre/
│   │   ├── tactics/
│   │   ├── techniques/
│   │   ├── mitigations/
│   │   ├── data-sources/
│   │   └── indexes/
│   └── indexes/
├── .cache/
└── .logs/
```

It generates files including:

```text
kb/mitre/techniques/T1003.002-security-account-manager.md
kb/mitre/indexes/all-techniques.md
kb/mitre/indexes/by-tactic.md
kb/indexes/mitre.md
```

## Safety acceptance

If a user manually creates:

```text
vault/kb/mitre/techniques/T1003.002-security-account-manager.md
```

without the generated marker, the builder must skip it and log a warning.

## Naming acceptance

The file for ATT&CK sub-technique `T1003.002 Security Account Manager` must be:

```text
T1003.002-security-account-manager.md
```

Not:

```text
Security Account Manager.md
T1003_002_Security_Account_Manager.md
T1003.002 - Security Account Manager.md
```

## Template acceptance

MITRE technique pages must be generated using:

```text
templates/mitre/technique.md.j2
```

Tactic pages must use:

```text
templates/mitre/tactic.md.j2
```

## Link acceptance

Generated pages must contain Obsidian wikilinks.

Example:

```markdown
[[kb/mitre/techniques/T1003.002-security-account-manager|T1003.002 - Security Account Manager]]
```

## Simplicity acceptance

No SQLite.

No graph DB.

No AI.

No Dataview.

No DataviewJS.

No complex plugin framework.

---

# 24. Future source design notes

Do not implement these in stage one, but structure the project so they are easy to add.

## LOLBAS

LOLBAS should generate central tool pages:

```text
kb/tools/windows/certutil.exe.md
kb/tools/windows/mshta.exe.md
```

It should not generate:

```text
kb/lolbas/certutil.exe.md
```

LOLBAS pages should use:

```text
templates/lolbas/tool.md.j2
```

## Sigma

Sigma should generate detection pages:

```text
kb/detections/sigma/<sigma-id-or-rule-slug>.md
```

Sigma pages should link to:

- ATT&CK techniques
- central tool pages
- log sources

Sigma pages should use:

```text
templates/sigma/rule.md.j2
```

## Atomic Red Team

Atomic should generate test pages:

```text
kb/tests/atomic/T1059.001-powershell-test-001.md
```

Atomic pages should link to:

- ATT&CK techniques
- central tool pages
- Sigma detections where obvious

Atomic pages should use:

```text
templates/atomic/test.md.j2
```

## PayloadsAllTheThings

PayloadsAllTheThings should generate topic/reference pages under:

```text
kb/payloads/
```

Examples:

```text
kb/payloads/web/sql-injection.md
kb/payloads/web/xss-injection.md
kb/payloads/web/command-injection.md
kb/payloads/methodology/reverse-shells.md
```

It should:

- preserve useful Markdown structure
- add frontmatter
- add source reference
- link obvious tool names to `kb/tools/`
- link obvious ATT&CK IDs if present
- not split every payload into its own note

PayloadsAllTheThings pages should use:

```text
templates/payloadsallthethings/payload-topic.md.j2
```

---

# 25. Suggested implementation sequence for Codex

Use this sequence.

## Step 1 — Scaffold

Create files and folders:

```text
builder.py
config.yml
requirements.txt
README.md
src/kb_builder/
templates/mitre/
tests/
```

## Step 2 — Config and logging

Implement:

```text
config.py
logging_setup.py
paths.py
```

Verify `doctor` works.

## Step 3 — Naming

Implement:

```text
naming.py
```

Add tests.

Ensure:

```text
T1003.002 + Security Account Manager → T1003.002-security-account-manager.md
```

## Step 4 — Safe writing

Implement:

```text
safe_write.py
```

Add tests.

Ensure manual files are skipped.

## Step 5 — Cache

Implement:

```text
cache.py
```

Support local path, cached file, and download.

## Step 6 — MITRE parser

Implement:

```text
sources/mitre.py
```

Parse:

- tactics
- techniques
- sub-techniques
- mitigations
- data sources

Skip revoked/deprecated.

## Step 7 — Link map

Build a mapping:

```text
ATT&CK ID → output path without .md
ATT&CK ID → display name
```

Use this to generate full-path wikilinks.

## Step 8 — Markdown renderer

Implement:

```text
render/markdown.py
render/links.py
```

Use Jinja2.

## Step 9 — MITRE indexes

Generate required indexes.

## Step 10 — End-to-end build

Run:

```bash
python builder.py build --config config.yml
```

Verify output manually in Obsidian.

---

# 26. Non-goals for first build

Do not implement:

```text
LOLBAS parsing
Sigma parsing
Atomic parsing
PayloadsAllTheThings parsing
tool alias extraction
advanced dashboards
coverage scoring
SQLite
graph database
AI
Dataview
```

Only create enough project structure so those sources can be added later.

---

# 27. Final summary for Codex

Build a simple Python-based Obsidian KB generator.

Use the existing `obsidian-mitre-attack` repository as a reference by cloning it into:

```text
reference/obsidian-mitre-attack/
```

Build the new project separately in:

```text
focuslocust/
```

Stage one must generate MITRE ATT&CK Markdown pages from STIX JSON.

The output must use:

```text
kb/mitre/tactics/
kb/mitre/techniques/
kb/mitre/mitigations/
kb/mitre/data-sources/
kb/mitre/indexes/
```

The required filename format is:

```text
<id>-<lowercase-kebab-slug>.md
```

Example:

```text
T1003.002-security-account-manager.md
```

Use source-specific templates:

```text
templates/mitre/technique.md.j2
templates/mitre/tactic.md.j2
templates/mitre/mitigation.md.j2
templates/mitre/data-source.md.j2
```

Generated files must contain:

```yaml
parsed_by: focuslocust
```

Only files with that marker may be overwritten or deleted.

Keep the build simple, deterministic, and repeatable.
