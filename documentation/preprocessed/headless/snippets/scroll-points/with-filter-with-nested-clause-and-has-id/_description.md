This code snippet demonstrates a POST request to filter data in a specific collection. The request includes a filter specifying nested conditions on elements within the data array. The nested conditions check for elements with a 'diet' key that matches 'meat' in the 'food' key and 'true' in the 'likes' key. The filter also includes a condition to check if the data has an ID of '1'. It notes that the 'has_id' condition is not supported within the nested filter and should be placed in an adjacent 'must' clause if needed.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: Nested("diet", MatchKeyword("food", "meat") & Match("likes", true)) & HasId(1)
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
			qdrant.NewHasID(qdrant.NewIDNum(1)),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/scroll
{
   "filter":{
      "must":[
         {
            "nested":{
               "key":"diet",
               "filter":{
                  "must":[
                     {
                        "key":"food",
                        "match":{
                           "value":"meat"
                        }
                     },
                     {
                        "key":"likes",
                        "match":{
                           "value":true
                        }
                     }
                  ]
               }
            }
         },
         {
            "has_id":[
               1
            ]
         }
      ]
   }
}
```


```java
import static io.qdrant.client.ConditionFactory.hasId;
import static io.qdrant.client.ConditionFactory.match;
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.ConditionFactory.nested;
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
                    .addMust(
                        nested(
                            "diet",
                            Filter.newBuilder()
                                .addAllMust(
                                    List.of(
                                        matchKeyword("food", "meat"), match("likes", true)))
                                .build()))
                    .addMust(hasId(id(1)))
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
            ),
            models.HasIdCondition(has_id=[1]),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, NestedCondition, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::must([
            NestedCondition {
                key: "diet".to_string(),
                filter: Some(Filter::must([
                    Condition::matches("food", "meat".to_string()),
                    Condition::matches("likes", true),
                ])),
            }
            .into(),
            Condition::has_id([1]),
        ])),
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
      {
        has_id: [1],
      },
    ],
  },
});
```
