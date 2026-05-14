This code snippet demonstrates an alternative way to specify and remove certain points from a collection by filtering based on a specific key-value pair. In this case, the filter is set to remove points with the key "color" that match the value "red".

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.DeleteAsync(collectionName: "{collection_name}", filter: MatchKeyword("color", "red"));
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
	Points: qdrant.NewPointsSelectorFilter(
		&qdrant.Filter{
			Must: []*qdrant.Condition{
				qdrant.NewMatch("color", "red"),
			},
		},
	),
})
```


```http
POST /collections/{collection_name}/points/delete
{
    "filter": {
        "must": [
            {
                "key": "color",
                "match": {
                    "value": "red"
                }
            }
        ]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Common.Filter;

client
    .deleteAsync(
        "{collection_name}",
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
    .get();
```


```python
client.delete(
    collection_name="{collection_name}",
    points_selector=models.FilterSelector(
        filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="color",
                    match=models.MatchValue(value="red"),
                ),
            ],
        )
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, DeletePointsBuilder, Filter};

client
    .delete_points(
        DeletePointsBuilder::new("{collection_name}")
            .points(Filter::must([Condition::matches(
                "color",
                "red".to_string(),
            )]))
            .wait(true),
    )
    .await?;
```


```typescript
client.delete("{collection_name}", {
  filter: {
    must: [
      {
        key: "color",
        match: {
          value: "red",
        },
      },
    ],
  },
});
```
