# Agent instructions

## Scope

Work only inside this repository.

Do not modify files outside the current repository root.

Do not modify the reference repository.

Do not use parent-directory paths such as `../`.

Do not write to absolute paths unless they are inside this repository.

## Permissions

Do not ask for permission to access files outside this repository.

If an action requires access outside the repository, do not perform it.

## Build constraints

- Python only.
- Keep the implementation simple.
- Stage one is MITRE ATT&CK only.
- No SQLite.
- No graph database.
- No AI layer.
- No Dataview.
- No DataviewJS.
- Use source-specific templates.
- Use the required naming convention: `<id>-<lowercase-kebab-slug>.md`.
- Only overwrite/delete generated files containing `generated_by: focuslocust`.
