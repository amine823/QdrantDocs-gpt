Tunes BM25 by setting `avg_len` to 5.0 for title fields, improving length normalization for scoring.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.UpsertAsync(
    collectionName: "books",
    wait: true,
    points: new List<PointStruct>
    {
        new()
        {
            Id = 1,
            Vectors = new Dictionary<string, Vector>
            {
                ["title-bm25"] = new Document
                {
                    Text = "The Time Machine",
                    Model = "qdrant/bm25",
                    Options = { ["avg_len"] = 5.0 },
                },
            },
            Payload =
            {
                ["title"] = "The Time Machine",
                ["author"] = "H.G. Wells",
                ["isbn"] = "9780553213515",
            },
        },
    }
);
```


```go
client.Upsert(context.Background(), &qdrant.UpsertPoints{
	CollectionName: "books",
	Points: []*qdrant.PointStruct{
		{
			Id: qdrant.NewIDNum(uint64(1)),
			Vectors: qdrant.NewVectorsMap(map[string]*qdrant.Vector{
				"title-bm25": qdrant.NewVectorDocument(&qdrant.Document{
					Model: "qdrant/bm25",
					Text:  "The Time Machine",
					Options: qdrant.NewValueMap(map[string]any{"avg_len": 5.0}),
				}),
			}),
			Payload: qdrant.NewValueMap(map[string]any{
				"title":  "The Time Machine",
				"author": "H.G. Wells",
				"isbn":   "9780553213515",
			}),
		},
	},
})
```


```http
PUT /collections/books/points?wait=true
{
  "points": [
    {
      "id": 1,
      "vector": {
        "title-bm25": {
          "text": "The Time Machine",
          "model": "qdrant/bm25",
          "options": {
            "avg_len": 5.0
          }
        }
      },
      "payload": {
        "title": "The Time Machine",
        "author": "H.G. Wells",
        "isbn": "9780553213515"
      }
    }
  ]
}
```

```java
import static io.qdrant.client.PointIdFactory.id;
import static io.qdrant.client.ValueFactory.value;
import static io.qdrant.client.VectorFactory.vector;
import static io.qdrant.client.VectorsFactory.namedVectors;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.*;
import java.util.*;

QdrantClient client =

PointStruct point =
    PointStruct.newBuilder()
        .setId(id(1))
        .setVectors(
            namedVectors(
                Map.of(
                    "title-bm25",
                    vector(
                        Document.newBuilder()
                            .setText("The Time Machine")
                            .setModel("qdrant/bm25")
                            .putOptions("avg_len", value(5.0))
                            .build()))))
        .putAllPayload(
            Map.of(
                "title", value("The Time Machine"),
                "author", value("H.G. Wells"),
                "isbn", value("9780553213515")))
        .build();

client.upsertAsync("books", List.of(point)).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.upsert(
    collection_name="books",
    points=[
        models.PointStruct(
            id=1,
            vector={
                "title-bm25": models.Document(
                    text="The Time Machine",
                    model="qdrant/bm25",
                    options={"avg_len": 5.0}
                )
            },
            payload={
                "title": "The Time Machine",
                "author": "H.G. Wells",
                "isbn": "9780553213515",
            },
        )
    ],
)
```


```rust
use std::collections::HashMap;

use qdrant_client::qdrant::{DocumentBuilder, PointStruct, UpsertPointsBuilder, Value};
use qdrant_client::{Payload, Qdrant};
use serde_json::json;

let mut options = HashMap::new();
options.insert("avg_len".to_string(), Value::from(5.0));

let point = PointStruct::new(
    1,
    HashMap::from([(
        "title-bm25".to_string(),
        DocumentBuilder::new("The Time Machine", "qdrant/bm25")
                    .options(options)
                    .build(),
    )]),
    Payload::try_from(json!({
        "title": "The Time Machine",
        "author": "H.G. Wells",
        "isbn": "9780553213515",
    }))
    .unwrap(),
);

client
    .upsert_points(UpsertPointsBuilder::new("books", vec![point]).wait(true))
    .await?;
```


```typescript
client.upsert("books", {
  wait: true,
  points: [
    {
      id: 1,
      vector: {
        "title-bm25": {
          text: "The Time Machine",
          model: "qdrant/bm25",
          options: { avg_len: 5.0 },
        },
      },
      payload: {
        title: "The Time Machine",
        author: "H.G. Wells",
        isbn: "9780553213515",
      },
    },
  ],
});
```
