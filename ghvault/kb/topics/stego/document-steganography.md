---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Document Steganography

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-stego-documents-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/stego/documents/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Documents are often just containers:

## Preserved Body

````markdown
Documents are often just containers:

- PDF (embedded files, streams)
- Office OOXML (`.docx/.xlsx/.pptx` are ZIPs)
- RTF / OLE legacy formats

## PDF

### Technique

PDF is a structured container with objects, streams, and optional embedded files. In CTFs you often need to:

- Extract embedded attachments
- Decompress/flatten object streams so you can search content
- Identify hidden objects (JS, embedded images, odd streams)

### Quick checks

```bash
pdfinfo file.pdf
pdfdetach -list file.pdf
pdfdetach -saveall file.pdf
qpdf --qdf --object-streams=disable file.pdf out.pdf
```

Then search inside `out.pdf` for suspicious objects/strings.

## Office OOXML

### Technique

Treat OOXML as a ZIP + XML relationship graph; payloads often hide in media, relationships, or odd custom parts.

OOXML files are ZIP containers. That means:

- The document is a directory tree of XML and assets.
- The `_rels/` relationship files can point to external resources or hidden parts.
- Embedded data frequently lives in `word/media/`, custom XML parts, or unusual relationships.

### Quick checks

```bash
7z l file.docx
7z x file.docx -oout
```

Then inspect:

- `word/document.xml`
- `word/_rels/` for external relationships
- embedded media in `word/media/`
````

## Source Verification

[source record](../../sources/hacktricks/document-steganography.md)

## Evidence Excerpt

```text
_body: '# Document Steganography
{{#include ../../banners/hacktricks-training.md}}
Documents are often just containers:
- PDF (embedded files, streams)
- Office OOXML (`.docx/.xlsx/.pptx` are ZIPs)
- RTF / OLE legacy formats
## PDF
### Technique
```
