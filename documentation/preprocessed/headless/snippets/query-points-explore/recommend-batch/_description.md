This code snippet showcases a batch recommendation API that allows for multiple recommendation requests to be grouped together. Each request contains a query for positive and negative items, along with a filter to narrow down the results. The API is designed to handle multiple recommendation requests efficiently, similar to the batch search API, offering convenience and scalability.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

var filter = MatchKeyword("city", "london");

await client.QueryBatchAsync(
    collectionName: "{collection_name}",
    queries:
    [
        new QueryPoints()
        {
            CollectionName = "{collection_name}",
            Query = new RecommendInput {
                Positive = { 100, 231 },
                Negative = { 718 },
            },
            Limit = 3,
            Filter = filter,
        },
                new QueryPoints()
        {
            CollectionName = "{collection_name}",
            Query = new RecommendInput {
                Positive = { 200, 67 },
                Negative = { 300 },
            },
            Limit = 3,
            Filter = filter,
        }
    ]
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

filter := qdrant.Filter{
    Must: []*qdrant.Condition{
        qdrant.NewMatch("city", "London"),
    },
}
client.QueryBatch(context.Background(), &qdrant.QueryBatchPoints{
    CollectionName: "{collection_name}",
    QueryPoints: []*qdrant.QueryPoints{
        {
            CollectionName: "{collection_name}",
            Query: qdrant.NewQueryRecommend(&qdrant.RecommendInput{
                Positive: []*qdrant.VectorInput{
                    qdrant.NewVectorInputID(qdrant.NewIDNum(100)),
                    qdrant.NewVectorInputID(qdrant.NewIDNum(231)),
                },
                Negative: []*qdrant.VectorInput{
                    qdrant.NewVectorInputID(qdrant.NewIDNum(718)),
                },
            },
            ),
            Filter: &filter,
        },
        {
            CollectionName: "{collection_name}",
            Query: qdrant.NewQueryRecommend(&qdrant.RecommendInput{
                Positive: []*qdrant.VectorInput{
                    qdrant.NewVectorInputID(qdrant.NewIDNum(200)),
                    qdrant.NewVectorInputID(qdrant.NewIDNum(67)),
                },
                Negative: []*qdrant.VectorInput{
                    qdrant.NewVectorInputID(qdrant.NewIDNum(300)),
                },
            },
            ),
            Filter: &filter,
        },
    },
},
)
```


```http
POST /collections/{collection_name}/query/batch
{
  "searches": [
    {
      "query": {
        "recommend": {
          "positive": [100, 231],
          "negative": [718]
        }
      },
      "filter": {
        "must": [
          {
            "key": "city",
            "match": {
              "value": "London"
            }
          }
        ]
      },
      "limit": 10
    },
    {
      "query": {
        "recommend": {
          "positive": [200, 67],
          "negative": [300]
        }
      },
      "filter": {
        "must": [
          {
            "key": "city",
            "match": {
              "value": "London"
            }
          }
        ]
      },
      "limit": 10
    }
  ]
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;
import static io.qdrant.client.QueryFactory.recommend;
import static io.qdrant.client.VectorInputFactory.vectorInput;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.RecommendInput;
import java.util.List;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

Filter filter = Filter.newBuilder().addMust(matchKeyword("city", "London")).build();

List<QueryPoints> recommendQueries = List.of(
        QueryPoints.newBuilder()
                .setCollectionName("{collection_name}")
                .setQuery(recommend(
                        RecommendInput.newBuilder()
                                .addAllPositive(List.of(vectorInput(100), vectorInput(231)))
                                .addAllNegative(List.of(vectorInput(731)))
                                .build()))
                .setFilter(filter)
                .setLimit(3)
                .build(),
        QueryPoints.newBuilder()
                .setCollectionName("{collection_name}")
                .setQuery(recommend(
                        RecommendInput.newBuilder()
                                .addAllPositive(List.of(vectorInput(200), vectorInput(67)))
                                .addAllNegative(List.of(vectorInput(300)))
                                .build()))
                .setFilter(filter)
                .setLimit(3)
                .build());

client.queryBatchAsync("{collection_name}", recommendQueries).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

filter_ = models.Filter(
    must=[
        models.FieldCondition(
            key="city",
            match=models.MatchValue(
                value="London",
            ),
        )
    ]
)

recommend_queries = [
    models.QueryRequest(
        query=models.RecommendQuery(
            recommend=models.RecommendInput(positive=[100, 231], negative=[718])
        ),
        filter=filter_,
        limit=3,
    ),
    models.QueryRequest(
        query=models.RecommendQuery(
            recommend=models.RecommendInput(positive=[200, 67], negative=[300])
        ),
        filter=filter_,
        limit=3,
    ),
]

client.query_batch_points(
    collection_name="{collection_name}", requests=recommend_queries
)
```


```rust
use qdrant_client::qdrant::{
    Condition, Filter, QueryBatchPointsBuilder, QueryPointsBuilder,
    RecommendInputBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let filter = Filter::must([Condition::matches("city", "London".to_string())]);

let recommend_queries = vec![
    QueryPointsBuilder::new("{collection_name}")
        .query(
            RecommendInputBuilder::default()
                .add_positive(100)
                .add_positive(231)
                .add_negative(718)
                .build(),
        )
        .filter(filter.clone())
        .build(),
    QueryPointsBuilder::new("{collection_name}")
        .query(
            RecommendInputBuilder::default()
                .add_positive(200)
                .add_positive(67)
                .add_negative(300)
                .build(),
        )
        .filter(filter)
        .build(),
];

client
    .query_batch(QueryBatchPointsBuilder::new(
        "{collection_name}",
        recommend_queries,
    ))
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

const filter = {
    must: [
        {
            key: "city",
            match: {
                value: "London",
            },
        },
    ],
};

const searches = [
    {
        query: {
            recommend: {
                positive: [100, 231],
                negative: [718]
            }
        },
        filter,
        limit: 3,
    },
    {
        query: {
            recommend: {
                positive: [200, 67],
                negative: [300]
            }
        },
        filter,
        limit: 3,
    },
];

client.queryBatch("{collection_name}", {
    searches,
});
```
