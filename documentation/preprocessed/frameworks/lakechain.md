---
title: AWS Lakechain
---
# AWS Lakechain
Project Lakechain is a framework based on the AWS Cloud Development Kit (CDK), allowing to express and deploy scalable document processing pipelines on AWS using infrastructure-as-code. It emphasizes on modularity and extensibility of pipelines, and provides 60+ ready to use components for prototyping complex processing pipelines that scale out of the box to millions of documents.
The Qdrant storage connector available with Lakechain enables uploading vector embeddings produced by other middlewares to a Qdrant collection.
You can find an end-to-end example usage of the Qdrant Lakechain connector here.
To use the Qdrant storage connector, you import it in your CDK stack, and connect it to a data source providing document embeddings.
> You need to specify a Qdrant API key to the connector, by specifying a reference to an AWS Secrets Manager secret containing the API key.
```typescript
import { QdrantStorageConnector } from '@project-lakechain/qdrant-storage-connector';
import { CacheStorage } from '@project-lakechain/core';
class Stack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string) {
    const cache = new CacheStorage(this, 'Cache');
    const qdrantApiKey = secrets.Secret.fromSecretNameV2(
      this,
      'QdrantApiKey',
      process.env.QDRANT_API_KEY_SECRET_NAME as string
    );
    const connector = new QdrantStorageConnector.Builder()
      .withScope(this)
      .withIdentifier('QdrantStorageConnector')
      .withCacheStorage(cache)
      .withSource(source) // 👈 Specify a data source
      .withApiKey(qdrantApiKey)
      .withCollectionName('{collection_name}')
      .withUrl('the linked resource
      .build();
  }
}
```
When the document being processed is a text document, you can choose to store the text of the document in the Qdrant payload. To do so, you can use the `withStoreText` and `withTextKey` options. If the document is not a text, this option is ignored.
```typescript
const connector = new QdrantStorageConnector.Builder()
  .withScope(this)
  .withIdentifier('QdrantStorageConnector')
  .withCacheStorage(cache)
  .withSource(source)
  .withApiKey(qdrantApiKey)
  .withCollectionName('{collection_name}')
  .withStoreText(true)
  .withTextKey('my-content')
  .withUrl('the linked resource
  .build();
```
Since Qdrant supports multiple vectors per point, you can use the `withVectorName` option to specify one. The connector defaults to unnamed (default) vector.
```typescript
const connector = new QdrantStorageConnector.Builder()
      .withScope(this)
      .withIdentifier('QdrantStorageConnector')
      .withCacheStorage(cache)
      .withSource(source)
      .withApiKey(qdrantApiKey)
      .withCollectionName('collection_name')
      .withVectorName('my-vector-name')
      .withUrl('the linked resource
      .build();
```
## Further Reading
 Introduction to Lakechain
 Lakechain Examples
