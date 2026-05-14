Inserts a point with a sparse vector, identified by its ID and containing indices and corresponding values, into the specified collection.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
  collectionName: "{collection_name}",
  points: new List < PointStruct > {
    new() {
      Id = 1,
        Vectors = new Dictionary <string, Vector> {
          ["text"] = ([0.1f, 0.2f, 0.3f, 0.4f], [1, 3, 5, 7])
        }
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(
				map[string]*qdrant.Vector{
					"text": qdrant.NewVectorSparse(
						[]uint32{1, 3, 5, 7},
						[]float32{0.1, 0.2, 0.3, 0.4}),
				}),
		},
	},
})
```


```http
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "vector": {
                "text": {
                    "indices": [1, 3, 5, 7],
                    "values": [0.1, 0.2, 0.3, 0.4]
                }
            }
        }
    ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;
import java.util.Map;

QdrantClient client =
  new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
  .upsertAsync(
    "{collection_name}",
    List.of(
      PointStruct.newBuilder()
      .setId(id(1))
      .setVectors(
        namedVectors(Map.of(
          "text", vector(List.of(1.0f, 2.0f), List.of(6, 7))))
      )
      .build()))
  .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            payload={},  # Add any additional payload if necessary
            vector={
                "text": models.SparseVector(
                    indices=[1, 3, 5, 7],
                    values=[0.1, 0.2, 0.3, 0.4]
                )
            },
        )
    ],
)
```


```rust
use qdrant_client::qdrant::{NamedVectors, PointStruct, UpsertPointsBuilder, Vector};

use qdrant_client::{Payload, Qdrant};

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![PointStruct::new(
    1,
    NamedVectors::default().add_vector(
        "text",
        Vector::new_sparse(vec![1, 3, 5, 7], vec![0.1, 0.2, 0.3, 0.4]),
    ),
    Payload::new(),
)];

client
    .upsert_points(UpsertPointsBuilder::new("{collection_name}", points))
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      vector: {
        text: {
          indices: [1, 3, 5, 7],
          values: [0.1, 0.2, 0.3, 0.4]
        },
      },
    }
  ]
});
```
