This request is used to proote tenant from shared Shard to dedicated shard.
It takes two shard keys - one indicated where to transfer from, another where to thatsfer to,
as well as filtering condition which defines a subset of points to transfer.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionClusterSetupAsync(new()
{
    CollectionName = "{collection_name}",
	ReplicatePoints = new()
    {
        FromShardKey = "default",
		ToShardKey = "user_1",
		Filter = MatchKeyword("group_id", "user_1")
    }
});
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

client.UpdateClusterCollectionSetup(context.Background(), qdrant.NewUpdateCollectionClusterReplicatePoints(
	"{collection_name}", &qdrant.ReplicatePoints{
		FromShardKey: qdrant.NewShardKey("default"),
		ToShardKey:   qdrant.NewShardKey("user_1"),
		Filter: &qdrant.Filter{
			Must: []*qdrant.Condition{
				qdrant.NewMatch("group_id", "user_1"),
			},
		},
	},
))
```


```http
POST /collections/{collection_name}/cluster
{
    "replicate_points": {
        "filter": {
            "must": {
                "key": "group_id",
                "match": {
                    "value": "user_1"
                }
            }
        },
        "from_shard_key": "default",
        "to_shard_key": "user_1"
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.ShardKeyFactory.shardKey;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.ReplicatePoints;
import io.qdrant.client.grpc.Collections.UpdateCollectionClusterSetupRequest;
import io.qdrant.client.grpc.Common.Filter;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .updateCollectionClusterSetupAsync(
        UpdateCollectionClusterSetupRequest.newBuilder()
            .setCollectionName("{collection_name}")
            .setReplicatePoints(
                ReplicatePoints.newBuilder()
                    .setFromShardKey(shardKey("default"))
                    .setToShardKey(shardKey("user_1"))
                    .setFilter(
                        Filter.newBuilder().addMust(matchKeyword("group_id", "user_1")).build())
                    .build())
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.cluster_collection_update(
    collection_name="{collection_name}",
    cluster_operation=models.ReplicatePointsOperation(
        replicate_points=models.ReplicatePoints(
            from_shard_key="default",
            to_shard_key="user_1",
            filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="group_id",
                        match=models.MatchValue(
                            value="user_1",
                        )
                    )
                ]
            )
        )
    )
)
```


```rust
use qdrant_client::qdrant::{
    update_collection_cluster_setup_request::Operation, Condition, Filter,
    ReplicatePointsBuilder, ShardKey, UpdateCollectionClusterSetupRequest,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .update_collection_cluster_setup(UpdateCollectionClusterSetupRequest {
        collection_name: "{collection_name}".to_string(),
        operation: Some(Operation::ReplicatePoints(
            ReplicatePointsBuilder::new(
                ShardKey::from("default"),
                ShardKey::from("user_1"),
            )
            .filter(Filter::must([Condition::matches(
                "group_id",
                "user_1".to_string(),
            )]))
            .build(),
        )),
        timeout: None,
    })
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.updateCollectionCluster("{collection_name}", {
    replicate_points: {
        filter: {
            must: {
                key: "group_id",
                match: {
                    value: "user_1"
                }
            }
        },
        from_shard_key: "default",
        to_shard_key: "user_1"
    }
});
```
