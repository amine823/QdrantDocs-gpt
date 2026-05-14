To utilize multivectors in Qdrant, you can create a collection with a specified configuration. This configuration includes defining the size of the vectors (128 in this case), setting the distance metric as cosine, and enabling the multivector feature with the comparator function as `max_sim`. The `max_sim` function calculates the similarity between matrices of vectors by summing the maximum similarities between each pair of vectors in the matrices. This allows for scenarios where you may have multiple representations of the same object or late interaction embeddings, such as text embedding models outputting multiple vectors for a single text sequence.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  vectorsConfig: new VectorParams {
    Size = 128,
      Distance = Distance.Cosine,
      MultivectorConfig = new() {
        Comparator = MultiVectorComparator.MaxSim
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
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     128,
		Distance: qdrant.Distance_Cosine,
		MultivectorConfig: &qdrant.MultiVectorConfig{
			Comparator: qdrant.MultiVectorComparator_MaxSim,
		},
	}),
})
```


```http
PUT collections/{collection_name}
{
  "vectors": {
    "size": 128,
    "distance": "Cosine",
    "multivector_config": {
      "comparator": "max_sim"
    }
  }
}
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.MultiVectorComparator;
import io.qdrant.client.grpc.Collections.MultiVectorConfig;
import io.qdrant.client.grpc.Collections.VectorParams;

QdrantClient client =
  new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.createCollectionAsync("{collection_name}",
  VectorParams.newBuilder().setSize(128)
  .setDistance(Distance.Cosine)
  .setMultivectorConfig(MultiVectorConfig.newBuilder()
    .setComparator(MultiVectorComparator.MaxSim)
    .build())
  .build()).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config=models.VectorParams(
        size=128,
        distance=models.Distance.COSINE,
        multivector_config=models.MultiVectorConfig(
            comparator=models.MultiVectorComparator.MAX_SIM
        ),
    ),
)
```


```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, VectorParamsBuilder,
    MultiVectorComparator, MultiVectorConfigBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(
                VectorParamsBuilder::new(100, Distance::Cosine)
                    .multivector_config(
                        MultiVectorConfigBuilder::new(MultiVectorComparator::MaxSim)
                    ),
            ),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: {
    size: 128,
    distance: "Cosine",
    multivector_config: {
      comparator: "max_sim"
    }
  },
});
```
