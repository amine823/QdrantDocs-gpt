Faceting is a feature that allows you to retrieve counts of unique values for a specific field within your data. In this case, the snippet demonstrates a request to generate facet counts for a field named "size" in a collection. The facet counts are filtered based on a condition where the "color" must match the value "red". This technique can help you understand the distribution of values in your data and assess the impact of applying filters based on specific values.

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.FacetAsync(
    "{collection_name}",
    key: "size",
    filter: MatchKeyword("color", "red")
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

res, err := client.Facet(context.Background(), &qdrant.FacetCounts{
    CollectionName: "{collection_name}",
    Key:            "size",
        Filter: &qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatch("color", "red"),
        },
    },
})
```


```http
POST /collections/{collection_name}/facet
{
    "key": "size",
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
import io.qdrant.client.grpc.Points;

QdrantClient client = new QdrantClient(
                QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .facetAsync(
        Points.FacetCounts.newBuilder()
            .setCollectionName("{collection_name}")
            .setKey("size")
            .setFilter(Filter.newBuilder().addMust(matchKeyword("color", "red")).build())
            .build())
        .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.facet(
    collection_name="{collection_name}",
    key="size",
    facet_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="color",
                match=models.MatchValue(value="red"),
            )
        ]
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, FacetCountsBuilder, Filter};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .facet(
         FacetCountsBuilder::new("{collection_name}", "size")
             .limit(10)
             .filter(Filter::must(vec![Condition::matches(
                 "color",
                 "red".to_string(),
             )])),
     )
     .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.facet("{collection_name}", {
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
    key: "size",
});
```
