You can create a collection with named vectors in Qdrant by defining multiple vector spaces for different features or modalities like image and text. Each vector space can have a unique name along with specific size and distance calculation method. Additionally, you can include sparse vectors in the collection configuration for more efficient representation of data points.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParamsMap
  {
      Map = {
      ["image"] = new VectorParams {
        Size = 4, Distance = Distance.Dot
      },
      ["text"] = new VectorParams {
        Size = 5, Distance = Distance.Cosine
      },
    }
  },
  sparseVectorsConfig: new SparseVectorConfig
  {
      Map = {
        ["text-sparse"] = new()
    }
  }
);
```


```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfigMap(
		map[string]*qdrant.VectorParams{
			"image": {
				Size:     4,
				Distance: qdrant.Distance_Dot,
			},
			"text": {
				Size:     5,
				Distance: qdrant.Distance_Cosine,
			},
		}),
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"text-sparse": {},
		},
	),
})
```


```http
PUT /collections/{collection_name}
{
  "vectors": {
    "image": {
      "size": 4,
      "distance": "Dot"
    },
    "text": {
      "size": 5,
      "distance": "Cosine"
    }
  },
  "sparse_vectors": {
    "text-sparse": {}
  }
}
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.SparseVectorConfig;
import io.qdrant.client.grpc.Collections.SparseVectorParams;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorParamsMap;
import io.qdrant.client.grpc.Collections.VectorsConfig;
import java.util.Map;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(VectorsConfig.newBuilder().setParamsMap(
                VectorParamsMap.newBuilder().putAllMap(Map.of("image",
                    VectorParams.newBuilder()
                        .setSize(4)
                        .setDistance(Distance.Dot)
                        .build(),
                    "text",
                    VectorParams.newBuilder()
                        .setSize(5)
                        .setDistance(Distance.Cosine)
                        .build()))))
            .setSparseVectorsConfig(SparseVectorConfig.newBuilder().putMap(
                "text-sparse", SparseVectorParams.getDefaultInstance()))
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config={
        "image": models.VectorParams(size=4, distance=models.Distance.DOT),
        "text": models.VectorParams(size=5, distance=models.Distance.COSINE),
    },
    sparse_vectors_config={"text-sparse": models.SparseVectorParams()},
)
```


```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, SparseVectorParamsBuilder, SparseVectorsConfigBuilder,
    VectorParamsBuilder, VectorsConfigBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut vector_config = VectorsConfigBuilder::default();
vector_config.add_named_vector_params("text", VectorParamsBuilder::new(5, Distance::Dot));
vector_config.add_named_vector_params("image", VectorParamsBuilder::new(4, Distance::Cosine));

let mut sparse_vectors_config = SparseVectorsConfigBuilder::default();
sparse_vectors_config
    .add_named_vector_params("text-sparse", SparseVectorParamsBuilder::default());

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(vector_config)
            .sparse_vectors_config(sparse_vectors_config),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
    vectors: {
        image: { size: 4, distance: "Dot" },
        text: { size: 5, distance: "Cosine" },
    },
    sparse_vectors: {
        text_sparse: {}
    }
});
```
