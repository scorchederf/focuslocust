---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Neo4j

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-neo4j` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/neo4j.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Neo4j](../../topics/miscellaneous-reversing-forensics/neo4j.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-neo4j |
| name | Neo4j |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/neo4j.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (731).png
- image (732).png
- image (733).png
- image (735).png
- image (736).png
- image (737).png
- image (740).png
- image (741).png
_body: "# Neo4j\n\nThis is a living document that captures notes related to anything and all neo4j and cypher queries.\n\n\
  ## List Databases\n\n```\nshow databases \n```\n\n![](<../.gitbook/assets/image (732).png>)\n\n## Create New Database\n\n\
  ```graphql\ncreate database spotless\n```\n\n![](<../.gitbook/assets/image (731).png>)\n\n## Switch Database\n\n```\n:use\
  \ spotless\n```\n\n![](<../.gitbook/assets/image (733).png>)\n\n## Import Data from CSV and Define Relationships Between\
  \ Nodes\n\n### Sample Data\n\nBelow is a sample CSV file with 3 columns, that represents Windows authentication information\
  \ between different endpoints (think lateral movement detection/investigation/threat hunting):\n\n| Column             \
  \   | Meaning                                                                       |\n| --------------------- | -----------------------------------------------------------------------------\
  \ |\n| `SourceComputer`      | A computer that successfully authenticated to a DestinationComputer           |\n| `DestinationComputer`\
  \ | A computer that SourceComputer authenticated to                               |\n| `DestinationUserName` | A user name\
  \ that was used to logon from SourceComputer to DestinationComputer |\n\n{% code title=\"lateral-movement.csv\" %}\n```scala\n\
  \"SourceComputer\",\"DestinationComputer\",\"DestinationUserName\"\n\"WS01\",\"WS02\",\"administrator\"\n\"WS01\",\"WS03\"\
  ,\"administrator\"\n\"WS02\",\"WS03\",\"administrator\"\n\"WS03\",\"WS04\",\"administrator\"\n\"WS04\",\"WS05\",\"administrator\"\
  \n\"WS05\",\"WS06\",\"administrator\"\n\"WS06\",\"WS07\",\"administrator\"\n\"WS07\",\"DB01\",\"administrator\"\n\"DB01\"\
  ,\"FS05\",\"administrator\"\n\"FS05\",\"DC01\",\"da-james\"\n\"WS01\",\"WS04\",\"billy\"\n\"WS02\",\"WS04\",\"sally\"\n\"\
  WS03\",\"WS02\",\"fred\"\n\"WS03\",\"WS02\",\"james\"\n\"WS01\",\"WS02\",\"james\"\n```\n{% endcode %}\n\n{% hint style=\"\
  info\" %}\nThe file needs to be saved to the `import` folder of your database folder. In my case, the path is C:\\Users\\\
  User\\AppData\\Local\\Neo4j\\Relate\\Data\\dbmss\\dbms-8320b8a8-e54d-4742-a432-c8014b5968ec\\import\\lateral-movement.csv\n\
  {% endhint %}\n\n### Importing Nodes from CSV and Creating Relationships\n\n```graphql\nLOAD CSV WITH HEADERS FROM 'file:///lateral-movement.csv'\
  \ AS line\nMERGE (a:Computer {Computer:line.SourceComputer} )\nMERGE (b:Computer {Computer:line.DestinationComputer} )\n\
  MERGE (a) -[:LOGGED_IN {loggedAs:line.DestinationUserName}]-> (b)\n```\n\n![](<../.gitbook/assets/image (735).png>)\n\n\
  ![](<../.gitbook/assets/image (736).png>)\n\n## Clean Database\n\n```graphql\nmatch (a) -[r] -> () delete a, r; match (a)\
  \ delete a\n```\n\n## Match Nodes WHERE DestinationComputer Contains \"WS\"\n\n```graphql\nMATCH p=()-[r:LOGGED_IN]->(m:Computer)\
  \ where m.Computer CONTAINS \"WS\" RETURN p LIMIT 25\n```\n\n![](<../.gitbook/assets/image (737).png>)\n\n## Match Nodes\
  \ WHERE Relationship Contains \"james\"\n\n```graphql\nMATCH p=()-[r:LOGGED_IN]->() where (r.loggedAs contains \"james\"\
  ) RETURN p LIMIT 25\n```\n\n![](<../.gitbook/assets/image (741).png>)\n\n## Match Nodes with 3 Hops Between Them\n\n```graphql\n\
  MATCH p=()-[r:LOGGED_IN*3]->() RETURN p LIMIT 25\n```\n\n![](<../.gitbook/assets/image (740).png>)"
_relative_path: miscellaneous-reversing-forensics/neo4j.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/neo4j.md
````
