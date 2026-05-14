This code snippet creates a collection configured for BM25-based lexical retrieval. It defines a sparse named vector with the IDF modifier enabled, ensuring that the Inverse Document Frequency, a core component of the BM25 scoring formula, is calculated on Qdrant’s side. This setup allows Qdrant to perform BM25-style retrieval based on keyword frequency and rarity.


```python
client.create_collection(
    collection_name="{bm25_collection_name}",
    sparse_vectors_config={
        "bm25": models.SparseVectorParams(
            modifier=models.Modifier.IDF
        )
    }
)
```
