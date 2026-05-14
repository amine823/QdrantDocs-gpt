Creates the `books` collection configured with a sparse vector `title-bm25` using the IDF modifier for BM25 queries.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.CreateCollectionAsync(
    collectionName: "books",
    sparseVectorsConfig: ("title-bm25", new SparseVectorParams { Modifier = Modifier.Idf })
);
```


```go
client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "books",
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"title-bm25": {Modifier: qdrant.Modifier_Idf.Enum()},
		}),
})
```


```http
PUT /collections/books?wait=true
{
  "sparse_vectors": {
    "title-bm25": {
      "modifier": "idf"
    }
  }
}
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.*;

QdrantClient client =

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("books")
            .setSparseVectorsConfig(
                SparseVectorConfig.newBuilder()
                    .putMap(
                        "title-bm25",
                        SparseVectorParams.newBuilder().setModifier(Modifier.Idf).build())
                    .build())
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.create_collection(
    collection_name="books",
    sparse_vectors_config={
        "title-bm25": models.SparseVectorParams(modifier=models.Modifier.IDF)
    },
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Modifier, SparseVectorParamsBuilder, SparseVectorsConfigBuilder,
};

let mut sparse = SparseVectorsConfigBuilder::default();
sparse.add_named_vector_params(
    "title-bm25",
    SparseVectorParamsBuilder::default().modifier(Modifier::Idf),
);

client
    .create_collection(CreateCollectionBuilder::new("books").sparse_vectors_config(sparse))
    .await?;
```


```typescript
client.createCollection("books", {
  sparse_vectors: {
    "title-bm25": { modifier: "idf" },
  },
});
```
