This code snippet represents a functionality to overwrite the payload for specified points within a collection. It allows you to replace the current payload of the specified points with a new set of properties and values provided in the request body. The points that will have their payloads overwritten are identified by their respective IDs within the collection.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.OverwritePayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
    ids: new ulong[] { 0, 3, 10 }
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

client.OverwritePayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})
```


```http
PUT /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
    "points": [
        0, 3, 100
    ]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;

import java.util.List;
import java.util.Map;

client
    .overwritePayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        List.of(id(0), id(3), id(10)),
        true,
        null,
        null)
    .get();
```


```python
client.overwrite_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
    points=[0, 3, 10],
)
```


```rust
use qdrant_client::qdrant::{PointsIdsList, SetPayloadPointsBuilder};
use qdrant_client::Payload;
use serde_json::json;

client
    .overwrite_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;
```


```typescript
client.overwritePayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
  points: [0, 3, 10],
});
```
