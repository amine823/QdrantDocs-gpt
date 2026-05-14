This code snippet is used to create a collection with a specific vector configuration and additional metadata. The metadata is provided as a JSON object, allowing you to store custom information about the collection. In this example, we add two metadata fields.

```bash
curl -X PUT http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
      "size": 300,
      "distance": "Cosine"
    },
    "metadata": {
      "my-metadata-field": "value-1",
      "another-field": 123
    }
  }'
```


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
	collectionName: "{collection_name}",
	vectorsConfig: new VectorParams { Size = 100, Distance = Distance.Cosine },
	metadata: new()
	{
		["my-metadata-field"] = "value-1",
		["another-field"] = 123
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

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	VectorsConfig: qdrant.NewVectorsConfig(&qdrant.VectorParams{
		Size:     100,
		Distance: qdrant.Distance_Cosine,
	}),
	Metadata: qdrant.NewValueMap(map[string]any{
		"my-metadata-field": "value-1",
		"another-field":     123,
	}),
})
```


```http
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 300,
      "distance": "Cosine"
    },
    "metadata": {
      "my-metadata-field": "value-1",
      "another-field": 123
    }
}
```


```java
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Distance;
import io.qdrant.client.grpc.Collections.VectorParams;
import io.qdrant.client.grpc.Collections.VectorsConfig;
import java.util.Map;

QdrantClient client = new QdrantClient(
    QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createCollectionAsync(
        CreateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setVectorsConfig(
                VectorsConfig.newBuilder()
                    .setParams(
                        VectorParams.newBuilder()
                            .setDistance(Distance.Cosine)
                            .setSize(100)
                            .build())
                    .build())
            .putAllMetadata(
                Map.of(
                    "my-metadata-field", value("value-1"),
                    "another-field", value(123)))
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    metadata={
        "my-metadata-field": "value-1",
        "another-field": 123
    },
)
```


```rust
use qdrant_client::qdrant::{CreateCollectionBuilder, Distance, VectorParamsBuilder};
use qdrant_client::Qdrant;
use serde_json::{json, Value};
use std::collections::HashMap;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut metadata: HashMap<String, Value> = HashMap::new();
metadata.insert("my-metadata-field".to_string(), json!("value-1"));
metadata.insert("another-field".to_string(), json!(123));

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .vectors_config(VectorParamsBuilder::new(100, Distance::Cosine))
            .metadata(metadata),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  vectors: { size: 100, distance: "Cosine" },
  metadata: {
    "my-metadata-field": "value-1",
    "another-field": 123
  }
});
```
