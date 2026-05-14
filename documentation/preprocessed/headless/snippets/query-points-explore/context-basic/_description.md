This code snippet showcases a context-based approach for performing a search operation on a collection of points. The search involves specifying positive and negative context points along with a limit on the number of results to be returned. By using a context score derived from the triplet-loss concept, the search is guided towards areas with fewer negative examples. This method allows for a more diverse and constrained result set, rather than only focusing on a single point. The approach can be utilized not just for general searching but also for recommendation systems by adapting it to specific use cases.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
  collectionName: "{collection_name}",
  query: new ContextInput {
    Pairs = {
      new ContextInputPair {
        Positive = 100,
          Negative = 718
      },
      new ContextInputPair {
        Positive = 200,
          Negative = 300
      },
    }
  },
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
    Query: qdrant.NewQueryContext(&qdrant.ContextInput{
        Pairs: []*qdrant.ContextInputPair{
            {
                Positive: qdrant.NewVectorInputID(qdrant.NewIDNum(100)),
                Negative: qdrant.NewVectorInputID(qdrant.NewIDNum(718)),
            },
            {
                Positive: qdrant.NewVectorInputID(qdrant.NewIDNum(200)),
                Negative: qdrant.NewVectorInputID(qdrant.NewIDNum(300)),
            },
        },
    }),
})
```


```http
POST /collections/{collection_name}/points/query
{
  "query": {
    "context": [
      {
        "positive": 100,
        "negative": 718
      },
      {
        "positive": 200,
        "negative": 300
      }
    ]
  },
  "limit": 10
}
```


```java
import static io.qdrant.client.QueryFactory.context;
import static io.qdrant.client.VectorInputFactory.vectorInput;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.ContextInput;
import io.qdrant.client.grpc.Points.ContextInputPair;
import io.qdrant.client.grpc.Points.QueryPoints;
import java.util.List;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(QueryPoints.newBuilder()
        .setCollectionName("{collection_name}")
        .setQuery(context(ContextInput.newBuilder()
                .addAllPairs(List.of(
                        ContextInputPair.newBuilder()
                                .setPositive(vectorInput(100))
                                .setNegative(vectorInput(718))
                                .build(),
                        ContextInputPair.newBuilder()
                                .setPositive(vectorInput(200))
                                .setNegative(vectorInput(300))
                                .build()))
                .build()))
        .setLimit(10)
        .build()).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

discover_queries = [
    models.QueryRequest(
        query=models.ContextQuery(
            context=[
                models.ContextPair(
                    positive=100,
                    negative=718,
                ),
                models.ContextPair(
                    positive=200,
                    negative=300,
                ),
            ],
        ),
        limit=10,
    ),
]

client.query_batch_points(
    collection_name="{collection_name}", requests=discover_queries
)
```


```rust
use qdrant_client::qdrant::{ContextInputBuilder, QueryPointsBuilder};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}").query(
            ContextInputBuilder::default()
                .add_pair(100, 718)
                .add_pair(200, 300)
                .build(),
        ),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    query: {
        context: [
            {
                positive: 100,
                negative: 718,
            },
            {
                positive: 200,
                negative: 300,
            },
        ]
    },
    limit: 10,
});
```
