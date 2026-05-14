This code snippet performs a search in a collection configured for BM25 sparse vectors using the Qdrant and FastEmbed integration. It infers a sparse BM25 vector for the query and retrieves the most relevant document (limit=1) based on the BM25 scoring. The response includes the top-matching document’s ID, score, and payload.

```python
query = "Vectors in Medicine"

client.query_points(
    collection_name="{bm25_collection_name}",
    query=models.Document(
        text=query, 
        model="Qdrant/bm25"
    ),
    using="bm25",
    limit=1,
)
```
