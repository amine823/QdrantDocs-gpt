When recovering a snapshot, you can set a priority to determine how conflicts between snapshot data and existing data are handled. There are three priority options available:

- `replica` (default): Prioritizes existing data over snapshot data.
- `snapshot`: Prioritizes snapshot data over existing data.
- `no_sync`: Restores snapshot without additional synchronization, useful for manual shard management.

By setting the priority to `snapshot`, all data from the snapshot will be recovered onto the cluster. Using `replica` may result in an empty collection if there was no existing data in the cluster. `no_sync` is for specialized cases involving manual shard management and should be used carefully to avoid cluster issues. The priority setting is essential for controlling the outcome of snapshot recoveries.

```bash
curl -X POST 'http://qdrant-node-1:6333/collections/{collection_name}/snapshots/upload?priority=snapshot' \
    -H 'api-key: ********' \
    -H 'Content-Type:multipart/form-data' \
    -F 'snapshot=@/path/to/snapshot-2022-10-10.snapshot'
```


```http
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot",
  "priority": "snapshot"
}
```


```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://qdrant-node-2:6333")

client.recover_snapshot(
    "{collection_name}",
    "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot",
    priority=models.SnapshotPriority.SNAPSHOT,
)
```


```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.recoverSnapshot("{collection_name}", {
  location: "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot",
  priority: "snapshot"
});
```
