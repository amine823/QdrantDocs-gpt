This code snippet demonstrates a way to combine multiple clauses to filter data. In this example, the code shows how to filter data based on a specific city value (in this case, "London") while excluding another specific value (in this case, the color "red"). The specified clauses work together in the filter to refine the results accordingly.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: MatchKeyword("city", "London") & !MatchKeyword("color", "red")
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

client.Scroll(context.Background(), &qdrant.ScrollPoints{
	CollectionName: "{collection_name}",
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("city", "London"),
		},
		MustNot: []*qdrant.Condition{
			qdrant.NewMatch("color", "red"),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must": [
            { "key": "city", "match": { "value": "London" } }
        ],
        "must_not": [
            { "key": "color", "match": { "value": "red" } }
        ]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(matchKeyword("city", "London"))
                    .addMustNot(matchKeyword("color", "red"))
                    .build())
            .build())
    .get();
```


```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[
            models.FieldCondition(key="city", match=models.MatchValue(value="London")),
        ],
        must_not=[
            models.FieldCondition(key="color", match=models.MatchValue(value="red")),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter {
            must: vec![Condition::matches("city", "London".to_string())],
            must_not: vec![Condition::matches("color", "red".to_string())],
            ..Default::default()
        }),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [
      {
        key: "city",
        match: { value: "London" },
      },
    ],
    must_not: [
      {
        key: "color",
        match: { value: "red" },
      },
    ],
  },
});
```
