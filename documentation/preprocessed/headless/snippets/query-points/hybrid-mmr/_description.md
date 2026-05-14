This code snippet demonstrates Maximal Marginal Relevance (MMR) query functionality. MMR is a technique used to balance relevance and diversity in search results by combining similarity scores with a diversity penalty. The `candidates_limit` parameter sets the number of nearest neighbors to consider for MMR. The `diversity` parameter controls this balance: values closer to 0.0 prioritize relevance, while values closer to 1.0 prioritize diversity. This approach helps avoid redundant results by penalizing documents that are too similar to already selected ones, making it particularly useful for recommendation systems and diverse result sets.


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
    collectionName: "{collection_name}",
    query: (
        new float[] { 0.01f, 0.45f, 0.67f },
        new Mmr
        {
            Diversity = 0.5f,         // 0.0 - relevance; 1.0 - diversity
            CandidatesLimit = 100     // Number of candidates to preselect
        }
    ),
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
	Query: qdrant.NewQueryMMR(
		qdrant.NewVectorInput(0.01, 0.45, 0.67),
		&qdrant.Mmr{
			Diversity:       qdrant.PtrOf(float32(0.5)), // 0.0 - relevance; 1.0 - diversity
			CandidatesLimit: qdrant.PtrOf(uint32(100)),  // num of candidates to preselect
		}),
	Limit: qdrant.PtrOf(uint64(10)),
})
```


```http
POST /collections/{collection_name}/points/query
{
  "query": {
    "nearest": [0.01, 0.45, 0.67, ...], // search vector
    "mmr": {
      "diversity": 0.5, // 0.0 - relevance; 1.0 - diversity
      "candidates_limit": 100 // num of candidates to preselect
    }
  },
  "limit": 10
}
```


```java
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.VectorInputFactory.vectorInput;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.Mmr;
import io.qdrant.client.grpc.Points.QueryPoints;

QdrantClient client = new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("{collection_name}")
            .setQuery(
                nearest(
                    vectorInput(0.01f, 0.45f, 0.67f), // <-- search vector
                    Mmr.newBuilder()
                        .setDiversity(0.5f) // 0.0 - relevance; 1.0 - diversity
                        .setCandidatesLimit(100) // num of candidates to preselect
                        .build()))
            .setLimit(10)
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=models.NearestQuery(
        nearest=[0.01, 0.45, 0.67], # search vector
        mmr=models.Mmr(
            diversity=0.5, # 0.0 - relevance; 1.0 - diversity
            candidates_limit=100, # num of candidates to preselect
        )
    ),
    limit=10,
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{MmrBuilder, Query, QueryPointsBuilder};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.query(
    QueryPointsBuilder::new("{collection_name}")
        .query(Query::new_nearest_with_mmr(
            vec![0.01, 0.45, 0.67], // search vector
            MmrBuilder::new()
                .diversity(0.5) // 0.0 - relevance; 1.0 - diversity
                .candidates_limit(100) // num of candidates to preselect
        ))
        .limit(10)
).await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
  query: {
    nearest: [0.01, 0.45, 0.67], // search vector
    mmr: {
      diversity: 0.5, // 0.0 - relevance; 1.0 - diversity
      candidates_limit: 100 // num of candidates to preselect
    }
  },
  limit: 10,
});
```
