This code snippet demonstrates a query that filters data based on specific IDs. By providing a list of IDs, the query filters out results that do not match these specific IDs. This type of filtering can be beneficial when there is a need to exclude certain data points or focus the search on a predefined set of IDs.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(collectionName: "{collection_name}", filter: HasId([1, 3, 5, 7, 9, 11]));
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
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewHasID(
				qdrant.NewIDNum(1),
				qdrant.NewIDNum(3),
				qdrant.NewIDNum(5),
				qdrant.NewIDNum(7),
				qdrant.NewIDNum(9),
				qdrant.NewIDNum(11),
			),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [
            { "has_id": [1,3,5,7,9,11] }
        ]
    }
    ...
}
```


```java
import static io.qdrant.client.ConditionFactory.hasId;
import static io.qdrant.client.PointIdFactory.id;

import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;
import java.util.List;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(hasId(List.of(id(1), id(3), id(5), id(7), id(9), id(11))))
                    .build())
            .build())
    .get();
```


```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[
            models.HasIdCondition(has_id=[1, 3, 5, 7, 9, 11]),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}")
            .filter(Filter::must([Condition::has_id([1, 3, 5, 7, 9, 11])])),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [
      {
        has_id: [1, 3, 5, 7, 9, 11],
      },
    ],
  },
});
```
