This code snippet set `max_collection_vector_size_bytes` and `max_collection_payload_size_bytes` on the strict mode configuration to cap the maximum size in bytes of a collection.

```bash
curl -X PUT http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "strict_mode_config": {
      "enabled":" true,
      "max_collection_vector_size_bytes": 100000,
      "max_collection_payload_size_bytes": 100000
    }
  }'
```


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  strictModeConfig: new StrictModeConfig { Enabled = true, MaxCollectionVectorSizeBytes = 1000000, MaxCollectionPayloadSizeBytes = 1000000 }
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
  StrictModeConfig: &qdrant.StrictModeConfig{
    Enabled: qdrant.PtrOf(true),
    MaxCollectionVectorSizeBytes: qdrant.PtrOf(uint64(1000000)),
    MaxCollectionPayloadSizeBytes: qdrant.PtrOf(uint64(1000000)),
  },
})
```


```http
PUT /collections/{collection_name}
{
    "strict_mode_config": {
        "enabled": true,
        "max_collection_vector_size_bytes": 1000000,
        "max_collection_payload_size_bytes": 1000000
    }
}
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.StrictModeConfig;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setStrictModeConfig(
                StrictModeConfig.newBuilder().setEnabled(true).setMaxCollectionVectorSizeBytes(1000000).setMaxCollectionPayloadSizeBytes(1000000).build())
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    strict_mode_config=models.StrictModeConfig(enabled=True, max_collection_vector_size_bytes=1000000, max_collection_payload_size_bytes=1000000),
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{CreateCollectionBuilder, StrictModeConfigBuilder};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .strict_mode_config(StrictModeConfigBuilder::default().enabled(true).max_collection_vector_size_bytes(1000000).max_collection_payload_size_bytes(1000000)),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  strict_mode_config: {
    enabled: true,
    max_collection_vector_size_bytes: 1000000,
    max_collection_payload_size_bytes: 1000000,
  },
});
```
