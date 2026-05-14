This code snippet demonstrates a discovery search functionality for querying points within a specific collection. The search query includes a target vector and contextual positive and negative examples. The search is constrained to a vector space for performing the search operation. The provided code showcases a POST request to query points based on specified parameters such as target vector values, positive and negative examples within the context, and a limit on the number of results to be returned.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
    collectionName: "{collection_name}",
    query: new DiscoverInput {
        Target = new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
        Context = new ContextInput {
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
    Query: qdrant.NewQueryDiscover(&qdrant.DiscoverInput{
        Target: qdrant.NewVectorInput(0.2, 0.1, 0.9, 0.7),
        Context: &qdrant.ContextInput{
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
        },
    }),
})
```


```http
POST /collections/{collection_name}/points/query
{
  "query": {
    "discover": {
      "target": [0.2, 0.1, 0.9, 0.7],
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
    }
  },
  "limit": 10
}
```


```java
import static io.qdrant.client.QueryFactory.discover;
import static io.qdrant.client.VectorInputFactory.vectorInput;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.ContextInput;
import io.qdrant.client.grpc.Points.ContextInputPair;
import io.qdrant.client.grpc.Points.DiscoverInput;
import io.qdrant.client.grpc.Points.QueryPoints;
import java.util.List;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(QueryPoints.newBuilder()
        .setCollectionName("{collection_name}")
        .setQuery(discover(DiscoverInput.newBuilder()
                .setTarget(vectorInput(0.2f, 0.1f, 0.9f, 0.7f))
                .setContext(ContextInput.newBuilder()
                        .addAllPairs(List.of(
                                ContextInputPair.newBuilder()
                                        .setPositive(vectorInput(100))
                                        .setNegative(vectorInput(718))
                                        .build(),
                                ContextInputPair.newBuilder()
                                        .setPositive(vectorInput(200))
                                        .setNegative(vectorInput(300))
                                        .build()))
                        .build())
                .build()))
        .setLimit(10)
        .build()).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

discover_queries = [
    models.QueryRequest(
        query=models.DiscoverQuery(
            discover=models.DiscoverInput(
                target=[0.2, 0.1, 0.9, 0.7],
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
            )
        ),
        limit=10,
    ),
]

client.query_batch_points(
    collection_name="{collection_name}", requests=discover_queries
)
```


```rust
use qdrant_client::qdrant::{ContextInputBuilder, DiscoverInputBuilder, QueryPointsBuilder};

client
    .query(
        QueryPointsBuilder::new("{collection_name}").query(
            DiscoverInputBuilder::new(
                vec![0.2, 0.1, 0.9, 0.7],
                ContextInputBuilder::default()
                    .add_pair(100, 718)
                    .add_pair(200, 300),
            )
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
        discover: {
            target: [0.2, 0.1, 0.9, 0.7],
            context: [
                {
                    positive: 100,
                    negative: 718,
                },
                {
                    positive: 200,
                    negative: 300,
                },
            ],
        }
    },
    limit: 10,
});
```
