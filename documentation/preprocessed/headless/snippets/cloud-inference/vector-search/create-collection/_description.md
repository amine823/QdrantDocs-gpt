This code snippet creates a collection configured for hybrid search using Qdrant's Cloud Inference. It defines a sparse BM25 vector and a dense vector for MiniLM. This setup allows Qdrant to perform hybrid search using the dense and sparse vectors. 

```csharp
await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParamsMap
  {
      Map = {
      ["dense_vector"] = new VectorParams {
        Size = 384, Distance = Distance.Cosine
      },
    }
  },
  sparseVectorsConfig: new SparseVectorConfig
  {
      Map = {
        ["bm25_sparse_vector"] = new() {
    	  Modifier = Modifier.Idf,  // Enable Inverse Document Frequency
  		}
    }
  }
);
```


```go
client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfigMap(
		map[string]*qdrant.VectorParams{
			"dense_vector": {
				Size:     384,
				Distance: qdrant.Distance_Cosine,
			},
		}),
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"bm25_sparse_vector": {
				Modifier: qdrant.Modifier_Idf.Enum(),
			},
		},
	),
})
```


```java
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.Modifier;
import io.qdrant.client.grpc.Collections.SparseVectorConfig;
import io.qdrant.client.grpc.Collections.SparseVectorParams;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorParamsMap;
import io.qdrant.client.grpc.Collections.VectorsConfig;
import java.util.Map;

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParamsMap(
                        VectorParamsMap.newBuilder()
                            .putAllMap(
                                Map.of(
                                    "dense_vector",
                                    VectorParams.newBuilder()
                                        .setSize(384)
                                        .setDistance(Distance.Cosine)
                                        .build())))
                    .build())
            .setSparseVectorsConfig(
                SparseVectorConfig.newBuilder()
                    .putMap(
                        "bm25_sparse_vector",
                        SparseVectorParams.newBuilder()
                            .setModifier(Modifier.Idf)
                            .build()))
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client.create_collection(
    collection_name="{collection_name}",
    vectors_config={
        "dense_vector": models.VectorParams(
            size=384,
            distance=models.Distance.COSINE
        )
    },
    sparse_vectors_config={
        "bm25_sparse_vector": models.SparseVectorParams(
            modifier=models.Modifier.IDF # Enable Inverse Document Frequency
        )
    }
)
```


```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, Modifier, SparseVectorParamsBuilder,
    SparseVectorsConfigBuilder, VectorParamsBuilder, VectorsConfigBuilder,
};

let mut vector_config = VectorsConfigBuilder::default();
vector_config.add_named_vector_params(
    "dense_vector",
    VectorParamsBuilder::new(384, Distance::Cosine),
);

let mut sparse_vectors_config = SparseVectorsConfigBuilder::default();
sparse_vectors_config.add_named_vector_params(
    "bm25_sparse_vector",
    SparseVectorParamsBuilder::default().modifier(Modifier::Idf), // Enable Inverse Document Frequency
);

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(vector_config)
            .sparse_vectors_config(sparse_vectors_config),
    )
    .await?;
```


```typescript
client.createCollection("{collection_name}", {
  vectors: {
    dense_vector: { size: 384, distance: "Cosine" },
  },
  sparse_vectors: {
    bm25_sparse_vector: {
      modifier: "idf" // Enable Inverse Document Frequency
    }
  }
});
```
