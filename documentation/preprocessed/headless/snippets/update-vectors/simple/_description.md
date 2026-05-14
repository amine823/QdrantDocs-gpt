This code snippet represents an operation to update vectors associated with points in a collection. The operation uses a PUT request to update vectors for specific points by providing their IDs along with the new vector data. This method ensures that only the specified vectors are updated, while leaving any unspecified vectors unchanged. It is important to note that all the provided points must already exist in the collection for the update to be successful.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateVectorsAsync(
	collectionName: "{collection_name}",
	points: new List<PointVectors>
	{
		new() { Id = 1, Vectors = ("image", new float[] { 0.1f, 0.2f, 0.3f, 0.4f }) },
		new()
		{
			Id = 2,
			Vectors = ("text", new float[] { 0.9f, 0.8f, 0.7f, 0.6f, 0.5f, 0.4f, 0.3f, 0.2f })
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

client.UpdateVectors(context.Background(), &qdrant.UpdatePointVectors{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointVectors{
		{
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"image": qdrant.NewVector(0.1, 0.2, 0.3, 0.4),
			}),
		},
		{
			Id: qdrant.NewIDNum(2),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"text": qdrant.NewVector(0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2),
			}),
		},
	},
})
```


```http
PUT /collections/{collection_name}/points/vectors
{
    "points": [
        {
            "id": 1,
            "vector": {
                "image": [0.1, 0.2, 0.3, 0.4]
            }
        },
        {
            "id": 2,
            "vector": {
                "text": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
            }
        }
    ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.grpc.Points.PointVectors;
import java.util.List;
import java.util.Map;

client
    .updateVectorsAsync(
        "{collection_name}",
        List.of(
            PointVectors.newBuilder()
                .setId(id(1))
                .setVectors(namedVectors(Map.of("image", vector(List.of(0.1f, 0.2f, 0.3f, 0.4f)))))
                .build(),
            PointVectors.newBuilder()
                .setId(id(2))
                .setVectors(
                    namedVectors(
                        Map.of(
                            "text", vector(List.of(0.9f, 0.8f, 0.7f, 0.6f, 0.5f, 0.4f, 0.3f, 0.2f)))))
                .build()))
    .get();
```


```python
client.update_vectors(
    collection_name="{collection_name}",
    points=[
        models.PointVectors(
            id=1,
            vector={
                "image": [0.1, 0.2, 0.3, 0.4],
            },
        ),
        models.PointVectors(
            id=2,
            vector={
                "text": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
            },
        ),
    ],
)
```


```rust
use std::collections::HashMap;

use qdrant_client::qdrant::{
    PointVectors, UpdatePointVectorsBuilder,
};

client
    .update_vectors(
        UpdatePointVectorsBuilder::new(
            "{collection_name}",
            vec![
                PointVectors {
                    id: Some(1.into()),
                    vectors: Some(
                        HashMap::from([("image".to_string(), vec![0.1, 0.2, 0.3, 0.4])]).into(),
                    ),
                },
                PointVectors {
                    id: Some(2.into()),
                    vectors: Some(
                        HashMap::from([(
                            "text".to_string(),
                            vec![0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
                        )])
                        .into(),
                    ),
                },
            ],
        )
        .wait(true),
    )
    .await?;
```


```typescript
client.updateVectors("{collection_name}", {
  points: [
    {
      id: 1,
      vector: {
        image: [0.1, 0.2, 0.3, 0.4],
      },
    },
    {
      id: 2,
      vector: {
        text: [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
      },
    },
  ],
});
```
