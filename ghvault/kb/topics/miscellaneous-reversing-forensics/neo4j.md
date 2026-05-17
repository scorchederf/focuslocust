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

## Summary

This is a living document that captures notes related to anything and all neo4j and cypher queries.

## Preserved Body

````markdown
This is a living document that captures notes related to anything and all neo4j and cypher queries.

## List Databases

```
show databases 
```

![](<../_assets/image (732).png>)

## Create New Database

```graphql
create database spotless
```

![](<../_assets/image (731).png>)

## Switch Database

```
:use spotless
```

![](<../_assets/image (733).png>)

## Import Data from CSV and Define Relationships Between Nodes

### Sample Data

Below is a sample CSV file with 3 columns, that represents Windows authentication information between different endpoints (think lateral movement detection/investigation/threat hunting):

| Column                | Meaning                                                                       |
| --------------------- | ----------------------------------------------------------------------------- |
| `SourceComputer`      | A computer that successfully authenticated to a DestinationComputer           |
| `DestinationComputer` | A computer that SourceComputer authenticated to                               |
| `DestinationUserName` | A user name that was used to logon from SourceComputer to DestinationComputer |
```scala
"SourceComputer","DestinationComputer","DestinationUserName"
"WS01","WS02","administrator"
"WS01","WS03","administrator"
"WS02","WS03","administrator"
"WS03","WS04","administrator"
"WS04","WS05","administrator"
"WS05","WS06","administrator"
"WS06","WS07","administrator"
"WS07","DB01","administrator"
"DB01","FS05","administrator"
"FS05","DC01","da-james"
"WS01","WS04","billy"
"WS02","WS04","sally"
"WS03","WS02","fred"
"WS03","WS02","james"
"WS01","WS02","james"
```
The file needs to be saved to the `import` folder of your database folder. In my case, the path is C:\Users\User\AppData\Local\Neo4j\Relate\Data\dbmss\dbms-8320b8a8-e54d-4742-a432-c8014b5968ec\import\lateral-movement.csv
### Importing Nodes from CSV and Creating Relationships

```graphql
LOAD CSV WITH HEADERS FROM 'file:///lateral-movement.csv' AS line
MERGE (a:Computer {Computer:line.SourceComputer} )
MERGE (b:Computer {Computer:line.DestinationComputer} )
MERGE (a) -[:LOGGED_IN {loggedAs:line.DestinationUserName}]-> (b)
```

![](<../_assets/image (735).png>)

![](<../_assets/image (736).png>)

## Clean Database

```graphql
match (a) -[r] -> () delete a, r; match (a) delete a
```

## Match Nodes WHERE DestinationComputer Contains "WS"

```graphql
MATCH p=()-[r:LOGGED_IN]->(m:Computer) where m.Computer CONTAINS "WS" RETURN p LIMIT 25
```

![](<../_assets/image (737).png>)

## Match Nodes WHERE Relationship Contains "james"

```graphql
MATCH p=()-[r:LOGGED_IN]->() where (r.loggedAs contains "james") RETURN p LIMIT 25
```

![](<../_assets/image (741).png>)

## Match Nodes with 3 Hops Between Them

```graphql
MATCH p=()-[r:LOGGED_IN*3]->() RETURN p LIMIT 25
```

![](<../_assets/image (740).png>)
````

## Source Verification

[source record](../../sources/redteamingtactics/neo4j.md)

## Evidence Excerpt

```text
_asset_filenames:
- image (731).png
- image (732).png
- image (733).png
- image (735).png
- image (736).png
- image (737).png
- image (740).png
```
