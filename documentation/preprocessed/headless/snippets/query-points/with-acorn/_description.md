This code snippet demonstrates how to enable ACORN for HNSW search.
ACORN improves search recall for searches with multiple low-selectivity payload filters, at the cost of reduced performance.
The `enable` parameter activates ACORN based on filter selectivity.
The `max_selectivity` parameter controls the threshold - if estimated filter selectivity is higher than this value, ACORN will not be used.
Selectivity is estimated as the ratio of points satisfying the filters to total points.
Values range from 0.0 (never use ACORN) to 1.0 (always use ACORN), with a default of 0.4.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
	collectionName: "{collection_name}",
	query: new float[] { 0.2f, 0.1f, 0.9f, 0.7f },
	searchParams: new SearchParams
	{
		Acorn = new AcornSearchParams
		{
			Enable = true,
			MaxSelectivity = 0.4
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
	Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
	Params: &qdrant.SearchParams{
		Acorn: &qdrant.AcornSearchParams{
			Enable:          qdrant.PtrOf(true),
			MaxSelectivity:  qdrant.PtrOf(0.4),
		},
	},
})
```


```http
POST /collections/{collection_name}/points/query
{
    "query": [0.2, 0.1, 0.9, 0.7],
    "params": {
        "acorn": {
            "enable": true,
            "max_selectivity": 0.4
        }
    },
    "limit": 10
}
```

```java
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.AcornSearchParams;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.SearchParams;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(
        QueryPoints.newBuilder()
                .setCollectionName("{collection_name}")
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .setParams(
                        SearchParams.newBuilder()
                                .setAcorn(
                                        AcornSearchParams.newBuilder()
                                                .setEnable(true)
                                                .setMaxSelectivity(0.4)
                                                .build())
                                .build())
                .setLimit(10)
                .build())
        .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=[0.2, 0.1, 0.9, 0.7],
    search_params=models.SearchParams(
        acorn=models.AcornSearchParams(
            enable=True,
            max_selectivity=0.4,
        )
    ),
    limit=10,
)
```


```rust
use qdrant_client::qdrant::{
    AcornSearchParamsBuilder, QueryPointsBuilder, SearchParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(vec![0.2, 0.1, 0.9, 0.7])
            .limit(10)
            .params(
                SearchParamsBuilder::default().acorn(
                    AcornSearchParamsBuilder::new(true)
                        .max_selectivity(0.4),
                ),
            ),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
    query: [0.2, 0.1, 0.9, 0.7],
    params: {
        acorn: {
            enable: true,
            max_selectivity: 0.4,
        },
    },
    limit: 10,
});
```
