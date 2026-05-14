This code snippet showcases a scenario where a collection of points can be queried with a focus on the contents of the payload data associated with each point. The example demonstrates the use of dense vectors as queries along with filters based on payload fields such as 'color' with values like "red" or "green". Additionally, the results can be limited and ordered based on a specific payload field such as "price". This functionality allows for more refined and customized querying based on both vector similarity and payload content.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
  collectionName: "{collection_name}",
  prefetch: new List <PrefetchQuery> {
    new() {
      Query = new float[] {
          0.01f, 0.45f, 0.67f
        },
        Filter = MatchKeyword("color", "red"),
        Limit = 10
    },
    new() {
      Query = new float[] {
          0.01f, 0.45f, 0.67f
        },
        Filter = MatchKeyword("color", "green"),
        Limit = 10
    }
  },
  query: (OrderBy) "price",
  limit: 10
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

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Prefetch: []*qdrant.PrefetchQuery{
		{
			Query: qdrant.NewQuery(0.01, 0.45, 0.67),
			Filter: &qdrant.Filter{
				Must: []*qdrant.Condition{
					qdrant.NewMatch("color", "red"),
				},
			},
		},
		{
			Query: qdrant.NewQuery(0.01, 0.45, 0.67),
			Filter: &qdrant.Filter{
				Must: []*qdrant.Condition{
					qdrant.NewMatch("color", "green"),
				},
			},
		},
	},
	Query: qdrant.NewQueryOrderBy(&qdrant.OrderBy{
		Key: "price",
	}),
})
```


```http
POST /collections/{collection_name}/points/query
{
    "prefetch": [
        {
            "query": [0.01, 0.45, 0.67, ...], // <-- dense vector
            "filter": {
                "must": {
                    "key": "color",
                    "match": {
                        "value": "red"
                    }
                }
            },
            "limit": 10
        },
        {
            "query": [0.01, 0.45, 0.67, ...], // <-- dense vector
            "filter": {
                "must": {
                    "key": "color",
                    "match": {
                        "value": "green"
                    }
                }
            },
            "limit": 10
        }
    ],
    "query": { "order_by": "price" }
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.QueryFactory.orderBy;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.PrefetchQuery;
import io.qdrant.client.grpc.Points.QueryPoints;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .addPrefetch(
                PrefetchQuery.newBuilder()
                    .setQuery(nearest(0.01f, 0.45f, 0.67f))
                    .setFilter(
                        Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
                    .setLimit(10)
                    .build())
            .addPrefetch(
                PrefetchQuery.newBuilder()
                    .setQuery(nearest(0.01f, 0.45f, 0.67f))
                    .setFilter(
                        Filter.newBuilder().addMust(matchKeyword("color", "green")).build())
                    .setLimit(10)
                    .build())
            .setQuery(orderBy("price"))
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    prefetch=[
        models.Prefetch(
            query=[0.01, 0.45, 0.67],  # <-- dense vector
            filter=models.Filter(
                must=models.FieldCondition(
                    key="color",
                    match=models.MatchValue(value="red"),
                ),
            ),
            limit=10,
        ),
        models.Prefetch(
            query=[0.01, 0.45, 0.67],  # <-- dense vector
            filter=models.Filter(
                must=models.FieldCondition(
                    key="color",
                    match=models.MatchValue(value="green"),
                ),
            ),
            limit=10,
        ),
    ],
    query=models.OrderByQuery(order_by="price"),
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Filter, PrefetchQueryBuilder, Query, QueryPointsBuilder};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.query(
    QueryPointsBuilder::new("{collection_name}")
        .add_prefetch(PrefetchQueryBuilder::default()
            .query(Query::new_nearest(vec![0.01, 0.45, 0.67]))
            .filter(Filter::must([Condition::matches(
                "color",
                "red".to_string(),
            )]))
            .limit(10u64)
        )
        .add_prefetch(PrefetchQueryBuilder::default()
            .query(Query::new_nearest(vec![0.01, 0.45, 0.67]))
            .filter(Filter::must([Condition::matches(
                "color",
                "green".to_string(),
            )]))
            .limit(10u64)
        )
        .query(Query::new_order_by("price"))
).await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    prefetch: [
        {
            query: [0.01, 0.45, 0.67], // <-- dense vector
            filter: {
                must: {
                    key: 'color',
                    match: {
                        value: 'red',
                    },
                }
            },
            limit: 10,
        },
        {
            query: [0.01, 0.45, 0.67], // <-- dense vector
            filter: {
                must: {
                    key: 'color',
                    match: {
                        value: 'green',
                    },
                }
            },
            limit: 10,
        },
    ],
    query: {
        order_by: 'price',
    },
});
```
