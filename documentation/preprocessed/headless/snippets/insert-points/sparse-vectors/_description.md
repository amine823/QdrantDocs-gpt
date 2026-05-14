This code snippet showcases a system for inserting points with sparse vectors into collections. Each point consists of an ID and a vector, where the vector data includes the indices and corresponding values. The `indices` and `values` arrays are required to have the same length, with unique `indices`. If the `indices` are not sorted, the system will internally sort them. Sparse vectors can be uploaded in a similar manner as dense vectors.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
	collectionName: "{collection_name}",
	points: new List<PointStruct>
	{
		new()
		{
			Id = 1,
			Vectors = new Dictionary<string, Vector> { ["text"] = ([1.0f, 2.0f], [6, 7]) }
		},
		new()
		{
			Id = 2,
			Vectors = new Dictionary<string, Vector>
			{
				["text"] = ([0.1f, 0.2f, 0.3f, 0.4f, 0.5f], [1, 2, 3, 4, 5])
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
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"text": qdrant.NewVectorSparse(
					[]uint32{6, 7},
					[]float32{1.0, 2.0}),
			}),
		},
		{
			Id: qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"text": qdrant.NewVectorSparse(
					[]uint32{1, 2, 3, 4, 5},
					[]float32{0.1, 0.2, 0.3, 0.4, 0.5}),
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
                    "indices": [6, 7],
                    "values": [1.0, 2.0]
                }
            }
        },
        {
            "id": 2,
            "vector": {
                "text": {
                    "indices": [1, 2, 4, 15, 33, 34],
                    "values": [0.1, 0.2, 0.3, 0.4, 0.5]
                }
            }
        }
    ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;

import io.qdrant.client.grpc.Points.NamedVectors;
import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.Vectors;
import java.util.List;
import java.util.Map;

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(
                    Vectors.newBuilder()
                        .setVectors(
                            NamedVectors.newBuilder()
                                .putAllVectors(
                                    Map.of(
                                        "text", vector(List.of(1.0f, 2.0f), List.of(6, 7))))
                                .build())
                        .build())
                .build(),
            PointStruct.newBuilder()
                .setId(id(2))
                .setVectors(
                    Vectors.newBuilder()
                        .setVectors(
                            NamedVectors.newBuilder()
                                .putAllVectors(
                                    Map.of(
                                        "text",
                                        vector(
                                            List.of(0.1f, 0.2f, 0.3f, 0.4f, 0.5f),
                                            List.of(1, 2, 3, 4, 5))))
                                .build())
                        .build())
                .build()))
    .get();
```


```python
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "text": models.SparseVector(
                    indices=[6, 7],
                    values=[1.0, 2.0],
                )
            },
        ),
        models.PointStruct(
            id=2,
            vector={
                "text": models.SparseVector(
                    indices=[1, 2, 3, 4, 5],
                    values=[0.1, 0.2, 0.3, 0.4, 0.5],
                )
            },
        ),
    ],
)
```


```rust
use std::collections::HashMap;

use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder};
use qdrant_client::Payload;

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![
                PointStruct::new(
                    1,
                    HashMap::from([("text".to_string(), vec![(6, 1.0), (7, 2.0)])]),
                    Payload::default(),
                ),
                PointStruct::new(
                    2,
                    HashMap::from([(
                        "text".to_string(),
                        vec![(1, 0.1), (2, 0.2), (3, 0.3), (4, 0.4), (5, 0.5)],
                    )]),
                    Payload::default(),
                ),
            ],
        )
        .wait(true),
    )
    .await?;
```


```typescript
client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      vector: {
        text: {
          indices: [6, 7],
          values: [1.0, 2.0],
        },
      },
    },
    {
      id: 2,
      vector: {
        text: {
          indices: [1, 2, 3, 4, 5],
          values: [0.1, 0.2, 0.3, 0.4, 0.5],
        },
      },
    },
  ],
});
```
