---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# CI/CD - Azure DevOps

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-cicd-azure-devops` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-azure-devops.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CI/CD - Azure DevOps](../../topics/devops/ci-cd-azure-devops.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-devops-cicd-azure-devops |
| name | CI/CD - Azure DevOps |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/devops/cicd-azure-devops.md |

## Preserved Source Material

````yaml
_body: "# CI/CD - Azure DevOps\n\n## Azure Pipelines\n\nThe configuration files for azure pipelines are normally located in\
  \ the root directory of the repository and called - `azure-pipelines.yml`\\\nYou can tell if the pipeline builds pull requests\
  \ based on its trigger instructions. Look for `pr:` instruction:\n\n```yaml\ntrigger:\n  branches:\n      include:\n   \
  \   - master\n      - refs/tags/*\npr:\n- master\n```\n\n## Secret Extractions\n\nExtract secrets for these service connection:\n\
  \n* AzureRM\n* GitHub\n* AWS\n* SonarQube\n* SSH\n\n```ps1\nnord-stream.py devops ... --build-yaml test.yml --build-type\
  \ ssh  \n```\n\n## References\n\n* [Azure DevOps CICD Pipelines - Command Injection with Parameters, Variables and a discussion\
  \ on Runner hijacking - Sana Oshika - May 1 2023](https://pulsesecurity.co.nz/advisories/Azure-Devops-Command-Injection)"
_relative_path: devops/cicd-azure-devops.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/cicd-azure-devops.md
````
