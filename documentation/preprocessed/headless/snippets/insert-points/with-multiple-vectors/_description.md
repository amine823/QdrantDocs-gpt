This code snippet demonstrates the insertion of points with multiple vectors into a collection. Each point has an id associated with it, along with vectors containing numerical values. The vectors are named 'image' and 'text' and consist of arrays of floating-point numbers. The API request uses the PUT method to upload the point data. Qdrant's idempotent nature ensures that re-uploading points with the same id will overwrite existing data, providing data consistency even in environments like message queues that lack exactly-once delivery guarantees. This feature is available starting from version 0.10.0.

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
			Vectors = new Dictionary<string, float[]>
			{
				["image"] = [0.9f, 0.1f, 0.1f, 0.2f],
				["text"] = [0.4f, 0.7f, 0.1f, 0.8f, 0.1f, 0.1f, 0.9f, 0.2f]
			}
		},
		new()
		{
			Id = 2,
			Vectors = new Dictionary<string, float[]>
			{
				["image"] = [0.2f, 0.1f, 0.3f, 0.9f],
				["text"] = [0.5f, 0.2f, 0.7f, 0.4f, 0.7f, 0.2f, 0.3f, 0.9f]
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
				"image": qdrant.NewVector(0.9, 0.1, 0.1, 0.2),
				"text":  qdrant.NewVector(0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2),
			}),
		},
		{
			Id: qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"image": qdrant.NewVector(0.2, 0.1, 0.3, 0.9),
				"text":  qdrant.NewVector(0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9),
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
                "image": [0.9, 0.1, 0.1, 0.2],
                "text": [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2]
            }
        },
        {
            "id": 2,
            "vector": {
                "image": [0.2, 0.1, 0.3, 0.9],
                "text": [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9]
            }
        }
    ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;
import java.util.Map;

client
    .upsertAsync(
        "{collection_name}",
        List.of(
            PointStruct.newBuilder()
                .setId(id(1))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "image",
                            vector(List.of(0.9f, 0.1f, 0.1f, 0.2f)),
                            "text",
                            vector(List.of(0.4f, 0.7f, 0.1f, 0.8f, 0.1f, 0.1f, 0.9f, 0.2f)))))
                .build(),
            PointStruct.newBuilder()
                .setId(id(2))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "image",
                            vector(List.of(0.2f, 0.1f, 0.3f, 0.9f)),
                            "text",
                            vector(List.of(0.5f, 0.2f, 0.7f, 0.4f, 0.7f, 0.2f, 0.3f, 0.9f)))))
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
                "image": [0.9, 0.1, 0.1, 0.2],
                "text": [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2],
            },
        ),
        models.PointStruct(
            id=2,
            vector={
                "image": [0.2, 0.1, 0.3, 0.9],
                "text": [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9],
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
                    HashMap::from([
                        ("image".to_string(), vec![0.9, 0.1, 0.1, 0.2]),
                        (
                            "text".to_string(),
                            vec![0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2],
                        ),
                    ]),
                    Payload::default(),
                ),
                PointStruct::new(
                    2,
                    HashMap::from([
                        ("image".to_string(), vec![0.2, 0.1, 0.3, 0.9]),
                        (
                            "text".to_string(),
                            vec![0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9],
                        ),
                    ]),
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
        image: [0.9, 0.1, 0.1, 0.2],
        text: [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2],
      },
    },
    {
      id: 2,
      vector: {
        image: [0.2, 0.1, 0.3, 0.9],
        text: [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9],
      },
    },
  ],
});
```
