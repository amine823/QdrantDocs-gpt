Uses a BM25 query with the multilingual tokenizer to handle non-Latin scripts or languages without whitespace separation.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "村上春樹",
        Model = "qdrant/bm25",
        Options = { ["tokenizer"] = "multilingual" },
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
			Text:    "村上春樹",
			Options: qdrant.NewValueMap(map[string]any{"tokenizer": "multilingual"}),
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
    "text": "村上春樹",
    "model": "qdrant/bm25",
    "options": {
      "tokenizer": "multilingual"
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
                nearest(Document.newBuilder().setText("村上春樹").setModel("qdrant/bm25").build()))
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

# Note: the tokenizer option is not supported by FastEmbed
client.query_points(
    collection_name="books",
    query=models.Document(text="村上春樹", model="qdrant/bm25", options={"tokenizer": "multilingual"}),
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
options.insert("tokenizer".to_string(), Value::from("multilingual"));

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(
                DocumentBuilder::new("村上春樹", "qdrant/bm25")
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
    text: "村上春樹",
    model: "qdrant/bm25",
    options: { tokenizer: "multilingual" },
  },
  using: "author-bm25",
  limit: 10,
  with_payload: true,
});
```
