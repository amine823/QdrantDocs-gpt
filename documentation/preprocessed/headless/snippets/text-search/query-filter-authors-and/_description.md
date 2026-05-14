Finds books related to "space opera" where both `author` filters must match: Larry Niven and Jerry Pournelle.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var andFilter = new Filter
{
    Must =
    {
        MatchKeyword("author", "Larry Niven"),
        MatchKeyword("author", "Jerry Pournelle"),
    },
};

await client.QueryAsync(
    collectionName: "books",
    query: new Document
    {
        Text = "space opera",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    usingVector: "description-dense",
    filter: andFilter,
    payloadSelector: true
);
```


```go
andFilter := qdrant.Filter{
	Must: []*qdrant.Condition{
		qdrant.NewMatch("author", "Larry Niven"),
		qdrant.NewMatch("author", "Jerry Pournelle"),
	},
}

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{
			Model: "sentence-transformers/all-minilm-l6-v2",
			Text:  "space opera",
		}),
	),
	Using:       qdrant.PtrOf("description-dense"),
	WithPayload: qdrant.NewWithPayload(true),
	Filter:      &andFilter,
})
```


```http
POST /collections/books/points/query
{
  "query": {
    "text": "space opera",
    "model": "sentence-transformers/all-minilm-l6-v2"
  },
  "using": "description-dense",
  "with_payload": true,
  "filter": {
    "must": [
      {
        "key": "author",
        "match": {
          "value": "Larry Niven"
        }
      },
      {
        "key": "author",
        "match": {
          "value": "Jerry Pournelle"
        }
      }
    ]
  }
}
```

```java
import static io.qdrant.client.ConditionFactory.*;
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.WithPayloadSelectorFactory.enable;

import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Common.Filter;
import io.qdrant.client.grpc.Points.*;

QdrantClient client =

Filter filter =
    Filter.newBuilder()
        .addMust(matchKeyword("author", "Larry Niven"))
        .addMust(matchKeyword("author", "Jerry Pournelle"))
        .build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .setQuery(
                nearest(
                    Document.newBuilder()
                        .setText("space opera")
                        .setModel("sentence-transformers/all-minilm-l6-v2")
                        .build()))
            .setUsing("description-dense")
            .setFilter(filter)
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
    query=models.Document(text="space opera", model="sentence-transformers/all-minilm-l6-v2"),
    using="description-dense",
    with_payload=True,
    query_filter=models.Filter(
        must=[
            models.FieldCondition(key="author", match=models.MatchValue(value="Larry Niven")),
            models.FieldCondition(key="author", match=models.MatchValue(value="Jerry Pournelle")),
        ]
    ),
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Condition, Document, Filter, Query, QueryPointsBuilder};

let filter = Filter::must([
    Condition::matches("author", "Larry Niven".to_string()),
    Condition::matches("author", "Jerry Pournelle".to_string()),
]);

client
    .query(
        QueryPointsBuilder::new("books")
            .query(Query::new_nearest(Document::new(
                "space opera",
                "sentence-transformers/all-minilm-l6-v2",
            )))
            .using("description-dense")
            .filter(filter)
            .with_payload(true)
            .build(),
    )
    .await?;
```


```typescript
client.query("books", {
  query: {
    text: "space opera",
    model: "sentence-transformers/all-minilm-l6-v2",
  },
  using: "description-dense",
  with_payload: true,
  filter: {
    must: [
      { key: "author", match: { value: "Larry Niven" } },
      { key: "author", match: { value: "Jerry Pournelle" } },
    ],
  },
});
```
