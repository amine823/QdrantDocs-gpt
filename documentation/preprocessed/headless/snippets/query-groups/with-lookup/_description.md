This code snippet demonstrates how to use the feature for looking up information from another collection while grouping data. By utilizing the `with_lookup` parameter in the request payload, you can efficiently retrieve shared information associated with points grouped by a specific identifier. This approach helps in reducing redundancy and optimizing storage space, especially when dealing with large payloads across multiple grouped points. The `with_lookup` parameter allows you to specify what data to bring from the related points in the lookup collection, such as titles and text, providing a consolidated view of information within each group.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.SearchGroupsAsync(
    collectionName: "{collection_name}",
    vector: new float[] { 0.2f, 0.1f, 0.9f, 0.7f},
    groupBy: "document_id",
    limit: 2,
    groupSize: 2,
    withLookup: new WithLookup
    {
        Collection = "documents",
        WithPayload = new WithPayloadSelector
        {
            Include = new PayloadIncludeSelector { Fields = { new string[] { "title", "text" } } }
        },
        WithVectors = false
    }
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

client.QueryGroups(context.Background(), &qdrant.QueryPointGroups{
	CollectionName: "{collection_name}",
	Query:          qdrant.NewQuery(0.2, 0.1, 0.9, 0.7),
	GroupBy:        "document_id",
	GroupSize:      qdrant.PtrOf(uint64(2)),
	WithLookup: &qdrant.WithLookup{
		Collection:  "documents",
		WithPayload: qdrant.NewWithPayloadInclude("title", "text"),
	},
})
```


```http
POST /collections/chunks/points/query/groups
{
    // Same as in the regular query API
    "query": [1.1],

    // Grouping parameters
    "group_by": "document_id",
    "limit": 2,
    "group_size": 2,

    // Lookup parameters
    "with_lookup": {
        // Name of the collection to look up points in
        "collection": "documents",

        // Options for specifying what to bring from the payload 
        // of the looked up point, true by default
        "with_payload": ["title", "text"],

        // Options for specifying what to bring from the vector(s) 
        // of the looked up point, true by default
        "with_vectors": false
    }
}
```


```java
import static io.qdrant.client.QueryFactory.nearest;
import static io.qdrant.client.WithPayloadSelectorFactory.include;
import static io.qdrant.client.WithVectorsSelectorFactory.enable;

import io.qdrant.client.grpc.Points.QueryPointGroups;
import io.qdrant.client.grpc.Points.WithLookup;
import java.util.List;

client.queryGroupsAsync(
        QueryPointGroups.newBuilder()
                .setCollectionName("{collection_name}")
                .setQuery(nearest(0.2f, 0.1f, 0.9f, 0.7f))
                .setGroupBy("document_id")
                .setLimit(2)
                .setGroupSize(2)
                .setWithLookup(
                        WithLookup.newBuilder()
                                .setCollection("documents")
                                .setWithPayload(include(List.of("title", "text")))
                                .setWithVectors(enable(false))
                                .build())
                .build())
        .get();
```


```python
client.query_points_groups(
    collection_name="chunks",
    # Same as in the regular search() API
    query=[1.1],
    # Grouping parameters
    group_by="document_id",  # Path of the field to group by
    limit=2,  # Max amount of groups
    group_size=2,  # Max amount of points per group
    # Lookup parameters
    with_lookup=models.WithLookup(
        # Name of the collection to look up points in
        collection="documents",
        # Options for specifying what to bring from the payload
        # of the looked up point, True by default
        with_payload=["title", "text"],
        # Options for specifying what to bring from the vector(s)
        # of the looked up point, True by default
        with_vectors=False,
    ),
)
```


```rust
use qdrant_client::qdrant::{with_payload_selector::SelectorOptions, QueryPointGroupsBuilder, WithLookupBuilder};

client
    .query_groups(
        QueryPointGroupsBuilder::new("{collection_name}", "document_id")
            .query(vec![0.2, 0.1, 0.9, 0.7])
            .limit(2u64)
            .limit(2u64)
            .with_lookup(
                WithLookupBuilder::new("documents")
                    .with_payload(SelectorOptions::Include(
                        vec!["title".to_string(), "text".to_string()].into(),
                    ))
                    .with_vectors(false),
            ),
    )
    .await?;
```


```typescript
client.queryGroups("{collection_name}", {
    query: [1.1],
    group_by: "document_id",
    limit: 2,
    group_size: 2,
    with_lookup: {
        collection: "documents",
        with_payload: ["title", "text"],
        with_vectors: false,
    },
});
```
