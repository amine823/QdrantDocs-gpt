This code snippet allows you to perform a search operation on a collection by specifying a filter condition based on a nested field. In this case, the search is filtering points where the `country.name` field matches the value "Germany". This enables you to retrieve scroll points that meet the specified criteria.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(collectionName: "{collection_name}", filter: MatchKeyword("country.name", "Germany"));
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
		Should: []*qdrant.Condition{
			qdrant.NewMatch("country.name", "Germany"),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/scroll
{
    "filter": {
        "should": [
            {
                "key": "country.name",
                "match": {
                    "value": "Germany"
                }
            }
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
                    .addShould(matchKeyword("country.name", "Germany"))
                    .build())
            .build())
    .get();
```


```python
client.scroll(
    collection_name="{collection_name}",
    scroll_filter=models.Filter(
        should=[
            models.FieldCondition(
                key="country.name", match=models.MatchValue(value="Germany")
            ),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::should([
            Condition::matches("country.name", "Germany".to_string()),
        ])),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  filter: {
    should: [
      {
        key: "country.name",
        match: { value: "Germany" },
      },
    ],
  },
});
```
