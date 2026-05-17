---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# AI in Cybersecurity

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-ai-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/AI/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The best starting point to learn about AI is to understand how the main machine learning algorithms work. This will help you to understand how AI works, how to use it and how to attack it:

## Preserved Body

```markdown
## Main Machine Learning Algorithms

The best starting point to learn about AI is to understand how the main machine learning algorithms work. This will help you to understand how AI works, how to use it and how to attack it:


{{#ref}}
./AI-Supervised-Learning-Algorithms.md
{{#endref}}


{{#ref}}
./AI-Unsupervised-Learning-Algorithms.md
{{#endref}}


{{#ref}}
./AI-Reinforcement-Learning-Algorithms.md
{{#endref}}


{{#ref}}
./AI-Deep-Learning.md
{{#endref}}

### LLMs Architecture

In the following page you will find the basics of each component to build a basic LLM using transformers:


{{#ref}}
AI-llm-architecture/README.md
{{#endref}}

## AI Security

### AI Risk Frameworks

At this moment, the main 2 frameworks to assess the risks of AI systems are the OWASP ML Top 10 and the Google SAIF:


{{#ref}}
AI-Risk-Frameworks.md
{{#endref}}

### AI Prompts Security

LLMs have made the use of AI explode in the last years, but they are not perfect and can be tricked by adversarial prompts. This is a very important topic to understand how to use AI safely and how to attack it:


{{#ref}}
AI-Prompts.md
{{#endref}}

### AI Models RCE

It's very common to developers and companies to run models downloaded from the Internet, however just loading a model might be enough to execute arbitrary code on the system. This is a very important topic to understand how to use AI safely and how to attack it:


{{#ref}}
AI-Models-RCE.md
{{#endref}}

### AI Model Context Protocol

MCP (Model Context Protocol) is a protocol that allows AI agent clients to connect with external tools and data sources in a plug-and-play fashion. This enables complex workflows and interactions between AI models and external systems:


{{#ref}}
AI-MCP-Servers.md
{{#endref}} 

### AI-Assisted Fuzzing & Automated Vulnerability Discovery


{{#ref}}
AI-Assisted-Fuzzing-and-Vulnerability-Discovery.md
{{#endref}}
```

## Source Verification

[source record](../../sources/hacktricks/ai-in-cybersecurity.md)

## Evidence Excerpt

```text
_body: "# AI in Cybersecurity\n\n{{#include ../banners/hacktricks-training.md}}\n\n## Main Machine Learning Algorithms\n\n\
The best starting point to learn about AI is to understand how the main machine learning algorithms work. This will help\
\ you to understand how AI works, how to use it and how to attack it:\n\n\n{{#ref}}\n./AI-Supervised-Learning-Algorithms.md\n\
{{#endref}}\n\n\n{{#ref}}\n./AI-Unsupervised-Learning-Algorithms.md\n{{#endref}}\n\n\n{{#ref}}\n./AI-Reinforcement-Learning-Algorithms.md\n\
{{#endref}}\n\n\n{{#ref}}\n./AI-Deep-Learning.md\n{{#endref}}\n\n### LLMs Architecture\n\nIn the following page you will\
\ find the basics of each component to build a basic LLM using transformers:\n\n\n{{#ref}}\nAI-llm-architecture/README.md\n\
{{#endref}}\n\n## AI Security\n\n### AI Risk Frameworks\n\nAt this moment, the main 2 frameworks to assess the risks of\
\ AI systems are the OWASP ML Top 10 and the Google SAIF:\n\n\n{{#ref}}\nAI-Risk-Frameworks.md\n{{#endref}}\n\n### AI Prompts\
```
