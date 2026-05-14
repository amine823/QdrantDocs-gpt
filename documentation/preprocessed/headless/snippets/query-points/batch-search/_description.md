This code snippet demonstrates the batch search feature of a system. The batch search API allows you to send multiple search queries in a single request. Each search query includes a set of criteria to filter results and a limit on the number of expected results. By batching search requests together, the system can optimize processing by sharing intermediary results when queries have the same filters. This approach helps reduce network connections and improve overall efficiency, especially for complex filters. To use the batch search API, package your search requests together with the desired criteria.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

var filter = MatchKeyword("city", "London");

var queries = new List<QueryPoints>
{
    new()
    {
        CollectionName = "{collection_name}",
        Query = new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
        Filter = filter,
        Limit = 3
    },
    new()
    {
        CollectionName = "{collection_name}",
        Query = new float[] { 0.5f, 0.3f, 0.2f, 0.3f },
        Filter = filter,
        Limit = 3
    }
};

await client.QueryBatchAsync(collectionName: "{collection_name}", queries: queries);
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

filter := qdrant.Filter{
	Must: []*qdrant.Condition{
		qdrant.NewMatch("city", "London"),
	},
}

client.QueryBatch(context.Background(), &qdrant.QueryBatchPoints{
	CollectionName: "{collection_name}",
	QueryPoints: []*qdrant.QueryPoints{
		{
			CollectionName: "{collection_name}",
			Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
			Filter:         &filter,
		},
		{
			CollectionName: "{collection_name}",
			Query:          qdrant.NewQuery(0.5, 0.3, 0.2, 0.3),
			Filter:         &filter,
		},
	},
})
```


```http
POST /collections/{collection_name}/points/query/batch
{
    "searches": [
        {
            "query": [0.2, 0.1, 0.9, 0.7],
            "filter": {
                "must": [
                    {
                        "key": "city",
                        "match": {
                            "value": "London"
                        }
                    }
                ]
            },
            "limit": 3
        },
        {
            "query": [0.5, 0.3, 0.2, 0.3],
            "filter": {
                "must": [
                    {
                        "key": "city",
                        "match": {
                            "value": "London"
                        }
                    }
                ]
            },
            "limit": 3
        }
    ]
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.QueryPoints;
import java.util.List;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

Filter filter = Filter.newBuilder().addMust(matchKeyword("city", "London")).build();

List<QueryPoints> searches = List.of(
        QueryPoints.newBuilder()
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .setFilter(filter)
                .setLimit(3)
                .build(),
        QueryPoints.newBuilder()
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .setFilter(filter)
                .setLimit(3)
                .build());

client.queryBatchAsync("{collection_name}", searches).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

filter_ = models.Filter(
    must=[
        models.FieldCondition(
            key="city",
            match=models.MatchValue(
                value="London",
            ),
        )
    ]
)

search_queries = [
    models.QueryRequest(query=[0.2, 0.1, 0.9, 0.7], filter=filter_, limit=3),
    models.QueryRequest(query=[0.5, 0.3, 0.2, 0.3], filter=filter_, limit=3),
]

client.query_batch_points(collection_name="{collection_name}", requests=search_queries)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, QueryBatchPointsBuilder, QueryPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let filter = Filter::must([Condition::matches("city", "London".to_string())]);

let searches = vec![
    QueryPointsBuilder::new("{collection_name}")
        .query(vec![0.1, 0.2, 0.3, 0.4])
        .limit(3)
        .filter(filter.clone())
        .build(),
    QueryPointsBuilder::new("{collection_name}")
        .query(vec![0.5, 0.3, 0.2, 0.3])
        .limit(3)
        .filter(filter)
        .build(),
];

client
        .query_batch(QueryBatchPointsBuilder::new("{collection_name}", searches))
        .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

const filter = {
    must: [
        {
            key: "city",
            match: {
                value: "London",
            },
        },
    ],
};

const searches = [
    {
        query: [0.2, 0.1, 0.9, 0.7],
        filter,
        limit: 3,
    },
    {
        query: [0.5, 0.3, 0.2, 0.3],
        filter,
        limit: 3,
    },
];

client.queryBatch("{collection_name}", {
    searches,
});
```
