# Codex quick-start prompt

Use this prompt after opening Codex from the project root.

```text
Read AGENTS.md and README.md first.

Implement and improve this project only within the current repository.

Do not access parent directories.
Do not request elevated permissions.
Do not use the network unless explicitly required.
Do not modify the reference repository.

Stage one is MITRE ATT&CK only.

Keep the implementation simple:
- Python
- YAML config
- Jinja2 templates
- source-specific templates
- safe generated-file overwrites only
- deterministic filenames like T1003.002-security-account-manager.md
- Obsidian wikilinks

Do not add SQLite, graph databases, AI, Dataview, DataviewJS, plugin systems, or future source ingestion yet.

Run the tests and fix any failures.
```
