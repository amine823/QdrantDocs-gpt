This code snippet demonstrates how to utilize the `lookup_from` parameter when querying points. By specifying an external collection and vector name to lookup from, you can retrieve recommendations based on vectors from a different collection. This feature is beneficial when dealing with item-to-user recommendation scenarios, where vectors with the same parameters are stored in separate collections.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
    collectionName: "{collection_name}",
    query: new RecommendInput {
        Positive = { 100, 231 },
        Negative = { 718 }
    },
    usingVector: "image",
    limit: 10,
    lookupFrom: new LookupLocation
    {
        CollectionName = "{external_collection_name}",
        VectorName = "{external_vector_name}",
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
    Query: qdrant.NewQueryRecommend(&qdrant.RecommendInput{
        Positive: []*qdrant.VectorInput{
            qdrant.NewVectorInputID(qdrant.NewIDNum(100)),
            qdrant.NewVectorInputID(qdrant.NewIDNum(231)),
        },
        Negative: []*qdrant.VectorInput{
            qdrant.NewVectorInputID(qdrant.NewIDNum(718)),
        },
    }),
    Using: qdrant.PtrOf("image"),
    LookupFrom: &qdrant.LookupLocation{
        CollectionName: "{external_collection_name}",
        VectorName:     qdrant.PtrOf("{external_vector_name}"),
    },
})
```


```http
POST /collections/{collection_name}/points/query
{
  "query": {
    "recommend": {
      "positive": [100, 231],
      "negative": [718]
    }
  },
  "limit": 10,
  "lookup_from": {
    "collection": "{external_collection_name}",
    "vector": "{external_vector_name}"
  }
}
```


```java
import static io.qdrant.client.QueryFactory.recommend;
import static io.qdrant.client.VectorInputFactory.vectorInput;

import io.qdrant.client.grpc.Points.LookupLocation;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.RecommendInput;
import java.util.List;

client.queryAsync(QueryPoints.newBuilder()
        .setCollectionName("{collection_name}")
        .setQuery(recommend(RecommendInput.newBuilder()
                .addAllPositive(List.of(vectorInput(100), vectorInput(231)))
                .addAllNegative(List.of(vectorInput(718)))
                .build()))
        .setUsing("image")
        .setLimit(10)
        .setLookupFrom(
                LookupLocation.newBuilder()
                        .setCollectionName("{external_collection_name}")
                        .setVectorName("{external_vector_name}")
                        .build())
        .build()).get();
```


```python
client.query_points(
    collection_name="{collection_name}",
    query=models.RecommendQuery(
        recommend=models.RecommendInput(
            positive=[100, 231],
            negative=[718],
        )
    ),
    using="image",
    limit=10,
    lookup_from=models.LookupLocation(
        collection="{external_collection_name}", vector="{external_vector_name}"
    ),
)
```


```rust
use qdrant_client::qdrant::{LookupLocationBuilder, QueryPointsBuilder, RecommendInputBuilder};

client
    .query(
        QueryPointsBuilder::new("{collection_name}")
            .query(
                RecommendInputBuilder::default()
                    .add_positive(100)
                    .add_positive(231)
                    .add_negative(718)
                    .build(),
            )
            .limit(10)
            .using("image")
            .lookup_from(
                LookupLocationBuilder::new("{external_collection_name}")
                    .vector_name("{external_vector_name}"),
            ),
    )
    .await?;
```


```typescript
client.query("{collection_name}", {
    query: {
        recommend: {
            positive: [100, 231],
            negative: [718],
        }
    },
    using: "image",
    limit: 10,
    lookup_from: {
        collection: "{external_collection_name}",
        vector: "{external_vector_name}"
    }
});
```
