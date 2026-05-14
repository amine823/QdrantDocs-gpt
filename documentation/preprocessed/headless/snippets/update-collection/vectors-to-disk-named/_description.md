Update the collection by setting the vectors to be saved on disk for a specific vector named 'my_vector'. This code snippet demonstrates the configuration to ensure that the vector data is saved on disk within the collection.

```bash
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw '{
    "vectors": {
        "my_vector": { 
           "on_disk": true 
      }
    }
  }'
```


```http
PATCH /collections/{collection_name}
{
    "vectors": {
        "my_vector": {
            "on_disk": true
        }
    }
}
```
