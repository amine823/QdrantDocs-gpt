This code snippet demonstrates a way to delete specific vectors from specified points in a collection. It allows users to remove selected vectors while retaining other vectors associated with the points. The points themselves are not deleted during this process, only certain vectors are removed. This method is available starting from version 1.2.0.

```csharp
await client.DeleteVectorsAsync("{collection_name}", ["text", "image"], [0, 3, 10]);
```


```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client.DeleteVectors(context.Background(), &qdrant.DeletePointVectors{
	CollectionName: "{collection_name}",
	PointsSelector: qdrant.NewPointsSelector(
		qdrant.NewIDNum(0), qdrant.NewIDNum(3), qdrant.NewIDNum(10)),
	Vectors: &qdrant.VectorsSelector{
		Names: []string{"text", "image"},
	},
})
```


```http
POST /collections/{collection_name}/points/vectors/delete
{
    "points": [0, 3, 100],
    "vectors": ["text", "image"]
}
```


```java
import static io.qdrant.client.PointIdFactory.id;

import java.util.List;

client
    .deleteVectorsAsync(
        "{collection_name}", List.of("text", "image"), List.of(id(0), id(3), id(10)))
    .get();
```


```python
client.delete_vectors(
    collection_name="{collection_name}",
    points=[0, 3, 100],
    vectors=["text", "image"],
)
```


```rust
use qdrant_client::qdrant::{
    DeletePointVectorsBuilder, PointsIdsList,
};

client
    .delete_vectors(
        DeletePointVectorsBuilder::new("{collection_name}")
            .points_selector(PointsIdsList {
                ids: vec![0.into(), 3.into(), 10.into()],
            })
            .vectors(vec!["text".into(), "image".into()])
            .wait(true),
    )
    .await?;
```


```typescript
client.deleteVectors("{collection_name}", {
  points: [0, 3, 10],
  vector: ["text", "image"],
});
```
