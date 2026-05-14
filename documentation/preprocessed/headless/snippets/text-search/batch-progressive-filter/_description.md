Batch search that progressively relaxes title filters: exact `text`, then `text_any`, then no filter to return the first non-empty result set.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;
using static Qdrant.Client.Grpc.Conditions;

var searchStrict = new QueryPoints
{
    CollectionName = "books",
    Query = new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    Using = "description-dense",
    Filter = new Filter { Must = { MatchText("title", "time travel") } },
};

var searchRelaxed = new QueryPoints
{
    CollectionName = "books",
    Query = new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    Using = "description-dense",
    Filter = new Filter { Must = { MatchTextAny("title", "time travel") } },
};

var searchVectorOnly = new QueryPoints
{
    CollectionName = "books",
    Query = new Document
    {
        Text = "time travel",
        Model = "sentence-transformers/all-minilm-l6-v2",
    },
    Using = "description-dense",
};

await client.QueryBatchAsync(
    collectionName: "books",
    queries: new List<QueryPoints> { searchStrict, searchRelaxed, searchVectorOnly }
);
```


```go
strict := &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{Model: "sentence-transformers/all-minilm-l6-v2", Text: "time travel"}),
	),
	Using:  qdrant.PtrOf("description-dense"),
	Filter: &qdrant.Filter{Must: []*qdrant.Condition{qdrant.NewMatchText("title", "time travel")}},
}

relaxed := &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{Model: "sentence-transformers/all-minilm-l6-v2", Text: "time travel"}),
	),
	Using:  qdrant.PtrOf("description-dense"),
	Filter: &qdrant.Filter{Must: []*qdrant.Condition{qdrant.NewMatchTextAny("title", "time travel")}},
}

vectorOnly := &qdrant.QueryPoints{
	CollectionName: "books",
	Query: qdrant.NewQueryNearest(
		qdrant.NewVectorInputDocument(&qdrant.Document{Model: "sentence-transformers/all-minilm-l6-v2", Text: "time travel"}),
	),
	Using: qdrant.PtrOf("description-dense"),
}

client.QueryBatch(context.Background(), &qdrant.QueryBatchPoints{
	CollectionName: "books",
	QueryPoints:    []*qdrant.QueryPoints{strict, relaxed, vectorOnly},
})
```


```http
POST /collections/books/points/query/batch
{
  "searches": [
    {
      "query": {
        "text": "time travel",
        "model": "sentence-transformers/all-minilm-l6-v2"
      },
      "using": "description-dense",
      "with_payload": true,
      "filter": {
        "must": [
          {
            "key": "title",
            "match": {
              "text": "time travel"
            }
          }
        ]
      }
    },
    {
      "query": {
        "text": "time travel",
        "model": "sentence-transformers/all-minilm-l6-v2"
      },
      "using": "description-dense",
      "with_payload": true,
      "filter": {
        "must": [
          {
            "key": "title",
            "match": {
              "text_any": "time travel"
            }
          }
        ]
      }
    },
    {
      "query": {
        "text": "time travel",
        "model": "sentence-transformers/all-minilm-l6-v2"
      },
      "using": "description-dense",
      "with_payload": true
    }
  ]
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
import java.util.*;

QdrantClient client =

QueryPoints searchStrict =
    QueryPoints.newBuilder()
        .setCollectionName("books")
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("time travel")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .setUsing("description-dense")
        .setFilter(Filter.newBuilder().addMust(matchText("title", "time travel")).build())
        .setWithPayload(enable(true))
        .build();

QueryPoints searchRelaxed =
    QueryPoints.newBuilder()
        .setCollectionName("books")
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("time travel")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .setUsing("description-dense")
        .setFilter(Filter.newBuilder().addMust(matchTextAny("title", "time travel")).build())
        .setWithPayload(enable(true))
        .build();

QueryPoints searchVectorOnly =
    QueryPoints.newBuilder()
        .setCollectionName("books")
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("time travel")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .setUsing("description-dense")
        .setWithPayload(enable(true))
        .build();

client.queryBatchAsync("books", List.of(searchStrict, searchRelaxed, searchVectorOnly)).get();
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="https://xyz-example.qdrant.io:6333",
    api_key="<your-api-key>",
    cloud_inference=True,
)

client.query_batch_points(
    collection_name="books",
    requests=[
        models.QueryRequest(
            query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
            using="description-dense",
            with_payload=True,
            filter=models.Filter(
                must=[models.FieldCondition(key="title", match=models.MatchText(text="time travel"))]
            ),
        ),
        models.QueryRequest(
            query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
            using="description-dense",
            with_payload=True,
            filter=models.Filter(
                must=[models.FieldCondition(key="title", match=models.MatchTextAny(text_any="time travel"))]
            ),
        ),
        models.QueryRequest(
            query=models.Document(text="time travel", model="sentence-transformers/all-minilm-l6-v2"),
            using="description-dense",
            with_payload=True,
        ),
    ],
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    Condition, Document, Filter, Query, QueryBatchPointsBuilder, QueryPointsBuilder,
};

let strict_filter = Filter::must([Condition::matches("title", "time travel".to_string())]);
let relaxed_filter = Filter::must([Condition::matches("title", "time travel".to_string())]);

let searches = vec![
    QueryPointsBuilder::new("books")
        .query(Query::new_nearest(Document::new(
            "time travel",
            "sentence-transformers/all-minilm-l6-v2",
        )))
        .using("description-dense")
        .filter(strict_filter)
        .with_payload(true)
        .build(),
    QueryPointsBuilder::new("books")
        .query(Query::new_nearest(Document::new(
            "time travel",
            "sentence-transformers/all-minilm-l6-v2",
        )))
        .using("description-dense")
        .filter(relaxed_filter)
        .with_payload(true)
        .build(),
    QueryPointsBuilder::new("books")
        .query(Query::new_nearest(Document::new(
            "time travel",
            "sentence-transformers/all-minilm-l6-v2",
        )))
        .using("description-dense")
        .with_payload(true)
        .build(),
];

client
    .query_batch(QueryBatchPointsBuilder::new("books", searches))
    .await?;
```


```typescript
client.queryBatch("books", {
  searches: [
    {
      query: { text: "time travel", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      with_payload: true,
      filter: {
        must: [{ key: "title", match: { text: "time travel" } }],
      },
    },
    {
      query: { text: "time travel", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      with_payload: true,
      filter: {
        must: [{ key: "title", match: { text_any: "time travel" } }],
      },
    },
    {
      query: { text: "time travel", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      with_payload: true,
    },
  ],
});
```
