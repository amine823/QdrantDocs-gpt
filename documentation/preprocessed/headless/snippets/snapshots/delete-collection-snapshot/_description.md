This code snippet deletes a specific snapshot associated with a collection. The `DELETE` method is used to initiate the deletion process for the snapshot with the specified `snapshot_name` within the `collection_name`.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeleteSnapshotAsync(collectionName: "{collection_name}", snapshotName: "{snapshot_name}");
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

client.DeleteSnapshot(context.Background(), "{collection_name}", "{snapshot_name}")
```


```http
DELETE /collections/{collection_name}/snapshots/{snapshot_name}
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.deleteSnapshotAsync("{collection_name}", "{snapshot_name}").get();
```


```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.delete_snapshot(
    collection_name="{collection_name}", snapshot_name="{snapshot_name}"
)
```


```rust
use qdrant_client::qdrant::DeleteSnapshotRequestBuilder;
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .delete_snapshot(DeleteSnapshotRequestBuilder::new(
        "{collection_name}",
        "{snapshot_name}",
    ))
    .await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.deleteSnapshot("{collection_name}", "{snapshot_name}");
```
