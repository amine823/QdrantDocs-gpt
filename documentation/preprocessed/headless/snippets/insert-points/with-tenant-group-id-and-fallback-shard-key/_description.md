This code snippet is for a PUT request to insert points into a collection, where each point has an ID, a payload containing a group ID, and a vector. The code illustrates partitioning vectors by user to ensure that each user can only access their own vectors. It emphasizes adding a `group_id` field to each vector in the collection, facilitating user-specific data access control. Additionally, it suggests using an appropriate naming convention for the key in the payload for flexibility in data structures.
In addition, the snippet includes a shard key selector, allowing a dymamic routing between shared and dedicated shards based on the existance of `target` shard in the collection.


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
			Vectors = new[] { 0.9f, 0.1f, 0.1f },
			Payload = { ["group_id"] = "user_1" }
		}
	},
	shardKeySelector: new ShardKeySelector { 
		ShardKeys = { new List<ShardKey> { "user_1" } },
		Fallback = new ShardKey { Keyword = "default" }
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
			Id:      qdrant.NewIDNum(1),
			Vectors: qdrant.NewVectors(0.9, 0.1, 0.1),
			Payload: qdrant.NewValueMap(map[string]any{"group_id": "user_1"}),
		},
	},
	ShardKeySelector: &qdrant.ShardKeySelector{
		ShardKeys: []*qdrant.ShardKey{
			qdrant.NewShardKey("user_1"),
		},
		Fallback: qdrant.NewShardKey("default"),
	},
})
```


```http
PUT /collections/{collection_name}/points
{
    "points": [
        {
            "id": 1,
            "payload": {"group_id": "user_1"},
            "vector": [0.9, 0.1, 0.1]
        }
    ],
    "shard_key": {
        "fallback": "default",
        "target": "user_1"
    }
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ShardKeyFactory.shardKey;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorsFactory.vectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.PointStruct;
import io.qdrant.client.grpc.Points.ShardKeySelector;
import io.qdrant.client.grpc.Points.UpsertPoints;
import java.util.List;
import java.util.Map;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .upsertAsync(
        UpsertPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .addAllPoints(
                List.of(
                    PointStruct.newBuilder()
                        .setId(id(1))
                        .setVectors(vectors(0.9f, 0.1f, 0.1f))
                        .putAllPayload(Map.of("group_id", value("user_1")))
                        .build()))
            .setShardKeySelector(
                ShardKeySelector.newBuilder()
                    .addShardKeys(shardKey("user_1"))
                    .setFallback(shardKey("default"))
                    .build())
            .build())
    .get();
```


```python
client.upsert(
    collection_name="{collection_name}",
    points=[
        models.PointStruct(
            id=1,
            payload={"group_id": "user_1"},
            vector=[0.9, 0.1, 0.1],
        ),
    ],
    shard_key_selector=models.ShardKeyWithFallback(
        target="user_1",
        fallback="default"
    )
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{PointStruct, ShardKeySelectorBuilder, UpsertPointsBuilder};

let client = Qdrant::from_url("http://localhost:6334").build()?;

let shard_key_selector = ShardKeySelectorBuilder::with_shard_key("user_1")
    .fallback("default")
    .build();

client
    .upsert_points(
        UpsertPointsBuilder::new(
            "{collection_name}",
            vec![
                PointStruct::new(
                    1,
                    vec![0.9, 0.1, 0.1],
                    [("group_id", "user_1".into())]
                ),
            ],
        )
        .shard_key_selector(shard_key_selector),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.upsert("{collection_name}", {
  points: [
    {
      id: 1,
      payload: { group_id: "user_1" },
      vector: [0.9, 0.1, 0.1],
    }
  ],
  shard_key: {
    target: "user_1",
    fallback: "default"
  }
});
```
