---
title: Mastra
---
# Mastra
Mastra is a Typescript framework to build AI applications and features quickly. It gives you the set of primitives you need: workflows, agents, RAG, integrations, syncs and evals. You can run Mastra on your local machine, or deploy to a serverless cloud.
Qdrant is available as a vector store in Mastra node to augment application with retrieval capabilities.
## Setup
```bash
npm install @mastra/core
```
## Usage
```typescript
import { QdrantVector } from "@mastra/rag";
const qdrant = new QdrantVector({
  url: "the linked resource
  apiKey: "",
  https: true
});
```
## Constructor Options
`url` — `string` — REST URL of the Qdrant instance. Eg.
`apiKey` — `string` — Optional Qdrant API key
`https` — `boolean` — Whether to use TLS when setting up the connection. Recommended.
## Methods
### `createIndex()`
`indexName` — `string` — Name of the index to create
`dimension` — `number` — Vector dimension size
`metric` — `string` — Distance metric for similarity search — `cosine`
### `upsert()`
`vectors` — `number[][]` — Array of embedding vectors
`metadata` — `Record[]` — Metadata for each vector (optional)
`namespace` — `string` — Optional namespace for organization
### `query()`
`vector` — `number[]` — Query vector to find similar vectors
`topK` — `number` — Number of results to return (optional) — `10`
`filter` — `Record` — Metadata filters for the query (optional)
### `listIndexes()`
Returns an array of index names as strings.
### `describeIndex()`
`indexName` — `string` — Name of the index to describe
#### Returns
```typescript
interface IndexStats {
  dimension: number;
  count: number;
  metric: "cosine" | "euclidean" | "dotproduct";
}
```
### `deleteIndex()`
`indexName` — `string` — Name of the index to delete
## Response Types
Query results are returned in this format:
```typescript
interface QueryResult {
  id: string;
  score: number;
  metadata: Record;
}
```
## Further Reading
 Mastra Examples
 Mastra Documentation
