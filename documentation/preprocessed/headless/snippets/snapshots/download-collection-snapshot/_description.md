Retrieve a specific snapshot from a collection by its name using the available REST API. This code snippet allows downloading the snapshot as a file once it is fetched from the collection.

```bash
curl 'http://{qdrant-url}:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot' \
    -H 'api-key: ********' \
    --output 'filename.snapshot'
```


```http
GET /collections/{collection_name}/snapshots/{snapshot_name}
```


```shell
curl 'http://{qdrant-url}:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot' \
    -H 'api-key: ********' \
    --output 'filename.snapshot'
```
