Read AGENTS.md, README.md, and focuslocust-builder-stage-1.md first.

Write clear project documentation for this repository.

Audience:
- Me as the project owner
- A future developer extending the builder
- A security practitioner using the generated Obsidian vault

Documentation goals:
1. Explain what the project does.
2. Explain the completed MITRE stage-one scope, completed LOLBAS scope, completed GTFOBins scope, completed PayloadsAllTheThings scope, and completed InternalAllTheThings scope.
3. Explain what is intentionally not implemented yet.
4. Explain the folder structure.
5. Explain the generated file safety rule.
6. Explain the naming convention.
7. Explain how templates work.
8. Explain how to run, test, clean, and troubleshoot the project.
9. Explain how future sources like Sigma, Atomic, and other datasources could be added later without implementing them.

Constraints:
- Keep the docs practical and concise.
- Do not overhype the project.
- Do not describe features that are not implemented.
- Do not add SQLite, graph DB, AI, Dataview, or plugin-framework language.
- Use Markdown.
- Prefer examples over vague explanations.
- Keep all work inside the current repository.
- Add mermaidjs diagrams. 

Files to update or create:
- README.md
- docs/architecture.md
- docs/usage.md
- docs/templates.md
- docs/adding-a-source.md
- docs/troubleshooting.md

Done when:
- A new user can install dependencies, run tests, run doctor, and build the MITRE, LOLBAS, GTFOBins, PayloadsAllTheThings, and InternalAllTheThings vault.
- A developer can understand where parser, renderer, templates, cache, and safe-write logic live.
- The docs clearly state that only files with `parsed_by: focuslocust` may be overwritten.
- The docs clearly show the filename format, for example `T1003.002-security-account-manager.md`.
- The docs mention future sources as design notes only, not implemented features, while documenting LOLBAS, GTFOBins, PayloadsAllTheThings, and InternalAllTheThings as complete.
- Run a quick documentation review for consistency before finishing.
