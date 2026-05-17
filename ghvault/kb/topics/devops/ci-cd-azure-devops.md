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

## Summary

The configuration files for azure pipelines are normally located in the root directory of the repository and called - azure-pipelines.yml\

## Preserved Body

````markdown
## Azure Pipelines

The configuration files for azure pipelines are normally located in the root directory of the repository and called - `azure-pipelines.yml`\
You can tell if the pipeline builds pull requests based on its trigger instructions. Look for `pr:` instruction:

```yaml
trigger:
  branches:
      include:
      - master
      - refs/tags/*
pr:
- master
```

## Secret Extractions

Extract secrets for these service connection:

* AzureRM
* GitHub
* AWS
* SonarQube
* SSH

```ps1
nord-stream.py devops ... --build-yaml test.yml --build-type ssh  
```

## References

* [Azure DevOps CICD Pipelines - Command Injection with Parameters, Variables and a discussion on Runner hijacking - Sana Oshika - May 1 2023](https://pulsesecurity.co.nz/advisories/Azure-Devops-Command-Injection)
````

## Source Verification

[source record](../../sources/internalallthethings/ci-cd-azure-devops.md)

## Evidence Excerpt

````text
_body: "# CI/CD - Azure DevOps\n\n## Azure Pipelines\n\nThe configuration files for azure pipelines are normally located in\
\ the root directory of the repository and called - `azure-pipelines.yml`\\\nYou can tell if the pipeline builds pull requests\
\ based on its trigger instructions. Look for `pr:` instruction:\n\n```yaml\ntrigger:\n  branches:\n      include:\n   \
\   - master\n      - refs/tags/*\npr:\n- master\n```\n\n## Secret Extractions\n\nExtract secrets for these service connection:\n\
\n* AzureRM\n* GitHub\n* AWS\n* SonarQube\n* SSH\n\n```ps1\nnord-stream.py devops ... --build-yaml test.yml --build-type\
\ ssh  \n```\n\n## References\n\n* [Azure DevOps CICD Pipelines - Command Injection with Parameters, Variables and a discussion\
\ on Runner hijacking - Sana Oshika - May 1 2023](https://pulsesecurity.co.nz/advisories/Azure-Devops-Command-Injection)"
_relative_path: devops/cicd-azure-devops.md
````
