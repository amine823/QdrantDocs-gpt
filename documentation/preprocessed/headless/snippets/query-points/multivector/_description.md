Perform a multivector search within the specified collection by using the `query` endpoint. The request includes a list of arrays representing points to be queried for similarity matching within the collection.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
  collectionName: "{collection_name}",
  query: new float[][] {
    [-0.013f, 0.020f, -0.007f, -0.111f],
    [-0.030f, -0.055f, 0.001f, 0.072f],
    [-0.041f, 0.014f, -0.032f, -0.062f],
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
	Query: qdrant.NewQueryMulti(
		[][]float32{
			{-0.013, 0.020, -0.007, -0.111},
			{-0.030, -0.055, 0.001, 0.072},
			{-0.041, 0.014, -0.032, -0.062},
		}),
})
```


```http
POST collections/{collection_name}/points/query
{
  "query": [
    [-0.013,  0.020, -0.007, -0.111, ...],
    [-0.030, -0.055,  0.001,  0.072, ...],
    [-0.041,  0.014, -0.032, -0.062, ...]
  ]
}
```


```java
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.QueryPoints;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.queryAsync(QueryPoints.newBuilder()
    .setCollectionName("{collection_name}")
    .setQuery(nearest(new float[][] {
        {-0.013f, 0.020f, -0.007f, -0.111f}, 
        {-0.030f, -0.055f, 0.001f, 0.072f}, 
        {-0.041f, 0.014f, -0.032f, -0.062f}
    }))
    .build()).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.query_points(
    collection_name="{collection_name}",
    query=[
        [-0.013,  0.020, -0.007, -0.111],
        [-0.030, -0.055,  0.001,  0.072],
        [-0.041,  0.014, -0.032, -0.062]
    ],
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{ QueryPointsBuilder, VectorInput };

let client = Qdrant::from_url("http://localhost:6334").build()?;

let res = client.query(
    QueryPointsBuilder::new("{collection_name}")
        .query(VectorInput::new_multi(
            vec![
                vec![-0.013,  0.020, -0.007, -0.111],
                vec![-0.030, -0.055,  0.001,  0.072],
                vec![-0.041,  0.014, -0.032, -0.062],
            ]
        ))
).await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.query("{collection_name}", {
  "query": [
    [-0.013, 0.020, -0.007, -0.111],
    [-0.030, -0.055, 0.001, 0.072],
    [-0.041, 0.014, -0.032, -0.062]
  ]
});
```
