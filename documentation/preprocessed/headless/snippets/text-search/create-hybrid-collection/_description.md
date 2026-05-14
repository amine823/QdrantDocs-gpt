Creates a hybrid collection combining a dense `description-dense` vector with a sparse `isbn-bm25` vector for semantic + lexical search.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.CreateCollectionAsync(
    collectionName: "books",
    vectorsConfig: new VectorParamsMap
    {
        Map =
        {
            ["description-dense"] = new VectorParams
            {
                Size = 384,
                Distance = Distance.Cosine,
            },
        },
    },
    sparseVectorsConfig: new SparseVectorConfig
    {
        Map = { ["isbn-bm25"] = new SparseVectorParams { Modifier = Modifier.Idf } },
    }
);
```


```go
client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "books",
	VectorsConfig: qdrant.NewVectorsConfigMap(
		map[string]*qdrant.VectorParams{
			"description-dense": {Size: 384, Distance: qdrant.Distance_Cosine},
		}),
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"isbn-bm25": {Modifier: qdrant.Modifier_Idf.Enum()},
		}),
})
```


```http
PUT /collections/books?wait=true
{
  "vectors": {
    "description-dense": {
      "size": 384,
      "distance": "Cosine"
    }
  },
  "sparse_vectors": {
    "isbn-bm25": {
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
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParamsMap(
                        VectorParamsMap.newBuilder()
                            .putMap(
                                "description-dense",
                                VectorParams.newBuilder()
                                    .setSize(384)
                                    .setDistance(Distance.Cosine)
                                    .build())
                            .build())
                    .build())
            .setSparseVectorsConfig(
                SparseVectorConfig.newBuilder()
                    .putMap(
                        "isbn-bm25",
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
    vectors_config={
        "description-dense": models.VectorParams(size=384, distance=models.Distance.COSINE)
    },
    sparse_vectors_config={
        "isbn-bm25": models.SparseVectorParams(modifier=models.Modifier.IDF)
    },
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, Modifier, SparseVectorParamsBuilder,
    SparseVectorsConfigBuilder, VectorParamsBuilder, VectorsConfigBuilder,
};

let mut vectors = VectorsConfigBuilder::default();
vectors.add_named_vector_params(
    "description-dense",
    VectorParamsBuilder::new(384, Distance::Cosine),
);

let mut sparse = SparseVectorsConfigBuilder::default();
sparse.add_named_vector_params(
    "isbn-bm25",
    SparseVectorParamsBuilder::default().modifier(Modifier::Idf),
);

client
    .create_collection(
        CreateCollectionBuilder::new("books")
            .vectors_config(vectors)
            .sparse_vectors_config(sparse),
    )
    .await?;
```


```typescript
client.createCollection("books", {
  vectors: {
    "description-dense": { size: 384, distance: "Cosine" },
  },
  sparse_vectors: {
    "isbn-bm25": { modifier: "idf" },
  },
});
```
