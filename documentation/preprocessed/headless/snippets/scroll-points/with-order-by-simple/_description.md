Sort your collection points by a custom payload key when using the scroll API. This feature enables you to order and retrieve the points based on a specific payload key, in this case, the `"timestamp"` field. Just keep in mind that for this to work efficiently, Qdrant needs a payload index supporting range filtering conditions.

```csharp
await client.ScrollAsync("{collection_name}", limit: 15, orderBy: "timestamp");
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Limit:          qdrant.PtrOf(uint32(15)),
	OrderBy: &qdrant.OrderBy{
		Key: "timestamp",
	},
})
```


```http
POST /collections/{collection_name}/points/scroll
{
    "limit": 15,
    "order_by": "timestamp", // <-- this!
}
```


```java
import io.qdrant.client.grpc.Points.OrderBy;
import io.qdrant.client.grpc.Points.ScrollPoints;

client.scrollAsync(ScrollPoints.newBuilder()
  .setCollectionName("{collection_name}")
  .setLimit(15)
  .setOrderBy(OrderBy.newBuilder().setKey("timestamp").build())
  .build()).get();
```


```python
client.scroll(
    collection_name="{collection_name}",
    limit=15,
    order_by="timestamp", # <-- this!
)
```


```rust
use qdrant_client::qdrant::{OrderByBuilder, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}")
            .limit(15)
            .order_by(OrderByBuilder::new("timestamp")),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  limit: 15,
  order_by: "timestamp", // <-- this!
});
```
