Runs a hybrid search by prefetching dense and BM25 sparse queries for an ISBN and fusing results with Reciprocal Rank Fusion.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.QueryAsync(
    collectionName: "books",
    prefetch: new List<PrefetchQuery>
    {
        new()
        {
            Using = "description-dense",
            Query = new Document
            {
                Text = "9780553213515",
                Model = "sentence-transformers/all-minilm-l6-v2",
            },
            ScoreThreshold = 0.5f,
        },
        new()
        {
            Using = "isbn-bm25",
            Query = new Document { Text = "9780553213515", Model = "Qdrant/bm25" },
        },
    },
    query: Fusion.Rrf,
    payloadSelector: true,
    limit: 10
);
```


```go
client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "books",
	Prefetch: []*qdrant.PrefetchQuery{
		{
			Using: qdrant.PtrOf("description-dense"),
			Query: qdrant.NewQueryDocument(&qdrant.Document{
				Text:  "9780553213515",
				Model: "sentence-transformers/all-minilm-l6-v2",
			}),
		},
		{
			Using: qdrant.PtrOf("isbn-bm25"),
			Query: qdrant.NewQueryDocument(&qdrant.Document{
				Text:  "9780553213515",
				Model: "qdrant/bm25",
			}),
		},
	},
	Query:       qdrant.NewQueryFusion(qdrant.Fusion_RRF),
	WithPayload: qdrant.NewWithPayload(true),
	Limit:       qdrant.PtrOf(uint64(10)),
})
```


```http
POST /collections/books/points/query
{
  "prefetch": [
    {
      "query": {
        "text": "9780553213515",
        "model": "sentence-transformers/all-minilm-l6-v2"
      },
      "using": "description-dense",
      "score_threshold": 0.5
    },
    {
      "query": {
        "text": "9780553213515",
        "model": "Qdrant/bm25"
      },
      "using": "isbn-bm25"
    }
  ],
  "query": {
    "fusion": "rrf"
  },
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

PrefetchQuery densePrefetch =
    PrefetchQuery.newBuilder()
        .setUsing("description-dense")
        .setScoreThreshold(0.5f)
        .setQuery(
            nearest(
                Document.newBuilder()
                    .setText("9780553213515")
                    .setModel("sentence-transformers/all-minilm-l6-v2")
                    .build()))
        .build();

PrefetchQuery bm25Prefetch =
    PrefetchQuery.newBuilder()
        .setUsing("isbn-bm25")
        .setQuery(
            nearest(
                Document.newBuilder().setText("9780553213515").setModel("Qdrant/bm25").build()))
        .build();

client
    .queryAsync(
        QueryPoints.newBuilder()
            .setCollectionName("books")
            .addPrefetch(densePrefetch)
            .addPrefetch(bm25Prefetch)
            .setQuery(Query.newBuilder().setFusion(Fusion.RRF).build())
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
    prefetch=[
        models.Prefetch(
            query=models.Document(
                    text="9780553213515",
                    model="sentence-transformers/all-minilm-l6-v2"
            ),
            using="description-dense",
            score_threshold=0.5,
        ),
        models.Prefetch(
            query=models.Document(
                text="9780553213515", 
                model="Qdrant/bm25",
            ),
            using="isbn-bm25",
        ),
    ],
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    limit=10,
    with_payload=True,
)
```


```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{Document, Fusion, PrefetchQueryBuilder, Query, QueryPointsBuilder};

let dense_prefetch = PrefetchQueryBuilder::default()
    .query(Query::new_nearest(Document::new(
        "9780553213515",
        "sentence-transformers/all-minilm-l6-v2",
    )))
    .using("description-dense")
    .score_threshold(0.5)
    .build();

let bm25_prefetch = PrefetchQueryBuilder::default()
    .query(Query::new_nearest(Document::new(
        "9780553213515",
        "Qdrant/bm25",
    )))
    .using("isbn-bm25")
    .build();

client
    .query(
        QueryPointsBuilder::new("books")
            .add_prefetch(dense_prefetch)
            .add_prefetch(bm25_prefetch)
            .query(Query::new_fusion(Fusion::Rrf))
            .limit(10)
            .with_payload(true)
            .build(),
    )
    .await?;
```


```typescript
client.query("books", {
  prefetch: [
    {
      query: { text: "9780553213515", model: "sentence-transformers/all-minilm-l6-v2" },
      using: "description-dense",
      score_threshold: 0.5,
    },
    {
      query: { text: "9780553213515", model: "Qdrant/bm25" },
      using: "isbn-bm25",
    },
  ],
  query: { fusion: "rrf" },
  limit: 10,
  with_payload: true,
});
```
