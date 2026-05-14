This code snippet applies exponential decay to boost the relevance of search results based on a datetime field called "upload_time" in the payload (which can be when a point was uploaded to Qdrant). Items closer in time to a specified `target`, so, in our case, the current datetime, which means "fresher" results, receive higher scores. Relevance score is decreasing exponentially with "upload_time" getting further away from `target` time, reaching a 0.5 `midpoint` of relevance after a defined `scale` period of 1 day.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
    collectionName: "{collection_name}",
    prefetch:
    [
        new PrefetchQuery {
            Query = new float[] { 0.1f, 0.45f, 0.67f }, // <-- dense vector
            Limit = 50
        },
    ],
    query: new Formula
     {
        Expression = new SumExpression
        {
            Sum = //  the final score = score + exp_decay(target_time - x_time)
            {
                "$score",
                Expression.FromExpDecay(
                    new()
                    {
                        X = Expression.FromDateTimeKey("update_time"),  // payload key
                        Target = Expression.FromDateTime("YYYY-MM-DDT00:00:00Z"),  // current datetime
                        Midpoint = 0.5f,
                        Scale = 86400 // 1 day in seconds
                    }
                )
            }
        }
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
    Prefetch: []*qdrant.PrefetchQuery{
        {
            Query: qdrant.NewQuery(0.1, 0.45, 0.67), // <-- dense vector
            Limit: qdrant.PtrOf(uint64(50)),
        },
    },
    Query: qdrant.NewQueryFormula(&qdrant.Formula{
        Expression: qdrant.NewExpressionSum(&qdrant.SumExpression{
            Sum: []*qdrant.Expression{ //  the final score = score + exp_decay(target_time - x_time)
                qdrant.NewExpressionVariable("$score"), 
                qdrant.NewExpressionExpDecay(&qdrant.DecayParamsExpression{
                    X: qdrant.NewExpressionDatetimeKey("update_time"), // payload key
                    Target: qdrant.NewExpressionDatetime("YYYY-MM-DDT00:00:00Z"), // current datetime
                    Scale:  qdrant.PtrOf(float32(86400)), // 1 day in seconds
                    Midpoint: qdrant.PtrOf(float32(0.5)),
                }),
            },
        }),
    }),
})
```


```http
POST /collections/{collection_name}/points/query
{
    "prefetch": {
        "query": [0.2, 0.8, ...],  // <-- dense vector
        "limit": 50
    },
    "query": {
        "formula": {
            "sum": [
                "$score", // the final score = score + exp_decay(target_time - x_time)
                {
                    "exp_decay": {
                        "x": {
                            "datetime_key": "update_time" // payload key
                        },
                        "target": {
                            "datetime": "YYYY-MM-DDT00:00:00Z" // current datetime
                        },
                        "scale": 86400, // 1 day in seconds
                        "midpoint": 0.5 // if item's "update_time" is more than 1 day apart from current datetime, relevance score is less than 0.5
                    }
                }
            ]
        }
    }
}
```


```java
import static io.qdrant.client.ExpressionFactory.datetime;
import static io.qdrant.client.ExpressionFactory.datetimeKey;
import static io.qdrant.client.ExpressionFactory.expDecay;
import static io.qdrant.client.ExpressionFactory.sum;
import static io.qdrant.client.ExpressionFactory.variable;
import static io.qdrant.client.QueryFactory.formula;
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.DecayParamsExpression;
import io.qdrant.client.grpc.Points.Formula;
import io.qdrant.client.grpc.Points.PrefetchQuery;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.ScoredPoint;
import io.qdrant.client.grpc.Points.SumExpression;
import java.util.List;

QdrantClient client =
  new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

List<ScoredPoint> time_boosted = client.queryAsync(
    QueryPoints.newBuilder()
        .setCollectionName("{collection_name}")
        .addPrefetch(
            PrefetchQuery.newBuilder()
                .setQuery(nearest(0.1f, 0.45f, 0.67f))  // <-- dense vector
                .setLimit(50)
                .build())
        .setQuery(
            formula(
                Formula.newBuilder()
                    .setExpression(
                        sum( //  the final score = score + exp_decay(target_time - x_time)
                            SumExpression.newBuilder()
                                .addSum(variable("$score"))
                                .addSum(
                                    expDecay(
                                        DecayParamsExpression.newBuilder()
                                            .setX(
                                                datetimeKey("update_time"))  // payload key
                                            .setTarget(
                                                datetime("YYYY-MM-DDT00:00:00Z"))  // current datetime
                                            .setMidpoint(0.5f)
                                            .setScale(86400)  // 1 day in seconds
                                            .build()))
                                .build()))
                    .build()))
        .build()
).get();
```


```python
from qdrant_client import QdrantClient, models

time_boosted = client.query_points(
    collection_name="{collection_name}",
    prefetch=models.Prefetch(
        query=[0.1, 0.45, 0.67],  # <-- dense vector
        limit=50
    ),
    query=models.FormulaQuery(
        formula=models.SumExpression(
            sum=[
                "$score", # the final score = score + exp_decay(target_time - x_time)
                models.ExpDecayExpression(
                    exp_decay=models.DecayParamsExpression(
                        x=models.DatetimeKeyExpression(
                            datetime_key="upload_time" # payload key 
                        ),
                        target=models.DatetimeExpression(
                            datetime="YYYY-MM-DDT00:00:00Z" # current datetime
                        ),
                        scale=86400, # 1 day in seconds
                        midpoint=0.5 # if item's "update_time" is more than 1 day apart from current datetime, relevance score is less than 0.5
                    )
                )
            ]
        )
    )
)
```


```rust
use qdrant_client::qdrant::{
    DecayParamsExpressionBuilder, Expression, FormulaBuilder, PrefetchQueryBuilder, QueryPointsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let _geo_boosted = client.query(
    QueryPointsBuilder::new("{collection_name}")
            .add_prefetch(
                PrefetchQueryBuilder::default()
                    .query(vec![0.1, 0.45, 0.67]) // <-- dense vector
                    .limit(50u64),
            )
            .query(
                FormulaBuilder::new(Expression::sum_with([ //  the final score = score + exp_decay(target_time - x_time)
                    Expression::score(),
                    Expression::exp_decay(
                        DecayParamsExpressionBuilder::new(Expression::datetime_key("update_time")) // payload key
                            .target(Expression::datetime("YYYY-MM-DDT00:00:00Z"))
                            .midpoint(0.5)
                            .scale(86400.0), // 1 day in seconds
                    ),
                ]))
            )
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

const time_boosted = await client.query('collectionName', {
  prefetch: {
    query: [0.1, 0.45, 0.67], // <-- dense vector
    limit: 50
  },
   query: {
      formula: {
          sum: [ //  the final score = score + exp_decay(target_time - x_time)
              "$score",
              {
                  exp_decay: {
                      x: {
                          datetime_key: "update_time" // payload key
                      },
                      target: {
                          datetime: "YYYY-MM-DDT00:00:00Z" // current datetime
                      },
                      midpoint: 0.5,
                      scale: 86400 // 1 day in seconds
                  }
              }
          ]
      }
  }
});
```
