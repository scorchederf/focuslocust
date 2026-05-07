# Obsidian KB Builder

A simple Python tool for generating an Obsidian security knowledge base from structured security datasets.

Stage one supports:

- MITRE ATT&CK Enterprise STIX JSON
- Obsidian Markdown output
- deterministic filenames
- source-specific Jinja2 templates
- safe generated-file overwrite behaviour
- simple index pages

Future sources will include:

- LOLBAS / LOLBins
- GTFOBins
- Sigma
- Atomic Red Team
- PayloadsAllTheThings
- InternalAllTheThings / HackTricks-style Markdown repositories
- CSV / XLSX / JSON / YAML / Markdown / GitHub sources

## Non-goals for stage one

This project intentionally does **not** include:

- SQLite
- graph databases
- AI summaries
- Dataview
- DataviewJS
- plugin framework
- fuzzy matching
- complex dashboards

The stage-one pipeline is:

```text
MITRE STIX JSON
    -> parse
    -> normalise
    -> render Markdown
    -> generate indexes
```

## Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Check environment

```bash
python builder.py doctor --config config.yml
```

## Build the vault

```bash
python builder.py build --config config.yml
```

The generated vault is written to:

```text
./vault/
```

## Clean generated files

```bash
python builder.py clean --config config.yml
```

This deletes only Markdown files that contain:

```yaml
generated_by: focuslocust
```

Manual notes without that marker are preserved.

## Naming convention

Generated notes use:

```text
<canonical-id>-<lowercase-kebab-slug>.md
```

Example:

```text
T1003.002-security-account-manager.md
```

## Vault structure

Stage one generates content under:

```text
vault/
├── kb/
│   ├── mitre/
│   │   └── attack/
│   │       ├── tactics/
│   │       ├── techniques/
│   │       ├── mitigations/
│   │       ├── data-sources/
│   │       ├── software/
│   │       └── indexes/
│   └── indexes/
├── .cache/
└── .logs/
```

Future folders are reserved for:

```text
kb/tools/
kb/detections/
kb/tests/
kb/payloads/
ws/
```

## Generated-file safety

Generated Markdown files include:

```yaml
generated_by: focuslocust
```

The builder may only overwrite or delete files containing that marker.

If a target file already exists and does not contain that marker, the builder skips it and logs a warning.

## Templates

Each source has its own templates.

Stage one uses:

```text
templates/mitre/tactic.md.j2
templates/mitre/technique.md.j2
templates/mitre/mitigation.md.j2
templates/mitre/data-source.md.j2
templates/mitre/tool.md.j2
templates/mitre/index.md.j2
```

## Reference repo usage

The reference repository should be cloned beside this project, not inside it:

```bash
mkdir -p ../reference
git clone https://github.com/vincenzocaputo/obsidian-mitre-attack.git ../reference/obsidian-mitre-attack
```

Use it only as a behavioural/style reference. Do not modify it from this project.
