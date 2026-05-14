The snippet demonstrates how to boost the score of points based on their tag field. If the tag field is one of the headers, it will be more relevant to the query. Tags are located in the payload and included in the boost formula as a filtering condition.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.QueryAsync(
  collectionName: "{collection_name}",
  prefetch:
  [
    new PrefetchQuery { Query = new float[] { 0.01f, 0.45f, 0.67f }, Limit = 100 },
  ],
  query: new Formula
  {
    Expression = new SumExpression
    {
      Sum =
      {
        "$score",
        new MultExpression
        {
          Mult = { 0.5f, Match("tag", ["h1", "h2", "h3", "h4"]) },
        },
        new MultExpression { Mult = { 0.25f, Match("tag", ["p", "li"]) } },
      },
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
    Prefetch: []*qdrant.PrefetchQuery{
        {
            Query: qdrant.NewQuery(0.01, 0.45, 0.67),
        },
    },
    Query: qdrant.NewQueryFormula(&qdrant.Formula{
        Expression: qdrant.NewExpressionSum(&qdrant.SumExpression{
            Sum: []*qdrant.Expression{
                qdrant.NewExpressionVariable("$score"),
                qdrant.NewExpressionMult(&qdrant.MultExpression{
                    Mult: []*qdrant.Expression{
                        qdrant.NewExpressionConstant(0.5),
                        qdrant.NewExpressionCondition(qdrant.NewMatchKeywords("tag", "h1", "h2", "h3", "h4")),
                    },
                }),
                qdrant.NewExpressionMult(&qdrant.MultExpression{
                    Mult: []*qdrant.Expression{
                        qdrant.NewExpressionConstant(0.25),
                        qdrant.NewExpressionCondition(qdrant.NewMatchKeywords("tag", "p", "li")),
                    },
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
    }
    "query": {
        "formula": {
            "sum": [
                "$score",
                { 
                    "mult": [ 
                        0.5,
                        { 
                            "key": "tag",
                            "match": { "any": ["h1", "h2", "h3", "h4"] } 
                        } 
                    ]
                },
                {
                    "mult": [
                        0.25,
                        { 
                            "key": "tag",
                            "match": { "any": ["p", "li"] } 
                        }
                    ]
                }
            ]
        }
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeywords;
import static io.qdrant.client.ExpressionFactory.condition;
import static io.qdrant.client.ExpressionFactory.constant;
import static io.qdrant.client.ExpressionFactory.mult;
import static io.qdrant.client.ExpressionFactory.sum;
import static io.qdrant.client.ExpressionFactory.variable;
import static io.qdrant.client.QueryFactory.formula;
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.Formula;
import io.qdrant.client.grpc.Points.MultExpression;
import io.qdrant.client.grpc.Points.PrefetchQuery;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.SumExpression;
import java.util.List;

QdrantClient client =
  new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
  .queryAsync(
    QueryPoints.newBuilder()
      .setCollectionName("{collection_name}")
      .addPrefetch(
        PrefetchQuery.newBuilder()
          .setQuery(nearest(0.01f, 0.45f, 0.67f))
          .setLimit(100)
          .build())
      .setQuery(
        formula(
          Formula.newBuilder()
            .setExpression(
              sum(
                SumExpression.newBuilder()
                  .addSum(variable("$score"))
                  .addSum(
                    mult(
                      MultExpression.newBuilder()
                        .addMult(constant(0.5f))
                        .addMult(
                          condition(
                            matchKeywords(
                              "tag",
                              List.of("h1", "h2", "h3", "h4"))))
                        .build()))
                  .addSum(mult(MultExpression.newBuilder()
                  .addMult(constant(0.25f))
                  .addMult(
                    condition(
                      matchKeywords(
                        "tag",
                        List.of("p", "li"))))
                  .build()))
                  .build()))
            .build()))
      .build())
  .get();
```


```python
from qdrant_client import QdrantClient, models

tag_boosted = client.query_points(
    collection_name="{collection_name}",
    prefetch=models.Prefetch(
        query=[0.1, 0.45, 0.67],  # <-- dense vector
        limit=50
    ),
    query=models.FormulaQuery(
        formula=models.SumExpression(sum=[
            "$score",
            models.MultExpression(mult=[0.5, models.FieldCondition(key="tag", match=models.MatchAny(any=["h1", "h2", "h3", "h4"]))]),
            models.MultExpression(mult=[0.25, models.FieldCondition(key="tag", match=models.MatchAny(any=["p", "li"]))])
        ]
    ))
)
```


```rust
use qdrant_client::qdrant::{
    Condition, Expression, FormulaBuilder, PrefetchQueryBuilder, QueryPointsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let _tag_boosted = client.query(
    QueryPointsBuilder::new("{collection_name}")
        .add_prefetch(PrefetchQueryBuilder::default()
            .query(vec![0.01, 0.45, 0.67])
            .limit(100u64)
        )
        .query(FormulaBuilder::new(Expression::sum_with([
            Expression::score(),
            Expression::mult_with([
                Expression::constant(0.5),
                Expression::condition(Condition::matches("tag", ["h1", "h2", "h3", "h4"])),
            ]),
            Expression::mult_with([
                Expression::constant(0.25),
                Expression::condition(Condition::matches("tag", ["p", "li"])),
            ]),
        ])))
        .limit(10)
    ).await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

const tag_boosted = await client.query("{collection_name}", {
  prefetch: {
    query: [0.2, 0.8, 0.1, 0.9],
    limit: 50
  },
  query: {
    formula: {
      sum: [
        "$score",
        {
          mult: [ 0.5, { key: "tag", match: { any: ["h1", "h2", "h3", "h4"] }} ]
        },
        {
          mult: [ 0.25, { key: "tag", match: { any: ["p", "li"] }} ]
        }
      ]
    }
  }
});
```
