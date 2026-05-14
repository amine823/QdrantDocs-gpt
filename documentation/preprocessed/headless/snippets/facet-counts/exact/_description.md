This code snippet is a request to retrieve facet counts for a specific key within a collection. The response will contain values sorted by count in descending order and then by value in ascending order. It specifies that only values with non-zero counts will be included in the results. By setting the `exact` parameter to `true`, it ensures that the counts returned are precise instead of approximate, which is useful for debugging storage or when an exact count is needed.

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

await client.FacetAsync(
    "{collection_name}",
    key: "size",
    exact: true
);
```


```go
res, err := client.Facet(context.Background(), &qdrant.FacetCounts{
    CollectionName: "{collection_name}",
    Key:            "key",
    Exact:          qdrant.PtrOf(true),
})
```


```http
POST /collections/{collection_name}/facet
{
    "key": "size",
    "exact": true
}
```


```java
import io.qdrant.client.grpc.Points.FacetCounts;

client
      .facetAsync(
          FacetCounts.newBuilder()
              .setCollectionName("{collection_name}")
              .setKey("foo")
              .setExact(true)
              .build())
      .get();
```


```python
client.facet(
    collection_name="{collection_name}",
    key="size",
    exact=True,
)
```


```rust
use qdrant_client::qdrant::FacetCountsBuilder;

client
    .facet(
         FacetCountsBuilder::new("{collection_name}", "size")
             .limit(10)
             .exact(true),
     )
     .await?;
```


```typescript
client.facet("{collection_name}", {
    key: "size",
    exact: true,
});
```
