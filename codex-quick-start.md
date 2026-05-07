# Codex quick-start prompt

Use this prompt after opening Codex from the project root.

```text
Read AGENTS.md and README.md first.

Implement and improve this project only within the current repository.

Do not access parent directories.
Any network access must be requested. 
Do not modify originalgithub/.
Do not modify baseline snapshots unless explicitly asked.

Stage one MITRE ATT&CK is complete.
LOLBAS / LOLBins is complete.

Keep the implementation simple:
- Python
- YAML config
- Jinja2 templates
- source-specific templates
- safe generated-file overwrites only
- deterministic filenames like T1003.002-security-account-manager.md
- Obsidian wikilinks

Do not add SQLite, graph databases, AI, Dataview, DataviewJS, plugin systems, generated group pages, campaign pages, malware pages, or new future source ingestion without an explicit task.

Current procedure-example rules:
- Include only ATT&CK `uses` relationships where the target is a technique or sub-technique and the source ATT&CK ID starts with `S`.
- This includes tools and malware because both use `S...` ATT&CK IDs.
- Exclude groups and campaigns from Procedure Examples.
- Use local wikilinks only when the referenced object exists in the generated link map.
- If the source is malware and no local page exists, link the ID to the external MITRE ATT&CK URL.
- Leave non-local, non-malware IDs as plain text.

The current accepted generated-vault snapshot is baseline/01.

Run the tests and fix any failures.
Use `python3 -m pytest`.
Use `python3 builder.py build --config config.yml` to build the vault.
```
