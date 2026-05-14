Update collection metadata. This example demonstrates how to overwrite a specific field in the collection's metadata while leaving other fields unchanged. Collection metadata can be any JSON object that provides additional information about the collection.

```bash
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "metadata": {
      "my-metadata-field": {
        "key-a": "value-a",
        "key-b": 42    
      }
    }
  }'
```


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	optimizersConfig: new OptimizersConfigDiff { IndexingThreshold = 10000 },
	metadata: new()
	{
		["my-metadata-field"] = new Dictionary<string, Value>
		{
			["key-a"] = "value-a",
			["key-b"] = 42
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

client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
	CollectionName: "{collection_name}",
	OptimizersConfig: &qdrant.OptimizersConfigDiff{
		IndexingThreshold: qdrant.PtrOf(uint64(10000)),
	},
	Metadata: qdrant.NewValueMap(map[string]any{
		"my-metadata-field": map[string]any{
			"key-a": "value-a",
			"key-b": 42,
		},
	}),
})
```


```http
PATCH /collections/{collection_name}
{
    "metadata": {
        "my-metadata-field": {
            "key-a": "value-a",
            "key-b": 42
        }
    }
}
```


```java
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.grpc.Collections.OptimizersConfigDiff;
import io.qdrant.client.grpc.Collections.UpdateCollection;
import java.util.Map;

client
    .updateCollectionAsync(
        UpdateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setOptimizersConfig(
                OptimizersConfigDiff.newBuilder().setIndexingThreshold(10000).build())
            .putAllMetadata(
                Map.of(
                    "my-metadata-field",
                    value(
                        Map.of(
                            "key-a", value("value-a"),
                            "key-b", value(42)))))
            .build())
    .get();
```


```python
client.update_collection(
    collection_name="{collection_name}",
    metadata={
        "my-metadata-field": {
            "key-a": "value-a",
            "key-b": 42
        }
    },
)
```


```rust
use qdrant_client::qdrant::{UpdateCollectionBuilder};
use qdrant_client::Qdrant;
use serde_json::{json, Value};
use std::collections::HashMap;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut metadata: HashMap<String, Value> = HashMap::new();
metadata.insert("my-metadata-field".to_string(), json!({
    "key-a": "value-a",
    "key-b": 42
}));

client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}").metadata(metadata),
    )
    .await?;
```


```typescript
client.updateCollection("{collection_name}", {
  metadata: {
    "my-metadata-field": {
      "key-a": "value-a",
      "key-b": 42
    }
  },
});
```
