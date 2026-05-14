Recover a collection snapshot by providing a URL pointing to the location of the snapshot file. This method allows you to recover a collection snapshot from a URL or a local file stored on the node. If the specified collection does not exist, a new collection will be created upon recovery.

```http
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot"
}
```


```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://qdrant-node-2:6333")

client.recover_snapshot(
    "{collection_name}",
    "http://qdrant-node-1:6333/collections/collection_name/snapshots/snapshot-2022-10-10.snapshot",
)
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.recoverSnapshot("{collection_name}", {
  location: "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot",
});
```
