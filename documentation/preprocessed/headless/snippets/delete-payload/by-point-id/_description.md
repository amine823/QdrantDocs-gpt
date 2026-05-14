This code snippet pertains to deleting specific keys from the payload of points. It specifies the keys to be deleted as 'color' and 'price' from the points with IDs 0, 3, and 100 within a collection.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeletePayloadAsync(
    collectionName: "{collection_name}",
    keys: ["color", "price"],
    ids: new ulong[] { 0, 3, 100 }
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

client.DeletePayload(context.Background(), &qdrant.DeletePayloadPoints{
    CollectionName: "{collection_name}",
    Keys:           []string{"color", "price"},
    PointsSelector: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})
```


```http
POST /collections/{collection_name}/points/payload/delete
{
    "keys": ["color", "price"],
    "points": [0, 3, 100]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .deletePayloadAsync(
        "{collection_name}",
        List.of("color", "price"),
        List.of(id(0), id(3), id(100)),
        true,
        null,
        null)
    .get();
```


```python
client.delete_payload(
    collection_name="{collection_name}",
    keys=["color", "price"],
    points=[0, 3, 100],
)
```


```rust
use qdrant_client::qdrant::{DeletePayloadPointsBuilder, PointsIdsList};

client
    .delete_payload(
        DeletePayloadPointsBuilder::new(
            "{collection_name}",
            vec!["color".to_string(), "price".to_string()],
        )
        .points_selector(PointsIdsList {
            ids: vec![0.into(), 3.into(), 10.into()],
        })
        .wait(true),
    )
    .await?;
```


```typescript
client.deletePayload("{collection_name}", {
  keys: ["color", "price"],
  points: [0, 3, 100],
});
```
