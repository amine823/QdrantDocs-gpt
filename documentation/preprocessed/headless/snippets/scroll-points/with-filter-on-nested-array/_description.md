This code snippet showcases a filtering setup that allows searching for specific values within nested arrays. In this case, it focuses on retrieving data where the population of cities within a country is equal to or greater than a certain value. The notation `country.cities[].population` targets these nested values efficiently.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.ScrollAsync(
	collectionName: "{collection_name}",
	filter: Range("country.cities[].population", new Qdrant.Client.Grpc.Range { Gte = 9.0 })
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
		Should: []*qdrant.Condition{
			qdrant.NewRange("country.cities[].population", &qdrant.Range{
				Gte: qdrant.PtrOf(9.0),
			}),
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
                "key": "country.cities[].population",
                "range": {
                    "gte": 9.0,
                }
            }
        ]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.range;

import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Common.Range;
import io.qdrant.client.grpc.Points.ScrollPoints;

client
    .scrollAsync(
        ScrollPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(
                Filter.newBuilder()
                    .addShould(
                        range(
                            "country.cities[].population",
                            Range.newBuilder().setGte(9.0).build()))
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
                key="country.cities[].population",
                range=models.Range(
                    gt=None,
                    gte=9.0,
                    lt=None,
                    lte=None,
                ),
            ),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, Range, ScrollPointsBuilder};

client
    .scroll(
        ScrollPointsBuilder::new("{collection_name}").filter(Filter::should([
            Condition::range(
                "country.cities[].population",
                Range {
                    gte: Some(9.0),
                    ..Default::default()
                },
            ),
        ])),
    )
    .await?;
```


```typescript
client.scroll("{collection_name}", {
  filter: {
    should: [
      {
        key: "country.cities[].population",
        range: {
          gt: null,
          gte: 9.0,
          lt: null,
          lte: null,
        },
      },
    ],
  },
});
```
