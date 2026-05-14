This code snippet allows inserting a point with named vectors into a collection. The point has an ID and contains vectors labeled as "image," "text," and "text-sparse." The "image" vector has four values, the "text" vector has five values, and the "text-sparse" vector includes indices and corresponding values.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new()
        {
            Id = 1,
            Vectors = new Dictionary<string, Vector>
            {
                ["image"] = new float[] {0.9f, 0.1f, 0.1f, 0.2f},
                ["text"] = new float[] {0.4f, 0.7f, 0.1f, 0.8f, 0.1f},
                ["text-sparse"] = ([0.1f, 0.2f, 0.3f, 0.4f], [1, 3, 5, 7]),
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

client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "{collection_name}",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"image": qdrant.NewVector(0.9, 0.1, 0.1, 0.2),
				"text":  qdrant.NewVector(0.4, 0.7, 0.1, 0.8, 0.1),
				"text-sparse": qdrant.NewVectorSparse(
					[]uint32{1, 3, 5, 7},
					[]float32{0.1, 0.2, 0.3, 0.4}),
			}),
		},
	},
})
```


```http
PUT /collections/{collection_name}/points?wait=true
{
    "points": [
        {
            "id": 1,
            "vector": {
                "image": [0.9, 0.1, 0.1, 0.2],
                "text": [0.4, 0.7, 0.1, 0.8, 0.1],
                "text-sparse": {
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
                            vector(List.of(0.4f, 0.7f, 0.1f, 0.8f, 0.1f)),
                            "text-sparse",
                            vector(List.of(0.1f, 0.2f, 0.3f, 0.4f), List.of(1, 3, 5, 7)))))
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
                "text": [0.4, 0.7, 0.1, 0.8, 0.1],
                "text-sparse": {
                    "indices": [1, 3, 5, 7],
                    "values": [0.1, 0.2, 0.3, 0.4],
                },
            },
        ),
    ],
)
```


```rust
use qdrant_client::qdrant::{
    NamedVectors, PointStruct, UpsertPointsBuilder, Vector,
};
use qdrant_client::Payload;

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![PointStruct::new(
                1,
                NamedVectors::default()
                    .add_vector("text", Vector::new_dense(vec![0.4, 0.7, 0.1, 0.8, 0.1]))
                    .add_vector("image", Vector::new_dense(vec![0.9, 0.1, 0.1, 0.2]))
                    .add_vector(
                        "text-sparse",
                        Vector::new_sparse(vec![1, 3, 5, 7], vec![0.1, 0.2, 0.3, 0.4]),
                    ),
                Payload::default(),
            )],
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
                text: [0.4, 0.7, 0.1, 0.8, 0.1],
                text_sparse: {
                    indices: [1, 3, 5, 7],
                    values: [0.1, 0.2, 0.3, 0.4]
                }
            },
        },
    ],
});
```
