This code snippet demonstrates how to use the Universal Query API to prefetch results with dense and sparse vector search, and then rerank them with Reciprocal Rank Fusion. It uses Cloud Inference to create embeddings by passing document text along with the model names, instead of vectors. 

```csharp
await client.QueryAsync(
collectionName: "{collection_name}", prefetch: new List <PrefetchQuery> {
  new() {
    Query = new Document {
      Text = queryText,
      Model = bm25Model
    },
    Using = "bm25_sparse_vector",
    Limit = 5
  },
  new() {
    Query = new Document {
      Text = queryText,
      Model = denseModel
    },
    Using = "dense_vector",
    Limit = 5
  }
},
query: Fusion.Rrf,
limit: 5
);
```


```go
prefetch := []*qdrant.PrefetchQuery{
	{
		Query: qdrant.NewQueryDocument(&qdrant.Document{
			Text:  queryText,
			Model: bm25Model,
		}),
		Using: qdrant.PtrOf("bm25_sparse_vector"),
	},
	{
		Query: qdrant.NewQueryDocument(&qdrant.Document{
			Text:  queryText,
			Model: denseModel,
		}),
		Using: qdrant.PtrOf("dense_vector"),
	},
}

client.Query(context.Background(), &qdrant.QueryPoints{
	CollectionName: "{collection_name}",
	Prefetch:       prefetch,
	Query:          qdrant.NewQueryFusion(qdrant.Fusion_RRF),
})
```


```java
import static io.qdrant.client.QueryFactory.fusion;
import static io.qdrant.client.QueryFactory.nearest;

import io.qdrant.client.grpc.Points.Document;
import io.qdrant.client.grpc.Points.Fusion;
import io.qdrant.client.grpc.Points.PrefetchQuery;
import io.qdrant.client.grpc.Points.QueryPoints;

PrefetchQuery densePrefetch =
    PrefetchQuery.newBuilder()
        .setQuery(
            nearest(Document.newBuilder().setText(queryText).setModel(denseModel).build()))
        .setUsing("dense_vector")
        .build();

PrefetchQuery bm25Prefetch =
    PrefetchQuery.newBuilder()
        .setQuery(nearest(Document.newBuilder().setText(queryText).setModel(bm25Model).build()))
        .setUsing("bm25_sparse_vector")
        .build();

QueryPoints request =
    QueryPoints.newBuilder()
        .setCollectionName("{collection_name}")
        .addPrefetch(densePrefetch)
        .addPrefetch(bm25Prefetch)
        .setQuery(fusion(Fusion.RRF))
        .build();

client.queryAsync(request).get();
```


```python
results = client.query_points(
    collection_name="{collection_name}",
    prefetch=[
        models.Prefetch(
            query=models.Document(
                text=query_text,
                model=dense_model
            ),
            using="dense_vector",
            limit=5
        ),
        models.Prefetch(
            query=models.Document(
                text=query_text,
                model=bm25_model
            ),
            using="bm25_sparse_vector",
            limit=5
        )
    ],
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    limit=5,
    with_payload=True
)

print(results.points)
```


```rust
use qdrant_client::qdrant::{Document, Fusion, PrefetchQueryBuilder, Query, QueryPointsBuilder};

let dense_prefetch = PrefetchQueryBuilder::default()
    .query(Query::new_nearest(Document::new(query_text, dense_model)))
    .using("dense_vector")
    .build();

let bm25_prefetch = PrefetchQueryBuilder::default()
    .query(Query::new_nearest(Document::new(query_text, bm25_model)))
    .using("bm25_sparse_vector")
    .build();

let query_request = QueryPointsBuilder::new("{collection_name}")
    .add_prefetch(dense_prefetch)
    .add_prefetch(bm25_prefetch)
    .query(Query::new_fusion(Fusion::Rrf))
    .with_payload(true)
    .build();

let results = client.query(query_request).await?;
```


```typescript
const results = await client.query("{collection_name}", {
    prefetch: [
        {
            query: {
                text: queryText,
                model: denseModel,
            },
            using: "dense_vector",
        },
        {
            query: {
                text: queryText,
                model: bm25Model,
            },
            using: "bm25_sparse_vector",
        },
    ],
    query: {
        fusion: "rrf",
    },
});
```
