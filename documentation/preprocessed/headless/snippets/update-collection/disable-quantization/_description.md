This code snippet demonstrates disabling quantization for a collection.


```bash
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "quantization_config": "Disabled"
  }'
```


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	quantizationConfig: new QuantizationConfigDiff { Disabled = new Disabled() }
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

client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
	CollectionName:     "{collection_name}",
	QuantizationConfig: qdrant.NewQuantizationDiffDisabled(),
})
```


```http
PATCH /collections/{collection_name}
{
    "quantization_config": "Disabled"
}
```


```java
import io.qdrant.client.grpc.Collections.Disabled;
import io.qdrant.client.grpc.Collections.QuantizationConfigDiff;
import io.qdrant.client.grpc.Collections.UpdateCollection;

client.updateCollectionAsync(
    UpdateCollection.newBuilder()
        .setCollectionName("{collection_name}")
        .setQuantizationConfig(
            QuantizationConfigDiff.newBuilder()
                .setDisabled(Disabled.getDefaultInstance())
                .build())
        .build());
```


```python
client.update_collection(
    collection_name="{collection_name}",
    quantization_config=models.Disabled.DISABLED,
)
```


```rust
use qdrant_client::qdrant::{Disabled, UpdateCollectionBuilder};

client
    .update_collection(UpdateCollectionBuilder::new("{collection_name}").quantization_config(Disabled {}))
    .await?;
```


```typescript
client.updateCollection("{collection_name}", {
    quantization_config: 'Disabled'
});
```
