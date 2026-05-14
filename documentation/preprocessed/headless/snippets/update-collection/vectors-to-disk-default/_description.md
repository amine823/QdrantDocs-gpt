Update the collection with patch requests to put vector data on disk. This functionality allows you to specify vector parameters, such as setting vectors to be stored on disk, for a specific collection. In cases where the collection does not have named vectors, an empty name (`""`) should be used to perform this update. This feature provided by Qdrant version 1.4 enables modifications to collection parameters, including HNSW index, quantization, and disk configurations dynamically, without the need to recreate the collection. Additionally, segments containing index and quantized data will be automatically rebuilt in the background to align with the new parameters.

```bash
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
        "": { 
            "on_disk": true 
      }
    }
  }'
```


```http
PATCH /collections/{collection_name}
{
    "vectors": {
        "": {
            "on_disk": true
        }
    }
}
```
