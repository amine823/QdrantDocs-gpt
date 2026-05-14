This code represents a task to delete specific points from a collection. The API endpoint allows you to send a POST request to delete points with the specified indexes (0, 3, and 100) from a collection specified by its name.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeleteAsync(collectionName: "{collection_name}", ids: (ulong[])[0, 3, 100]);
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

client.Delete(context.Background(), &qdrant.DeletePoints{
	CollectionName: "{collection_name}",
	Points: qdrant.NewPointsSelector(
		qdrant.NewIDNum(0), qdrant.NewIDNum(3), qdrant.NewIDNum(100),
	),
})
```


```http
POST /collections/{collection_name}/points/delete
{
    "points": [0, 3, 100]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client.deleteAsync("{collection_name}", List.of(id(0), id(3), id(100)));
```


```python
client.delete(
    collection_name="{collection_name}",
    points_selector=models.PointIdsList(
        points=[0, 3, 100],
    ),
)
```


```rust
use qdrant_client::qdrant::{DeletePointsBuilder, PointsIdsList};

client
    .delete_points(
        DeletePointsBuilder::new("{collection_name}")
            .points(PointsIdsList {
                ids: vec![0.into(), 3.into(), 100.into()],
            })
            .wait(true),
    )
    .await?;
```


```typescript
client.delete("{collection_name}", {
  points: [0, 3, 100],
});
```
