This code snippet demonstrates a POST request that filters through a collection of points based on nested conditions. It showcases how to filter points based on specific criteria within nested objects. In this case, the filter looks for points where a nested object with the key "diet" contains sub-objects that match the conditions specified for "food" and "likes". The snippet illustrates the concept of nested object filters, enabling the querying of arrays of objects independently.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: Nested("diet", MatchKeyword("food", "meat") & Match("likes", true))
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
			qdrant.NewNestedFilter("diet", &qdrant.Filter{
				Must: []*qdrant.Condition{
					qdrant.NewMatch("food", "meat"),
					qdrant.NewMatchBool("likes", true),
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
        "must": [{
            "nested": {
                "key": "diet",
                "filter":{
                    "must": [
                        {
                            "key": "food",
                            "match": {
                                "value": "meat"
                            }
                        },
                        {
                            "key": "likes",
                            "match": {
                                "value": true
                            }
                        }
                    ]
                }
            }
        }]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.ConditionFactory.nested;

import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.ScrollPoints;
import java.util.List;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addMust(
                        nested(
                            "diet",
                            Filter.newBuilder()
                                .addAllMust(
                                    List.of(
                                        matchKeyword("food", "meat"), match("likes", true)))
                                .build()))
                    .build())
            .build())
    .get();
```


```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        must=[
            models.NestedCondition(
                nested=models.Nested(
                    key="diet",
                    filter=models.Filter(
                        must=[
                            models.FieldCondition(
                                key="food", match=models.MatchValue(value="meat")
                            ),
                            models.FieldCondition(
                                key="likes", match=models.MatchValue(value=True)
                            ),
                        ]
                    ),
                )
            )
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, NestedCondition, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must([NestedCondition {
            key: "diet".to_string(),
            filter: Some(Filter::must([
                Condition::matches("food", "meat".to_string()),
                Condition::matches("likes", true),
            ])),
        }
        .into()])),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  filter: {
    must: [
      {
        nested: {
          key: "diet",
          filter: {
            must: [
              {
                key: "food",
                match: { value: "meat" },
              },
              {
                key: "likes",
                match: { value: true },
              },
            ],
          },
        },
      },
    ],
  },
});
```
