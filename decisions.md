# Decisions

This file records baseline-level project decisions. Keep entries short and concrete.

## Baseline 01

`baseline/01/` is the first accepted generated vault snapshot for stage one.

It was copied from `vault/` after the MITRE ATT&CK procedure-example rendering was updated. At creation time, `vault/` and `baseline/01/` both contained 971 files.

## Stage-One Scope

Stage one is MITRE ATT&CK Enterprise only.

Included generated object types:

- tactics
- techniques
- sub-techniques
- mitigations
- data sources and data components as data-source notes
- tools as software notes under `kb/mitre/attack/software/`

Excluded generated object types:

- groups
- campaigns
- malware pages
- non-MITRE sources

Excluded implementation choices:

- SQLite
- graph databases
- AI enrichment
- Dataview
- DataviewJS
- plugin system

## Procedure Examples

Procedure examples are rendered from ATT&CK `uses` relationships only when:

- the target is a technique or sub-technique
- the source ATT&CK ID starts with `S`

This includes software/tool examples and malware examples, because ATT&CK uses `S...` IDs for both. It excludes groups (`G...`) and campaigns (`C...`).

Link behavior:

- If the source object exists in the generated link map, render the ID as a local Obsidian wikilink.
- If the source is malware and no local page exists, render the ID as an external MITRE ATT&CK link.
- Otherwise, keep the ID as plain text.

This avoids broken local links to pages the baseline does not generate.

## Generated-File Safety

Generated files must include:

```yaml
parsed_by: focuslocust
```

The builder may overwrite or delete only generated Markdown files containing that marker.

Manual notes without the marker must be preserved.

## Naming

Generated Markdown filenames use:

```text
<id>-<lowercase-kebab-slug>.md
```

Examples:

```text
T1003.002-security-account-manager.md
S0002-mimikatz.md
M1027-password-policies.md
```

## Commands

Run tests:

```bash
python3 -m pytest
```

Build:

```bash
python builder.py build --config config.yml
```

Create a future baseline:

```bash
mkdir -p baseline
cp -a vault baseline/02
```
