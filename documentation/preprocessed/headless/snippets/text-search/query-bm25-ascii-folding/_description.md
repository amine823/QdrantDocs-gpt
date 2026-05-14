Runs a BM25 query with ASCII folding enabled so searches ignore diacritics (for example, matches "Mieville" and "Miéville").

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "Mieville",
        Model = "qdrant/bm25",
        Options = { ["ascii_folding"] = true },
    },
    usingVector: "author-bm25",
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
			Text:    "Mieville",
			Options: qdrant.NewValueMap(map[string]any{"ascii_folding": true}),
		}),
	),
	Using:       qdrant.PtrOf("author-bm25"),
	WithPayload: qdrant.NewWithPayload(true),
	Limit:       qdrant.PtrOf(uint64(10)),
})
```


```http
POST /collections/books/points/query
{
  "query": {
    "text": "Mieville",
    "model": "qdrant/bm25",
    "options": {
      "ascii_folding": true
    }
  },
  "using": "author-bm25",
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
                    Document.newBuilder().setText("Mieville").setModel("qdrant/bm25").build()))
            .setUsing("author-bm25")
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

# Note: the ascii_folding option is not supported by FastEmbed
client.query_points(
    collection_name="books",
    query=models.Document(text="Mieville", model="qdrant/bm25", options={"ascii_folding": True}),
    using="author-bm25",
    limit=10,
    with_payload=True,
)
```


```rust
use std::collections::HashMap;

use qdrant_client::Qdrant;
use qdrant_client::qdrant::{DocumentBuilder, Query, QueryPointsBuilder, Value};

let mut options = HashMap::new();
options.insert("ascii_folding".to_string(), Value::from(true));

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(
                DocumentBuilder::new("Mieville", "qdrant/bm25")
                    .options(options)
                    .build(),
            ))
            .using("author-bm25")
            .limit(10)
            .with_payload(true)
            .build(),
    )
    .await?;
```


```typescript
client.query("books", {
  query: {
    text: "Mieville",
    model: "qdrant/bm25",
    options: { ascii_folding: true },
  },
  using: "author-bm25",
  limit: 10,
  with_payload: true,
});
```
