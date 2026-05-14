This code snippet demonstrates how to use a filter to exclude certain points when scrolling through a collection. In this case, points with the key "city" set to "London" and the key "color" set to "red" are excluded from the results.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

// The ! operator negates the condition(must not)
await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: !(MatchKeyword("city", "London") & MatchKeyword("color", "red"))
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
		MustNot: []*qdrant.Condition{
			qdrant.NewMatch("city", "London"),
			qdrant.NewMatch("color", "red"),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must_not": [
            { "key": "city", "match": { "value": "London" } },
            { "key": "color", "match": { "value": "red" } }
        ]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;
import java.util.List;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addAllMustNot(
                        List.of(matchKeyword("city", "London"), matchKeyword("color", "red")))
                    .build())
            .build())
    .get();
```


```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must_not=[
            models.FieldCondition(key="city", match=models.MatchValue(value="London")),
            models.FieldCondition(key="color", match=models.MatchValue(value="red")),
        ]
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must_not([
            Condition::matches("city", "london".to_string()),
            Condition::matches("color", "red".to_string()),
        ])),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  filter: {
    must_not: [
      {
        key: "city",
        match: { value: "London" },
      },
      {
        key: "color",
        match: { value: "red" },
      },
    ],
  },
});
```
