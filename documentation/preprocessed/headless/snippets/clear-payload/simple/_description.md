This code snippet demonstrates a functionality to clear payload keys from specific points by providing a list of point identifiers.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ClearPayloadAsync(collectionName: "{collection_name}", ids: new ulong[] { 0, 3, 100 });
```


```go
import (
    "context"

    "github.com/qdrant/go-client/qdrant"
)

client.ClearPayload(context.Background(), &qdrant.ClearPayloadPoints{
    CollectionName: "{collection_name}",
    Points: qdrant.NewPointsSelector(
        qdrant.NewIDNum(0),
        qdrant.NewIDNum(3)),
})
```


```http
POST /collections/{collection_name}/points/payload/clear
{
    "points": [0, 3, 100]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .clearPayloadAsync("{collection_name}", List.of(id(0), id(3), id(100)), true, null, null)
    .get();
```


```python
client.clear_payload(
    collection_name="{collection_name}",
    points_selector=[0, 3, 100],
)
```


```rust
use qdrant_client::qdrant::{ClearPayloadPointsBuilder, PointsIdsList};

client
    .clear_payload(
        ClearPayloadPointsBuilder::new("{collection_name}")
            .points(PointsIdsList {
                ids: vec![0.into(), 3.into(), 10.into()],
            })
            .wait(true),
    )
    .await?;
```


```typescript
client.clearPayload("{collection_name}", {
  points: [0, 3, 100],
});
```
