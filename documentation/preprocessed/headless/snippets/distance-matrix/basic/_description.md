This code snippet represents a request to retrieve a distance matrix in pairwise format for points in a collection. The matrix will contain pairs of point IDs along with their corresponding scores based on a specific filtering condition (in this case, filtering by the color red). The request aims to return a limited number of samples that meet the filter criteria.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.SearchMatrixPairsAsync(
    collectionName: "{collection_name}",
    filter: MatchKeyword("color", "red"),
    sample: 10,
    limit: 2
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

sample := uint64(10)
limit := uint64(2)
res, err := client.SearchMatrixPairs(context.Background(), &qdrant.SearchMatrixPoints{
    CollectionName: "{collection_name}",
    Sample:         &sample,
    Limit:          &limit,
    Filter: &qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatch("color", "red"),
        },
    },
})
```


```http
POST /collections/{collection_name}/points/search/matrix/pairs
{
    "sample": 10,
    "limit": 2,
    "filter": {
        "must": {
            "key": "color",
            "match": { "value": "red" }
        }
    }  
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.SearchMatrixPoints;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .searchMatrixPairsAsync(
        SearchMatrixPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setFilter(Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
            .setSample(10)
            .setLimit(2)
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.search_matrix_pairs(
    collection_name="{collection_name}",
    sample=10,
    limit=2,
    query_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="color", match=models.MatchValue(value="red")
            ),
        ]
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, Filter, SearchMatrixPointsBuilder};

client
    .search_matrix_pairs(
        SearchMatrixPointsBuilder::new("collection_name")
           .filter(Filter::must(vec![Condition::matches(
               "color",
               "red".to_string(),
           )]))
           .sample(10)
           .limit(2),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.searchMatrixPairs("{collection_name}", {
    filter: {
        must: [
            {
                key: "color",
                match: {
                    value: "red",
                },
            },
        ],
    },
    sample: 10,
    limit: 2,
});
```
