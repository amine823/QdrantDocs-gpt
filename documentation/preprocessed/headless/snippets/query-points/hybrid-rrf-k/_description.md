This code snippet demonstrates a hybrid search functionality where you can query points from a collection using both sparse and dense vectors. The code showcases how to combine the results of multiple queries with different vector representations using Reciprocal Rank Fusion (RRF), parametrized by constant k. RRF boosts results that are closer to the top in multiple queries. This hybrid search approach can be useful for obtaining semantic and specific word matching results simultaneously.


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
  collectionName: "{collection_name}",
  prefetch: new List<PrefetchQuery>
  {
	  // 2+ prefetches here
  },
  query: new Rrf
  {
	  K = 60,
  }
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
	Prefetch:       []*qdrant.PrefetchQuery{
		// 2+ prefetches here
	},
	Query: qdrant.NewQueryRRF(
		&qdrant.Rrf{
			K: qdrant.PtrOf(uint32(60)),
		}),
})
```


```http
POST /collections/{collection_name}/points/query
{
    "prefetch": [
      // 2+ prefetches here
    ],
    "query": { "rrf": {"k": 60 } }, // <--- parameterized reciprocal rank fusion
    "limit": 10
}
```


```java
import static io.qdrant.client.QueryFactory.rrf;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.PrefetchQuery;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.Rrf;
import java.util.List;

QdrantClient client = new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("{collection_name}")
            // .addPrefetch(...) <┐
            // .addPrefetch(...) <┴─ 2+ prefetches here
            .setQuery(rrf(Rrf.newBuilder().setK(60).build()))
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    prefetch=[
        # 2+ prefetches here
    ],
    query=models.RrfQuery(rrf=models.Rrf(k=60)),
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{RrfBuilder, Query, QueryPointsBuilder};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.query(
    QueryPointsBuilder::new("{collection_name}")
        // .add_prefetch(...)  <┐
        // .add_prefetch(...)  <┴─ 2+ prefetches here
        .query(Query::new_rrf(RrfBuilder::with_k(60)))
).await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    prefetch: [
      // 2+ prefetches here
    ],
    query: { rrf: { k: 60 } },
});
```
