This code snippet performs a search in a collection configured for miniCOIL sparse vectors using the Qdrant and FastEmbed integration. It infers a sparse miniCOIL vector for the query and retrieves the most relevant document (limit=1) based on the miniCOIL scoring. The response includes the top-matching document’s ID, score, and payload.

```python
query = "Vectors in Medicine"

client.query_points(
    collection_name="{minicoil_collection_name}",
    query=models.Document(
        text=query, 
        model="Qdrant/minicoil-v1"
    ), 
    using="minicoil",
    limit=1
)
```
