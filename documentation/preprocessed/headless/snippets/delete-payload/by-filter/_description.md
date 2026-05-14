This code snippet shows an example of using filters to delete specific keys from a payload based on defined criteria. In this example, it showcases how to delete keys "color" and "price" where the "color" key matches the value "red".

```csharp
using Qdrant.Client;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.DeletePayloadAsync(
    collectionName: "{collection_name}",
    keys: ["color", "price"],
    filter: MatchKeyword("color", "red")
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

client.DeletePayload(context.Background(), &qdrant.DeletePayloadPoints{
    CollectionName: "{collection_name}",
    Keys:           []string{"color", "price"},
    PointsSelector: qdrant.NewPointsSelectorFilter(
        &qdrant.Filter{
            Must: []*qdrant.Condition{qdrant.NewMatch("color", "red")},
        },
    ),
})
```


```http
POST /collections/{collection_name}/points/payload/delete
{
    "keys": ["color", "price"],
    "filter": {
        "must": [
            {
                "key": "color",
                "match": {
                    "value": "red"
                }
            }
        ]
    }
}
```


```java
import static io.qdrant.client.ConditionFactory.matchKeyword;

import io.qdrant.client.grpc.Common.Filter;
import java.util.List;

client
    .deletePayloadAsync(
        "{collection_name}",
        List.of("color", "price"),
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true,
        null,
        null)
    .get();
```


```python
client.delete_payload(
    collection_name="{collection_name}",
    keys=["color", "price"],
    points=models.Filter(
        must=[
            models.FieldCondition(
                key="color",
                match=models.MatchValue(value="red"),
            ),
        ],
    ),
)
```


```rust
use qdrant_client::qdrant::{Condition, DeletePayloadPointsBuilder, Filter};

client
    .delete_payload(
        DeletePayloadPointsBuilder::new(
            "{collection_name}",
            vec!["color".to_string(), "price".to_string()],
        )
        .points_selector(Filter::must([Condition::matches(
            "color",
            "red".to_string(),
        )]))
        .wait(true),
    )
    .await?;
```


```typescript
client.deletePayload("{collection_name}", {
  keys: ["color", "price"],
  filter: {
    must: [
      {
        key: "color",
        match: {
          value: "red",
        },
      },
    ],
  },
});
```
