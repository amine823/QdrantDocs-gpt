This code snippet allows you to create a snapshot for a specific collection. It mentions that when working with a distributed deployment, snapshots should be created for each node individually as a snapshot will only include the data from the node it was created on.

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.CreateSnapshotAsync("{collection_name}");
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

client.CreateSnapshot(context.Background(), "{collection_name}")
```


```http
POST /collections/{collection_name}/snapshots
```


```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
      new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.createSnapshotAsync("{collection_name}").get();
```


```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.create_snapshot(collection_name="{collection_name}")
```


```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_snapshot("{collection_name}").await?;
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createSnapshot("{collection_name}");
```
