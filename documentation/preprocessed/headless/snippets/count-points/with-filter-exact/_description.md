This code snippet demonstrates a POST request to count points based on specific filter conditions within a collection. The filter criteria include checking for points with a key "color" that matches the value "red" precisely. By setting the "exact" parameter to true, the count will consider only exact matches. This functionality is helpful for scenarios such as evaluating result sizes for faceted search, determining pagination numbers, and debugging query performance.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.CountAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("color", "red"),
	exact: true
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

client.Count(context.Background(), &qdrant.CountPoints{
	CollectionName: "midlib",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("color", "red"),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/count
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
    },
    "exact": true
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Common.Filter;

client
    .countAsync(
        "{collection_name}",
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true)
    .get();
```


```python
client.count(
    collection_name="{collection_name}",
    count_filter=models.Filter(
        must=[
            models.FieldCondition(key="color", match=models.MatchValue(value="red")),
        ]
    ),
    exact=True,
)
```


```rust
use qdrant_client::qdrant::{Condition, CountPointsBuilder, Filter};

client
    .count(
        CountPointsBuilder::new("{collection_name}")
            .filter(Filter::must([Condition::matches(
                "color",
                "red".to_string(),
            )]))
            .exact(true),
    )
    .await?;
```


```typescript
client.count("{collection_name}", {
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
  exact: true,
});
```
