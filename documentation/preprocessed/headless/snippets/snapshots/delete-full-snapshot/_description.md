This code snippet represents functionality to delete a full storage snapshot. It allows users to send a request to delete a specific snapshot by its name. This operation can be used to manage storage snapshots efficiently.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeleteFullSnapshotAsync("{snapshot_name}");
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

client.DeleteFullSnapshot(context.Background(), "{snapshot_name}")
```


```http
DELETE /snapshots/{snapshot_name}
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.deleteFullSnapshotAsync("{snapshot_name}").get();
```


```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.delete_full_snapshot(snapshot_name="{snapshot_name}")
```


```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.delete_full_snapshot("{snapshot_name}").await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.deleteFullSnapshot("{snapshot_name}");
```
