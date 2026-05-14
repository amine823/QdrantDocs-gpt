This code snippet represents a method for retrieving points by their ids from a collection. The function allows users to specify the ids of the points to be retrieved as part of a POST request to the specified endpoint. The provided ids are an array of integers, indicating the specific points to retrieve.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.RetrieveAsync(
	collectionName: "{collection_name}",
	ids: [0, 30, 100],
	withPayload: false,
	withVectors: false
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

client.Get(context.Background(), &qdrant.GetPoints{
	CollectionName: "{collection_name}",
	Ids: []*qdrant.PointId{
		qdrant.NewIDNum(0), qdrant.NewIDNum(3), qdrant.NewIDNum(100),
	},
})
```


```http
POST /collections/{collection_name}/points
{
    "ids": [0, 3, 100]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .retrieveAsync("{collection_name}", List.of(id(0), id(30), id(100)), false, false, null)
    .get();
```


```python
client.retrieve(
    collection_name="{collection_name}",
    ids=[0, 3, 100],
)
```


```rust
use qdrant_client::qdrant::GetPointsBuilder;

client
    .get_points(GetPointsBuilder::new(
        "{collection_name}",
        vec![0.into(), 30.into(), 100.into()],
    ))
    .await?;
```


```typescript
client.retrieve("{collection_name}", {
  ids: [0, 3, 100],
});
```
