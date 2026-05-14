Retrieve vectors from a collection by specifying a query and applying a filter to only retrieve vectors that have a `group_id` matching a specific value like "user_1". You can also set a limit on the number of vectors to be returned.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
	collectionName: "{collection_name}",
	query: new float[] { 0.1f, 0.1f, 0.9f },
	filter: MatchKeyword("group_id", "user_1"),
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
	Query:          qdrant.NewQuery(0.1, 0.1, 0.9),
	Filter: &qdrant.Filter{
		Must: []*qdrant.Condition{
			qdrant.NewMatch("group_id", "user_1"),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/query
{
    "query": [0.1, 0.1, 0.9],
    "filter": {
        "must": [
            {
                "key": "group_id",
                "match": {
                    "value": "user_1"
                }
            }
        ]
    },
    "limit": 10
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

client.queryAsync(
        QueryPoints.newBuilder()
                .setCollectionName("{collection_name}")
                .setFilter(
                        Filter.newBuilder().addMust(matchKeyword("group_id", "user_1")).build())
                .setQuery(nearest(0.1f, 0.1f, 0.9f))
                .setLimit(10)
                .build())
        .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=[0.1, 0.1, 0.9],
    query_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="group_id",
                match=models.MatchValue(
                    value="user_1",
                ),
            )
        ]
    ),
    limit=10,
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, QueryPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(vec![0.1, 0.1, 0.9])
            .limit(10)
            .filter(Filter::must([Condition::matches(
                "group_id",
                "user_1".to_string(),
            )])),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    query: [0.1, 0.1, 0.9],
    filter: {
        must: [{ key: "group_id", match: { value: "user_1" } }],
    },
    limit: 10,
});
```
