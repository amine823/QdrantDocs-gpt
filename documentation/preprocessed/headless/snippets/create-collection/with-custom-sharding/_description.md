This code snippet is used to create a collection with a User Defined Sharding (aka custom sharding) configured.
Unlike default auto-sharding, that uses hash-based sharding strategy, user-defined sharding allows to create named Shards and route requests to specific Shards based on application-level logic.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
	collectionName: "{collection_name}",
	// ... other collection parameters
	shardNumber: 1,
	shardingMethod: ShardingMethod.Custom
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
	// ... other collection parameters
	ShardNumber:    qdrant.PtrOf(uint32(1)),
	ShardingMethod: qdrant.ShardingMethod_Custom.Enum(),
})
```


```http
PUT /collections/{collection_name}
{
    "shard_number": 1,
    "sharding_method": "custom"
    // ... other collection parameters
}
```


```java
import static io.qdrant.client.ShardKeyFactory.shardKey;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.ShardingMethod;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            // ... other collection parameters
            .setShardNumber(1)
            .setShardingMethod(ShardingMethod.Custom)
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    shard_number=1,
    sharding_method=models.ShardingMethod.CUSTOM,
    # ... other collection parameters
)
```


```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Distance, ShardingMethod, VectorParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(300, Distance::Cosine))
            .shard_number(1)
            .sharding_method(ShardingMethod::Custom.into()),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
    shard_number: 1,
    sharding_method: "custom",
    // ... other collection parameters
});
```
