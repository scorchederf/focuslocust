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
- Stage one MITRE ATT&CK is complete.
- LOLBAS / LOLBins is complete and uses source-specific output under `kb/lolbas/`.
- No SQLite.
- No graph database.
- No AI layer.
- No Dataview.
- No DataviewJS.
- Use source-specific templates.
- Use the required naming convention: `<id>-<lowercase-kebab-slug>.md`.
- Only overwrite/delete generated files containing `parsed_by: focuslocust`.
