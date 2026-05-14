This code snippet demonstrates how to perform a POST request to filter items based on specific criteria. The filter specifies that the collection should not include points where the city is "London" and the color is "red". The conditions are nested within each other to create complex filtering logic.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: new Filter { MustNot = { MatchKeyword("city", "London") & MatchKeyword("color", "red") } }
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
			qdrant.NewFilterAsCondition(&qdrant.Filter{
				Must: []*qdrant.Condition{
					qdrant.NewMatch("city", "London"),
					qdrant.NewMatch("color", "red"),
				},
			}),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "must_not": [
            {
                "must": [
                    { "key": "city", "match": { "value": "London" } },
                    { "key": "color", "match": { "value": "red" } }
                ]
            }
        ]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.filter;
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
                    .addMustNot(
                        filter(
                            Filter.newBuilder()
                                .addAllMust(
                                    List.of(
                                        matchKeyword("city", "London"),
                                        matchKeyword("color", "red")))
                                .build()))
                    .build())
            .build())
    .get();
```


```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must_not=[
            models.Filter(
                must=[
                    models.FieldCondition(
                        key="city", match=models.MatchValue(value="London")
                    ),
                    models.FieldCondition(
                        key="color", match=models.MatchValue(value="red")
                    ),
                ],
            ),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must_not([Filter::must(
            [
                Condition::matches("city", "London".to_string()),
                Condition::matches("color", "red".to_string()),
            ],
        )
        .into()])),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  filter: {
    must_not: [
      {
        must: [
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
    ],
  },
});
```
