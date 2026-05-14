This code snippet is for inserting a point with a multivector into a collection. It defines an operation to update a collection with a new point containing an ID and a vector represented by multiple arrays of values.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
  collectionName: "{collection_name}",
  points: new List <PointStruct> {
    new() {
      Id = 1,
        Vectors = new float[][] {
          [-0.013f, 0.020f, -0.007f, -0.111f],
          [-0.030f, -0.05f, 0.001f, 0.072f],
          [-0.041f, 0.014f, -0.032f, -0.062f ],
        },
    },
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
			Vectors: qdrant.NewVectorsMulti(
				[][]float32{
					{-0.013, 0.020, -0.007, -0.111},
					{-0.030, -0.055, 0.001, 0.072},
					{-0.041, 0.014, -0.032, -0.062}}),
		},
	},
})
```


```http
PUT collections/{collection_name}/points
{
  "points": [
    {
      "id": 1,
      "vector": [
        [-0.013,  0.020, -0.007, -0.111, ...],
        [-0.030, -0.055,  0.001,  0.072, ...],
        [-0.041,  0.014, -0.032, -0.062, ...]
      ]
    }
  ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.VectorFactory.multiVector;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.PointStruct;
import java.util.List;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
.upsertAsync(
    "{collection_name}",
    List.of(
        PointStruct.newBuilder()
            .setId(id(1))
            .setVectors(vectors(multiVector(new float[][] {
                {-0.013f,  0.020f, -0.007f, -0.111f},
                {-0.030f, -0.055f,  0.001f,  0.072f},
                {-0.041f,  0.014f, -0.032f, -0.062f}
            })))
            .build()
    ))
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
            vector=[
                [-0.013,  0.020, -0.007, -0.111],
                [-0.030, -0.055,  0.001,  0.072],
                [-0.041,  0.014, -0.032, -0.062]
            ],
        )
    ],
)
```


```rust
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder, Vector};
use qdrant_client::{Payload, Qdrant};

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![
    PointStruct::new(
        1,
        Vector::new_multi(vec![
            vec![-0.013, 0.020, -0.007, -0.111],
            vec![-0.030, -0.055, 0.001, 0.072],
            vec![-0.041, 0.014, -0.032, -0.062],
        ]),
        Payload::new()
    )
];

client
    .upsert_points(
        UpsertPointsBuilder::new("{collection_name}", points)
    ).await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      vector: [
        [-0.013,  0.020, -0.007, -0.111],
        [-0.030, -0.055,  0.001,  0.072],
        [-0.041,  0.014, -0.032, -0.062]
      ],
    }
  ]
});
```
