This code snippet creates a named shard with the name "default" in a Qdrant collection.
Collection is required to be configured with `custom` sharding method to support named shards.
Once created, named shard will receive all requests that specify its name in the shard key selector.

If no named shard is specified in the request, request will be broadcasted to all shards in the collection.


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateShardKeyAsync(
    "{collection_name}",
    new CreateShardKey { ShardKey = new ShardKey { Keyword = "default", } }
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

client.CreateShardKey(context.Background(), "{collection_name}", &qdrant.CreateShardKey{
	ShardKey: qdrant.NewShardKey("default"),
})
```


```http
PUT /collections/{collection_name}/shards
{
  "shard_key": "default"
}
```


```java
import static io.qdrant.client.ShardKeyFactory.shardKey;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateShardKey;
import io.qdrant.client.grpc.Collections.CreateShardKeyRequest;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.createShardKeyAsync(CreateShardKeyRequest.newBuilder()
                .setCollectionName("{collection_name}")
                .setRequest(CreateShardKey.newBuilder()
                                .setShardKey(shardKey("default"))
                                .build())
                .build()).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_shard_key("{collection_name}", "default")
```


```rust
use qdrant_client::qdrant::{
    CreateShardKeyBuilder, CreateShardKeyRequestBuilder
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_shard_key(
        CreateShardKeyRequestBuilder::new("{collection_name}")
            .request(CreateShardKeyBuilder::default().shard_key("default".to_string())),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createShardKey("{collection_name}", {
    shard_key: "default"
});
```
