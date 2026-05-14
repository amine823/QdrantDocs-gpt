Set the payload for points in a collection by applying a filter based on the specified properties. In this case, the code will set the payload with "property1" and "property2" values for points where the value of the "color" property is "red" within the specified collection. This approach allows for targeted modifications without needing to know the specific point ids.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var client = new QdrantClient("localhost", 6334);

await client.SetPayloadAsync(
    collectionName: "{collection_name}",
    payload: new Dictionary<string, Value> { { "property1", "string" }, { "property2", "string" } },
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

client.SetPayload(context.Background(), &qdrant.SetPayloadPoints{
    CollectionName: "{collection_name}",
    Payload: qdrant.NewValueMap(
        map[string]any{"property1": "string", "property2": "string"}),
    PointsSelector: qdrant.NewPointsSelectorFilter(&qdrant.Filter{
        Must: []*qdrant.Condition{
            qdrant.NewMatch("color", "red"),
        },
    }),
})
```


```http
POST /collections/{collection_name}/points/payload
{
    "payload": {
        "property1": "string",
        "property2": "string"
    },
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
import static io.qdrant.client.ValueFactory.value;

import io.qdrant.client.grpc.Common.Filter;
import java.util.Map;

client
    .setPayloadAsync(
        "{collection_name}",
        Map.of("property1", value("string"), "property2", value("string")),
        Filter.newBuilder().addMust(matchKeyword("color", "red")).build(),
        true,
        null,
        null)
    .get();
```


```python
client.set_payload(
    collection_name="{collection_name}",
    payload={
        "property1": "string",
        "property2": "string",
    },
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
use qdrant_client::qdrant::{Condition, Filter, SetPayloadPointsBuilder};
use qdrant_client::Payload;
use serde_json::json;

client
    .set_payload(
        SetPayloadPointsBuilder::new(
            "{collection_name}",
            Payload::try_from(json!({
                "property1": "string",
                "property2": "string",
            }))
            .unwrap(),
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
client.setPayload("{collection_name}", {
  payload: {
    property1: "string",
    property2: "string",
  },
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
