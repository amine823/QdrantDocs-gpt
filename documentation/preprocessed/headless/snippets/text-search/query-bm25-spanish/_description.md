Uses a BM25 query with Spanish language options to match the ingest configuration for consistent tokenization, stemming, and stopwords.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "tiempo",
        Model = "qdrant/bm25",
        Options = { ["language"] = "spanish" },
    },
    usingVector: "title-bm25",
    payloadSelector: true,
    limit: 10
);
```


```go
client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model:   "qdrant/bm25",
			Text:    "tiempo",
			Options: qdrant.NewValueMap(map[string]any{"language": "spanish"}),
		}),
	),
	Using:       qdrant.PtrOf("title-bm25"),
	WithPayload: qdrant.NewWithPayload(true),
	Limit:       qdrant.PtrOf(uint64(10)),
})
```


```http
POST /collections/books/points/query
{
  "query": {
    "text": "tiempo",
    "model": "qdrant/bm25",
    "options": {
      "language": "spanish"
    }
  },
  "using": "title-bm25",
  "limit": 10,
  "with_payload": true
}
```

```java
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.WithPayloadSelectorFactory.enable;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Points.*;

QdrantClient client =

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .setQuery(
                nearest(
                    Document.newBuilder().setText("tiempo").setModel("qdrant/bm25").build()))
            .setUsing("title-bm25")
            .setLimit(10)
            .setWithPayload(enable(true))
            .build())
    .get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_points(
    collection_name="books",
    query=models.Document(text="tiempo", model="qdrant/bm25", options={"language": "spanish"}),
    using="title-bm25",
    limit=10,
    with_payload=True,
)
```


```rust
use std::collections::HashMap;

use qdrant_client::Qdrant;
use qdrant_client::qdrant::{DocumentBuilder, Query, QueryPointsBuilder, Value};

let mut options = HashMap::new();
options.insert("language".to_string(), Value::from("spanish"));

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(
                DocumentBuilder::new("tiempo", "qdrant/bm25")
                    .options(options)
                    .build(),
            ))
            .using("title-bm25")
            .limit(10)
            .with_payload(true)
            .build(),
    )
    .await?;
```


```typescript
client.query("books", {
  query: {
    text: "tiempo",
    model: "qdrant/bm25",
    options: { language: "spanish" },
  },
  using: "title-bm25",
  limit: 10,
  with_payload: true,
});
```
