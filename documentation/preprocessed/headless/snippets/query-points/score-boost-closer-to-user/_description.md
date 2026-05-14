The snippet demonstrates how to use decay functions and geo distance functions to boost the score of points closer to a user. Function will boost the scores of points, that are closer to specified location `x`. Point locations is taken from the `geo.location` field. If the field is not present, the `defaults` parameter can be used to fill in the missing values. Scale parameter is used to control the decay rate.


```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Expression;

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
                FromExpDecay(
                    new()
                    {
                        X = new GeoDistance
                        {
                            Origin = new GeoPoint { Lat = 52.504043, Lon = 13.393236 },
                            To = "geo.location",
                        },
                        Scale = 5000,
                    }
                ),
            },
        },
        Defaults =
        {
            ["geo.location"] = new Dictionary<string, Value>
            {
                ["lat"] = 48.137154,
                ["lon"] = 11.576124,
            },
        },
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
            Query: qdrant.NewQuery(0.2, 0.8),
        },
    },
    Query: qdrant.NewQueryFormula(&qdrant.Formula{
        Expression: qdrant.NewExpressionSum(&qdrant.SumExpression{
            Sum: []*qdrant.Expression{
                qdrant.NewExpressionVariable("$score"),
                qdrant.NewExpressionExpDecay(&qdrant.DecayParamsExpression{
                    X: qdrant.NewExpressionGeoDistance(&qdrant.GeoDistance{
                        Origin: &qdrant.GeoPoint{
                            Lat: 52.504043,
                            Lon: 13.393236,
                        },
                        To: "geo.location",
                    }),
                }),
            },
        }),
        Defaults: qdrant.NewValueMap(map[string]any{
            "geo.location": map[string]any{
                "lat": 48.137154,
                "lon": 11.576124,
            },
        }),
    }),
})
```


```http
POST /collections/{collection_name}/points/query
{
    "prefetch": { "query": [0.2, 0.8, ...], "limit": 50 },
    "query": {
        "formula": {
            "sum": [
                "$score",
                {
                    "gauss_decay": {
                        "x": {
                            "geo_distance": {
                                "origin": { "lat": 52.504043, "lon": 13.393236 }
                                "to": "geo.location"
                            }
                        },
                        "scale": 5000 // 5km
                    }
                }
            ]
        },
        "defaults": { "geo.location": {"lat": 48.137154, "lon": 11.576124} }
    }
}
```


```java
import static io.qdrant.client.ExpressionFactory.expDecay;
import static io.qdrant.client.ExpressionFactory.geoDistance;
import static io.qdrant.client.ExpressionFactory.sum;
import static io.qdrant.client.ExpressionFactory.variable;
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.QueryFactory.formula;
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.GeoPoint;
import io.qdrant.client.grpc.Points.DecayParamsExpression;
import io.qdrant.client.grpc.Points.Formula;
import io.qdrant.client.grpc.Points.GeoDistance;
import io.qdrant.client.grpc.Points.PrefetchQuery;
import io.qdrant.client.grpc.Points.QueryPoints;
import io.qdrant.client.grpc.Points.SumExpression;
import java.util.Map;

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
                    expDecay(
                      DecayParamsExpression.newBuilder()
                        .setX(
                          geoDistance(
                            GeoDistance.newBuilder()
                              .setOrigin(
                                GeoPoint.newBuilder()
                                  .setLat(52.504043)
                                  .setLon(13.393236)
                                  .build())
                              .setTo("geo.location")
                              .build()))
                        .setScale(5000)
                        .build()))
                  .build()))
            .putDefaults(
              "geo.location",
              value(
                Map.of(
                  "lat", value(48.137154),
                  "lon", value(11.576124))))
            .build()))
      .build())
  .get();
```


```python
from qdrant_client import QdrantClient, models

geo_boosted = client.query_points(
    collection_name="{collection_name}",
    prefetch=models.Prefetch(
        query=[0.1, 0.45, 0.67],  # <-- dense vector
        limit=50
    ),
    query=models.FormulaQuery(
        formula=models.SumExpression(sum=[
            "$score",
            models.GaussDecayExpression(
                gauss_decay=models.DecayParamsExpression(
                    x=models.GeoDistance(
                        geo_distance=models.GeoDistanceParams(
                            origin=models.GeoPoint(
                                lat=52.504043,
                                lon=13.393236
                            ),  # Berlin
                            to="geo.location"
                        )
                    ),
                    scale=5000  # 5km
                )
            )
        ]),
        defaults={"geo.location": models.GeoPoint(lat=48.137154, lon=11.576124)}  # Munich
    )
)
```


```rust
use qdrant_client::qdrant::{
    GeoPoint,  DecayParamsExpressionBuilder, Expression, FormulaBuilder, PrefetchQueryBuilder, QueryPointsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let _geo_boosted = client.query(
    QueryPointsBuilder::new("{collection_name}")
            .add_prefetch(
                PrefetchQueryBuilder::default()
                    .query(vec![0.01, 0.45, 0.67])
                    .limit(100u64),
            )
            .query(
                FormulaBuilder::new(Expression::sum_with([
                    Expression::score(),
                    Expression::exp_decay(
                        DecayParamsExpressionBuilder::new(Expression::geo_distance_with(
                            // Berlin
                            GeoPoint { lat: 52.504043, lon: 13.393236 },
                            "geo.location",
                        ))
                        .scale(5_000.0),
                    ),
                ]))
                // Munich
                .add_default("geo.location", GeoPoint { lat: 48.137154, lon: 11.576124 }),
            )
            .limit(10),
    )
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

const distance_boosted = await client.query("{collection_name}", {
  prefetch: {
    query: [0.1, 0.45, 0.67],
    limit: 50
  },
  query: {
    formula: {
      sum: [
        "$score",
        {
          gauss_decay: {
            x: {
              geo_distance: {
                origin: { lat: 52.504043, lon: 13.393236 }, // Berlin
                to: "geo.location"
              }
            },
            scale: 5000 // 5km
          }
        }
      ]
    },
    defaults: { "geo.location": { lat: 48.137154, lon: 11.576124 } } // Munich
  }
});
```
