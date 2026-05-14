This code snippet demonstrates how to insert a point with conditionally. Update condition is represented by a filter, if the filter matches existing points, the point will be updated. If condition doesn't match the point, the upsert operation will be ignored. If the point doesn't exist, it will be inserted as a new point.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.UpsertAsync(
    collectionName: "{collection_name}",
    points: new List<PointStruct>
    {
        new PointStruct
        {
            Id = 1,
            Vectors = new[] { 0.05f, 0.61f, 0.76f, 0.74f },
            Payload = { 
                ["city"] = "Berlin",
                ["price"] = 1.99,
                ["version"] = 3
            }
        }
    },
    updateFilter: Match("version", 2)
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
            Id:      qdrant.NewIDNum(1),
            Vectors: qdrant.NewVectors(0.05, 0.61, 0.76, 0.74),
            Payload: qdrant.NewValueMap(map[string]any{
                "city": "Berlin", "price": 1.99, "version": 3}),
        },
    },
    UpdateFilter: &qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatchInt("version", 2),
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
            "vector": [0.05, 0.61, 0.76, 0.74],
            "payload": {
                "city": "Berlin",
                "price": 1.99,
                "version": 3
            }
        }
    ],
    "update_filter": {
        "must": [
            {
                "key": "version",
                "match": {
                    "value": 2
                }
            }
        ]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.UpsertPoints;
import java.util.Map;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .upsertAsync(
        UpsertPoints.newBuilder()
            .setCollectionName("{collectionName}")
            .addPoints(
                PointStruct.newBuilder()
                    .setId(id(1))
                    .setVectors(vectors(0.05f, 0.61f, 0.76f, 0.74f))
                    .putAllPayload(Map.of("city", value("Berlin"), "price", value(1.99)))
                    .build())
            .setUpdateFilter(Filter.newBuilder().addMust(match("version", 2)).build())
            .build())
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
            vector=[0.05, 0.61, 0.76, 0.74],
            payload={
                "city": "Berlin",
                "price": 1.99,
                "version": 3,
            },
        ),
    ],
    update_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="version",
                match=models.MatchValue(value=2),
            ),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{PointStruct, UpsertPointsBuilder, Filter, Condition};
use qdrant_client::{Payload, Qdrant};
use serde_json::json;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let points = vec![
    PointStruct::new(
        1,
        vec![0.05, 0.61, 0.76, 0.74],
        Payload::try_from(json!({
            "city": "Berlin", 
            "price": 1.99,
            "version": 3
        })).unwrap(),
    )
];

client
    .upsert_points(
        UpsertPointsBuilder::new("{collection_name}", points)
            .wait(true)
            .update_filter(Filter::must([Condition::matches("version", 2)]))
    ).await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      vector: [0.05, 0.61, 0.76, 0.74],
      payload: {
        city: "Berlin",
        price: 1.99,
        version: 3
      },
    }
  ],
  update_filter: {
    must: [
      {
        key: "version",
        match: {
          value: 2
        }
      }
    ]
  }
});
```
